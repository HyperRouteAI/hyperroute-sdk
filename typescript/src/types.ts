export type JsonObject = Record<string, unknown>;

export interface RecommendRequest {
  query: string;
  facets?: Record<string, Facet> | null;
  context?: JsonObject | null;
  project_id?: string | null;
  detail?: "min" | "lean" | "full" | null;
  format?: "json" | "text" | null;
  n_runner_ups?: number | null;
  evidence_k?: number | null;
  caller?: unknown;
}

export interface DescribeRequest {
  tool_id: string;
  sections?: Array<string> | null;
  session_id?: string | null;
  query?: string | null;
  context?: JsonObject | null;
  facets?: JsonObject | null;
  evidence_k?: number | null;
}

export interface ExecuteRequest {
  tool_id: string;
  query: string;
  session_id?: string | null;
  caller?: unknown;
}

export interface ReportOutcomeRequest {
  session_id?: string | null;
  run_id?: string | null;
  tool_id?: string | null;
  score?: string | null;
  reason?: string | null;
  comment?: string | null;
  status?: string | null;
  completed?: boolean | null;
  coordinator_signal?: JsonObject | null;
  human_survey?: JsonObject | null;
  time_to_outcome_ms?: number | null;
  downstream_action?: string | null;
  dispute?: boolean | null;
  caller?: unknown;
}

export interface NarrativeReport {
  session_id?: string | null;
  text: string;
  author?: string;
  steps?: Array<JsonObject> | null;
}

export interface OnboardRequest {
  tool_id: string;
  api_key: string;
  label?: string | null;
}

export interface ConnectRequest {
  tool_id: string;
  api_key: string;
  label?: string | null;
}

export interface PreferencesRequest {
  facets: JsonObject;
  project_id?: string | null;
}

export interface PrivateToolRequest {
  name: string;
  description?: string;
  triggers?: Array<string>;
  anchors?: Array<string>;
  stance?: string;
  project_id?: string | null;
}

export interface PrivateToolPatch {
  name?: string | null;
  description?: string | null;
  triggers?: Array<string> | null;
  anchors?: Array<string> | null;
  stance?: string | null;
}

export interface PreferredToolRequest {
  tool: string;
  margin?: number | null;
  note?: string;
  project_id?: string | null;
}

export interface PreferredToolPatch {
  margin?: number | null;
  note?: string | null;
}

export interface ResultReadRequest {
  op?: string;
  offset?: number;
  limit?: number;
  path?: Array<unknown> | null;
  query?: string | null;
}

export interface RegisterRequest {
  email: string;
  password: string;
  display_name?: string | null;
}

export interface VerifyRequest {
  email: string;
  code: string;
}

