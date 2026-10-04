import type { Recommendation, RecommendRequest, RecommendationSubmission } from './types.js';

export interface ApiResponse<T> { data: T; statusCode: number; headers: Headers }
export interface RequestOptions { timeoutMs?: number; signal?: AbortSignal; headers?: HeadersInit }
export interface ClientOptions { apiKey?: string; baseUrl?: string; timeoutMs?: number; maxRetries?: number; fetch?: typeof globalThis.fetch }
export type StreamEvent =
  | { event: 'queued' | 'running'; data: RecommendationSubmission; headers: Headers }
  | { event: 'result'; data: Recommendation; headers: Headers };
export class HyperRouteError extends Error {}
export class ApiError extends HyperRouteError {
  constructor(public statusCode: number, public body: unknown, public headers: Headers) {
    super(`HyperRoute HTTP ${statusCode}`);
  }
}
export class TransportError extends HyperRouteError {}
export class RequestTimeout extends TransportError {}
export class CancelledError extends TransportError {}
export class ProtocolError extends HyperRouteError {}
export class JobError extends HyperRouteError {
  constructor(public body: unknown) { super('HyperRoute job failed'); }
}

function positive(value: number, name: string): number {
  if (!Number.isFinite(value) || value <= 0) throw new RangeError(`${name} must be finite and positive`);
  return value;
}

function delayMs(value: string | null, attempt: number): number {
  if (value) {
    const numeric = Number(value);
    const delay = Number.isFinite(numeric) ? numeric * 1000 : Date.parse(value) - Date.now();
    if (Number.isFinite(delay) && delay >= 0) return delay;
  }
  return Math.min(500 * 2 ** attempt, 8000) * (0.5 + Math.random() / 2);
}

function sleep(ms: number, signal: AbortSignal): Promise<void> {
  signal.throwIfAborted();
  return new Promise((resolve, reject) => {
    const abort = () => { clearTimeout(timer); signal.removeEventListener('abort', abort); reject(signal.reason); };
    const timer = setTimeout(() => { signal.removeEventListener('abort', abort); resolve(); }, ms);
    signal.addEventListener('abort', abort, { once: true });
  });
}

async function apiError(response: Response): Promise<ApiError> {
  const text = await response.text();
  let body: unknown = text;
  try { body = JSON.parse(text); } catch {}
  return new ApiError(response.status, body, response.headers);
}

export class Transport {
  private readonly baseUrl: string;
  private readonly apiKey?: string;
  private readonly timeoutMs: number;
  private readonly maxRetries: number;
  private readonly fetcher: typeof globalThis.fetch;

  constructor(options: ClientOptions = {}) {
    const env = typeof process !== 'undefined' ? process.env : {};
    this.baseUrl = (options.baseUrl ?? env.HYPERROUTE_BASE_URL ?? 'https://hyperroute.io').replace(/\/+$/, '');
    const url = new URL(this.baseUrl);
    if (!['https:', 'http:'].includes(url.protocol) || url.username || url.password || url.search || url.hash) throw new TypeError('Invalid base URL');
    if (url.protocol === 'http:' && !['localhost', '127.0.0.1', '[::1]'].includes(url.hostname)) throw new TypeError('Remote endpoints require HTTPS');
    this.apiKey = options.apiKey ?? env.HYPERROUTE_API_KEY;
    this.timeoutMs = positive(options.timeoutMs ?? 60000, 'timeoutMs');
    this.maxRetries = options.maxRetries ?? 0;
    if (!Number.isInteger(this.maxRetries) || this.maxRetries < 0 || this.maxRetries > 10) throw new RangeError('maxRetries must be an integer from 0 to 10');
    this.fetcher = options.fetch ?? globalThis.fetch;
  }

  private headers(options: RequestOptions, body: unknown): Headers {
    const headers = new Headers({ accept: 'application/json', 'user-agent': 'hyperroute-typescript/0.1.0', 'x-hyperroute-surface': 'sdk-typescript' });
    if (this.apiKey) headers.set('authorization', `Bearer ${this.apiKey}`);
    if (body !== undefined) headers.set('content-type', 'application/json');
    new Headers(options.headers).forEach((value, key) => headers.set(key, value));
    return headers;
  }

  private translate(error: unknown, options: RequestOptions, deadline: AbortSignal): never {
    if (options.signal?.aborted) throw new CancelledError('Request cancelled', { cause: error });
    if (deadline.aborted) throw new RequestTimeout('Request deadline exceeded', { cause: error });
    if (error instanceof HyperRouteError) throw error;
    throw new TransportError('HTTP transport failed', { cause: error });
  }

