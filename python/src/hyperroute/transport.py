from __future__ import annotations

import asyncio
import json
import math
import os
import random
import threading
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from typing import Any, Generic, Iterator, AsyncIterator, TypeVar, Self, cast, Literal
from urllib.parse import quote, urlsplit
from .types import Recommendation, RecommendRequest, RecommendationSubmission

import httpx

T = TypeVar('T', covariant=True)


@dataclass(frozen=True)
class ApiResponse(Generic[T]):
    data: T
    status_code: int
    headers: httpx.Headers


@dataclass
class RequestOptions:
    timeout: float | None = None
    headers: dict[str, str] = field(default_factory=dict)
    cancel: threading.Event | None = None


@dataclass(frozen=True)
class QueueEvent:
    event: Literal["queued", "running"]
    data: RecommendationSubmission
    headers: httpx.Headers


@dataclass(frozen=True)
class ResultEvent:
    event: Literal["result"]
    data: Recommendation
    headers: httpx.Headers


StreamEvent = QueueEvent | ResultEvent


class HyperRouteError(Exception):
    pass


class ApiError(HyperRouteError):
    def __init__(self, status_code: int, body: Any, headers: httpx.Headers):
        super().__init__(f'HyperRoute HTTP {status_code}')
        self.status_code = status_code
        self.body = body
        self.headers = headers


class TransportError(HyperRouteError):
    pass


class RequestTimeout(TransportError):
    pass


class CancelledError(TransportError):
    pass


class ProtocolError(HyperRouteError):
    pass


class JobError(HyperRouteError):
    def __init__(self, body: Any):
        super().__init__('HyperRoute job failed')
        self.body = body


def _positive(value: float, name: str) -> float:
    if not math.isfinite(value) or value <= 0:
        raise ValueError(f'{name} must be finite and positive')
    return value


def _check(options: RequestOptions) -> None:
    if options.cancel is not None and options.cancel.is_set():
        raise CancelledError('Request cancelled')


def _delay(value: str | None, attempt: int) -> float:
    if value:
        try:
            seconds = float(value)
        except ValueError:
            try:
                seconds = (parsedate_to_datetime(value) - datetime.now(timezone.utc)).total_seconds()
            except (ValueError, TypeError, OverflowError):
                seconds = -1
        if math.isfinite(seconds) and seconds >= 0:
            return seconds
    return min(0.5 * 2 ** attempt, 8) * (0.5 + random.random() / 2)


def _decode(response: httpx.Response, mode: str) -> Any:
    if mode == 'bytes':
        return response.content
    if response.status_code == 204:
        return None
    if mode == 'auto' and 'json' not in response.headers.get('content-type', ''):
        return response.text
    try:
        return response.json()
    except ValueError as e:
        raise ProtocolError('Expected a JSON response') from e


def _error(response: httpx.Response) -> ApiError:
    try:
        body = response.json()
    except ValueError:
        body = response.text
    return ApiError(response.status_code, body, response.headers)


class _Base:
    def __init__(self, api_key: str | None = None, *, base_url: str | None = None, timeout: float = 60, max_retries: int = 0):
        self.base_url = (base_url or os.getenv('HYPERROUTE_BASE_URL') or 'https://hyperroute.io').rstrip('/')
        url = urlsplit(self.base_url)
        if url.scheme not in {'https', 'http'} or not url.netloc or url.username or url.password or url.query or url.fragment:
            raise ValueError('base_url must be an HTTP(S) URL without credentials, query, or fragment')
        if url.scheme == 'http' and url.hostname not in {'localhost', '127.0.0.1', '::1'}:
            raise ValueError('Remote endpoints require HTTPS')
        if isinstance(max_retries, bool) or not isinstance(max_retries, int) or not 0 <= max_retries <= 10:
            raise ValueError('max_retries must be an integer from 0 to 10')
        self.timeout = _positive(timeout, 'timeout')
        self.max_retries = max_retries
        self.api_key = api_key if api_key is not None else os.getenv('HYPERROUTE_API_KEY')

    def _headers(self, options: RequestOptions) -> dict[str, str]:
        headers = httpx.Headers({'accept': 'application/json', 'user-agent': 'hyperroute-python/0.1.0', 'x-hyperroute-surface': 'sdk-python'})
        if self.api_key:
            headers['authorization'] = 'Bearer ' + self.api_key
        headers.update(options.headers)
        return dict(headers)

    def _budget(self, options: RequestOptions) -> float:
        _check(options)
        return _positive(options.timeout if options.timeout is not None else self.timeout, 'timeout')


