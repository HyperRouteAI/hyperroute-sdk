# Run

[`run.mjs`](../run.mjs) sends several lookups in one call and prints the complete response. Each item is routed on its own: the best tool runs and its result returns, or the item is handed back, needs a key, or lists choices.

```sh
node examples/typescript/run.mjs 'EUR to GBP exchange rate on 2024-03-15' 'Geocode 350 Fifth Avenue, New York to latitude and longitude' 'Latest version of the npm package react'
```

Example output. Item 2 returned the wrong place; item 3's best tool needs a key.

```json
{
  "run": "r_example1",
  "items": [
    {
      "action": "run",
      "tool": "frankfurter",
      "name": null,
      "note": "sonar_deep_research +0.07, needs a key",
      "query": "EUR to GBP exchange rate on 2024-03-15",
      "session_id": "session-1",
      "stakes": "commodity",
      "area_state": "settled",
      "confidence": "high",
      "not_checked": [],
      "report": "always",
      "out": {
        "ok": true,
        "tool_id": "frankfurter",
        "query": "EUR to GBP exchange rate on 2024-03-15",
        "adapted_query": null,
        "latency_ms": 200,
        "result": {
          "query": "EUR to GBP exchange rate on 2024-03-15",
          "adapted_query": "EUR -> GBP on 2024-03-15",
          "provider": "Frankfurter (ECB reference rates)",
          "tool_kind": "currency exchange / conversion",
          "base": "EUR",
          "target": "GBP",
          "amount": 1.0,
          "rate": 0.8541,
          "converted": 0.8541,
          "requested_date": "2024-03-15",
          "rate_date": "2024-03-15",
          "human": "1 EUR = 0.8541 GBP (rate 0.8541, ECB 2024-03-15)"
        }
      },
      "instruction": null,
      "connect": null,
      "tools": null,
      "failed": [],
      "reopens": null
    },
    {
      "action": "run",
      "tool": "nominatim",
      "name": null,
      "note": "capability 0.88",
      "query": "Geocode 350 Fifth Avenue, New York to latitude and longitude",
      "session_id": "session-2",
      "stakes": "commodity",
      "area_state": "open",
      "confidence": "low",
      "not_checked": [],
      "report": "always",
      "out": {
        "ok": true,
        "tool_id": "nominatim",
        "query": "Geocode 350 Fifth Avenue, New York to latitude and longitude",
        "adapted_query": "350 Fifth Avenue, New York, NY, USA\nNew York, New York, USA",
        "latency_ms": 200,
        "result": {
          "query": "Geocode 350 Fifth Avenue, New York to latitude and longitude",
          "adapted_query": "geocode 350 Fifth Avenue, New York, NY, USA",
          "provider": "OpenStreetMap Nominatim",
          "tool_kind": "forward geocoding",
          "lat": "41.1033570",
          "lon": "-72.3659952",
          "display_name": "350, Fifth Avenue, Village of Greenport, Town of Southold, Suffolk County, New York, 11944, United States",
          "results": [
            {
              "lat": "41.1033570",
              "lon": "-72.3659952",
              "display_name": "350, Fifth Avenue, Village of Greenport, Town of Southold, Suffolk County, New York, 11944, United States",
              "class": "place",
              "type": "house"
            },
            {
              "lat": "42.7096512",
              "lon": "-73.7105988",
              "display_name": "350, 5th Avenue, City of Watervliet, Albany County, New York, 12189, United States",
              "class": "place",
              "type": "house"
            },
            {
              "lat": "40.9161016",
              "lon": "-73.8071811",
              "display_name": "350, 5th Avenue, North Pelham, Village of Pelham, Town of Pelham, Westchester County, New York, 10803, United States",
              "class": "place",
              "type": "house"
            }
          ]
        }
      },
      "instruction": null,
      "connect": null,
      "tools": null,
      "failed": [],
      "reopens": null
    },
    {
      "action": "needs_key",
      "tool": "sonar_deep_research",
      "name": null,
      "note": "Perplexity Agent API (medium / deep-research preset) is the best tool for this",
      "query": "Latest version of the npm package react",
      "session_id": "session-3",
      "stakes": "standard",
      "area_state": null,
      "confidence": "med",
      "not_checked": [],
      "report": null,
      "out": null,
      "instruction": null,
      "connect": {
        "tool": "sonar_deep_research",
        "signup_url": "https://www.perplexity.ai/settings/api",
        "steps": [
          "Create a Perplexity account, or sign in.",
          "Open the API settings page.",
          "Add a payment method and buy some API credit.",
          "Generate an API key and copy it."
        ],
        "field": "PERPLEXITY_API_KEY"
      },
      "tools": null,
      "failed": [],
      "reopens": null
    }
  ],
  "reports": null,
  "text": "run r_example1\n[1] frankfurter (sonar_deep_research +0.07, needs a key) [settled, conf high; report this one]\n  EUR -> GBP on 2024-03-15: 1 EUR = 0.8541 GBP (rate 0.8541, ECB 2024-03-15)\n[2] nominatim [open, conf low; report this one]\n  {\"adapted_query\":\"geocode 350 Fifth Avenue, New York, NY, USA\",\"lat\":\"41.1033570\",\"lon\":\"-72.3659952\",\"display_name\":\"350, Fifth Avenue, Village of Greenport, Town of Southold, Suffolk County, New York, 11944, United States\",\"results\":[{\"lat\":\"41.1033570\",\"lon\":\"-72.3659952\",\"display_name\":\"350, Fifth Avenue, Village of Greenport, Town of Southold, Suffolk County, New York, 11944, United States\",\"class\":\"place\",\"type\":\"house\"},{\"lat\":\"42.7096512\",\"lon\":\"-73.7105988\",\"display_name\":\"350, 5th Avenue, City of Watervliet, Albany County, New York, 12189, United States\",\"class\":\"place\",\"type\":\"house\"},{\"lat\":\"40.9161016\",\"lon\":\"-73.8071811\",\"display_name\":\"350, 5th Avenue, North Pelham, Village of Pelham, Town of Pelham, Westchester County, New York, 10803, United States\",\"class\":\"place\",\"type\":\"house\"}]}\n[3] needs a key: sonar_deep_research is best. STOP; ask the user (signup https://www.perplexity.ai/settings/api)\n  1. Create a Perplexity account, or sign in.\n  2. Open the API settings page.\n  3. Add a payment method and buy some API credit.\n  4. Generate an API key and copy it.\n  then onboard('sonar_deep_research', <key>) and resend this item\nowed: r_example1/1, r_example1/2 → reports=[{item, score}] on next run"
}
```

