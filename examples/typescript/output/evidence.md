# Full recommendation

[`evidence.mjs`](../evidence.mjs) requests `detail="full"` with `evidence_k=3` and prints every returned field, including scores, facets, probe evidence, and judgments.

```sh
node examples/typescript/evidence.mjs
```

Example output:

```json
{
  "session_id": "s-be04ce67cc5c46cd",
  "kind": "ranked",
  "status": "needs_facets",
  "provisional": true,
  "best": {
    "tool_id": "tavily_search",
    "name": "Tavily Search API",
    "variant": null,
    "capabilities": [
      "web_search",
      "realtime"
    ],
    "description": "AI-optimized search API designed for LLM applications. Returns clean, relevant results with high snippet quality.",
    "kind": "external_tool",
    "endpoint": {
      "api_type": "rest",
      "base_url": "https://api.tavily.com",
      "status_url": "https://app.tavily.com"
    },
    "reason": "highest-ranked: capability 0.98; meets the required capability bar; effective $0.0080/query.",
    "capability": 0.9798,
    "band": 0.0059,
    "cap_lcb": 0.9739,
    "rank": 0.9879,
    "price": {
      "amount": 0.008,
      "per_query_usd": 0.008,
      "currency": "USD",
      "confidence": "high",
      "selected_plan": "pay_as_you_go",
      "held": false,
      "estimated": true,
      "cost_unknown": false,
      "breakdown": [
        {
          "plan_id": "pay_as_you_go",
          "kind": "metered",
          "plan_group": "tavily",
          "effective_usd": 0.008,
          "held": false,
          "currency": "USD",
          "confidence": "high",
          "overridden": false
        }
      ]
    },
    "calling": {
      "tool_id": "tavily_search",
      "coordinator_class": false,
      "executable": true,
      "endpoint": {
        "base_url": "https://api.tavily.com",
        "api_type": "rest"
      },
      "adapter": {
        "type": "llm"
      },
      "auth": {
        "method": "api_key",
        "env_var": "TAVILY_API_KEY",
        "connected": false
      },
      "summary": {
        "usability": "connect_key",
        "auth_method": "api_key",
        "api_type": "rest",
        "connected": false,
        "free": false,
        "how": "connect a key → app.tavily.com/home",
        "signup_url": "https://app.tavily.com/home"
      },
      "connect": {
        "tool_id": "tavily_search",
        "name": "Tavily Search API",
        "auth_method": "api_key",
        "signup_url": "https://app.tavily.com/home",
        "instructions": "  1. Create a Tavily account — it comes with free monthly credits.\n  2. Open the API Keys section of the dashboard.\n  3. Create a key and copy it.",
        "methods": [
          {
            "auth_method": "api_key",
            "label": "Tavily API key",
            "signup_url": "https://app.tavily.com/home",
            "instructions": [
              "Create a Tavily account — it comes with free monthly credits.",
              "Open the API Keys section of the dashboard.",
              "Create a key and copy it."
            ],
            "fields": [
              {
                "key": "TAVILY_API_KEY",
                "label": "Tavily API key",
                "secret": true,
                "required": true,
                "help": "Dashboard → API Keys → Create"
              }
            ]
          }
        ],
        "fields": [
          {
            "key": "TAVILY_API_KEY",
            "label": "Tavily API key",
            "secret": true,
            "required": true,
            "help": "Dashboard → API Keys → Create"
          }
        ],
        "source": "evaluator",
        "connect_via": {
          "surface": "POST /credentials/connect",
          "method": "Tavily API key",
          "field_key": "TAVILY_API_KEY",
          "payload": {
            "tool_id": "tavily_search",
            "api_key": "<paste your key here>"
          },
          "curl": "curl -s https://hyperroute.io/credentials/connect -H 'content-type: application/json' -d '{\"tool_id\":\"tavily_search\",\"api_key\":\"<YOUR_KEY>\"}'"
        }
      }
    },
    "facets": [
      {
        "name": "capability",
        "kano": "must_be",
        "weight": 1,
        "threshold": 0.5,
        "raw": 0.9739,
        "contribution": 0.9635
      },
      {
        "name": "price",
        "kano": "performance",
        "weight": 0.3,
        "threshold": 0.5,
        "raw": 0.9885,
        "contribution": 0.2965
      },
      {
        "name": "no_machine_harm",
        "kano": "must_be",
        "weight": 2,
        "threshold": 0.5,
        "raw": 1,
        "contribution": 2
      }
    ],
    "evidence": {
      "n_real": 602,
      "n_near": 24,
      "near_mean": 0.721,
      "dist": [
        0.567,
        0.917,
        1,
        0.967,
        1,
        0.9,
        1,
        1,
        0.267,
        1,
        0.633,
        0.4,
        0.333,
        0.933,
        1,
        0.967,
        0.783,
        0.733,
        0,
        1,
        0.95,
        0,
        0,
        0.95
      ],
      "probes": [
        {
          "probe_id": "obs-28642",
          "similarity": 0.97,
          "task_text": "Find recent papers by Geoffrey Hinton on neural networks published in the last few years.",
          "adapted_input": "Find recent papers by Geoffrey Hinton on neural networks published in the last few years.",
          "score": 0.567,
          "redacted": null,
          "output_chars": 20000,
          "truncated": true,
          "created_at": "2026-08-12T17:17:38.587502Z",
          "judges": [
            {
              "facet": "capability",
              "verdict": "partial",
              "score": 0.567,
              "rationale": "The tool successfully identifies specific recent work by Geoffrey Hinton, such as the 'Forward-Forwa | The tool returned a Wikipedia page about Geoffrey Hinton, which is not a list of recent papers. The  | The tool's answer field accurately names some recent papers by Geoffrey Hinton (e.g., 'The Forward-F",
              "panel": [
                {
                  "model": "google/gemma-4-26b-a4b-it",
                  "rationale": "The tool successfully identifies specific recent work by Geoffrey Hinton, such as the 'Forward-Forward Algorithm', which is a genuine recent contribution. The 'answer' field provides a helpful summary, and the search results include a highly relevant Wikipedia snippet that confirms his recent career…",
                  "score": 0.8
                },
                {
                  "model": "deepseek/deepseek-v4-flash",
                  "rationale": "The tool returned a Wikipedia page about Geoffrey Hinton, which is not a list of recent papers. The 'answer' field mentions 'The Forward-Forward Algorithm' and 'Layer Normalization' but these are not verified by the actual results, and the snippet does not include paper titles or publication years. …",
                  "score": 0.4
                },
                {
                  "model": "xiaomi/mimo-v2.5",
                  "rationale": "The tool's answer field accurately names some recent papers by Geoffrey Hinton (e.g., 'The Forward-Forward Algorithm'), which aligns with the ground truth, but the visible search results only show a general Wikipedia page, not direct links to indexed papers. The response partially addresses the quer…",
                  "score": 0.5
                }
              ]
            },
            {
              "facet": "relevance",
              "verdict": "poor",
              "score": 0.25,
              "rationale": "The top search result is a Wikipedia biography page, which is tangentially related but does not provide direct access to recent papers, requiring the user to dig for relevant information.",
              "panel": [
                {
                  "model": "deepseek/deepseek-v4-flash",
                  "rationale": "The top result is a Wikipedia page that provides background but does not directly list recent papers, and the answer mentions only two papers without clear publication years or links to actual papers, mixing relevant content with noise.",
                  "label": "partial",
                  "value": 0.5
                },
                {
                  "model": "google/gemma-4-26b-a4b-it",
                  "rationale": "The tool provides a direct answer mentioning specific recent papers like 'The Forward-Forward Algorithm', though the search results themselves are dominated by a Wikipedia biography rather than a list of papers.",
                  "label": "good",
                  "value": 0.75
                },
                {
                  "model": "xiaomi/mimo-v2.5",
                  "rationale": "The top search result is a Wikipedia biography page, which is tangentially related but does not provide direct access to recent papers, requiring the user to dig for relevant information.",
                  "label": "poor",
                  "value": 0.25
                }
              ]
            },
            {
              "facet": "source_quality",
              "verdict": "tertiary",
              "score": 0.4,
              "rationale": "The tool provides a Wikipedia snippet as its primary source of information, which is categorized as a tertiary aggregator.",
              "panel": [
                {
                  "model": "google/gemma-4-26b-a4b-it",
                  "rationale": "The tool provides a Wikipedia snippet as its primary source of information, which is categorized as a tertiary aggregator.",
                  "label": "tertiary",
                  "value": 0.4
                },
                {
                  "model": "deepseek/deepseek-v4-flash",
                  "rationale": "The tool's output primarily cites Wikipedia, a tertiary aggregator, rather than providing direct links to peer-reviewed papers or primary sources.",
                  "label": "tertiary",
                  "value": 0.4
                },
                {
                  "model": "xiaomi/mimo-v2.5",
                  "rationale": "The tool's output includes a citation from Wikipedia, which is explicitly listed as a tertiary aggregator in the rubric.",
                  "label": "tertiary",
                  "value": 0.4
                }
              ]
            },
            {
              "facet": "references_present",
              "verdict": "present",
              "score": 1,
              "rationale": "The tool output includes a specific URL (https://en.wikipedia.org/wiki/Geoffrey_Hinton) as a source for the information provided.",
              "panel": [
                {
                  "model": "google/gemma-4-26b-a4b-it",
                  "rationale": "The tool output includes a specific URL (https://en.wikipedia.org/wiki/Geoffrey_Hinton) as a source for the information provided.",
                  "label": "present",
                  "value": 1
                },
                {
                  "model": "deepseek/deepseek-v4-flash",
                  "rationale": "The tool's output includes explicit source references, such as the Wikipedia URL for Geoffrey Hinton.",
                  "label": "present",
                  "value": 1
                },
                {
                  "model": "xiaomi/mimo-v2.5",
                  "rationale": "The tool's output includes explicit URLs in the results section, which are source references that a reader can follow back to the underlying material.",
                  "label": "present",
                  "value": 1
                }
              ]
            },
            {
              "facet": "output_was_returned",
              "verdict": "returned",
              "score": 1,
              "rationale": "The tool returned a non-empty JSON object containing an answer and search results.",
              "panel": [
                {
                  "model": "google/gemma-4-26b-a4b-it",
                  "rationale": "The tool returned a non-empty JSON object containing an answer and search results.",
                  "label": "returned",
                  "value": 1
                },
                {
                  "model": "deepseek/deepseek-v4-flash",
                  "rationale": "The tool's output contains multiple results including an AI-generated summary answering the query and a detailed search result snippet from Wikipedia, so non-empty output was returned.",
                  "label": "returned",
                  "value": 1
                },
                {
                  "model": "xiaomi/mimo-v2.5",
                  "rationale": "The tool returned a non-empty JSON output containing fields like 'answer' and 'results', which is usable for the query.",
                  "label": "returned",
                  "value": 1
                }
              ]
            }
          ],
          "raw_output": "{\n  \"query\": \"Find recent papers by Geoffrey Hinton on neural networks published in the last few years.\",\n  \"adapted_query\": \"Find recent papers by Geoffrey Hinton on neural networks published in the last few years.\",\n  \"provider\": \"Tavily\",\n  \"answer\": \"Geoffrey Hinton's recent papers include \\\"The Forward-Forward Algorithm\\\" and \\\"Layer Normalization.\\\" He also discussed new learning algorithms for neural networks in 2022.\",\n  \"total_results\": 17,\n  \"api_params\": {\n    \"search_depth\": \"advanced\",\n    \"include_answer\": true,\n    \"include_raw_content\": false,\n    \"max_results\": 20\n  },\n  \"results\": [\n    {\n      \"title\": \"Geoffrey Hinton\",\n      \"url\": \"https://en.wikipedia.org/wiki/Geoffrey_Hinton\",\n      \"snippet\": \"| Hinton at his home in 2026 |\\n| Born | Geoffrey Everest Hinton   (1947-12-06) 6 December 1947 (age 78)  London, England, UK |\\n| Education |  King's College, Cambridge (MA \\\"MA (Cantab)\\\"))  University of Edinburgh (PhD) |\\n| Known for |  Applications of backpropagation  Boltzmann machine  Restricted Boltzmann machine  Deep learning  Deep belief network  Knowledge distillation (\\\"Dark knowledge\\\")  Capsule neural networks  Mixture of experts  Product of experts  Time delay neural network  t-SNE  AlexNet  Dropout \\\"Dilution (neural networks)\\\") |\\n| Spouses |  Joanne  Rosalind Zalin   \\u200b (died 1994)\\u200b  Jacqueline Ford  \\u200b   \\u200b (m. 1997; died 2018) …[truncated]"
        },
        {
          "probe_id": "obs-28362",
          "similarity": 0.968,
          "task_text": "Find scientific literature on graphene field-effect transistors for biosensing applications.",
          "adapted_input": "Find scientific literature on graphene field-effect transistors for biosensing applications.",
          "score": 0.917,
          "redacted": null,
          "output_chars": 20000,
          "truncated": true,
          "created_at": "2026-08-12T10:25:14.686269Z",
          "judges": [
            {
              "facet": "capability",
              "verdict": "pass",
              "score": 0.917,
              "rationale": "The tool performed exceptionally well. It provided highly relevant, authoritative scientific literat | The tool returned relevant, authoritative results (PMC, MDPI) with real citations and URLs, directly | The tool returned a relevant and diverse set of authoritative results from indexed scientific source",
              "panel": [
                {
                  "model": "google/gemma-4-26b-a4b-it",
                  "rationale": "The tool performed exceptionally well. It provided highly relevant, authoritative scientific literature (including links to PMC and MDPI) that directly addresses the query. The snippets contain specific, real-world citations with authors, journals, years, and DOIs, which perfectly aligns with the gr…",
                  "score": 1
                },
                {
                  "model": "deepseek/deepseek-v4-flash",
                  "rationale": "The tool returned relevant, authoritative results (PMC, MDPI) with real citations and URLs, directly addressing the query for scientific literature on graphene FET biosensors. The answer provides a concise summary. No off-topic or fabricated results. Minor clutter in snippet formatting does not detr…",
                  "score": 0.85
                },
                {
                  "model": "xiaomi/mimo-v2.5",
                  "rationale": "The tool returned a relevant and diverse set of authoritative results from indexed scientific sources (e.g., PubMed, MDPI) on graphene FET biosensors, including recent peer-reviewed papers with correct titles and valid URLs, aligning well with the ground truth. Minor deductions for not explicitly li…",
                  "score": 0.9
                }
              ]
            },
            {
              "facet": "relevance",
              "verdict": "excellent",
              "score": 1,
              "rationale": "The top results are directly relevant, providing peer-reviewed articles and reviews specifically on graphene field-effect transistors for biosensing, which matches the query intent for scientific literature.",
              "panel": [
                {
                  "model": "deepseek/deepseek-v4-flash",
                  "rationale": "The top results are directly relevant, providing peer-reviewed articles and reviews specifically on graphene field-effect transistors for biosensing, which matches the query intent for scientific literature.",
                  "label": "excellent",
                  "value": 1
                },
                {
                  "model": "google/gemma-4-26b-a4b-it",
                  "rationale": "The top results provide highly relevant, high-quality scientific literature including specific titles, authors, and DOI/journal information directly related to graphene field-effect transistors for biosensing.",
                  "label": "excellent",
                  "value": 1
                },
                {
                  "model": "xiaomi/mimo-v2.5",
                  "rationale": "The top results are highly relevant, directly addressing graphene field-effect transistors for biosensing with peer-reviewed scientific literature from reputable sources.",
                  "label": "excellent",
                  "value": 1
                }
              ]
            },
            {
              "facet": "source_quality",
              "verdict": "primary",
              "score": 1,
              "rationale": "The tool output includes citations to peer-reviewed papers from reputable journals such as Proceedings of the National Academy of Sciences, Nano Letters, and Advanced Materials, which are primary authoritative sources.",
              "panel": [
                {
                  "model": "deepseek/deepseek-v4-flash",
                  "rationale": "The tool output includes citations to peer-reviewed papers from reputable journals such as Proceedings of the National Academy of Sciences, Nano Letters, and Advanced Materials, which are primary authoritative sources.",
                  "label": "primary",
                  "value": 1
                },
                {
                  "model": "google/gemma-4-26b-a4b-it",
                  "rationale": "The tool provides citations to peer-reviewed scientific journals such as PNAS, Nano Letters, and Advanced Materials.",
                  "label": "primary",
                  "value": 1
                },
                {
                  "model": "xiaomi/mimo-v2.5",
                  "rationale": "The tool's results cite peer-reviewed academic papers from sources like PubMed Central and MDPI, which are primary sources.",
                  "label": "primary",
                  "value": 1
                }
              ]
            },
            {
              "facet": "references_present",
              "verdict": "present",
              "score": 1,
              "rationale": "The tool output provides specific URLs, article titles, and detailed citation markers (authors, journals, DOIs) for several scientific papers.",
              "panel": [
                {
                  "model": "google/gemma-4-26b-a4b-it",
                  "rationale": "The tool output provides specific URLs, article titles, and detailed citation markers (authors, journals, DOIs) for several scientific papers.",
                  "label": "present",
                  "value": 1
                },
                {
                  "model": "deepseek/deepseek-v4-flash",
                  "rationale": "The output includes multiple results with URLs and citation details (e.g., DOI, PubMed, Google Scholar links) that a reader can follow back to the original papers.",
                  "label": "present",
                  "value": 1
                },
                {
                  "model": "xiaomi/mimo-v2.5",
                  "rationale": "The tool's output includes explicit source references such as URLs and citation markers in the search results, enabling readers to follow them back to the underlying material.",
                  "label": "present",
                  "value": 1
                }
              ]
            },
            {
              "facet": "output_was_returned",
              "verdict": "returned",
              "score": 1,
              "rationale": "The tool returned a non-empty JSON object containing a summary and a list of relevant search results with titles and URLs.",
              "panel": [
                {
                  "model": "google/gemma-4-26b-a4b-it",
                  "rationale": "The tool returned a non-empty JSON object containing a summary and a list of relevant search results with titles and URLs.",
                  "label": "returned",
                  "value": 1
                },
                {
                  "model": "deepseek/deepseek-v4-flash",
                  "rationale": "The tool returned a JSON object containing an answer, results list, and other fields, which is non-empty output.",
                  "label": "returned",
                  "value": 1
                },
                {
                  "model": "xiaomi/mimo-v2.5",
                  "rationale": "The tool output contains a non-empty JSON response with search results, an answer, and structured data.",
                  "label": "returned",
                  "value": 1
                }
              ]
            }
          ],
          "raw_output": "{\n  \"query\": \"Find scientific literature on graphene field-effect transistors for biosensing applications.\",\n  \"adapted_query\": \"Find scientific literature on graphene field-effect transistors for biosensing applications.\",\n  \"provider\": \"Tavily\",\n  \"answer\": \"Graphene field-effect transistors (GFETs) are used for biosensing due to their high sensitivity and fast response. They detect biomolecules by changes in charge carrier density. GFETs have been applied to detect various biomolecules including proteins and DNA.\",\n  \"total_results\": 20,\n  \"api_params\": {\n    \"search_depth\": \"advanced\",\n    \"include_answer\": true,\n    \"include_raw_content\": false,\n    \"max_results\": 20\n  },\n  \"results\": [\n    {\n      \"title\": \"Challenges for Field-Effect-Transistor-Based Graphene Biosensors\",\n      \"url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC10817696\",\n      \"snippet\": \"155..Gao N., Gao T., Yang X., Dai X., Zhou W., Zhang A., Lieber C.M.. Specific Detection of Biomolecules in Physiological Solutions Using Graphene Transistor Biosensors. _Proc. Natl. Acad. Sci. USA_. 2016. 113:14633-14638. doi: 10.1073/pnas.1625010114 [DOI] [PMC free article] [PubMed] [Google Scholar]\\n   156..Bliem C., Piccinini E., Knoll W., Azzaroni O.. Enzyme Multilayers on Graphene-Based FETs for Biosensing Applications. In: Kumar C.V., editors. _Methods in Enzymology_. Amsterdam, The Netherlands: Elsevier; 2018. Vo …[truncated]"
        },
        {
          "probe_id": "obs-32704",
          "similarity": 0.966,
          "task_text": "Find the 2026 Applied Energy paper by Chen et al. on turning current mismatch into an advantage to suppress hysteresis in two-terminal tandem cells, and give me its DOI.",
          "adapted_input": "Chen 2026 Applied Energy tandem two-terminal current mismatch hysteresis suppression perovskite",
          "score": 1,
          "redacted": null,
          "output_chars": 20000,
          "truncated": true,
          "created_at": "2026-08-29T10:47:02.333840Z",
          "judges": [
            {
              "facet": "capability",
              "verdict": "pass",
              "score": 1,
              "rationale": "Deterministic check — matched 1/1 required string(s).",
              "panel": null
            }
          ],
          "raw_output": "{\n  \"query\": \"Chen 2026 Applied Energy tandem two-terminal current mismatch hysteresis suppression perovskite\",\n  \"adapted_query\": \"Chen 2026 Applied Energy tandem two-terminal current mismatch hysteresis suppression perovskite\",\n  \"provider\": \"Tavily\",\n  \"answer\": \"Two-terminal perovskite/silicon tandem solar cells face current mismatch issues, leading to hysteresis and performance instability. Strategies to mitigate this include precise interface passivation and ion suppression. Research shows these cells may not perform optimally in all climates due to spectral variations.\",\n  \"total_results\": 20,\n  \"api_params\": {\n    \"search_depth\": \"advanced\",\n    \"include_answer\": true,\n    \"include_raw_content\": \"markdown\",\n    \"max_results\": 20\n  },\n  \"top_documents\": [\n    {\n      \"url\": \"https://www.sciencedirect.com/science/article/abs/pii/S0306261926012328\",\n      \"title\": \"Turning current mismatch into advantage: suppressing hysteresis and improving operational stability in two-terminal perovskite/silicon tandem solar cells\",\n      \"text\": \"[Skip to main content](https://www.sciencedirect.com/science/article/abs/pii/S0306261926012328#screen-reader-main-content)[Skip to article](https://www.sciencedirect.com/science/article/abs/pii/S0306261926012328#screen-reader-main-title)\\n\\n[![Image 2: Elsevier logo](https://www.sciencedirect.com/shared-assets/24/images/elsevier-non-solus-new-g …[truncated]"
        }
      ]
    },
    "evidence_teaser": {
      "task_text": "Find recent papers by Geoffrey Hinton on neural networks published in the last few years.",
      "verdict": "returned",
      "score": 0.567,
      "similarity": 0.97,
      "n_real": 602
    }
  },
  "runner_ups": [
    {
      "tool_id": "sonar_deep_research",
      "name": "Perplexity Agent API (medium / deep-research preset)",
      "variant": null,
      "capabilities": [
        "deep_research",
        "web_search",
        "realtime",
        "references",
        "synthesis",
        "fact_check"
      ],
      "description": "Composite deep-research agent on Perplexity's Agent API, `medium` preset (their rename of deep-research; the model is Perplexity-managed and reported per response). Issues multiple web searches and page fetches per query, cross-checks claims, and synthesises a long-form answer with inline citations. Shares the PERPLEXITY_API_KEY credential with perplexity_sonar.",
      "kind": "external_tool",
      "endpoint": {
        "api_type": "rest",
        "base_url": "https://api.perplexity.ai",
        "status_url": "https://status.perplexity.com"
      },
      "reason": "lower capability (0.96 vs 0.98); pricier ($0.0200 vs $0.0080/query).",
      "capability": 0.9586,
      "band": 0.0203,
      "cap_lcb": 0.9384,
      "rank": 0.9712,
      "price": {
        "amount": 0.02,
        "per_query_usd": 0.02,
        "currency": "USD",
        "confidence": "medium",
        "selected_plan": "api",
        "held": false,
        "estimated": true,
        "cost_unknown": false,
        "breakdown": [
          {
            "plan_id": "api",
            "kind": "metered",
            "plan_group": "perplexity_api",
            "effective_usd": 0.02,
            "held": false,
            "currency": "USD",
            "confidence": "medium",
            "overridden": false
          }
        ]
      },
      "calling": {
        "tool_id": "sonar_deep_research",
        "coordinator_class": false,
        "executable": true,
        "endpoint": {
          "base_url": "https://api.perplexity.ai",
          "api_type": "rest"
        },
        "adapter": {
          "type": "none"
        },
        "auth": {
          "method": "api_key",
          "env_var": "PERPLEXITY_API_KEY",
          "connected": false
        },
        "summary": {
          "usability": "connect_key",
          "auth_method": "api_key",
          "api_type": "rest",
          "connected": false,
          "free": false,
          "how": "connect a key → www.perplexity.ai/settings/api",
          "signup_url": "https://www.perplexity.ai/settings/api"
        },
        "connect": {
          "tool_id": "sonar_deep_research",
          "name": "Perplexity Agent API (medium / deep-research preset)",
          "auth_method": "api_key",
          "signup_url": "https://www.perplexity.ai/settings/api",
          "instructions": "  1. Create a Perplexity account, or sign in.\n  2. Open the API settings page.\n  3. Add a payment method and buy some API credit.\n  4. Generate an API key and copy it.",
          "methods": [
            {
              "auth_method": "api_key",
              "label": "Perplexity API key",
              "signup_url": "https://www.perplexity.ai/settings/api",
              "instructions": [
                "Create a Perplexity account, or sign in.",
                "Open the API settings page.",
                "Add a payment method and buy some API credit.",
                "Generate an API key and copy it."
              ],
              "fields": [
                {
                  "key": "PERPLEXITY_API_KEY",
                  "label": "Perplexity API key",
                  "secret": true,
                  "required": true,
                  "help": "Settings → API → Generate"
                }
              ]
            }
          ],
          "fields": [
            {
              "key": "PERPLEXITY_API_KEY",
              "label": "Perplexity API key",
              "secret": true,
              "required": true,
              "help": "Settings → API → Generate"
            }
          ],
          "source": "evaluator",
          "connect_via": {
            "surface": "POST /credentials/connect",
            "method": "Perplexity API key",
            "field_key": "PERPLEXITY_API_KEY",
            "payload": {
              "tool_id": "sonar_deep_research",
              "api_key": "<paste your key here>"
            },
            "curl": "curl -s https://hyperroute.io/credentials/connect -H 'content-type: application/json' -d '{\"tool_id\":\"sonar_deep_research\",\"api_key\":\"<YOUR_KEY>\"}'"
          }
        }
      },
      "facets": [
        {
          "name": "capability",
          "kano": "must_be",
          "weight": 1,
          "threshold": 0.5,
          "raw": 0.9384,
          "contribution": 0.9137
        },
        {
          "name": "price",
          "kano": "performance",
          "weight": 0.3,
          "threshold": 0.5,
          "raw": 0.9714,
          "contribution": 0.2914
        },
        {
          "name": "no_machine_harm",
          "kano": "must_be",
          "weight": 2,
          "threshold": 0.5,
          "raw": 1,
          "contribution": 2
        }
      ],
      "evidence": {
        "n_real": 165,
        "n_near": 24,
        "near_mean": 0.924,
        "dist": [
          1,
          0.9,
          0.94,
          1,
          0.967,
          0.733,
          0.983,
          1,
          0.933,
          0.7,
          0.95,
          1,
          0.933,
          0.967,
          0.733,
          0.967,
          0.867,
          0.867,
          0.733,
          1,
          1,
          1,
          1,
          1
        ],
        "probes": [
          {
            "probe_id": "obs-826",
            "similarity": 0.958,
            "task_text": "Find the LIGO Scientific Collaboration paper reporting the first direct observation of gravitational waves from a binary black hole merger (GW150914).",
            "adapted_input": "Find the LIGO Scientific Collaboration paper reporting the first direct observation of gravitational waves from a binary black hole merger (GW150914).",
            "score": 1,
            "redacted": null,
            "output_chars": 20000,
            "truncated": true,
            "created_at": "2026-05-17T19:11:49.804516Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "The tool provided a highly detailed and accurate response. It correctly identified the paper title,  | The tool correctly identifies the exact paper requested: 'Observation of Gravitational Waves from a  | The tool accurately identifies the paper with the exact title, authors (in standard citation form), ",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provided a highly detailed and accurate response. It correctly identified the paper title, authors (Abbott et al.), year (2016), journal (Physical Review Letters), DOI, and the arXiv identifier. It even included the internal LIGO report number and specific astrophysical details, exceeding t…",
                    "score": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool correctly identifies the exact paper requested: 'Observation of Gravitational Waves from a Binary Black Hole Merger' by B. P. Abbott et al., published in Physical Review Letters (116, 061102, 2016), with DOI 10.1103/PhysRevLett.116.061102, arXiv:1602.03837. It provides full bibliographic de…",
                    "score": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool accurately identifies the paper with the exact title, authors (in standard citation form), year, venue, and DOI as specified in the ground truth, providing a comprehensive and correct response.",
                    "score": 1
                  }
                ]
              },
              {
                "facet": "format",
                "verdict": "unstructured",
                "score": 0,
                "rationale": "The tool output is provided as a long-form prose response in Markdown format rather than a machine-parseable JSON or structured data object.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool output is provided as a long-form prose response in Markdown format rather than a machine-parseable JSON or structured data object.",
                    "label": "unstructured",
                    "value": 0
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool output is a JSON object with clearly defined fields (query, provider, tool_kind, answer), making it machine-parseable structured data despite the prose content within the answer field.",
                    "label": "structured",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output is presented as a detailed prose narrative with no machine-parseable structured data format such as JSON or a list.",
                    "label": "unstructured",
                    "value": 0
                  }
                ]
              },
              {
                "facet": "freshness",
                "verdict": "not_applicable",
                "score": 1,
                "rationale": "The query asks for a specific scientific paper regarding a historical discovery, which is a static fact where freshness is irrelevant.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The query asks for a specific scientific paper regarding a historical discovery, which is a static fact where freshness is irrelevant.",
                    "label": "not_applicable",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The query asks for a specific historical paper from 2016, which is a static fact where freshness is irrelevant.",
                    "label": "not_applicable",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The query is about identifying a historical paper from 2016, which is a static fact where freshness is irrelevant as the publication details are fixed and do not change over time.",
                    "label": "not_applicable",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "The tool directly identifies the correct paper, providing the title, authors, year, journal, DOI, and arXiv identifier as requested.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool directly identifies the correct paper, providing the title, authors, year, journal, DOI, and arXiv identifier as requested.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool output directly and accurately identifies the discovery paper for GW150914 with its title, authors, year, DOI, and LIGO document number, fully satisfying the query intent with high-quality source information.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output directly identifies the exact paper requested with complete bibliographic details, perfectly matching the query intent and ground truth.",
                    "label": "excellent",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool cites the peer-reviewed paper itself (Physical Review Letters) and its arXiv preprint as the basis for its answer.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool cites the peer-reviewed paper itself (Physical Review Letters) and its arXiv preprint as the basis for its answer.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool output cites peer-reviewed scientific papers (e.g., Phys. Rev. Lett. 116, 061102) and official LIGO document numbers as primary authoritative sources.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output directly cites and provides bibliographic details for the original peer-reviewed paper in Physical Review Letters, which is a primary source for scientific research.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "snippet_quality",
                "verdict": "informative",
                "score": 1,
                "rationale": "The output provides a highly detailed description including the paper title, authors, journal, year, DOI, arXiv identifier, and specific scientific findings, allowing the user to fully assess relevance without further searching.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The output provides a highly detailed description including the paper title, authors, journal, year, DOI, arXiv identifier, and specific scientific findings, allowing the user to fully assess relevance without further searching.",
                    "label": "informative",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output provides a detailed summary including the exact title, authors, year, DOI, arXiv ID, and specific scientific details (masses, distance, significance) that allow full assessment of relevance without needing to click through.",
                    "label": "informative",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The output provides specific facts such as the paper title, authors, publication details, DOI, and key scientific findings, allowing the reader to assess relevance without clicking through.",
                    "label": "informative",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool provides explicit citation markers, the DOI, the arXiv identifier, and the specific journal publication details.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides explicit citation markers, the DOI, the arXiv identifier, and the specific journal publication details.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The output contains multiple explicit source references including a DOI, arXiv ID, and internal LIGO document number, along with citation markers, allowing a reader to trace back to the original paper.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output includes explicit source references like the arXiv ID (1602.03837) and DOI (10.1103/PhysRevLett.116.061102), which are direct identifiers for the paper.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool provided a detailed and comprehensive response containing the requested information.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provided a detailed and comprehensive response containing the requested information.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a substantial, non-empty answer describing the requested paper with bibliographic details and analysis.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool output is non-empty and provides a detailed response with bibliographic information about the paper, meeting the criteria for usable output.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find the LIGO Scientific Collaboration paper reporting the first direct observation of gravitational waves from a binary black hole merger (GW150914).\",\n  \"provider\": \"Perplexity (sonar-deep-research)\",\n  \"tool_kind\": \"composite deep-research agent (multi-step search + LLM synthesis)\",\n  \"answer\": \"# The First Direct Detection of Gravitational Waves from a Binary Black Hole Merger: The LIGO GW150914 Discovery Paper\\n\\nThe foundational paper reporting the first direct observation of gravitational waves from a binary black hole merger is the LIGO\\u2013Virgo collaboration article titled **\\u201cObservation of Gravitational Waves from a Binary Black Hole Merger\\u201d**, with report number **LIGO\\u2011P150914**, published in *Physical Review Letters* (volume 116, article 061102, 2016) and first released as **arXiv:1602.03837**.[7][7][7] This paper, authored by B. P. Abbott and the LIGO Scientific Collaboration and Virgo Collaboration, presents the detection and analysis of the event designated **GW150914**, a transient gravitational\\u2011wave signal recorded on 14 September 2015 by the two Advanced LIGO detectors, and interprets it as the inspiral, merger, and ringdown of a binary black hole system with component masses of approximately \\\\(36 M_\\\\odot\\\\) and \\\\(29 M_\\\\odot\\\\) at a luminosity distance of roughly 410 Mpc.[7][7][12] The paper establishes that the observed …[truncated]"
          },
          {
            "probe_id": "obs-641",
            "similarity": 0.949,
            "task_text": "Devlin et al. 2018 paper on bidirectional Transformer pre-training for language understanding (BERT).",
            "adapted_input": "Devlin et al. 2018 paper on bidirectional Transformer pre-training for language understanding (BERT).",
            "score": 0.9,
            "redacted": null,
            "output_chars": 20000,
            "truncated": true,
            "created_at": "2026-05-17T09:26:21.565254Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 0.9,
                "rationale": "The tool provided a highly detailed and accurate response. It correctly identified the title, all au | The tool's output is highly relevant, accurate, and comprehensive. It correctly identifies the paper | The tool accurately identifies the BERT paper by its title and authors, provides a comprehensive ana",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provided a highly detailed and accurate response. It correctly identified the title, all authors, and the core technical contributions of the paper. While the output was truncated (likely due to length limits of the tool's synthesis), the information provided was perfectly aligned with the …",
                    "score": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output is highly relevant, accurate, and comprehensive. It correctly identifies the paper's title, authors, year, and key contributions (bidirectional Transformer, masked LM, next sentence prediction, fine-tuning). It provides detailed historical context, architecture, and impact, closely…",
                    "score": 0.9
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool accurately identifies the BERT paper by its title and authors, provides a comprehensive analysis of its content, and mentions the year (with a slight variation to 2018/2019), which is largely correct. However, it does not explicitly include the persistent identifier (arXiv ID or URL) as spe…",
                    "score": 0.8
                  }
                ]
              },
              {
                "facet": "format",
                "verdict": "semi_structured",
                "score": 0.5,
                "rationale": "The output is a valid JSON object with metadata fields, but the main answer is unstructured prose (Markdown text), so it is only partially machine-parseable for the expected structured fields.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returns a long-form prose report in Markdown format rather than a machine-parseable JSON object or a list of search results with specific fields.",
                    "label": "unstructured",
                    "value": 0
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The output is a valid JSON object with metadata fields, but the main answer is unstructured prose (Markdown text), so it is only partially machine-parseable for the expected structured fields.",
                    "label": "semi_structured",
                    "value": 0.5
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The output is a JSON object with an unstructured prose answer embedded in the 'answer' field, matching the definition of partially structured data.",
                    "label": "semi_structured",
                    "value": 0.5
                  }
                ]
              },
              {
                "facet": "freshness",
                "verdict": "not_applicable",
                "score": 1,
                "rationale": "The query is about a specific academic paper from 2018, which is a static historical fact where freshness is not a relevant metric.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The query is about a specific academic paper from 2018, which is a static historical fact where freshness is not a relevant metric.",
                    "label": "not_applicable",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The query is about a specific 2018 research paper, so freshness of evidence is irrelevant as it is a static historical fact.",
                    "label": "not_applicable",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The query targets a historical paper from 2018, which is a static fact with no dependence on current evidence.",
                    "label": "not_applicable",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "The tool directly identifies the specific paper requested and provides a comprehensive, high-quality technical summary that addresses the query intent perfectly.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool directly identifies the specific paper requested and provides a comprehensive, high-quality technical summary that addresses the query intent perfectly.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool output directly and comprehensively addresses the query intent by providing a detailed analysis of the Devlin et al. 2018 BERT paper, including its title, authors, context, and impact, making it highly relevant and useful.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool output directly and comprehensively identifies the specified BERT paper with accurate details, fully addressing the query intent without any irrelevant information.",
                    "label": "excellent",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool's output is a technical analysis of the specific peer-reviewed paper requested, and while the snippet itself is a synthesis, it is built upon and cites the primary research paper (Devlin et al., 2018).",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool's output is a technical analysis of the specific peer-reviewed paper requested, and while the snippet itself is a synthesis, it is built upon and cites the primary research paper (Devlin et al., 2018).",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output cites the original BERT paper and other peer-reviewed sources, which are primary academic sources.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output includes citations to peer-reviewed academic papers, which are classified as primary sources in the rubric.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "snippet_quality",
                "verdict": "informative",
                "score": 1,
                "rationale": "The output provides a highly detailed technical summary of the paper, including its core objectives (MLM and NSP), its architectural significance, and its historical context in NLP.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The output provides a highly detailed technical summary of the paper, including its core objectives (MLM and NSP), its architectural significance, and its historical context in NLP.",
                    "label": "informative",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output provides a comprehensive, detailed summary of the BERT paper including its title, authors, year, and specific technical descriptions, which allows the reader to assess relevance without needing to click through to external sources.",
                    "label": "informative",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output includes specific facts such as the paper title, authors, year, and detailed content summaries, allowing assessment of relevance without further action.",
                    "label": "informative",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool's output includes specific citation markers (e.g., [5], [1], [4]) throughout the text to refer to underlying sources.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool's output includes specific citation markers (e.g., [5], [1], [4]) throughout the text to refer to underlying sources.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool output includes multiple citation markers like [5][1][4] and others that serve as explicit source references, allowing a reader to trace back to the underlying material.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool output includes explicit citation markers such as [5], [1], and [4] throughout the text, which are specific references that a reader can follow back to the underlying material.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool provided a detailed, non-empty response containing information about the requested paper.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provided a detailed, non-empty response containing information about the requested paper.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a detailed synthesis about the BERT paper, which is non-empty and usable.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool provided a non-empty, detailed answer addressing the query, confirming usable output was returned.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Devlin et al. 2018 paper on bidirectional Transformer pre-training for language understanding (BERT).\",\n  \"provider\": \"Perplexity (sonar-deep-research)\",\n  \"tool_kind\": \"composite deep-research agent (multi-step search + LLM synthesis)\",\n  \"answer\": \"# BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding \\u2013 A Comprehensive Analysis of Devlin et al. (2018/2019)\\n\\nThe paper \\u201cBERT: Pre-training of Deep Bidirectional Transformers for Language Understanding\\u201d by Devlin, Chang, Lee and Toutanova introduced a deceptively simple but transformative idea: take the encoder half of the Transformer architecture, train it at large scale on raw text with two carefully designed self-supervised objectives\\u2014masked language modeling and next sentence prediction\\u2014and then reuse this single, generic model across a wide variety of downstream natural language processing (NLP) tasks with minimal architectural modification.[5][1][4] BERT (Bidirectional Encoder Representations from Transformers) is trained to jointly condition on both left and right context in all layers, in contrast to earlier unidirectional language models, which unlocks richer contextual representations that substantially improve performance on benchmarks such as GLUE, MultiNLI and SQuAD.[5][5][13] Remarkably, the same pre-trained BERT model can be adapted to classificat …[truncated]"
          },
          {
            "probe_id": "obs-549",
            "similarity": 0.949,
            "task_text": "Find the 1986 Nature paper by Rumelhart, Hinton and Williams that introduced back-propagation for training multi-layer neural networks.",
            "adapted_input": "Find the 1986 Nature paper by Rumelhart, Hinton and Williams that introduced back-propagation for training multi-layer neural networks.",
            "score": 0.94,
            "redacted": null,
            "output_chars": 20000,
            "truncated": true,
            "created_at": "2026-05-17T05:09:51.106423Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 0.94,
                "rationale": "The tool correctly identified the paper title, authors, year, and journal. It provided highly detail | The tool accurately identifies the requested paper with correct title, authors, year, venue, and vol | The tool accurately identified the paper's title, authors, year, and venue, matching the ground trut",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool correctly identified the paper title, authors, year, and journal. It provided highly detailed bibliographic information including volume, issue, and page numbers, which exceeds the requirements of the ground truth. Although the output was truncated at the end, the core answer to the user's …",
                    "score": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool accurately identifies the requested paper with correct title, authors, year, venue, and volume/issue/pages. It provides additional context and citation details, closely matching the ground truth. However, it does not explicitly state the DOI or URL, which are expected as persistent identifi…",
                    "score": 0.92
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool accurately identified the paper's title, authors, year, and venue, matching the ground truth. It also provided additional bibliographic details and context. However, it did not explicitly include the persistent identifiers (DOI and URL) specified in the ground truth, which is a minor gap.",
                    "score": 0.9
                  }
                ]
              },
              {
                "facet": "format",
                "verdict": "unstructured",
                "score": 0,
                "rationale": "The tool output is provided as a long-form prose response in Markdown format rather than a machine-parseable JSON or structured data object.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool output is provided as a long-form prose response in Markdown format rather than a machine-parseable JSON or structured data object.",
                    "label": "unstructured",
                    "value": 0
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool output is a valid JSON object with distinct fields, allowing programmatic extraction of the query, provider, tool kind, and the answer text.",
                    "label": "structured",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool output is a JSON object with structured keys like 'query' and 'provider', but the 'answer' field contains unstructured prose, making it partially machine-parseable.",
                    "label": "semi_structured",
                    "value": 0.5
                  }
                ]
              },
              {
                "facet": "freshness",
                "verdict": "not_applicable",
                "score": 1,
                "rationale": "The query asks for a specific historical scientific paper from 1986, which is a static fact where freshness is irrelevant.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The query asks for a specific historical scientific paper from 1986, which is a static fact where freshness is irrelevant.",
                    "label": "not_applicable",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The query requests a historical paper from 1986, a static fact for which freshness is irrelevant.",
                    "label": "not_applicable",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The query is about a static historical paper from 1986, where freshness is irrelevant to the fact itself.",
                    "label": "not_applicable",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "The tool directly identifies the correct paper, including the title, authors, year, and specific volume/issue details, perfectly matching the query intent.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool directly identifies the correct paper, including the title, authors, year, and specific volume/issue details, perfectly matching the query intent.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool output directly and accurately identifies the requested 1986 Nature paper by Rumelhart, Hinton, and Williams with full bibliographic details, perfectly matching the query intent.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool output directly identifies the specified 1986 Nature paper with accurate title, authors, venue, and bibliographic details, fully answering the query intent with high-quality sources.",
                    "label": "excellent",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool cites the specific peer-reviewed paper in Nature and mentions authoritative databases like NASA ADS to provide the bibliographic information.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool cites the specific peer-reviewed paper in Nature and mentions authoritative databases like NASA ADS to provide the bibliographic information.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output cites the original 1986 Nature paper by Rumelhart, Hinton, and Williams, which is a peer-reviewed primary source.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool cites primary sources such as the peer-reviewed paper via NASA ADS and official repositories, which are authoritative for accessing the original publication.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "snippet_quality",
                "verdict": "informative",
                "score": 1,
                "rationale": "The output provides a highly detailed description including the full title, complete author list, specific volume/issue/page numbers, and a summary of the paper's technical content.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The output provides a highly detailed description including the full title, complete author list, specific volume/issue/page numbers, and a summary of the paper's technical content.",
                    "label": "informative",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output provides specific bibliographic details including exact title, authors, year, journal, volume, pages, and citation references, allowing the reader to assess relevance without needing to click through.",
                    "label": "informative",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output contains specific bibliographic details and descriptive content that allow assessment of relevance without clicking.",
                    "label": "informative",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool includes explicit citation markers (e.g., [7], [8], [3]) throughout the text to refer to underlying sources.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool includes explicit citation markers (e.g., [7], [8], [3]) throughout the text to refer to underlying sources.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The output contains explicit citation markers (e.g., [7], [8], [3]) that point to specific sources, which a reader can use to locate the original material.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output includes explicit citation markers such as [7] and references to specific sources like Nature volume and page numbers.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool provided a detailed response containing the title, authors, year, and publication details of the requested paper.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provided a detailed response containing the title, authors, year, and publication details of the requested paper.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool provided a substantial, non-empty answer with detailed bibliographic information and analysis.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool output includes a detailed answer with the paper's title, authors, year, venue, and additional context, indicating non-empty and usable output.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find the 1986 Nature paper by Rumelhart, Hinton and Williams that introduced back-propagation for training multi-layer neural networks.\",\n  \"provider\": \"Perplexity (sonar-deep-research)\",\n  \"tool_kind\": \"composite deep-research agent (multi-step search + LLM synthesis)\",\n  \"answer\": \"# The 1986 Nature Paper \\u201cLearning representations by back-propagating errors\\u201d by Rumelhart, Hinton and Williams\\n\\nThe paper you are looking for is the 1986 *Nature* article titled **\\u201cLearning representations by back-propagating errors\\u201d** by **David E. Rumelhart, Geoffrey E. Hinton and Ronald J. Williams**, published in *Nature*, volume 323, issue 6088, pages 533\\u2013536, on 9 October 1986.[7][7][7] In modern bibliographic form, it is usually cited as: Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). Learning representations by back-propagating errors. *Nature*, 323(6088), 533\\u2013536.[8][8] The paper describes a general learning procedure, now universally called **backpropagation**, for adjusting the connection weights in multi-layer networks of neuron-like units so as to minimize a differentiable measure of error between the network\\u2019s actual outputs and desired targets.[3][7] As the authors emphasize in the abstract, this process leads internal \\u201chidden\\u201d units to develop distributed representations that capture important structure in the …[truncated]"
          }
        ]
      },
      "evidence_teaser": {
        "task_text": "Find the LIGO Scientific Collaboration paper reporting the first direct observation of gravitational waves from a binary black hole merger (GW150914).",
        "verdict": "excellent",
        "score": 1,
        "similarity": 0.958,
        "n_real": 165
      }
    },
    {
      "tool_id": "pubmed",
      "name": "PubMed (NCBI E-utilities)",
      "variant": null,
      "capabilities": [
        "paper_search",
        "academic",
        "references",
        "abstracts",
        "medical_literature",
        "biomedical"
      ],
      "description": "Canonical biomedical and life-science literature index maintained by the US National Library of Medicine. MeSH-indexed; supports clinical filters, publication-type metadata, and PMID-keyed lookups. Returns title, authors, abstract, journal, publication date, DOI, and publication types.",
      "kind": "external_tool",
      "endpoint": {
        "api_type": "rest",
        "base_url": "https://eutils.ncbi.nlm.nih.gov",
        "status_url": "https://www.ncbi.nlm.nih.gov"
      },
      "reason": "lower capability (0.94 vs 0.98).",
      "capability": 0.9435,
      "band": 0.0168,
      "cap_lcb": 0.9266,
      "rank": 0.9689,
      "price": {
        "amount": 0,
        "per_query_usd": 0,
        "currency": "USD",
        "confidence": "high",
        "selected_plan": "free",
        "held": false,
        "estimated": true,
        "cost_unknown": false,
        "breakdown": [
          {
            "plan_id": "free",
            "kind": "free",
            "plan_group": null,
            "effective_usd": 0,
            "held": false,
            "currency": "USD",
            "confidence": "high",
            "overridden": false
          }
        ]
      },
      "calling": {
        "tool_id": "pubmed",
        "coordinator_class": false,
        "executable": true,
        "endpoint": {
          "base_url": "https://eutils.ncbi.nlm.nih.gov",
          "api_type": "rest"
        },
        "adapter": {
          "type": "llm"
        },
        "auth": {
          "method": "none"
        },
        "summary": {
          "usability": "ready",
          "auth_method": "none",
          "api_type": "rest",
          "connected": false,
          "free": true,
          "how": "free · ready to use",
          "signup_url": null
        }
      },
      "facets": [
        {
          "name": "capability",
          "kano": "must_be",
          "weight": 1,
          "threshold": 0.5,
          "raw": 0.9266,
          "contribution": 0.8973
        },
        {
          "name": "price",
          "kano": "performance",
          "weight": 0.3,
          "threshold": 0.5,
          "raw": 1,
          "contribution": 0.3
        },
        {
          "name": "no_machine_harm",
          "kano": "must_be",
          "weight": 2,
          "threshold": 0.5,
          "raw": 1,
          "contribution": 2
        }
      ],
      "evidence": {
        "n_real": 181,
        "n_near": 24,
        "near_mean": 0.784,
        "dist": [
          0,
          0.933,
          1,
          1,
          1,
          0.933,
          0.4,
          0.433,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          1,
          0.95,
          0.933,
          1,
          1,
          0.033,
          0.2,
          0,
          1
        ],
        "probes": [
          {
            "probe_id": "obs-31831",
            "similarity": 0.97,
            "task_text": "Find recent papers by Geoffrey Hinton on neural networks published in the last few years.",
            "adapted_input": "Hinton neural networks 2022 2023 2024",
            "score": 0,
            "redacted": null,
            "output_chars": 335,
            "truncated": false,
            "created_at": "2026-08-26T02:34:35.232411Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "fail",
                "score": 0,
                "rationale": "The tool returned zero results for a very high-profile researcher. The adapted query 'Hinton neural  | The tool returned zero results for a query that should have returned real papers by Geoffrey Hinton  | The tool returned an empty list of results, completely failing to surface any papers by Geoffrey Hin",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned zero results for a very high-profile researcher. The adapted query 'Hinton neural networks 2022 2023 2024' was too restrictive and poorly constructed for a PubMed search, failing to find any relevant papers that clearly exist in the scientific literature. This is a failure of the t…",
                    "score": 0
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned zero results for a query that should have returned real papers by Geoffrey Hinton on neural networks published in recent years (e.g., 2022–2024). This is a complete failure to retrieve relevant, accurate information, as the ground truth confirms such papers exist. The output is emp…",
                    "score": 0
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned an empty list of results, completely failing to surface any papers by Geoffrey Hinton as expected by the ground truth. This empty output is directly penalized per the tool contract and represents a total failure in relevance, accuracy, and completeness for the query.",
                    "score": 0
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "irrelevant",
                "score": 0,
                "rationale": "The tool returned zero results, failing to provide any papers that address the user's query intent.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned zero results, failing to provide any papers that address the user's query intent.",
                    "label": "irrelevant",
                    "value": 0
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned zero results despite the existence of real papers by Geoffrey Hinton on neural networks in the specified timeframe, completely missing the query intent.",
                    "label": "irrelevant",
                    "value": 0
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned zero results, completely missing the query intent to find recent papers by Geoffrey Hinton on neural networks.",
                    "label": "irrelevant",
                    "value": 0
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "not_applicable",
                "score": 1,
                "rationale": "The tool returned zero results, so no citations were provided to evaluate.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned zero results, so no citations were provided to evaluate.",
                    "label": "not_applicable",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned zero results and provided no citations, so the source quality facet does not apply.",
                    "label": "not_applicable",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool output returned zero results with no citations provided, so the source quality facet does not apply as absence is handled by citation_existence.",
                    "label": "not_applicable",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "absent",
                "score": 0,
                "rationale": "The tool output returned zero results and contains no references to any papers or sources.",
                "panel": [
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool output returned zero results and contains no references to any papers or sources.",
                    "label": "absent",
                    "value": 0
                  },
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned zero results, and therefore provided no source references, URLs, or document names.",
                    "label": "absent",
                    "value": 0
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool output contains no explicit source references, as it returned zero results without any URLs, document names, or citation markers.",
                    "label": "absent",
                    "value": 0
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "empty",
                "score": 0,
                "rationale": "The tool returned zero results and an empty list for the query.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned zero results and an empty list for the query.",
                    "label": "empty",
                    "value": 0
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned zero results, meaning it did not find any papers by Geoffrey Hinton despite their existence, resulting in an empty output.",
                    "label": "empty",
                    "value": 0
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned a structured JSON response with fields like query and results, which is non-empty output despite having zero results.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find recent papers by Geoffrey Hinton on neural networks published in the last few years.\",\n  \"adapted_query\": \"Hinton neural networks 2022 2023 2024\",\n  \"provider\": \"PubMed (NCBI E-utilities)\",\n  \"tool_kind\": \"biomedical literature search (MeSH-indexed)\",\n  \"total_results\": 0,\n  \"returned_results\": 0,\n  \"results\": []\n}"
          },
          {
            "probe_id": "obs-28354",
            "similarity": 0.968,
            "task_text": "Find scientific literature on graphene field-effect transistors for biosensing applications.",
            "adapted_input": "graphene field-effect transistor biosensor",
            "score": 0.933,
            "redacted": null,
            "output_chars": 20000,
            "truncated": true,
            "created_at": "2026-08-12T09:56:23.063234Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 0.933,
                "rationale": "The tool performed exactly as expected for a PubMed API. It adapted the query into a searchable form | The tool returned a large set of relevant peer-reviewed papers on graphene FET biosensors, with the  | The tool returns relevant, accurate, and structured literature on graphene FET biosensors with real ",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool performed exactly as expected for a PubMed API. It adapted the query into a searchable format, identified a significant number of relevant results (498), and returned highly relevant, high-quality metadata (titles, authors, abstracts, PMIDs, and DOIs) for papers that directly address the us…",
                    "score": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a large set of relevant peer-reviewed papers on graphene FET biosensors, with the top results directly matching the query. The first two papers are clearly on-topic, with correct titles, authors, and DOIs, and the total result count (498) indicates good coverage. The output satisfi…",
                    "score": 0.9
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returns relevant, accurate, and structured literature on graphene FET biosensors with real PMIDs, titles, authors, and abstracts, matching the ground truth expectations. It adapts the query appropriately, provides current papers (2024), and offers clear metadata. Minor truncation in the pro…",
                    "score": 0.9
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "The top results are highly relevant, high-quality peer-reviewed papers that directly address graphene field-effect transistors for biosensing applications as requested.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The top results are highly relevant, high-quality peer-reviewed papers that directly address graphene field-effect transistors for biosensing applications as requested.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The top two results are directly relevant, peer-reviewed papers on graphene FET biosensors, matching the query intent with high-quality sources.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returns multiple peer-reviewed papers with titles and abstracts directly addressing graphene field-effect transistors for biosensing, perfectly matching the query intent.",
                    "label": "excellent",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool returns citations from PubMed, a database of peer-reviewed biomedical literature, which are primary sources.",
                "panel": [
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returns citations from PubMed, a database of peer-reviewed biomedical literature, which are primary sources.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides citations to peer-reviewed journal articles from PubMed, which are considered primary scientific sources.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output cites peer-reviewed papers from PubMed, which are primary sources as per the rubric.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool provides explicit source references including PMIDs, DOIs, and direct URLs to the PubMed entries.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides explicit source references including PMIDs, DOIs, and direct URLs to the PubMed entries.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The output includes explicit source references such as PubMed URLs, DOIs, and citation information for each returned article.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The output includes explicit URLs and DOIs for each referenced paper, providing clear, followable references.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool returned a structured JSON object containing a list of relevant scientific publications with titles, abstracts, and metadata.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned a structured JSON object containing a list of relevant scientific publications with titles, abstracts, and metadata.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool produced a non-empty output containing 15 results with titles, authors, and abstracts related to graphene field-effect transistors for biosensing, rather than an error or empty response.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool output contains a non-empty JSON response with search results, including titles, abstracts, and other details for multiple papers.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find scientific literature on graphene field-effect transistors for biosensing applications.\",\n  \"adapted_query\": \"graphene field-effect transistor biosensor\",\n  \"provider\": \"PubMed (NCBI E-utilities)\",\n  \"tool_kind\": \"biomedical literature search (MeSH-indexed)\",\n  \"total_results\": 498,\n  \"returned_results\": 15,\n  \"results\": [\n    {\n      \"pmid\": \"38255502\",\n      \"title\": \"Challenges for Field-Effect-Transistor-Based Graphene Biosensors.\",\n      \"abstract\": \"Owing to its outstanding physical properties, graphene has attracted attention as a promising biosensor material. Field-effect-transistor (FET)-based biosensors are particularly promising because of their high sensitivity that is achieved through the high carrier mobility of graphene. However, graphene-FET biosensors have not yet reached widespread practical applications owing to several problems. In this review, the authors focus on graphene-FET biosensors and discuss their advantages, the challenges to their development, and the solutions to the challenges. The problem of Debye screening, in which the surface charges of the detection target are shielded and undetectable, can be solved by using small-molecule receptors and their deformations and by using enzyme reaction products. To address the complexity of sample components and the detection mechanisms of graphene-FET biosensors, the authors outline measu …[truncated]"
          },
          {
            "probe_id": "obs-32817",
            "similarity": 0.964,
            "task_text": "Find the 2026 Phytomedicine paper by Meng et al. showing obacunone attenuates cholestatic liver disease via PPARα activation and gut microbiota remodeling. Give me the PubMed ID.",
            "adapted_input": "obacunone cholestatic PPARα gut microbiota Meng 2026",
            "score": 1,
            "redacted": null,
            "output_chars": 4164,
            "truncated": false,
            "created_at": "2026-08-29T11:55:47.593721Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "Deterministic check — matched 1/1 required string(s).",
                "panel": null
              }
            ],
            "raw_output": "{\n  \"query\": \"Find the 2026 Phytomedicine paper by Meng et al. showing obacunone attenuates cholestatic liver disease via PPAR\\u03b1 activation and gut microbiota remodeling. Give me the PubMed ID.\",\n  \"adapted_query\": \"obacunone cholestatic PPAR\\u03b1 gut microbiota Meng 2026\",\n  \"provider\": \"PubMed (NCBI E-utilities)\",\n  \"tool_kind\": \"biomedical literature search (MeSH-indexed)\",\n  \"total_results\": 1,\n  \"returned_results\": 1,\n  \"results\": [\n    {\n      \"pmid\": \"42551234\",\n      \"title\": \"Obacunone attenuates Cholestatic liver disease via PPAR\\u03b1 activation and gut microbiota remodeling.\",\n      \"abstract\": \"BACKGROUND: Cholestatic liver disease (CLD) comprises a collection of disorders marked by impaired bile formation or flow, which can progress to fibrosis, cirrhosis, and liver failure if left untreated. Although there have been significant advances in understanding its pathogenesis, effective pharmacotherapies are still limited; ursodeoxycholic acid (UDCA), the first-line treatment, exhibits an incomplete response in approximately 30-40% of patients. Obacunone (OBA), a naturally occurring limonoid triterpenoid, has shown potent anti-inflammatory and antioxidant effects in various models of liver injury; however, its role in CLD has yet to be investigated.\\nPURPOSE: To investigate the mechanism by which OBA ameliorates \\u03b1-naphthyl isothiocyanate (ANIT)/ethinyl estrad …[truncated]"
          }
        ]
      },
      "evidence_teaser": {
        "task_text": "Find recent papers by Geoffrey Hinton on neural networks published in the last few years.",
        "verdict": "not_applicable",
        "score": 0,
        "similarity": 0.97,
        "n_real": 181
      }
    },
    {
      "tool_id": "crossref+references",
      "name": "crossref+references",
      "variant": null,
      "capabilities": [
        "academic",
        "doi_metadata",
        "paper_search",
        "references"
      ],
      "description": "Crossref DOI resolution that additionally returns the deposited cited-reference DOI list in the same call, so the works a record cites are surfaced without a second lookup.",
      "kind": "external_tool",
      "endpoint": {
        "api_type": "rest",
        "base_url": "https://api.crossref.org",
        "status_url": "https://status.crossref.org"
      },
      "reason": "lower capability (0.94 vs 0.98).",
      "capability": 0.9375,
      "band": 0.0268,
      "cap_lcb": 0.9107,
      "rank": 0.9621,
      "price": {
        "amount": 0,
        "per_query_usd": 0,
        "currency": "USD",
        "confidence": "high",
        "selected_plan": "free",
        "held": false,
        "estimated": true,
        "cost_unknown": false,
        "breakdown": [
          {
            "plan_id": "free",
            "kind": "free",
            "plan_group": null,
            "effective_usd": 0,
            "held": false,
            "currency": "USD",
            "confidence": "high",
            "overridden": false
          }
        ]
      },
      "calling": {
        "tool_id": "crossref+references",
        "coordinator_class": false,
        "executable": true,
        "endpoint": {
          "base_url": "https://api.crossref.org",
          "api_type": "rest"
        },
        "adapter": {
          "type": "llm"
        },
        "auth": {
          "method": "none"
        },
        "summary": {
          "usability": "ready",
          "auth_method": "none",
          "api_type": "rest",
          "connected": false,
          "free": true,
          "how": "free · ready to use",
          "signup_url": null
        },
        "base_tool": "crossref",
        "adapter_mode": "references"
      },
      "facets": [
        {
          "name": "capability",
          "kano": "must_be",
          "weight": 1,
          "threshold": 0.5,
          "raw": 0.9107,
          "contribution": 0.875
        },
        {
          "name": "price",
          "kano": "performance",
          "weight": 0.3,
          "threshold": 0.5,
          "raw": 1,
          "contribution": 0.3
        },
        {
          "name": "no_machine_harm",
          "kano": "must_be",
          "weight": 2,
          "threshold": 0.5,
          "raw": 1,
          "contribution": 2
        }
      ],
      "evidence": {
        "n_real": 55,
        "n_near": 24,
        "near_mean": 0.667,
        "dist": [
          1,
          1,
          1,
          1,
          1,
          0.667,
          1,
          1,
          0,
          0.667,
          1,
          0.667,
          0.5,
          0.5,
          0,
          0.5,
          0.5,
          0,
          1,
          0.5,
          0,
          0.5,
          1,
          1
        ],
        "probes": [
          {
            "probe_id": "obs-33345",
            "similarity": 0.942,
            "task_text": "Find the 'Segment Anything' paper by Kirillov and colleagues from Meta AI.",
            "adapted_input": "{\"search\": \"Segment Anything\", \"year\": null}",
            "score": 1,
            "redacted": null,
            "output_chars": 19541,
            "truncated": false,
            "created_at": "2026-09-08T03:51:06.470034Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "Deterministic check — matched 1/1 required string(s).",
                "panel": null
              }
            ],
            "raw_output": "{\n  \"query\": \"Find the 'Segment Anything' paper by Kirillov and colleagues from Meta AI.\",\n  \"adapted_spec\": {\n    \"search\": \"Segment Anything\",\n    \"year\": null\n  },\n  \"lookup_mode\": \"title\",\n  \"provider\": \"Crossref\",\n  \"tool_kind\": \"citation metadata search (publisher-contributed)\",\n  \"total_results\": 79730,\n  \"returned_results\": 30,\n  \"results\": [\n    {\n      \"doi\": \"10.1109/iccv51070.2023.00371\",\n      \"title\": \"Segment Anything\",\n      \"authors\": [\n        \"Alexander Kirillov\",\n        \"Eric Mintun\",\n        \"Nikhila Ravi\",\n        \"Hanzi Mao\",\n        \"Chloe Rolland\",\n        \"Laura Gustafson\",\n        \"Tete Xiao\",\n        \"Spencer Whitehead\",\n        \"Alexander C. Berg\",\n        \"Wan-Yen Lo\",\n        \"Piotr Doll\\u00e1r\",\n        \"Ross Girshick\"\n      ],\n      \"year\": 2023,\n      \"container_title\": \"2023 IEEE/CVF International Conference on Computer Vision (ICCV)\",\n      \"type\": \"proceedings-article\",\n      \"cited_by_count\": 11074,\n      \"url\": \"https://doi.org/10.1109/iccv51070.2023.00371\",\n      \"subject\": [],\n      \"abstract\": \"\",\n      \"reference_count\": 115,\n      \"references\": [\n        \"10.1117/12.429489\",\n        \"10.1109/TPAMI.2010.161\",\n        \"10.1109/CVPR52688.2022.02047\",\n        \"10.1038/s41592-019-0582-9\",\n        \"10.1007/978-3-030-00919-9_42\",\n        \"10.1038/s41592-019-0612-7\",\n        \"10.1109/TPAMI.1986.4767851\",\n        \"10.1007/978-3-030-58452-8_13 …[truncated]"
          },
          {
            "probe_id": "obs-33174",
            "similarity": 0.888,
            "task_text": "Find the paper that introduced the Transformer architecture, 'Attention Is All You Need' by Vaswani and colleagues.",
            "adapted_input": "{\"search\": \"Attention Is All You Need\", \"year\": null}",
            "score": 1,
            "redacted": null,
            "output_chars": 16205,
            "truncated": false,
            "created_at": "2026-09-08T01:56:25.591211Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "Deterministic check — matched 1/1 required string(s).",
                "panel": null
              }
            ],
            "raw_output": "{\n  \"query\": \"Find the paper that introduced the Transformer architecture, 'Attention Is All You Need' by Vaswani and colleagues.\",\n  \"adapted_spec\": {\n    \"search\": \"Attention Is All You Need\",\n    \"year\": null\n  },\n  \"lookup_mode\": \"title\",\n  \"provider\": \"Crossref\",\n  \"tool_kind\": \"citation metadata search (publisher-contributed)\",\n  \"total_results\": 1233947,\n  \"returned_results\": 30,\n  \"results\": [\n    {\n      \"doi\": \"10.65215/ysbyhc05\",\n      \"title\": \"Attention Is All You Need\",\n      \"authors\": [\n        \"Ashish Vaswani\",\n        \"Noam Shazeer\",\n        \"Niki Parmar\",\n        \"Jakob Uszkoreit\",\n        \"Llion Jones\",\n        \"Aidan N.Gomez\",\n        \"Lukasz Kaiser\",\n        \"Illia Polosukhin\"\n      ],\n      \"year\": 2025,\n      \"container_title\": null,\n      \"type\": \"posted-content\",\n      \"cited_by_count\": 21,\n      \"url\": \"https://doi.org/10.65215/ysbyhc05\",\n      \"subject\": [],\n      \"abstract\": \"The dominant sequence transduction models are based on complex recurrent or convolutional neural networks in an encoder-decoder configuration. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely. Experiments on two machine translation tasks show these models to be superior in quality …[truncated]"
          },
          {
            "probe_id": "obs-35115",
            "similarity": 0.862,
            "task_text": "A July 2026 paper in an open-access journal described a new species of Colobus monkey discovered in Lomami National Park in the Democratic Republic of Congo, nicknamed 'Likweli' by local communities for its distinctive orange-cream muzzle patch. Its bibliography cites an earlier 2021 paper reporting a morphological analysis of newly found specimens of another Congo Basin primate, the Dryas monkey. What is the DOI of that cited paper, and what journal did it appear in?",
            "adapted_input": "{\"search\": \"Dryas monkey morphological Congo\", \"year\": 2021}",
            "score": 1,
            "redacted": null,
            "output_chars": 20000,
            "truncated": true,
            "created_at": "2026-09-12T15:08:06.854324Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "Deterministic check — matched 2/2 required string(s).",
                "panel": null
              }
            ],
            "raw_output": "{\n  \"query\": \"A July 2026 paper in an open-access journal described a new species of Colobus monkey discovered in Lomami National Park in the Democratic Republic of Congo, nicknamed 'Likweli' by local communities for its distinctive orange-cream muzzle patch. Its bibliography cites an earlier 2021 paper reporting a morphological analysis of newly found specimens of another Congo Basin primate, the Dryas monkey. What is the DOI of that cited paper, and what journal did it appear in?\",\n  \"adapted_spec\": {\n    \"search\": \"Dryas monkey morphological Congo\",\n    \"year\": 2021\n  },\n  \"lookup_mode\": \"keyword\",\n  \"provider\": \"Crossref\",\n  \"tool_kind\": \"citation metadata search (publisher-contributed)\",\n  \"total_results\": 241526,\n  \"returned_results\": 30,\n  \"results\": [\n    {\n      \"doi\": \"10.1371/journal.pone.0349857\",\n      \"title\": \"Likweli: A remarkable new species of Colobus monkey from the Lomami National Park, Democratic Republic of Congo\",\n      \"authors\": [\n        \"John A. Hart\",\n        \"Junior D. Amboko\",\n        \"Julia L. Arenson\",\n        \"Emma R. Horton\",\n        \"Kathryn F. Coates\",\n        \"Jean-Pierre I. Kapale\",\n        \"Mardoch\\u00e9 B. Koko\",\n        \"Terese B. Hart\",\n        \"Christopher C. Gilbert\",\n        \"Eric J. Sargis\",\n        \"Kate M. Detwiler\"\n      ],\n      \"year\": 2026,\n      \"container_title\": \"PLOS One\",\n      \"type\": \"journal-article\",\n      \"cited_by_c …[truncated]"
          }
        ]
      },
      "evidence_teaser": {
        "task_text": "Find the 'Segment Anything' paper by Kirillov and colleagues from Meta AI.",
        "verdict": "pass",
        "score": 1,
        "similarity": 0.942,
        "n_real": 55
      }
    },
    {
      "tool_id": "perplexity_sonar",
      "name": "Perplexity Agent API (fast preset)",
      "variant": null,
      "capabilities": [
        "web_search",
        "realtime",
        "references"
      ],
      "description": "Web-grounded LLM verifier on Perplexity's Agent API, `fast` preset (single-fact lookups with inline citations; the model is Perplexity-managed and reported per response). Performs live web search and synthesises a structured verdict per claim with citations. Verdicts via the FactCheckResult JSON schema (overall_rating + per-claim {claim, rating, explanation, sources}). Strong on fresh / niche / cross-domain claims where Google FCT is silent.",
      "kind": "external_tool",
      "endpoint": {
        "api_type": "rest",
        "base_url": "https://api.perplexity.ai",
        "status_url": "https://status.perplexity.com"
      },
      "reason": "lower capability (0.91 vs 0.98); pricier ($0.0130 vs $0.0080/query).",
      "capability": 0.9055,
      "band": 0.0395,
      "cap_lcb": 0.866,
      "rank": 0.9414,
      "price": {
        "amount": 0.013,
        "per_query_usd": 0.013,
        "currency": "USD",
        "confidence": "high",
        "selected_plan": "api",
        "held": false,
        "estimated": true,
        "cost_unknown": false,
        "breakdown": [
          {
            "plan_id": "api",
            "kind": "metered",
            "plan_group": "perplexity_api",
            "effective_usd": 0.013,
            "held": false,
            "currency": "USD",
            "confidence": "high",
            "overridden": false
          }
        ]
      },
      "calling": {
        "tool_id": "perplexity_sonar",
        "coordinator_class": false,
        "executable": true,
        "endpoint": {
          "base_url": "https://api.perplexity.ai",
          "api_type": "rest"
        },
        "adapter": {
          "type": "none"
        },
        "auth": {
          "method": "api_key",
          "env_var": "PERPLEXITY_API_KEY",
          "connected": false
        },
        "summary": {
          "usability": "connect_key",
          "auth_method": "api_key",
          "api_type": "rest",
          "connected": false,
          "free": false,
          "how": "connect a key → www.perplexity.ai/settings/api",
          "signup_url": "https://www.perplexity.ai/settings/api"
        },
        "connect": {
          "tool_id": "perplexity_sonar",
          "name": "Perplexity Agent API (fast preset)",
          "auth_method": "api_key",
          "signup_url": "https://www.perplexity.ai/settings/api",
          "instructions": "  1. Create a Perplexity account, or sign in.\n  2. Open the API settings page.\n  3. Add a payment method and buy some API credit.\n  4. Generate an API key and copy it.",
          "methods": [
            {
              "auth_method": "api_key",
              "label": "Perplexity API key",
              "signup_url": "https://www.perplexity.ai/settings/api",
              "instructions": [
                "Create a Perplexity account, or sign in.",
                "Open the API settings page.",
                "Add a payment method and buy some API credit.",
                "Generate an API key and copy it."
              ],
              "fields": [
                {
                  "key": "PERPLEXITY_API_KEY",
                  "label": "Perplexity API key",
                  "secret": true,
                  "required": true,
                  "help": "Settings → API → Generate"
                }
              ]
            }
          ],
          "fields": [
            {
              "key": "PERPLEXITY_API_KEY",
              "label": "Perplexity API key",
              "secret": true,
              "required": true,
              "help": "Settings → API → Generate"
            }
          ],
          "source": "evaluator",
          "connect_via": {
            "surface": "POST /credentials/connect",
            "method": "Perplexity API key",
            "field_key": "PERPLEXITY_API_KEY",
            "payload": {
              "tool_id": "perplexity_sonar",
              "api_key": "<paste your key here>"
            },
            "curl": "curl -s https://hyperroute.io/credentials/connect -H 'content-type: application/json' -d '{\"tool_id\":\"perplexity_sonar\",\"api_key\":\"<YOUR_KEY>\"}'"
          }
        }
      },
      "facets": [
        {
          "name": "capability",
          "kano": "must_be",
          "weight": 1,
          "threshold": 0.5,
          "raw": 0.866,
          "contribution": 0.8124
        },
        {
          "name": "price",
          "kano": "performance",
          "weight": 0.3,
          "threshold": 0.5,
          "raw": 0.9814,
          "contribution": 0.2944
        },
        {
          "name": "no_machine_harm",
          "kano": "must_be",
          "weight": 2,
          "threshold": 0.5,
          "raw": 1,
          "contribution": 2
        }
      ],
      "evidence": {
        "n_real": 226,
        "n_near": 24,
        "near_mean": 0.87,
        "dist": [
          0.983,
          0.933,
          0.95,
          0.933,
          0.9,
          0.9,
          0.983,
          0.85,
          0.333,
          0.283,
          0.933,
          0.967,
          0.867,
          0.933,
          0.967,
          0.933,
          0.983,
          0.95,
          1,
          0.917,
          0.967,
          0.883,
          0.933,
          0.6
        ],
        "probes": [
          {
            "probe_id": "obs-822",
            "similarity": 0.958,
            "task_text": "Find the LIGO Scientific Collaboration paper reporting the first direct observation of gravitational waves from a binary black hole merger (GW150914).",
            "adapted_input": "Find the LIGO Scientific Collaboration paper reporting the first direct observation of gravitational waves from a binary black hole merger (GW150914).",
            "score": 0.983,
            "redacted": null,
            "output_chars": 8284,
            "truncated": false,
            "created_at": "2026-05-17T18:58:04.701179Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 0.983,
                "rationale": "The tool successfully identified the exact paper requested. It provided the correct title, authors ( | The tool correctly identifies the LIGO Scientific Collaboration paper reporting the first direct obs | The tool accurately identifies the paper with all key details matching the ground truth: title, auth",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool successfully identified the exact paper requested. It provided the correct title, authors (as B. P. Abbott et al.), journal (Physical Review Letters), volume/article number (116, 061102), year (2016), arXiv ID, and internal LIGO document ID. It also provided direct links to the source, matc…",
                    "score": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool correctly identifies the LIGO Scientific Collaboration paper reporting the first direct observation of gravitational waves from GW150914. It provides the exact title, authors (Abbott et al.), year (2016), venue (Physical Review Letters), DOI (10.1103/PhysRevLett.116.061102), and arXiv ID (1…",
                    "score": 0.95
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool accurately identifies the paper with all key details matching the ground truth: title, authors (correctly abbreviated as B. P. Abbott et al.), year (2016), venue (Physical Review Letters), and persistent identifier (DOI 10.1103/PhysRevLett.116.061102). It provides clear, verifiable sources …",
                    "score": 1
                  }
                ]
              },
              {
                "facet": "format",
                "verdict": "structured",
                "score": 1,
                "rationale": "The tool returns a valid JSON object containing all the expected fields such as query, provider, fact_check_result, and citations.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returns a valid JSON object containing all the expected fields such as query, provider, fact_check_result, and citations.",
                    "label": "structured",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool output is a well-formed JSON object with nested fields like fact_check_result containing claims, ratings, and citations, which is explicitly designed for programmatic parsing.",
                    "label": "structured",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool output is a complete JSON object with the fact_check result structured to include verdict label, citations, and other expected fields in a machine-parseable format.",
                    "label": "structured",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "freshness",
                "verdict": "not_applicable",
                "score": 1,
                "rationale": "The query asks for a specific scientific paper published in 2016, which is a static historical fact where freshness is irrelevant.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The query asks for a specific scientific paper published in 2016, which is a static historical fact where freshness is irrelevant.",
                    "label": "not_applicable",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The query concerns a static historical fact (a 2016 scientific paper), so the freshness of the verification is irrelevant.",
                    "label": "not_applicable",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The query concerns a static historical paper from 2016 that does not require current evidence, so freshness is irrelevant.",
                    "label": "not_applicable",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "The tool directly identifies the specific paper requested, providing the correct title, authors, journal, year, arXiv ID, and DOI, all of which match the ground truth perfectly.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool directly identifies the specific paper requested, providing the correct title, authors, journal, year, arXiv ID, and DOI, all of which match the ground truth perfectly.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool output directly identifies the exact paper requested, including title, authors, year, venue, and persistent identifiers, with verifiable high-quality sources.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The top results include one directly relevant citation to the correct paper (LIGO DCC link), but others are companion papers or have incorrect identifiers, mixing relevant with off-topic items.",
                    "label": "partial",
                    "value": 0.5
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool cites the peer-reviewed journal Physical Review Letters, the arXiv preprint server, and the official LIGO Document Control Center, which are all primary or authoritative scientific sources.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool cites the peer-reviewed journal Physical Review Letters, the arXiv preprint server, and the official LIGO Document Control Center, which are all primary or authoritative scientific sources.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "All citations are from official LIGO sites, the journal publisher (APS/PRL), or arXiv, which are primary and authoritative sources for a peer-reviewed research paper.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool cites official LIGO documents and peer-reviewed journal articles, which are primary sources.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "snippet_quality",
                "verdict": "informative",
                "score": 1,
                "rationale": "The tool provides a highly detailed summary including the paper title, authors, journal, volume, article number, year, arXiv ID, and specific DOI, allowing the user to assess relevance immediately.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides a highly detailed summary including the paper title, authors, journal, volume, article number, year, arXiv ID, and specific DOI, allowing the user to assess relevance immediately.",
                    "label": "informative",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool output includes detailed bibliographic details such as the exact title, journal, volume, DOI, and arXiv identifier within the claim explanations, allowing the user to assess the relevance without needing to click through to the sources.",
                    "label": "informative",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output includes a detailed summary with specific facts such as paper title, authors, year, and venue, allowing relevance assessment without clicking.",
                    "label": "informative",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool provides specific URLs, the paper title, journal details, and arXiv identifiers that allow a reader to locate the source material.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides specific URLs, the paper title, journal details, and arXiv identifiers that allow a reader to locate the source material.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output includes multiple explicit URLs and document references, such as links to LIGO, APS, and arXiv sources, meeting the criterion for present references.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output provides explicit URLs under the 'sources' section that readers can follow to the underlying material.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool provided a detailed response containing the requested paper's title, authors, journal, and identifiers.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provided a detailed response containing the requested paper's title, authors, journal, and identifiers.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a comprehensive JSON response with fact-check results, claims, and citations, indicating non-empty and usable output.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool output contains a structured JSON response with fact-check results, claims, explanations, and citations, indicating non-empty output was returned.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find the LIGO Scientific Collaboration paper reporting the first direct observation of gravitational waves from a binary black hole merger (GW150914).\",\n  \"provider\": \"Perplexity Sonar (sonar-pro)\",\n  \"tool_kind\": \"verifier (live web search + LLM synthesis with structured output)\",\n  \"fact_check_result\": {\n    \"overall_rating\": \"MIXED\",\n    \"summary\": \"The claim is framed as a task rather than a factual statement, but it implicitly assumes there is a specific LIGO/Virgo collaboration paper reporting the first direct observation of gravitational waves from the GW150914 binary black hole merger. This is correct: the canonical paper is \\u201cObservation of Gravitational Waves from a Binary Black Hole Merger,\\u201d LIGO-P150914, published in Physical Review Letters 116, 061102 (2016) and on arXiv as 1602.03837. Several related LIGO papers on GW150914 also exist, but the main discovery paper is well defined and verifiable.\",\n    \"claims\": [\n      {\n        \"claim\": \"There is a LIGO Scientific Collaboration paper reporting the first direct observation of gravitational waves from a binary black hole merger (GW150914), and it can be found.\",\n        \"rating\": \"TRUE\",\n        \"explanation\": \"The core factual assumption behind the user\\u2019s task is that a specific LIGO Scientific Collaboration paper exists that reports the first direct observation of gravitational waves f …[truncated]"
          },
          {
            "probe_id": "obs-728",
            "similarity": 0.956,
            "task_text": "Gu and Dao's 2023 selective state-space model architecture proposed as an alternative to Transformers (Mamba).",
            "adapted_input": "Gu and Dao's 2023 selective state-space model architecture proposed as an alternative to Transformers (Mamba).",
            "score": 0.933,
            "redacted": null,
            "output_chars": 8072,
            "truncated": false,
            "created_at": "2026-05-17T13:47:52.497100Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 0.933,
                "rationale": "The tool perfectly identified the paper, authors, year, and the specific technical nature of the arc | The tool correctly identifies all key aspects of the ground truth: authors (Gu and Dao), year (2023) | The tool accurately verifies all key components of the ground truth: authors (Albert Gu, Tri Dao), y",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool perfectly identified the paper, authors, year, and the specific technical nature of the architecture (selective state-space models). It even provided the arXiv identifier and confirmed the context of it being an alternative to Transformers, matching all requirements of the ground truth.",
                    "score": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool correctly identifies all key aspects of the ground truth: authors (Gu and Dao), year (2023), the architecture (Mamba as a selective state space model), and its positioning as an alternative to Transformers. It provides the arXiv link and identifier. The output is thorough and accurate, thou…",
                    "score": 0.9
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool accurately verifies all key components of the ground truth: authors (Albert Gu, Tri Dao), year (2023), selective state-space model architecture (Mamba), and persistent identifier (arXiv: 2312.00752 with URL). It provides clear, structured output with sources, demonstrating relevance, accura…",
                    "score": 0.9
                  }
                ]
              },
              {
                "facet": "format",
                "verdict": "structured",
                "score": 1,
                "rationale": "The tool returns a valid JSON object containing the expected fields such as query, provider, and a detailed fact_check_result object.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returns a valid JSON object containing the expected fields such as query, provider, and a detailed fact_check_result object.",
                    "label": "structured",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool output is a valid JSON object with clearly defined keys and nested structures (e.g., fact_check_result with claims array), making it machine-parseable and fully structured.",
                    "label": "structured",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output is a well-formed JSON object with all key fields populated, including a nested fact_check_result structure, ensuring it is machine-parseable.",
                    "label": "structured",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "freshness",
                "verdict": "not_applicable",
                "score": 1,
                "rationale": "The query concerns a specific academic paper and its technical details, which are static historical facts rather than ongoing events or changing regulations.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The query concerns a specific academic paper and its technical details, which are static historical facts rather than ongoing events or changing regulations.",
                    "label": "not_applicable",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The query is about a static fact—the publication of a specific 2023 paper—so the freshness of the verification evidence is irrelevant, and the tool's use of the original paper and current citations is appropriate.",
                    "label": "not_applicable",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The query is about a static historical fact (a paper published in 2023), so freshness is not relevant to the verification.",
                    "label": "not_applicable",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "The tool directly identifies the correct paper, authors, year, and core technical details requested in the query, providing high-quality source verification.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool directly identifies the correct paper, authors, year, and core technical details requested in the query, providing high-quality source verification.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool output directly confirms all key components of the query—authors, year, architecture name, and its positioning as a Transformer alternative—with citations to authoritative sources like the arXiv paper.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output directly verifies the query's factual components with accurate details and high-quality sources, perfectly aligning with the ground truth paper.",
                    "label": "excellent",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool cites the original arXiv preprint (the primary source for the research) and Semantic Scholar to verify the paper's details.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool cites the original arXiv preprint (the primary source for the research) and Semantic Scholar to verify the paper's details.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's citations reference the original arXiv preprint and Semantic Scholar entry, which are primary academic sources.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool cites the original arXiv preprint paper directly, which serves as the primary source for the research findings.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "snippet_quality",
                "verdict": "informative",
                "score": 1,
                "rationale": "The tool provides a highly detailed breakdown of the claim, including specific author names, publication dates, arXiv identifiers, and direct quotes from the paper's abstract to verify the information.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides a highly detailed breakdown of the claim, including specific author names, publication dates, arXiv identifiers, and direct quotes from the paper's abstract to verify the information.",
                    "label": "informative",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool output provides specific facts, numbers, and direct quotes from the paper, such as authors, year, arXiv link, and positioning as an alternative to Transformers, allowing assessment of relevance without clicking through.",
                    "label": "informative",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output contains specific facts like authors, publication date, and paper details from sources, allowing relevance assessment without further action.",
                    "label": "informative",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool provides explicit source references, including a direct URL to the arXiv paper and specific citations from Semantic Scholar and the arXiv abstract.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides explicit source references, including a direct URL to the arXiv paper and specific citations from Semantic Scholar and the arXiv abstract.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output includes explicit source references such as URLs (e.g., https://arxiv.org/abs/2312.00752) and named sources (e.g., Semantic Scholar) that readers can follow back to the underlying material.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output explicitly lists URLs and document names, such as the arXiv link, which readers can follow to access the source material.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool provided a detailed fact-check response containing the requested information and sources.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provided a detailed fact-check response containing the requested information and sources.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a detailed JSON response with fact-check results and sources, so output was non-empty.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned a detailed JSON response with structured fact-check results, summary, and sources, confirming non-empty output.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Gu and Dao's 2023 selective state-space model architecture proposed as an alternative to Transformers (Mamba).\",\n  \"provider\": \"Perplexity Sonar (sonar-pro)\",\n  \"tool_kind\": \"verifier (live web search + LLM synthesis with structured output)\",\n  \"fact_check_result\": {\n    \"overall_rating\": \"MIXED\",\n    \"summary\": \"The claim correctly identifies Mamba as a selective state space model architecture introduced by Albert Gu and Tri Dao in 2023 and positioned as an alternative to Transformers. However, as written it is incomplete/underspecified rather than strictly factual or false: it reads more like a fragment than a full factual statement. The core factual components (who, what, when, and its role as an alternative to Transformers) are supported by the cited sources.\",\n    \"claims\": [\n      {\n        \"claim\": \"Gu and Dao\\u2019s 2023 selective state-space model architecture (Mamba) was proposed as an alternative to Transformers.\",\n        \"rating\": \"TRUE\",\n        \"explanation\": \"Breaking the claim into components:\\n\\n1. **Authorship (Gu and Dao)**  \\n   The arXiv paper \\\"Mamba: Linear-Time Sequence Modeling with Selective State Spaces\\\" lists the authors as **Albert Gu** and **Tri Dao**:\\n   - Semantic Scholar: \\u201cMamba: Linear-Time Sequence Modeling with Selective State Spaces \\u00b7 **Albert Gu, Tri Dao** \\u00b7 Published in arXiv.org 1 December 2023.\\u201d\\n   \\ …[truncated]"
          },
          {
            "probe_id": "obs-692",
            "similarity": 0.952,
            "task_text": "Ho, Jain and Abbeel's 2020 paper on denoising diffusion probabilistic models for image generation.",
            "adapted_input": "Ho, Jain and Abbeel's 2020 paper on denoising diffusion probabilistic models for image generation.",
            "score": 0.95,
            "redacted": null,
            "output_chars": 7252,
            "truncated": false,
            "created_at": "2026-05-17T11:51:04.348734Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 0.95,
                "rationale": "The tool correctly identified the paper, its title, authors, year, and provided the correct arXiv li | The tool correctly identifies the paper, its authors, year, and topic, providing accurate citations  | The tool accurately identifies and verifies the paper's details, providing correct title, authors, y",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool correctly identified the paper, its title, authors, year, and provided the correct arXiv link and venue (NeurIPS 2020). It went above and beyond by providing a detailed fact-check structure that matches all requirements of the ground truth.",
                    "score": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool correctly identifies the paper, its authors, year, and topic, providing accurate citations and a thorough fact-check. It matches the ground truth closely, though the query is a fragment and the tool's response is slightly verbose. Minor deduction for not explicitly listing the arXiv ID in t…",
                    "score": 0.95
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool accurately identifies and verifies the paper's details, providing correct title, authors, year, and URLs with supporting sources, closely aligning with the ground truth. It addresses the query comprehensively with clear structure and evidence, though minor differences in venue specification…",
                    "score": 0.9
                  }
                ]
              },
              {
                "facet": "format",
                "verdict": "structured",
                "score": 1,
                "rationale": "The tool returns a complete, valid JSON object containing all the required fields such as fact_check_result, top_level_citations, and search_results.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returns a complete, valid JSON object containing all the required fields such as fact_check_result, top_level_citations, and search_results.",
                    "label": "structured",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool output is a complete JSON object with well-defined fields including query, provider, tool_kind, fact_check_result, top_level_citations, and search_results, all properly populated.",
                    "label": "structured",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool output is a well-formed JSON object with populated fields for verdict, citations, and search results, adhering to the expected structured format for fact_check tools.",
                    "label": "structured",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "freshness",
                "verdict": "not_applicable",
                "score": 1,
                "rationale": "The query concerns a specific academic paper published in 2020, which is a static historical fact where freshness is irrelevant.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The query concerns a specific academic paper published in 2020, which is a static historical fact where freshness is irrelevant.",
                    "label": "not_applicable",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The query refers to a specific 2020 paper, which is a static fact where the freshness of the evidence is irrelevant.",
                    "label": "not_applicable",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The query is about a historical paper publication, which is a static fact where freshness is irrelevant.",
                    "label": "not_applicable",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "The tool correctly identifies the specific paper, authors, year, and title, providing direct links to the arXiv preprint and the NeurIPS proceedings as top results.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool correctly identifies the specific paper, authors, year, and title, providing direct links to the arXiv preprint and the NeurIPS proceedings as top results.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's top results, including citations and search results, directly cite the exact paper by Ho, Jain, and Abbeel with correct title, authors, year, and persistent identifier, fully satisfying the query intent.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output confirms the paper's existence with correct authors, year, and topic, and provides direct high-quality sources like the arXiv and NeurIPS links that exactly match the query intent.",
                    "label": "excellent",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool cites the original peer-reviewed paper from the NeurIPS proceedings and the official arXiv preprint, which are primary sources.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool cites the original peer-reviewed paper from the NeurIPS proceedings and the official arXiv preprint, which are primary sources.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool cites the original arXiv preprint and NeurIPS proceedings, which are direct, authoritative primary sources for the paper by Ho, Jain, and Abbeel.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool cites peer-reviewed papers and authoritative academic sources such as arXiv preprints and NeurIPS conference proceedings, which are primary sources.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "snippet_quality",
                "verdict": "generic",
                "score": 0.5,
                "rationale": "The only provided snippet in the search results section is heavily truncated and provides almost no information beyond the title.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The only provided snippet in the search results section is heavily truncated and provides almost no information beyond the title.",
                    "label": "generic",
                    "value": 0.5
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The search result snippet is truncated to only a few words ('We present high quality image synth'), providing minimal information to assess relevance without clicking.",
                    "label": "generic",
                    "value": 0.5
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The snippet is truncated, making it vague and insufficient to assess relevance without clicking through.",
                    "label": "generic",
                    "value": 0.5
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool provides multiple explicit source references, including direct URLs to arXiv, NeurIPS proceedings, and the authors' project page.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides multiple explicit source references, including direct URLs to arXiv, NeurIPS proceedings, and the authors' project page.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output contains multiple explicit URLs (e.g., arXiv, NeurIPS proceedings) that a reader can follow back to the underlying material.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output includes explicit URLs in the 'Sources' section and 'top_level_citations' array, providing direct references to the paper.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool provided a detailed fact-check response including the paper title, authors, year, and several source URLs.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provided a detailed fact-check response including the paper title, authors, year, and several source URLs.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a detailed JSON with fact-checking results, citations, and search results, indicating non-empty output.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool output is a non-empty JSON response containing fact-check details, citations, and search snippets, fulfilling the criteria for usable output.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Ho, Jain and Abbeel's 2020 paper on denoising diffusion probabilistic models for image generation.\",\n  \"provider\": \"Perplexity Sonar (sonar-pro)\",\n  \"tool_kind\": \"verifier (live web search + LLM synthesis with structured output)\",\n  \"fact_check_result\": {\n    \"overall_rating\": \"MOSTLY_TRUE\",\n    \"summary\": \"The claim is incomplete but essentially refers to the well\\u2011known 2020 paper by Ho, Jain, and Abbeel titled \\u201cDenoising Diffusion Probabilistic Models,\\u201d which indeed introduces a diffusion-based generative model for high\\u2011quality image synthesis. The authors, year, and topic (denoising diffusion probabilistic models for image generation) are correct, though the wording is more like a fragment than a full factual statement.\",\n    \"claims\": [\n      {\n        \"claim\": \"Ho, Jain and Abbeel's 2020 paper on denoising diffusion probabilistic models for image generation.\",\n        \"rating\": \"TRUE\",\n        \"explanation\": \"Interpreting this as the implicit claim: \\u201cIn 2020, Ho, Jain, and Abbeel published a paper on denoising diffusion probabilistic models for image generation,\\u201d this is accurate.\\n\\nEvidence:\\n\\n1. **Authors and year**: The NeurIPS 2020 proceedings version lists the paper:\\n   - Title: \\u201cDenoising Diffusion Probabilistic Models\\u201d\\n   - Authors: Jonathan Ho, Ajay Jain, Pieter Abbeel\\n   - Venue: Advances in Neural Informa …[truncated]"
          }
        ]
      },
      "evidence_teaser": {
        "task_text": "Find the LIGO Scientific Collaboration paper reporting the first direct observation of gravitational waves from a binary black hole merger (GW150914).",
        "verdict": "excellent",
        "score": 0.983,
        "similarity": 0.958,
        "n_real": 226
      }
    },
    {
      "tool_id": "semantic_scholar",
      "name": "Semantic Scholar Graph API",
      "variant": null,
      "capabilities": [
        "paper_search",
        "academic",
        "references",
        "abstracts",
        "citation_graph"
      ],
      "description": "Academic graph API covering all research fields with title, abstract, authors, venue, year, citation counts, external IDs (DOI, PMID, arXiv), and open-access PDF locations when known. Requires a free Semantic Scholar API key for reliable use: the unauthenticated endpoint shares one global rate pool and frequently times out. Commercial use is restricted — AI2's Semantic Scholar API License Agreement conditions commercial use; review it before using the tool in a commercial product.",
      "kind": "external_tool",
      "endpoint": {
        "api_type": "rest",
        "base_url": "https://api.semanticscholar.org",
        "status_url": "https://api.semanticscholar.org/health"
      },
      "reason": "lower capability (0.89 vs 0.98).",
      "capability": 0.8859,
      "band": 0.0372,
      "cap_lcb": 0.8488,
      "rank": 0.9358,
      "price": {
        "amount": 0,
        "per_query_usd": 0,
        "currency": "USD",
        "confidence": "high",
        "selected_plan": "free",
        "held": false,
        "estimated": true,
        "cost_unknown": false,
        "breakdown": [
          {
            "plan_id": "free",
            "kind": "free",
            "plan_group": null,
            "effective_usd": 0,
            "held": false,
            "currency": "USD",
            "confidence": "high",
            "overridden": false
          }
        ]
      },
      "calling": {
        "tool_id": "semantic_scholar",
        "coordinator_class": false,
        "executable": true,
        "endpoint": {
          "base_url": "https://api.semanticscholar.org",
          "api_type": "rest"
        },
        "adapter": {
          "type": "llm"
        },
        "auth": {
          "method": "api_key",
          "env_var": "SEMANTIC_SCHOLAR_API_KEY",
          "connected": false
        },
        "summary": {
          "usability": "connect_key",
          "auth_method": "api_key",
          "api_type": "rest",
          "connected": false,
          "free": false,
          "how": "connect a key → www.semanticscholar.org/product/api",
          "signup_url": "https://www.semanticscholar.org/product/api"
        },
        "connect": {
          "tool_id": "semantic_scholar",
          "name": "Semantic Scholar Graph API",
          "auth_method": "api_key",
          "signup_url": "https://www.semanticscholar.org/product/api",
          "instructions": "  1. Open the Semantic Scholar API page.\n  2. Fill in the 'Request an API Key' form with your name, email, and intended use.\n  3. Wait for the approval email (it arrives from the Semantic Scholar team).\n  4. Copy the API key from that email.",
          "methods": [
            {
              "auth_method": "api_key",
              "label": "Semantic Scholar API key",
              "signup_url": "https://www.semanticscholar.org/product/api",
              "instructions": [
                "Open the Semantic Scholar API page.",
                "Fill in the 'Request an API Key' form with your name, email, and intended use.",
                "Wait for the approval email (it arrives from the Semantic Scholar team).",
                "Copy the API key from that email."
              ],
              "fields": [
                {
                  "key": "SEMANTIC_SCHOLAR_API_KEY",
                  "label": "Semantic Scholar API key",
                  "secret": true,
                  "required": true,
                  "help": "From the approval email after you submit the API key request form"
                }
              ]
            }
          ],
          "fields": [
            {
              "key": "SEMANTIC_SCHOLAR_API_KEY",
              "label": "Semantic Scholar API key",
              "secret": true,
              "required": true,
              "help": "From the approval email after you submit the API key request form"
            }
          ],
          "source": "evaluator",
          "connect_via": {
            "surface": "POST /credentials/connect",
            "method": "Semantic Scholar API key",
            "field_key": "SEMANTIC_SCHOLAR_API_KEY",
            "payload": {
              "tool_id": "semantic_scholar",
              "api_key": "<paste your key here>"
            },
            "curl": "curl -s https://hyperroute.io/credentials/connect -H 'content-type: application/json' -d '{\"tool_id\":\"semantic_scholar\",\"api_key\":\"<YOUR_KEY>\"}'"
          }
        }
      },
      "facets": [
        {
          "name": "capability",
          "kano": "must_be",
          "weight": 1,
          "threshold": 0.5,
          "raw": 0.8488,
          "contribution": 0.7883
        },
        {
          "name": "price",
          "kano": "performance",
          "weight": 0.3,
          "threshold": 0.5,
          "raw": 1,
          "contribution": 0.3
        },
        {
          "name": "no_machine_harm",
          "kano": "must_be",
          "weight": 2,
          "threshold": 0.5,
          "raw": 1,
          "contribution": 2
        }
      ],
      "evidence": {
        "n_real": 83,
        "n_near": 24,
        "near_mean": 0.675,
        "dist": [
          1,
          0.983,
          0.2,
          0,
          1,
          1,
          1,
          1,
          0,
          0,
          0.967,
          1,
          0.967,
          1,
          0.1,
          0.933,
          0,
          0.86,
          0.1,
          0.1,
          1,
          0.983,
          1,
          1
        ],
        "probes": [
          {
            "probe_id": "obs-32554",
            "similarity": 0.96,
            "task_text": "Find the 2026 Frontiers in Plant Science paper by Song et al. on arbuscular mycorrhizal fungi and rhizobium facilitating nitrogen uptake and transfer in a soybean/tobacco intercropping system. Give me its DOI.",
            "adapted_input": "Song arbuscular mycorrhizal fungi rhizobium nitrogen soybean tobacco intercropping 2026",
            "score": 1,
            "redacted": null,
            "output_chars": 2464,
            "truncated": false,
            "created_at": "2026-08-29T09:54:09.497513Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "Deterministic check — matched 1/1 required string(s).",
                "panel": null
              }
            ],
            "raw_output": "{\n  \"query\": \"Find the 2026 Frontiers in Plant Science paper by Song et al. on arbuscular mycorrhizal fungi and rhizobium facilitating nitrogen uptake and transfer in a soybean/tobacco intercropping system. Give me its DOI.\",\n  \"adapted_query\": \"Song arbuscular mycorrhizal fungi rhizobium nitrogen soybean tobacco intercropping 2026\",\n  \"provider\": \"Semantic Scholar\",\n  \"tool_kind\": \"academic paper search (broad coverage, citation graph)\",\n  \"total_results\": 1,\n  \"returned_results\": 1,\n  \"results\": [\n    {\n      \"paper_id\": \"aec971a94f2d92b2c1f16bcbbeb919d257454ddc\",\n      \"title\": \"Arbuscular mycorrhizal fungi and rhizobium facilitate nitrogen uptake and transfer in soybean/tobacco intercropping system\",\n      \"abstract\": \"Introduction The tripartite symbiosis of legume-AMF-rhizobia is widely considered to facilitate nitrogen (N) uptakeby legumes, but its effect on non-legume plants in intercropping systems remains unclear. Methods A pot experiment with three root separations (PS, MS, NS) was conducted using \\u00b9\\u2075N isotope tracing in a soybean/tobacco intercropping system with double inoculation of Claroideoglomus etunicatum (CE) and Bradyrhizobium japonicum 5016 (BJ). Results Double inoculation (CE+BJ) significantly increased bioaccumulation, N uptake, and N transfer from soybean to tobacco compared to single or no inoculation. Mycorrhizal colonization in soybean increa …[truncated]"
          },
          {
            "probe_id": "obs-8910",
            "similarity": 0.96,
            "task_text": "Find the recent arXiv paper \"Spin disorder competing with positional symmetry\" on the metal-insulator behavior of oxide paramagnets.",
            "adapted_input": "spin disorder positional symmetry metal-insulator oxide paramagnets",
            "score": 0.983,
            "redacted": null,
            "output_chars": 20000,
            "truncated": true,
            "created_at": "2026-06-16T20:05:31.133647Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 0.983,
                "rationale": "The tool successfully identified the exact paper requested. It provided the correct title, authors,  | The tool correctly identified the exact arXiv paper (2606.14624) with the precise title, authors, ye | The tool returned the exact arXiv paper with correct title, arXiv ID (2606.14624), authors, and year",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool successfully identified the exact paper requested. It provided the correct title, authors, publication date, and the specific arXiv ID (2606.14624) mentioned in the ground truth.",
                    "score": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool correctly identified the exact arXiv paper (2606.14624) with the precise title, authors, year, and abstract matching the ground truth. The adapted query effectively retrieved the target paper as the top result. Minor deduction for returning 15 results when the query asked for a specific pap…",
                    "score": 0.95
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned the exact arXiv paper with correct title, arXiv ID (2606.14624), authors, and year (2026), perfectly matching the ground truth. No issues with relevance, accuracy, or completeness, as all key details are present and correct.",
                    "score": 1
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "The top result is the exact paper requested by the user, matching the title, topic, and arXiv ID provided in the ground truth.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The top result is the exact paper requested by the user, matching the title, topic, and arXiv ID provided in the ground truth.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The top result is the exact arXiv paper requested, with matching title, authors, and abstract, directly fulfilling the query intent.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output directly returns the exact arXiv paper requested as the top result, matching the ground truth with correct details, thus perfectly answering the query intent.",
                    "label": "excellent",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool provides a direct citation to a peer-reviewed/academic preprint from arXiv, which is a primary source for scientific research.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides a direct citation to a peer-reviewed/academic preprint from arXiv, which is a primary source for scientific research.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output directly cites a peer-reviewed arXiv preprint (arXiv:2606.14624) and other academic papers, which are primary authoritative sources.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool output cites academic papers, including preprints from arXiv, which are primary sources in the context of research.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool output provides explicit source references including the paper title, authors, arXiv ID, and a Semantic Scholar URL.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool output provides explicit source references including the paper title, authors, arXiv ID, and a Semantic Scholar URL.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The output includes explicit source references such as a Semantic Scholar URL and an ArXiv ID (2606.14624) for the first paper, allowing a reader to follow back to the underlying material.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output includes explicit URLs and ArXiv IDs in the results, providing clear source references that a reader can follow back to the papers.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool returned a list of results containing the specific paper requested by the user.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned a list of results containing the specific paper requested by the user.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a list of 15 results, including the exact paper requested as the top result, so the output is non-empty and usable.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned a non-empty JSON output with multiple results, including the correct paper, fulfilling the requirement for usable output.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find the recent arXiv paper \\\"Spin disorder competing with positional symmetry\\\" on the metal-insulator behavior of oxide paramagnets.\",\n  \"adapted_query\": \"spin disorder positional symmetry metal-insulator oxide paramagnets\",\n  \"provider\": \"Semantic Scholar\",\n  \"tool_kind\": \"academic paper search (broad coverage, citation graph)\",\n  \"total_results\": 28,\n  \"returned_results\": 15,\n  \"results\": [\n    {\n      \"paper_id\": \"22de36ef6d33ab78fe7a104a0cbe12ef82375637\",\n      \"title\": \"Spin disorder competing with positional symmetry breaking governs the metal-insulator behavior in oxide paramagnets\",\n      \"abstract\": \"Numerous transition-metal oxides have low-temperature antiferromagnetic (AFM) states and high-temperature paramagnetic (PM) phases, where the AFM state is usually insulating while the PM phase can be either insulating or metallic. Without involving strong correlation, we use symmetry-broken density-functional theory (DFT) to obtain the PM phases of insulating NaFeO3 vs the recently discovered metallic NaOsO3. We develop the understanding of insulating and metallic behaviors in paramagnetic oxides by analyzing the interactions between magnetic and positional symmetry breaking: The insulating gap is governed by the competition between the spin disorder that induces a distribution of different magnitudes of local magnetic moments and the polymorphous distribut …[truncated]"
          },
          {
            "probe_id": "obs-8764",
            "similarity": 0.957,
            "task_text": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
            "adapted_input": "AlphaFold2 protein structure prediction Jumper 2021 Nature DeepMind",
            "score": 0.2,
            "redacted": null,
            "output_chars": 20000,
            "truncated": true,
            "created_at": "2026-06-13T22:13:31.499960Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "fail",
                "score": 0.2,
                "rationale": "The tool failed to return the actual canonical paper as a direct result. Instead, the top result is  | The tool failed to return the requested canonical paper (Jumper et al. 2021 Nature). The top results | The tool returned papers related to AlphaFold2, but the specific paper by Jumper et al. ('Highly acc",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool failed to return the actual canonical paper as a direct result. Instead, the top result is a different paper that merely cites the target paper in its abstract. While the first result's abstract contains the correct citation information (Jumper et al., 2021, Nature, 596, 583), the tool did …",
                    "score": 0.3
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool failed to return the requested canonical paper (Jumper et al. 2021 Nature). The top results are irrelevant: a commentary and a review discussing AlphaFold2 but not the actual paper itself. No correct title, authors, or identifier are present despite the query being clear and the ground trut…",
                    "score": 0
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned papers related to AlphaFold2, but the specific paper by Jumper et al. ('Highly accurate protein structure prediction with AlphaFold.') did not appear in the visible top results, failing to retrieve the canonical paper as required by the query.",
                    "score": 0.3
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "partial",
                "score": 0.5,
                "rationale": "The top results are secondary papers discussing AlphaFold2 rather than the primary research paper requested, although the first result's abstract does contain the correct citation information.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The top results are secondary papers discussing AlphaFold2 rather than the primary research paper requested, although the first result's abstract does contain the correct citation information.",
                    "label": "partial",
                    "value": 0.5
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The top results discuss AlphaFold2 but do not include the specific 2021 Nature paper by Jumper et al. that announced it, so the user would need to dig further to find the exact paper.",
                    "label": "partial",
                    "value": 0.5
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The top results are relevant to AlphaFold2 and include citations to the target paper, offering useful context though not directly providing the specific Nature paper itself.",
                    "label": "good",
                    "value": 0.75
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool provides results from academic databases including peer-reviewed journals like Nature and Microbial Biotechnology, which are primary sources.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides results from academic databases including peer-reviewed journals like Nature and Microbial Biotechnology, which are primary sources.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "All returned results are from peer-reviewed journals, which are primary academic sources.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output consists of peer-reviewed academic papers, which are primary sources as defined in the rubric.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool output provides specific paper titles, authors, publication venues, DOIs, and Semantic Scholar URLs for the results found.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool output provides specific paper titles, authors, publication venues, DOIs, and Semantic Scholar URLs for the results found.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The output includes explicit source references such as URLs, DOIs, and other identifiers for each paper, allowing a reader to follow back to the underlying material.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output includes explicit URLs and DOI numbers for each search result, which are direct source references that a reader can follow back to the underlying material.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool returned a list of search results containing paper titles, abstracts, and metadata.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned a list of search results containing paper titles, abstracts, and metadata.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned multiple paper results with titles, abstracts, and metadata, so the output is non-empty.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned a detailed JSON response with multiple paper results and metadata, confirming non-empty output.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.\",\n  \"adapted_query\": \"AlphaFold2 protein structure prediction Jumper 2021 Nature DeepMind\",\n  \"provider\": \"Semantic Scholar\",\n  \"tool_kind\": \"academic paper search (broad coverage, citation graph)\",\n  \"total_results\": 24,\n  \"returned_results\": 15,\n  \"results\": [\n    {\n      \"paper_id\": \"eed8d8fd7fd3ccfe13585cb0cd51654436a5f820\",\n      \"title\": \"Artificial intelligence for microbial biotechnology: beyond the hype\",\n      \"abstract\": \"It has been a landmark year for artificial intelligence (AI) and biotechnology. Perhaps the most noteworthy of these advances was Google DeepMind\\u2019s AlphaFold2 algorithm which smashed records in protein structure prediction (Jumper et al., 2021, Nature, 596, 583) complemented by progress made by other research groups around the globe (Baek et al., 2021, Science, 373, 871; Zheng et al., 2021, Proteins). For the first time in history, AI achieved protein structure models rivalling the accuracy of experimentally determined structures. The power of accurate protein structure prediction at our fingertips has countless implications for drug discovery, de novo protein design and fundamental research in chemical biology. While acknowledging the significance of these breakthroughs, this perspective aims to cut through the hype and exam …[truncated]"
          }
        ]
      },
      "evidence_teaser": {
        "task_text": "Find the 2026 Frontiers in Plant Science paper by Song et al. on arbuscular mycorrhizal fungi and rhizobium facilitating nitrogen uptake and transfer in a soybean/tobacco intercropping system. Give me its DOI.",
        "verdict": "pass",
        "score": 1,
        "similarity": 0.96,
        "n_real": 83
      }
    },
    {
      "tool_id": "serp_search",
      "name": "SerpAPI (Google)",
      "variant": null,
      "capabilities": [
        "web_search",
        "realtime"
      ],
      "description": "Google search results via API. Returns structured JSON with organic results, answer boxes, knowledge panels, and news.",
      "kind": "external_tool",
      "endpoint": {
        "api_type": "rest",
        "base_url": "https://serpapi.com",
        "status_url": "https://serpapi.com"
      },
      "reason": "lower capability (0.88 vs 0.98).",
      "capability": 0.8835,
      "band": 0.0332,
      "cap_lcb": 0.8503,
      "rank": 0.9355,
      "price": {
        "amount": 0.0075,
        "per_query_usd": 0.0075,
        "currency": "USD",
        "confidence": "high",
        "selected_plan": "free",
        "held": false,
        "estimated": true,
        "cost_unknown": false,
        "breakdown": [
          {
            "plan_id": "free",
            "kind": "free",
            "plan_group": "serpapi",
            "effective_usd": 0.0075,
            "held": false,
            "currency": "USD",
            "confidence": "high",
            "overridden": false
          },
          {
            "plan_id": "starter",
            "kind": "subscription",
            "plan_group": "serpapi",
            "effective_usd": 0.025,
            "held": false,
            "currency": "USD",
            "confidence": "high",
            "overridden": false
          },
          {
            "plan_id": "developer",
            "kind": "subscription",
            "plan_group": "serpapi",
            "effective_usd": 0.075,
            "held": false,
            "currency": "USD",
            "confidence": "high",
            "overridden": false
          },
          {
            "plan_id": "production",
            "kind": "subscription",
            "plan_group": "serpapi",
            "effective_usd": 0.15,
            "held": false,
            "currency": "USD",
            "confidence": "high",
            "overridden": false
          }
        ]
      },
      "calling": {
        "tool_id": "serp_search",
        "coordinator_class": false,
        "executable": true,
        "endpoint": {
          "base_url": "https://serpapi.com",
          "api_type": "rest"
        },
        "adapter": {
          "type": "llm"
        },
        "auth": {
          "method": "api_key",
          "env_var": "SERPAPI_KEY",
          "connected": false
        },
        "summary": {
          "usability": "connect_key",
          "auth_method": "api_key",
          "api_type": "rest",
          "connected": false,
          "free": false,
          "how": "connect a key → serpapi.com/users/sign_up",
          "signup_url": "https://serpapi.com/users/sign_up"
        },
        "connect": {
          "tool_id": "serp_search",
          "name": "SerpAPI (Google)",
          "auth_method": "api_key",
          "signup_url": "https://serpapi.com/users/sign_up",
          "instructions": "  1. Create a SerpApi account — the free tier is enough to start.\n  2. Confirm your email address.\n  3. Open the API Key page in your dashboard.\n  4. Copy your private API key.",
          "methods": [
            {
              "auth_method": "api_key",
              "label": "SerpApi private key",
              "signup_url": "https://serpapi.com/users/sign_up",
              "instructions": [
                "Create a SerpApi account — the free tier is enough to start.",
                "Confirm your email address.",
                "Open the API Key page in your dashboard.",
                "Copy your private API key."
              ],
              "fields": [
                {
                  "key": "SERPAPI_KEY",
                  "label": "SerpApi private key",
                  "secret": true,
                  "required": true,
                  "help": "Dashboard → Your Account → API Key"
                }
              ]
            }
          ],
          "fields": [
            {
              "key": "SERPAPI_KEY",
              "label": "SerpApi private key",
              "secret": true,
              "required": true,
              "help": "Dashboard → Your Account → API Key"
            }
          ],
          "source": "evaluator",
          "connect_via": {
            "surface": "POST /credentials/connect",
            "method": "SerpApi private key",
            "field_key": "SERPAPI_KEY",
            "payload": {
              "tool_id": "serp_search",
              "api_key": "<paste your key here>"
            },
            "curl": "curl -s https://hyperroute.io/credentials/connect -H 'content-type: application/json' -d '{\"tool_id\":\"serp_search\",\"api_key\":\"<YOUR_KEY>\"}'"
          }
        }
      },
      "facets": [
        {
          "name": "capability",
          "kano": "must_be",
          "weight": 1,
          "threshold": 0.5,
          "raw": 0.8503,
          "contribution": 0.7905
        },
        {
          "name": "price",
          "kano": "performance",
          "weight": 0.3,
          "threshold": 0.5,
          "raw": 0.9892,
          "contribution": 0.2968
        },
        {
          "name": "no_machine_harm",
          "kano": "must_be",
          "weight": 2,
          "threshold": 0.5,
          "raw": 1,
          "contribution": 2
        }
      ],
      "evidence": {
        "n_real": 399,
        "n_near": 24,
        "near_mean": 0.73,
        "dist": [
          0.667,
          0.867,
          0,
          1,
          0.933,
          1,
          1,
          0.633,
          1,
          0.967,
          0.967,
          1,
          0.967,
          0.967,
          0,
          1,
          0.7,
          0,
          0,
          0.983,
          1,
          0.867,
          1,
          0
        ],
        "probes": [
          {
            "probe_id": "obs-28658",
            "similarity": 0.97,
            "task_text": "Find recent papers by Geoffrey Hinton on neural networks published in the last few years.",
            "adapted_input": "Find recent papers by Geoffrey Hinton on neural networks published in the last few years.",
            "score": 0.667,
            "redacted": null,
            "output_chars": 4517,
            "truncated": false,
            "created_at": "2026-08-12T17:47:11.895385Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "partial",
                "score": 0.667,
                "rationale": "The tool provides several highly relevant authoritative sources that would allow a user to find the  | The tool returns relevant authoritative sources for finding Geoffrey Hinton's recent papers (Google  | The tool provided authoritative sources (e.g., Google Scholar and University of Toronto pages) that ",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides several highly relevant authoritative sources that would allow a user to find the requested information, specifically the Google Scholar profile (Result 1), the University of Toronto personal page (Result 4), and the Google Research profile (Result 6). While the snippets themselves…",
                    "score": 0.7
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returns relevant authoritative sources for finding Geoffrey Hinton's recent papers (Google Scholar, his personal page, Google Research), but the snippets do not directly display specific recent papers or their titles/years. The query asks for 'recent papers ... in the last few years', and t…",
                    "score": 0.6
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool provided authoritative sources (e.g., Google Scholar and University of Toronto pages) that enable access to Hinton's papers, aligning with the contract's reward for canonical sources. However, some results (e.g., YouTube, Reddit) are less relevant for papers, and snippets focus on older pub…",
                    "score": 0.7
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "partial",
                "score": 0.5,
                "rationale": "The top results include a Google Scholar profile and a personal publications page, but the actual recent papers by Hinton are not directly surfaced, and many results are interviews, news articles, or older works.",
                "panel": [
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The top results include a Google Scholar profile and a personal publications page, but the actual recent papers by Hinton are not directly surfaced, and many results are interviews, news articles, or older works.",
                    "label": "partial",
                    "value": 0.5
                  },
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "While the results provide links to Geoffrey Hinton's profiles and general information, they fail to directly list specific recent papers as requested, instead providing a mix of biographical links, YouTube videos, and older publications.",
                    "label": "partial",
                    "value": 0.5
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The top results include non-paper items like videos, profiles, and articles about Hinton, with no specific recent papers listed in the snippets, requiring the user to dig for relevant information.",
                    "label": "poor",
                    "value": 0.25
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool's output includes links to Google Scholar, the University of Toronto's publication list, and Google Research, which are authoritative sources for peer-reviewed papers and primary research.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides a mix of sources including Google Scholar and University websites (reputable secondary/primary indicators) alongside Wikipedia and Reddit (tertiary/low-quality), but fails to provide direct links to the actual peer-reviewed papers requested.",
                    "label": "reputable_secondary",
                    "value": 0.75
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output includes links to Google Scholar, the University of Toronto's publication list, and Google Research, which are authoritative sources for peer-reviewed papers and primary research.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The output includes citations to primary sources such as peer-reviewed papers from ACM Digital Library and official academic publications from institutions like the University of Toronto and Google Research.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool's output includes multiple explicit URLs and document names (e.g., Google Scholar, YouTube, Reddit, University of Toronto page, MIT Sloan article) that a reader can follow back to the underlying material.",
                "panel": [
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output includes multiple explicit URLs and document names (e.g., Google Scholar, YouTube, Reddit, University of Toronto page, MIT Sloan article) that a reader can follow back to the underlying material.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool output provides multiple explicit source references, including URLs and titles for various web pages and documents.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output includes multiple URLs in the results section, which are explicit source references that a reader can follow back to the underlying material.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool returned a list of search results containing various links and snippets related to Geoffrey Hinton.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned a list of search results containing various links and snippets related to Geoffrey Hinton.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned a non-empty JSON response with a list of search results, which constitutes usable output regardless of correctness.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a list of 10 results with titles, URLs, and snippets, which is non-empty output.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find recent papers by Geoffrey Hinton on neural networks published in the last few years.\",\n  \"adapted_query\": \"Find recent papers by Geoffrey Hinton on neural networks published in the last few years.\",\n  \"provider\": \"SerpAPI (Google)\",\n  \"answer\": \"\",\n  \"total_results\": 10,\n  \"api_params\": {\n    \"engine\": \"google\",\n    \"num\": 20\n  },\n  \"results\": [\n    {\n      \"title\": \"Geoffrey Hinton\",\n      \"url\": \"https://scholar.google.com/citations?user=JicYPdAAAAAJ&hl=en\",\n      \"snippet\": \"Hinton Advances in neural information processing systems 25, 2012. Hinton Journal of Machine Learning Research 9 (Nov), 2579-2605, International conference on ...\",\n      \"date\": \"\",\n      \"position\": 1,\n      \"source\": \"Google Scholar\"\n    },\n    {\n      \"title\": \"Ep. 2 - Five Decades of Neural Networks with Geoffrey Hinton\",\n      \"url\": \"https://www.youtube.com/watch?v=i1KUdDo2eOo\",\n      \"snippet\": \"Geoffrey explains how he got into the field, He explains the burst of neural network progress in the mid-1980s \\u2026 re-emergence of deep neural ...\",\n      \"date\": \"\",\n      \"position\": 2,\n      \"source\": \"YouTube \\u00b7 Stanford Digital Economy Lab\"\n    },\n    {\n      \"title\": \"AMA Geoffrey Hinton : r/MachineLearning\",\n      \"url\": \"https://www.reddit.com/r/MachineLearning/comments/2lmo0l/ama_geoffrey_hinton/\",\n      \"snippet\": \"I design learning algorithms for neural networks. My ai …[truncated]"
          },
          {
            "probe_id": "obs-28376",
            "similarity": 0.968,
            "task_text": "Find scientific literature on graphene field-effect transistors for biosensing applications.",
            "adapted_input": "Find scientific literature on graphene field-effect transistors for biosensing applications.",
            "score": 0.867,
            "redacted": null,
            "output_chars": 4493,
            "truncated": false,
            "created_at": "2026-08-12T10:51:37.077669Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 0.867,
                "rationale": "The tool performed exceptionally well. It provided a diverse set of highly relevant, authoritative,  | The tool returned a diverse set of highly relevant, authoritative results (NIH, ScienceDirect, MDPI, | The tool returned mostly relevant results from authoritative sources (e.g., PMC, ScienceDirect, ACS)",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool performed exceptionally well. It provided a diverse set of highly relevant, authoritative, and high-quality scientific sources including PMC (NIH), ScienceDirect, MDPI, Royal Society of Chemistry, and ACS Publications. The results directly address the specific technical query and provide th…",
                    "score": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a diverse set of highly relevant, authoritative results (NIH, ScienceDirect, MDPI, ACS, RSC, etc.) with correct titles and snippets that match the query. No empty or off-topic results, and all URLs appear valid. This aligns well with the ground truth expectation of surfacing real i…",
                    "score": 0.9
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned mostly relevant results from authoritative sources (e.g., PMC, ScienceDirect, ACS) that align with the query for scientific literature, but included an off-topic YouTube video and a potential non-peer-reviewed site, partially missing the ground truth requirement for peer-reviewed p…",
                    "score": 0.7
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "The top three results are highly relevant, high-quality scientific sources (PMC, ScienceDirect, and MDPI) that directly address the user's request for literature on graphene field-effect transistors for biosensing.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The top three results are highly relevant, high-quality scientific sources (PMC, ScienceDirect, and MDPI) that directly address the user's request for literature on graphene field-effect transistors for biosensing.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The top three results are directly relevant, from high-quality peer-reviewed sources, and address the query intent of finding scientific literature on graphene field-effect transistors for biosensing.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The top three results directly answer the query intent with high-quality, peer-reviewed sources on graphene FET biosensors from reputable publishers like NIH, ScienceDirect, and MDPI.",
                    "label": "excellent",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool provides links to peer-reviewed scientific literature from authoritative sources such as PMC (NIH), ScienceDirect, MDPI, RSC, and ACS Publications.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides links to peer-reviewed scientific literature from authoritative sources such as PMC (NIH), ScienceDirect, MDPI, RSC, and ACS Publications.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output primarily consists of peer-reviewed scientific articles from reputable publishers and government databases, which are primary authoritative sources.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output includes multiple citations from peer-reviewed scientific publishers and academic databases, which are primary sources.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool's output includes multiple explicit source references with URLs, such as the first result linking to pmc.ncbi.nlm.nih.gov.",
                "panel": [
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output includes multiple explicit source references with URLs, such as the first result linking to pmc.ncbi.nlm.nih.gov.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool output provides multiple explicit source references, including URLs, titles, and source names for each search result.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output includes explicit URLs for each search result, enabling readers to follow back to the underlying scientific literature.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool returned a list of nine search results containing titles, URLs, and snippets relevant to the query.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned a list of nine search results containing titles, URLs, and snippets relevant to the query.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a JSON object containing a non-empty list of search results with titles, URLs, and snippets.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output includes a structured JSON response with multiple search results, titles, URLs, and snippets, demonstrating non-empty output was returned.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find scientific literature on graphene field-effect transistors for biosensing applications.\",\n  \"adapted_query\": \"Find scientific literature on graphene field-effect transistors for biosensing applications.\",\n  \"provider\": \"SerpAPI (Google)\",\n  \"answer\": \"\",\n  \"total_results\": 9,\n  \"api_params\": {\n    \"engine\": \"google\",\n    \"num\": 20\n  },\n  \"results\": [\n    {\n      \"title\": \"Graphene-Based Field-Effect Transistors in Biosensing ... - PMC\",\n      \"url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC11386440/\",\n      \"snippet\": \"GFET biosensors usually have a high signal-to-noise ratio due to the high carrier mobility and low electronic noise of graphene. Bonding of biomolecules to the ...\",\n      \"date\": \"\",\n      \"position\": 1,\n      \"source\": \"National Institutes of Health (NIH) | (.gov)\"\n    },\n    {\n      \"title\": \"Field-effect transistor for biosensing applications using a ...\",\n      \"url\": \"https://www.sciencedirect.com/science/article/pii/S2590137025001001\",\n      \"snippet\": \"In this paper, we report the use of amine-functionalized graphene by plasma polymerization to detect the presence of biomolecules in graphene channel based on ...\",\n      \"date\": \"\",\n      \"position\": 2,\n      \"source\": \"ScienceDirect.com\"\n    },\n    {\n      \"title\": \"Recent Advances in Graphene-Based Field-Effect ...\",\n      \"url\": \"https://www.mdpi.com/2079-6374/16/4/190\",\n      \"snipp …[truncated]"
          },
          {
            "probe_id": "obs-32721",
            "similarity": 0.966,
            "task_text": "Find the 2026 Applied Energy paper by Chen et al. on turning current mismatch into an advantage to suppress hysteresis in two-terminal tandem cells, and give me its DOI.",
            "adapted_input": "Chen et al. 2026 Applied Energy current mismatch hysteresis two-terminal tandem solar cells",
            "score": 0,
            "redacted": null,
            "output_chars": 4272,
            "truncated": false,
            "created_at": "2026-08-29T10:55:30.318527Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "fail",
                "score": 0,
                "rationale": "Deterministic check — matched 0/1 required string(s); missing: 10.1016/j.apenergy.2026.128576.",
                "panel": null
              }
            ],
            "raw_output": "{\n  \"query\": \"Chen et al. 2026 Applied Energy current mismatch hysteresis two-terminal tandem solar cells\",\n  \"adapted_query\": \"Chen et al. 2026 Applied Energy current mismatch hysteresis two-terminal tandem solar cells\",\n  \"provider\": \"SerpAPI (Google)\",\n  \"answer\": \"\",\n  \"total_results\": 9,\n  \"api_params\": {\n    \"engine\": \"google\",\n    \"num\": 20\n  },\n  \"results\": [\n    {\n      \"title\": \"suppressing hysteresis and improving operational stability ...\",\n      \"url\": \"https://www.sciencedirect.com/science/article/abs/pii/S0306261926012328\",\n      \"snippet\": \"Turning current mismatch into advantage: suppressing hysteresis and improving operational stability in two-terminal perovskite/silicon tandem solar cells.\",\n      \"date\": \"\",\n      \"position\": 1,\n      \"source\": \"ScienceDirect.com\"\n    },\n    {\n      \"title\": \"Origin of the Voltage Gap and Recombination Losses in All ...\",\n      \"url\": \"https://advanced.onlinelibrary.wiley.com/doi/10.1002/aenm.202505590?utm_source\\\\u003dresearchgate.net\\\\u0026utm_medium\\\\u003darticle\",\n      \"snippet\": \"The EL spectrum of the tandem solar cell exhibits two EL emission peaks at \\u223c1.23 eV (from NBG subcell) and \\u223c1.82 eV (from WBG subcell). The ...\",\n      \"date\": \"15\\u200f/01\\u200f/2026\",\n      \"position\": 2,\n      \"source\": \"Wiley & Sons\"\n    },\n    {\n      \"title\": \"Opto-electro-thermal Multiphysical Mechanisms and ...\",\n      \"url\": …[truncated]"
          }
        ]
      },
      "evidence_teaser": {
        "task_text": "Find recent papers by Geoffrey Hinton on neural networks published in the last few years.",
        "verdict": "partial",
        "score": 0.667,
        "similarity": 0.97,
        "n_real": 399
      }
    },
    {
      "tool_id": "openalex",
      "name": "OpenAlex Works API",
      "variant": null,
      "capabilities": [
        "paper_search",
        "academic",
        "references",
        "abstracts",
        "citation_graph"
      ],
      "description": "Open academic knowledge graph covering hundreds of millions of works across every research field. Returns titles, reconstructed abstracts, authors, venues, citation counts, DOI, OA URLs, and topic classifications.",
      "kind": "external_tool",
      "endpoint": {
        "api_type": "rest",
        "base_url": "https://api.openalex.org",
        "status_url": "https://status.openalex.org"
      },
      "reason": "lower capability (0.86 vs 0.98).",
      "capability": 0.8577,
      "band": 0.0389,
      "cap_lcb": 0.8188,
      "rank": 0.9231,
      "price": {
        "amount": 0,
        "per_query_usd": 0,
        "currency": "USD",
        "confidence": "high",
        "selected_plan": "free",
        "held": false,
        "estimated": true,
        "cost_unknown": false,
        "breakdown": [
          {
            "plan_id": "free",
            "kind": "free",
            "plan_group": null,
            "effective_usd": 0,
            "held": false,
            "currency": "USD",
            "confidence": "high",
            "overridden": false
          }
        ]
      },
      "calling": {
        "tool_id": "openalex",
        "coordinator_class": false,
        "executable": true,
        "endpoint": {
          "base_url": "https://api.openalex.org",
          "api_type": "rest"
        },
        "adapter": {
          "type": "llm"
        },
        "auth": {
          "method": "none"
        },
        "summary": {
          "usability": "ready",
          "auth_method": "none",
          "api_type": "rest",
          "connected": false,
          "free": true,
          "how": "free · ready to use",
          "signup_url": null
        }
      },
      "facets": [
        {
          "name": "capability",
          "kano": "must_be",
          "weight": 1,
          "threshold": 0.5,
          "raw": 0.8188,
          "contribution": 0.7463
        },
        {
          "name": "price",
          "kano": "performance",
          "weight": 0.3,
          "threshold": 0.5,
          "raw": 1,
          "contribution": 0.3
        },
        {
          "name": "no_machine_harm",
          "kano": "must_be",
          "weight": 2,
          "threshold": 0.5,
          "raw": 1,
          "contribution": 2
        }
      ],
      "evidence": {
        "n_real": 195,
        "n_near": 24,
        "near_mean": 0.71,
        "dist": [
          0.233,
          0.933,
          1,
          1,
          1,
          0.983,
          1,
          0.983,
          1,
          1,
          1,
          1,
          0.983,
          0.983,
          0.133,
          0,
          0,
          0.75,
          0,
          0,
          1,
          0.1,
          0.983,
          0.967
        ],
        "probes": [
          {
            "probe_id": "obs-28653",
            "similarity": 0.97,
            "task_text": "Find recent papers by Geoffrey Hinton on neural networks published in the last few years.",
            "adapted_input": "{\"search\": \"neural networks deep learning\"}",
            "score": 0.233,
            "redacted": null,
            "output_chars": 19797,
            "truncated": false,
            "created_at": "2026-08-12T17:34:57.049433Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "fail",
                "score": 0.233,
                "rationale": "The tool failed significantly to address the core constraints of the query. It ignored the specific  | The tool returned a generic search for 'neural networks deep learning' without filtering by author G | The tool returned papers on neural networks but failed to adequately filter for Geoffrey Hinton as a",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool failed significantly to address the core constraints of the query. It ignored the specific author 'Geoffrey Hinton' in its search adaptation (using only 'neural networks deep learning'), resulting in a list of highly cited papers on the topic that do not feature Hinton as a primary author. …",
                    "score": 0.2
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a generic search for 'neural networks deep learning' without filtering by author Geoffrey Hinton or recency. Only one result (ImageNet classification, 2017) includes Hinton, but it is not recent (last few years). The vast majority of results are irrelevant, failing to address the q…",
                    "score": 0.2
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned papers on neural networks but failed to adequately filter for Geoffrey Hinton as an author. Only one paper in the top results includes Hinton, and it is an older publication (2017) not matching the recent works highlighted in the ground truth (e.g., capsule networks, forward-forwar…",
                    "score": 0.3
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "partial",
                "score": 0.5,
                "rationale": "The top results include many papers on neural networks but only one (the 4th result) has Geoffrey Hinton as a co-author, and the query specifically asks for papers by Hinton, so the results are mixed with off-topic items.",
                "panel": [
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The top results include many papers on neural networks but only one (the 4th result) has Geoffrey Hinton as a co-author, and the query specifically asks for papers by Hinton, so the results are mixed with off-topic items.",
                    "label": "partial",
                    "value": 0.5
                  },
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "While one result includes Geoffrey Hinton as an author, the majority of the top results are general papers on neural networks that do not feature him, failing to prioritize the specific author requested.",
                    "label": "partial",
                    "value": 0.5
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returns some relevant papers by Geoffrey Hinton, such as a 2017 publication, but the top results are largely dominated by non-Hinton papers, mixing relevance with noise.",
                    "label": "partial",
                    "value": 0.5
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool's output includes citations to peer-reviewed papers and academic venues, which are primary authoritative sources.",
                "panel": [
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output includes citations to peer-reviewed papers and academic venues, which are primary authoritative sources.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides citations to peer-reviewed academic papers from journals and conferences such as CVPR and Communications of the ACM.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output cites peer-reviewed academic papers from reputable journals and conferences, which are primary sources.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool output provides explicit source references including DOIs and OpenAlex URLs for each paper listed.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool output provides explicit source references including DOIs and OpenAlex URLs for each paper listed.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The output includes explicit source references such as DOIs, OpenAlex IDs, and open access URLs for each paper, allowing a reader to follow back to the underlying material.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The output includes explicit URLs and DOIs for each paper, which are direct source references that a reader can follow.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool returned a non-empty JSON output containing multiple paper results, indicating a usable response.",
                "panel": [
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a non-empty JSON output containing multiple paper results, indicating a usable response.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool provided a detailed JSON response with multiple results, which is non-empty output for the query.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned a non-empty list of search results containing academic papers.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find recent papers by Geoffrey Hinton on neural networks published in the last few years.\",\n  \"adapted_spec\": {\n    \"search\": \"neural networks deep learning\"\n  },\n  \"lookup_mode\": \"keyword\",\n  \"provider\": \"OpenAlex\",\n  \"tool_kind\": \"academic paper search (all fields, citation graph)\",\n  \"total_results\": 1793304,\n  \"returned_results\": 30,\n  \"results\": [\n    {\n      \"id\": \"https://openalex.org/W2194775991\",\n      \"doi\": \"https://doi.org/10.1109/cvpr.2016.90\",\n      \"title\": \"Deep Residual Learning for Image Recognition\",\n      \"authors\": [\n        \"Kaiming He\",\n        \"Xiangyu Zhang\",\n        \"Shaoqing Ren\",\n        \"Jian Sun\"\n      ],\n      \"publication_year\": 2016,\n      \"publication_date\": \"2016-06-01\",\n      \"venue\": null,\n      \"venue_type\": null,\n      \"cited_by_count\": 225525,\n      \"open_access_url\": \"https://repositorio.unal.edu.co/handle/unal/81443\",\n      \"is_open_access\": true,\n      \"abstract\": \"Deeper neural networks are more difficult to train. We present a residual learning framework to ease the training of networks that are substantially deeper than those used previously. We explicitly reformulate the layers as learning residual functions with reference to the layer inputs, instead of learning unreferenced functions. We provide comprehensive empirical evidence showing that these residual networks are easier to optimize, and can gain accuracy from c …[truncated]"
          },
          {
            "probe_id": "obs-28372",
            "similarity": 0.968,
            "task_text": "Find scientific literature on graphene field-effect transistors for biosensing applications.",
            "adapted_input": "{\"search\": \"graphene field-effect transistor biosensing\"}",
            "score": 0.933,
            "redacted": null,
            "output_chars": 20000,
            "truncated": true,
            "created_at": "2026-08-12T10:40:04.218083Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 0.933,
                "rationale": "The tool successfully identified highly relevant, high-quality scientific literature that matches al | The tool returned highly relevant, correctly indexed papers on graphene FET biosensors, with accurat | The tool returned multiple relevant, real peer-reviewed papers on graphene field-effect transistors ",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool successfully identified highly relevant, high-quality scientific literature that matches all components of the query (graphene, field-effect transistors, and biosensing). The results include specific research papers and reviews with correct metadata (titles, authors, DOIs, and abstracts) an…",
                    "score": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned highly relevant, correctly indexed papers on graphene FET biosensors, with accurate metadata (titles, authors, years, DOIs, venues). The top results directly match the query, and the output is well-structured. Minor note: the first result is broader but still relevant. Overall, exc…",
                    "score": 0.9
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned multiple relevant, real peer-reviewed papers on graphene field-effect transistors for biosensing, with accurate metadata including titles, authors, years, DOIs, and venues. It successfully surfaced indexed literature matching the query, and the top results include canonical and spe…",
                    "score": 0.9
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "The top three results are highly specific and directly address the query, covering graphene biosensing, graphene-based FET biosensors for cancer, and rGO FETs for biosensing applications.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The top three results are highly specific and directly address the query, covering graphene biosensing, graphene-based FET biosensors for cancer, and rGO FETs for biosensing applications.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The top three results are directly relevant peer-reviewed papers on graphene field-effect transistors for biosensing, with correct titles, authors, and venues, perfectly matching the query intent.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The top three results directly address graphene field-effect transistors for biosensing, with high-quality sources like Materials Today, Carbon, and Biosensors and Bioelectronics.",
                    "label": "excellent",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool provides citations to peer-reviewed scientific journal articles from reputable publishers like Elsevier (Carbon, Biosensors and Bioelectronics) and ACS (ACS Nano).",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides citations to peer-reviewed scientific journal articles from reputable publishers like Elsevier (Carbon, Biosensors and Bioelectronics) and ACS (ACS Nano).",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool outputs peer-reviewed journal articles, which are primary authoritative sources in scientific literature.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output consists of peer-reviewed academic papers, which are primary sources as defined in the rubric.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The output includes explicit source references such as DOIs, URLs, and document IDs for each result, allowing a reader to follow back to the original papers.",
                "panel": [
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The output includes explicit source references such as DOIs, URLs, and document IDs for each result, allowing a reader to follow back to the original papers.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides explicit source references including DOIs, OpenAlex IDs, and URLs for each paper listed.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output includes explicit source references such as DOIs and OpenAlex URLs for each listed paper, allowing readers to directly access the underlying material.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool returned a structured JSON object containing a list of relevant scientific papers with titles, authors, and DOIs.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned a structured JSON object containing a list of relevant scientific papers with titles, authors, and DOIs.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a non-empty output with a list of 30 results and a total count of 9076, so it provided usable output.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output includes a structured list of academic papers with titles, authors, and other details, which is non-empty and usable for the query.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find scientific literature on graphene field-effect transistors for biosensing applications.\",\n  \"adapted_spec\": {\n    \"search\": \"graphene field-effect transistor biosensing\"\n  },\n  \"lookup_mode\": \"keyword\",\n  \"provider\": \"OpenAlex\",\n  \"tool_kind\": \"academic paper search (all fields, citation graph)\",\n  \"total_results\": 9076,\n  \"returned_results\": 30,\n  \"results\": [\n    {\n      \"id\": \"https://openalex.org/W2122857078\",\n      \"doi\": \"https://doi.org/10.1016/s1369-7021(11)70160-2\",\n      \"title\": \"Graphene in biosensing\",\n      \"authors\": [\n        \"Martin Pumera\"\n      ],\n      \"publication_year\": 2011,\n      \"publication_date\": \"2011-07-01\",\n      \"venue\": \"Materials Today\",\n      \"venue_type\": \"journal\",\n      \"cited_by_count\": 844,\n      \"open_access_url\": \"https://www.sciencedirect.com/science/article/pii/S1369702111701602/pdf\",\n      \"is_open_access\": true,\n      \"abstract\": \"Biosensing is paramount for improving the quality of human life. Biosensors and biosensing protocols are able to detect a wide range of compounds, sensitively and selectively, with applications in security, health care for point-of-care analyses of diseases, and environmental safety. Here, we describe biosensors and biosensing systems employing graphene. Graphene is a zero-gap semiconductor material, which is electroactive and transparent. Because of its interesting properties, graphene h …[truncated]"
          },
          {
            "probe_id": "obs-12382",
            "similarity": 0.966,
            "task_text": "Find the 2024 Quaternary Science Reviews paper reporting isotope analysis of remains from the A14 road project in Cambridgeshire, UK.",
            "adapted_input": "{\"search\": \"A14 isotope Cambridgeshire\", \"year\": 2024}",
            "score": 1,
            "redacted": null,
            "output_chars": 1783,
            "truncated": false,
            "created_at": "2026-06-27T00:51:51.983863Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "The tool successfully identified the exact paper requested. The title, journal (Quaternary Science R | The tool returned exactly one result, which is the correct 2024 Quaternary Science Reviews paper wit | The tool returned the exact paper specified in the ground truth with correct title, authors, year, D",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool successfully identified the exact paper requested. The title, journal (Quaternary Science Reviews), year (2024), authors, and DOI all match the ground truth perfectly.",
                    "score": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned exactly one result, which is the correct 2024 Quaternary Science Reviews paper with the precise title, authors, DOI, and abstract matching the ground truth. No irrelevant records or fabricated identifiers were present.",
                    "score": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned the exact paper specified in the ground truth with correct title, authors, year, DOI, and venue, fully addressing the query without any errors or irrelevant results.",
                    "score": 1
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "The tool returned the exact paper requested by the user, matching the title, journal, year, and DOI specified in the ground truth.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned the exact paper requested by the user, matching the title, journal, year, and DOI specified in the ground truth.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The single result returned is the exact paper requested, directly matching the query intent with the correct title, journal, year, and topic of isotope analysis from the A14 project.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output directly returns the exact paper specified in the query, matching all criteria including year, journal, and topic.",
                    "label": "excellent",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool provides a citation for a peer-reviewed academic paper published in the journal Quaternary Science Reviews.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides a citation for a peer-reviewed academic paper published in the journal Quaternary Science Reviews.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool output cites a specific peer-reviewed paper from the journal Quaternary Science Reviews, which is a primary source per the rubric definition.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output cites a peer-reviewed paper, which is a primary source according to the rubric.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool provides a direct OpenAlex ID, a DOI URL, and an open access URL for the identified paper.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides a direct OpenAlex ID, a DOI URL, and an open access URL for the identified paper.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The output includes explicit source references such as a DOI, open access URL, and full bibliographic details like title, authors, and journal.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output includes explicit URLs and DOI that serve as source references.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool successfully returned a JSON object containing a specific academic paper that matches the user's query.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool successfully returned a JSON object containing a specific academic paper that matches the user's query.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a single paper that matches the requested query.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned a non-empty JSON response with structured search results, indicating usable output.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find the 2024 Quaternary Science Reviews paper reporting isotope analysis of remains from the A14 road project in Cambridgeshire, UK.\",\n  \"adapted_spec\": {\n    \"search\": \"A14 isotope Cambridgeshire\",\n    \"year\": 2024\n  },\n  \"lookup_mode\": \"keyword\",\n  \"provider\": \"OpenAlex\",\n  \"tool_kind\": \"academic paper search (all fields, citation graph)\",\n  \"total_results\": 1,\n  \"returned_results\": 1,\n  \"results\": [\n    {\n      \"id\": \"https://openalex.org/W4404281390\",\n      \"doi\": \"https://doi.org/10.1016/j.quascirev.2024.109059\",\n      \"title\": \"Revealing continuity and sustainability through isotope analysis on the A14 project, Cambridgeshire, UK\",\n      \"authors\": [\n        \"Michael Wallace\",\n        \"Janet Montgomery\",\n        \"B. Rogers\",\n        \"Joanna Moore\",\n        \"Geoff Nowell\",\n        \"David Bowsher\",\n        \"Albert E. Smith\"\n      ],\n      \"publication_year\": 2024,\n      \"publication_date\": \"2024-11-13\",\n      \"venue\": \"Quaternary Science Reviews\",\n      \"venue_type\": \"journal\",\n      \"cited_by_count\": 1,\n      \"open_access_url\": \"https://doi.org/10.1016/j.quascirev.2024.109059\",\n      \"is_open_access\": true,\n      \"abstract\": \"The A14 archaeological project was the largest commercial archaeological programme in the UK - spanning a 25 km stretch of rural Cambridgeshire, which included a pioneering and ambitious multi-isotope programme to examine crop, livestoc …[truncated]"
          }
        ]
      },
      "evidence_teaser": {
        "task_text": "Find recent papers by Geoffrey Hinton on neural networks published in the last few years.",
        "verdict": "returned",
        "score": 0.233,
        "similarity": 0.97,
        "n_real": 195
      }
    },
    {
      "tool_id": "unpaywall",
      "name": "Unpaywall (via Crossref)",
      "variant": null,
      "capabilities": [
        "pdf_locator",
        "open_access",
        "references",
        "academic"
      ],
      "description": "Open-access PDF locator. Resolves a query to the top-ranked Crossref DOI, then asks Unpaywall for the best legally-available open-access copy (publisher OA, repository deposit, preprint). Reports whether a paywalled paper has a free alternative, and reports a DOI Unpaywall does not index (DataCite-registered, figure/supplement component DOIs) as not held rather than as an error.",
      "kind": "external_tool",
      "endpoint": {
        "api_type": "rest",
        "base_url": "https://api.unpaywall.org",
        "status_url": "https://unpaywall.org"
      },
      "reason": "lower capability (0.85 vs 0.98).",
      "capability": 0.8526,
      "band": 0.0378,
      "cap_lcb": 0.8148,
      "rank": 0.9214,
      "price": {
        "amount": 0,
        "per_query_usd": 0,
        "currency": "USD",
        "confidence": "high",
        "selected_plan": "free",
        "held": false,
        "estimated": true,
        "cost_unknown": false,
        "breakdown": [
          {
            "plan_id": "free",
            "kind": "free",
            "plan_group": null,
            "effective_usd": 0,
            "held": false,
            "currency": "USD",
            "confidence": "high",
            "overridden": false
          }
        ]
      },
      "calling": {
        "tool_id": "unpaywall",
        "coordinator_class": false,
        "executable": true,
        "endpoint": {
          "base_url": "https://api.unpaywall.org",
          "api_type": "rest"
        },
        "adapter": {
          "type": "llm"
        },
        "auth": {
          "method": "none"
        },
        "summary": {
          "usability": "ready",
          "auth_method": "none",
          "api_type": "rest",
          "connected": false,
          "free": true,
          "how": "free · ready to use",
          "signup_url": null
        }
      },
      "facets": [
        {
          "name": "capability",
          "kano": "must_be",
          "weight": 1,
          "threshold": 0.5,
          "raw": 0.8148,
          "contribution": 0.7407
        },
        {
          "name": "price",
          "kano": "performance",
          "weight": 0.3,
          "threshold": 0.5,
          "raw": 1,
          "contribution": 0.3
        },
        {
          "name": "no_machine_harm",
          "kano": "must_be",
          "weight": 2,
          "threshold": 0.5,
          "raw": 1,
          "contribution": 2
        }
      ],
      "evidence": {
        "n_real": 113,
        "n_near": 24,
        "near_mean": 0.67,
        "dist": [
          1,
          1,
          0.1,
          0.233,
          1,
          1,
          1,
          1,
          0.933,
          0.2,
          0.267,
          0.267,
          0,
          0,
          1,
          0.933,
          0.883,
          0.967,
          0,
          0.767,
          0.8,
          0.767,
          1,
          0.967
        ],
        "probes": [
          {
            "probe_id": "obs-32706",
            "similarity": 0.966,
            "task_text": "Find the 2026 Applied Energy paper by Chen et al. on turning current mismatch into an advantage to suppress hysteresis in two-terminal tandem cells, and give me its DOI.",
            "adapted_input": "{\"title\": \"current mismatch suppress hysteresis two-terminal tandem solar cells\", \"author\": \"Chen\", \"year\": 2026}",
            "score": 1,
            "redacted": null,
            "output_chars": 1124,
            "truncated": false,
            "created_at": "2026-08-29T10:47:57.929256Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "Deterministic check — matched 1/1 required string(s).",
                "panel": null
              }
            ],
            "raw_output": "{\n  \"query\": \"Find the 2026 Applied Energy paper by Chen et al. on turning current mismatch into an advantage to suppress hysteresis in two-terminal tandem cells, and give me its DOI.\",\n  \"provider\": \"Unpaywall (via Crossref top-DOI lookup)\",\n  \"tool_kind\": \"open-access PDF locator (DOI-keyed)\",\n  \"resolved_paper\": {\n    \"doi\": \"10.1016/j.apenergy.2026.128576\",\n    \"resolved_by\": \"crossref:query.title\",\n    \"title\": \"Turning current mismatch into advantage: suppressing hysteresis and improving operational stability in two-terminal perovskite/silicon tandem solar cells\",\n    \"year\": 2026,\n    \"journal\": \"Applied Energy\",\n    \"is_open_access\": true,\n    \"oa_status\": \"hybrid\"\n  },\n  \"best_open_access_location\": {\n    \"url\": \"https://doi.org/10.1016/j.apenergy.2026.128576\",\n    \"url_for_pdf\": null,\n    \"host_type\": \"publisher\",\n    \"version\": \"publishedVersion\",\n    \"license\": \"cc-by\"\n  },\n  \"all_oa_locations\": [\n    {\n      \"url\": \"https://doi.org/10.1016/j.apenergy.2026.128576\",\n      \"url_for_pdf\": null,\n      \"host_type\": \"publisher\",\n      \"version\": \"publishedVersion\",\n      \"license\": \"cc-by\"\n    }\n  ]\n}"
          },
          {
            "probe_id": "obs-32683",
            "similarity": 0.959,
            "task_text": "I'm after the 2026 Advanced Energy Materials paper by Zhang et al. on molecular design and interfacial functions of self-assembled monolayers for perovskite and tandem solar cells. Give me the DOI.",
            "adapted_input": "{\"title\": \"molecular design and interfacial functions of self-assembled monolayers for perovskite and tandem solar cells\", \"author\": \"Zhang\", \"year\": 2026}",
            "score": 1,
            "redacted": null,
            "output_chars": 1088,
            "truncated": false,
            "created_at": "2026-08-29T10:36:59.959081Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "Deterministic check — matched 1/1 required string(s).",
                "panel": null
              }
            ],
            "raw_output": "{\n  \"query\": \"I'm after the 2026 Advanced Energy Materials paper by Zhang et al. on molecular design and interfacial functions of self-assembled monolayers for perovskite and tandem solar cells. Give me the DOI.\",\n  \"provider\": \"Unpaywall (via Crossref top-DOI lookup)\",\n  \"tool_kind\": \"open-access PDF locator (DOI-keyed)\",\n  \"resolved_paper\": {\n    \"doi\": \"10.1002/aenm.70979\",\n    \"resolved_by\": \"crossref:query.title\",\n    \"title\": \"Molecular Design and Interfacial Functions of Self\\u2010Assembled Monolayers for Perovskite and Tandem Solar Cells\",\n    \"year\": 2026,\n    \"journal\": \"Advanced Energy Materials\",\n    \"is_open_access\": true,\n    \"oa_status\": \"hybrid\"\n  },\n  \"best_open_access_location\": {\n    \"url\": \"https://doi.org/10.1002/aenm.70979\",\n    \"url_for_pdf\": null,\n    \"host_type\": \"publisher\",\n    \"version\": \"publishedVersion\",\n    \"license\": \"cc-by\"\n  },\n  \"all_oa_locations\": [\n    {\n      \"url\": \"https://doi.org/10.1002/aenm.70979\",\n      \"url_for_pdf\": null,\n      \"host_type\": \"publisher\",\n      \"version\": \"publishedVersion\",\n      \"license\": \"cc-by\"\n    }\n  ]\n}"
          },
          {
            "probe_id": "obs-1805",
            "similarity": 0.958,
            "task_text": "Find the LIGO Scientific Collaboration paper reporting the first direct observation of gravitational waves from a binary black hole merger (GW150914).",
            "adapted_input": "Find the LIGO Scientific Collaboration paper reporting the first direct observation of gravitational waves from a binary black hole merger (GW150914).",
            "score": 0.1,
            "redacted": null,
            "output_chars": 1154,
            "truncated": false,
            "created_at": "2026-05-20T02:19:30.850657Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "fail",
                "score": 0.1,
                "rationale": "The tool failed to identify the correct paper. Instead of finding the seminal 2016 Physical Review L | The tool returned a review paper (DOI 10.22541/au.161220228.87275329) that discusses the original GW | The tool returned a review paper from 2021 about GW150914 instead of the original 2016 LIGO Scientif",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool failed to identify the correct paper. Instead of finding the seminal 2016 Physical Review Letters paper (DOI: 10.1103/physrevlett.116.061102), it returned a 2021 review paper from Authorea. This is a significant error in accuracy and relevance.",
                    "score": 0
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a review paper (DOI 10.22541/au.161220228.87275329) that discusses the original GW150914 observation but is not the actual LIGO Scientific Collaboration paper reporting the discovery. The ground truth expects the 2016 Physical Review Letters paper by Abbott et al. (DOI 10.1103/phys…",
                    "score": 0
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned a review paper from 2021 about GW150914 instead of the original 2016 LIGO Scientific Collaboration paper in Physical Review Letters, misidentifying the specific paper requested in the query.",
                    "score": 0.3
                  }
                ]
              },
              {
                "facet": "format",
                "verdict": "structured",
                "score": 1,
                "rationale": "The tool output is a valid JSON object containing all the expected fields for a machine-parseable response.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool output is a valid JSON object containing all the expected fields for a machine-parseable response.",
                    "label": "structured",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool output is a valid JSON object with well-defined fields such as resolved_paper, best_open_access_location, and all_oa_locations, making it machine-parseable and structured.",
                    "label": "structured",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output is a complete JSON object with clearly defined fields like doi, title, year, and access locations, making it fully machine-parseable.",
                    "label": "structured",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "freshness",
                "verdict": "not_applicable",
                "score": 1,
                "rationale": "The query asks for a specific historical scientific paper, which is a static fact where freshness is not a relevant metric.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The query asks for a specific historical scientific paper, which is a static fact where freshness is not a relevant metric.",
                    "label": "not_applicable",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The query asks for a static historical fact (the original 2016 paper), so the freshness of the tool's output is irrelevant to evaluating its correctness.",
                    "label": "not_applicable",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The query is about a historical scientific paper from 2016, which is a static fact where freshness is irrelevant.",
                    "label": "not_applicable",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "poor",
                "score": 0.25,
                "rationale": "The tool returned a review paper about reproducing the event rather than the actual primary research paper requested by the user.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned a review paper about reproducing the event rather than the actual primary research paper requested by the user.",
                    "label": "poor",
                    "value": 0.25
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returns a 2021 review of the GW150914 paper rather than the original 2016 LIGO Scientific Collaboration paper, so it is topically relevant but not the exact requested source.",
                    "label": "partial",
                    "value": 0.5
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned a review article from 2021 instead of the original 2016 paper, making the result only tangentially related to the query intent.",
                    "label": "poor",
                    "value": 0.25
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "reputable_secondary",
                "score": 0.75,
                "rationale": "The tool failed to find the primary peer-reviewed paper and instead provided a review/reproduction paper from Authorea, which acts as a secondary source regarding the original discovery.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool failed to find the primary peer-reviewed paper and instead provided a review/reproduction paper from Authorea, which acts as a secondary source regarding the original discovery.",
                    "label": "reputable_secondary",
                    "value": 0.75
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a review article on Authorea instead of the original peer-reviewed Physical Review Letters paper, thus citing a low-quality source.",
                    "label": "low_quality",
                    "value": 0
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned a review paper from Authorea, which is a secondary source analyzing the primary research, rather than the original peer-reviewed publication.",
                    "label": "reputable_secondary",
                    "value": 0.75
                  }
                ]
              },
              {
                "facet": "snippet_quality",
                "verdict": "informative",
                "score": 1,
                "rationale": "The output provides specific metadata including the DOI, title, year, journal, and open access status, allowing the user to evaluate the relevance of the result.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The output provides specific metadata including the DOI, title, year, journal, and open access status, allowing the user to evaluate the relevance of the result.",
                    "label": "informative",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output provides a detailed title, DOI, year, journal, and open-access status, allowing the reader to see that it is a review article rather than the original GW150914 paper, thus enabling relevance assessment without clicking through.",
                    "label": "informative",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool output provides structured metadata such as title and URL but lacks any descriptive text snippets that would let the reader assess relevance without clicking.",
                    "label": "absent",
                    "value": 0
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool output provides a specific DOI, a title, and multiple direct URLs to the document.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool output provides a specific DOI, a title, and multiple direct URLs to the document.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output includes a DOI, a URL for the PDF, and a named document title, all of which are explicit source references that a reader can follow back to the underlying material.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output includes explicit URLs and a DOI that serve as source references for the paper.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool provided a structured JSON response containing a resolved paper, DOI, and URL, even though it identified a review paper rather than the original discovery paper.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provided a structured JSON response containing a resolved paper, DOI, and URL, even though it identified a review paper rather than the original discovery paper.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a non-empty JSON object containing metadata and open-access location details for a paper.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned a non-empty JSON object containing paper details, which is usable output regardless of correctness.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find the LIGO Scientific Collaboration paper reporting the first direct observation of gravitational waves from a binary black hole merger (GW150914).\",\n  \"provider\": \"Unpaywall (via Crossref top-DOI lookup)\",\n  \"tool_kind\": \"open-access PDF locator (DOI-keyed)\",\n  \"resolved_paper\": {\n    \"doi\": \"10.22541/au.161220228.87275329/v1\",\n    \"title\": \"Review: \\\"Reproducing GW150914: the first observation of gravitational waves from a binary black hole merger\\\"\",\n    \"year\": 2021,\n    \"journal\": \"Authorea, Inc.\",\n    \"is_open_access\": true,\n    \"oa_status\": \"gold\"\n  },\n  \"best_open_access_location\": {\n    \"url\": \"https://www.authorea.com/doi/pdf/10.22541/au.161220228.87275329\",\n    \"url_for_pdf\": \"https://www.authorea.com/doi/pdf/10.22541/au.161220228.87275329\",\n    \"host_type\": null,\n    \"version\": \"acceptedVersion\",\n    \"license\": null\n  },\n  \"all_oa_locations\": [\n    {\n      \"url\": \"https://www.authorea.com/doi/pdf/10.22541/au.161220228.87275329\",\n      \"url_for_pdf\": \"https://www.authorea.com/doi/pdf/10.22541/au.161220228.87275329\",\n      \"host_type\": null,\n      \"version\": \"acceptedVersion\",\n      \"license\": null\n    }\n  ]\n}"
          }
        ]
      },
      "evidence_teaser": {
        "task_text": "Find the 2026 Applied Energy paper by Chen et al. on turning current mismatch into an advantage to suppress hysteresis in two-terminal tandem cells, and give me its DOI.",
        "verdict": "pass",
        "score": 1,
        "similarity": 0.966,
        "n_real": 113
      }
    },
    {
      "tool_id": "europe_pmc",
      "name": "Europe PMC",
      "variant": null,
      "capabilities": [
        "paper_search",
        "academic",
        "references",
        "abstracts",
        "medical_literature",
        "biomedical",
        "full_text"
      ],
      "description": "Life-science literature search covering peer-reviewed papers plus preprints (medRxiv, bioRxiv) plus the PubMed Central open-access subset with full-text URLs. Returns title, abstract, authors, journal, PMID/PMCID/DOI, OA full-text links, and citation counts.",
      "kind": "external_tool",
      "endpoint": {
        "api_type": "rest",
        "base_url": "https://www.ebi.ac.uk/europepmc",
        "status_url": "https://europepmc.org"
      },
      "reason": "lower capability (0.83 vs 0.98).",
      "capability": 0.8261,
      "band": 0.0477,
      "cap_lcb": 0.7784,
      "rank": 0.906,
      "price": {
        "amount": 0,
        "per_query_usd": 0,
        "currency": "USD",
        "confidence": "high",
        "selected_plan": "free",
        "held": false,
        "estimated": true,
        "cost_unknown": false,
        "breakdown": [
          {
            "plan_id": "free",
            "kind": "free",
            "plan_group": null,
            "effective_usd": 0,
            "held": false,
            "currency": "USD",
            "confidence": "high",
            "overridden": false
          }
        ]
      },
      "calling": {
        "tool_id": "europe_pmc",
        "coordinator_class": false,
        "executable": true,
        "endpoint": {
          "base_url": "https://www.ebi.ac.uk/europepmc",
          "api_type": "rest"
        },
        "adapter": {
          "type": "llm"
        },
        "auth": {
          "method": "none"
        },
        "summary": {
          "usability": "ready",
          "auth_method": "none",
          "api_type": "rest",
          "connected": false,
          "free": true,
          "how": "free · ready to use",
          "signup_url": null
        }
      },
      "facets": [
        {
          "name": "capability",
          "kano": "must_be",
          "weight": 1,
          "threshold": 0.5,
          "raw": 0.7784,
          "contribution": 0.6898
        },
        {
          "name": "price",
          "kano": "performance",
          "weight": 0.3,
          "threshold": 0.5,
          "raw": 1,
          "contribution": 0.3
        },
        {
          "name": "no_machine_harm",
          "kano": "must_be",
          "weight": 2,
          "threshold": 0.5,
          "raw": 1,
          "contribution": 2
        }
      ],
      "evidence": {
        "n_real": 91,
        "n_near": 24,
        "near_mean": 0.873,
        "dist": [
          0.733,
          1,
          1,
          0.5,
          0.983,
          1,
          0.95,
          1,
          1,
          1,
          0.967,
          1,
          0.983,
          0.833,
          1,
          1,
          1,
          0,
          0.933,
          0.167,
          0.967,
          1,
          0.967,
          0.967
        ],
        "probes": [
          {
            "probe_id": "obs-28353",
            "similarity": 0.968,
            "task_text": "Find scientific literature on graphene field-effect transistors for biosensing applications.",
            "adapted_input": "Find scientific literature on graphene field-effect transistors for biosensing applications.",
            "score": 0.733,
            "redacted": null,
            "output_chars": 18045,
            "truncated": false,
            "created_at": "2026-08-12T09:54:28.112732Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 0.733,
                "rationale": "The tool returned a large number of results (2410) and the top results are real indexed papers, but  | The tool successfully identified highly relevant scientific literature. The first result is a specif | The tool successfully returns real, indexed peer-reviewed papers with correct metadata (DOIs, PMIDs)",
                "panel": [
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a large number of results (2410) and the top results are real indexed papers, but their relevance to the specific query 'graphene field-effect transistors for biosensing' is mixed. The first result is about a FET-based biosensor for SARS-CoV-2 but does not explicitly mention graphe…",
                    "score": 0.6
                  },
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool successfully identified highly relevant scientific literature. The first result is a specific paper on FET-based biosensors (though it focuses on SARS-CoV-2, it fits the technology profile), and the third result is a highly relevant review on graphene biofunctionalization and biosensors. Th…",
                    "score": 0.9
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool successfully returns real, indexed peer-reviewed papers with correct metadata (DOIs, PMIDs) and adapts the query effectively, yielding 2410 results. However, the top results shown include some papers not specifically focused on graphene FETs (e.g., one on carbon nanotubes, another on genera…",
                    "score": 0.7
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "partial",
                "score": 0.5,
                "rationale": "While the first and third results are highly relevant to graphene and biosensing, the second result focuses on carbon nanotubes rather than graphene, introducing off-topic noise into the top results.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "While the first and third results are highly relevant to graphene and biosensing, the second result focuses on carbon nanotubes rather than graphene, introducing off-topic noise into the top results.",
                    "label": "partial",
                    "value": 0.5
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The top results include highly relevant papers like the FET-based SARS-CoV-2 biosensor and graphene bioapplications, but the second result focuses on carbon nanotubes rather than graphene FETs, reducing perfect targeting.",
                    "label": "good",
                    "value": 0.75
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The top results include some relevant items like graphene bioapplications but mixed with off-topic results like carbon nanotubes and non-graphene FET biosensors, not perfectly targeted to the query.",
                    "label": "partial",
                    "value": 0.5
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool provides citations to peer-reviewed scientific papers from indexed databases like MED/PubMed.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides citations to peer-reviewed scientific papers from indexed databases like MED/PubMed.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returns peer-reviewed papers from Europe PMC (MED), which are authoritative primary sources in scientific literature.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool cites peer-reviewed scientific papers from Europe PMC, which are primary sources as per the rubric.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool's output includes explicit citation markers like DOIs and PMIDs for each paper, allowing readers to follow back to the underlying material.",
                "panel": [
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output includes explicit citation markers like DOIs and PMIDs for each paper, allowing readers to follow back to the underlying material.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides explicit source references including DOIs, PMIDs, and PMCID identifiers for each scientific paper listed.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output includes explicit references such as PubMed IDs (PMID), DOIs, and publication details for each of the returned results, allowing a reader to follow back to the original papers.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool returned a structured JSON object containing a list of relevant scientific papers and metadata.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned a structured JSON object containing a list of relevant scientific papers and metadata.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a non-empty JSON object containing 30 results with titles and metadata.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool output contains a non-empty JSON object with a list of scientific literature results, indicating that usable output was returned.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find scientific literature on graphene field-effect transistors for biosensing applications.\",\n  \"adapted_query\": \"graphene field-effect transistor biosensor\",\n  \"provider\": \"Europe PMC\",\n  \"tool_kind\": \"life-science literature search (papers + preprints + OA full text)\",\n  \"total_results\": 2410,\n  \"returned_results\": 30,\n  \"results\": [\n    {\n      \"id\": \"32293168\",\n      \"source\": \"MED\",\n      \"pmid\": \"32293168\",\n      \"pmcid\": null,\n      \"doi\": \"10.1021/acsnano.0c02823\",\n      \"title\": \"Rapid Detection of COVID-19 Causative Virus (SARS-CoV-2) in Human Nasopharyngeal Swab Specimens Using Field-Effect Transistor-Based Biosensor.\",\n      \"authors\": \"Seo G, Lee G, Kim MJ, Baek SH, Choi M, Ku KB, Lee CS, Jun S, Park D, Kim HG, Kim SJ, Lee JO, Kim BT, Park EC, Kim SI.\",\n      \"journal\": null,\n      \"publication_year\": \"2020\",\n      \"publication_type\": null,\n      \"cited_by_count\": 1029,\n      \"is_open_access\": false,\n      \"abstract\": \"Coronavirus disease 2019 (COVID-19) is a newly emerging human infectious disease caused by severe acute respiratory syndrome coronavirus 2 (SARS-CoV-2, previously called 2019-nCoV). Based on the rapid increase in the rate of human infection, the World Health Organization (WHO) has classified the COVID-19 outbreak as a pandemic. Because no specific drugs or vaccines for COVID-19 are yet available, early diagnosis and management are cruc …[truncated]"
          },
          {
            "probe_id": "obs-7287",
            "similarity": 0.965,
            "task_text": "Find Maude et al. 2014 NEJM paper showing chimeric antigen receptor (CAR) T-cell therapy producing sustained remissions in children and young adults with B-cell acute lymphoblastic leukemia.",
            "adapted_input": "Find Maude et al. 2014 NEJM paper showing chimeric antigen receptor (CAR) T-cell therapy producing sustained remissions in children and young adults with B-cell acute lymphoblastic leukemia.",
            "score": 1,
            "redacted": null,
            "output_chars": 3857,
            "truncated": false,
            "created_at": "2026-05-23T21:38:38.417660Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "The tool successfully identified the exact paper requested. The first result in the list matches the | Exactly retrieved the target Maude et al. 2014 NEJM paper (PMID 25317870, DOI 10.1056/nejmoa1407222) | The tool returned the exact Maude et al. 2014 NEJM paper as the top result with correct title, autho",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool successfully identified the exact paper requested. The first result in the list matches the title, author (Maude SL et al.), year (2014), and DOI (10.1056/nejmoa1407222) of the canonical NEJM paper described in the ground truth.",
                    "score": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "Exactly retrieved the target Maude et al. 2014 NEJM paper (PMID 25317870, DOI 10.1056/nejmoa1407222) as the top result with correct title, authors, year, and identifiers. The additional results are relevant but not incorrect. No fabrication or emptiness issues.",
                    "score": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned the exact Maude et al. 2014 NEJM paper as the top result with correct title, authors, year, and identifiers (DOI, PMID) that match the ground truth, fulfilling all query requirements perfectly.",
                    "score": 1
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "The first result is the exact paper requested by the user, including the correct title, author, year, and DOI.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The first result is the exact paper requested by the user, including the correct title, author, year, and DOI.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The first result is exactly the requested Maude et al. 2014 NEJM paper on CAR T-cell therapy for sustained remissions in leukemia, directly answering the query intent.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The first result is the exact paper requested, and the other two are relevant articles by the same author on the same topic but not the specific NEJM publication.",
                    "label": "good",
                    "value": 0.75
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool provides citations to peer-reviewed medical journal articles from PubMed/Europe PMC, which are primary scientific sources.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides citations to peer-reviewed medical journal articles from PubMed/Europe PMC, which are primary scientific sources.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "All returned results are peer-reviewed papers from authoritative journals (NEJM, Cancer Journal, ASH Education Book), which are primary sources.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output lists search results that are peer-reviewed medical journal articles, which are primary sources.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool provides explicit source references including PMIDs, PMCIDs, and DOIs for the search results.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides explicit source references including PMIDs, PMCIDs, and DOIs for the search results.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output includes explicit source references such as PMID, PMCID, and DOI for each result, allowing a reader to locate the underlying papers.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output includes explicit citation markers like pmid, pmcid, and doi for the relevant paper, enabling readers to access the source directly.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool successfully returned a list of three relevant search results including the specific paper requested.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool successfully returned a list of three relevant search results including the specific paper requested.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned three search results, including the target paper, so output is non-empty.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool provided a non-empty JSON response with search results, which is usable output regardless of correctness.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find Maude et al. 2014 NEJM paper showing chimeric antigen receptor (CAR) T-cell therapy producing sustained remissions in children and young adults with B-cell acute lymphoblastic leukemia.\",\n  \"adapted_query\": \"AUTH:\\\"Maude\\\" PUB_YEAR:2014 CAR-T leukemia\",\n  \"provider\": \"Europe PMC\",\n  \"tool_kind\": \"life-science literature search (papers + preprints + OA full text)\",\n  \"total_results\": 3,\n  \"returned_results\": 3,\n  \"results\": [\n    {\n      \"id\": \"25317870\",\n      \"source\": \"MED\",\n      \"pmid\": \"25317870\",\n      \"pmcid\": \"PMC4267531\",\n      \"doi\": \"10.1056/nejmoa1407222\",\n      \"title\": \"Chimeric antigen receptor T cells for sustained remissions in leukemia.\",\n      \"authors\": \"Maude SL, Frey N, Shaw PA, Aplenc R, Barrett DM, Bunin NJ, Chew A, Gonzalez VE, Zheng Z, Lacey SF, Mahnke YD, Melenhorst JJ, Rheingold SR, Shen A, Teachey DT, Levine BL, June CH, Porter DL, Grupp SA.\",\n      \"journal\": null,\n      \"publication_year\": \"2014\",\n      \"publication_type\": null,\n      \"cited_by_count\": 4154,\n      \"is_open_access\": false,\n      \"abstract\": \"<h4>Background</h4>Relapsed acute lymphoblastic leukemia (ALL) is difficult to treat despite the availability of aggressive therapies. Chimeric antigen receptor-modified T cells targeting CD19 may overcome many limitations of conventional therapies and induce remission in patients with refractory disease.<h4>Methods</h4>We in …[truncated]"
          },
          {
            "probe_id": "obs-32816",
            "similarity": 0.964,
            "task_text": "Find the 2026 Phytomedicine paper by Meng et al. showing obacunone attenuates cholestatic liver disease via PPARα activation and gut microbiota remodeling. Give me the PubMed ID.",
            "adapted_input": "Find the 2026 Phytomedicine paper by Meng et al. showing obacunone attenuates cholestatic liver disease via PPARα activation and gut microbiota remodeling. Give me the PubMed ID.",
            "score": 1,
            "redacted": null,
            "output_chars": 1584,
            "truncated": false,
            "created_at": "2026-08-29T11:55:26.244923Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "Deterministic check — matched 1/1 required string(s).",
                "panel": null
              }
            ],
            "raw_output": "{\n  \"query\": \"Find the 2026 Phytomedicine paper by Meng et al. showing obacunone attenuates cholestatic liver disease via PPAR\\u03b1 activation and gut microbiota remodeling. Give me the PubMed ID.\",\n  \"adapted_query\": \"AUTH:\\\"Meng\\\" PUB_YEAR:2026 obacunone cholestatic PPAR\\u03b1\",\n  \"provider\": \"Europe PMC\",\n  \"tool_kind\": \"life-science literature search (papers + preprints + OA full text)\",\n  \"total_results\": 1,\n  \"returned_results\": 1,\n  \"results\": [\n    {\n      \"id\": \"42551234\",\n      \"source\": \"MED\",\n      \"pmid\": \"42551234\",\n      \"pmcid\": null,\n      \"doi\": \"10.1016/j.phymed.2026.158648\",\n      \"title\": \"Obacunone attenuates Cholestatic liver disease via PPAR\\u03b1 activation and gut microbiota remodeling.\",\n      \"authors\": \"Meng X, Zeng C, Deng H, Jiang S, Du X, Xiao Y, Liu C.\",\n      \"journal\": null,\n      \"publication_year\": \"2026\",\n      \"publication_type\": null,\n      \"cited_by_count\": 0,\n      \"is_open_access\": false,\n      \"abstract\": \"<h4>Background</h4>Cholestatic liver disease (CLD) comprises a collection of disorders marked by impaired bile formation or flow, which can progress to fibrosis, cirrhosis, and liver failure if left untreated. Although there have been significant advances in understanding its pathogenesis, effective pharmacotherapies are still limited; ursodeoxycholic acid (UDCA), the first-line treatment, exhibits an incomplete response in approxi …[truncated]"
          }
        ]
      },
      "evidence_teaser": {
        "task_text": "Find scientific literature on graphene field-effect transistors for biosensing applications.",
        "verdict": "pass",
        "score": 0.733,
        "similarity": 0.968,
        "n_real": 91
      }
    }
  ],
  "decidable": false,
  "decide_margin": 0.0356,
  "not_checked": [],
  "flags": {
    "short_circuit": false,
    "digest_skipped": false,
    "digest_applied": false,
    "excluded": {
      "count": 27,
      "facets": [
        "no_machine_harm"
      ],
      "tool_ids": [
        "abuseipdb_api",
        "anthropic_memory_server",
        "antv_mcp_server_chart",
        "api_data_gov",
        "applescript_mcp",
        "browserbase_mcp",
        "chroma_mcp",
        "chrome_devtools_mcp",
        "desktop_commander",
        "dify",
        "docling",
        "easypost",
        "excel_mcp_server",
        "git_reference_server",
        "gnews",
        "neo4j_memory_mcp",
        "newsapi_ai",
        "openapi_mcp_server",
        "playwright_mcp",
        "postgres_mcp_pro",
        "semgrep_mcp",
        "skyvern",
        "telegram_bot_api",
        "tmdb_api",
        "trello",
        "usda_fooddata_central",
        "windows_mcp"
      ]
    },
    "verdict": "interpose"
  },
  "disclaimer": "Scores are advisory, not guarantees. Bands reflect observation age, not certainty of outcome; consequential decisions need human review.",
  "calling": {
    "tool_id": "tavily_search",
    "coordinator_class": false,
    "executable": true,
    "endpoint": {
      "base_url": "https://api.tavily.com",
      "api_type": "rest"
    },
    "adapter": {
      "type": "llm"
    },
    "auth": {
      "method": "api_key",
      "env_var": "TAVILY_API_KEY",
      "connected": false
    },
    "summary": {
      "usability": "connect_key",
      "auth_method": "api_key",
      "api_type": "rest",
      "connected": false,
      "free": false,
      "how": "connect a key → app.tavily.com/home",
      "signup_url": "https://app.tavily.com/home"
    },
    "connect": {
      "tool_id": "tavily_search",
      "name": "Tavily Search API",
      "auth_method": "api_key",
      "signup_url": "https://app.tavily.com/home",
      "instructions": "  1. Create a Tavily account — it comes with free monthly credits.\n  2. Open the API Keys section of the dashboard.\n  3. Create a key and copy it.",
      "methods": [
        {
          "auth_method": "api_key",
          "label": "Tavily API key",
          "signup_url": "https://app.tavily.com/home",
          "instructions": [
            "Create a Tavily account — it comes with free monthly credits.",
            "Open the API Keys section of the dashboard.",
            "Create a key and copy it."
          ],
          "fields": [
            {
              "key": "TAVILY_API_KEY",
              "label": "Tavily API key",
              "secret": true,
              "required": true,
              "help": "Dashboard → API Keys → Create"
            }
          ]
        }
      ],
      "fields": [
        {
          "key": "TAVILY_API_KEY",
          "label": "Tavily API key",
          "secret": true,
          "required": true,
          "help": "Dashboard → API Keys → Create"
        }
      ],
      "source": "evaluator",
      "connect_via": {
        "surface": "POST /credentials/connect",
        "method": "Tavily API key",
        "field_key": "TAVILY_API_KEY",
        "payload": {
          "tool_id": "tavily_search",
          "api_key": "<paste your key here>"
        },
        "curl": "curl -s https://hyperroute.io/credentials/connect -H 'content-type: application/json' -d '{\"tool_id\":\"tavily_search\",\"api_key\":\"<YOUR_KEY>\"}'"
      }
    }
  },
  "facet_form": {
    "reason": "these unset facets diverge across the shortlist and would reorder it; set any to refine with the full facet set, or proceed with the current best pick",
    "decidable": false,
    "decide_margin": 0.0356,
    "shortlist": [
      "tavily_search",
      "sonar_deep_research",
      "pubmed",
      "crossref+references"
    ],
    "fields": [
      {
        "name": "format",
        "optional": true,
        "default": "not applied — Pass 2 ranks with the engine's Kano defaults",
        "spread": 0.7734,
        "divergence_over_shortlist": {
          "tavily_search": 0.991,
          "sonar_deep_research": 0.217,
          "pubmed": 0.974,
          "crossref+references": 0.5
        },
        "note": "leave blank to accept the default; or set kano/weight/threshold to apply it"
      },
      {
        "name": "output_was_returned",
        "optional": true,
        "default": "not applied — Pass 2 ranks with the engine's Kano defaults",
        "spread": 0.4932,
        "divergence_over_shortlist": {
          "tavily_search": 0.993,
          "sonar_deep_research": 0.917,
          "pubmed": 0.93,
          "crossref+references": 0.5
        },
        "note": "leave blank to accept the default; or set kano/weight/threshold to apply it"
      },
      {
        "name": "snippet_quality",
        "optional": true,
        "default": "not applied — Pass 2 ranks with the engine's Kano defaults",
        "spread": 0.4804,
        "divergence_over_shortlist": {
          "tavily_search": 0.98,
          "sonar_deep_research": 0.885,
          "pubmed": 0.811,
          "crossref+references": 0.5
        },
        "note": "leave blank to accept the default; or set kano/weight/threshold to apply it"
      }
    ]
  },
  "facet_state": {
    "active": [
      {
        "name": "no_machine_harm",
        "kano": "must_be",
        "weight": 2,
        "threshold": 0.5,
        "scope": "global",
        "kind": "compliance",
        "source": "default"
      },
      {
        "name": "price",
        "kano": "performance",
        "weight": 0.3,
        "threshold": 0.5,
        "scope": "global",
        "kind": "price",
        "source": "default"
      },
      {
        "name": "capability",
        "kano": "must_be",
        "weight": 1,
        "threshold": 0.5,
        "scope": "tool",
        "kind": "quality",
        "source": "default"
      }
    ],
    "query_specific_available": [
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
    "hint": "`active` is what this route ranked under (source: default=bundle, stored=your standing account layer, request=this call). Supply any `query_specific_available` facet in `facets` and re-call recommend to refine THIS task; persist a standing constraint/preference (e.g. gdpr_compliant, price) via set_preferences so it applies automatically on every future call without re-sending it."
  },
  "facet_options": [
    {
      "name": "ccpa_compliant",
      "label": "CCPA/CPRA compliant",
      "description": "Documented California Consumer Privacy Act / CPRA compliance.",
      "text_source": "authored",
      "scope": "global",
      "kind": "compliance",
      "spread": 1,
      "divergent": false,
      "on": false,
      "kano": "must_be",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 1,
        "sonar_deep_research": 1,
        "pubmed": 0,
        "crossref+references": 0
      }
    },
    {
      "name": "code_due_diligence",
      "label": "Source code reviewed",
      "description": "Stage 2 (specs/30-probing.md): for a tool whose code we run locally (MCP server, package, executable, CLI), the actual on-disk artifact we execute was statically reviewed — read-only, before any execution — and shows no obvious malicious or high-risk behavior: no covert network exfiltration, credential/secret harvesting, install- or load-time code execution, shell-out, obfuscation, or provenance/typosquat mismatch. Mark `na` for hosted APIs whose code we never run.",
      "text_source": "authored",
      "scope": "global",
      "kind": "compliance",
      "spread": 0,
      "divergent": false,
      "on": false,
      "kano": "must_be",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 0,
        "sonar_deep_research": 0,
        "pubmed": 0,
        "crossref+references": 0
      }
    },
    {
      "name": "data_deletion",
      "label": "Honors deletion",
      "description": "Provides a documented way to delete user data on request.",
      "text_source": "authored",
      "scope": "global",
      "kind": "compliance",
      "spread": 1,
      "divergent": false,
      "on": false,
      "kano": "must_be",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 1,
        "sonar_deep_research": 1,
        "pubmed": 0,
        "crossref+references": 1
      }
    },
    {
      "name": "data_residency",
      "label": "Data residency control",
      "description": "Offers data-residency / region control (e.g. EU-only processing) or clearly documents where data is processed and stored.",
      "text_source": "authored",
      "scope": "global",
      "kind": "compliance",
      "spread": 1,
      "divergent": false,
      "on": false,
      "kano": "must_be",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 1,
        "sonar_deep_research": 0,
        "pubmed": 1,
        "crossref+references": 1
      }
    },
    {
      "name": "data_retention_limited",
      "label": "Limited retention",
      "description": "Enforces a documented data-retention limit, or offers a zero/short-retention option for user inputs.",
      "text_source": "authored",
      "scope": "global",
      "kind": "compliance",
      "spread": 1,
      "divergent": false,
      "on": false,
      "kano": "must_be",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 1,
        "sonar_deep_research": 1,
        "pubmed": 1,
        "crossref+references": 0
      }
    },
    {
      "name": "dpa_available",
      "label": "DPA available",
      "description": "Offers a Data Processing Agreement (DPA) to customers.",
      "text_source": "authored",
      "scope": "global",
      "kind": "compliance",
      "spread": 1,
      "divergent": false,
      "on": false,
      "kano": "attractive",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 0,
        "sonar_deep_research": 1
      }
    },
    {
      "name": "encrypted_at_rest",
      "label": "Encrypted at rest",
      "description": "Stored user data is encrypted at rest.",
      "text_source": "authored",
      "scope": "global",
      "kind": "compliance",
      "spread": 1,
      "divergent": false,
      "on": false,
      "kano": "must_be",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 1,
        "sonar_deep_research": 1,
        "pubmed": 0,
        "crossref+references": 0
      }
    },
    {
      "name": "encrypted_in_transit",
      "label": "Encrypted in transit",
      "description": "Data and credentials are sent over TLS; credentials are not exposed in URLs, query strings, or logs.",
      "text_source": "authored",
      "scope": "global",
      "kind": "compliance",
      "spread": 0,
      "divergent": false,
      "on": false,
      "kano": "must_be",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 1,
        "sonar_deep_research": 1,
        "pubmed": 1,
        "crossref+references": 1
      }
    },
    {
      "name": "gdpr_compliant",
      "label": "GDPR compliant",
      "description": "Documented GDPR compliance — lawful basis and EU data-protection handling.",
      "text_source": "authored",
      "scope": "global",
      "kind": "compliance",
      "spread": 1,
      "divergent": false,
      "on": false,
      "kano": "must_be",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 1,
        "sonar_deep_research": 1,
        "pubmed": 0,
        "crossref+references": 1
      }
    },
    {
      "name": "hipaa_compliant",
      "label": "HIPAA compliant",
      "description": "Supports HIPAA compliance for protected health information (BAA available). Mark `na` for tools that never touch health data.",
      "text_source": "authored",
      "scope": "global",
      "kind": "compliance",
      "spread": null,
      "divergent": false,
      "on": false,
      "kano": "must_be",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "sonar_deep_research": 1
      }
    },
    {
      "name": "iso_27001",
      "label": "ISO 27001",
      "description": "Holds a current ISO/IEC 27001 certification.",
      "text_source": "authored",
      "scope": "global",
      "kind": "compliance",
      "spread": 0,
      "divergent": false,
      "on": false,
      "kano": "attractive",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 0,
        "sonar_deep_research": 0,
        "pubmed": 0,
        "crossref+references": 0
      }
    },
    {
      "name": "least_privilege_credentials",
      "label": "Scoped credentials",
      "description": "API credentials are scope-limited and revocable (least privilege); not a single all-powerful static secret.",
      "text_source": "authored",
      "scope": "global",
      "kind": "compliance",
      "spread": 0,
      "divergent": false,
      "on": false,
      "kano": "must_be",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 1,
        "sonar_deep_research": 1
      }
    },
    {
      "name": "no_data_exfiltration",
      "label": "Won't leak your data",
      "description": "Does not send the user's documents/inputs to third parties beyond what is strictly required to serve the request.",
      "text_source": "authored",
      "scope": "global",
      "kind": "compliance",
      "spread": 0,
      "divergent": false,
      "on": false,
      "kano": "must_be",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 1,
        "sonar_deep_research": 1,
        "pubmed": 1,
        "crossref+references": 1
      }
    },
    {
      "name": "no_machine_harm",
      "label": "Won't harm your machine",
      "description": "Does not run untrusted code on the host, instruct the user to install suspicious binaries / zip files, or otherwise endanger the local machine.",
      "text_source": "authored",
      "scope": "global",
      "kind": "compliance",
      "spread": 0,
      "divergent": false,
      "on": true,
      "kano": "must_be",
      "weight": 2,
      "default_weight": 2,
      "threshold": 0.5,
      "values": {
        "tavily_search": 1,
        "sonar_deep_research": 1,
        "pubmed": 1,
        "crossref+references": 1
      }
    },
    {
      "name": "no_train_on_data",
      "label": "Won't train on your data",
      "description": "Does not train models on, or otherwise repurpose, user-submitted data.",
      "text_source": "authored",
      "scope": "global",
      "kind": "compliance",
      "spread": 0,
      "divergent": false,
      "on": false,
      "kano": "must_be",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 1,
        "sonar_deep_research": 1,
        "pubmed": 1,
        "crossref+references": 1
      }
    },
    {
      "name": "price",
      "label": "Price",
      "description": "How much it costs to serve your request.",
      "text_source": "authored",
      "scope": "global",
      "kind": "price",
      "spread": null,
      "divergent": false,
      "on": true,
      "kano": "performance",
      "weight": 0.3,
      "default_weight": 0.3,
      "threshold": 0.5,
      "values": {}
    },
    {
      "name": "rate_headroom",
      "label": "Rate capacity",
      "description": "Whether the tool's rate limits can handle your expected volume.",
      "text_source": "authored",
      "scope": "global",
      "kind": "capacity",
      "spread": 0,
      "divergent": false,
      "on": false,
      "kano": "performance",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 1,
        "sonar_deep_research": 1,
        "pubmed": 1,
        "crossref+references": 1
      }
    },
    {
      "name": "reliability",
      "label": "Reliability",
      "description": "How consistently the tool is up and returns a result.",
      "text_source": "authored",
      "scope": "global",
      "kind": "live",
      "spread": 0.0206,
      "divergent": false,
      "on": false,
      "kano": "must_be",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 0.997,
        "sonar_deep_research": 0.993,
        "pubmed": 0.993,
        "crossref+references": 0.977
      }
    },
    {
      "name": "safe_distribution",
      "label": "Trusted distribution",
      "description": "Obtained/installed from a verified, reputable source (official hosted API, signed package, known registry); no suspicious downloads.",
      "text_source": "authored",
      "scope": "global",
      "kind": "compliance",
      "spread": 0,
      "divergent": false,
      "on": false,
      "kano": "must_be",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 1,
        "sonar_deep_research": 1,
        "pubmed": 1,
        "crossref+references": 1
      }
    },
    {
      "name": "soc2",
      "label": "SOC 2",
      "description": "Holds a current SOC 2 (Type II preferred) report from an independent auditor.",
      "text_source": "authored",
      "scope": "global",
      "kind": "compliance",
      "spread": 1,
      "divergent": false,
      "on": false,
      "kano": "attractive",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 1,
        "sonar_deep_research": 1,
        "pubmed": 0,
        "crossref+references": 0
      }
    },
    {
      "name": "subprocessors_disclosed",
      "label": "Subprocessors disclosed",
      "description": "Publicly discloses its sub-processors / fourth parties that may handle user data.",
      "text_source": "authored",
      "scope": "global",
      "kind": "compliance",
      "spread": 0,
      "divergent": false,
      "on": false,
      "kano": "attractive",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 1,
        "sonar_deep_research": 1,
        "pubmed": 1,
        "crossref+references": 1
      }
    },
    {
      "name": "third_party_pentest",
      "label": "Third-party pentest",
      "description": "Has a recent independent penetration test on record.",
      "text_source": "authored",
      "scope": "global",
      "kind": "compliance",
      "spread": 1,
      "divergent": false,
      "on": false,
      "kano": "attractive",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 1,
        "sonar_deep_research": 1,
        "pubmed": 0,
        "crossref+references": 0
      }
    },
    {
      "name": "vuln_disclosure",
      "label": "Vulnerability disclosure program",
      "description": "Has a documented vulnerability-disclosure / responsible-disclosure process and a security contact; the project's public issue tracker and security advisories show no unresolved or actively-exploited security reports; no known unremediated breaches.",
      "text_source": "authored",
      "scope": "global",
      "kind": "compliance",
      "spread": 1,
      "divergent": false,
      "on": false,
      "kano": "attractive",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 1,
        "sonar_deep_research": 1,
        "pubmed": 1,
        "crossref+references": 0
      }
    },
    {
      "name": "citation_existence",
      "label": "Real citations",
      "description": "Are the sources it cites real and reachable, not made up or dead?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.3437,
      "divergent": true,
      "on": false,
      "kano": "attractive",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 0.944,
        "sonar_deep_research": 0.6,
        "pubmed": 0.636,
        "crossref+references": 0.6
      }
    },
    {
      "name": "citation_support",
      "label": "Citations back the claim",
      "description": "Do the cited sources actually contain the evidence the answer relies on?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.2411,
      "divergent": true,
      "on": false,
      "kano": "performance",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 0.829,
        "sonar_deep_research": 0.587,
        "pubmed": 0.587,
        "crossref+references": 0.587
      }
    },
    {
      "name": "cited_references",
      "label": "Lists the works it cites",
      "description": "Does it return the record's own cited references, not just a link per result?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.3333,
      "divergent": true,
      "on": false,
      "kano": "attractive",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 0.5,
        "sonar_deep_research": 0.5,
        "pubmed": 0.5,
        "crossref+references": 0.833
      }
    },
    {
      "name": "completeness",
      "label": "Complete coverage",
      "description": "Does the result cover the topic's main angles, not just one?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.4271,
      "divergent": true,
      "on": false,
      "kano": "performance",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 0.46,
        "sonar_deep_research": 0.708,
        "pubmed": 0.281,
        "crossref+references": 0.562
      }
    },
    {
      "name": "explanation_quality",
      "label": "Clear reasoning",
      "description": "Does it explain its answer in a way you can check against the sources?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.1764,
      "divergent": true,
      "on": false,
      "kano": "performance",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 0.643,
        "sonar_deep_research": 0.6,
        "pubmed": 0.467,
        "crossref+references": 0.467
      }
    },
    {
      "name": "format",
      "label": "Structured output",
      "description": "Is the response cleanly structured so software can read it reliably?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.7734,
      "divergent": true,
      "on": false,
      "kano": "attractive",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 0.991,
        "sonar_deep_research": 0.217,
        "pubmed": 0.974,
        "crossref+references": 0.5
      }
    },
    {
      "name": "freshness",
      "label": "Up to date",
      "description": "Is the answer based on current information rather than stale data?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.3401,
      "divergent": true,
      "on": false,
      "kano": "performance",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 0.965,
        "sonar_deep_research": 0.942,
        "pubmed": 0.95,
        "crossref+references": 0.625
      }
    },
    {
      "name": "output_was_returned",
      "label": "Returned an answer",
      "description": "Did the tool return any usable result at all?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.4932,
      "divergent": true,
      "on": false,
      "kano": "must_be",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 0.993,
        "sonar_deep_research": 0.917,
        "pubmed": 0.93,
        "crossref+references": 0.5
      }
    },
    {
      "name": "references_present",
      "label": "Shows its sources",
      "description": "Does the output include links or references you can follow?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.3891,
      "divergent": true,
      "on": false,
      "kano": "attractive",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 0.989,
        "sonar_deep_research": 0.867,
        "pubmed": 0.864,
        "crossref+references": 0.6
      }
    },
    {
      "name": "relevance",
      "label": "Relevant results",
      "description": "Are the most useful results surfaced first?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.3917,
      "divergent": true,
      "on": false,
      "kano": "performance",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 0.892,
        "sonar_deep_research": 0.836,
        "pubmed": 0.719,
        "crossref+references": 0.5
      }
    },
    {
      "name": "snippet_quality",
      "label": "Useful previews",
      "description": "Are the result summaries informative enough to judge without clicking through?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.4804,
      "divergent": true,
      "on": false,
      "kano": "attractive",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 0.98,
        "sonar_deep_research": 0.885,
        "pubmed": 0.811,
        "crossref+references": 0.5
      }
    },
    {
      "name": "source_quality",
      "label": "Trustworthy sources",
      "description": "Does it cite authoritative sources over low-quality ones?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.3375,
      "divergent": true,
      "on": false,
      "kano": "performance",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "tavily_search": 0.833,
        "sonar_deep_research": 0.877,
        "pubmed": 0.968,
        "crossref+references": 0.63
      }
    }
  ]
}
```
