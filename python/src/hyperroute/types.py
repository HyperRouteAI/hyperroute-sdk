from __future__ import annotations
from typing import Any, Literal, NotRequired, TypedDict, TypeAlias, Union

JsonObject = dict[str, Any]

class RecommendRequest(TypedDict):
    query: str
    facets: NotRequired[dict[str, Facet] | None]
    context: NotRequired[JsonObject | None]
    project_id: NotRequired[str | None]
    detail: NotRequired[Literal['min', 'lean', 'full'] | None]
    format: NotRequired[Literal['json', 'text'] | None]
    n_runner_ups: NotRequired[int | None]
    evidence_k: NotRequired[int | None]
    caller: NotRequired[Any]

class DescribeRequest(TypedDict):
    tool_id: str
    sections: NotRequired[list[str] | None]
    session_id: NotRequired[str | None]
    query: NotRequired[str | None]
    context: NotRequired[JsonObject | None]
    facets: NotRequired[JsonObject | None]
    evidence_k: NotRequired[int | None]

class ExecuteRequest(TypedDict):
    tool_id: str
    query: str
    session_id: NotRequired[str | None]
    caller: NotRequired[Any]

class ReportOutcomeRequest(TypedDict):
    session_id: NotRequired[str | None]
    run_id: NotRequired[str | None]
    tool_id: NotRequired[str | None]
    score: NotRequired[str | None]
    reason: NotRequired[str | None]
    comment: NotRequired[str | None]
    status: NotRequired[str | None]
    completed: NotRequired[bool | None]
    coordinator_signal: NotRequired[JsonObject | None]
    human_survey: NotRequired[JsonObject | None]
    time_to_outcome_ms: NotRequired[int | None]
    downstream_action: NotRequired[str | None]
    dispute: NotRequired[bool | None]
    caller: NotRequired[Any]

class NarrativeReport(TypedDict):
    session_id: NotRequired[str | None]
    text: str
    author: NotRequired[str]
    steps: NotRequired[list[JsonObject] | None]

class OnboardRequest(TypedDict):
    tool_id: str
    api_key: str
    label: NotRequired[str | None]

class ConnectRequest(TypedDict):
    tool_id: str
    api_key: str
    label: NotRequired[str | None]

class PreferencesRequest(TypedDict):
    facets: JsonObject
    project_id: NotRequired[str | None]

class PrivateToolRequest(TypedDict):
    name: str
    description: NotRequired[str]
    triggers: NotRequired[list[str]]
    anchors: NotRequired[list[str]]
    stance: NotRequired[str]
    project_id: NotRequired[str | None]

class PrivateToolPatch(TypedDict):
    name: NotRequired[str | None]
    description: NotRequired[str | None]
    triggers: NotRequired[list[str] | None]
    anchors: NotRequired[list[str] | None]
    stance: NotRequired[str | None]

class PreferredToolRequest(TypedDict):
    tool: str
    margin: NotRequired[float | None]
    note: NotRequired[str]
    project_id: NotRequired[str | None]

class PreferredToolPatch(TypedDict):
    margin: NotRequired[float | None]
    note: NotRequired[str | None]

class ResultReadRequest(TypedDict):
    op: NotRequired[str]
    offset: NotRequired[int]
    limit: NotRequired[int]
    path: NotRequired[list[Any] | None]
    query: NotRequired[str | None]

class RegisterRequest(TypedDict):
    email: str
    password: str
    display_name: NotRequired[str | None]

class VerifyRequest(TypedDict):
    email: str
    code: str

class EmailRequest(TypedDict):
    email: str

class LoginRequest(TypedDict):
    email: str
    password: str

class CodeLoginRequest(TypedDict):
    email: str
    code: str

class ResetPasswordRequest(TypedDict):
    email: str
    code: str
    new_password: str

class RecoverRequest(TypedDict):
    email: str
    recovery_code: str
    new_password: NotRequired[str | None]

class TokenCreateRequest(TypedDict):
    label: NotRequired[str | None]

class InviteAcceptRequest(TypedDict):
    token: str
    email: NotRequired[str | None]
    password: str

class BetaApplicationRequest(TypedDict):
    name: str
    email: str
    company: NotRequired[str | None]
    role: NotRequired[str | None]
    purpose: NotRequired[str | None]
    frameworks: NotRequired[list[str] | None]
    other_tools: NotRequired[list[str] | None]
    track: NotRequired[str | None]
    survey: NotRequired[JsonObject | None]

