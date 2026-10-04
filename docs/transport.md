# Transport behavior

## Timeouts and cancellation

The client timeout defaults to 60 seconds and can be overridden per call. Python uses seconds;
TypeScript uses milliseconds. Values must be finite and positive.

Python asynchronous requests and TypeScript requests enforce a total deadline across request,
response consumption, and retry delays. Streaming deadlines include time spent consuming events.
Python synchronous HTTPX requests use the remaining budget as each network-phase timeout and
check the deadline between attempts and stream lines. A synchronous blocked network operation
may finish after the overall budget; this is not a hard wall-clock deadline. Use the asynchronous
client when a strict total deadline is required.

The polling helper defaults to 120 seconds with a one-second interval. Python's `timeout` argument
sets the polling budget; `RequestOptions.timeout` limits individual polls. TypeScript's
`timeoutMs` sets the polling budget. No new job is submitted by the helper.

Cancel Python async operations by cancelling the task. Python synchronous calls accept a
`threading.Event` as `RequestOptions.cancel`: it is checked between network operations and stream
lines and interrupts retry/poll sleeps. It does not interrupt an already blocked network operation.
Use task cancellation for asynchronous calls rather than a thread event.

TypeScript calls accept an `AbortSignal`. Cancelling a call closes local transport activity; it
does not undo server-side execution or cancel a submitted job. A timed-out execution has an
unknown outcome and must not be blindly repeated.

## Retries

Retries default to zero. Set `max_retries` / `maxRetries` to enable up to ten additional attempts.
Only GET responses with status 429, 502, 503, or 504 are eligible. A valid `Retry-After` value
(seconds or HTTP date) is honored if it fits the remaining request budget; otherwise the HTTP
error is returned immediately. Without that header, exponential backoff starts at 0.5 seconds,
caps at 8 seconds, and uses jitter between half and the full delay.

POST, PUT, PATCH, DELETE, transport errors, and streaming requests are never retried. This includes
recommendation submission, execution, credential testing, and feedback. No idempotency key is
invented or sent by the SDK. HTTP 200 responses containing a business error are returned as data.

## HTTP and events

The clients send a package version in `User-Agent` and identify the SDK through
`X-HyperRoute-Surface`. Response headers remain available on ordinary responses and stream events,
including `X-HyperRoute-Caller`, the caller-profile reference returned by the server. Per-call headers may be supplied.
Custom transports must honor request cancellation and timeout arguments.

The SDK preserves JSON fields it does not recognize. Types describe the public contract; values
are not validated at runtime. Open-ended server records use `JsonObject`.

SSE parsers accept comment lines, multiline JSON data, and LF/CRLF line endings. They raise on
malformed JSON, unknown event types, server error events, premature EOF, and oversized events. The event limit is
8 MiB of decoded text, measured in language-native string units. Clients do not resume a stream.
