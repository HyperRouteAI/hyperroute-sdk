# Data types

Generated from the [OpenAPI contract](../contract/openapi.json). Python exports these types from
`hyperroute.types`; TypeScript exports them from `@hyperroute/sdk`. Python values are ordinary
dictionaries described by `TypedDict`. TypeScript values are ordinary objects described by interfaces.
Optional means a field may be absent. Nullable means it may contain JSON null. Unknown additional
response fields are preserved at runtime. See [recommendations](recommendations.md) for score semantics.

## RecommendRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `query` | `string` | Yes |  |
| `facets` | `Record<string, Facet> \| null` | No |  |
| `context` | `JsonObject \| null` | No |  |
| `project_id` | `string \| null` | No |  |
| `detail` | `"min" \| "lean" \| "full" \| null` | No |  |
| `format` | `"json" \| "text" \| null` | No |  |
| `n_runner_ups` | `number \| null` | No |  |
| `evidence_k` | `number \| null` | No |  |
| `caller` | `unknown` | No |  |

## DescribeRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `tool_id` | `string` | Yes |  |
| `sections` | `Array<string> \| null` | No |  |
| `session_id` | `string \| null` | No |  |
| `query` | `string \| null` | No |  |
| `context` | `JsonObject \| null` | No |  |
| `facets` | `JsonObject \| null` | No |  |
| `evidence_k` | `number \| null` | No |  |

## ExecuteRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `tool_id` | `string` | Yes |  |
| `query` | `string` | Yes |  |
| `session_id` | `string \| null` | No |  |
| `caller` | `unknown` | No |  |

## ReportOutcomeRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `session_id` | `string \| null` | No |  |
| `run_id` | `string \| null` | No |  |
| `tool_id` | `string \| null` | No |  |
| `score` | `string \| null` | No |  |
| `reason` | `string \| null` | No |  |
| `comment` | `string \| null` | No |  |
| `status` | `string \| null` | No |  |
| `completed` | `boolean \| null` | No |  |
| `coordinator_signal` | `JsonObject \| null` | No |  |
| `human_survey` | `JsonObject \| null` | No |  |
| `time_to_outcome_ms` | `number \| null` | No |  |
| `downstream_action` | `string \| null` | No |  |
| `dispute` | `boolean \| null` | No |  |
| `caller` | `unknown` | No |  |

## NarrativeReport

| Field | Type | Required | Description |
|---|---|---|---|
| `session_id` | `string \| null` | No |  |
| `text` | `string` | Yes |  |
| `author` | `string` | No |  |
| `steps` | `Array<JsonObject> \| null` | No |  |

## OnboardRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `tool_id` | `string` | Yes |  |
| `api_key` | `string` | Yes |  |
| `label` | `string \| null` | No |  |

## ConnectRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `tool_id` | `string` | Yes |  |
| `api_key` | `string` | Yes |  |
| `label` | `string \| null` | No |  |

## PreferencesRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `facets` | `JsonObject` | Yes |  |
| `project_id` | `string \| null` | No |  |

## PrivateToolRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | `string` | Yes |  |
| `description` | `string` | No |  |
| `triggers` | `Array<string>` | No |  |
| `anchors` | `Array<string>` | No |  |
| `stance` | `string` | No |  |
| `project_id` | `string \| null` | No |  |

## PrivateToolPatch

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | `string \| null` | No |  |
| `description` | `string \| null` | No |  |
| `triggers` | `Array<string> \| null` | No |  |
| `anchors` | `Array<string> \| null` | No |  |
| `stance` | `string \| null` | No |  |

## PreferredToolRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `tool` | `string` | Yes |  |
| `margin` | `number \| null` | No |  |
| `note` | `string` | No |  |
| `project_id` | `string \| null` | No |  |

## PreferredToolPatch

| Field | Type | Required | Description |
|---|---|---|---|
| `margin` | `number \| null` | No |  |
| `note` | `string \| null` | No |  |

## ResultReadRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `op` | `string` | No |  |
| `offset` | `number` | No |  |
| `limit` | `number` | No |  |
| `path` | `Array<unknown> \| null` | No |  |
| `query` | `string \| null` | No |  |

## RegisterRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `email` | `string` | Yes |  |
| `password` | `string` | Yes |  |
| `display_name` | `string \| null` | No |  |

## VerifyRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `email` | `string` | Yes |  |
| `code` | `string` | Yes |  |

## EmailRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `email` | `string` | Yes |  |

## LoginRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `email` | `string` | Yes |  |
| `password` | `string` | Yes |  |

## CodeLoginRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `email` | `string` | Yes |  |
| `code` | `string` | Yes |  |

## ResetPasswordRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `email` | `string` | Yes |  |
| `code` | `string` | Yes |  |
| `new_password` | `string` | Yes |  |

## RecoverRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `email` | `string` | Yes |  |
| `recovery_code` | `string` | Yes |  |
| `new_password` | `string \| null` | No |  |

## TokenCreateRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `label` | `string \| null` | No |  |

## InviteAcceptRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `token` | `string` | Yes |  |
| `email` | `string \| null` | No |  |
| `password` | `string` | Yes |  |

## BetaApplicationRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | `string` | Yes |  |
| `email` | `string` | Yes |  |
| `company` | `string \| null` | No |  |
| `role` | `string \| null` | No |  |
| `purpose` | `string \| null` | No |  |
| `frameworks` | `Array<string> \| null` | No |  |
| `other_tools` | `Array<string> \| null` | No |  |
| `track` | `string \| null` | No |  |
| `survey` | `JsonObject \| null` | No |  |

## JsonObject

| Field | Type | Required | Description |
|---|---|---|---|
| — | Open JSON object | — | Additional fields are preserved. |

## Facet

| Field | Type | Required | Description |
|---|---|---|---|
| `kano` | `"must_be" \| "performance" \| "attractive"` | No |  |
| `weight` | `number` | No |  |
| `threshold` | `number` | No |  |

## Candidate

| Field | Type | Required | Description |
|---|---|---|---|
| — | `MinCandidate` or `LeanCandidate` or `FullCandidate` | — | Projection-specific union. |

## Recommendation

| Field | Type | Required | Description |
|---|---|---|---|
| — | `MinRecommendation` or `LeanRecommendation` or `FullRecommendation` | — | Projection-specific union. |

## RecommendationJob

| Field | Type | Required | Description |
|---|---|---|---|
| — | `QueuedRecommendationJob` or `RunningRecommendationJob` or `CompletedRecommendationJob` or `FailedRecommendationJob` | — | Projection-specific union. |

## ExecutionResult

| Field | Type | Required | Description |
|---|---|---|---|
| — | `ExecutionSuccess` or `ExecutionOverflow` or `ExecutionFailure` | — | Projection-specific union. |

## Health

| Field | Type | Required | Description |
|---|---|---|---|
| `ready` | `boolean` | Yes |  |
| `routable` | `boolean` | Yes |  |

## JudgePanelMember

| Field | Type | Required | Description |
|---|---|---|---|
| `model` | `string \| null` | Yes |  |
| `rationale` | `string \| null` | Yes |  |
| `score` | `number` | No |  |
| `label` | `string` | No |  |
| `value` | `number` | No |  |

## ProbeJudgment

| Field | Type | Required | Description |
|---|---|---|---|
| `facet` | `string \| null` | Yes |  |
| `verdict` | `string \| null` | Yes |  |
| `score` | `number \| null` | Yes |  |
| `rationale` | `string \| null` | Yes |  |
| `panel` | `Array<JudgePanelMember> \| null` | Yes |  |

## Probe

| Field | Type | Required | Description |
|---|---|---|---|
| `probe_id` | `number \| string \| null` | Yes |  |
| `similarity` | `number` | Yes | Cosine similarity to the requested task; not a success probability. |
| `task_text` | `string \| null` | Yes |  |
| `adapted_input` | `string \| null` | Yes |  |
| `score` | `number` | Yes | Observed aggregate score for this probe, on a 0–1 scale. |
| `redacted` | `boolean \| null` | Yes |  |
| `output_chars` | `number \| null` | Yes |  |
| `truncated` | `boolean` | Yes |  |
| `created_at` | `string \| null` | Yes |  |
| `judges` | `Array<ProbeJudgment>` | Yes |  |
| `raw_output` | `string \| null` | Yes | Transport-sized output excerpt; null when redacted. May contain a truncation marker. |

## ProbeEvidence

| Field | Type | Required | Description |
|---|---|---|---|
| `n_real` | `number` | Yes | Count of real probes available for this tool. |
| `n_near` | `number` | Yes |  |
| `near_mean` | `number` | Yes |  |
| `dist` | `Array<number>` | Yes | Scores of nearby probes; not distances. |
| `probes` | `Array<Probe>` | Yes |  |

## EvidenceTeaser

| Field | Type | Required | Description |
|---|---|---|---|
| `task_text` | `string \| null` | Yes |  |
| `verdict` | `string \| null` | Yes |  |
| `score` | `number` | Yes |  |
| `similarity` | `number` | Yes |  |
| `n_real` | `number` | Yes |  |

## FacetBreakdown

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | `string` | Yes |  |
| `kano` | `"must_be" \| "performance" \| "attractive"` | Yes |  |
| `weight` | `number` | Yes |  |
| `threshold` | `number` | Yes |  |
| `raw` | `number` | Yes | Raw facet value before its Kano transform. |
| `contribution` | `number` | Yes | Weighted contribution before normalization and must-have gates. |

## PriceEstimate

| Field | Type | Required | Description |
|---|---|---|---|
| `amount` | `number \| null` | No |  |
| `per_query_usd` | `number` | Yes |  |
| `currency` | `string` | No |  |
| `confidence` | `string` | No |  |
| `selected_plan` | `string \| null` | No |  |
| `held` | `boolean` | Yes |  |
| `estimated` | `boolean` | No |  |
| `cost_unknown` | `boolean` | Yes |  |
| `breakdown` | `Array<PricePlan>` | No |  |
| `note` | `string` | No |  |

## CallingSummary