class Facet(TypedDict):
    kano: NotRequired[Literal['must_be', 'performance', 'attractive']]
    weight: NotRequired[float]
    threshold: NotRequired[float]

Candidate: TypeAlias = Union['MinCandidate', 'LeanCandidate', 'FullCandidate']
Recommendation: TypeAlias = Union['MinRecommendation', 'LeanRecommendation', 'FullRecommendation']
RecommendationJob: TypeAlias = Union['QueuedRecommendationJob', 'RunningRecommendationJob', 'CompletedRecommendationJob', 'FailedRecommendationJob']
ExecutionResult: TypeAlias = Union['ExecutionSuccess', 'ExecutionOverflow', 'ExecutionFailure']
class Health(TypedDict):
    ready: bool
    routable: bool

class JudgePanelMember(TypedDict):
    model: str | None
    rationale: str | None
    score: NotRequired[float]
    label: NotRequired[str]
    value: NotRequired[float]

class ProbeJudgment(TypedDict):
    facet: str | None
    verdict: str | None
    score: float | None
    rationale: str | None
    panel: list[JudgePanelMember] | None

class Probe(TypedDict):
    probe_id: int | str | None
    similarity: float
    task_text: str | None
    adapted_input: str | None
    score: float
    redacted: bool | None
    output_chars: int | None
    truncated: bool
    created_at: str | None
    judges: list[ProbeJudgment]
    raw_output: str | None

class ProbeEvidence(TypedDict):
    n_real: int
    n_near: int
    near_mean: float
    dist: list[float]
    probes: list[Probe]

class EvidenceTeaser(TypedDict):
    task_text: str | None
    verdict: str | None
    score: float
    similarity: float
    n_real: int

class FacetBreakdown(TypedDict):
    name: str
    kano: Literal['must_be', 'performance', 'attractive']
    weight: float
    threshold: float
    raw: float
    contribution: float

class PriceEstimate(TypedDict):
    amount: NotRequired[float | None]
    per_query_usd: float
    currency: NotRequired[str]
    confidence: NotRequired[str]
    selected_plan: NotRequired[str | None]
    held: bool
    estimated: NotRequired[bool]
    cost_unknown: bool
    breakdown: NotRequired[list[PricePlan]]
    note: NotRequired[str]

class CallingSummary(TypedDict):
    usability: NotRequired[str]
    auth_method: NotRequired[str]
    api_type: NotRequired[str | None]
    connected: NotRequired[bool]
    free: NotRequired[bool]
    how: NotRequired[str]
    signup_url: NotRequired[str | None]

class CallingDescriptor(TypedDict):
    tool_id: NotRequired[str]
    coordinator_class: NotRequired[bool]
    executable: NotRequired[bool]
    endpoint: NotRequired[JsonObject]
    adapter: NotRequired[JsonObject]
    auth: NotRequired[JsonObject]
    summary: NotRequired[CallingSummary]
    base_tool: NotRequired[str]
    adapter_mode: NotRequired[Any]
    connect: NotRequired[JsonObject]
    mcp_install: NotRequired[JsonObject]

class OutcomeHealth(TypedDict):
    level: Literal['green', 'amber', 'red']
    label: str

class FacetFormField(TypedDict):
    name: NotRequired[str]
    optional: NotRequired[bool]
    default: NotRequired[str]
    spread: NotRequired[float]
    divergence_over_shortlist: NotRequired[dict[str, float]]
    note: NotRequired[str]

class FacetForm(TypedDict):
    reason: NotRequired[str]
    decidable: NotRequired[bool]
    decide_margin: NotRequired[float]
    shortlist: NotRequired[list[str]]
    fields: NotRequired[list[FacetFormField]]

class ActiveFacet(TypedDict):
    name: NotRequired[str]
    kano: NotRequired[str]
    weight: NotRequired[float]
    threshold: NotRequired[float]
    scope: NotRequired[str]
    kind: NotRequired[str]
    source: NotRequired[str]

class FacetState(TypedDict):
    active: NotRequired[list[ActiveFacet]]
    query_specific_available: NotRequired[list[str]]
    hint: NotRequired[str]

class FacetOption(TypedDict):
    name: NotRequired[str]
    label: NotRequired[str]
    description: NotRequired[str]
    text_source: NotRequired[str]
    scope: NotRequired[str]
    kind: NotRequired[str]
    spread: NotRequired[float | None]
    divergent: NotRequired[bool]
    on: NotRequired[bool]
    kano: NotRequired[str]
    weight: NotRequired[float]
    default_weight: NotRequired[float]
    threshold: NotRequired[float]
    values: NotRequired[dict[str, float]]