class SyncTransport(_Base):
    def __init__(self, *args: Any, http_client: httpx.Client | None = None, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self._owned = http_client is None
        self._http = http_client or httpx.Client()

    def close(self) -> None:
        if self._owned:
            self._http.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(self, *args):
        self.close()

    def _sleep(self, delay: float, options: RequestOptions) -> None:
        if options.cancel is not None:
            if options.cancel.wait(delay):
                raise CancelledError('Request cancelled')
        else:
            time.sleep(delay)

    def _request(self, method: str, path: str, *, body=None, query=None, mode='json', options=None) -> ApiResponse[Any]:
        options = options or RequestOptions()
        deadline = time.monotonic() + self._budget(options)
        for attempt in range(self.max_retries + 1):
            _check(options)
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise RequestTimeout('Request deadline exceeded')
            try:
                response = self._http.request(method, self.base_url + path, json=body, params={k:v for k,v in (query or {}).items() if v is not None}, headers=self._headers(options), timeout=remaining, follow_redirects=False)
            except httpx.TimeoutException as e:
                raise RequestTimeout('Request timed out') from e
            except httpx.HTTPError as e:
                raise TransportError('HTTP transport failed') from e
            _check(options)
            if time.monotonic() >= deadline:
                raise RequestTimeout('Request deadline exceeded')
            if method == 'GET' and response.status_code in {429, 502, 503, 504} and attempt < self.max_retries:
                delay = _delay(response.headers.get('retry-after'), attempt)
                if delay >= deadline - time.monotonic():
                    raise _error(response)
                self._sleep(delay, options)
                continue
            if not 200 <= response.status_code < 300:
                raise _error(response)
            return ApiResponse(_decode(response, mode), response.status_code, response.headers)
        raise ProtocolError('Retry loop exhausted')

    def wait_for_recommendation(self, job_id: str, *, timeout: float = 120, poll_interval: float = 1, options: RequestOptions | None = None) -> ApiResponse[Recommendation]:
        options = options or RequestOptions()
        deadline = time.monotonic() + _positive(timeout, 'timeout')
        _positive(poll_interval, 'poll_interval')
        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise RequestTimeout('Polling deadline exceeded')
            result = self._request('GET', '/recommend/status/' + quote(job_id, safe=''), options=RequestOptions(min(remaining, options.timeout or self.timeout), options.headers, options.cancel))
            state = result.data.get('state')
            if state == 'done':
                if 'result' not in result.data:
                    raise ProtocolError('Completed job has no result')
                return ApiResponse(result.data['result'], result.status_code, result.headers)
            if state == 'error':
                raise JobError(result.data)
            if state not in {'queued', 'running'}:
                raise ProtocolError('Unknown job state')
            self._sleep(min(poll_interval, max(0, deadline-time.monotonic())), options)

    def stream_recommendation(self, body: RecommendRequest, *, options: RequestOptions | None = None) -> Iterator[StreamEvent]:
        options = options or RequestOptions()
        if body.get('format') == 'text':
            raise ValueError('Streaming requires JSON format')
        deadline = time.monotonic() + self._budget(options)
        headers = self._headers(options)
        headers['accept'] = 'text/event-stream'
        parser = _SSE()
        try:
            with self._http.stream('POST', self.base_url+'/recommend', json=body, headers=headers, timeout=deadline-time.monotonic(), follow_redirects=False) as response:
                if not 200 <= response.status_code < 300:
                    response.read()
                    raise _error(response)
                if 'text/event-stream' not in response.headers.get('content-type',''):
                    raise ProtocolError('Expected an event stream')
                for line in response.iter_lines():
                    _check(options)
                    if time.monotonic() >= deadline:
                        raise RequestTimeout('Stream deadline exceeded')
                    event = parser.line(line, response.headers)
                    if event:
                        yield event
                        if event.event == 'result':
                            return
                raise ProtocolError('Stream ended before a result')
        except httpx.TimeoutException as e:
            raise RequestTimeout('Stream timed out') from e
        except httpx.HTTPError as e:
            raise TransportError('Stream transport failed') from e


class AsyncTransport(_Base):
    def __init__(self, *args: Any, http_client: httpx.AsyncClient | None = None, **kwargs: Any):
        super().__init__(*args, **kwargs)
        self._owned = http_client is None
        self._http = http_client or httpx.AsyncClient()

    async def aclose(self) -> None:
        if self._owned:
            await self._http.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(self, *args):
        await self.aclose()

    async def _request(self, method: str, path: str, *, body=None, query=None, mode='json', options=None) -> ApiResponse[Any]:
        options = options or RequestOptions()
        budget = self._budget(options)
        deadline = time.monotonic() + budget
        try:
            async with asyncio.timeout(budget):
                for attempt in range(self.max_retries + 1):
                    _check(options)
                    response = await self._http.request(method, self.base_url+path, json=body, params={k:v for k,v in (query or {}).items() if v is not None}, headers=self._headers(options), timeout=max(0.001,deadline-time.monotonic()), follow_redirects=False)
                    _check(options)
                    if method == 'GET' and response.status_code in {429,502,503,504} and attempt < self.max_retries:
                        delay = _delay(response.headers.get('retry-after'),attempt)
                        if delay >= deadline-time.monotonic():
                            raise _error(response)
                        await asyncio.sleep(delay)
                        continue
                    if not 200 <= response.status_code < 300:
                        raise _error(response)
                    return ApiResponse(_decode(response,mode),response.status_code,response.headers)
        except (TimeoutError,httpx.TimeoutException) as e:
            raise RequestTimeout('Request timed out') from e
        except httpx.HTTPError as e:
            raise TransportError('HTTP transport failed') from e
        raise ProtocolError('Retry loop exhausted')

    async def wait_for_recommendation(self, job_id: str, *, timeout: float = 120, poll_interval: float = 1, options: RequestOptions | None = None) -> ApiResponse[Recommendation]:
        _positive(timeout,'timeout')
        _positive(poll_interval,'poll_interval')
        options = options or RequestOptions()
        try:
            async with asyncio.timeout(timeout):
                while True:
                    response = await self._request('GET','/recommend/status/'+quote(job_id,safe=''),options=options)
                    state = response.data.get('state')
                    if state == 'done':
                        if 'result' not in response.data:
                            raise ProtocolError('Completed job has no result')
                        return ApiResponse(response.data['result'],response.status_code,response.headers)
                    if state == 'error':
                        raise JobError(response.data)
                    if state not in {'queued','running'}:
                        raise ProtocolError('Unknown job state')
                    await asyncio.sleep(poll_interval)
        except TimeoutError as e:
            raise RequestTimeout('Polling deadline exceeded') from e

    async def stream_recommendation(self, body: RecommendRequest, *, options: RequestOptions | None = None) -> AsyncIterator[StreamEvent]:
        options = options or RequestOptions()
        if body.get('format') == 'text':
            raise ValueError('Streaming requires JSON format')
        budget = self._budget(options)
        headers = self._headers(options)
        headers['accept'] = 'text/event-stream'
        parser = _SSE()
        try:
            async with asyncio.timeout(budget):
                async with self._http.stream('POST',self.base_url+'/recommend',json=body,headers=headers,timeout=budget,follow_redirects=False) as response:
                    if not 200 <= response.status_code < 300:
                        await response.aread()
                        raise _error(response)
                    if 'text/event-stream' not in response.headers.get('content-type',''):
                        raise ProtocolError('Expected an event stream')
                    async for line in response.aiter_lines():
                        _check(options)
                        event = parser.line(line,response.headers)
                        if event:
                            yield event
                            if event.event == 'result':
                                return
                    raise ProtocolError('Stream ended before a result')
        except (TimeoutError,httpx.TimeoutException) as e:
            raise RequestTimeout('Stream timed out') from e
        except httpx.HTTPError as e:
            raise TransportError('Stream transport failed') from e


class _SSE:
    def __init__(self):
        self.event = 'message'
        self.data: list[str] = []
        self.size = 0

    def line(self, line: str, headers: httpx.Headers) -> StreamEvent | None:
        if not line:
            event, data = self.event, self.data
            self.event, self.data, self.size = 'message', [], 0
            if not data:
                return None
            try:
                value = json.loads('\n'.join(data))
            except ValueError as e:
                raise ProtocolError('Invalid JSON in stream event') from e
            if event == 'error':
                raise JobError(value)
            if event == "result":
                return ResultEvent("result", value, headers)
            if event in {"queued", "running"}:
                return QueueEvent(cast(Literal["queued", "running"], event), value, headers)
            raise ProtocolError("Unknown stream event")
        if line.startswith(':'):
            return None
        name, _, value = line.partition(':')
        if value.startswith(' '):
            value = value[1:]
        self.size += len(line)
        if self.size > 8 * 1024 * 1024:
            raise ProtocolError('Stream event exceeds 8 MiB')
        if name == 'event':
            self.event = value
        elif name == 'data':
            self.data.append(value)
        return None
