from __future__ import annotations
from typing import Any, overload
from urllib.parse import quote
from .transport import SyncTransport, AsyncTransport, ApiResponse, RequestOptions
from .types import *

class HyperRoute(SyncTransport):
    @overload
    def recommend(self, body: TextRecommendRequest, *, options: RequestOptions | None = None) -> ApiResponse[str]: ...

    @overload
    def recommend(self, body: FullRecommendRequest, *, options: RequestOptions | None = None) -> ApiResponse[FullRecommendation]: ...

    @overload
    def recommend(self, body: MinRecommendRequest, *, options: RequestOptions | None = None) -> ApiResponse[MinRecommendation]: ...

    @overload
    def recommend(self, body: LeanRecommendRequest, *, options: RequestOptions | None = None) -> ApiResponse[LeanRecommendation]: ...

    @overload
    def recommend(self, body: RecommendRequest, *, options: RequestOptions | None = None) -> ApiResponse[Recommendation | str]: ...

    def recommend(self, body: RecommendRequest | TextRecommendRequest | FullRecommendRequest | MinRecommendRequest | LeanRecommendRequest, *, options: RequestOptions | None = None) -> ApiResponse[Recommendation | str]:
        return self._request('POST', '/recommend', body=body, query=None, mode='auto', options=options)

    def submit_recommendation(self, body: RecommendRequest, *, options: RequestOptions | None = None) -> ApiResponse[RecommendationSubmission]:
        return self._request('POST', '/recommend/submit', body=body, query=None, mode='json', options=options)

    def recommendation_status(self, job_id: str, *, options: RequestOptions | None = None) -> ApiResponse[RecommendationJob]:
        return self._request('GET', '/recommend/status/{job_id}'.replace("{job_id}", quote(job_id, safe="")), body=None, query=None, mode='json', options=options)

    def describe(self, body: DescribeRequest, *, options: RequestOptions | None = None) -> ApiResponse[Description]:
        return self._request('POST', '/describe', body=body, query=None, mode='json', options=options)

    def execute(self, body: ExecuteRequest, *, options: RequestOptions | None = None) -> ApiResponse[ExecutionResult]:
        return self._request('POST', '/execute', body=body, query=None, mode='json', options=options)

    def report_outcome(self, body: ReportOutcomeRequest, *, options: RequestOptions | None = None) -> ApiResponse[OutcomeReport]:
        return self._request('POST', '/report_outcome', body=body, query=None, mode='json', options=options)

    def report_narrative(self, body: NarrativeReport, *, options: RequestOptions | None = None) -> ApiResponse[NarrativeResult]:
        return self._request('POST', '/report_narrative', body=body, query=None, mode='json', options=options)

    def health(self, *, options: RequestOptions | None = None) -> ApiResponse[Health]:
        return self._request('GET', '/health', body=None, query=None, mode='json', options=options)

    def queue(self, *, options: RequestOptions | None = None) -> ApiResponse[QueueStatus]:
        return self._request('GET', '/queue', body=None, query=None, mode='json', options=options)

    def facets_catalog(self, *, options: RequestOptions | None = None) -> ApiResponse[FacetCatalog]:
        return self._request('GET', '/facets/catalog', body=None, query=None, mode='json', options=options)

    def onboard(self, body: OnboardRequest, *, options: RequestOptions | None = None) -> ApiResponse[CredentialResult]:
        return self._request('POST', '/onboard', body=body, query=None, mode='json', options=options)

    def onboard_info(self, tool_id: str, *, options: RequestOptions | None = None) -> ApiResponse[OnboardInfo]:
        return self._request('GET', '/onboard/{tool_id}'.replace("{tool_id}", quote(tool_id, safe="")), body=None, query=None, mode='json', options=options)

    def connect_credential(self, body: ConnectRequest, *, options: RequestOptions | None = None) -> ApiResponse[CredentialResult]:
        return self._request('POST', '/credentials/connect', body=body, query=None, mode='json', options=options)

    def list_credentials(self, *, options: RequestOptions | None = None) -> ApiResponse[CredentialList]:
        return self._request('GET', '/credentials', body=None, query=None, mode='json', options=options)

    def test_credential(self, query: TestCredentialQuery, *, options: RequestOptions | None = None) -> ApiResponse[CredentialResult]:
        return self._request('POST', '/credentials/test', body=None, query=query, mode='json', options=options)

    def delete_credential(self, tool_id: str, *, options: RequestOptions | None = None) -> ApiResponse[DeletedResponse]:
        return self._request('DELETE', '/credentials/{tool_id}'.replace("{tool_id}", quote(tool_id, safe="")), body=None, query=None, mode='json', options=options)

    def get_preferences(self, query: GetPreferencesQuery | None = None, *, options: RequestOptions | None = None) -> ApiResponse[Preferences]:
        return self._request('GET', '/preferences', body=None, query=query, mode='json', options=options)

    def set_preferences(self, body: PreferencesRequest, *, options: RequestOptions | None = None) -> ApiResponse[StoredPreferences]:
        return self._request('PUT', '/preferences', body=body, query=None, mode='json', options=options)

    def clear_preferences(self, query: ClearPreferencesQuery | None = None, *, options: RequestOptions | None = None) -> ApiResponse[DeletedResponse]:
        return self._request('DELETE', '/preferences', body=None, query=query, mode='json', options=options)

    def list_private_tools(self, query: ListPrivateToolsQuery | None = None, *, options: RequestOptions | None = None) -> ApiResponse[PrivateToolList]:
        return self._request('GET', '/private-tools', body=None, query=query, mode='json', options=options)

    def declare_private_tool(self, body: PrivateToolRequest, *, options: RequestOptions | None = None) -> ApiResponse[DeclaredPrivateTool]:
        return self._request('PUT', '/private-tools', body=body, query=None, mode='json', options=options)

    def update_private_tool(self, tool_slug: str, body: PrivateToolPatch, *, options: RequestOptions | None = None) -> ApiResponse[UpdatedPrivateTool]:
        return self._request('PATCH', '/private-tools/{tool_slug}'.replace("{tool_slug}", quote(tool_slug, safe="")), body=body, query=None, mode='json', options=options)

    def delete_private_tool(self, tool_slug: str, query: DeletePrivateToolQuery | None = None, *, options: RequestOptions | None = None) -> ApiResponse[DeletedResponse]:
        return self._request('DELETE', '/private-tools/{tool_slug}'.replace("{tool_slug}", quote(tool_slug, safe="")), body=None, query=query, mode='json', options=options)

    def suggest_private_tools(self, body: PrivateToolRequest, *, options: RequestOptions | None = None) -> ApiResponse[RegionSuggestions]:
        return self._request('POST', '/private-tools/suggest', body=body, query=None, mode='json', options=options)

    def set_private_stance(self, tool_slug: str, query: SetPrivateStanceQuery, *, options: RequestOptions | None = None) -> ApiResponse[UpdatedPrivateTool]:
        return self._request('POST', '/private-tools/{tool_slug}/stance'.replace("{tool_slug}", quote(tool_slug, safe="")), body=None, query=query, mode='json', options=options)

    def list_preferred_tools(self, query: ListPreferredToolsQuery | None = None, *, options: RequestOptions | None = None) -> ApiResponse[PreferredToolList]:
        return self._request('GET', '/preferred-tools', body=None, query=query, mode='json', options=options)

    def prefer_tool(self, body: PreferredToolRequest, *, options: RequestOptions | None = None) -> ApiResponse[PreferredToolResult]:
        return self._request('PUT', '/preferred-tools', body=body, query=None, mode='json', options=options)

    def update_preferred_tool(self, tool_id: str, body: PreferredToolPatch, *, options: RequestOptions | None = None) -> ApiResponse[UpdatedPreferredTool]:
        return self._request('PATCH', '/preferred-tools/{tool_id}'.replace("{tool_id}", quote(tool_id, safe="")), body=body, query=None, mode='json', options=options)

    def unprefer_tool(self, tool_id: str, query: UnpreferToolQuery | None = None, *, options: RequestOptions | None = None) -> ApiResponse[DeletedResponse]:
        return self._request('DELETE', '/preferred-tools/{tool_id}'.replace("{tool_id}", quote(tool_id, safe="")), body=None, query=query, mode='json', options=options)

    def download_result(self, ref: str, *, options: RequestOptions | None = None) -> ApiResponse[bytes]:
        return self._request('GET', '/result/{ref}'.replace("{ref}", quote(ref, safe="")), body=None, query=None, mode='bytes', options=options)

    def read_result(self, ref: str, body: ResultReadRequest, *, options: RequestOptions | None = None) -> ApiResponse[ReadResult]:
        return self._request('POST', '/result/{ref}/read'.replace("{ref}", quote(ref, safe="")), body=body, query=None, mode='json', options=options)

    def console(self, query: ConsoleQuery | None = None, *, options: RequestOptions | None = None) -> ApiResponse[ConsoleResult | str]:
        return self._request('GET', '/console', body=None, query=query, mode='auto', options=options)

    def console_view(self, view: str, query: ConsoleViewQuery | None = None, *, options: RequestOptions | None = None) -> ApiResponse[ConsoleResult | str]:
        return self._request('GET', '/console/{view}'.replace("{view}", quote(view, safe="")), body=None, query=query, mode='auto', options=options)

    def register(self, body: RegisterRequest, *, options: RequestOptions | None = None) -> ApiResponse[RegistrationResponse]:
        return self._request('POST', '/auth/register', body=body, query=None, mode='json', options=options)

    def verify(self, body: VerifyRequest, *, options: RequestOptions | None = None) -> ApiResponse[AuthSession]:
        return self._request('POST', '/auth/verify', body=body, query=None, mode='json', options=options)

    def resend_verification(self, body: EmailRequest, *, options: RequestOptions | None = None) -> ApiResponse[MessageResponse]:
        return self._request('POST', '/auth/resend', body=body, query=None, mode='json', options=options)

    def login(self, body: LoginRequest, *, options: RequestOptions | None = None) -> ApiResponse[AuthSession]:
        return self._request('POST', '/auth/login', body=body, query=None, mode='json', options=options)

    def request_login_code(self, body: EmailRequest, *, options: RequestOptions | None = None) -> ApiResponse[MessageResponse]:
        return self._request('POST', '/auth/login/request-code', body=body, query=None, mode='json', options=options)

    def login_with_code(self, body: CodeLoginRequest, *, options: RequestOptions | None = None) -> ApiResponse[AuthSession]:
        return self._request('POST', '/auth/login/code', body=body, query=None, mode='json', options=options)

    def forgot_password(self, body: EmailRequest, *, options: RequestOptions | None = None) -> ApiResponse[MessageResponse]:
        return self._request('POST', '/auth/password/forgot', body=body, query=None, mode='json', options=options)

    def reset_password(self, body: ResetPasswordRequest, *, options: RequestOptions | None = None) -> ApiResponse[AuthSession]:
        return self._request('POST', '/auth/password/reset', body=body, query=None, mode='json', options=options)

    def recover_account(self, body: RecoverRequest, *, options: RequestOptions | None = None) -> ApiResponse[AuthSession]:
        return self._request('POST', '/auth/recover', body=body, query=None, mode='json', options=options)

    def whoami(self, *, options: RequestOptions | None = None) -> ApiResponse[User]:
        return self._request('POST', '/auth/whoami', body=None, query=None, mode='json', options=options)

    def create_token(self, body: TokenCreateRequest, *, options: RequestOptions | None = None) -> ApiResponse[CreatedToken]:
        return self._request('POST', '/auth/tokens', body=body, query=None, mode='json', options=options)

    def list_tokens(self, *, options: RequestOptions | None = None) -> ApiResponse[TokenList]:
        return self._request('GET', '/auth/tokens', body=None, query=None, mode='json', options=options)

    def revoke_token(self, token_id: str, *, options: RequestOptions | None = None) -> ApiResponse[RevokedResponse]:
        return self._request('DELETE', '/auth/tokens/{token_id}'.replace("{token_id}", quote(token_id, safe="")), body=None, query=None, mode='json', options=options)

    def accept_invite(self, body: InviteAcceptRequest, *, options: RequestOptions | None = None) -> ApiResponse[AuthSession]:
        return self._request('POST', '/invite/accept', body=body, query=None, mode='json', options=options)

    def apply_beta(self, body: BetaApplicationRequest, *, options: RequestOptions | None = None) -> ApiResponse[BetaApplication]:
        return self._request('POST', '/beta/apply', body=body, query=None, mode='json', options=options)

    def caller_collectors(self, *, options: RequestOptions | None = None) -> ApiResponse[CallerCollectors]:
        return self._request('GET', '/caller/collectors', body=None, query=None, mode='json', options=options)