| Field | Type | Required | Description |
|---|---|---|---|
| `usability` | `string` | No |  |
| `auth_method` | `string` | No |  |
| `api_type` | `string \| null` | No |  |
| `connected` | `boolean` | No |  |
| `free` | `boolean` | No |  |
| `how` | `string` | No |  |
| `signup_url` | `string \| null` | No |  |

## CallingDescriptor

| Field | Type | Required | Description |
|---|---|---|---|
| `tool_id` | `string` | No |  |
| `coordinator_class` | `boolean` | No |  |
| `executable` | `boolean` | No |  |
| `endpoint` | `JsonObject` | No |  |
| `adapter` | `JsonObject` | No |  |
| `auth` | `JsonObject` | No |  |
| `summary` | `CallingSummary` | No |  |
| `base_tool` | `string` | No |  |
| `adapter_mode` | `unknown` | No |  |
| `connect` | `JsonObject` | No |  |
| `mcp_install` | `JsonObject` | No |  |

## OutcomeHealth

| Field | Type | Required | Description |
|---|---|---|---|
| `level` | `"green" \| "amber" \| "red"` | Yes |  |
| `label` | `string` | Yes |  |

## FacetFormField

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | `string` | No |  |
| `optional` | `boolean` | No |  |
| `default` | `string` | No |  |
| `spread` | `number` | No |  |
| `divergence_over_shortlist` | `Record<string, number>` | No |  |
| `note` | `string` | No |  |

## FacetForm

| Field | Type | Required | Description |
|---|---|---|---|
| `reason` | `string` | No |  |
| `decidable` | `boolean` | No |  |
| `decide_margin` | `number` | No |  |
| `shortlist` | `Array<string>` | No |  |
| `fields` | `Array<FacetFormField>` | No |  |

## ActiveFacet

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | `string` | No |  |
| `kano` | `string` | No |  |
| `weight` | `number` | No |  |
| `threshold` | `number` | No |  |
| `scope` | `string` | No |  |
| `kind` | `string` | No |  |
| `source` | `string` | No |  |

## FacetState

| Field | Type | Required | Description |
|---|---|---|---|
| `active` | `Array<ActiveFacet>` | No |  |
| `query_specific_available` | `Array<string>` | No |  |
| `hint` | `string` | No |  |

## FacetOption

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | `string` | No |  |
| `label` | `string` | No |  |
| `description` | `string` | No |  |
| `text_source` | `string` | No |  |
| `scope` | `string` | No |  |
| `kind` | `string` | No |  |
| `spread` | `number \| null` | No |  |
| `divergent` | `boolean` | No |  |
| `on` | `boolean` | No |  |
| `kano` | `string` | No |  |
| `weight` | `number` | No |  |
| `default_weight` | `number` | No |  |
| `threshold` | `number` | No |  |
| `values` | `Record<string, number>` | No |  |

## Description

| Field | Type | Required | Description |
|---|---|---|---|
| `tool_id` | `string` | Yes |  |
| `name` | `string \| null` | Yes |  |
| `about` | `JsonObject` | No |  |
| `price` | `PriceEstimate` | No |  |
| `facets` | `Array<FacetBreakdown>` | No |  |
| `evidence` | `ProbeEvidence \| null` | No |  |
| `error` | `string` | No |  |
| `note` | `string` | No |  |

## FullCandidate

| Field | Type | Required | Description |
|---|---|---|---|
| `tool_id` | `string` | Yes |  |
| `name` | `string` | Yes |  |
| `reason` | `string` | Yes |  |
| `calling` | `CallingDescriptor \| null` | Yes |  |
| `capability` | `number \| null` | Yes | Estimated capability mean on a 0–1 scale; null for an unrated private tool. |
| `variant` | `string \| null` | Yes |  |
| `capabilities` | `Array<string>` | Yes |  |
| `description` | `string` | Yes |  |
| `kind` | `string` | Yes |  |
| `endpoint` | `JsonObject` | Yes |  |
| `band` | `number \| null` | Yes | Capability uncertainty band; null for an unrated private tool. |
| `cap_lcb` | `number \| null` | Yes | Risk-adjusted lower-confidence capability estimate. |
| `rank` | `number \| null` | Yes | Final preference-weighted ranking score; not a probability. |
| `price` | `PriceEstimate \| null` | Yes |  |
| `unrated` | `boolean` | No |  |
| `field_health` | `string` | No |  |
| `outcome_health` | `OutcomeHealth` | No |  |
| `facets` | `Array<FacetBreakdown>` | Yes | Present in the full projection. |
| `evidence` | `ProbeEvidence \| null` | Yes | Full projection only; null when probe evidence is unavailable or not requested. |
| `evidence_teaser` | `EvidenceTeaser` | No |  |

## LeanCandidate