  protected async request<T>(method: string, path: string, body?: unknown, query?: object, mode = 'json', options: RequestOptions = {}): Promise<ApiResponse<T>> {
    const budget = positive(options.timeoutMs ?? this.timeoutMs, 'timeoutMs');
    const deadline = AbortSignal.timeout(budget);
    const end = Date.now() + budget;
    const signal = options.signal ? AbortSignal.any([options.signal, deadline]) : deadline;
    const url = new URL(this.baseUrl + path);
    for (const [key, value] of Object.entries(query ?? {})) if (value != null) url.searchParams.set(key, String(value));
    try {
      for (let attempt = 0; attempt <= this.maxRetries; attempt++) {
        signal.throwIfAborted();
        const response = await this.fetcher(url, { method, headers: this.headers(options, body), body: body === undefined ? undefined : JSON.stringify(body), signal, redirect: 'manual' });
        if (method === 'GET' && [429, 502, 503, 504].includes(response.status) && attempt < this.maxRetries) {
          const delay = delayMs(response.headers.get('retry-after'), attempt);
          if (delay >= end - Date.now()) throw await apiError(response);
          await response.body?.cancel();
          await sleep(delay, signal);
          continue;
        }
        if (!response.ok) throw await apiError(response);
        let data: unknown;
        if (mode === 'bytes') data = new Uint8Array(await response.arrayBuffer());
        else if (response.status === 204) data = null;
        else if (mode === 'auto' && !response.headers.get('content-type')?.includes('json')) data = await response.text();
        else {
          const text = await response.text();
          try { data = JSON.parse(text); } catch { throw new ProtocolError('Expected a JSON response'); }
        }
        signal.throwIfAborted();
        return { data: data as T, statusCode: response.status, headers: response.headers };
      }
      throw new ProtocolError('Retry loop exhausted');
    } catch (error) { this.translate(error, options, deadline); }
  }

  async waitForRecommendation(jobId: string, options: RequestOptions & { pollIntervalMs?: number } = {}): Promise<ApiResponse<Recommendation>> {
    const budget = positive(options.timeoutMs ?? 120000, 'timeoutMs');
    const interval = positive(options.pollIntervalMs ?? 1000, 'pollIntervalMs');
    const deadline = AbortSignal.timeout(budget);
    const end = Date.now() + budget;
    const signal = options.signal ? AbortSignal.any([options.signal, deadline]) : deadline;
    try {
      while (true) {
        signal.throwIfAborted();
        const response = await this.request<Record<string, unknown>>('GET', '/recommend/status/' + encodeURIComponent(jobId), undefined, undefined, 'json', { ...options, signal, timeoutMs: Math.max(1, end-Date.now()) });
        const state = response.data.state;
        if (state === 'done') {
          if (!response.data.result || typeof response.data.result !== 'object') throw new ProtocolError('Completed job has no result');
          return { ...response, data: response.data.result as Recommendation };
        }
        if (state === 'error') throw new JobError(response.data);
        if (state !== 'queued' && state !== 'running') throw new ProtocolError('Unknown job state');
        await sleep(interval, signal);
      }
    } catch (error) { this.translate(error, options, deadline); }
  }

  async *streamRecommendation(body: RecommendRequest, options: RequestOptions = {}): AsyncGenerator<StreamEvent> {
    if (body.format === 'text') throw new TypeError('Streaming requires JSON format');
    const deadline = AbortSignal.timeout(positive(options.timeoutMs ?? this.timeoutMs, 'timeoutMs'));
    const signal = options.signal ? AbortSignal.any([options.signal, deadline]) : deadline;
    const headers = this.headers(options, body);
    headers.set('accept', 'text/event-stream');
    let reader: ReadableStreamDefaultReader<Uint8Array> | undefined;
    try {
      signal.throwIfAborted();
      const response = await this.fetcher(this.baseUrl+'/recommend', { method: 'POST', headers, body: JSON.stringify(body), signal, redirect: 'manual' });
      if (!response.ok) throw await apiError(response);
      if (!response.headers.get('content-type')?.includes('text/event-stream') || !response.body) throw new ProtocolError('Expected an event stream');
      reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = '';
      let event = 'message';
      let data: string[] = [];
      let size = 0;
      while (true) {
        signal.throwIfAborted();
        const next = await reader.read();
        buffer += decoder.decode(next.value, { stream: !next.done });
        if (buffer.length > 8 * 1024 * 1024) throw new ProtocolError('Stream buffer exceeds 8 MiB');
        let match: RegExpExecArray | null;
        while ((match = /\r\n|\r(?!$)|\n/.exec(buffer))) {
          const line = buffer.slice(0, match.index);
          buffer = buffer.slice(match.index + match[0].length);
          if (!line) {
            if (data.length) {
              let value: unknown;
              try { value = JSON.parse(data.join('\n')); } catch { throw new ProtocolError('Invalid JSON in stream event'); }
              if (event === 'error') throw new JobError(value);
              if (event === 'result') {
                yield { event, data: value as Recommendation, headers: response.headers };
                return;
              }
              if (event === 'queued' || event === 'running') yield { event, data: value as RecommendationSubmission, headers: response.headers };
              else throw new ProtocolError('Unknown stream event');
            }
            event = 'message'; data = []; size = 0;
          } else if (!line.startsWith(':')) {
            const colon = line.indexOf(':');
            const key = colon < 0 ? line : line.slice(0, colon);
            const value = colon < 0 ? '' : line.slice(colon+1).replace(/^ /, '');
            size += line.length;
            if (size > 8*1024*1024) throw new ProtocolError('Stream event exceeds 8 MiB');
            if (key === 'event') event = value;
            if (key === 'data') data.push(value);
          }
        }
        if (next.done) throw new ProtocolError('Stream ended before a result');
      }
    } catch (error) { this.translate(error, options, deadline); }
    finally { if (reader) { try { await reader.cancel(); } finally { reader.releaseLock(); } } }
  }
}