class AsyncHyperRoute(AsyncTransport):
    @overload
    async def recommend(self, body: TextRecommendRequest, *, options: RequestOptions | None = None) -> ApiResponse[str]: ...

    @overload
    async def recommend(self, body: FullRecommendRequest, *, options: RequestOptions | None = None) -> ApiResponse[FullRecommendation]: ...

    @overload
    async def recommend(self, body: MinRecommendRequest, *, options: RequestOptions | None = None) -> ApiResponse[MinRecommendation]: ...

    @overload
    async def recommend(self, body: LeanRecommendRequest, *, options: RequestOptions | None = None) -> ApiResponse[LeanRecommendation]: ...

    @overload
    async def recommend(self, body: RecommendRequest, *, options: RequestOptions | None = None) -> ApiResponse[Recommendation | str]: ...

    async def recommend(self, body: RecommendRequest | TextRecommendRequest | FullRecommendRequest | MinRecommendRequest | LeanRecommendRequest, *, options: RequestOptions | None = None) -> ApiResponse[Recommendation | str]:
        return await self._request('POST', '/recommend', body=body, query=None, mode='auto', options=options)

    async def submit_recommendation(self, body: RecommendRequest, *, options: RequestOptions | None = None) -> ApiResponse[RecommendationSubmission]:
        return await self._request('POST', '/recommend/submit', body=body, query=None, mode='json', options=options)

    async def recommendation_status(self, job_id: str, *, options: RequestOptions | None = None) -> ApiResponse[RecommendationJob]:
        return await self._request('GET', '/recommend/status/{job_id}'.replace("{job_id}", quote(job_id, safe="")), body=None, query=None, mode='json', options=options)

    async def describe(self, body: DescribeRequest, *, options: RequestOptions | None = None) -> ApiResponse[Description]:
        return await self._request('POST', '/describe', body=body, query=None, mode='json', options=options)

    async def execute(self, body: ExecuteRequest, *, options: RequestOptions | None = None) -> ApiResponse[ExecutionResult]:
        return await self._request('POST', '/execute', body=body, query=None, mode='json', options=options)

    async def report_outcome(self, body: ReportOutcomeRequest, *, options: RequestOptions | None = None) -> ApiResponse[OutcomeReport]:
        return await self._request('POST', '/report_outcome', body=body, query=None, mode='json', options=options)

    async def report_narrative(self, body: NarrativeReport, *, options: RequestOptions | None = None) -> ApiResponse[NarrativeResult]:
        return await self._request('POST', '/report_narrative', body=body, query=None, mode='json', options=options)

    async def health(self, *, options: RequestOptions | None = None) -> ApiResponse[Health]:
        return await self._request('GET', '/health', body=None, query=None, mode='json', options=options)

    async def queue(self, *, options: RequestOptions | None = None) -> ApiResponse[QueueStatus]:
        return await self._request('GET', '/queue', body=None, query=None, mode='json', options=options)

    async def facets_catalog(self, *, options: RequestOptions | None = None) -> ApiResponse[FacetCatalog]:
        return await self._request('GET', '/facets/catalog', body=None, query=None, mode='json', options=options)

    async def onboard(self, body: OnboardRequest, *, options: RequestOptions | None = None) -> ApiResponse[CredentialResult]:
        return await self._request('POST', '/onboard', body=body, query=None, mode='json', options=options)

    async def onboard_info(self, tool_id: str, *, options: RequestOptions | None = None) -> ApiResponse[OnboardInfo]:
        return await self._request('GET', '/onboard/{tool_id}'.replace("{tool_id}", quote(tool_id, safe="")), body=None, query=None, mode='json', options=options)

    async def connect_credential(self, body: ConnectRequest, *, options: RequestOptions | None = None) -> ApiResponse[CredentialResult]:
        return await self._request('POST', '/credentials/connect', body=body, query=None, mode='json', options=options)

    async def list_credentials(self, *, options: RequestOptions | None = None) -> ApiResponse[CredentialList]:
        return await self._request('GET', '/credentials', body=None, query=None, mode='json', options=options)

    async def test_credential(self, query: TestCredentialQuery, *, options: RequestOptions | None = None) -> ApiResponse[CredentialResult]:
        return await self._request('POST', '/credentials/test', body=None, query=query, mode='json', options=options)

    async def delete_credential(self, tool_id: str, *, options: RequestOptions | None = None) -> ApiResponse[DeletedResponse]:
        return await self._request('DELETE', '/credentials/{tool_id}'.replace("{tool_id}", quote(tool_id, safe="")), body=None, query=None, mode='json', options=options)

    async def get_preferences(self, query: GetPreferencesQuery | None = None, *, options: RequestOptions | None = None) -> ApiResponse[Preferences]:
        return await self._request('GET', '/preferences', body=None, query=query, mode='json', options=options)

    async def set_preferences(self, body: PreferencesRequest, *, options: RequestOptions | None = None) -> ApiResponse[StoredPreferences]:
        return await self._request('PUT', '/preferences', body=body, query=None, mode='json', options=options)

    async def clear_preferences(self, query: ClearPreferencesQuery | None = None, *, options: RequestOptions | None = None) -> ApiResponse[DeletedResponse]:
        return await self._request('DELETE', '/preferences', body=None, query=query, mode='json', options=options)

    async def list_private_tools(self, query: ListPrivateToolsQuery | None = None, *, options: RequestOptions | None = None) -> ApiResponse[PrivateToolList]:
        return await self._request('GET', '/private-tools', body=None, query=query, mode='json', options=options)

    async def declare_private_tool(self, body: PrivateToolRequest, *, options: RequestOptions | None = None) -> ApiResponse[DeclaredPrivateTool]:
        return await self._request('PUT', '/private-tools', body=body, query=None, mode='json', options=options)

    async def update_private_tool(self, tool_slug: str, body: PrivateToolPatch, *, options: RequestOptions | None = None) -> ApiResponse[UpdatedPrivateTool]:
        return await self._request('PATCH', '/private-tools/{tool_slug}'.replace("{tool_slug}", quote(tool_slug, safe="")), body=body, query=None, mode='json', options=options)

    async def delete_private_tool(self, tool_slug: str, query: DeletePrivateToolQuery | None = None, *, options: RequestOptions | None = None) -> ApiResponse[DeletedResponse]:
        return await self._request('DELETE', '/private-tools/{tool_slug}'.replace("{tool_slug}", quote(tool_slug, safe="")), body=None, query=query, mode='json', options=options)

    async def suggest_private_tools(self, body: PrivateToolRequest, *, options: RequestOptions | None = None) -> ApiResponse[RegionSuggestions]:
        return await self._request('POST', '/private-tools/suggest', body=body, query=None, mode='json', options=options)

    async def set_private_stance(self, tool_slug: str, query: SetPrivateStanceQuery, *, options: RequestOptions | None = None) -> ApiResponse[UpdatedPrivateTool]:
        return await self._request('POST', '/private-tools/{tool_slug}/stance'.replace("{tool_slug}", quote(tool_slug, safe="")), body=None, query=query, mode='json', options=options)

    async def list_preferred_tools(self, query: ListPreferredToolsQuery | None = None, *, options: RequestOptions | None = None) -> ApiResponse[PreferredToolList]:
        return await self._request('GET', '/preferred-tools', body=None, query=query, mode='json', options=options)

    async def prefer_tool(self, body: PreferredToolRequest, *, options: RequestOptions | None = None) -> ApiResponse[PreferredToolResult]:
        return await self._request('PUT', '/preferred-tools', body=body, query=None, mode='json', options=options)

    async def update_preferred_tool(self, tool_id: str, body: PreferredToolPatch, *, options: RequestOptions | None = None) -> ApiResponse[UpdatedPreferredTool]:
        return await self._request('PATCH', '/preferred-tools/{tool_id}'.replace("{tool_id}", quote(tool_id, safe="")), body=body, query=None, mode='json', options=options)

    async def unprefer_tool(self, tool_id: str, query: UnpreferToolQuery | None = None, *, options: RequestOptions | None = None) -> ApiResponse[DeletedResponse]:
        return await self._request('DELETE', '/preferred-tools/{tool_id}'.replace("{tool_id}", quote(tool_id, safe="")), body=None, query=query, mode='json', options=options)

    async def download_result(self, ref: str, *, options: RequestOptions | None = None) -> ApiResponse[bytes]:
        return await self._request('GET', '/result/{ref}'.replace("{ref}", quote(ref, safe="")), body=None, query=None, mode='bytes', options=options)

    async def read_result(self, ref: str, body: ResultReadRequest, *, options: RequestOptions | None = None) -> ApiResponse[ReadResult]:
        return await self._request('POST', '/result/{ref}/read'.replace("{ref}", quote(ref, safe="")), body=body, query=None, mode='json', options=options)

    async def console(self, query: ConsoleQuery | None = None, *, options: RequestOptions | None = None) -> ApiResponse[ConsoleResult | str]:
        return await self._request('GET', '/console', body=None, query=query, mode='auto', options=options)

    async def console_view(self, view: str, query: ConsoleViewQuery | None = None, *, options: RequestOptions | None = None) -> ApiResponse[ConsoleResult | str]:
        return await self._request('GET', '/console/{view}'.replace("{view}", quote(view, safe="")), body=None, query=query, mode='auto', options=options)

    async def register(self, body: RegisterRequest, *, options: RequestOptions | None = None) -> ApiResponse[RegistrationResponse]:
        return await self._request('POST', '/auth/register', body=body, query=None, mode='json', options=options)

    async def verify(self, body: VerifyRequest, *, options: RequestOptions | None = None) -> ApiResponse[AuthSession]:
        return await self._request('POST', '/auth/verify', body=body, query=None, mode='json', options=options)

    async def resend_verification(self, body: EmailRequest, *, options: RequestOptions | None = None) -> ApiResponse[MessageResponse]:
        return await self._request('POST', '/auth/resend', body=body, query=None, mode='json', options=options)

    async def login(self, body: LoginRequest, *, options: RequestOptions | None = None) -> ApiResponse[AuthSession]:
        return await self._request('POST', '/auth/login', body=body, query=None, mode='json', options=options)

    async def request_login_code(self, body: EmailRequest, *, options: RequestOptions | None = None) -> ApiResponse[MessageResponse]:
        return await self._request('POST', '/auth/login/request-code', body=body, query=None, mode='json', options=options)

    async def login_with_code(self, body: CodeLoginRequest, *, options: RequestOptions | None = None) -> ApiResponse[AuthSession]:
        return await self._request('POST', '/auth/login/code', body=body, query=None, mode='json', options=options)

    async def forgot_password(self, body: EmailRequest, *, options: RequestOptions | None = None) -> ApiResponse[MessageResponse]:
        return await self._request('POST', '/auth/password/forgot', body=body, query=None, mode='json', options=options)

    async def reset_password(self, body: ResetPasswordRequest, *, options: RequestOptions | None = None) -> ApiResponse[AuthSession]:
        return await self._request('POST', '/auth/password/reset', body=body, query=None, mode='json', options=options)

    async def recover_account(self, body: RecoverRequest, *, options: RequestOptions | None = None) -> ApiResponse[AuthSession]:
        return await self._request('POST', '/auth/recover', body=body, query=None, mode='json', options=options)

    async def whoami(self, *, options: RequestOptions | None = None) -> ApiResponse[User]:
        return await self._request('POST', '/auth/whoami', body=None, query=None, mode='json', options=options)

    async def create_token(self, body: TokenCreateRequest, *, options: RequestOptions | None = None) -> ApiResponse[CreatedToken]:
        return await self._request('POST', '/auth/tokens', body=body, query=None, mode='json', options=options)

    async def list_tokens(self, *, options: RequestOptions | None = None) -> ApiResponse[TokenList]:
        return await self._request('GET', '/auth/tokens', body=None, query=None, mode='json', options=options)

    async def revoke_token(self, token_id: str, *, options: RequestOptions | None = None) -> ApiResponse[RevokedResponse]:
        return await self._request('DELETE', '/auth/tokens/{token_id}'.replace("{token_id}", quote(token_id, safe="")), body=None, query=None, mode='json', options=options)

    async def accept_invite(self, body: InviteAcceptRequest, *, options: RequestOptions | None = None) -> ApiResponse[AuthSession]:
        return await self._request('POST', '/invite/accept', body=body, query=None, mode='json', options=options)

    async def apply_beta(self, body: BetaApplicationRequest, *, options: RequestOptions | None = None) -> ApiResponse[BetaApplication]:
        return await self._request('POST', '/beta/apply', body=body, query=None, mode='json', options=options)

    async def caller_collectors(self, *, options: RequestOptions | None = None) -> ApiResponse[CallerCollectors]:
        return await self._request('GET', '/caller/collectors', body=None, query=None, mode='json', options=options)
