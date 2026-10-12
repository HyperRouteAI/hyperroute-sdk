# Default recommendation

[`recommend.py`](../recommend.py) requests the default lean response and prints every returned field.

```sh
python examples/python/recommend.py
```

Example output:

```json
{
  "session_id": "s-9e6a17c8ecd141c0",
  "kind": "ranked",
  "status": "needs_facets",
  "provisional": true,
  "best": {
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
    "reason": "highest-ranked: capability 0.98; meets the required capability bar; effective $0.0000/query.",
    "capability": 0.9809,
    "band": 0.0172,
    "cap_lcb": 0.9637,
    "rank": 0.9846,
    "price": {
      "amount": 0.0,
      "per_query_usd": 0.0,
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
          "effective_usd": 0.0,
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
  "runner_ups": [
    {
      "tool_id": "kagi_search",
      "name": "Kagi Search API",
      "variant": null,
      "capabilities": [
        "web_search",
        "realtime"
      ],
      "description": "Premium, ad-free search engine with independent index. Strong anti-SEO-spam filtering and high-quality results.",
      "kind": "external_tool",
      "endpoint": {
        "api_type": "rest",
        "base_url": "https://kagi.com",
        "status_url": "https://kagi.com"
      },
      "reason": "lower capability (0.94 vs 0.98); pricier ($0.0120 vs $0.0000/query).",
      "capability": 0.9402,
      "band": 0.1177,
      "cap_lcb": 0.8226,
      "rank": 0.9232,
      "price": {
        "amount": 0.012,
        "per_query_usd": 0.012,
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
            "plan_group": "kagi_search_api",
            "effective_usd": 0.012,
            "held": false,
            "currency": "USD",
            "confidence": "high",
            "overridden": false
          }
        ]
      },
      "calling": {
        "tool_id": "kagi_search",
        "coordinator_class": false,
        "executable": true,
        "endpoint": {
          "base_url": "https://kagi.com",
          "api_type": "rest"
        },
        "adapter": {
          "type": "llm"
        },
        "auth": {
          "method": "api_key",
          "env_var": "KAGI_API_KEY",
          "connected": false
        },
        "summary": {
          "usability": "connect_key",
          "auth_method": "api_key",
          "api_type": "rest",
          "connected": false,
          "free": false,
          "how": "connect a key → kagi.com/signup",
          "signup_url": "https://kagi.com/signup"
        },
        "connect": {
          "tool_id": "kagi_search",
          "name": "Kagi Search API",
          "auth_method": "api_key",
          "signup_url": "https://kagi.com/signup",
          "instructions": "  1. Create a Kagi account and subscribe to a plan.\n  2. Open Settings → Advanced → API portal.\n  3. Add API credit, then generate a Search API token.\n  4. Copy the token.",
          "methods": [
            {
              "auth_method": "api_key",
              "label": "Kagi Search API token",
              "signup_url": "https://kagi.com/signup",
              "instructions": [
                "Create a Kagi account and subscribe to a plan.",
                "Open Settings → Advanced → API portal.",
                "Add API credit, then generate a Search API token.",
                "Copy the token."
              ],
              "fields": [
                {
                  "key": "KAGI_API_KEY",
                  "label": "Kagi Search API token",
                  "secret": true,
                  "required": true,
                  "help": "Settings → Advanced → API → Generate API Token"
                }
              ]
            }
          ],
          "fields": [
            {
              "key": "KAGI_API_KEY",
              "label": "Kagi Search API token",
              "secret": true,
              "required": true,
              "help": "Settings → Advanced → API → Generate API Token"
            }
          ],
          "source": "evaluator",
          "connect_via": {
            "surface": "POST /credentials/connect",
            "method": "Kagi Search API token",
            "field_key": "KAGI_API_KEY",
            "payload": {
              "tool_id": "kagi_search",
              "api_key": "<paste your key here>"
            },
            "curl": "curl -s https://hyperroute.io/credentials/connect -H 'content-type: application/json' -d '{\"tool_id\":\"kagi_search\",\"api_key\":\"<YOUR_KEY>\"}'"
          }
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
      "capability": 0.8523,
      "band": 0.1253,
      "cap_lcb": 0.727,
      "rank": 0.8842,
      "price": {
        "amount": 0.0,
        "per_query_usd": 0.0,
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
            "effective_usd": 0.0,
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
      "tool_id": "ddg_search",
      "name": "DuckDuckGo Search (MCP)",
      "variant": null,
      "capabilities": [
        "web_search",
        "realtime"
      ],
      "description": "Privacy-focused web search via self-hosted MCP server. Scrapes DuckDuckGo HTML results. No API key required.",
      "kind": "external_tool",
      "endpoint": {
        "api_type": "mcp_stdio",
        "base_url": "https://duckduckgo.com",
        "status_url": "https://duckduckgo.com"
      },
      "reason": "lower capability (0.91 vs 0.98).",
      "capability": 0.9056,
      "band": 0.192,
      "cap_lcb": 0.7136,
      "rank": 0.8785,
      "price": {
        "amount": 0.0,
        "per_query_usd": 0.0,
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
            "effective_usd": 0.0,
            "held": false,
            "currency": "USD",
            "confidence": "high",
            "overridden": false
          }
        ]
      },
      "calling": {
        "tool_id": "ddg_search",
        "coordinator_class": false,
        "executable": false,
        "endpoint": {
          "base_url": "https://duckduckgo.com",
          "api_type": "mcp_stdio"
        },
        "adapter": {
          "type": "llm"
        },
        "auth": {
          "method": "none"
        },
        "summary": {
          "usability": "add_mcp",
          "auth_method": "none",
          "api_type": "mcp_stdio",
          "connected": false,
          "free": true,
          "how": "free · one-time: add the DuckDuckGo Search (MCP) MCP server (duckduckgo.com)",
          "signup_url": "https://github.com/nickclyde/duckduckgo-mcp-server"
        },
        "mcp_install": {
          "transport": "stdio",
          "command": "uvx",
          "args": [
            "duckduckgo-mcp-server"
          ],
          "package": {
            "registry": "pypi",
            "name": "duckduckgo-mcp-server",
            "version": null
          },
          "server_name": "ddg",
          "tools": [
            "search",
            "fetch_content"
          ],
          "env": [],
          "docs_url": "https://github.com/nickclyde/duckduckgo-mcp-server",
          "instructions": [
            "Add the DuckDuckGo MCP server: claude mcp add ddg -- uvx duckduckgo-mcp-server",
            "Restart the coordinator so the server connects.",
            "Re-run the task — the search tool is now available."
          ]
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
      "capability": 0.8614,
      "band": 0.2385,
      "cap_lcb": 0.6229,
      "rank": 0.84,
      "price": {
        "amount": 0.0,
        "per_query_usd": 0.0,
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
            "effective_usd": 0.0,
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
      "reason": "lower capability (0.83 vs 0.98); pricier ($0.0080 vs $0.0000/query).",
      "capability": 0.8332,
      "band": 0.2892,
      "cap_lcb": 0.544,
      "rank": 0.8055,
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
      "description": "Composite deep-research agent on Perplexity's Agent API, `medium` preset (their rename of deep-research; model pinned to openai/gpt-6-luna as a preset override, served model checked per response). Issues multiple web searches and page fetches per query, cross-checks claims, and synthesises a long-form answer with inline citations. Shares the PERPLEXITY_API_KEY credential with perplexity_sonar.",
      "kind": "external_tool",
      "endpoint": {
        "api_type": "rest",
        "base_url": "https://api.perplexity.ai",
        "status_url": "https://status.perplexity.com"
      },
      "reason": "lower capability (0.78 vs 0.98); pricier ($0.0200 vs $0.0000/query).",
      "capability": 0.7795,
      "band": 0.2329,
      "cap_lcb": 0.5466,
      "rank": 0.8051,
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
      "reason": "falls short of the required capability bar for this task.",
      "capability": 0.753,
      "band": 0.4113,
      "cap_lcb": 0.3417,
      "rank": 0.5188,
      "price": {
        "amount": 0.0,
        "per_query_usd": 0.0,
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
            "effective_usd": 0.0,
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
    },
    {
      "tool_id": "arxiv",
      "name": "arXiv API",
      "variant": null,
      "capabilities": [
        "paper_search",
        "academic",
        "references",
        "abstracts"
      ],
      "description": "Open-access preprint repository search. STEM-heavy: physics, mathematics, computer science, quantitative biology, statistics, electrical engineering. Returns title, authors, abstract, publication date, and the arXiv ID / URL per paper.",
      "kind": "external_tool",
      "endpoint": {
        "api_type": "rest",
        "base_url": "http://export.arxiv.org",
        "status_url": "https://status.arxiv.org"
      },
      "reason": "falls short of the required capability bar for this task.",
      "capability": 0.5031,
      "band": 0.3505,
      "cap_lcb": 0.1526,
      "rank": 0.2212,
      "price": {
        "amount": 0.0,
        "per_query_usd": 0.0,
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
            "effective_usd": 0.0,
            "held": false,
            "currency": "USD",
            "confidence": "high",
            "overridden": false
          }
        ]
      },
      "calling": {
        "tool_id": "arxiv",
        "coordinator_class": false,
        "executable": true,
        "endpoint": {
          "base_url": "http://export.arxiv.org",
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
      "tool_id": "brave_search",
      "name": "Brave Search API",
      "variant": null,
      "capabilities": [
        "web_search",
        "realtime"
      ],
      "description": "Privacy-focused web search API with structured results, snippets, and news. Independent web index.",
      "kind": "external_tool",
      "endpoint": {
        "api_type": "rest",
        "base_url": "https://api.search.brave.com",
        "status_url": "https://search.brave.com"
      },
      "reason": "falls short of the required capability bar for this task.",
      "capability": 0.5655,
      "band": 0.4132,
      "cap_lcb": 0.1523,
      "rank": 0.2205,
      "price": {
        "amount": 0.005,
        "per_query_usd": 0.005,
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
            "plan_group": "brave_search",
            "effective_usd": 0.005,
            "held": false,
            "currency": "USD",
            "confidence": "high",
            "overridden": false
          }
        ]
      },
      "calling": {
        "tool_id": "brave_search",
        "coordinator_class": false,
        "executable": true,
        "endpoint": {
          "base_url": "https://api.search.brave.com",
          "api_type": "rest"
        },
        "adapter": {
          "type": "llm"
        },
        "auth": {
          "method": "api_key",
          "env_var": "BRAVE_API_KEY",
          "connected": false
        },
        "summary": {
          "usability": "connect_key",
          "auth_method": "api_key",
          "api_type": "rest",
          "connected": false,
          "free": false,
          "how": "connect a key → api-dashboard.search.brave.com/register",
          "signup_url": "https://api-dashboard.search.brave.com/register"
        },
        "connect": {
          "tool_id": "brave_search",
          "name": "Brave Search API",
          "auth_method": "api_key",
          "signup_url": "https://api-dashboard.search.brave.com/register",
          "instructions": "  1. Create a Brave Search account.\n  2. Subscribe to a plan — the free tier is enough to start.\n  3. Open the API Keys page in the dashboard.\n  4. Generate a key and copy it.",
          "methods": [
            {
              "auth_method": "api_key",
              "label": "Brave Search API key",
              "signup_url": "https://api-dashboard.search.brave.com/register",
              "instructions": [
                "Create a Brave Search account.",
                "Subscribe to a plan — the free tier is enough to start.",
                "Open the API Keys page in the dashboard.",
                "Generate a key and copy it."
              ],
              "fields": [
                {
                  "key": "BRAVE_API_KEY",
                  "label": "Brave Search API key",
                  "secret": true,
                  "required": true,
                  "help": "Dashboard → API Keys → Add API key"
                }
              ]
            }
          ],
          "fields": [
            {
              "key": "BRAVE_API_KEY",
              "label": "Brave Search API key",
              "secret": true,
              "required": true,
              "help": "Dashboard → API Keys → Add API key"
            }
          ],
          "source": "evaluator",
          "connect_via": {
            "surface": "POST /credentials/connect",
            "method": "Brave Search API key",
            "field_key": "BRAVE_API_KEY",
            "payload": {
              "tool_id": "brave_search",
              "api_key": "<paste your key here>"
            },
            "curl": "curl -s https://hyperroute.io/credentials/connect -H 'content-type: application/json' -d '{\"tool_id\":\"brave_search\",\"api_key\":\"<YOUR_KEY>\"}'"
          }
        }
      }
    }
  ],
  "decidable": false,
  "decide_margin": 0.0448,
  "not_checked": [],
  "flags": {
    "short_circuit": false,
    "digest_skipped": false,
    "digest_applied": false,
    "excluded": {
      "count": 15,
      "facets": [
        "no_machine_harm"
      ],
      "tool_ids": [
        "anthropic_memory_server",
        "antv_mcp_server_chart",
        "applescript_mcp",
        "browserbase_mcp",
        "chrome_devtools_mcp",
        "desktop_commander",
        "docling",
        "excel_mcp_server",
        "git_reference_server",
        "gnews",
        "newsapi_ai",
        "openapi_mcp_server",
        "playwright_mcp",
        "semgrep_mcp",
        "windows_mcp"
      ]
    },
    "verdict": "interpose"
  },
  "disclaimer": "Scores are advisory, not guarantees. Bands reflect observation age, not certainty of outcome; consequential decisions need human review.",
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
  "facet_form": {
    "reason": "these unset facets diverge across the shortlist and would reorder it; set any to refine with the full facet set, or proceed with the current best pick",
    "decidable": false,
    "decide_margin": 0.0448,
    "shortlist": [
      "pubmed",
      "kagi_search",
      "unpaywall",
      "ddg_search"
    ],
    "fields": [
      {
        "name": "format",
        "optional": true,
        "default": "not applied — Pass 2 ranks with the engine's Kano defaults",
        "spread": 0.4932,
        "divergence_over_shortlist": {
          "pubmed": 0.5,
          "kagi_search": 0.988,
          "unpaywall": 0.979,
          "ddg_search": 0.993
        },
        "note": "leave blank to accept the default; or set kano/weight/threshold to apply it"
      },
      {
        "name": "snippet_quality",
        "optional": true,
        "default": "not applied — Pass 2 ranks with the engine's Kano defaults",
        "spread": 0.4726,
        "divergence_over_shortlist": {
          "pubmed": 0.5,
          "kagi_search": 0.959,
          "unpaywall": 0.824,
          "ddg_search": 0.973
        },
        "note": "leave blank to accept the default; or set kano/weight/threshold to apply it"
      },
      {
        "name": "explanation_quality",
        "optional": true,
        "default": "not applied — Pass 2 ranks with the engine's Kano defaults",
        "spread": 0.448,
        "divergence_over_shortlist": {
          "pubmed": 0.467,
          "kagi_search": 0.033,
          "unpaywall": 0.35,
          "ddg_search": 0.019
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
        "weight": 2.0,
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
        "weight": 1.0,
        "threshold": 0.5,
        "scope": "tool",
        "kind": "quality",
        "source": "default"
      }
    ],
    "query_specific_available": [
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
    "hint": "`active` is what this route ranked under (source: default=bundle, stored=your standing account layer, request=this call). Supply any `query_specific_available` facet in `facets` and re-call recommend to refine THIS task; persist a standing constraint/preference (e.g. gdpr_compliant, price) via set_preferences so it applies automatically on every future call without re-sending it."
  }
}
```
