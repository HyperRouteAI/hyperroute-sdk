# Recommendation structure

`response.data` is a structured recommendation when `format` is JSON. Python returns a dictionary
with `TypedDict` definitions in `hyperroute.types`; TypeScript returns an object with exported
interfaces. The envelope also exposes HTTP status and headers. `format: "text"` explicitly opts
into a string response.

## Projections

| Field | `min` | `lean` (default) | `full` |
|---|---|---|---|
| `session_id`, `kind`, `status`, `best` | Yes | Yes | Yes |
| Alternative candidates | `alts` | `runner_ups` | `runner_ups` |
| Candidate identifier | `id` | `tool_id` | `tool_id` |
| Candidate explanation | `why` | `reason` | `reason` |
| Capability, uncertainty, LCB, rank | No | Yes | Yes |
| Price estimate and calling descriptor | Compact price/use fields | Yes | Yes |
| Per-candidate `facets` | No | No | Yes |
| Per-candidate `evidence` | No | No | Yes, nullable |
| `facet_options` | No | No | Yes |

Request `detail: "full"` and `evidence_k: 3` to include up to three nearby probes for each shown
tool. `evidence_k: 0` suppresses detailed evidence; an evidence teaser may still be returned.
Evidence is nullable when no probe evidence is available. `best` may be null.

## Scores and evidence

| Candidate field | Meaning |
|---|---|
| `capability` | Estimated capability mean, on a 0–1 scale |
| `band` | Capability uncertainty band |
| `cap_lcb` | Capability lower-confidence bound, accounting for risk aversion |
| `rank` | Final score under the selected preferences; not a success probability |
| `facets[].raw` | Raw value of one preference dimension |
| `facets[].contribution` | Weighted contribution before normalization and must-have gates |
| `evidence.n_real` | Number of real probes available for this tool |
| `evidence.near_mean` | Average score over the nearby probe sample |
| `evidence.dist` | Nearby probe scores, not geometric distances |
| `evidence.probes[].similarity` | Similarity of that probe to the current task |
| `evidence.probes[].score` | Observed aggregate probe score |
| `evidence.probes[].judges` | Facet verdicts, scores, reasoning, and optional individual judge panels |

A private tool is unrated: numeric scores can be null. Do not substitute zero for null. Probe
scores describe past tests, not a guarantee for the current task. A probe's `raw_output` may be
redacted or shortened for transport; judge rationale and panel fields describe the supplied evidence.

`kind` distinguishes `ranked`, `advisory`, and `no_tool`. `status: "needs_facets"` means the pick is
provisional and `facet_form` describes preferences that can refine it. Check the calling descriptor
and connection requirements before execution.

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
    if isinstance(recommendation, str):
        raise TypeError("Expected JSON")
    best = recommendation["best"]
    if best is not None:
        print(best.get("tool_id"), best.get("capability"), best.get("band"), best.get("rank"))
        for facet in best.get("facets", []):
            print(facet["name"], facet["raw"], facet["contribution"])
        evidence = best.get("evidence")
        if evidence is not None:
            for probe in evidence["probes"]:
                print(probe["task_text"], probe["score"], probe["similarity"])
                for judge in probe["judges"]:
                    print(judge["facet"], judge["verdict"], judge["rationale"])
```

## TypeScript

```typescript
import { HyperRoute } from '@hyperroute/sdk';

const client = new HyperRoute();
const { data } = await client.recommend({
  query: 'Find recent research on battery recycling',
  detail: 'full',
  evidence_k: 3,
});
if (typeof data === 'string') throw new TypeError('Expected JSON');
if (data.best) {
  console.log(data.best.tool_id, data.best.capability, data.best.band, data.best.rank);
  for (const facet of data.best.facets ?? []) {
    console.log(facet.name, facet.raw, facet.contribution);
  }
  for (const probe of data.best.evidence?.probes ?? []) {
    console.log(probe.task_text, probe.score, probe.similarity);
    for (const judge of probe.judges) {
      console.log(judge.facet, judge.verdict, judge.rationale);
    }
  }
}
```

See [all data types](types.md) for field-level request and response schemas, including
`Candidate`, `FacetBreakdown`, `ProbeEvidence`, `Probe`, `ProbeJudgment`, and `JudgePanelMember`.
