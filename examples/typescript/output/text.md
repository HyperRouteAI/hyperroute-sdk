# Text recommendation

[`text.mjs`](../text.mjs) requests `format="text"` and prints the complete text response.

```sh
node examples/typescript/text.mjs
```

Example output:

```text
session: s-998b0cbcc62d4379
verdict: interpose
status:  needs_facets (pick is provisional; a refine facet could reorder it)
refine:  format, output_was_returned, snippet_quality, completeness, relevance, references_present, citation_existence, freshness, source_quality, cited_references, citation_support, explanation_quality

  tool                 name                                                  price          use        why
→ tavily_search        Tavily Search API                                     $0.0080/query  needs_key  highest-ranked: capability 0.98; meets the required capability bar; effective $0.0080/query.
  sonar_deep_research  Perplexity Agent API (medium / deep-research preset)  $0.0200/query  needs_key  lower capability (0.96 vs 0.98); pricier ($0.0200 vs $0.0080/query).
  pubmed               PubMed (NCBI E-utilities)                             free           ready      lower capability (0.94 vs 0.98).
  crossref+references  crossref+references                                   free           ready      lower capability (0.94 vs 0.98).
  perplexity_sonar     Perplexity Agent API (fast preset)                    $0.0130/query  needs_key  lower capability (0.91 vs 0.98); pricier ($0.0130 vs $0.0080/query).
  semantic_scholar     Semantic Scholar Graph API                            free           needs_key  lower capability (0.89 vs 0.98).
  serp_search          SerpAPI (Google)                                      $0.0075/query  needs_key  lower capability (0.88 vs 0.98).
  openalex             OpenAlex Works API                                    free           ready      lower capability (0.86 vs 0.98).
  unpaywall            Unpaywall (via Crossref)                              free           ready      lower capability (0.85 vs 0.98).
  europe_pmc           Europe PMC                                            free           ready      lower capability (0.83 vs 0.98).

confidence: high (on the pick)
act: execute('pubmed', <query>)  — the user can already run it; 'tavily_search' scores 0.05 higher but needs a key  — or set a refine facet and re-route first

```