| Field | Type | Required | Description |
|---|---|---|---|
| `tool_id` | `string` | Yes |  |
| `name` | `string` | Yes |  |
| `reason` | `string` | Yes |  |
| `calling` | `CallingDescriptor \| null` | Yes |  |
| `capability` | `number \| null` | Yes | Estimated capability mean on a 0–1 scale; null for an unrated private tool. |
| `variant` | `string \| null` | Yes |  |
| `capabilities` | `Array<string>` | Yes |  |
| `description` | `string` | Yes |  |
| `kind` | `string` | Yes |  |
| `endpoint` | `JsonObject` | Yes |  |
| `band` | `number \| null` | Yes | Capability uncertainty band; null for an unrated private tool. |
| `cap_lcb` | `number \| null` | Yes | Risk-adjusted lower-confidence capability estimate. |
| `rank` | `number \| null` | Yes | Final preference-weighted ranking score; not a probability. |
| `price` | `PriceEstimate \| null` | Yes |  |
| `unrated` | `boolean` | No |  |
| `field_health` | `string` | No |  |
| `outcome_health` | `OutcomeHealth` | No |  |

## MinCandidate

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | `string` | Yes |  |
| `name` | `string` | Yes |  |
| `why` | `string` | Yes |  |
| `price` | `string` | Yes |  |
| `use` | `string` | Yes |  |
| `confidence` | `string` | No |  |

## LeanRecommendation

| Field | Type | Required | Description |
|---|---|---|---|
| `session_id` | `string \| null` | Yes |  |
| `kind` | `"ranked" \| "advisory" \| "no_tool"` | Yes |  |
| `status` | `"ok" \| "needs_facets"` | Yes |  |
| `best` | `LeanCandidate \| null` | Yes |  |
| `runner_ups` | `Array<LeanCandidate>` | Yes |  |
| `calling` | `CallingDescriptor \| null` | Yes |  |
| `provisional` | `boolean` | Yes |  |
| `disclaimer` | `string` | Yes |  |
| `facet_form` | `FacetForm \| null` | Yes |  |
| `decidable` | `boolean` | Yes |  |
| `decide_margin` | `number` | Yes |  |
| `not_checked` | `Array<string>` | Yes |  |
| `flags` | `RoutingFlags` | Yes |  |
| `facet_state` | `FacetState \| null` | Yes |  |
| `coverage` | `JsonObject` | No |  |
| `input_truncated` | `JsonObject` | No |  |

## FullRecommendation

| Field | Type | Required | Description |
|---|---|---|---|
| `session_id` | `string \| null` | Yes |  |
| `kind` | `"ranked" \| "advisory" \| "no_tool"` | Yes |  |
| `status` | `"ok" \| "needs_facets"` | Yes |  |
| `best` | `FullCandidate \| null` | Yes |  |
| `runner_ups` | `Array<FullCandidate>` | Yes |  |
| `calling` | `CallingDescriptor \| null` | Yes |  |
| `provisional` | `boolean` | Yes |  |
| `disclaimer` | `string` | Yes |  |
| `facet_form` | `FacetForm \| null` | Yes |  |
| `decidable` | `boolean` | Yes |  |
| `decide_margin` | `number` | Yes |  |
| `not_checked` | `Array<string>` | Yes |  |
| `flags` | `RoutingFlags` | Yes |  |
| `facet_state` | `FacetState \| null` | Yes |  |
| `coverage` | `JsonObject` | No |  |
| `input_truncated` | `JsonObject` | No |  |
| `facet_options` | `Array<FacetOption>` | Yes |  |

## MinRecommendation

| Field | Type | Required | Description |
|---|---|---|---|
| `session_id` | `string \| null` | Yes |  |
| `kind` | `"ranked" \| "advisory" \| "no_tool"` | Yes |  |
| `status` | `"ok" \| "needs_facets"` | Yes |  |
| `coverage` | `JsonObject` | No |  |
| `not_checked` | `Array<string>` | No |  |
| `input_truncated` | `JsonObject` | No |  |
| `best` | `MinCandidate \| null` | Yes |  |
| `alts` | `Array<MinCandidate>` | Yes |  |
| `verdict` | `string \| null` | Yes |  |
| `refine` | `Array<string>` | Yes |  |
| `act` | `string` | Yes |  |
| `connect` | `JsonObject` | No |  |
| `consider` | `Array<JsonObject>` | No |  |
| `preferred` | `PreferredDecision` | No |  |

## LeanRecommendRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `query` | `string` | Yes |  |
| `facets` | `Record<string, Facet> \| null` | No |  |
| `context` | `JsonObject \| null` | No |  |
| `project_id` | `string \| null` | No |  |
| `detail` | `"lean" \| null` | No |  |
| `format` | `"json" \| null` | No |  |
| `n_runner_ups` | `number \| null` | No |  |
| `evidence_k` | `number \| null` | No |  |
| `caller` | `unknown` | No |  |

## FullRecommendRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `query` | `string` | Yes |  |
| `facets` | `Record<string, Facet> \| null` | No |  |
| `context` | `JsonObject \| null` | No |  |
| `project_id` | `string \| null` | No |  |
| `detail` | `"full"` | Yes |  |
| `format` | `"json" \| null` | No |  |
| `n_runner_ups` | `number \| null` | No |  |
| `evidence_k` | `number \| null` | No |  |
| `caller` | `unknown` | No |  |

## MinRecommendRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `query` | `string` | Yes |  |
| `facets` | `Record<string, Facet> \| null` | No |  |
| `context` | `JsonObject \| null` | No |  |
| `project_id` | `string \| null` | No |  |
| `detail` | `"min"` | Yes |  |
| `format` | `"json" \| null` | No |  |
| `n_runner_ups` | `number \| null` | No |  |
| `evidence_k` | `number \| null` | No |  |
| `caller` | `unknown` | No |  |

## TextRecommendRequest

| Field | Type | Required | Description |
|---|---|---|---|
| `query` | `string` | Yes |  |
| `facets` | `Record<string, Facet> \| null` | No |  |
| `context` | `JsonObject \| null` | No |  |
| `project_id` | `string \| null` | No |  |
| `detail` | `"min" \| "lean" \| "full" \| null` | No |  |
| `format` | `"text"` | Yes |  |
| `n_runner_ups` | `number \| null` | No |  |
| `evidence_k` | `number \| null` | No |  |
| `caller` | `unknown` | No |  |

## User

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | `string` | Yes |  |
| `email` | `string \| null` | Yes |  |
| `display_name` | `string \| null` | Yes |  |
| `tier` | `string` | Yes |  |
| `status` | `string` | Yes |  |
| `verified` | `boolean` | Yes |  |

## AuthSession

| Field | Type | Required | Description |
|---|---|---|---|
| `ok` | `true` | Yes |  |
| `user` | `User \| null` | Yes |  |
| `api_key` | `string` | Yes |  |
| `recovery_codes` | `Array<string>` | No |  |

## MessageResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `ok` | `boolean` | Yes |  |
| `message` | `string` | Yes |  |

## RegistrationResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `ok` | `true` | Yes |  |
| `verification_required` | `boolean` | Yes |  |
| `email` | `string` | Yes |  |
| `message` | `string` | Yes |  |

## CreatedToken

| Field | Type | Required | Description |
|---|---|---|---|
| `ok` | `true` | Yes |  |
| `api_key` | `string` | Yes |  |
| `label` | `string` | Yes |  |

## Token

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | `string` | No |  |
| `label` | `string \| null` | No |  |
| `created_at` | `string \| null` | No |  |
| `last_used_at` | `string \| null` | No |  |
| `kind` | `string` | No |  |
| `client_name` | `string` | No |  |
| `scopes` | `Array<string>` | No |  |

## TokenList

| Field | Type | Required | Description |
|---|---|---|---|
| `tokens` | `Array<Token>` | Yes |  |

## RevokedResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `revoked` | `boolean` | Yes |  |

## DeletedResponse

| Field | Type | Required | Description |
|---|---|---|---|
| `deleted` | `boolean` | Yes |  |
| `reason` | `string` | No |  |

## Credential

| Field | Type | Required | Description |
|---|---|---|---|
| `credential_id` | `string \| null` | Yes |  |
| `tool_id` | `string \| null` | Yes |  |
| `label` | `string \| null` | Yes |  |
| `connected_at` | `string \| null` | Yes |  |
| `last_test_at` | `string \| null` | Yes |  |
| `last_test_status` | `string \| null` | Yes |  |
| `name` | `string` | No |  |

## CredentialResult

| Field | Type | Required | Description |
|---|---|---|---|
| `credential_id` | `string \| null` | No |  |
| `tool_id` | `string \| null` | No |  |
| `label` | `string \| null` | No |  |
| `connected_at` | `string \| null` | No |  |
| `last_test_at` | `string \| null` | No |  |
| `last_test_status` | `string \| null` | No |  |
| `name` | `string` | No |  |
| `ok` | `boolean` | Yes |  |
| `status` | `string` | No |  |
| `reason` | `string` | No |  |

## CredentialList

| Field | Type | Required | Description |
|---|---|---|---|
| `credentials` | `Array<Credential>` | Yes |  |

## OnboardInfo

| Field | Type | Required | Description |
|---|---|---|---|
| `tool_id` | `string` | Yes |  |
| `name` | `string \| null` | Yes |  |
| `auth_method` | `string` | Yes |  |
| `requires_key` | `boolean` | Yes |  |
| `connected` | `boolean` | Yes |  |
| `summary` | `CallingSummary \| null` | Yes |  |
| `connect` | `JsonObject \| null` | Yes |  |

## Preferences

| Field | Type | Required | Description |
|---|---|---|---|
| `user` | `Record<string, Facet>` | Yes |  |
| `project_id` | `string` | No |  |
| `project` | `Record<string, Facet>` | No |  |
| `effective` | `Record<string, Facet>` | Yes |  |

## StoredPreferences

| Field | Type | Required | Description |
|---|---|---|---|
| `stored` | `Record<string, Facet>` | Yes |  |
| `project_id` | `string \| null` | Yes |  |
| `effective` | `Record<string, Facet>` | Yes |  |

## Region

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | `string` | Yes |  |
| `label` | `string` | Yes |  |

## PrivateTool

| Field | Type | Required | Description |
|---|---|---|---|
| `tool_id` | `string` | Yes |  |
| `name` | `string` | Yes |  |
| `description` | `string` | Yes |  |
| `triggers` | `Array<string>` | Yes |  |
| `anchors` | `Array<string>` | Yes |  |
| `stance` | `string` | Yes |  |
| `project_id` | `string` | Yes |  |
| `regions` | `Array<Region>` | No |  |