class Description(TypedDict):
    tool_id: str
    name: str | None
    about: NotRequired[JsonObject]
    price: NotRequired[PriceEstimate]
    facets: NotRequired[list[FacetBreakdown]]
    evidence: NotRequired[ProbeEvidence | None]
    error: NotRequired[str]
    note: NotRequired[str]

class FullCandidate(TypedDict):
    tool_id: str
    name: str
    reason: str
    calling: CallingDescriptor | None
    capability: float | None
    variant: str | None
    capabilities: list[str]
    description: str
    kind: str
    endpoint: JsonObject
    band: float | None
    cap_lcb: float | None
    rank: float | None
    price: PriceEstimate | None
    unrated: NotRequired[bool]
    field_health: NotRequired[str]
    outcome_health: NotRequired[OutcomeHealth]
    facets: list[FacetBreakdown]
    evidence: ProbeEvidence | None
    evidence_teaser: NotRequired[EvidenceTeaser]

class LeanCandidate(TypedDict):
    tool_id: str
    name: str
    reason: str
    calling: CallingDescriptor | None
    capability: float | None
    variant: str | None
    capabilities: list[str]
    description: str
    kind: str
    endpoint: JsonObject
    band: float | None
    cap_lcb: float | None
    rank: float | None
    price: PriceEstimate | None
    unrated: NotRequired[bool]
    field_health: NotRequired[str]
    outcome_health: NotRequired[OutcomeHealth]

class MinCandidate(TypedDict):
    id: str
    name: str
    why: str
    price: str
    use: str
    confidence: NotRequired[str]

class LeanRecommendation(TypedDict):
    session_id: str | None
    kind: Literal['ranked', 'advisory', 'no_tool']
    status: Literal['ok', 'needs_facets']
    best: LeanCandidate | None
    runner_ups: list[LeanCandidate]
    calling: CallingDescriptor | None
    provisional: bool
    disclaimer: str
    facet_form: FacetForm | None
    decidable: bool
    decide_margin: float
    not_checked: list[str]
    flags: RoutingFlags
    facet_state: FacetState | None
    coverage: NotRequired[JsonObject]
    input_truncated: NotRequired[JsonObject]

class FullRecommendation(TypedDict):
    session_id: str | None
    kind: Literal['ranked', 'advisory', 'no_tool']
    status: Literal['ok', 'needs_facets']
    best: FullCandidate | None
    runner_ups: list[FullCandidate]
    calling: CallingDescriptor | None
    provisional: bool
    disclaimer: str
    facet_form: FacetForm | None
    decidable: bool
    decide_margin: float
    not_checked: list[str]
    flags: RoutingFlags
    facet_state: FacetState | None
    coverage: NotRequired[JsonObject]
    input_truncated: NotRequired[JsonObject]
    facet_options: list[FacetOption]

class MinRecommendation(TypedDict):
    session_id: str | None
    kind: Literal['ranked', 'advisory', 'no_tool']
    status: Literal['ok', 'needs_facets']
    coverage: NotRequired[JsonObject]
    not_checked: NotRequired[list[str]]
    input_truncated: NotRequired[JsonObject]
    best: MinCandidate | None
    alts: list[MinCandidate]
    verdict: str | None
    refine: list[str]
    act: str
    connect: NotRequired[JsonObject]
    consider: NotRequired[list[JsonObject]]
    preferred: NotRequired[PreferredDecision]

class LeanRecommendRequest(TypedDict):
    query: str
    facets: NotRequired[dict[str, Facet] | None]
    context: NotRequired[JsonObject | None]
    project_id: NotRequired[str | None]
    detail: NotRequired[Literal['lean'] | None]
    format: NotRequired[Literal['json'] | None]
    n_runner_ups: NotRequired[int | None]
    evidence_k: NotRequired[int | None]
    caller: NotRequired[Any]

class FullRecommendRequest(TypedDict):
    query: str
    facets: NotRequired[dict[str, Facet] | None]
    context: NotRequired[JsonObject | None]
    project_id: NotRequired[str | None]
    detail: Literal['full']
    format: NotRequired[Literal['json'] | None]
    n_runner_ups: NotRequired[int | None]
    evidence_k: NotRequired[int | None]
    caller: NotRequired[Any]

