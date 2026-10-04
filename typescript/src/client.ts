import { Transport, type ApiResponse, type RequestOptions } from "./transport.js";
import type * as T from "./types.js";

export class HyperRoute extends Transport {
  recommend(body: T.TextRecommendRequest, options?: RequestOptions): Promise<ApiResponse<string>>;
  recommend(body: T.FullRecommendRequest, options?: RequestOptions): Promise<ApiResponse<T.FullRecommendation>>;
  recommend(body: T.MinRecommendRequest, options?: RequestOptions): Promise<ApiResponse<T.MinRecommendation>>;
  recommend(body: T.LeanRecommendRequest, options?: RequestOptions): Promise<ApiResponse<T.LeanRecommendation>>;
  recommend(body: T.RecommendRequest, options?: RequestOptions): Promise<ApiResponse<T.Recommendation | string>>;
  recommend(body: T.RecommendRequest, options: RequestOptions = {}): Promise<ApiResponse<T.Recommendation | string>> {
    return this.request("POST", "/recommend", body, undefined, "auto", options);
  }

  submitRecommendation(body: T.RecommendRequest, options: RequestOptions = {}): Promise<ApiResponse<T.RecommendationSubmission>> {
    return this.request("POST", "/recommend/submit", body, undefined, "json", options);
  }

  recommendationStatus(job_id: string, options: RequestOptions = {}): Promise<ApiResponse<T.RecommendationJob>> {
    return this.request("GET", "/recommend/status/{job_id}".replace("{job_id}", encodeURIComponent(job_id)), undefined, undefined, "json", options);
  }

  describe(body: T.DescribeRequest, options: RequestOptions = {}): Promise<ApiResponse<T.Description>> {
    return this.request("POST", "/describe", body, undefined, "json", options);
  }

  execute(body: T.ExecuteRequest, options: RequestOptions = {}): Promise<ApiResponse<T.ExecutionResult>> {
    return this.request("POST", "/execute", body, undefined, "json", options);
  }

  reportOutcome(body: T.ReportOutcomeRequest, options: RequestOptions = {}): Promise<ApiResponse<T.OutcomeReport>> {
    return this.request("POST", "/report_outcome", body, undefined, "json", options);
  }

  reportNarrative(body: T.NarrativeReport, options: RequestOptions = {}): Promise<ApiResponse<T.NarrativeResult>> {
    return this.request("POST", "/report_narrative", body, undefined, "json", options);
  }

  health(options: RequestOptions = {}): Promise<ApiResponse<T.Health>> {
    return this.request("GET", "/health", undefined, undefined, "json", options);
  }

  queue(options: RequestOptions = {}): Promise<ApiResponse<T.QueueStatus>> {
    return this.request("GET", "/queue", undefined, undefined, "json", options);
  }

  facetsCatalog(options: RequestOptions = {}): Promise<ApiResponse<T.FacetCatalog>> {
    return this.request("GET", "/facets/catalog", undefined, undefined, "json", options);
  }

  onboard(body: T.OnboardRequest, options: RequestOptions = {}): Promise<ApiResponse<T.CredentialResult>> {
    return this.request("POST", "/onboard", body, undefined, "json", options);
  }

  onboardInfo(tool_id: string, options: RequestOptions = {}): Promise<ApiResponse<T.OnboardInfo>> {
    return this.request("GET", "/onboard/{tool_id}".replace("{tool_id}", encodeURIComponent(tool_id)), undefined, undefined, "json", options);
  }

  connectCredential(body: T.ConnectRequest, options: RequestOptions = {}): Promise<ApiResponse<T.CredentialResult>> {
    return this.request("POST", "/credentials/connect", body, undefined, "json", options);
  }

  listCredentials(options: RequestOptions = {}): Promise<ApiResponse<T.CredentialList>> {
    return this.request("GET", "/credentials", undefined, undefined, "json", options);
  }

  testCredential(query: T.TestCredentialQuery, options: RequestOptions = {}): Promise<ApiResponse<T.CredentialResult>> {
    return this.request("POST", "/credentials/test", undefined, query, "json", options);
  }

