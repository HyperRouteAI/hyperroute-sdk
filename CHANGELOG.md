# Changelog

## 0.1.0 — Unreleased

- Waitlist updates now require the original submission cookie; email-only updates return HTTP 403.
  Python sync/async clients retain cookies within a client. Node callers forward the returned
  session cookie via request headers. This is a breaking server validation change documented
  before the first SDK release; package versions remain at unreleased 0.1.0.

- Python synchronous and asynchronous clients.
- TypeScript and JavaScript client for Node.js.
- Recommendation, execution, feedback, account, credentials, preferences, and tool-management APIs.
- Recommendation polling and server-sent events.
- Typed requests, response metadata, structured errors, configurable timeouts, and optional GET retries.
- OpenAPI contract, examples, package checks, and release workflows.