## PrivateToolList

| Field | Type | Required | Description |
|---|---|---|---|
| `tools` | `Array<PrivateTool>` | Yes |  |
| `anchors_available` | `boolean` | Yes |  |

## DeclaredPrivateTool

| Field | Type | Required | Description |
|---|---|---|---|
| `declared` | `PrivateTool` | Yes |  |
| `triggers` | `Array<string>` | Yes |  |
| `regions` | `Array<Region>` | Yes |  |

## UpdatedPrivateTool

| Field | Type | Required | Description |
|---|---|---|---|
| `updated` | `PrivateTool` | Yes |  |

## RegionSuggestion

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | `string` | Yes |  |
| `label` | `string` | Yes |  |
| `similarity` | `number` | Yes |  |
| `group` | `string` | Yes |  |
| `in_taxonomy` | `boolean` | Yes |  |

## RegionSuggestions

| Field | Type | Required | Description |
|---|---|---|---|
| `suggestions` | `Array<RegionSuggestion>` | Yes |  |

## PreferredTool

| Field | Type | Required | Description |
|---|---|---|---|
| `tool_id` | `string` | Yes |  |
| `margin` | `number` | Yes |  |
| `note` | `string` | Yes |  |
| `project_id` | `string` | Yes |  |
| `name` | `string` | No |  |
| `in_catalog` | `boolean` | No |  |

## PreferredToolList

| Field | Type | Required | Description |
|---|---|---|---|
| `tools` | `Array<PreferredTool>` | Yes |  |

## ToolIdentity

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | `string` | Yes |  |
| `name` | `string \| null` | Yes |  |

## PreferredToolResult

| Field | Type | Required | Description |
|---|---|---|---|
| `preferred` | `PreferredTool` | Yes |  |
| `tool` | `ToolIdentity` | Yes |  |

## UpdatedPreferredTool

| Field | Type | Required | Description |
|---|---|---|---|
| `updated` | `PreferredTool` | Yes |  |

## FacetCatalogEntry

| Field | Type | Required | Description |
|---|---|---|---|
| `name` | `string` | Yes |  |
| `label` | `string` | Yes |  |
| `description` | `string` | Yes |  |
| `scope` | `string` | Yes |  |
| `kind` | `string` | Yes |  |
| `constraint` | `boolean` | Yes |  |
| `spine` | `boolean` | Yes |  |
| `default_kano` | `string` | Yes |  |
| `default_weight` | `number` | Yes |  |
| `default_threshold` | `number` | Yes |  |

## FacetCatalog

| Field | Type | Required | Description |
|---|---|---|---|
| `ready` | `boolean` | Yes |  |
| `facets` | `Array<FacetCatalogEntry>` | Yes |  |

## QueueLane

| Field | Type | Required | Description |
|---|---|---|---|
| `queued` | `number` | Yes |  |
| `avg_ms` | `number` | Yes |  |
| `completed` | `number` | Yes |  |

## RunningJob

| Field | Type | Required | Description |
|---|---|---|---|
| `lane` | `string` | Yes |  |

## QueueStatus

| Field | Type | Required | Description |
|---|---|---|---|
| `concurrency` | `number` | Yes |  |
| `queued_total` | `number` | Yes |  |
| `running` | `Array<RunningJob>` | Yes |  |
| `lanes` | `Record<string, QueueLane>` | Yes |  |

## AcceptedOutcome

| Field | Type | Required | Description |
|---|---|---|---|
| `score` | `string \| null` | No |  |
| `reason` | `string \| null` | No |  |
| `counts_as_quality` | `boolean` | No |  |
| `quality` | `number \| null` | No |  |
| `comment` | `boolean` | No |  |
| `human_survey` | `boolean` | No |  |

## OutcomeReport

| Field | Type | Required | Description |
|---|---|---|---|
| `ok` | `true` | Yes |  |
| `session_id` | `string` | Yes |  |
| `tool_id` | `string \| null` | Yes |  |
| `accepted` | `AcceptedOutcome` | Yes |  |
| `field_probe` | `FieldProbeResult \| null` | Yes |  |
| `triggers_raised` | `Array<string>` | Yes |  |
| `score_moved` | `false` | Yes |  |
| `private` | `boolean` | No |  |

## NarrativeResult

| Field | Type | Required | Description |
|---|---|---|---|
| `ok` | `true` | Yes |  |
| `id` | `number` | Yes |  |
| `stored` | `"db" \| "memory"` | Yes |  |

## OverflowResult

| Field | Type | Required | Description |
|---|---|---|---|
| `ref` | `string` | Yes |  |
| `bytes` | `number` | Yes |  |
| `content_type` | `string` | Yes |  |
| `preview` | `string` | Yes |  |
| `resource_url` | `string` | Yes |  |
| `note` | `string` | Yes |  |

## ResultShape

