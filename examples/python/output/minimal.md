# Minimal recommendation

[`minimal.py`](../minimal.py) requests `detail="min"` and prints the complete minimal response.

```sh
python examples/python/minimal.py
```

Example output:

```json
{
  "session_id": "s-03444b0ccab14e42",
  "kind": "ranked",
  "status": "needs_facets",
  "verdict": "interpose",
  "best": {
    "id": "tavily_search",
    "name": "Tavily Search API",
    "why": "highest-ranked: capability 0.98; meets the required capability bar; effective $0.0080/query.",
    "price": "$0.0080/query",
    "use": "needs_key",
    "confidence": "high"
  },
  "alts": [
    {
      "id": "sonar_deep_research",
      "name": "Perplexity Agent API (medium / deep-research preset)",
      "why": "lower capability (0.96 vs 0.98); pricier ($0.0200 vs $0.0080/query).",
      "price": "$0.0200/query",
      "use": "needs_key"
    },
    {
      "id": "pubmed",
      "name": "PubMed (NCBI E-utilities)",
      "why": "lower capability (0.94 vs 0.98).",
      "price": "free",
      "use": "ready"
    },
    {
      "id": "crossref+references",
      "name": "crossref+references",
      "why": "lower capability (0.94 vs 0.98).",
      "price": "free",
      "use": "ready"
    },
    {
      "id": "perplexity_sonar",
      "name": "Perplexity Agent API (fast preset)",
      "why": "lower capability (0.91 vs 0.98); pricier ($0.0130 vs $0.0080/query).",
      "price": "$0.0130/query",
      "use": "needs_key"
    },
    {
      "id": "semantic_scholar",
      "name": "Semantic Scholar Graph API",
      "why": "lower capability (0.89 vs 0.98).",
      "price": "free",
      "use": "needs_key"
    },
    {
      "id": "serp_search",
      "name": "SerpAPI (Google)",
      "why": "lower capability (0.88 vs 0.98).",
      "price": "$0.0075/query",
      "use": "needs_key"
    },
    {
      "id": "openalex",
      "name": "OpenAlex Works API",
      "why": "lower capability (0.86 vs 0.98).",
      "price": "free",
      "use": "ready"
    },
    {
      "id": "unpaywall",
      "name": "Unpaywall (via Crossref)",
      "why": "lower capability (0.85 vs 0.98).",
      "price": "free",
      "use": "ready"
    },
    {
      "id": "europe_pmc",
      "name": "Europe PMC",
      "why": "lower capability (0.83 vs 0.98).",
      "price": "free",
      "use": "ready"
    }
  ],
  "refine": [
    "format",
    "output_was_returned",
    "snippet_quality",
    "completeness",
    "relevance",
    "references_present",
    "citation_existence",
    "freshness",
    "source_quality",
    "cited_references",
    "citation_support",
    "explanation_quality"
  ],
  "act": "execute('pubmed', <query>)  — the user can already run it; 'tavily_search' scores 0.05 higher but needs a key  — or set a refine facet and re-route first"
}
```
