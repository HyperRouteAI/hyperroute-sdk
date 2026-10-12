# Minimal recommendation

[`minimal.py`](../minimal.py) requests `detail="min"` and prints the complete minimal response.

```sh
python examples/python/minimal.py
```

Example output:

```json
{
  "session_id": "s-9903eb3f15b9456b",
  "kind": "ranked",
  "status": "needs_facets",
  "verdict": "interpose",
  "best": {
    "id": "pubmed",
    "name": "PubMed (NCBI E-utilities)",
    "why": "highest-ranked: capability 0.98; meets the required capability bar; effective $0.0000/query.",
    "price": "free",
    "use": "ready",
    "confidence": "high"
  },
  "alts": [
    {
      "id": "kagi_search",
      "name": "Kagi Search API",
      "why": "lower capability (0.94 vs 0.98); pricier ($0.0120 vs $0.0000/query).",
      "price": "$0.0120/query",
      "use": "needs_key"
    },
    {
      "id": "unpaywall",
      "name": "Unpaywall (via Crossref)",
      "why": "lower capability (0.85 vs 0.98).",
      "price": "free",
      "use": "ready"
    },
    {
      "id": "ddg_search",
      "name": "DuckDuckGo Search (MCP)",
      "why": "lower capability (0.91 vs 0.98).",
      "price": "free",
      "use": "soon"
    },
    {
      "id": "openalex",
      "name": "OpenAlex Works API",
      "why": "lower capability (0.86 vs 0.98).",
      "price": "free",
      "use": "ready"
    },
    {
      "id": "tavily_search",
      "name": "Tavily Search API",
      "why": "lower capability (0.83 vs 0.98); pricier ($0.0080 vs $0.0000/query).",
      "price": "$0.0080/query",
      "use": "needs_key"
    },
    {
      "id": "sonar_deep_research",
      "name": "Perplexity Agent API (medium / deep-research preset)",
      "why": "lower capability (0.78 vs 0.98); pricier ($0.0200 vs $0.0000/query).",
      "price": "$0.0200/query",
      "use": "needs_key"
    },
    {
      "id": "europe_pmc",
      "name": "Europe PMC",
      "why": "falls short of the required capability bar for this task.",
      "price": "free",
      "use": "ready"
    },
    {
      "id": "arxiv",
      "name": "arXiv API",
      "why": "falls short of the required capability bar for this task.",
      "price": "free",
      "use": "ready"
    },
    {
      "id": "brave_search",
      "name": "Brave Search API",
      "why": "falls short of the required capability bar for this task.",
      "price": "$0.0050/query",
      "use": "needs_key"
    }
  ],
  "refine": [
    "format",
    "snippet_quality",
    "explanation_quality",
    "transparency",
    "citation_existence",
    "relevance",
    "freshness",
    "verdict_accuracy",
    "references_present",
    "output_was_returned",
    "safety",
    "completeness"
  ],
  "act": "execute('pubmed', <query>)  — or set a refine facet and re-route first"
}
```