| Field | Type | Required | Description |
|---|---|---|---|
| `type` | `string` | Yes |  |
| `keys` | `Array<string>` | No |  |
| `length` | `number` | No |  |

## ReadResult

| Field | Type | Required | Description |
|---|---|---|---|
| — | `ResultSlice` or `ResultSearch` or `ResultJsonPath` or `ResultReadError` | — | Projection-specific union. |

## BetaApplication

| Field | Type | Required | Description |
|---|---|---|---|
| `ok` | `true` | Yes |  |
| `persisted` | `boolean` | Yes |  |
| `id` | `string` | No |  |
| `track` | `string` | Yes |  |
| `position` | `number` | No |  |

## CollectorRule

| Field | Type | Required | Description |
|---|---|---|---|
| `id` | `string` | No |  |
| `kind` | `string` | No |  |
| `path` | `string` | No |  |
| `var` | `string` | No |  |
| `tail` | `number` | No |  |
| `out` | `Record<string, string>` | No |  |
| `set` | `JsonObject` | No |  |
| `where` | `JsonObject` | No |  |
| `table` | `string` | No |  |
| `order` | `string` | No |  |

## AgentCollector

| Field | Type | Required | Description |
|---|---|---|---|
| `match` | `Record<string, Array<string>>` | Yes |  |
| `probes` | `Array<CollectorRule>` | Yes |  |

## CallerCollectors

| Field | Type | Required | Description |
|---|---|---|---|
| `version` | `number` | Yes |  |
| `agents` | `Record<string, AgentCollector>` | Yes |  |

## ConsoleResult

| Field | Type | Required | Description |
|---|---|---|---|
| `view` | `string` | Yes |  |
| `tools` | `Array<JsonObject>` | No |  |
| `connections` | `number \| Array<Credential>` | No |  |
| `events` | `Array<JsonObject>` | No |  |
| `categories` | `Array<JsonObject>` | No |  |
| `preferred` | `Array<PreferredTool>` | No |  |
| `present` | `boolean` | No |  |
| `model` | `string` | No |  |
| `n_tools` | `number` | No |  |
| `n_facets` | `number` | No |  |
| `stats` | `JsonObject` | No |  |
| `recent` | `Array<JsonObject>` | No |  |
| `total_calls` | `number` | No |  |
| `routed` | `number` | No |  |
| `passed_through` | `number` | No |  |
| `verdicts` | `Record<string, number>` | No |  |
| `top_tools` | `Array<Array<string \| number>>` | No |  |
| `executed` | `number` | No |  |
| `outcomes` | `Record<string, number>` | No |  |
| `avg_latency_ms` | `number \| null` | No |  |

## QueuedRecommendationJob

| Field | Type | Required | Description |
|---|---|---|---|
| `job` | `string` | Yes |  |
| `state` | `"queued"` | Yes |  |
| `lane` | `string` | Yes |  |
| `position` | `number \| null` | Yes |  |
| `lane_position` | `number \| null` | No |  |
| `eta_ms` | `number` | Yes |  |

## RunningRecommendationJob

| Field | Type | Required | Description |
|---|---|---|---|
| `job` | `string` | Yes |  |
| `state` | `"running"` | Yes |  |
| `lane` | `string` | Yes |  |
| `position` | `number \| null` | Yes |  |
| `lane_position` | `number \| null` | No |  |
| `eta_ms` | `number` | Yes |  |

## CompletedRecommendationJob

| Field | Type | Required | Description |
|---|---|---|---|
| `job` | `string` | Yes |  |
| `state` | `"done"` | Yes |  |
| `lane` | `string` | Yes |  |
| `position` | `number \| null` | Yes |  |
| `lane_position` | `number \| null` | No |  |
| `eta_ms` | `number` | Yes |  |
| `result` | `Recommendation` | Yes |  |

## FailedRecommendationJob

| Field | Type | Required | Description |
|---|---|---|---|
| `job` | `string` | Yes |  |
| `state` | `"error"` | Yes |  |
| `lane` | `string` | Yes |  |
| `position` | `number \| null` | Yes |  |
| `lane_position` | `number \| null` | No |  |
| `eta_ms` | `number` | Yes |  |
| `error` | `string` | Yes |  |

## ExecutionSuccess

| Field | Type | Required | Description |
|---|---|---|---|
| `ok` | `true` | Yes |  |
| `tool_id` | `string` | Yes |  |
| `result` | `unknown` | Yes |  |
| `error` | `string \| null` | No |  |
| `latency_ms` | `number` | No |  |
| `query` | `string` | No |  |
| `adapted_query` | `string` | No |  |
| `message` | `string` | No |  |
| `status` | `string` | No |  |
| `credentials` | `Array<string>` | No |  |
| `connect` | `JsonObject` | No |  |

## ExecutionOverflow

| Field | Type | Required | Description |
|---|---|---|---|
| `ok` | `true` | Yes |  |
| `tool_id` | `string` | Yes |  |
| `error` | `string \| null` | No |  |
| `latency_ms` | `number` | No |  |
| `overflow` | `OverflowResult` | Yes |  |
| `query` | `string` | No |  |
| `adapted_query` | `string` | No |  |
| `message` | `string` | No |  |
| `status` | `string` | No |  |
| `credentials` | `Array<string>` | No |  |
| `connect` | `JsonObject` | No |  |

