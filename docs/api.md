# API reference

Python methods use snake_case; TypeScript methods use camelCase. Methods return an
`ApiResponse` with `data`, `status_code` / `statusCode`, and response `headers`.
Python accepts request options as keyword arguments; TypeScript takes a final options object.
Body parameters are typed request objects. Path parameters precede the body or query object.

| Python | TypeScript | HTTP | Body | Response data |
|---|---|---|---|---|
| `recommend` | `recommend` | `POST /recommend` | `RecommendRequest` | `Recommendation | str` |
| `submit_recommendation` | `submitRecommendation` | `POST /recommend/submit` | `RecommendRequest` | `RecommendationSubmission` |
| `recommendation_status` | `recommendationStatus` | `GET /recommend/status/{job_id}` | — | `RecommendationJob` |
| `describe` | `describe` | `POST /describe` | `DescribeRequest` | `Description` |
| `execute` | `execute` | `POST /execute` | `ExecuteRequest` | `ExecutionResult` |
| `report_outcome` | `reportOutcome` | `POST /report_outcome` | `ReportOutcomeRequest` | `OutcomeReport` |
| `report_narrative` | `reportNarrative` | `POST /report_narrative` | `NarrativeReport` | `NarrativeResult` |
| `health` | `health` | `GET /health` | — | `Health` |
| `queue` | `queue` | `GET /queue` | — | `QueueStatus` |
| `facets_catalog` | `facetsCatalog` | `GET /facets/catalog` | — | `FacetCatalog` |
| `onboard` | `onboard` | `POST /onboard` | `OnboardRequest` | `CredentialResult` |
| `onboard_info` | `onboardInfo` | `GET /onboard/{tool_id}` | — | `OnboardInfo` |
| `connect_credential` | `connectCredential` | `POST /credentials/connect` | `ConnectRequest` | `CredentialResult` |
| `list_credentials` | `listCredentials` | `GET /credentials` | — | `CredentialList` |
| `test_credential` | `testCredential` | `POST /credentials/test` | — | `CredentialResult` |
| `delete_credential` | `deleteCredential` | `DELETE /credentials/{tool_id}` | — | `DeletedResponse` |
| `get_preferences` | `getPreferences` | `GET /preferences` | — | `Preferences` |
| `set_preferences` | `setPreferences` | `PUT /preferences` | `PreferencesRequest` | `StoredPreferences` |
| `clear_preferences` | `clearPreferences` | `DELETE /preferences` | — | `DeletedResponse` |
| `list_private_tools` | `listPrivateTools` | `GET /private-tools` | — | `PrivateToolList` |
| `declare_private_tool` | `declarePrivateTool` | `PUT /private-tools` | `PrivateToolRequest` | `DeclaredPrivateTool` |
| `update_private_tool` | `updatePrivateTool` | `PATCH /private-tools/{tool_slug}` | `PrivateToolPatch` | `UpdatedPrivateTool` |
| `delete_private_tool` | `deletePrivateTool` | `DELETE /private-tools/{tool_slug}` | — | `DeletedResponse` |
| `suggest_private_tools` | `suggestPrivateTools` | `POST /private-tools/suggest` | `PrivateToolRequest` | `RegionSuggestions` |
| `set_private_stance` | `setPrivateStance` | `POST /private-tools/{tool_slug}/stance` | — | `UpdatedPrivateTool` |
| `list_preferred_tools` | `listPreferredTools` | `GET /preferred-tools` | — | `PreferredToolList` |
| `prefer_tool` | `preferTool` | `PUT /preferred-tools` | `PreferredToolRequest` | `PreferredToolResult` |
| `update_preferred_tool` | `updatePreferredTool` | `PATCH /preferred-tools/{tool_id}` | `PreferredToolPatch` | `UpdatedPreferredTool` |
| `unprefer_tool` | `unpreferTool` | `DELETE /preferred-tools/{tool_id}` | — | `DeletedResponse` |
| `download_result` | `downloadResult` | `GET /result/{ref}` | — | `bytes` |
| `read_result` | `readResult` | `POST /result/{ref}/read` | `ResultReadRequest` | `ReadResult` |
| `console` | `console` | `GET /console` | — | `ConsoleResult | str` |
| `console_view` | `consoleView` | `GET /console/{view}` | — | `ConsoleResult | str` |
| `register` | `register` | `POST /auth/register` | `RegisterRequest` | `RegistrationResponse` |
| `verify` | `verify` | `POST /auth/verify` | `VerifyRequest` | `AuthSession` |
| `resend_verification` | `resendVerification` | `POST /auth/resend` | `EmailRequest` | `MessageResponse` |
| `login` | `login` | `POST /auth/login` | `LoginRequest` | `AuthSession` |
| `request_login_code` | `requestLoginCode` | `POST /auth/login/request-code` | `EmailRequest` | `MessageResponse` |
| `login_with_code` | `loginWithCode` | `POST /auth/login/code` | `CodeLoginRequest` | `AuthSession` |
| `forgot_password` | `forgotPassword` | `POST /auth/password/forgot` | `EmailRequest` | `MessageResponse` |
| `reset_password` | `resetPassword` | `POST /auth/password/reset` | `ResetPasswordRequest` | `AuthSession` |
| `recover_account` | `recoverAccount` | `POST /auth/recover` | `RecoverRequest` | `AuthSession` |
| `whoami` | `whoami` | `POST /auth/whoami` | — | `User` |
| `create_token` | `createToken` | `POST /auth/tokens` | `TokenCreateRequest` | `CreatedToken` |
| `list_tokens` | `listTokens` | `GET /auth/tokens` | — | `TokenList` |
| `revoke_token` | `revokeToken` | `DELETE /auth/tokens/{token_id}` | — | `RevokedResponse` |
| `accept_invite` | `acceptInvite` | `POST /invite/accept` | `InviteAcceptRequest` | `AuthSession` |
| `apply_beta` | `applyBeta` | `POST /beta/apply` | `BetaApplicationRequest` | `BetaApplication` |
| `caller_collectors` | `callerCollectors` | `GET /caller/collectors` | — | `CallerCollectors` |
