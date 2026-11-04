# Changelog

## 0.1.0 — Unreleased

- Python synchronous and asynchronous clients.
- TypeScript and JavaScript client for Node.js.
- Recommendation, execution, feedback, account, credentials, preferences, and tool-management APIs.
- Recommendation polling and server-sent events.
- `instruction` on recommendations that point to your own agent: the evaluated prompt, search budget, tools, and alternative configurations.
- `run`: several lookups in one call, each routed on its own and acted on; fallback to the next ready tool when the best fails; reports owed from earlier runs carried in the same call, and a `useless` or `blocked` report reopens the item; a report may carry `satisfied`, the user's own thumbs up or down. `run` is limited per account by items routed (HTTP 429 with `Retry-After`). `ranking` returns the stored ranking behind a run item.
- `adapted_query` on execution responses may be null when the tool takes the query as given.
- `connect_mode`, `connect_note` and `fields` on `OnboardInfo`. `onboard` takes `values` for a tool that needs several values, and answers 409 for one that connects by OAuth or runs where HyperRoute cannot use them.
- Typed requests, response metadata, structured errors, configurable timeouts, and optional GET retries.
- OpenAPI contract, examples, package checks, and release workflows.
