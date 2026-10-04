# HyperRoute TypeScript SDK

TypeScript and JavaScript client for [HyperRoute](https://hyperroute.io).
Requires Node.js 22 or newer and uses ES modules.

## Installation

Version 0.1.0 is unreleased. After publication:

```sh
npm install @hyperroute/sdk
```

From the repository root, build and install locally:

```sh
npm --prefix typescript ci
npm --prefix typescript run build
npm install ./typescript
```

## Usage

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

The package exports request and response types. `detail: 'full'` selects the `FullRecommendation`
return type. Compact and lean projections have separate types. Scores, facets, probe evidence,
and judge panels have explicit field definitions. JavaScript uses the same methods.

Every method returns a promise of `ApiResponse` with `data`, `statusCode`, and `headers`.

## Configuration

The default endpoint is `https://hyperroute.io`. Set `HYPERROUTE_API_KEY` to a personal access token
for authenticated operations. Public recommendations do not require a token. Tool credentials are
connected separately using `onboard`.

Constructor options include `apiKey`, `baseUrl`, `timeoutMs`, `maxRetries`, and a custom `fetch`.
Methods accept a final options object with
`timeoutMs`, `signal`, and `headers`.

The default timeout is 60 seconds. Automatic retries are disabled; enabling them permits bounded
retries of eligible GET responses only. Execution and other mutations are never automatically retried.
Use an `AbortSignal` to cancel a request. Browser use is not currently supported.

## Documentation

- [Examples](https://github.com/HyperRouteAI/hyperroute-sdk/tree/main/examples/typescript)
- [Usage guide](https://github.com/HyperRouteAI/hyperroute-sdk/blob/main/docs/usage.md)
- [API reference](https://github.com/HyperRouteAI/hyperroute-sdk/blob/main/docs/api.md)
- [Response types](https://github.com/HyperRouteAI/hyperroute-sdk/blob/main/docs/types.md)
- [Scores and probe evidence](https://github.com/HyperRouteAI/hyperroute-sdk/blob/main/docs/recommendations.md)
- [Transport behavior](https://github.com/HyperRouteAI/hyperroute-sdk/blob/main/docs/transport.md)
- [Changelog](https://github.com/HyperRouteAI/hyperroute-sdk/blob/main/CHANGELOG.md)

## License

[MIT](LICENSE).