class MinRecommendRequest(TypedDict):
    query: str
    facets: NotRequired[dict[str, Facet] | None]
    context: NotRequired[JsonObject | None]
    project_id: NotRequired[str | None]
    detail: Literal['min']
    format: NotRequired[Literal['json'] | None]
    n_runner_ups: NotRequired[int | None]
    evidence_k: NotRequired[int | None]
    caller: NotRequired[Any]

class TextRecommendRequest(TypedDict):
    query: str
    facets: NotRequired[dict[str, Facet] | None]
    context: NotRequired[JsonObject | None]
    project_id: NotRequired[str | None]
    detail: NotRequired[Literal['min', 'lean', 'full'] | None]
    format: Literal['text']
    n_runner_ups: NotRequired[int | None]
    evidence_k: NotRequired[int | None]
    caller: NotRequired[Any]

class User(TypedDict):
    id: str
    email: str | None
    display_name: str | None
    tier: str
    status: str
    verified: bool

class AuthSession(TypedDict):
    ok: Literal[True]
    user: User | None
    api_key: str
    recovery_codes: NotRequired[list[str]]

class MessageResponse(TypedDict):
    ok: bool
    message: str

class RegistrationResponse(TypedDict):
    ok: Literal[True]
    verification_required: bool
    email: str
    message: str

class CreatedToken(TypedDict):
    ok: Literal[True]
    api_key: str
    label: str

class Token(TypedDict):
    id: NotRequired[str]
    label: NotRequired[str | None]
    created_at: NotRequired[str | None]
    last_used_at: NotRequired[str | None]
    kind: NotRequired[str]
    client_name: NotRequired[str]
    scopes: NotRequired[list[str]]

class TokenList(TypedDict):
    tokens: list[Token]

class RevokedResponse(TypedDict):
    revoked: bool

class DeletedResponse(TypedDict):
    deleted: bool
    reason: NotRequired[str]

class Credential(TypedDict):
    credential_id: str | None
    tool_id: str | None
    label: str | None
    connected_at: str | None
    last_test_at: str | None
    last_test_status: str | None
    name: NotRequired[str]

class CredentialResult(TypedDict):
    credential_id: NotRequired[str | None]
    tool_id: NotRequired[str | None]
    label: NotRequired[str | None]
    connected_at: NotRequired[str | None]
    last_test_at: NotRequired[str | None]
    last_test_status: NotRequired[str | None]
    name: NotRequired[str]
    ok: bool
    status: NotRequired[str]
    reason: NotRequired[str]

class CredentialList(TypedDict):
    credentials: list[Credential]

class OnboardInfo(TypedDict):
    tool_id: str
    name: str | None
    auth_method: str
    requires_key: bool
    connected: bool
    summary: CallingSummary | None
    connect: JsonObject | None

class Preferences(TypedDict):
    user: dict[str, Facet]
    project_id: NotRequired[str]
    project: NotRequired[dict[str, Facet]]
    effective: dict[str, Facet]

class StoredPreferences(TypedDict):
    stored: dict[str, Facet]
    project_id: str | None
    effective: dict[str, Facet]

class Region(TypedDict):
    id: str
    label: str

class PrivateTool(TypedDict):
    tool_id: str
    name: str
    description: str
    triggers: list[str]
    anchors: list[str]
    stance: str
    project_id: str
    regions: NotRequired[list[Region]]

class PrivateToolList(TypedDict):
    tools: list[PrivateTool]
    anchors_available: bool

class DeclaredPrivateTool(TypedDict):
    declared: PrivateTool
    triggers: list[str]
    regions: list[Region]

class UpdatedPrivateTool(TypedDict):
    updated: PrivateTool

class RegionSuggestion(TypedDict):
    id: str
    label: str
    similarity: float
    group: str
    in_taxonomy: bool

class RegionSuggestions(TypedDict):
    suggestions: list[RegionSuggestion]

class PreferredTool(TypedDict):
    tool_id: str
    margin: float
    note: str
    project_id: str
    name: NotRequired[str]
    in_catalog: NotRequired[bool]

class PreferredToolList(TypedDict):
    tools: list[PreferredTool]

class ToolIdentity(TypedDict):
    id: str
    name: str | None

class PreferredToolResult(TypedDict):
    preferred: PreferredTool
    tool: ToolIdentity

class UpdatedPreferredTool(TypedDict):
    updated: PreferredTool

