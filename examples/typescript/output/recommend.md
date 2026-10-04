# Default recommendation

[`recommend.mjs`](../recommend.mjs) requests the default lean response and prints every returned field.

```sh
node examples/typescript/recommend.mjs
```

Example output:

```json
{
  "session_id": "s-c3235ccf3b244495",
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
  }
}
```