  deleteCredential(tool_id: string, options: RequestOptions = {}): Promise<ApiResponse<T.DeletedResponse>> {
    return this.request("DELETE", "/credentials/{tool_id}".replace("{tool_id}", encodeURIComponent(tool_id)), undefined, undefined, "json", options);
  }

  getPreferences(query: T.GetPreferencesQuery = {}, options: RequestOptions = {}): Promise<ApiResponse<T.Preferences>> {
    return this.request("GET", "/preferences", undefined, query, "json", options);
  }

  setPreferences(body: T.PreferencesRequest, options: RequestOptions = {}): Promise<ApiResponse<T.StoredPreferences>> {
    return this.request("PUT", "/preferences", body, undefined, "json", options);
  }

  clearPreferences(query: T.ClearPreferencesQuery = {}, options: RequestOptions = {}): Promise<ApiResponse<T.DeletedResponse>> {
    return this.request("DELETE", "/preferences", undefined, query, "json", options);
  }

  listPrivateTools(query: T.ListPrivateToolsQuery = {}, options: RequestOptions = {}): Promise<ApiResponse<T.PrivateToolList>> {
    return this.request("GET", "/private-tools", undefined, query, "json", options);
  }

  declarePrivateTool(body: T.PrivateToolRequest, options: RequestOptions = {}): Promise<ApiResponse<T.DeclaredPrivateTool>> {
    return this.request("PUT", "/private-tools", body, undefined, "json", options);
  }

  updatePrivateTool(tool_slug: string, body: T.PrivateToolPatch, options: RequestOptions = {}): Promise<ApiResponse<T.UpdatedPrivateTool>> {
    return this.request("PATCH", "/private-tools/{tool_slug}".replace("{tool_slug}", encodeURIComponent(tool_slug)), body, undefined, "json", options);
  }

  deletePrivateTool(tool_slug: string, query: T.DeletePrivateToolQuery = {}, options: RequestOptions = {}): Promise<ApiResponse<T.DeletedResponse>> {
    return this.request("DELETE", "/private-tools/{tool_slug}".replace("{tool_slug}", encodeURIComponent(tool_slug)), undefined, query, "json", options);
  }

  suggestPrivateTools(body: T.PrivateToolRequest, options: RequestOptions = {}): Promise<ApiResponse<T.RegionSuggestions>> {
    return this.request("POST", "/private-tools/suggest", body, undefined, "json", options);
  }

  setPrivateStance(tool_slug: string, query: T.SetPrivateStanceQuery, options: RequestOptions = {}): Promise<ApiResponse<T.UpdatedPrivateTool>> {
    return this.request("POST", "/private-tools/{tool_slug}/stance".replace("{tool_slug}", encodeURIComponent(tool_slug)), undefined, query, "json", options);
  }

  listPreferredTools(query: T.ListPreferredToolsQuery = {}, options: RequestOptions = {}): Promise<ApiResponse<T.PreferredToolList>> {
    return this.request("GET", "/preferred-tools", undefined, query, "json", options);
  }

  preferTool(body: T.PreferredToolRequest, options: RequestOptions = {}): Promise<ApiResponse<T.PreferredToolResult>> {
    return this.request("PUT", "/preferred-tools", body, undefined, "json", options);
  }

  updatePreferredTool(tool_id: string, body: T.PreferredToolPatch, options: RequestOptions = {}): Promise<ApiResponse<T.UpdatedPreferredTool>> {
    return this.request("PATCH", "/preferred-tools/{tool_id}".replace("{tool_id}", encodeURIComponent(tool_id)), body, undefined, "json", options);
  }

  unpreferTool(tool_id: string, query: T.UnpreferToolQuery = {}, options: RequestOptions = {}): Promise<ApiResponse<T.DeletedResponse>> {
    return this.request("DELETE", "/preferred-tools/{tool_id}".replace("{tool_id}", encodeURIComponent(tool_id)), undefined, query, "json", options);
  }

  downloadResult(ref: string, options: RequestOptions = {}): Promise<ApiResponse<Uint8Array>> {
    return this.request("GET", "/result/{ref}".replace("{ref}", encodeURIComponent(ref)), undefined, undefined, "bytes", options);
  }