class FacetCatalogEntry(TypedDict):
    name: str
    label: str
    description: str
    scope: str
    kind: str
    constraint: bool
    spine: bool
    default_kano: str
    default_weight: float
    default_threshold: float

class FacetCatalog(TypedDict):
    ready: bool
    facets: list[FacetCatalogEntry]

class QueueLane(TypedDict):
    queued: int
    avg_ms: float
    completed: int

class RunningJob(TypedDict):
    lane: str

class QueueStatus(TypedDict):
    concurrency: int
    queued_total: int
    running: list[RunningJob]
    lanes: dict[str, QueueLane]

class AcceptedOutcome(TypedDict):
    score: NotRequired[str | None]
    reason: NotRequired[str | None]
    counts_as_quality: NotRequired[bool]
    quality: NotRequired[float | None]
    comment: NotRequired[bool]
    human_survey: NotRequired[bool]

class OutcomeReport(TypedDict):
    ok: Literal[True]
    session_id: str
    tool_id: str | None
    accepted: AcceptedOutcome
    field_probe: FieldProbeResult | None
    triggers_raised: list[str]
    score_moved: Literal[False]
    private: NotRequired[bool]

class NarrativeResult(TypedDict):
    ok: Literal[True]
    id: int
    stored: Literal['db', 'memory']

class OverflowResult(TypedDict):
    ref: str
    bytes: int
    content_type: str
    preview: str
    resource_url: str
    note: str

class ResultShape(TypedDict):
    type: str
    keys: NotRequired[list[str]]
    length: NotRequired[int]

ReadResult: TypeAlias = Union['ResultSlice', 'ResultSearch', 'ResultJsonPath', 'ResultReadError']
class BetaApplication(TypedDict):
    ok: Literal[True]
    persisted: bool
    id: NotRequired[str]
    track: str
    position: NotRequired[int]

class CollectorRule(TypedDict):
    id: NotRequired[str]
    kind: NotRequired[str]
    path: NotRequired[str]
    var: NotRequired[str]
    tail: NotRequired[int]
    out: NotRequired[dict[str, str]]
    set: NotRequired[JsonObject]
    where: NotRequired[JsonObject]
    table: NotRequired[str]
    order: NotRequired[str]

class AgentCollector(TypedDict):
    match: dict[str, list[str]]
    probes: list[CollectorRule]

class CallerCollectors(TypedDict):
    version: int
    agents: dict[str, AgentCollector]

class ConsoleResult(TypedDict):
    view: str
    tools: NotRequired[list[JsonObject]]
    connections: NotRequired[int | list[Credential]]
    events: NotRequired[list[JsonObject]]
    categories: NotRequired[list[JsonObject]]
    preferred: NotRequired[list[PreferredTool]]
    present: NotRequired[bool]
    model: NotRequired[str]
    n_tools: NotRequired[int]
    n_facets: NotRequired[int]
    stats: NotRequired[JsonObject]
    recent: NotRequired[list[JsonObject]]
    total_calls: NotRequired[int]
    routed: NotRequired[int]
    passed_through: NotRequired[int]
    verdicts: NotRequired[dict[str, int]]
    top_tools: NotRequired[list[list[str | int]]]
    executed: NotRequired[int]
    outcomes: NotRequired[dict[str, int]]
    avg_latency_ms: NotRequired[float | None]

class QueuedRecommendationJob(TypedDict):
    job: str
    state: Literal['queued']
    lane: str
    position: int | None
    lane_position: NotRequired[int | None]
    eta_ms: int

class RunningRecommendationJob(TypedDict):
    job: str
    state: Literal['running']
    lane: str
    position: int | None
    lane_position: NotRequired[int | None]
    eta_ms: int

class CompletedRecommendationJob(TypedDict):
    job: str
    state: Literal['done']
    lane: str
    position: int | None
    lane_position: NotRequired[int | None]
    eta_ms: int
    result: Recommendation

class FailedRecommendationJob(TypedDict):
    job: str
    state: Literal['error']
    lane: str
    position: int | None
    lane_position: NotRequired[int | None]
    eta_ms: int
    error: str

class ExecutionSuccess(TypedDict):
    ok: Literal[True]
    tool_id: str
    result: Any
    error: NotRequired[str | None]
    latency_ms: NotRequired[float]
    query: NotRequired[str]
    adapted_query: NotRequired[str]
    message: NotRequired[str]
    status: NotRequired[str]
    credentials: NotRequired[list[str]]
    connect: NotRequired[JsonObject]