A `useless` report on item 2, sent with the next lookup, reopens it. No other ready geocoder is close enough, so the item is handed back to the caller:

```sh
node examples/typescript/run.mjs 'USD to JPY exchange rate on 2023-01-02' --report r_example1/2=useless
```

```json
{
  "run": "r_example2",
  "items": [
    {
      "action": "run",
      "tool": "frankfurter",
      "name": null,
      "note": "sonar_deep_research +0.03, needs a key",
      "query": "USD to JPY exchange rate on 2023-01-02",
      "session_id": "session-1",
      "stakes": "commodity",
      "area_state": "open",
      "confidence": "high",
      "not_checked": [],
      "report": "always",
      "out": {
        "ok": true,
        "tool_id": "frankfurter",
        "query": "USD to JPY exchange rate on 2023-01-02",
        "adapted_query": null,
        "latency_ms": 200,
        "result": {
          "query": "USD to JPY exchange rate on 2023-01-02",
          "adapted_query": "USD -> JPY on 2023-01-02",
          "provider": "Frankfurter (ECB reference rates)",
          "tool_kind": "currency exchange / conversion",
          "base": "USD",
          "target": "JPY",
          "amount": 1.0,
          "rate": 130.69,
          "converted": 130.69,
          "requested_date": "2023-01-02",
          "rate_date": "2023-01-02",
          "human": "1 USD = 130.69 JPY (rate 130.69, ECB 2023-01-02)"
        }
      },
      "instruction": null,
      "connect": null,
      "tools": null,
      "failed": [],
      "reopens": null
    },
    {
      "action": "do_yourself",
      "tool": null,
      "name": null,
      "note": "nominatim useless",
      "query": "Geocode 350 Fifth Avenue, New York to latitude and longitude",
      "session_id": "session-2",
      "stakes": "commodity",
      "area_state": null,
      "confidence": null,
      "not_checked": [],
      "report": null,
      "out": null,
      "instruction": null,
      "connect": null,
      "tools": null,
      "failed": [
        {
          "tool": "nominatim",
          "error": "useless"
        }
      ],
      "reopens": "r_example1/2"
    }
  ],
  "reports": {
    "accepted": 1,
    "failed": []
  },
  "text": "run r_example2\n[1] frankfurter (sonar_deep_research +0.03, needs a key) [open, conf high; report this one]\n  USD -> JPY on 2023-01-02: 1 USD = 130.69 JPY (rate 130.69, ECB 2023-01-02)\n[2] do it yourself, for r_example1/2 (nominatim useless; nothing else close)\nowed: r_example2/1 → reports=[{item, score}] on next run\nreports: 1 accepted"
}
```