## ExecutionFailure

| Field | Type | Required | Description |
|---|---|---|---|
| `ok` | `false` | Yes |  |
| `tool_id` | `string` | Yes |  |
| `result` | `unknown` | No |  |
| `error` | `string \| null` | Yes |  |
| `latency_ms` | `number` | No |  |
| `overflow` | `OverflowResult` | No |  |
| `query` | `string` | No |  |
| `adapted_query` | `string` | No |  |
| `message` | `string` | No |  |
| `status` | `string` | No |  |
| `credentials` | `Array<string>` | No |  |
| `connect` | `JsonObject` | No |  |

## ResultSlice

| Field | Type | Required | Description |
|---|---|---|---|
| `offset` | `number` | Yes |  |
| `limit` | `number` | Yes |  |
| `total_lines` | `number` | Yes |  |
| `content` | `string` | Yes |  |
| `truncated` | `boolean` | Yes |  |
| `ok` | `true` | Yes |  |
| `op` | `"slice"` | Yes |  |

## ResultSearch

| Field | Type | Required | Description |
|---|---|---|---|
| `count` | `number` | Yes |  |
| `matches_json` | `string` | Yes |  |
| `truncated` | `boolean` | Yes |  |
| `ok` | `true` | Yes |  |
| `op` | `"search"` | Yes |  |

## ResultJsonPath

| Field | Type | Required | Description |
|---|---|---|---|
| `shape` | `ResultShape` | Yes |  |
| `value_json` | `string` | Yes |  |
| `truncated` | `boolean` | Yes |  |
| `ok` | `true` | Yes |  |
| `op` | `"json_path"` | Yes |  |

## ResultReadError

| Field | Type | Required | Description |
|---|---|---|---|
| `ok` | `false` | Yes |  |
| `error` | `string` | Yes |  |
| `message` | `string` | Yes |  |

## RecommendationSubmission

| Field | Type | Required | Description |
|---|---|---|---|
| `job` | `string` | Yes |  |
| `state` | `"queued" \| "running" \| "done" \| "error"` | Yes |  |
| `lane` | `string` | Yes |  |
| `position` | `number \| null` | Yes |  |
| `lane_position` | `number \| null` | No |  |
| `eta_ms` | `number` | Yes |  |
| `error` | `string` | No |  |

## FieldProbeResult

| Field | Type | Required | Description |
|---|---|---|---|
| `ok` | `boolean` | Yes |  |
| `id` | `number` | No |  |
| `stored` | `string` | No |  |
| `error` | `string` | No |  |

## PricePlan

| Field | Type | Required | Description |
|---|---|---|---|
| `plan_id` | `string \| null` | Yes |  |
| `kind` | `string \| null` | Yes |  |
| `plan_group` | `string \| null` | Yes |  |
| `effective_usd` | `number` | Yes |  |
| `held` | `boolean` | Yes |  |
| `currency` | `string` | Yes |  |
| `confidence` | `string` | Yes |  |
| `overridden` | `boolean` | Yes |  |

## PreferredDecision

| Field | Type | Required | Description |
|---|---|---|---|
| `tool_id` | `string` | No |  |
| `name` | `string` | No |  |
| `honoured` | `boolean` | No |  |
| `acceptable` | `boolean` | No |  |
| `gap` | `number` | No |  |
| `margin` | `number` | No |  |
| `cap_lcb` | `number` | No |  |
| `threshold` | `number` | No |  |
| `best` | `string` | No |  |
| `best_name` | `string` | No |  |

## ExcludedTools

| Field | Type | Required | Description |
|---|---|---|---|
| `count` | `number` | Yes |  |
| `facets` | `Array<string>` | Yes |  |
| `tool_ids` | `Array<string>` | Yes |  |

## NativeBaseline

| Field | Type | Required | Description |
|---|---|---|---|
| `score` | `number` | Yes |  |
| `source` | `string` | Yes |  |
| `tau` | `number` | Yes |  |
| `self` | `boolean` | Yes |  |

## OwnToolDecision

| Field | Type | Required | Description |
|---|---|---|---|
| `tool_id` | `string` | No |  |
| `trigger` | `string` | No |  |
| `match` | `number` | No |  |
| `stance` | `string` | No |  |
| `own_quality_mean` | `number \| null` | No |  |
| `outcomes` | `number` | No |  |

## RoutingFlags

| Field | Type | Required | Description |
|---|---|---|---|
| `short_circuit` | `boolean` | No |  |
| `learned_preset` | `string` | No |  |
| `match_similarity` | `number` | No |  |
| `digest_skipped` | `boolean` | No |  |
| `digest_applied` | `boolean` | No |  |
| `excluded` | `ExcludedTools` | No |  |
| `verdict` | `string` | No |  |
| `preferred` | `PreferredDecision` | No |  |
| `own` | `OwnToolDecision` | No |  |
| `consider` | `Array<JsonObject>` | No |  |
| `baseline` | `NativeBaseline` | No |  |