class ExecutionOverflow(TypedDict):
    ok: Literal[True]
    tool_id: str
    error: NotRequired[str | None]
    latency_ms: NotRequired[float]
    overflow: OverflowResult
    query: NotRequired[str]
    adapted_query: NotRequired[str]
    message: NotRequired[str]
    status: NotRequired[str]
    credentials: NotRequired[list[str]]
    connect: NotRequired[JsonObject]

class ExecutionFailure(TypedDict):
    ok: Literal[False]
    tool_id: str
    result: NotRequired[Any]
    error: str | None
    latency_ms: NotRequired[float]
    overflow: NotRequired[OverflowResult]
    query: NotRequired[str]
    adapted_query: NotRequired[str]
    message: NotRequired[str]
    status: NotRequired[str]
    credentials: NotRequired[list[str]]
    connect: NotRequired[JsonObject]

class ResultSlice(TypedDict):
    offset: int
    limit: int
    total_lines: int
    content: str
    truncated: bool
    ok: Literal[True]
    op: Literal['slice']

class ResultSearch(TypedDict):
    count: int
    matches_json: str
    truncated: bool
    ok: Literal[True]
    op: Literal['search']

class ResultJsonPath(TypedDict):
    shape: ResultShape
    value_json: str
    truncated: bool
    ok: Literal[True]
    op: Literal['json_path']

class ResultReadError(TypedDict):
    ok: Literal[False]
    error: str
    message: str

class RecommendationSubmission(TypedDict):
    job: str
    state: Literal['queued', 'running', 'done', 'error']
    lane: str
    position: int | None
    lane_position: NotRequired[int | None]
    eta_ms: int
    error: NotRequired[str]

class FieldProbeResult(TypedDict):
    ok: bool
    id: NotRequired[int]
    stored: NotRequired[str]
    error: NotRequired[str]

class PricePlan(TypedDict):
    plan_id: str | None
    kind: str | None
    plan_group: str | None
    effective_usd: float
    held: bool
    currency: str
    confidence: str
    overridden: bool

class PreferredDecision(TypedDict):
    tool_id: NotRequired[str]
    name: NotRequired[str]
    honoured: NotRequired[bool]
    acceptable: NotRequired[bool]
    gap: NotRequired[float]
    margin: NotRequired[float]
    cap_lcb: NotRequired[float]
    threshold: NotRequired[float]
    best: NotRequired[str]
    best_name: NotRequired[str]

class ExcludedTools(TypedDict):
    count: int
    facets: list[str]
    tool_ids: list[str]

class NativeBaseline(TypedDict):
    score: float
    source: str
    tau: float
    self: bool

class OwnToolDecision(TypedDict):
    tool_id: NotRequired[str]
    trigger: NotRequired[str]
    match: NotRequired[float]
    stance: NotRequired[str]
    own_quality_mean: NotRequired[float | None]
    outcomes: NotRequired[int]

class RoutingFlags(TypedDict):
    short_circuit: NotRequired[bool]
    learned_preset: NotRequired[str]
    match_similarity: NotRequired[float]
    digest_skipped: NotRequired[bool]
    digest_applied: NotRequired[bool]
    excluded: NotRequired[ExcludedTools]
    verdict: NotRequired[str]
    preferred: NotRequired[PreferredDecision]
    own: NotRequired[OwnToolDecision]
    consider: NotRequired[list[JsonObject]]
    baseline: NotRequired[NativeBaseline]


class TestCredentialQuery(TypedDict):
    tool_id: str

class GetPreferencesQuery(TypedDict):
    project_id: NotRequired[str | None]

class ClearPreferencesQuery(TypedDict):
    project_id: NotRequired[str | None]

class ListPrivateToolsQuery(TypedDict):
    project_id: NotRequired[str | None]

class DeletePrivateToolQuery(TypedDict):
    project_id: NotRequired[str | None]

class SetPrivateStanceQuery(TypedDict):
    stance: str
    project_id: NotRequired[str | None]

class ListPreferredToolsQuery(TypedDict):
    project_id: NotRequired[str | None]

class UnpreferToolQuery(TypedDict):
    project_id: NotRequired[str | None]

class ConsoleQuery(TypedDict):
    view: NotRequired[str]
    format: NotRequired[str]
    limit: NotRequired[int]
    project_id: NotRequired[str | None]

class ConsoleViewQuery(TypedDict):
    limit: NotRequired[int]
    project_id: NotRequired[str | None]