export interface EmailRequest {
  email: string;
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface CodeLoginRequest {
  email: string;
  code: string;
}

export interface ResetPasswordRequest {
  email: string;
  code: string;
  new_password: string;
}

export interface RecoverRequest {
  email: string;
  recovery_code: string;
  new_password?: string | null;
}

export interface TokenCreateRequest {
  label?: string | null;
}

export interface InviteAcceptRequest {
  token: string;
  email?: string | null;
  password: string;
}

export interface BetaApplicationRequest {
  name: string;
  email: string;
  company?: string | null;
  role?: string | null;
  purpose?: string | null;
  frameworks?: Array<string> | null;
  other_tools?: Array<string> | null;
  track?: string | null;
  survey?: JsonObject | null;
}

export interface Facet {
  kano?: "must_be" | "performance" | "attractive";
  weight?: number;
  threshold?: number;
}

export type Candidate = MinCandidate | LeanCandidate | FullCandidate;
export type Recommendation = MinRecommendation | LeanRecommendation | FullRecommendation;
export type RecommendationJob = QueuedRecommendationJob | RunningRecommendationJob | CompletedRecommendationJob | FailedRecommendationJob;
export type ExecutionResult = ExecutionSuccess | ExecutionOverflow | ExecutionFailure;
export interface Health {
  ready: boolean;
  routable: boolean;
}

export interface JudgePanelMember {
  model: string | null;
  rationale: string | null;
  score?: number;
  label?: string;
  value?: number;
}

export interface ProbeJudgment {
  facet: string | null;
  verdict: string | null;
  score: number | null;
  rationale: string | null;
  panel: Array<JudgePanelMember> | null;
}

export interface Probe {
  probe_id: number | string | null;
  similarity: number;
  task_text: string | null;
  adapted_input: string | null;
  score: number;
  redacted: boolean | null;
  output_chars: number | null;
  truncated: boolean;
  created_at: string | null;
  judges: Array<ProbeJudgment>;
  raw_output: string | null;
}

export interface ProbeEvidence {
  n_real: number;
  n_near: number;
  near_mean: number;
  dist: Array<number>;
  probes: Array<Probe>;
}

export interface EvidenceTeaser {
  task_text: string | null;
  verdict: string | null;
  score: number;
  similarity: number;
  n_real: number;
}

export interface FacetBreakdown {
  name: string;
  kano: "must_be" | "performance" | "attractive";
  weight: number;
  threshold: number;
  raw: number;
  contribution: number;
}

export interface PriceEstimate {
  amount?: number | null;
  per_query_usd: number;
  currency?: string;
  confidence?: string;
  selected_plan?: string | null;
  held: boolean;
  estimated?: boolean;
  cost_unknown: boolean;
  breakdown?: Array<PricePlan>;
  note?: string;
}

export interface CallingSummary {
  usability?: string;
  auth_method?: string;
  api_type?: string | null;
  connected?: boolean;
  free?: boolean;
  how?: string;
  signup_url?: string | null;
}

export interface CallingDescriptor {
  tool_id?: string;
  coordinator_class?: boolean;
  executable?: boolean;
  endpoint?: JsonObject;
  adapter?: JsonObject;
  auth?: JsonObject;
  summary?: CallingSummary;
  base_tool?: string;
  adapter_mode?: unknown;
  connect?: JsonObject;
  mcp_install?: JsonObject;
}

export interface OutcomeHealth {
  level: "green" | "amber" | "red";
  label: string;
}

export interface FacetFormField {
  name?: string;
  optional?: boolean;
  default?: string;
  spread?: number;
  divergence_over_shortlist?: Record<string, number>;
  note?: string;
}

export interface FacetForm {
  reason?: string;
  decidable?: boolean;
  decide_margin?: number;
  shortlist?: Array<string>;
  fields?: Array<FacetFormField>;
}

export interface ActiveFacet {
  name?: string;
  kano?: string;
  weight?: number;
  threshold?: number;
  scope?: string;
  kind?: string;
  source?: string;
}

export interface FacetState {
  active?: Array<ActiveFacet>;
  query_specific_available?: Array<string>;
  hint?: string;
}

export interface FacetOption {
  name?: string;
  label?: string;
  description?: string;
  text_source?: string;
  scope?: string;
  kind?: string;
  spread?: number | null;
  divergent?: boolean;
  on?: boolean;
  kano?: string;
  weight?: number;
  default_weight?: number;
  threshold?: number;
  values?: Record<string, number>;
}

export interface Description {
  tool_id: string;
  name: string | null;
  about?: JsonObject;
  price?: PriceEstimate;
  facets?: Array<FacetBreakdown>;
  evidence?: ProbeEvidence | null;
  error?: string;
  note?: string;
}

export interface FullCandidate {
  tool_id: string;
  name: string;
  reason: string;
  calling: CallingDescriptor | null;
  capability: number | null;
  variant: string | null;
  capabilities: Array<string>;
  description: string;
  kind: string;
  endpoint: JsonObject;
  band: number | null;
  cap_lcb: number | null;
  rank: number | null;
  price: PriceEstimate | null;
  unrated?: boolean;
  field_health?: string;
  outcome_health?: OutcomeHealth;
  facets: Array<FacetBreakdown>;
  evidence: ProbeEvidence | null;
  evidence_teaser?: EvidenceTeaser;
}

export interface LeanCandidate {
  tool_id: string;
  name: string;
  reason: string;
  calling: CallingDescriptor | null;
  capability: number | null;
  variant: string | null;
  capabilities: Array<string>;
  description: string;
  kind: string;
  endpoint: JsonObject;
  band: number | null;
  cap_lcb: number | null;
  rank: number | null;
  price: PriceEstimate | null;
  unrated?: boolean;
  field_health?: string;
  outcome_health?: OutcomeHealth;
}

export interface MinCandidate {
  id: string;
  name: string;
  why: string;
  price: string;
  use: string;
  confidence?: string;
}

export interface LeanRecommendation {
  session_id: string | null;
  kind: "ranked" | "advisory" | "no_tool";
  status: "ok" | "needs_facets";
  best: LeanCandidate | null;
  runner_ups: Array<LeanCandidate>;
  calling: CallingDescriptor | null;
  provisional: boolean;
  disclaimer: string;
  facet_form: FacetForm | null;
  decidable: boolean;
  decide_margin: number;
  not_checked: Array<string>;
  flags: RoutingFlags;
  facet_state: FacetState | null;
  coverage?: JsonObject;
  input_truncated?: JsonObject;
}

export interface FullRecommendation {
  session_id: string | null;
  kind: "ranked" | "advisory" | "no_tool";
  status: "ok" | "needs_facets";
  best: FullCandidate | null;
  runner_ups: Array<FullCandidate>;
  calling: CallingDescriptor | null;
  provisional: boolean;
  disclaimer: string;
  facet_form: FacetForm | null;
  decidable: boolean;
  decide_margin: number;
  not_checked: Array<string>;
  flags: RoutingFlags;
  facet_state: FacetState | null;
  coverage?: JsonObject;
  input_truncated?: JsonObject;
  facet_options: Array<FacetOption>;
}

export interface MinRecommendation {
  session_id: string | null;
  kind: "ranked" | "advisory" | "no_tool";
  status: "ok" | "needs_facets";
  coverage?: JsonObject;
  not_checked?: Array<string>;
  input_truncated?: JsonObject;
  best: MinCandidate | null;
  alts: Array<MinCandidate>;
  verdict: string | null;
  refine: Array<string>;
  act: string;
  connect?: JsonObject;
  consider?: Array<JsonObject>;
  preferred?: PreferredDecision;
}

export interface LeanRecommendRequest {
  query: string;
  facets?: Record<string, Facet> | null;
  context?: JsonObject | null;
  project_id?: string | null;
  detail?: "lean" | null;
  format?: "json" | null;
  n_runner_ups?: number | null;
  evidence_k?: number | null;
  caller?: unknown;
}

export interface FullRecommendRequest {
  query: string;
  facets?: Record<string, Facet> | null;
  context?: JsonObject | null;
  project_id?: string | null;
  detail: "full";
  format?: "json" | null;
  n_runner_ups?: number | null;
  evidence_k?: number | null;
  caller?: unknown;
}

export interface MinRecommendRequest {
  query: string;
  facets?: Record<string, Facet> | null;
  context?: JsonObject | null;
  project_id?: string | null;
  detail: "min";
  format?: "json" | null;
  n_runner_ups?: number | null;
  evidence_k?: number | null;
  caller?: unknown;
}

export interface TextRecommendRequest {
  query: string;
  facets?: Record<string, Facet> | null;
  context?: JsonObject | null;
  project_id?: string | null;
  detail?: "min" | "lean" | "full" | null;
  format: "text";
  n_runner_ups?: number | null;
  evidence_k?: number | null;
  caller?: unknown;
}

export interface User {
  id: string;
  email: string | null;
  display_name: string | null;
  tier: string;
  status: string;
  verified: boolean;
}

export interface AuthSession {
  ok: true;
  user: User | null;
  api_key: string;
  recovery_codes?: Array<string>;
}

export interface MessageResponse {
  ok: boolean;
  message: string;
}

export interface RegistrationResponse {
  ok: true;
  verification_required: boolean;
  email: string;
  message: string;
}

export interface CreatedToken {
  ok: true;
  api_key: string;
  label: string;
}

export interface Token {
  id?: string;
  label?: string | null;
  created_at?: string | null;
  last_used_at?: string | null;
  kind?: string;
  client_name?: string;
  scopes?: Array<string>;
}

export interface TokenList {
  tokens: Array<Token>;
}

export interface RevokedResponse {
  revoked: boolean;
}

export interface DeletedResponse {
  deleted: boolean;
  reason?: string;
}

export interface Credential {
  credential_id: string | null;
  tool_id: string | null;
  label: string | null;
  connected_at: string | null;
  last_test_at: string | null;
  last_test_status: string | null;
  name?: string;
}

export interface CredentialResult {
  credential_id?: string | null;
  tool_id?: string | null;
  label?: string | null;
  connected_at?: string | null;
  last_test_at?: string | null;
  last_test_status?: string | null;
  name?: string;
  ok: boolean;
  status?: string;
  reason?: string;
}

export interface CredentialList {
  credentials: Array<Credential>;
}

export interface OnboardInfo {
  tool_id: string;
  name: string | null;
  auth_method: string;
  requires_key: boolean;
  connected: boolean;
  summary: CallingSummary | null;
  connect: JsonObject | null;
}

export interface Preferences {
  user: Record<string, Facet>;
  project_id?: string;
  project?: Record<string, Facet>;
  effective: Record<string, Facet>;
}

export interface StoredPreferences {
  stored: Record<string, Facet>;
  project_id: string | null;
  effective: Record<string, Facet>;
}

export interface Region {
  id: string;
  label: string;
}

export interface PrivateTool {
  tool_id: string;
  name: string;
  description: string;
  triggers: Array<string>;
  anchors: Array<string>;
  stance: string;
  project_id: string;
  regions?: Array<Region>;
}

export interface PrivateToolList {
  tools: Array<PrivateTool>;
  anchors_available: boolean;
}

export interface DeclaredPrivateTool {
  declared: PrivateTool;
  triggers: Array<string>;
  regions: Array<Region>;
}

export interface UpdatedPrivateTool {
  updated: PrivateTool;
}

export interface RegionSuggestion {
  id: string;
  label: string;
  similarity: number;
  group: string;
  in_taxonomy: boolean;
}

export interface RegionSuggestions {
  suggestions: Array<RegionSuggestion>;
}

export interface PreferredTool {
  tool_id: string;
  margin: number;
  note: string;
  project_id: string;
  name?: string;
  in_catalog?: boolean;
}

export interface PreferredToolList {
  tools: Array<PreferredTool>;
}

export interface ToolIdentity {
  id: string;
  name: string | null;
}

export interface PreferredToolResult {
  preferred: PreferredTool;
  tool: ToolIdentity;
}

export interface UpdatedPreferredTool {
  updated: PreferredTool;
}

export interface FacetCatalogEntry {
  name: string;
  label: string;
  description: string;
  scope: string;
  kind: string;
  constraint: boolean;
  spine: boolean;
  default_kano: string;
  default_weight: number;
  default_threshold: number;
}

export interface FacetCatalog {
  ready: boolean;
  facets: Array<FacetCatalogEntry>;
}

export interface QueueLane {
  queued: number;
  avg_ms: number;
  completed: number;
}

export interface RunningJob {
  lane: string;
}

export interface QueueStatus {
  concurrency: number;
  queued_total: number;
  running: Array<RunningJob>;
  lanes: Record<string, QueueLane>;
}

export interface AcceptedOutcome {
  score?: string | null;
  reason?: string | null;
  counts_as_quality?: boolean;
  quality?: number | null;
  comment?: boolean;
  human_survey?: boolean;
}

export interface OutcomeReport {
  ok: true;
  session_id: string;
  tool_id: string | null;
  accepted: AcceptedOutcome;
  field_probe: FieldProbeResult | null;
  triggers_raised: Array<string>;
  score_moved: false;
  private?: boolean;
}

export interface NarrativeResult {
  ok: true;
  id: number;
  stored: "db" | "memory";
}

export interface OverflowResult {
  ref: string;
  bytes: number;
  content_type: string;
  preview: string;
  resource_url: string;
  note: string;
}

export interface ResultShape {
  type: string;
  keys?: Array<string>;
  length?: number;
}

export type ReadResult = ResultSlice | ResultSearch | ResultJsonPath | ResultReadError;
export interface BetaApplication {
  ok: true;
  persisted: boolean;
  id?: string;
  track: string;
  position?: number;
}

export interface CollectorRule {
  id?: string;
  kind?: string;
  path?: string;
  var?: string;
  tail?: number;
  out?: Record<string, string>;
  set?: JsonObject;
  where?: JsonObject;
  table?: string;
  order?: string;
}

export interface AgentCollector {
  match: Record<string, Array<string>>;
  probes: Array<CollectorRule>;
}

export interface CallerCollectors {
  version: number;
  agents: Record<string, AgentCollector>;
}

export interface ConsoleResult {
  view: string;
  tools?: Array<JsonObject>;
  connections?: number | Array<Credential>;
  events?: Array<JsonObject>;
  categories?: Array<JsonObject>;
  preferred?: Array<PreferredTool>;
  present?: boolean;
  model?: string;
  n_tools?: number;
  n_facets?: number;
  stats?: JsonObject;
  recent?: Array<JsonObject>;
  total_calls?: number;
  routed?: number;
  passed_through?: number;
  verdicts?: Record<string, number>;
  top_tools?: Array<Array<string | number>>;
  executed?: number;
  outcomes?: Record<string, number>;
  avg_latency_ms?: number | null;
}

export interface QueuedRecommendationJob {
  job: string;
  state: "queued";
  lane: string;
  position: number | null;
  lane_position?: number | null;
  eta_ms: number;
}

export interface RunningRecommendationJob {
  job: string;
  state: "running";
  lane: string;
  position: number | null;
  lane_position?: number | null;
  eta_ms: number;
}

export interface CompletedRecommendationJob {
  job: string;
  state: "done";
  lane: string;
  position: number | null;
  lane_position?: number | null;
  eta_ms: number;
  result: Recommendation;
}

export interface FailedRecommendationJob {
  job: string;
  state: "error";
  lane: string;
  position: number | null;
  lane_position?: number | null;
  eta_ms: number;
  error: string;
}

export interface ExecutionSuccess {
  ok: true;
  tool_id: string;
  result: unknown;
  error?: string | null;
  latency_ms?: number;
  query?: string;
  adapted_query?: string;
  message?: string;
  status?: string;
  credentials?: Array<string>;
  connect?: JsonObject;
}

export interface ExecutionOverflow {
  ok: true;
  tool_id: string;
  error?: string | null;
  latency_ms?: number;
  overflow: OverflowResult;
  query?: string;
  adapted_query?: string;
  message?: string;
  status?: string;
  credentials?: Array<string>;
  connect?: JsonObject;
}

export interface ExecutionFailure {
  ok: false;
  tool_id: string;
  result?: unknown;
  error: string | null;
  latency_ms?: number;
  overflow?: OverflowResult;
  query?: string;
  adapted_query?: string;
  message?: string;
  status?: string;
  credentials?: Array<string>;
  connect?: JsonObject;
}

export interface ResultSlice {
  offset: number;
  limit: number;
  total_lines: number;
  content: string;
  truncated: boolean;
  ok: true;
  op: "slice";
}

export interface ResultSearch {
  count: number;
  matches_json: string;
  truncated: boolean;
  ok: true;
  op: "search";
}

export interface ResultJsonPath {
  shape: ResultShape;
  value_json: string;
  truncated: boolean;
  ok: true;
  op: "json_path";
}

export interface ResultReadError {
  ok: false;
  error: string;
  message: string;
}

export interface RecommendationSubmission {
  job: string;
  state: "queued" | "running" | "done" | "error";
  lane: string;
  position: number | null;
  lane_position?: number | null;
  eta_ms: number;
  error?: string;
}

export interface FieldProbeResult {
  ok: boolean;
  id?: number;
  stored?: string;
  error?: string;
}

export interface PricePlan {
  plan_id: string | null;
  kind: string | null;
  plan_group: string | null;
  effective_usd: number;
  held: boolean;
  currency: string;
  confidence: string;
  overridden: boolean;
}

export interface PreferredDecision {
  tool_id?: string;
  name?: string;
  honoured?: boolean;
  acceptable?: boolean;
  gap?: number;
  margin?: number;
  cap_lcb?: number;
  threshold?: number;
  best?: string;
  best_name?: string;
}

export interface ExcludedTools {
  count: number;
  facets: Array<string>;
  tool_ids: Array<string>;
}

export interface NativeBaseline {
  score: number;
  source: string;
  tau: number;
  self: boolean;
}

export interface OwnToolDecision {
  tool_id?: string;
  trigger?: string;
  match?: number;
  stance?: string;
  own_quality_mean?: number | null;
  outcomes?: number;
}

export interface RoutingFlags {
  short_circuit?: boolean;
  learned_preset?: string;
  match_similarity?: number;
  digest_skipped?: boolean;
  digest_applied?: boolean;
  excluded?: ExcludedTools;
  verdict?: string;
  preferred?: PreferredDecision;
  own?: OwnToolDecision;
  consider?: Array<JsonObject>;
  baseline?: NativeBaseline;
}


export interface TestCredentialQuery {
  tool_id: string;
}

export interface GetPreferencesQuery {
  project_id?: string | null;
}

export interface ClearPreferencesQuery {
  project_id?: string | null;
}

export interface ListPrivateToolsQuery {
  project_id?: string | null;
}

export interface DeletePrivateToolQuery {
  project_id?: string | null;
}

export interface SetPrivateStanceQuery {
  stance: string;
  project_id?: string | null;
}

export interface ListPreferredToolsQuery {
  project_id?: string | null;
}

export interface UnpreferToolQuery {
  project_id?: string | null;
}

export interface ConsoleQuery {
  view?: string;
  format?: string;
  limit?: number;
  project_id?: string | null;
}

export interface ConsoleViewQuery {
  limit?: number;
  project_id?: string | null;
}
