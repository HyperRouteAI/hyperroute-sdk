# Usage

## Configuration

| Setting | Python | TypeScript | Default |
|---|---|---|---|
| Token | `api_key` | `apiKey` | `HYPERROUTE_API_KEY` |
| Endpoint | `base_url` | `baseUrl` | `https://hyperroute.io` |
| Timeout | `timeout` (seconds) | `timeoutMs` | 60 seconds |
| GET retries | `max_retries` | `maxRetries` | 0; permitted range 0–10 |
| Custom HTTP transport | `http_client` | `fetch` | HTTPX / native fetch |

Use HTTPS for remote endpoints. HTTP is accepted for loopback development. Redirects are not
followed. Close Python clients with a context manager or `close()` / `aclose()`; an injected HTTPX
client remains owned by the application.

## Preferences

```python
from hyperroute import HyperRoute

with HyperRoute() as client:
    response = client.recommend({
        "query": "Find recent research on battery recycling",
        "facets": {"price": {"kano": "performance", "weight": 10}},
        "detail": "full",
    })
    print(response.data)
```

`detail` selects `min`, `lean` (the server default), or `full`. The `min` projection identifies
candidates with `id`; `lean` and `full` use `tool_id`. `format: "text"` returns a string and implies
the compact projection. Streaming requires JSON. The SDK forwards server defaults rather than
replacing them with client defaults.

## Execution

```python
import os
from hyperroute import HyperRoute

with HyperRoute() as client:
    response = client.execute({
        "tool_id": os.environ["HYPERROUTE_TOOL_ID"],
        "query": "Find recent research on battery recycling",
    })
    if response.data.get("ok"):
        print(response.data.get("result"))
    else:
        print(response.data.get("error"))
```

Supply the originating recommendation's `session_id` when executing a selected recommendation.
Report the observed outcome with `report_outcome` / `reportOutcome`; do not infer task success from
HTTP status alone. The runnable execution examples require an explicit tool ID and confirmation
through the `--execute` argument.

`onboard({"tool_id": ..., "api_key": ...})` connects a tool credential to your account.
Use `onboard_info` / `onboardInfo` to read connection requirements first. Recommendations may
point to a native or private tool that your own application must run.

## Several lookups in one call

`run` routes each item on its own and acts on the route: the best tool runs and its result
returns in the same response. One item is one lookup; send up to 50 in one call.

```python
from hyperroute import HyperRoute

with HyperRoute() as client:
    reply = client.run({"items": [
        {"query": "EUR to GBP exchange rate on 2024-03-15"},
        {"query": "Geocode 350 Fifth Avenue, New York to latitude and longitude"},
    ]}).data
    for n, item in enumerate(reply["items"], 1):
        ref = f'{reply["run"]}/{n}'
        if item["action"] == "run" and item["out"]["ok"]:
            print(ref, item["out"]["result"])
        else:
            print(ref, item["action"], item["note"])
```

Each item's `action` says what happened: `run` (the tool ran; `out` is its execution response),
`do_yourself` (your own tools are the best choice; `instruction` carries how they were measured),
`use_own` (a tool you declared), `needs_key` (the best tool needs a credential; `connect` lists the
steps; run the item again after `onboard`), `no_tool`, `advisory`, `choose` (with `mode: "ask"`,
the top three for your user to pick; send the item again with `tool`) and `not_ranked`.

When the best tool fails, the next ready tool within the same quality margin runs; `failed` lists
the tools that failed. Report the items whose `report` is `always`, and the others only when the
result was wrong, in `reports` on your next `run`, addressed `<run>/<n>`. A `useless` or `blocked`
report reopens that item: the response carries the next tool's result, or the item handed back,
as an extra item whose `reopens` names it. `ranking({"run": ..., "item": n})` returns the stored
ranking behind an item as text; with `"evidence": true` it returns JSON with the probes behind the
top rows. Runs are kept for six hours.

`run` executes tools, so like `execute` it is never retried automatically.

## Polling

```python
from hyperroute import HyperRoute

with HyperRoute() as client:
    job = client.submit_recommendation({"query": "Find recent research on battery recycling"})
    response = client.wait_for_recommendation(job.data["job"], timeout=120)
    print(response.data)
```

```typescript
import { HyperRoute } from '@hyperroute/sdk';

const client = new HyperRoute();
const job = await client.submitRecommendation({ query: 'Find recent research on battery recycling' });
const response = await client.waitForRecommendation(job.data.job, { timeoutMs: 120000 });
console.log(response.data);
```

Keep the same authentication identity for submission and polling. A helper only polls the existing
job; it never resubmits. A missing or expired job raises `ApiError`. A failed job raises `JobError`.
Stopping polling does not cancel the server job.

## Streaming

```python
from hyperroute import HyperRoute

with HyperRoute() as client:
    for event in client.stream_recommendation({"query": "Find recent research on battery recycling"}):
        print(event.event, event.data)
```

```typescript
import { HyperRoute } from '@hyperroute/sdk';

const client = new HyperRoute();
for await (const event of client.streamRecommendation({ query: 'Find recent research on battery recycling' })) {
  console.log(event.event, event.data);
}
```

Events include `queued`, `running`, and terminal `result`. Queue events carry a typed
`RecommendationSubmission`; a result event carries a typed `Recommendation`. An `error` event raises `JobError`.
A stream that closes without a result raises `ProtocolError`. Streams are never reconnected
automatically. Python async usage is `async for` over `AsyncHyperRoute.stream_recommendation`.
When stopping a Python iterator early, call its `close()` / `aclose()` to release the connection.

## Errors and response metadata

```python
from hyperroute import ApiError, HyperRoute, RequestOptions

with HyperRoute() as client:
    try:
        response = client.health(options=RequestOptions(timeout=10))
        print(response.status_code, response.headers, response.data)
    except ApiError as error:
        print(error.status_code, error.body)
```

TypeScript methods accept a final options object, for example
`client.health({ timeoutMs: 10000, signal: controller.signal })`.

`ApiError` preserves the HTTP status, response headers, and structured JSON or text error body.
`TransportError` represents an HTTP transport failure; `RequestTimeout` and `CancelledError` are
transport subclasses. `ProtocolError` reports malformed JSON or an invalid stream/job response.
Error messages do not include tokens, request bodies, or server response bodies; inspect `body`
explicitly when needed. Native Python `asyncio.CancelledError` is preserved for task cancellation.

## Large results

Use `read_result` / `readResult` to request a slice, JSON path, or search from a result reference.
`download_result` / `downloadResult` returns bytes / `Uint8Array`. Both require the account that
owns the reference. Downloads are held in memory; size them appropriately for your application.