  readResult(ref: string, body: T.ResultReadRequest, options: RequestOptions = {}): Promise<ApiResponse<T.ReadResult>> {
    return this.request("POST", "/result/{ref}/read".replace("{ref}", encodeURIComponent(ref)), body, undefined, "json", options);
  }

  console(query: T.ConsoleQuery = {}, options: RequestOptions = {}): Promise<ApiResponse<T.ConsoleResult | string>> {
    return this.request("GET", "/console", undefined, query, "auto", options);
  }

  consoleView(view: string, query: T.ConsoleViewQuery = {}, options: RequestOptions = {}): Promise<ApiResponse<T.ConsoleResult | string>> {
    return this.request("GET", "/console/{view}".replace("{view}", encodeURIComponent(view)), undefined, query, "auto", options);
  }

  register(body: T.RegisterRequest, options: RequestOptions = {}): Promise<ApiResponse<T.RegistrationResponse>> {
    return this.request("POST", "/auth/register", body, undefined, "json", options);
  }

  verify(body: T.VerifyRequest, options: RequestOptions = {}): Promise<ApiResponse<T.AuthSession>> {
    return this.request("POST", "/auth/verify", body, undefined, "json", options);
  }

  resendVerification(body: T.EmailRequest, options: RequestOptions = {}): Promise<ApiResponse<T.MessageResponse>> {
    return this.request("POST", "/auth/resend", body, undefined, "json", options);
  }

  login(body: T.LoginRequest, options: RequestOptions = {}): Promise<ApiResponse<T.AuthSession>> {
    return this.request("POST", "/auth/login", body, undefined, "json", options);
  }

  requestLoginCode(body: T.EmailRequest, options: RequestOptions = {}): Promise<ApiResponse<T.MessageResponse>> {
    return this.request("POST", "/auth/login/request-code", body, undefined, "json", options);
  }

  loginWithCode(body: T.CodeLoginRequest, options: RequestOptions = {}): Promise<ApiResponse<T.AuthSession>> {
    return this.request("POST", "/auth/login/code", body, undefined, "json", options);
  }

  forgotPassword(body: T.EmailRequest, options: RequestOptions = {}): Promise<ApiResponse<T.MessageResponse>> {
    return this.request("POST", "/auth/password/forgot", body, undefined, "json", options);
  }

  resetPassword(body: T.ResetPasswordRequest, options: RequestOptions = {}): Promise<ApiResponse<T.AuthSession>> {
    return this.request("POST", "/auth/password/reset", body, undefined, "json", options);
  }

  recoverAccount(body: T.RecoverRequest, options: RequestOptions = {}): Promise<ApiResponse<T.AuthSession>> {
    return this.request("POST", "/auth/recover", body, undefined, "json", options);
  }

  whoami(options: RequestOptions = {}): Promise<ApiResponse<T.User>> {
    return this.request("POST", "/auth/whoami", undefined, undefined, "json", options);
  }

  createToken(body: T.TokenCreateRequest, options: RequestOptions = {}): Promise<ApiResponse<T.CreatedToken>> {
    return this.request("POST", "/auth/tokens", body, undefined, "json", options);
  }

  listTokens(options: RequestOptions = {}): Promise<ApiResponse<T.TokenList>> {
    return this.request("GET", "/auth/tokens", undefined, undefined, "json", options);
  }

  revokeToken(token_id: string, options: RequestOptions = {}): Promise<ApiResponse<T.RevokedResponse>> {
    return this.request("DELETE", "/auth/tokens/{token_id}".replace("{token_id}", encodeURIComponent(token_id)), undefined, undefined, "json", options);
  }

  acceptInvite(body: T.InviteAcceptRequest, options: RequestOptions = {}): Promise<ApiResponse<T.AuthSession>> {
    return this.request("POST", "/invite/accept", body, undefined, "json", options);
  }

  applyBeta(body: T.BetaApplicationRequest, options: RequestOptions = {}): Promise<ApiResponse<T.BetaApplication>> {
    return this.request("POST", "/beta/apply", body, undefined, "json", options);
  }

  callerCollectors(options: RequestOptions = {}): Promise<ApiResponse<T.CallerCollectors>> {
    return this.request("GET", "/caller/collectors", undefined, undefined, "json", options);
  }

}
