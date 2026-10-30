# Ranking

[`ranking.py`](../ranking.py) prints the stored ranking that decided one run item.

```sh
python examples/python/ranking.py --run r_example1 --item 2
```

Example output:

```text
session: session-2
verdict: interpose
status:  needs_facets (pick is provisional; a refine facet could reorder it)
refine:  output_was_returned, format, references_present, citation_existence, citation_support, relevance, verdict_accuracy, source_quality, safety, snippet_quality, explanation_quality, freshness

  tool              name                                 price          use        why
→ nominatim         OpenStreetMap Nominatim (Geocoding)  free           ready      highest-ranked: capability 0.88; meets the required capability bar; effective $0.0000/query.
  google_maps       Google Maps Geocoding                $0.0050/query  needs_key  falls short of the required capability bar for this task.
  exa               Exa Search                           free           needs_key  falls short of the required capability bar for this task.
  browse_ai         Browse AI                            free           needs_key  falls short of the required capability bar for this task.
  dropbox_sign_api  Dropbox Sign API                     free           needs_key  falls short of the required capability bar for this task.
  site_spy          Site Spy                             free           needs_key  falls short of the required capability bar for this task.
  peopledatalabs    People Data Labs                     $0.2800/query  needs_key  falls short of the required capability bar for this task.
  snaptrade         SnapTrade                            free           needs_key  falls short of the required capability bar for this task.
  page_deltas       Page Deltas                          free           needs_key  falls short of the required capability bar for this task.
  api_data_gov      api.data.gov gateway (openFDA)       free           needs_key  falls short of the required capability bar for this task.

confidence: low (on the pick)
act: this is the route the run acted on; to run a different row, send the item again with "tool": "<id>"
```
