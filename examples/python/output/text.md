# Text recommendation

[`text.py`](../text.py) requests `format="text"` and prints the complete text response.

```sh
python examples/python/text.py
```

Example output:

```text
session: s-0478213cf96240b5
verdict: interpose
status:  needs_facets (pick is provisional; a refine facet could reorder it)
refine:  format, snippet_quality, explanation_quality, transparency, citation_existence, relevance, freshness, verdict_accuracy, references_present, output_was_returned, safety, completeness

  tool                 name                                                  price          use        why
→ pubmed               PubMed (NCBI E-utilities)                             free           ready      highest-ranked: capability 0.98; meets the required capability bar; effective $0.0000/query.
  kagi_search          Kagi Search API                                       $0.0120/query  needs_key  lower capability (0.94 vs 0.98); pricier ($0.0120 vs $0.0000/query).
  unpaywall            Unpaywall (via Crossref)                              free           ready      lower capability (0.85 vs 0.98).
  ddg_search           DuckDuckGo Search (MCP)                               free           soon       lower capability (0.91 vs 0.98).
  openalex             OpenAlex Works API                                    free           ready      lower capability (0.86 vs 0.98).
  tavily_search        Tavily Search API                                     $0.0080/query  needs_key  lower capability (0.83 vs 0.98); pricier ($0.0080 vs $0.0000/query).
  sonar_deep_research  Perplexity Agent API (medium / deep-research preset)  $0.0200/query  needs_key  lower capability (0.78 vs 0.98); pricier ($0.0200 vs $0.0000/query).
  europe_pmc           Europe PMC                                            free           ready      falls short of the required capability bar for this task.
  arxiv                arXiv API                                             free           ready      falls short of the required capability bar for this task.
  brave_search         Brave Search API                                      $0.0050/query  needs_key  falls short of the required capability bar for this task.

confidence: high (on the pick)
act: execute('pubmed', <query>)  — or set a refine facet and re-route first
```
