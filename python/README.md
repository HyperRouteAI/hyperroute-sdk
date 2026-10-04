# HyperRoute Python SDK

Python client for [HyperRoute](https://hyperroute.io), with synchronous and asynchronous APIs.
Requires Python 3.11 or newer.

## Installation

Version 0.1.0 is unreleased. After publication:

```sh
pip install hyperroute-sdk
```

From the repository root:

```sh
pip install ./python
```

## Usage

```python
from hyperroute import HyperRoute

with HyperRoute() as client:
    recommendation = client.recommend({
        "query": "Find recent research on battery recycling",
        "detail": "full",
        "evidence_k": 3,
    }).data
    best = recommendation["best"]
    if best is not None:
        print(best["tool_id"], best["capability"], best["band"], best["rank"])
        if best["evidence"] is not None:
            for probe in best["evidence"]["probes"]:
                print(probe["task_text"], probe["score"])
```

Responses are ordinary dictionaries with `TypedDict` definitions in `hyperroute.types`.
`detail: "full"` selects the `FullRecommendation` return type. Compact and lean projections have
separate types. Scores, facets, probe evidence, and judge panels have explicit field definitions.

Every method returns an `ApiResponse` with `data`, `status_code`, and `headers`.

## Asynchronous usage

```python
import asyncio
from hyperroute import AsyncHyperRoute

async def main():
    async with AsyncHyperRoute() as client:
        response = await client.recommend({"query": "Find recent research on battery recycling"})
        print(response.data)

asyncio.run(main())
```

## Configuration

The default endpoint is `https://hyperroute.io`. Set `HYPERROUTE_API_KEY` to a personal access token
for authenticated operations. Public recommendations do not require a token. Tool credentials are
connected separately using `onboard`.

Constructor options include `api_key`, `base_url`, `timeout` in seconds, and `max_retries`.
Use `RequestOptions` for per-call timeouts and headers.

The default timeout is 60 seconds. Automatic retries are disabled; enabling them permits bounded
retries of eligible GET responses only. Execution and other mutations are never automatically retried.
Async calls support task cancellation. The synchronous client checks cancellation between network
operations; see the transport reference for deadline behavior.

## Documentation

- [Python examples](https://github.com/HyperRouteAI/hyperroute-sdk/tree/main/examples/python)
- [Usage guide](https://github.com/HyperRouteAI/hyperroute-sdk/blob/main/docs/usage.md)
- [API reference](https://github.com/HyperRouteAI/hyperroute-sdk/blob/main/docs/api.md)
- [Response types](https://github.com/HyperRouteAI/hyperroute-sdk/blob/main/docs/types.md)
- [Scores and probe evidence](https://github.com/HyperRouteAI/hyperroute-sdk/blob/main/docs/recommendations.md)
- [Transport behavior](https://github.com/HyperRouteAI/hyperroute-sdk/blob/main/docs/transport.md)
- [Changelog](https://github.com/HyperRouteAI/hyperroute-sdk/blob/main/CHANGELOG.md)

## License

[MIT](LICENSE).
