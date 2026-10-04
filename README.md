# HyperRoute SDK

Official Python and TypeScript/JavaScript clients for [HyperRoute](https://hyperroute.io).

Clients for tool recommendations, execution, credentials, preferences, and outcome reporting.

## Languages and frameworks

| Language / runtime | Support |
|---|---|
| Python 3.11+ | Synchronous and asynchronous clients |
| TypeScript / JavaScript on Node.js 22+ | Typed asynchronous client; ES modules |
| Other languages | HTTP API and [OpenAPI contract](contract/openapi.json); no dedicated package yet |

The clients are framework-independent. Use the Python client from Python applications and agent
workflows, or the TypeScript client from Node.js services and server-side application code.
There are no dedicated LangChain, LangGraph, FastAPI, Express, or Next.js adapters in this release.
Framework compatibility comes from calling the ordinary client methods. Browser clients, Deno,
Bun, Go, Rust, Java, C#, and C++ are not currently tested or supported packages.

For MCP-compatible agents, use [hyperroute-mcp](https://github.com/HyperRouteAI/hyperroute-mcp).
The SDK provides direct programmatic access; the MCP package exposes tools to an MCP client.

## Install

Version 0.1.0 is unreleased. Registry installation commands apply after publication:

```sh
pip install hyperroute-sdk
```

```sh
npm install @hyperroute/sdk
```

To install from source:

```sh
pip install ./python
npm install ./typescript
```

Build the TypeScript package first with `cd typescript && npm ci && npm run build`.

## Python

```python
from hyperroute import HyperRoute

with HyperRoute() as client:
    response = client.recommend({
        "query": "Find recent research on battery recycling",
        "detail": "full",
        "evidence_k": 3,
    })
    recommendation = response.data
    if recommendation["best"] is not None:
        best = recommendation["best"]
        print(best["tool_id"], best["capability"], best["band"], best["rank"])
        if best["evidence"] is not None:
            for probe in best["evidence"]["probes"]:
                print(probe["task_text"], probe["score"])
```

```python
import asyncio
from hyperroute import AsyncHyperRoute

async def main():
    async with AsyncHyperRoute() as client:
        response = await client.recommend({"query": "Find recent research on battery recycling"})
        print(response.data)

asyncio.run(main())
```

## TypeScript / JavaScript

```typescript
import { HyperRoute } from '@hyperroute/sdk';

const client = new HyperRoute();
const response = await client.recommend({
  query: 'Find recent research on battery recycling',
  detail: 'full',
  evidence_k: 3,
});
const best = response.data.best;
if (best) {
  console.log(best.tool_id, best.capability, best.band, best.rank);
  for (const probe of best.evidence?.probes ?? []) {
    console.log(probe.task_text, probe.score);
  }
}
```

`detail: "full"` selects a `FullRecommendation` return type. Responses are structured dictionaries
in Python and typed objects in TypeScript. [Data types](docs/types.md) document every named schema;
[recommendations](docs/recommendations.md) explains score meanings and field availability.

The default endpoint is `https://hyperroute.io`. Set `HYPERROUTE_API_KEY` to a HyperRoute personal
access token for authenticated operations. Public recommendations do not require a token.
Tool credentials are connected separately using `onboard`; they are not the SDK authentication token.
You can also pass `api_key` in Python or `apiKey` in TypeScript explicitly.

## Recommend, execute, report

Recommendation and execution are separate calls. Inspect the recommendation before selecting a
tool: it may request additional preferences, suggest your own tools, or require a connection.
Execution may return HTTP 200 with `ok: false`; check that field before using the result.

See [Python examples](examples/python), [TypeScript examples](examples/typescript), and the
[usage guide](docs/usage.md) for execution, feedback, polling, streaming, and error handling.

## Client behavior

- Responses include the parsed `data`, HTTP status, and response headers.
- Default timeout: 60 seconds. Polling helpers default to 120 seconds, checking once per second.
- Automatic retries are off by default. Optional bounded retries apply only to GET responses with
  status 429, 502, 503, or 504, respecting `Retry-After` within the request budget.
- POST, PUT, PATCH, DELETE, network failures, and streams are never automatically retried.
- Clients never automatically execute a recommendation or replay an uncertain execution.
- Python async calls support task cancellation; TypeScript accepts `AbortSignal`.
- JSON responses preserve additional fields. The clients do not perform runtime schema validation.

See [transport behavior](docs/transport.md) for timeout and cancellation details.

## Documentation

- [Usage and configuration](docs/usage.md)
- [Recommendation scores and probe evidence](docs/recommendations.md)
- [Typed request and response fields](docs/types.md)
- [API reference](docs/api.md)
- [Transport behavior](docs/transport.md)
- [Compatibility and releases](docs/releases.md)
- [Contributing](CONTRIBUTING.md)
- [Changelog](CHANGELOG.md)

## License

[MIT](LICENSE).
