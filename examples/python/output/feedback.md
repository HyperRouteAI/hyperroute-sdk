# Feedback

[`feedback.py`](../feedback.py) reports a tool outcome and prints the complete feedback response.

```sh
python examples/python/feedback.py --session-id SESSION --tool-id TOOL --score full
```

Example output:

```json
{
  "ok": true,
  "session_id": "session-1",
  "tool_id": "example_search",
  "accepted": {
    "score": "full",
    "reason": null,
    "counts_as_quality": true,
    "quality": 1.0,
    "comment": false,
    "human_survey": false
  },
  "field_probe": null,
  "triggers_raised": [],
  "score_moved": false
}
```
