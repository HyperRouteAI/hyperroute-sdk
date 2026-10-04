# Execution

[`execute.mjs`](../execute.mjs) runs the specified tool and prints the complete execution response. This output shows a tool requiring a connected credential.

```sh
node examples/typescript/execute.mjs --execute --tool-id TOOL --session-id SESSION --query 'Your task'
```

Example output:

```json
{
  "ok": false,
  "tool_id": "example_search",
  "error": "needs_onboard"
}
```
