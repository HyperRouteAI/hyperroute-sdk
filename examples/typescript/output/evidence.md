# Full recommendation

[`evidence.mjs`](../evidence.mjs) requests `detail="full"` with `evidence_k=3` and prints every returned field, including scores, facets, probe evidence, and judgments.

```sh
node examples/typescript/evidence.mjs
```

Example output:

```json
{
  "session_id": "s-13ab2e6e2bd24fc1",
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
        "raw": 0.9637,
        "contribution": 0.9492
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
      "n_real": 82,
      "n_near": 24,
      "near_mean": 0.827,
      "dist": [
        0.399,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        0.052,
        1,
        0.036,
        0.973,
        0.977,
        1,
        0.911,
        0,
        1,
        1,
        0.5,
        0.998
      ],
      "probes": [
        {
          "probe_id": "obs-42591",
          "similarity": 0.983,
          "task_text": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
          "adapted_input": "AlphaFold2 protein structure prediction Jumper 2021",
          "score": 0.399,
          "redacted": null,
          "output_chars": 6526,
          "truncated": false,
          "created_at": "2026-10-08T06:23:24.965500Z",
          "judges": [
            {
              "facet": "capability",
              "verdict": "partial",
              "score": 0.399,
              "rationale": "jev score 1.59/4 p=0.01/0.54/0.31/0.12/0.02 conf=0.48 | The tool returned AlphaFold-related 2021 Nature papers (the human proteome companion paper and the C | The canonical paper — Jumper et al., 'Highly accurate protein structure prediction with AlphaFold' (",
              "panel": [
                {
                  "model": "typesafe/jev-1.13.0",
                  "rationale": "jev score 1.59/4 p=0.01/0.54/0.31/0.12/0.02 conf=0.48",
                  "score": 0.398
                },
                {
                  "model": "deepseek/deepseek-v4.1-flash",
                  "rationale": "The tool returned AlphaFold-related 2021 Nature papers (the human proteome companion paper and the CASP14 paper), but missed the canonical target: Jumper et al., 'Highly accurate protein structure prediction with AlphaFold,' Nature 2021;596:583-589 (PMID 34265844). The requested paper is absent, and…",
                  "score": 0.3
                },
                {
                  "model": "z-ai/glm-5.3-flash",
                  "rationale": "The canonical paper — Jumper et al., 'Highly accurate protein structure prediction with AlphaFold' (Nature 2021, PMID 34211365) — does not appear as a top result. The top hit is the companion human-proteome paper (Tunyasuvunakool et al., PMID 34293799), which is closely related and often confused wi…",
                  "score": 0.5
                }
              ]
            },
            {
              "facet": "relevance",
              "verdict": "good",
              "score": 0.75,
              "rationale": "jev choice=good p{good=0.53, partial=0.24, excellent=0.17, poor=0.05, irrelevant=0.01} conf=0.41",
              "panel": [
                {
                  "model": "typesafe/jev-1.13.0",
                  "rationale": "jev choice=good p{good=0.53, partial=0.24, excellent=0.17, poor=0.05, irrelevant=0.01} conf=0.41",
                  "label": "good",
                  "value": 0.75
                },
                {
                  "model": "deepseek/deepseek-v4.1-flash",
                  "rationale": "The top results are all genuine 2021 Nature AlphaFold2 papers (Tunyasuvunakool et al. and the CASP14 paper), which are highly relevant and useful, but the specific Jumper et al. paper requested is not among them, so the targeting is imperfect.",
                  "label": "good",
                  "value": 0.75
                },
                {
                  "model": "z-ai/glm-5.3-flash",
                  "rationale": "The top results are highly relevant AlphaFold 2 papers from DeepMind in Nature 2021 (the human proteome paper and the CASP14 paper), but the exact target paper—Jumper et al., 'Highly accurate protein structure prediction with AlphaFold'—is not surfaced in the top results, making them useful but not …",
                  "label": "good",
                  "value": 0.75
                }
              ]
            },
            {
              "facet": "source_quality",
              "verdict": "primary",
              "score": 1,
              "rationale": "jev choice=primary p{primary=0.99, not_applicable=0.01, tertiary=0.00, reputable_secondary=0.00, low_quality=0.00} conf=0.99",
              "panel": [
                {
                  "model": "typesafe/jev-1.13.0",
                  "rationale": "jev choice=primary p{primary=0.99, not_applicable=0.01, tertiary=0.00, reputable_secondary=0.00, low_quality=0.00} conf=0.99",
                  "label": "primary",
                  "value": 1
                },
                {
                  "model": "deepseek/deepseek-v4.1-flash",
                  "rationale": "The tool returned peer-reviewed Nature journal articles indexed in PubMed, which are primary authoritative sources.",
                  "label": "primary",
                  "value": 1
                },
                {
                  "model": "z-ai/glm-5.3-flash",
                  "rationale": "The tool returns PubMed records of peer-reviewed Nature journal articles (e.g., the AlphaFold human proteome paper and CASP14 paper), which are primary, authoritative scientific sources.",
                  "label": "primary",
                  "value": 1
                }
              ]
            },
            {
              "facet": "references_present",
              "verdict": "present",
              "score": 1,
              "rationale": "jev choice=present p{present=1.00, absent=0.00, implied=0.00} conf=1.00",
              "panel": [
                {
                  "model": "typesafe/jev-1.13.0",
                  "rationale": "jev choice=present p{present=1.00, absent=0.00, implied=0.00} conf=1.00",
                  "label": "present",
                  "value": 1
                },
                {
                  "model": "deepseek/deepseek-v4.1-flash",
                  "rationale": "The output includes explicit PMIDs, DOIs, journal names, author lists, and PubMed URLs for each result, which a reader can follow back to the source material.",
                  "label": "present",
                  "value": 1
                },
                {
                  "model": "z-ai/glm-5.3-flash",
                  "rationale": "The output includes explicit source references such as PubMed URLs (e.g., https://pubmed.ncbi.nlm.nih.gov/34293799/), PMIDs, and DOIs (e.g., 10.1038/s41586-021-03828-1) that a reader can follow back to the underlying papers.",
                  "label": "present",
                  "value": 1
                }
              ]
            },
            {
              "facet": "output_was_returned",
              "verdict": "returned",
              "score": 1,
              "rationale": "jev choice=returned p{returned=1.00, empty=0.00} conf=1.00",
              "panel": [
                {
                  "model": "typesafe/jev-1.13.0",
                  "rationale": "jev choice=returned p{returned=1.00, empty=0.00} conf=1.00",
                  "label": "returned",
                  "value": 1
                },
                {
                  "model": "deepseek/deepseek-v4.1-flash",
                  "rationale": "The tool returned a non-empty PubMed result set with three records, including titles, abstracts, and metadata.",
                  "label": "returned",
                  "value": 1
                },
                {
                  "model": "z-ai/glm-5.3-flash",
                  "rationale": "The tool returned non-empty, structured output containing three PubMed results with titles, abstracts, authors, and metadata for the AlphaFold query.",
                  "label": "returned",
                  "value": 1
                }
              ]
            }
          ],
          "raw_output": "{\n  \"query\": \"Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.\",\n  \"adapted_query\": \"AlphaFold2 protein structure prediction Jumper 2021[dp]\",\n  \"provider\": \"PubMed (NCBI E-utilities)\",\n  \"tool_kind\": \"biomedical literature search (MeSH-indexed)\",\n  \"total_results\": 3,\n  \"returned_results\": 3,\n  \"results\": [\n    {\n      \"pmid\": \"34293799\",\n      \"title\": \"Highly accurate protein structure prediction for the human proteome.\",\n      \"abstract\": \"Protein structures can provide invaluable information, both for reasoning about biological processes and for enabling interventions such as structure-based drug development or targeted mutagenesis. After decades of effort, 17% of the total residues in human protein sequences are covered by an experimentally determined structure1. Here we markedly expand the structural coverage of the proteome by applying the state-of-the-art machine learning method, AlphaFold2, at a scale that covers almost the entire human proteome (98.5% of human proteins). The resulting dataset covers 58% of residues with a confident prediction, of which a subset (36% of all residues) have very high confidence. We introduce several metrics developed by building on the AlphaFold model and use them to interpret the dataset, identifying strong multi-domain predictions as well as regions that are likely to be disord …[truncated]"
        },
        {
          "probe_id": "obs-43539",
          "similarity": 0.982,
          "task_text": "What is the PMID of the 2026 Journal of Clinical Medicine paper by Xu et al. on early precise prediction and severe risk stratification of intrahepatic cholestasis of pregnancy?",
          "adapted_input": "intrahepatic cholestasis pregnancy prediction stratification Xu 2026",
          "score": 1,
          "redacted": null,
          "output_chars": 2853,
          "truncated": false,
          "created_at": "2026-10-08T22:50:55.723652Z",
          "judges": [
            {
              "facet": "capability",
              "verdict": "pass",
              "score": 1,
              "rationale": "Deterministic check — matched 1/1 required string(s).",
              "panel": null
            }
          ],
          "raw_output": "{\n  \"query\": \"What is the PMID of the 2026 Journal of Clinical Medicine paper by Xu et al. on early precise prediction and severe risk stratification of intrahepatic cholestasis of pregnancy?\",\n  \"adapted_query\": \"intrahepatic cholestasis pregnancy prediction stratification Xu 2026[dp]\",\n  \"provider\": \"PubMed (NCBI E-utilities)\",\n  \"tool_kind\": \"biomedical literature search (MeSH-indexed)\",\n  \"total_results\": 1,\n  \"returned_results\": 1,\n  \"results\": [\n    {\n      \"pmid\": \"42589990\",\n      \"title\": \"Early Precise Prediction and Severe Risk Stratification of Intrahepatic Cholestasis of Pregnancy: Advances and Future Directions in Clinical Translation from Traditional Models to Artificial Intelligence and Multi-Omics Technologies.\",\n      \"abstract\": \"Intrahepatic cholestasis of pregnancy (ICP) is a liver disorder unique to pregnancy, closely associated with severe adverse maternal and fetal outcomes such as preterm birth and intrauterine fetal death. Its pathogenesis involves a complex interplay of genetic, hormonal, metabolic, and environmental factors, with a higher risk observed in southern China and among individuals co-infected with hepatitis B virus. Substantial evidence demonstrates a significant dose-response relationship between serum total bile acid (TBA) levels and perinatal outcomes, with TBA \\u2265 40 \\u03bcmol/L commonly used as a criterion for severe ICP. However,  …[truncated]"
        },
        {
          "probe_id": "obs-43058",
          "similarity": 0.975,
          "task_text": "Find the August 2026 Diabetes, Obesity & Metabolism paper by Liao et al. asking whether more treatment translates to better outcomes for continuous glucose monitoring in gestational diabetes. PMID please.",
          "adapted_input": "Liao 2026 continuous glucose monitoring gestational diabetes",
          "score": 1,
          "redacted": null,
          "output_chars": 978,
          "truncated": false,
          "created_at": "2026-10-08T13:19:57.713161Z",
          "judges": [
            {
              "facet": "capability",
              "verdict": "pass",
              "score": 1,
              "rationale": "Deterministic check — matched 1/1 required string(s).",
              "panel": null
            }
          ],
          "raw_output": "{\n  \"query\": \"Find the August 2026 Diabetes, Obesity & Metabolism paper by Liao et al. asking whether more treatment translates to better outcomes for continuous glucose monitoring in gestational diabetes. PMID please.\",\n  \"adapted_query\": \"Liao continuous glucose monitoring gestational diabetes 2026[dp]\",\n  \"provider\": \"PubMed (NCBI E-utilities)\",\n  \"tool_kind\": \"biomedical literature search (MeSH-indexed)\",\n  \"total_results\": 1,\n  \"returned_results\": 1,\n  \"results\": [\n    {\n      \"pmid\": \"42642349\",\n      \"title\": \"Continuous Glucose Monitoring in Gestational Diabetes: Does More Treatment Translate to Better Outcomes?\",\n      \"abstract\": \"\",\n      \"authors\": [\n        \"Liao J\",\n        \"Yuan Q\",\n        \"Xia Y\"\n      ],\n      \"publication_date\": \"2026 Nov\",\n      \"journal\": \"Diabetes, obesity & metabolism\",\n      \"doi\": \"10.1111/dom.71282\",\n      \"publication_types\": [\n        \"Letter\"\n      ],\n      \"url\": \"https://pubmed.ncbi.nlm.nih.gov/42642349/\"\n    }\n  ]\n}"
        }
      ]
    },
    "evidence_teaser": {
      "task_text": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
      "verdict": "present",
      "score": 0.399,
      "similarity": 0.983,
      "n_real": 82
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
      },
      "facets": [
        {
          "name": "capability",
          "kano": "must_be",
          "weight": 1,
          "threshold": 0.5,
          "raw": 0.8226,
          "contribution": 0.7516
        },
        {
          "name": "price",
          "kano": "performance",
          "weight": 0.3,
          "threshold": 0.5,
          "raw": 0.9828,
          "contribution": 0.2948
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
        "n_real": 796,
        "n_near": 24,
        "near_mean": 0.851,
        "dist": [
          0.93,
          1,
          1,
          1,
          0,
          1,
          1,
          0.967,
          0.933,
          0.983,
          0.973,
          0.95,
          1,
          0.5,
          0.833,
          0.9,
          0.833,
          0.8,
          0.933,
          0,
          0.933,
          1,
          0.95,
          1
        ],
        "probes": [
          {
            "probe_id": "obs-42590",
            "similarity": 0.983,
            "task_text": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
            "adapted_input": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
            "score": 0.93,
            "redacted": null,
            "output_chars": 6055,
            "truncated": false,
            "created_at": "2026-10-08T06:21:58.891616Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 0.93,
                "rationale": "jev score 3.4/4 p=0.00/0.00/0.08/0.44/0.48 conf=0.50 | The top result is the exact canonical Nature paper (s41586-021-03819-2, 'Highly accurate protein str | The top result is the canonical Nature article (nature.com/articles/s41586-021-03819-2) for Jumper e",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev score 3.4/4 p=0.00/0.00/0.08/0.44/0.48 conf=0.50",
                    "score": 0.85
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The top result is the exact canonical Nature paper (s41586-021-03819-2, 'Highly accurate protein structure prediction with AlphaFold'), matching the ground truth Jumper et al. 2021. Additional authoritative results (PubMed, Wikipedia, DeepMind) reinforce coverage. Minor truncation of the last result…",
                    "score": 0.97
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The top result is the canonical Nature article (nature.com/articles/s41586-021-03819-2) for Jumper et al. 2021, 'Highly accurate protein structure prediction with AlphaFold' (Nature 596:583-589), exactly matching the ground truth. Supporting results include the PubMed record (PMID 34265844), the com…",
                    "score": 0.97
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "jev choice=excellent p{excellent=0.96, good=0.04, partial=0.00, irrelevant=0.00, poor=0.00} conf=0.95",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev choice=excellent p{excellent=0.96, good=0.04, partial=0.00, irrelevant=0.00, poor=0.00} conf=0.95",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The top two results are the exact Nature paper and its PubMed record, with the third being a closely related AlphaFold paper, directly satisfying the query intent.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The top two results are the exact target paper (Jumper et al., 'Highly accurate protein structure prediction with AlphaFold', Nature 2021) surfaced directly from nature.com and PubMed, with the third being the closely related companion human proteome paper, so the top results directly answer the que…",
                    "label": "excellent",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "jev choice=primary p{primary=1.00, low_quality=0.00, not_applicable=0.00, tertiary=0.00, reputable_secondary=0.00} conf=1.00",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev choice=primary p{primary=1.00, low_quality=0.00, not_applicable=0.00, tertiary=0.00, reputable_secondary=0.00} conf=1.00",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The top results cite the actual Nature peer-reviewed paper (s41586-021-03819-2) and its PubMed record, which are primary authoritative sources.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The top results directly surface the peer-reviewed Nature paper (nature.com s41586-021-03819-2) and its PubMed record, which are primary/authoritative sources, despite a few tertiary or low-quality entries mixed in lower down.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "jev choice=present p{present=1.00, implied=0.00, absent=0.00} conf=1.00",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev choice=present p{present=1.00, implied=0.00, absent=0.00} conf=1.00",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The output includes explicit URLs (e.g., nature.com/articles/s41586-021-03819-2, pubmed.ncbi.nlm.nih.gov/34265844/) and named documents, providing followable source references.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The output includes multiple explicit source references, including the direct Nature article URL (nature.com/articles/s41586-021-03819-2), PubMed links, and other named documents matching the ground truth citation.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "jev choice=returned p{returned=1.00, empty=0.00} conf=1.00",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev choice=returned p{returned=1.00, empty=0.00} conf=1.00",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The tool returned 14 non-empty search results, including the correct Nature paper URL, so usable output was produced.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The tool returned a non-empty JSON response with 14 search results, including the Nature paper URL and PubMed entries for the AlphaFold paper.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.\",\n  \"adapted_query\": \"Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.\",\n  \"provider\": \"Kagi Search\",\n  \"total_results\": 14,\n  \"api_params\": {\n    \"limit\": 20\n  },\n  \"results\": [\n    {\n      \"title\": \"Highly accurate protein structure prediction with AlphaFold\",\n      \"url\": \"https://www.nature.com/articles/s41586-021-03819-2\",\n      \"snippet\": \"AlphaFold predicts protein structures with an accuracy competitive with experimental structures in the majority of cases using a novel deep learning architecture.\",\n      \"published\": \"\"\n    },\n    {\n      \"title\": \"Highly accurate protein structure prediction with AlphaFold\",\n      \"url\": \"https://pubmed.ncbi.nlm.nih.gov/34265844/\",\n      \"snippet\": \"by J Jumper \\u00b7 2021 \\u00b7 Cited by 56055 \\u2014 Predicting the three-dimensional structure that a protein will adopt based solely on its amino acid sequence-the structure prediction component ...\",\n      \"published\": \"\"\n    },\n    {\n      \"title\": \"Highly accurate protein structure prediction for the human proteome\",\n      \"url\": \"https://pubmed.ncbi.nlm.nih.gov/34293799/\",\n      \"snippet\": \"Protein structures can provide invaluable information, both for reasoning about biological processes and for enabling i …[truncated]"
          },
          {
            "probe_id": "obs-33015",
            "similarity": 0.983,
            "task_text": "I'm after the 2026 Advanced Energy Materials paper by Zhang et al. on molecular design and interfacial functions of self-assembled monolayers for perovskite and tandem solar cells. Give me the DOI.",
            "adapted_input": "Zhang 2026 Advanced Energy Materials self-assembled monolayers molecular design interfacial perovskite tandem solar cells DOI",
            "score": 1,
            "redacted": null,
            "output_chars": 9251,
            "truncated": false,
            "created_at": "2026-09-07T20:19:39.882420Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "Deterministic check — matched 1/1 required string(s).",
                "panel": null
              }
            ],
            "raw_output": "{\n  \"query\": \"Zhang 2026 Advanced Energy Materials self-assembled monolayers molecular design interfacial perovskite tandem solar cells DOI\",\n  \"adapted_query\": \"Zhang 2026 Advanced Energy Materials self-assembled monolayers molecular design interfacial perovskite tandem solar cells DOI\",\n  \"provider\": \"Kagi Search\",\n  \"total_results\": 19,\n  \"api_params\": {\n    \"limit\": 20\n  },\n  \"results\": [\n    {\n      \"title\": \"Molecular Design and Interfacial Functions of Self\\u2010Assembled ...\",\n      \"url\": \"https://advanced.onlinelibrary.wiley.com/doi/abs/10.1002/aenm.70979\",\n      \"snippet\": \"by J Zhang \\u00b7 Cited by 3 \\u2014 Zhang, B. Kang, \\u201c Molecular Design and Interfacial Functions of Self-Assembled Monolayers for Perovskite and Tandem Solar Cells.\\u201d Advanced ...\",\n      \"published\": \"\"\n    },\n    {\n      \"title\": \"Molecular Design and Interfacial Functions of Self-Assembled Monolayers ...\",\n      \"url\": \"https://advanced.onlinelibrary.wiley.com/doi/10.1002/aenm.70979\",\n      \"snippet\": \"As a potent interfacial platform at the crossroads of molecular engineering and device physics, self-assembled monolayers (SAMs) have been demonstrated to enable molecular-level control over buried interfaces in perovskite solar cells (PSCs), whilst overcoming the intrinsic limitations of conventional charge transport layers (CTLs).\",\n      \"published\": \"\"\n    },\n    {\n      \"title\": \"Se …[truncated]"
          },
          {
            "probe_id": "obs-33020",
            "similarity": 0.982,
            "task_text": "What is the PMID of the 2026 Journal of Clinical Medicine paper by Xu et al. on early precise prediction and severe risk stratification of intrahepatic cholestasis of pregnancy?",
            "adapted_input": "Xu 2026 Journal of Clinical Medicine intrahepatic cholestasis pregnancy early prediction severe risk stratification PMID",
            "score": 1,
            "redacted": null,
            "output_chars": 5734,
            "truncated": false,
            "created_at": "2026-09-07T20:20:08.959650Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "Deterministic check — matched 1/1 required string(s).",
                "panel": null
              }
            ],
            "raw_output": "{\n  \"query\": \"Xu 2026 Journal of Clinical Medicine intrahepatic cholestasis pregnancy early prediction severe risk stratification PMID\",\n  \"adapted_query\": \"Xu 2026 Journal of Clinical Medicine intrahepatic cholestasis pregnancy early prediction severe risk stratification PMID\",\n  \"provider\": \"Kagi Search\",\n  \"total_results\": 10,\n  \"api_params\": {\n    \"limit\": 20\n  },\n  \"results\": [\n    {\n      \"title\": \"Early Precise Prediction and Severe Risk Stratification of Intrahepatic ...\",\n      \"url\": \"https://pubmed.ncbi.nlm.nih.gov/42589990/\",\n      \"snippet\": \"However, most existing prediction models are based on single-center, retrospective studies with small sample sizes and insufficient external validation, limiting their clinical generalizability. In recent years, nomograms and machine learning methods have demonstrated advantages in the early prediction and risk stratification of ICP.\",\n      \"published\": \"\"\n    },\n    {\n      \"title\": \"pubmed.ncbi.nlm.nih.gov\",\n      \"url\": \"https://pubmed.ncbi.nlm.nih.gov/33197417/\",\n      \"snippet\": \"Enable cookies for pubmed.ncbi.nlm.nih.govand reload this page to continue.\",\n      \"published\": \"\"\n    },\n    {\n      \"title\": \"Risk factors and machine learning prediction models for intrahepatic ...\",\n      \"url\": \"https://pmc.ncbi.nlm.nih.gov/articles/PMC11780866/\",\n      \"snippet\": \"Intrahepatic cholestasis of pregnancy (ICP) is a liver dis …[truncated]"
          }
        ]
      },
      "evidence_teaser": {
        "task_text": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
        "verdict": "present",
        "score": 0.93,
        "similarity": 0.983,
        "n_real": 796
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
          "raw": 0.727,
          "contribution": 0.6178
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
        "n_real": 158,
        "n_near": 24,
        "near_mean": 0.628,
        "dist": [
          0.932,
          1,
          1,
          1,
          1,
          1,
          0.933,
          0.133,
          0.167,
          0.067,
          0.1,
          0.5,
          0,
          0.967,
          0.967,
          0.967,
          0.967,
          0.1,
          1,
          1,
          0.343,
          0,
          0,
          0.938
        ],
        "probes": [
          {
            "probe_id": "obs-42594",
            "similarity": 0.983,
            "task_text": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
            "adapted_input": "{\"title\": \"highly accurate protein structure prediction with AlphaFold\", \"author\": \"Jumper\", \"year\": 2021}",
            "score": 0.932,
            "redacted": null,
            "output_chars": 1454,
            "truncated": false,
            "created_at": "2026-10-08T06:26:19.615381Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 0.932,
                "rationale": "jev score 3.5/4 p=0.00/0.00/0.06/0.38/0.56 conf=0.58 | The tool correctly identified the queried paper: DOI 10.1038/s41586-021-03819-2, title 'Highly accur | The tool correctly resolved the query to the exact target paper: Jumper et al., 'Highly accurate pro",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev score 3.5/4 p=0.00/0.00/0.06/0.38/0.56 conf=0.58",
                    "score": 0.875
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The tool correctly identified the queried paper: DOI 10.1038/s41586-021-03819-2, title 'Highly accurate protein structure prediction with AlphaFold', Nature 2021 — matching the ground truth (Jumper et al., Nature 596:583-589) exactly. It also returned a valid open-access PDF location (publisher publ…",
                    "score": 0.97
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The tool correctly resolved the query to the exact target paper: Jumper et al., 'Highly accurate protein structure prediction with AlphaFold', Nature 2021, with the correct DOI (10.1038/s41586-021-03819-2), title, year, and journal matching the ground truth. It accurately reports the paper as open a…",
                    "score": 0.95
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "jev choice=excellent p{excellent=1.00, poor=0.00, good=0.00, partial=0.00, irrelevant=0.00} conf=1.00",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev choice=excellent p{excellent=1.00, poor=0.00, good=0.00, partial=0.00, irrelevant=0.00} conf=1.00",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The tool resolved the exact target paper (DOI 10.1038/s41586-021-03819-2, 'Highly accurate protein structure prediction with AlphaFold', Nature 2021) with a direct open-access PDF link, perfectly matching the query intent.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The tool correctly resolved the exact AlphaFold 2 Nature 2021 paper (DOI 10.1038/s41586-021-03819-2) with an open-access publisher PDF, directly answering the query intent.",
                    "label": "excellent",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "jev choice=primary p{primary=0.99, not_applicable=0.01, tertiary=0.00, low_quality=0.00, reputable_secondary=0.00} conf=0.99",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev choice=primary p{primary=0.99, not_applicable=0.01, tertiary=0.00, low_quality=0.00, reputable_secondary=0.00} conf=0.99",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The tool resolves to the peer-reviewed Nature paper itself (DOI 10.1038/s41586-021-03819-2) with publisher-hosted OA locations, which is a primary authoritative source.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The tool resolved the query to the peer-reviewed Nature paper itself (DOI 10.1038/s41586-021-03819-2), a primary authoritative source.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "jev choice=present p{present=1.00, implied=0.00, absent=0.00} conf=1.00",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev choice=present p{present=1.00, implied=0.00, absent=0.00} conf=1.00",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The output includes explicit source references such as the DOI (10.1038/s41586-021-03819-2), the Nature article URL, and PMC repository links that a reader can follow back to the material.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The output explicitly includes the DOI (10.1038/s41586-021-03819-2) and multiple concrete URLs (Nature PDF, PMC repository, DOI link) that a reader can follow back to the source material.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "jev choice=returned p{returned=1.00, empty=0.00} conf=1.00",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev choice=returned p{returned=1.00, empty=0.00} conf=1.00",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The tool returned a complete JSON payload with a resolved DOI, title, journal, and open-access locations, so non-empty usable output was produced.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The tool returned a non-empty, structured JSON response containing a resolved DOI, title, OA status, and multiple open-access locations for the query.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.\",\n  \"provider\": \"Unpaywall (via Crossref top-DOI lookup)\",\n  \"tool_kind\": \"open-access PDF locator (DOI-keyed)\",\n  \"resolved_paper\": {\n    \"doi\": \"10.1038/s41586-021-03819-2\",\n    \"resolved_by\": \"crossref:query.title\",\n    \"title\": \"Highly accurate protein structure prediction with AlphaFold\",\n    \"year\": 2021,\n    \"journal\": \"Nature\",\n    \"is_open_access\": true,\n    \"oa_status\": \"hybrid\"\n  },\n  \"best_open_access_location\": {\n    \"url\": \"https://www.nature.com/articles/s41586-021-03819-2.pdf\",\n    \"url_for_pdf\": \"https://www.nature.com/articles/s41586-021-03819-2.pdf\",\n    \"host_type\": \"publisher\",\n    \"version\": \"publishedVersion\",\n    \"license\": \"cc-by\"\n  },\n  \"all_oa_locations\": [\n    {\n      \"url\": \"https://www.nature.com/articles/s41586-021-03819-2.pdf\",\n      \"url_for_pdf\": \"https://www.nature.com/articles/s41586-021-03819-2.pdf\",\n      \"host_type\": \"publisher\",\n      \"version\": \"publishedVersion\",\n      \"license\": \"cc-by\"\n    },\n    {\n      \"url\": \"https://www.ncbi.nlm.nih.gov/pmc/articles/8371605\",\n      \"url_for_pdf\": null,\n      \"host_type\": \"repository\",\n      \"version\": \"submittedVersion\",\n      \"license\": \"cc-by\"\n    },\n    {\n      \"url\": \"https://doi.org/10.25504/fairsharing.246086\",\n      \"url_for_pdf\": null,\n      \"host_type\": \"repository\",\n   …[truncated]"
          },
          {
            "probe_id": "obs-32683",
            "similarity": 0.983,
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
            "probe_id": "obs-32605",
            "similarity": 0.982,
            "task_text": "Locate the 2026 Applied Sciences paper by Duryagin et al. on nitrogen biostimulation of petroleum-contaminated sandy podzolic soil under boreal conditions. I need the DOI.",
            "adapted_input": "{\"title\": \"nitrogen biostimulation of petroleum-contaminated sandy podzolic soil under boreal conditions\", \"author\": \"Duryagin\", \"year\": 2026}",
            "score": 1,
            "redacted": null,
            "output_chars": 1487,
            "truncated": false,
            "created_at": "2026-08-29T10:08:51.915591Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "Deterministic check — matched 1/1 required string(s).",
                "panel": null
              }
            ],
            "raw_output": "{\n  \"query\": \"Locate the 2026 Applied Sciences paper by Duryagin et al. on nitrogen biostimulation of petroleum-contaminated sandy podzolic soil under boreal conditions. I need the DOI.\",\n  \"provider\": \"Unpaywall (via Crossref top-DOI lookup)\",\n  \"tool_kind\": \"open-access PDF locator (DOI-keyed)\",\n  \"resolved_paper\": {\n    \"doi\": \"10.3390/app16094190\",\n    \"resolved_by\": \"crossref:query.title\",\n    \"title\": \"Nitrogen Biostimulation of Petroleum-Contaminated Sandy Podzolic Soil Under Boreal Conditions: Effects of Temperature, Nitrogen Form, and Contamination Level\",\n    \"year\": 2026,\n    \"journal\": \"Applied Sciences\",\n    \"is_open_access\": true,\n    \"oa_status\": \"gold\"\n  },\n  \"best_open_access_location\": {\n    \"url\": \"https://www.mdpi.com/2076-3417/16/9/4190/pdf?version=1777038589\",\n    \"url_for_pdf\": \"https://www.mdpi.com/2076-3417/16/9/4190/pdf?version=1777038589\",\n    \"host_type\": \"publisher\",\n    \"version\": \"publishedVersion\",\n    \"license\": \"cc-by\"\n  },\n  \"all_oa_locations\": [\n    {\n      \"url\": \"https://www.mdpi.com/2076-3417/16/9/4190/pdf?version=1777038589\",\n      \"url_for_pdf\": \"https://www.mdpi.com/2076-3417/16/9/4190/pdf?version=1777038589\",\n      \"host_type\": \"publisher\",\n      \"version\": \"publishedVersion\",\n      \"license\": \"cc-by\"\n    },\n    {\n      \"url\": \"https://doaj.org/article/fa467b42a5714d798e0dabb225e61a11\",\n      \"url_for_pdf\": null,\n      \"host_type\": \"re …[truncated]"
          }
        ]
      },
      "evidence_teaser": {
        "task_text": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
        "verdict": "present",
        "score": 0.932,
        "similarity": 0.983,
        "n_real": 158
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
      },
      "facets": [
        {
          "name": "capability",
          "kano": "must_be",
          "weight": 1,
          "threshold": 0.5,
          "raw": 0.7136,
          "contribution": 0.599
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
        "n_real": 863,
        "n_near": 24,
        "near_mean": 0.827,
        "dist": [
          0.983,
          1,
          1,
          0,
          0,
          0,
          1,
          1,
          1,
          0.933,
          0.983,
          0.967,
          0.933,
          0.967,
          1,
          0.983,
          1,
          0.975,
          0.933,
          0.933,
          0.967,
          1,
          0.5,
          0.8
        ],
        "probes": [
          {
            "probe_id": "obs-5263",
            "similarity": 0.983,
            "task_text": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
            "adapted_input": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
            "score": 0.983,
            "redacted": null,
            "output_chars": 4950,
            "truncated": false,
            "created_at": "2026-05-21T12:10:18.291893Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 0.983,
                "rationale": "The tool provided the exact canonical source requested. The first result is the direct link to the N | The tool returns the canonical Nature paper (s41586-021-03819-2) as the first result, along with Dee | The tool returned the canonical Nature paper as the top result with correct URL and title, exactly m",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provided the exact canonical source requested. The first result is the direct link to the Nature article (https://www.nature.com/articles/s41586-021-03819-2), which matches the title, journal, and year specified in the ground truth. Subsequent results also confirm the same paper and provide…",
                    "score": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returns the canonical Nature paper (s41586-021-03819-2) as the first result, along with DeepMind's official page, a PDF, and other authoritative mirrors. All results are directly relevant, accurate, and cover the query comprehensively. The only minor deduction is that the snippet for the fi…",
                    "score": 0.95
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned the canonical Nature paper as the top result with correct URL and title, exactly matching the ground truth. It also provided diverse relevant sources, fulfilling the tool's contract perfectly.",
                    "score": 1
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "The top result is the exact Nature paper requested, and the subsequent results provide direct links to the paper, the official DeepMind page, and the PDF version.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The top result is the exact Nature paper requested, and the subsequent results provide direct links to the paper, the official DeepMind page, and the PDF version.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The top three results include the actual Nature paper and a direct link to DeepMind's official page, directly and accurately addressing the query intent.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The top results directly include the exact Nature paper from a high-quality source, fully answering the query intent.",
                    "label": "excellent",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool provides direct links to the peer-reviewed paper published in the journal Nature, which is a primary scientific source.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides direct links to the peer-reviewed paper published in the journal Nature, which is a primary scientific source.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output directly cites the peer-reviewed Nature paper (s41586-021-03819-2) and other authoritative sources like the DeepMind official site and PubMed Central, which are primary sources.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output cites the peer-reviewed Nature paper directly, which is a primary source.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool output provides multiple explicit source references, including direct URLs to Nature and Semantic Scholar, as well as specific paper titles and DOI information.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool output provides multiple explicit source references, including direct URLs to Nature and Semantic Scholar, as well as specific paper titles and DOI information.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output provides explicit URLs and document titles such as the Nature paper link, which are direct references to the underlying source material.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The output contains explicit URLs to the Nature paper and other sources, providing clear, followable references for readers.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool returned a list of search results containing the requested information regarding the AlphaFold 2 Nature paper.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned a list of search results containing the requested information regarding the AlphaFold 2 Nature paper.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a JSON response containing a query, provider, total_results count of 10, and an array of search results with titles, URLs, and snippets, which is non-empty and usable output.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool output contains a non-empty JSON object with search results, indicating usable output was returned for the query.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.\",\n  \"provider\": \"DuckDuckGo (MCP)\",\n  \"total_results\": 10,\n  \"results\": [\n    {\n      \"title\": \"Highly accurate protein structure prediction with AlphaFold - Nature\",\n      \"url\": \"https://www.nature.com/articles/s41586-021-03819-2\",\n      \"snippet\": \"AlphaFoldpredictsproteinstructureswith an accuracy competitive with experimentalstructuresin the majority of cases using a novel deep learning architecture.\"\n    },\n    {\n      \"title\": \"AlphaFold \\u2014 Google DeepMind\",\n      \"url\": \"https://deepmind.google/science/alphafold/\",\n      \"snippet\": \"NaturepublishesAlphaFold'sdetailed methodology in thepaper\\\"HighlyaccurateproteinstructurepredictionwithAlphaFold\\\" andDeepMindopen sources the code along with 60 pages of supplemental information.\"\n    },\n    {\n      \"title\": \"PDFHighly accurate protein structure prediction with AlphaFold\",\n      \"url\": \"https://dasher.wustl.edu/chem430/readings/nature-596-583-21.pdf\",\n      \"snippet\": \"By developing anaccurateproteinstructurepredictionalgorithm, coupled with existing large and well-curatedstructureandsequence databases assembled by the experimental community, we hope to accelerate the advancement of structural bioinformatics that can keep pace with the genomics revolution.\"\n    },\n    {\n      \"title\": \"Highly accurat …[truncated]"
          },
          {
            "probe_id": "obs-32676",
            "similarity": 0.983,
            "task_text": "I'm after the 2026 Advanced Energy Materials paper by Zhang et al. on molecular design and interfacial functions of self-assembled monolayers for perovskite and tandem solar cells. Give me the DOI.",
            "adapted_input": "I'm after the 2026 Advanced Energy Materials paper by Zhang et al. on molecular design and interfacial functions of self-assembled monolayers for perovskite and tandem solar cells. Give me the DOI.",
            "score": 1,
            "redacted": null,
            "output_chars": 4889,
            "truncated": false,
            "created_at": "2026-08-29T10:34:01.217994Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "Deterministic check — matched 1/1 required string(s).",
                "panel": null
              }
            ],
            "raw_output": "{\n  \"query\": \"I'm after the 2026 Advanced Energy Materials paper by Zhang et al. on molecular design and interfacial functions of self-assembled monolayers for perovskite and tandem solar cells. Give me the DOI.\",\n  \"adapted_query\": \"Zhang 2026 Advanced Energy Materials self-assembled monolayers molecular design interfacial perovskite tandem solar cells DOI\",\n  \"provider\": \"DuckDuckGo (MCP)\",\n  \"total_results\": 10,\n  \"top_documents\": [],\n  \"results\": [\n    {\n      \"title\": \"Molecular Design and Interfacial Functions of Self-Assembled Monolayers ...\",\n      \"url\": \"https://advanced.onlinelibrary.wiley.com/doi/abs/10.1002/aenm.70979\",\n      \"snippet\": \"ABSTRACT As a potentinterfacialplatform at the crossroads ofmolecularengineering and device physics,self-assembledmonolayers(SAMs) have been demonstrated to enablemolecular-level control over buried interfaces inperovskitesolarcells(PSCs), whilst overcoming the intrinsic limitations of conventional charge transport layers (CTLs). Over the past two years, SAM-enabled interface ...\"\n    },\n    {\n      \"title\": \"Self-Assembled Monolayers for Perovskite-Based Tandem Solar Cells\",\n      \"url\": \"https://advanced.onlinelibrary.wiley.com/doi/10.1002/adfm.202600042\",\n      \"snippet\": \"Perovskitetandemsolarcells(TSCs) are pivotal for breaking the S-Q limit and enabling low-cost, high-efficiency photovoltaics. In this pursuit,self-assembledmo …[truncated]"
          },
          {
            "probe_id": "obs-32795",
            "similarity": 0.982,
            "task_text": "What is the PMID of the 2026 Journal of Clinical Medicine paper by Xu et al. on early precise prediction and severe risk stratification of intrahepatic cholestasis of pregnancy?",
            "adapted_input": "What is the PMID of the 2026 Journal of Clinical Medicine paper by Xu et al. on early precise prediction and severe risk stratification of intrahepatic cholestasis of pregnancy?",
            "score": 1,
            "redacted": null,
            "output_chars": 5951,
            "truncated": false,
            "created_at": "2026-08-29T11:40:30.705127Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "Deterministic check — matched 1/1 required string(s).",
                "panel": null
              }
            ],
            "raw_output": "{\n  \"query\": \"What is the PMID of the 2026 Journal of Clinical Medicine paper by Xu et al. on early precise prediction and severe risk stratification of intrahepatic cholestasis of pregnancy?\",\n  \"adapted_query\": \"Xu et al 2026 Journal of Clinical Medicine intrahepatic cholestasis pregnancy early precise prediction severe risk stratification PMID\",\n  \"provider\": \"DuckDuckGo (MCP)\",\n  \"total_results\": 10,\n  \"top_documents\": [\n    {\n      \"url\": \"https://pubmed.ncbi.nlm.nih.gov/42589990/\",\n      \"title\": \"Early Precise Prediction and Severe Risk Stratification of Intrahepatic ...\",\n      \"text\": \"pubmed.ncbi.nlm.nih.gov Cookies must be enabled Enable cookies for pubmed.ncbi.nlm.nih.gov and reload this page to continue.\\n\\n---\\n[Content info: Showing characters 0-124 of 124 total]\",\n      \"truncated\": false\n    },\n    {\n      \"url\": \"https://www.mdpi.com/2077-0383/15/15/5887\",\n      \"title\": \"Early Precise Prediction and Severe Risk Stratification of Intrahepatic ...\",\n      \"text\": \"---\\n[Content info: Showing characters 0-0 of 0 total]\",\n      \"truncated\": false\n    }\n  ],\n  \"results\": [\n    {\n      \"title\": \"Early Precise Prediction and Severe Risk Stratification of Intrahepatic ...\",\n      \"url\": \"https://pubmed.ncbi.nlm.nih.gov/42589990/\",\n      \"snippet\": \"However, most existingpredictionmodels are based on single-center, retrospective studies with small sample sizes and ins …[truncated]"
          }
        ]
      },
      "evidence_teaser": {
        "task_text": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
        "verdict": "present",
        "score": 0.983,
        "similarity": 0.983,
        "n_real": 863
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
          "raw": 0.6229,
          "contribution": 0.472
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
        "n_real": 287,
        "n_near": 24,
        "near_mean": 0.756,
        "dist": [
          1,
          1,
          0.983,
          1,
          1,
          1,
          1,
          1,
          0.983,
          1,
          1,
          1,
          0.978,
          1,
          0.983,
          1,
          0.994,
          0,
          0.5,
          0.396,
          0.133,
          0.1,
          0.1,
          0
        ],
        "probes": [
          {
            "probe_id": "obs-12380",
            "similarity": 0.99,
            "task_text": "Find the 2025 NANO Select paper on heat-sterilizable antibacterial coatings based on Nafion and graphene quantum dots.",
            "adapted_input": "{\"search\": \"Nafion graphene quantum dots antibacterial\", \"year\": 2025}",
            "score": 1,
            "redacted": null,
            "output_chars": 20000,
            "truncated": true,
            "created_at": "2026-06-27T00:46:30.189166Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "The tool successfully identified the exact paper requested in the query. The first result in the lis | The tool correctly returned the exact paper as the first result, with correct title, authors, year,  | The tool returned the exact paper as specified in the ground truth, with correct title, authors, yea",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool successfully identified the exact paper requested in the query. The first result in the list matches the title, journal (Nano Select), year (2025), authors, and DOI specified in the ground truth perfectly.",
                    "score": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool correctly returned the exact paper as the first result, with correct title, authors, year, DOI (10.1002/nano.70012), and venue (Nano Select). The abstract confirms the topic of heat-sterilizable antibacterial coatings based on Nafion and graphene quantum dots. This fully addresses the query…",
                    "score": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned the exact paper as specified in the ground truth, with correct title, authors, year, DOI, and venue as the top result, perfectly matching all query criteria and metadata.",
                    "score": 1
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "The very first result is the exact paper requested by the user, matching the title, journal, year, and subject matter perfectly.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The very first result is the exact paper requested by the user, matching the title, journal, year, and subject matter perfectly.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The first result is the exact 2025 NANO Select paper on heat-sterilizable antibacterial coatings based on Nafion and graphene quantum dots, directly matching the query intent.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's top results include the exact paper as the first result, but the second and third results are not directly relevant to the specific query, showing a mix of relevant and off-topic items.",
                    "label": "partial",
                    "value": 0.5
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool provides citations to peer-reviewed academic papers from journals such as Nano Select, Polymers, and Biosensors.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides citations to peer-reviewed academic papers from journals such as Nano Select, Polymers, and Biosensors.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output includes a peer-reviewed paper from the journal NANO Select, which is a primary authoritative source.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output cites peer-reviewed academic papers, which are primary sources as defined in the rubric.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool output provides explicit source references including DOIs, OpenAlex IDs, and direct URLs for the papers found.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool output provides explicit source references including DOIs, OpenAlex IDs, and direct URLs for the papers found.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The output includes explicit DOIs, OpenAlex IDs, and open access URLs for each paper, allowing a reader to directly access the underlying sources.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output provides explicit URLs, including DOI and open access links, which are clear source references for readers to access the underlying material.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool returned a list of search results, including the specific paper requested in the query.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned a list of search results, including the specific paper requested in the query.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a non-empty list of search results including the exact paper requested.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned a non-empty JSON response containing search results and paper details, indicating usable output.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find the 2025 NANO Select paper on heat-sterilizable antibacterial coatings based on Nafion and graphene quantum dots.\",\n  \"adapted_spec\": {\n    \"search\": \"Nafion graphene quantum dots antibacterial\",\n    \"year\": 2025\n  },\n  \"lookup_mode\": \"keyword\",\n  \"provider\": \"OpenAlex\",\n  \"tool_kind\": \"academic paper search (all fields, citation graph)\",\n  \"total_results\": 110,\n  \"returned_results\": 30,\n  \"results\": [\n    {\n      \"id\": \"https://openalex.org/W4409052526\",\n      \"doi\": \"https://doi.org/10.1002/nano.70012\",\n      \"title\": \"Heat Sterilizable Coatings Based on Nafion and Graphene Quantum Dots With Advanced Antibacterial Performance\",\n      \"authors\": [\n        \"Mohammed Suleman Beg\",\n        \"Ella N. Gibbons\",\n        \"James Duncalf\",\n        \"Spyridon Gavalas\",\n        \"Daniel W. Redman\",\n        \"Mark A. Holden\",\n        \"Antonios Kelarakis\"\n      ],\n      \"publication_year\": 2025,\n      \"publication_date\": \"2025-03-31\",\n      \"venue\": \"Nano Select\",\n      \"venue_type\": \"journal\",\n      \"cited_by_count\": 1,\n      \"open_access_url\": \"https://onlinelibrary.wiley.com/doi/pdfdirect/10.1002/nano.70012\",\n      \"is_open_access\": true,\n      \"abstract\": \"ABSTRACT The study focuses on the preparation of electrostatically assembled layer\\u2010by\\u2010layer waterborne nanocoatings comprising negatively charged Nafion and positively charged imidazole modified\\u2010graphene …[truncated]"
          },
          {
            "probe_id": "obs-12382",
            "similarity": 0.985,
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
          },
          {
            "probe_id": "obs-7336",
            "similarity": 0.983,
            "task_text": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
            "adapted_input": "{\"search\": \"AlphaFold protein structure\", \"year\": 2021}",
            "score": 0.983,
            "redacted": null,
            "output_chars": 20000,
            "truncated": true,
            "created_at": "2026-05-23T23:07:01.471140Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 0.983,
                "rationale": "The tool successfully identified the exact canonical paper requested. The first result in the list m | The tool returned the exact canonical paper (Jumper et al., 'Highly accurate protein structure predi | The tool returned the exact paper specified in the ground truth as the top result with correct title",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool successfully identified the exact canonical paper requested. The first result in the list matches the title, authors (starting with John Jumper), year (2021), venue (Nature), and DOI provided in the ground truth. It also provided the correct abstract and metadata.",
                    "score": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned the exact canonical paper (Jumper et al., 'Highly accurate protein structure prediction with AlphaFold', Nature 2021) as the top result, with correct title, authors, year, DOI, and abstract. The second result is related but not the primary paper; however, the query is fully satisfi…",
                    "score": 0.95
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned the exact paper specified in the ground truth as the top result with correct title, authors, year, venue (Nature), and DOI, fully satisfying the query with accurate and complete metadata.",
                    "score": 1
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "The very first result is the exact paper requested by the user, including the correct title, journal (Nature), year (2021), and authors.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The very first result is the exact paper requested by the user, including the correct title, journal (Nature), year (2021), and authors.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The top result is precisely the requested DeepMind 2021 Nature paper on AlphaFold 2, directly and accurately addressing the query intent.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The first result directly matches the ground truth paper, fulfilling the query intent with high accuracy and relevance.",
                    "label": "excellent",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool provides a direct citation to a peer-reviewed paper published in the journal Nature, which is a primary scientific source.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides a direct citation to a peer-reviewed paper published in the journal Nature, which is a primary scientific source.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output includes a peer-reviewed Nature paper with a DOI, which is a primary source.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool cites a peer-reviewed paper in Nature, which is a primary source according to the facet description.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool output provides explicit source references including DOIs, OpenAlex IDs, and direct URLs to the papers.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool output provides explicit source references including DOIs, OpenAlex IDs, and direct URLs to the papers.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool output includes explicit source references such as DOIs and open access URLs for the identified papers.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output includes explicit source references such as URLs (e.g., open_access_url) and DOIs for each paper, allowing readers to directly access the underlying material.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool returned a JSON object containing a list of search results, including the specific paper requested.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned a JSON object containing a list of search results, including the specific paper requested.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a list of 30 results including the requested AlphaFold paper, so output is non-empty.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool output is a non-empty JSON object containing structured search results with the requested paper, fulfilling the requirement for usable output.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.\",\n  \"adapted_spec\": {\n    \"search\": \"AlphaFold protein structure\",\n    \"year\": 2021\n  },\n  \"provider\": \"OpenAlex\",\n  \"tool_kind\": \"academic paper search (all fields, citation graph)\",\n  \"total_results\": 970,\n  \"returned_results\": 30,\n  \"results\": [\n    {\n      \"id\": \"https://openalex.org/W3177828909\",\n      \"doi\": \"https://doi.org/10.1038/s41586-021-03819-2\",\n      \"title\": \"Highly accurate protein structure prediction with AlphaFold\",\n      \"authors\": [\n        \"John Jumper\",\n        \"Richard Evans\",\n        \"Alexander Pritzel\",\n        \"Tim Green\",\n        \"Michael Figurnov\",\n        \"Olaf Ronneberger\",\n        \"Kathryn Tunyasuvunakool\",\n        \"Russ Bates\",\n        \"Augustin \\u017d\\u00eddek\",\n        \"Anna Potapenko\",\n        \"Alex Bridgland\",\n        \"Clemens Meyer\",\n        \"Simon K\\u00f6hl\",\n        \"Andrew J. Ballard\",\n        \"Andrew Cowie\",\n        \"Bernardino Romera\\u2010Paredes\",\n        \"Stanislav Nikolov\",\n        \"Rishub Jain\",\n        \"Jonas Adler\",\n        \"Trevor Back\",\n        \"Stig Petersen\",\n        \"David Reiman\",\n        \"Ellen Clancy\",\n        \"Micha\\u0142 Zieli\\u0144ski\",\n        \"Martin Steinegger\",\n        \"Michalina Pacholska\",\n        \"Tamas Berghammer\",\n        \"Sebastian W. Bodenstein\",\n        \"David Silver\",\n        \"Oriol Vin …[truncated]"
          }
        ]
      },
      "evidence_teaser": {
        "task_text": "Find the 2025 NANO Select paper on heat-sterilizable antibacterial coatings based on Nafion and graphene quantum dots.",
        "verdict": "present",
        "score": 1,
        "similarity": 0.99,
        "n_real": 287
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
      },
      "facets": [
        {
          "name": "capability",
          "kano": "must_be",
          "weight": 1,
          "threshold": 0.5,
          "raw": 0.544,
          "contribution": 0.3616
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
        "n_real": 906,
        "n_near": 24,
        "near_mean": 0.833,
        "dist": [
          0.933,
          1,
          0,
          1,
          1,
          1,
          1,
          1,
          1,
          0.9,
          0.933,
          0.95,
          0.85,
          0.833,
          0.983,
          1,
          0.983,
          0.892,
          0.833,
          0.967,
          0.933,
          0,
          0.5,
          0.5
        ],
        "probes": [
          {
            "probe_id": "obs-5270",
            "similarity": 0.983,
            "task_text": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
            "adapted_input": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
            "score": 0.933,
            "redacted": null,
            "output_chars": 20000,
            "truncated": true,
            "created_at": "2026-05-21T12:18:08.601076Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 0.933,
                "rationale": "The tool provided the exact title, the correct journal (Nature), the correct year (2021), and the co | The tool correctly identified the paper title and DOI in its answer, and the top results include the | The tool accurately identified the paper with the correct title, publication, and DOI in the answer ",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provided the exact title, the correct journal (Nature), the correct year (2021), and the correct DOI (10.1038/s41586-021-03819-2) which leads directly to the canonical paper. The search results also included the direct link to the Nature article as the top relevant result.",
                    "score": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool correctly identified the paper title and DOI in its answer, and the top results include the canonical Nature page (result #4) and a relevant Reddit post. The answer is concise and accurate, matching the ground truth. Minor note: the first result is a Facebook post, but the authoritative sou…",
                    "score": 0.9
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool accurately identified the paper with the correct title, publication, and DOI in the answer field, and the top results include the canonical Nature link (s41586-021-03819-2). It directly addresses the query with relevant and authoritative results, though minor details like author names or pa…",
                    "score": 0.9
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "good",
                "score": 0.75,
                "rationale": "The tool provides a correct answer with the exact paper title, journal, and DOI, but the top three search results include a Facebook post and a Reddit discussion rather than the primary Nature article, and the third result is a related but different Nature paper.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The top results directly provide the exact paper title, the correct journal (Nature), the correct year (2021), and the specific DOI requested by the user.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool provides a correct answer with the exact paper title, journal, and DOI, but the top three search results include a Facebook post and a Reddit discussion rather than the primary Nature article, and the third result is a related but different Nature paper.",
                    "label": "good",
                    "value": 0.75
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's answer directly provides the accurate paper details, and the top results contain relevant references despite mixed source quality and one off-topic item.",
                    "label": "good",
                    "value": 0.75
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool provides the direct DOI and URL to the peer-reviewed paper published in the journal Nature, which is a primary source.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides the direct DOI and URL to the peer-reviewed paper published in the journal Nature, which is a primary source.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool cites the actual peer-reviewed Nature paper and its DOI, which is a primary authoritative source.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool explicitly cites a peer-reviewed paper in Nature, which is a primary source, despite including some low-quality search results.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool provides the specific paper title, the DOI, and multiple direct URLs to the source material.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides the specific paper title, the DOI, and multiple direct URLs to the source material.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The output includes explicit references such as the DOI (10.1038/s41586-021-03819-2) and a direct URL to the Nature article.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The output explicitly includes the DOI and multiple URLs pointing to the Nature paper and other sources, allowing readers to follow back to the underlying material.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool returned a detailed answer including the paper title, publication, and DOI, along with several search results.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned a detailed answer including the paper title, publication, and DOI, along with several search results.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a detailed answer and multiple search results, including the correct paper title, DOI, and a direct link to the Nature article.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool output contains a detailed answer, search results, and metadata, which constitutes non-empty and usable output.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.\",\n  \"provider\": \"Tavily\",\n  \"answer\": \"DeepMind's 2021 Nature paper announced AlphaFold 2, achieving highly accurate protein structure predictions. The paper is titled \\\"Highly accurate protein structure prediction with AlphaFold\\\" and published in Nature. The DOI is 10.1038/s41586-021-03819-2.\",\n  \"total_results\": 20,\n  \"api_params\": {\n    \"search_depth\": \"advanced\",\n    \"include_answer\": true,\n    \"include_raw_content\": false,\n    \"max_results\": 20\n  },\n  \"results\": [\n    {\n      \"title\": \"Highly accurate protein structure prediction with AlphaFold ...\",\n      \"url\": \"https://www.facebook.com/groups/DeepNetGroup/posts/1518854118507465\",\n      \"snippet\": \"Highly accurate protein structure prediction with AlphaFold (DeepMind, Nature 2021) Paper: https://www.nature.com/articles/s41586-021-03819-2\",\n      \"score\": 0.99993396,\n      \"published_date\": \"\"\n    },\n    {\n      \"title\": \"\\\"Highly accurate protein structure prediction with AlphaFold ... - Reddit\",\n      \"url\": \"https://www.reddit.com/r/genomics/comments/ol07ac/highly_accurate_protein_structure_prediction_with\",\n      \"snippet\": \"\\\"Highly accurate protein structure prediction with AlphaFold\\\", Jumper et al 2021 {DM} (AlphaFold 2 paper, source code) \\u00b7 Comments Section \\u00b7 More\",\n      \"score\": 0. …[truncated]"
          },
          {
            "probe_id": "obs-32681",
            "similarity": 0.983,
            "task_text": "I'm after the 2026 Advanced Energy Materials paper by Zhang et al. on molecular design and interfacial functions of self-assembled monolayers for perovskite and tandem solar cells. Give me the DOI.",
            "adapted_input": "Zhang 2026 Advanced Energy Materials self-assembled monolayers perovskite tandem solar cells molecular design interfacial",
            "score": 1,
            "redacted": null,
            "output_chars": 20000,
            "truncated": true,
            "created_at": "2026-08-29T10:36:04.540377Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "Deterministic check — matched 1/1 required string(s).",
                "panel": null
              }
            ],
            "raw_output": "{\n  \"query\": \"Zhang 2026 Advanced Energy Materials self-assembled monolayers perovskite tandem solar cells molecular design interfacial\",\n  \"adapted_query\": \"Zhang 2026 Advanced Energy Materials self-assembled monolayers perovskite tandem solar cells molecular design interfacial\",\n  \"provider\": \"Tavily\",\n  \"answer\": \"Self-assembled monolayers (SAMs) enhance perovskite solar cell efficiency through molecular design and interface engineering. They improve charge transport and stability. SAMs enable record efficiencies in tandem solar cells.\",\n  \"total_results\": 15,\n  \"api_params\": {\n    \"search_depth\": \"advanced\",\n    \"include_answer\": true,\n    \"include_raw_content\": \"markdown\",\n    \"max_results\": 20\n  },\n  \"top_documents\": [\n    {\n      \"url\": \"https://discovery.researcher.life/article/molecular-design-and-interfacial-functions-of-self-assembled-monolayers-for-perovskite-and-tandem-solar-cells/dadaee216a693bddad460a625fd298a6\",\n      \"title\": \"Molecular Design and Interfacial Functions of Self\\u2010Assembled Monolayers for Perovskite and Tandem Solar Cells\",\n      \"text\": \"[![Image 1: Discovery Logo menu](https://cdn.researcher.life/logos/discovery-by-editage.svg)](https://discovery.researcher.life/)\\n\\n[Sign In](https://sso.editage.com/login?continue=https%3A%2F%2Fdiscovery.researcher.life%2Farticle%2Fmolecular-design-and-interfacial-functions-of-self-assembled-monolayers-for- …[truncated]"
          },
          {
            "probe_id": "obs-32800",
            "similarity": 0.982,
            "task_text": "What is the PMID of the 2026 Journal of Clinical Medicine paper by Xu et al. on early precise prediction and severe risk stratification of intrahepatic cholestasis of pregnancy?",
            "adapted_input": "Xu et al 2026 Journal of Clinical Medicine intrahepatic cholestasis pregnancy early precise prediction severe risk stratification PMID",
            "score": 0,
            "redacted": null,
            "output_chars": 20000,
            "truncated": true,
            "created_at": "2026-08-29T11:45:01.942990Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "fail",
                "score": 0,
                "rationale": "Deterministic check — matched 0/1 required string(s); missing: 42589990.",
                "panel": null
              }
            ],
            "raw_output": "{\n  \"query\": \"Xu et al 2026 Journal of Clinical Medicine intrahepatic cholestasis pregnancy early precise prediction severe risk stratification PMID\",\n  \"adapted_query\": \"Xu et al 2026 Journal of Clinical Medicine intrahepatic cholestasis pregnancy early precise prediction severe risk stratification PMID\",\n  \"provider\": \"Tavily\",\n  \"answer\": \"Xu et al. 2026 in the Journal of Clinical Medicine developed a precise prediction model for early identification of severe risk in intrahepatic cholestasis of pregnancy. The study utilized clinical and laboratory indicators. PMID for the article is 41788159.\",\n  \"total_results\": 18,\n  \"api_params\": {\n    \"search_depth\": \"advanced\",\n    \"include_answer\": true,\n    \"include_raw_content\": \"markdown\",\n    \"max_results\": 20\n  },\n  \"top_documents\": [\n    {\n      \"url\": \"https://gorm.com.tr/index.php/GORM/article/download/1715/1150\",\n      \"title\": \"[PDF] 55 1715 G2025-023 Intrahepatic Cholestasis of Pregnancy_Layout 1\",\n      \"text\": \"55 Review Intrahepatic Cholestasis of Pregnancy: A Narrative Review Gorkem ARICA1, Ismail YILMAZ1, Dilek BULDUM1, Adil BARUT1, Riza MADAZLI1 Istanbul, T\\u00fcrkiye ABSTRACT This narrative review synthesizes current literature on the pathogenesis and management of Intrahepatic Cholestasis of Pregnancy (ICP). ICP is a multifactorial liver disorder. It is characterized by intense pruritus and elevated serum bile acids …[truncated]"
          }
        ]
      },
      "evidence_teaser": {
        "task_text": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
        "verdict": "present",
        "score": 0.933,
        "similarity": 0.983,
        "n_real": 906
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
      },
      "facets": [
        {
          "name": "capability",
          "kano": "must_be",
          "weight": 1,
          "threshold": 0.5,
          "raw": 0.5466,
          "contribution": 0.3653
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
        "n_real": 577,
        "n_near": 24,
        "near_mean": 0.814,
        "dist": [
          0.948,
          0.979,
          1,
          0.5,
          0.528,
          1,
          0,
          0,
          1,
          1,
          1,
          0.887,
          1,
          0.963,
          0.968,
          0.988,
          0.974,
          0.969,
          0,
          0.966,
          1,
          1,
          0.858,
          1
        ],
        "probes": [
          {
            "probe_id": "obs-42595",
            "similarity": 0.983,
            "task_text": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
            "adapted_input": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
            "score": 0.948,
            "redacted": null,
            "output_chars": 14137,
            "truncated": false,
            "created_at": "2026-10-08T06:27:34.238220Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 0.948,
                "rationale": "jev score 3.78/4 p=0.00/0.00/0.01/0.20/0.79 conf=0.82 | The answer correctly identifies the exact paper: 'Highly accurate protein structure prediction with  | The tool correctly identified the exact paper: 'Highly accurate protein structure prediction with Al",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev score 3.78/4 p=0.00/0.00/0.01/0.20/0.79 conf=0.82",
                    "score": 0.945
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The answer correctly identifies the exact paper: 'Highly accurate protein structure prediction with AlphaFold' by John Jumper et al., Nature 596(7873):583-589 (2021), with the correct DOI (10.1038/s41586-021-03819-2) and working links to the Nature article and PubMed record. It matches the ground tr…",
                    "score": 0.95
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The tool correctly identified the exact paper: 'Highly accurate protein structure prediction with AlphaFold' by Jumper et al., Nature 596(7873), 583–589 (2021), with the correct DOI (10.1038/s41586-021-03819-2) and direct links to the Nature article and correct PubMed record (34265844). It also adde…",
                    "score": 0.95
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "jev choice=excellent p{excellent=0.86, good=0.09, partial=0.05, irrelevant=0.00, poor=0.00} conf=0.82",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev choice=excellent p{excellent=0.86, good=0.09, partial=0.05, irrelevant=0.00, poor=0.00} conf=0.82",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The tool correctly identifies the exact AlphaFold 2 paper (Jumper et al., Nature 596:583-589, 2021) with the right DOI and high-quality sources (Nature, PubMed), directly answering the query intent.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The synthesized answer directly and correctly identifies the exact paper (Jumper et al., 'Highly accurate protein structure prediction with AlphaFold,' Nature 596:583–589, DOI 10.1038/s41586-021-03819-2) with authoritative Nature and PubMed links, and the top results are all closely relevant AlphaFo…",
                    "label": "excellent",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "jev choice=primary p{primary=1.00, tertiary=0.00, not_applicable=0.00, low_quality=0.00, reputable_secondary=0.00} conf=1.00",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev choice=primary p{primary=1.00, tertiary=0.00, not_applicable=0.00, low_quality=0.00, reputable_secondary=0.00} conf=1.00",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The citations include the Nature paper itself (nature.com/articles/s41586-021-03819-2), PubMed and PMC records, and other peer-reviewed journal articles, all of which are primary/authoritative sources.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The citations are dominated by primary, authoritative sources — the actual Nature paper (s41586-021-03819-2), PubMed/PMC records of peer-reviewed articles, PNAS, and DeepMind's official page — with no blogs or social media.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "jev choice=present p{present=1.00, implied=0.00, absent=0.00} conf=1.00",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev choice=present p{present=1.00, implied=0.00, absent=0.00} conf=1.00",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The output provides explicit followable references including the DOI (10.1038/s41586-021-03819-2) and URLs to the Nature article, PubMed record, and a list of citations.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The output contains multiple explicit source references, including the DOI (10.1038/s41586-021-03819-2), direct URLs to the Nature article and PubMed record, and a citations list of 15 URLs.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "jev choice=returned p{returned=1.00, empty=0.00} conf=1.00",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev choice=returned p{returned=1.00, empty=0.00} conf=1.00",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The tool produced a complete, non-empty answer identifying the AlphaFold 2 Nature paper with title, authors, journal details, DOI, and supporting citations.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The tool returned a non-empty, structured response containing an answer identifying the AlphaFold 2 Nature paper, along with citations and search results.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.\",\n  \"provider\": \"Perplexity Agent API (medium / deep-research preset; model openai/gpt-6-luna)\",\n  \"model_requested\": \"openai/gpt-6-luna\",\n  \"model_served\": \"openai/gpt-6-luna\",\n  \"tool_kind\": \"composite deep-research agent (multi-step search + LLM synthesis)\",\n  \"answer\": \"The paper is **\\u201cHighly accurate protein structure prediction with AlphaFold\\u201d** by John Jumper and colleagues, published in *Nature* **596**(7873), 583\\u2013589 (2021). DOI: [10.1038/s41586-021-03819-2](https://doi.org/10.1038/s41586-021-03819-2). [Nature article](https://www.nature.com/articles/s41586-021-03819-2) \\u00b7 [PubMed record](https://pubmed.ncbi.nlm.nih.gov/34265844/)\\n\\nThis is the AlphaFold 2 paper: the authors say their redesigned model competed with experimental structures in most CASP14 cases and greatly outperformed other methods. The paper reports median backbone accuracy of **0.96 \\u00c5 r.m.s.d.** for AlphaFold, compared with **2.8 \\u00c5** for the next-best method. [Nature article](https://www.nature.com/articles/s41586-021-03819-2)\",\n  \"citations\": [\n    \"https://pubmed.ncbi.nlm.nih.gov/34293799/\",\n    \"https://pmc.ncbi.nlm.nih.gov/articles/PMC8387240/\",\n    \"https://www.nature.com/articles/s41592-021-01380-4\",\n    \"https://ideas.repec.org/a/nat/nature/v596y …[truncated]"
          },
          {
            "probe_id": "obs-43138",
            "similarity": 0.978,
            "task_text": "Find the 1986 Nature paper by Rumelhart, Hinton and Williams that introduced back-propagation for training multi-layer neural networks.",
            "adapted_input": "Find the 1986 Nature paper by Rumelhart, Hinton and Williams that introduced back-propagation for training multi-layer neural networks.",
            "score": 0.979,
            "redacted": null,
            "output_chars": 13287,
            "truncated": false,
            "created_at": "2026-10-08T14:36:02.698809Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 0.979,
                "rationale": "jev score 3.95/4 p=0.00/0.00/0.00/0.04/0.96 conf=0.96 | The tool correctly identified the paper 'Learning representations by back-propagating errors' by Rum | The tool returned exactly the expected paper with all key fields matching ground truth: title ('Lear",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev score 3.95/4 p=0.00/0.00/0.00/0.04/0.96 conf=0.96",
                    "score": 0.988
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The tool correctly identified the paper 'Learning representations by back-propagating errors' by Rumelhart, Hinton, and Williams, published in Nature 323, 533–536 (1986), with the correct DOI (10.1038/323533a0) and URL. All ground-truth elements—title, authors, year, venue, and persistent identifier…",
                    "score": 1
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The tool returned exactly the expected paper with all key fields matching ground truth: title ('Learning representations by back-propagating errors'), full author list (Rumelhart, Hinton, Williams), year (1986), venue and volume/pages (Nature 323, 533–536), and the persistent identifier (DOI 10.1038…",
                    "score": 0.95
                  }
                ]
              },
              {
                "facet": "format",
                "verdict": "structured",
                "score": 1,
                "rationale": "jev choice=structured p{structured=0.60, semi_structured=0.36, unstructured=0.04} conf=0.40",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev choice=structured p{structured=0.60, semi_structured=0.36, unstructured=0.04} conf=0.40",
                    "label": "structured",
                    "value": 1
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The tool returned valid JSON with all expected fields populated, including an answer, a citations list, and search_results entries each containing title, URL, and snippet, making it fully machine-parseable.",
                    "label": "structured",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The tool returns a valid JSON object with populated fields (query, answer, citations, and search_results each containing title/URL/snippet), making it fully machine-parseable.",
                    "label": "structured",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "freshness",
                "verdict": "not_applicable",
                "score": 1,
                "rationale": "jev choice=not_applicable p{not_applicable=0.99, current=0.01, slightly_stale=0.00, stale=0.00} conf=0.99",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev choice=not_applicable p{not_applicable=0.99, current=0.01, slightly_stale=0.00, stale=0.00} conf=0.99",
                    "label": "not_applicable",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The query concerns a static historical fact (a 1986 Nature paper), so the currency of the evidence is irrelevant to correctness.",
                    "label": "not_applicable",
                    "value": 1
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The query asks about a fixed historical fact (the 1986 Nature back-propagation paper), whose title, authors, year, and DOI do not change over time, so freshness of the result is irrelevant to judging correctness.",
                    "label": "not_applicable",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "jev choice=excellent p{excellent=1.00, irrelevant=0.00, partial=0.00, good=0.00, poor=0.00} conf=1.00",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev choice=excellent p{excellent=1.00, irrelevant=0.00, partial=0.00, good=0.00, poor=0.00} conf=1.00",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The tool's top results directly surface the exact 1986 Nature paper with correct title, authors, year, volume/pages, DOI, and URL, fully answering the query intent.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The top result is the exact Nature page for 'Learning representations by back-propagating errors' (Nature 323, 533–536, 1986, DOI 10.1038/323533a0), and the answer correctly identifies the title, all three authors, year, venue, and persistent identifier, directly and fully satisfying the query inten…",
                    "label": "excellent",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "jev choice=primary p{primary=1.00, not_applicable=0.00, reputable_secondary=0.00, tertiary=0.00, low_quality=0.00} conf=1.00",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev choice=primary p{primary=1.00, not_applicable=0.00, reputable_secondary=0.00, tertiary=0.00, low_quality=0.00} conf=1.00",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The citations are led by the Nature article page itself (the peer-reviewed 1986 paper) and include academic sources like Semantic Scholar, ACM Digital Library, and PNAS, making the cited sources predominantly primary/authoritative.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The tool's citations center on the peer-reviewed Nature paper itself (nature.com article page and DOI 10.1038/323533a0), which is a primary source, with supporting academic indexes like Semantic Scholar.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "snippet_quality",
                "verdict": "informative",
                "score": 1,
                "rationale": "jev choice=informative p{informative=1.00, absent=0.00, generic=0.00} conf=1.00",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev choice=informative p{informative=1.00, absent=0.00, generic=0.00} conf=1.00",
                    "label": "informative",
                    "value": 1
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The snippets include the paper's abstract text plus full citation details (authors, Nature volume 323, pages 533–536, year 1986, and DOI), providing specific facts that let a reader assess relevance without clicking through.",
                    "label": "informative",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The snippets include the paper's abstract text plus full citation details (authors, journal, volume, pages, year, DOI), giving enough specific facts to assess relevance without clicking through.",
                    "label": "informative",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "jev choice=present p{present=1.00, implied=0.00, absent=0.00} conf=1.00",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev choice=present p{present=1.00, implied=0.00, absent=0.00} conf=1.00",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The output explicitly includes a Nature article URL, a DOI link (10.1038/323533a0), and a citations array with 15 source URLs, all of which a reader can follow back to the underlying material.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The output includes explicit followable references such as the Nature article URL, the DOI link, and a list of citations.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "jev choice=returned p{returned=1.00, empty=0.00} conf=1.00",
                "panel": [
                  {
                    "model": "typesafe/jev-1.13.0",
                    "rationale": "jev choice=returned p{returned=1.00, empty=0.00} conf=1.00",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "z-ai/glm-5.3-flash",
                    "rationale": "The tool returned a complete, non-empty response including an answer identifying the paper, citations, and search results, so usable output was clearly returned.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4.1-flash",
                    "rationale": "The tool produced a complete non-empty answer identifying the paper's title, authors, year, venue, and DOI.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find the 1986 Nature paper by Rumelhart, Hinton and Williams that introduced back-propagation for training multi-layer neural networks.\",\n  \"provider\": \"Perplexity Agent API (medium / deep-research preset; model openai/gpt-6-luna)\",\n  \"model_requested\": \"openai/gpt-6-luna\",\n  \"model_served\": \"openai/gpt-6-luna\",\n  \"tool_kind\": \"composite deep-research agent (multi-step search + LLM synthesis)\",\n  \"answer\": \"The paper is **\\u201cLearning representations by back-propagating errors\\u201d** by David E. Rumelhart, Geoffrey E. Hinton, and Ronald J. Williams, published in *Nature* **323**, 533\\u2013536 (1986).\\n\\n[Read the paper\\u2019s Nature page](https://www.nature.com/articles/323533a0) \\u00b7 [DOI: 10.1038/323533a0](https://doi.org/10.1038/323533a0)\\n\\nNature\\u2019s abstract describes back-propagation as a procedure for adjusting network connection weights so hidden units learn useful representations. **Historical note:** the paper is a landmark account of the method, but back-propagation had been explored in earlier work. ([Nature](https://www.nature.com/articles/323533a0))\",\n  \"citations\": [\n    \"https://www.nature.com/articles/323533a0\",\n    \"https://www.semanticscholar.org/paper/Learning-representations-by-back-propagating-errors-Rumelhart-Hinton/052b1d8ce63b07fec3de9dbb583772d860b7c769\",\n    \"https://papernex.us/paper/01cLHi\",\n    \"https://www.centerconsulting.c …[truncated]"
          },
          {
            "probe_id": "obs-43060",
            "similarity": 0.975,
            "task_text": "Find the August 2026 Diabetes, Obesity & Metabolism paper by Liao et al. asking whether more treatment translates to better outcomes for continuous glucose monitoring in gestational diabetes. PMID please.",
            "adapted_input": "Find the August 2026 Diabetes, Obesity & Metabolism paper by Liao et al. asking whether more treatment translates to better outcomes for continuous glucose monitoring in gestational diabetes. PMID please.",
            "score": 1,
            "redacted": null,
            "output_chars": 20000,
            "truncated": true,
            "created_at": "2026-10-08T13:21:35.724816Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "Deterministic check — matched 1/1 required string(s).",
                "panel": null
              }
            ],
            "raw_output": "{\n  \"query\": \"Find the August 2026 Diabetes, Obesity & Metabolism paper by Liao et al. asking whether more treatment translates to better outcomes for continuous glucose monitoring in gestational diabetes. PMID please.\",\n  \"provider\": \"Perplexity Agent API (medium / deep-research preset; model openai/gpt-6-luna)\",\n  \"model_requested\": \"openai/gpt-6-luna\",\n  \"model_served\": \"openai/gpt-6-luna\",\n  \"tool_kind\": \"composite deep-research agent (multi-step search + LLM synthesis)\",\n  \"answer\": \"The PMID is **42642349**. The PubMed record lists the article by Jie Liao, Qinqin Yuan, and Yanmei Xia, published online August 25, 2026, with DOI [10.1111/dom.71282](https://pubmed.ncbi.nlm.nih.gov/?term=10.1111%2Fdom.71282).\",\n  \"citations\": [\n    \"https://pubmed.ncbi.nlm.nih.gov/41178671/\",\n    \"https://amedeo.com/medicine/diab/j1307.htm\",\n    \"https://pubmed.ncbi.nlm.nih.gov/41421368/\",\n    \"https://pubmed.ncbi.nlm.nih.gov/42015100/\",\n    \"https://pubmed.ncbi.nlm.nih.gov/41505847/\",\n    \"https://pubmed.ncbi.nlm.nih.gov/42631793/\",\n    \"https://link.springer.com/journal/11154/articles?error=cookies_not_supported&code=1ae30208-1daa-4362-a411-7140af860d4c\",\n    \"https://assets.ctfassets.net/1p0t6jhbvwk9/6oPIxOGohAzlVs78UWPIw3/0635cd12d4a0767c22f9064ab9278e9a/MCT2D_GDM_2026_final.pdf\",\n    \"https://pmc.ncbi.nlm.nih.gov/articles/PMC13556021/\",\n    \"https://pmc.ncbi.nlm.nih.gov/articles/PMC13448 …[truncated]"
          }
        ]
      },
      "evidence_teaser": {
        "task_text": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
        "verdict": "present",
        "score": 0.948,
        "similarity": 0.983,
        "n_real": 577
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
          "raw": 0.3417,
          "contribution": 0.205
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
        "n_real": 165,
        "n_near": 24,
        "near_mean": 0.819,
        "dist": [
          0.983,
          1,
          1,
          0,
          1,
          1,
          1,
          0.983,
          1,
          0.96,
          1,
          1,
          1,
          1,
          0,
          1,
          1,
          0.233,
          1,
          0.5,
          1,
          0,
          1,
          1
        ],
        "probes": [
          {
            "probe_id": "obs-7286",
            "similarity": 0.983,
            "task_text": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
            "adapted_input": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
            "score": 0.983,
            "redacted": null,
            "output_chars": 19508,
            "truncated": false,
            "created_at": "2026-05-23T21:36:21.759814Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 0.983,
                "rationale": "The tool successfully identified the exact canonical paper requested. The first result in the list m | The tool correctly identified the canonical DeepMind 2021 Nature paper (PMID 34265844, DOI 10.1038/s | The tool's top result exactly matches the ground truth paper in title, authors, year, and DOI, provi",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool successfully identified the exact canonical paper requested. The first result in the list matches the title, authors (Jumper J et al.), year (2021), and DOI/PMID of the ground truth paper. The tool's adapted query was effective and the metadata provided is complete and accurate.",
                    "score": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool correctly identified the canonical DeepMind 2021 Nature paper (PMID 34265844, DOI 10.1038/s41586-021-03819-2) as the top result, with exact title, authors, year, and abstract matching the ground truth. The adapted query was appropriate, and the result was returned with correct identifiers a…",
                    "score": 0.95
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's top result exactly matches the ground truth paper in title, authors, year, and DOI, providing accurate and complete metadata as per the API's intended function, with no irrelevant records or fabricated identifiers.",
                    "score": 1
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "The first result is the exact paper requested by the user, including the correct title, authors, year, and DOI.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The first result is the exact paper requested by the user, including the correct title, authors, year, and DOI.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The top result is the exact AlphaFold 2 Nature paper from 2021, directly matching the query intent with high relevance and quality.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The first result directly matches the ground truth paper, but the other top results are relevant to protein structure prediction yet not the specific AlphaFold 2 announcement, making the overall relevance useful but not perfectly targeted.",
                    "label": "good",
                    "value": 0.75
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool provides citations to peer-reviewed scientific papers from PubMed/Europe PMC, which are primary sources.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides citations to peer-reviewed scientific papers from PubMed/Europe PMC, which are primary sources.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output directly returns a peer-reviewed Nature paper (PMID 34265844) from 2021, which is a primary authoritative source for the query.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output cites peer-reviewed papers, such as the Jumper et al. 2021 Nature paper, which are primary sources according to the rubric.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool output provides explicit source references including PMIDs, PMCIDs, and DOIs for the search results.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool output provides explicit source references including PMIDs, PMCIDs, and DOIs for the search results.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The output includes explicit DOIs, PMIDs, and other identifiers for the papers, allowing direct access to the underlying material.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output includes explicit source references such as DOI, PMID, and PMCIDs for each paper, which are specific identifiers that a reader can follow to access the underlying material.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool returned a JSON object containing a list of search results, including the specific paper requested.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned a JSON object containing a list of search results, including the specific paper requested.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a list of 30 results, including the correct AlphaFold paper, so it produced non-empty output.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output provides a detailed JSON response with multiple search results, confirming that non-empty output was returned.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.\",\n  \"adapted_query\": \"AlphaFold protein structure PUB_YEAR:2021\",\n  \"provider\": \"Europe PMC\",\n  \"tool_kind\": \"life-science literature search (papers + preprints + OA full text)\",\n  \"total_results\": 507,\n  \"returned_results\": 30,\n  \"results\": [\n    {\n      \"id\": \"34265844\",\n      \"source\": \"MED\",\n      \"pmid\": \"34265844\",\n      \"pmcid\": \"PMC8371605\",\n      \"doi\": \"10.1038/s41586-021-03819-2\",\n      \"title\": \"Highly accurate protein structure prediction with AlphaFold.\",\n      \"authors\": \"Jumper J, Evans R, Pritzel A, Green T, Figurnov M, Ronneberger O, Tunyasuvunakool K, Bates R, \\u017d\\u00eddek A, Potapenko A, Bridgland A, Meyer C, Kohl SAA, Ballard AJ, Cowie A, Romera-Paredes B, Nikolov S, Jain R, Adler J, Back T, Petersen S, Reiman D, Clancy E, Zielinski M, Steinegger M, Pacholska M, Berghammer T, Bodenstein S, Silver D, Vinyals O, Senior AW, Kavukcuoglu K, Kohli P, Hassabis D.\",\n      \"journal\": null,\n      \"publication_year\": \"2021\",\n      \"publication_type\": null,\n      \"cited_by_count\": 31765,\n      \"is_open_access\": true,\n      \"abstract\": \"Proteins are essential to life, and understanding their structure can facilitate a mechanistic understanding of their function. Through an enormous experimental effort<sup>1-4</sup>, the structures of around 100,000 …[truncated]"
          },
          {
            "probe_id": "obs-20024",
            "similarity": 0.983,
            "task_text": "Find Anzalone et al. 2019 Nature paper on prime editing: search-and-replace genome editing without double-strand breaks or donor DNA.",
            "adapted_input": "Find Anzalone et al. 2019 Nature paper on prime editing: search-and-replace genome editing without double-strand breaks or donor DNA.",
            "score": 1,
            "redacted": null,
            "output_chars": 1566,
            "truncated": false,
            "created_at": "2026-07-05T09:19:32.979025Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "Deterministic check — matched 3/3 required string(s).",
                "panel": null
              }
            ],
            "raw_output": "{\n  \"query\": \"Find Anzalone et al. 2019 Nature paper on prime editing: search-and-replace genome editing without double-strand breaks or donor DNA.\",\n  \"adapted_query\": \"AUTH:\\\"Anzalone\\\" PUB_YEAR:2019 prime editing genome\",\n  \"provider\": \"Europe PMC\",\n  \"tool_kind\": \"life-science literature search (papers + preprints + OA full text)\",\n  \"total_results\": 1,\n  \"returned_results\": 1,\n  \"results\": [\n    {\n      \"id\": \"31634902\",\n      \"source\": \"MED\",\n      \"pmid\": \"31634902\",\n      \"pmcid\": \"PMC6907074\",\n      \"doi\": \"10.1038/s41586-019-1711-4\",\n      \"title\": \"Search-and-replace genome editing without double-strand breaks or donor DNA.\",\n      \"authors\": \"Anzalone AV, Randolph PB, Davis JR, Sousa AA, Koblan LW, Levy JM, Chen PJ, Wilson C, Newby GA, Raguram A, Liu DR.\",\n      \"journal\": null,\n      \"publication_year\": \"2019\",\n      \"publication_type\": null,\n      \"cited_by_count\": 3370,\n      \"is_open_access\": true,\n      \"abstract\": \"Most genetic variants that contribute to disease<sup>1</sup> are challenging to correct efficiently and without excess byproducts<sup>2-5</sup>. Here we describe prime editing, a versatile and precise genome editing method that directly writes new genetic information into a specified DNA site using a catalytically impaired Cas9 endonuclease fused to an engineered reverse transcriptase, programmed with a prime editing guide RNA (pegRNA) that both spe …[truncated]"
          },
          {
            "probe_id": "obs-32793",
            "similarity": 0.982,
            "task_text": "What is the PMID of the 2026 Journal of Clinical Medicine paper by Xu et al. on early precise prediction and severe risk stratification of intrahepatic cholestasis of pregnancy?",
            "adapted_input": "What is the PMID of the 2026 Journal of Clinical Medicine paper by Xu et al. on early precise prediction and severe risk stratification of intrahepatic cholestasis of pregnancy?",
            "score": 1,
            "redacted": null,
            "output_chars": 7233,
            "truncated": false,
            "created_at": "2026-08-29T11:39:48.167254Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "Deterministic check — matched 1/1 required string(s).",
                "panel": null
              }
            ],
            "raw_output": "{\n  \"query\": \"What is the PMID of the 2026 Journal of Clinical Medicine paper by Xu et al. on early precise prediction and severe risk stratification of intrahepatic cholestasis of pregnancy?\",\n  \"adapted_query\": \"AUTH:\\\"Xu\\\" PUB_YEAR:2026 intrahepatic cholestasis pregnancy prediction\",\n  \"provider\": \"Europe PMC\",\n  \"tool_kind\": \"life-science literature search (papers + preprints + OA full text)\",\n  \"total_results\": 9,\n  \"returned_results\": 9,\n  \"results\": [\n    {\n      \"id\": \"41864912\",\n      \"source\": \"MED\",\n      \"pmid\": \"41864912\",\n      \"pmcid\": \"PMC13130792\",\n      \"doi\": \"10.1186/s12916-026-04794-z\",\n      \"title\": \"Artificial intelligence-based prediction of fetal hypoxia: a multicenter model development and nationwide AI-human comparison.\",\n      \"authors\": \"Lin S, Di X, Yao M, Xu Y, Wei H, Shi Z, Hao R, Wu N, Wang D, Wang Z, Liu B.\",\n      \"journal\": null,\n      \"publication_year\": \"2026\",\n      \"publication_type\": null,\n      \"cited_by_count\": 1,\n      \"is_open_access\": true,\n      \"abstract\": \"<h4>Background</h4>Fetal hypoxia is a leading cause of neonatal morbidity and mortality. Cardiotocography (CTG) is widely used to predict fetal hypoxia during labor, but its interpretation remains suboptimal. Artificial intelligence (AI) models have been developed for CTG interpretation, but their clinical utility is limited by two major challenges: demonstrating superiority o …[truncated]"
          }
        ]
      },
      "evidence_teaser": {
        "task_text": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
        "verdict": "present",
        "score": 0.983,
        "similarity": 0.983,
        "n_real": 165
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
      },
      "facets": [
        {
          "name": "capability",
          "kano": "must_be",
          "weight": 1,
          "threshold": 0.5,
          "raw": 0.1526,
          "contribution": 0.0916
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
        "n_real": 153,
        "n_near": 24,
        "near_mean": 0.631,
        "dist": [
          0.267,
          0.833,
          0.733,
          0.6,
          1,
          0.333,
          1,
          1,
          0.867,
          0.171,
          0.333,
          0.167,
          0,
          1,
          0.983,
          0,
          0.367,
          0,
          0.867,
          0.733,
          1,
          0.933,
          0.983,
          0.967
        ],
        "probes": [
          {
            "probe_id": "obs-19860",
            "similarity": 0.987,
            "task_text": "find recent physics preprints on quantum error correction",
            "adapted_input": "quantum error correction 2025 2026",
            "score": 0.267,
            "redacted": null,
            "output_chars": 20000,
            "truncated": true,
            "created_at": "2026-07-05T09:11:34.308144Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "fail",
                "score": 0.267,
                "rationale": "The tool failed significantly on the 'recent' constraint. The user requested recent preprints, but t | The tool returned preprints on quantum error correction but none are recent (all from 2003–2016), fa | The tool returned relevant papers on quantum error correction with structured metadata (titles, auth",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool failed significantly on the 'recent' constraint. The user requested recent preprints, but the tool's adapted query ('quantum error correction 2025 2026') resulted in papers from 2003, 2006, 2013, and 2016. This suggests the tool's internal logic for handling temporal queries is broken, as i…",
                    "score": 0.2
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned preprints on quantum error correction but none are recent (all from 2003–2016), failing the query's explicit 'recent' requirement. While the metadata is accurate for those papers, the lack of recency makes the output largely irrelevant to the user's request.",
                    "score": 0.2
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned relevant papers on quantum error correction with structured metadata (titles, authors, abstracts, dates), but failed to provide recent preprints as specified in the query. The results include older papers from 2003-2016, not aligning with the 'recent' requirement, and the adapted q…",
                    "score": 0.4
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"find recent physics preprints on quantum error correction\",\n  \"adapted_query\": \"quantum error correction 2025 2026\",\n  \"provider\": \"arXiv (export.arxiv.org)\",\n  \"tool_kind\": \"academic paper search (STEM/CS/physics/math)\",\n  \"total_results\": 1090438,\n  \"returned_results\": 15,\n  \"results\": [\n    {\n      \"arxiv_id\": \"1311.2485v2\",\n      \"title\": \"Continuous-time quantum error correction\",\n      \"abstract\": \"Continuous-time quantum error correction (CTQEC) is an approach to protecting quantum information from noise in which both the noise and the error correcting operations are treated as processes that are continuous in time. This chapter investigates CTQEC based on continuous weak measurements and feedback from the point of view of the subsystem principle, which states that protected quantum information is contained in a subsystem of the Hilbert space. We study how to approach the problem of constructing CTQEC protocols by looking at the evolution of the state of the system in an encoded basis in which the subsystem containing the protected information is explicit. This point of view allows us to reduce the problem to that of protecting a known state, and to design CTQEC procedures from protocols for the protection of a single qubit. We show how previously studied CTQEC schemes with both direct and indirect feedback can be obtained from strategies for the protection …[truncated]"
          },
          {
            "probe_id": "obs-20502",
            "similarity": 0.985,
            "task_text": "find arXiv preprints on reinforcement learning from human feedback for language models",
            "adapted_input": "RLHF language models reinforcement learning human feedback",
            "score": 0.833,
            "redacted": null,
            "output_chars": 20000,
            "truncated": true,
            "created_at": "2026-07-05T09:51:43.968950Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 0.833,
                "rationale": "The tool successfully interpreted the query and provided highly relevant arXiv preprints specificall | The tool returned multiple relevant arXiv preprints on RLHF for language models, with correct metada | The tool returned relevant RLHF papers with correct metadata (titles, authors, abstracts, dates), sh",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool successfully interpreted the query and provided highly relevant arXiv preprints specifically focused on RLHF for language models (e.g., 'RRHF: Rank Responses to Align Language Models with Human Feedback'). The results include all required metadata (title, authors, abstract, ID). The output …",
                    "score": 0.9
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned multiple relevant arXiv preprints on RLHF for language models, with correct metadata (title, authors, date, abstract), matching the query intent. The results are highly relevant and accurate, though the total_results count appears inflated, which does not affect the quality of the …",
                    "score": 0.9
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned relevant RLHF papers with correct metadata (titles, authors, abstracts, dates), showing good relevance and accuracy. However, it did not include the canonical InstructGPT paper (e.g., 2203.02155) in the top results shown, which is mentioned in the ground truth, indicating a gap in …",
                    "score": 0.7
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "The top results are highly relevant, specifically addressing RLHF and language model alignment as requested in the query.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The top results are highly relevant, specifically addressing RLHF and language model alignment as requested in the query.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The top two results are directly about RLHF for language models, matching the query intent precisely.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The top results are directly about reinforcement learning from human feedback for language models, which perfectly matches the query intent.",
                    "label": "excellent",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool provides citations to arXiv preprints, which are primary scientific research papers.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides citations to arXiv preprints, which are primary scientific research papers.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The arXiv tool returns academic preprints, which are peer-reviewed primary sources.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returns arXiv preprint papers, which are primary sources as they represent original research outputs in academic contexts.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool output includes explicit URLs (e.g., http://arxiv.org/abs/2308.04332v1) and arXiv IDs for the retrieved papers.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool output includes explicit URLs (e.g., http://arxiv.org/abs/2308.04332v1) and arXiv IDs for the retrieved papers.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The output includes explicit URLs (e.g., http://arxiv.org/abs/2308.04332v1) for each arXiv preprint, which are direct references a reader can follow.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The output includes explicit URLs in the 'url' field for each paper, such as http://arxiv.org/abs/2308.04332v1, which are direct references to the underlying material.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool returned a JSON object containing a list of search results with relevant arXiv paper details.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned a JSON object containing a list of search results with relevant arXiv paper details.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a JSON object with 15 results containing titles, authors, and abstracts, so output is non-empty.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool output is a non-empty JSON structure with detailed search results, including titles, abstracts, and metadata, indicating usable output was returned.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"find arXiv preprints on reinforcement learning from human feedback for language models\",\n  \"adapted_query\": \"RLHF language models reinforcement learning human feedback\",\n  \"provider\": \"arXiv (export.arxiv.org)\",\n  \"tool_kind\": \"academic paper search (STEM/CS/physics/math)\",\n  \"total_results\": 1441023,\n  \"returned_results\": 15,\n  \"results\": [\n    {\n      \"arxiv_id\": \"2308.04332v1\",\n      \"title\": \"RLHF-Blender: A Configurable Interactive Interface for Learning from Diverse Human Feedback\",\n      \"abstract\": \"To use reinforcement learning from human feedback (RLHF) in practical applications, it is crucial to learn reward models from diverse sources of human feedback and to consider human factors involved in providing feedback of different types. However, the systematic study of learning from diverse types of feedback is held back by limited standardized tooling available to researchers. To bridge this gap, we propose RLHF-Blender, a configurable, interactive interface for learning from human feedback. RLHF-Blender provides a modular experimentation framework and implementation that enables researchers to systematically investigate the properties and qualities of human feedback for reward learning. The system facilitates the exploration of various feedback types, including demonstrations, rankings, comparisons, and natural language instructions, as well as studies co …[truncated]"
          },
          {
            "probe_id": "obs-20216",
            "similarity": 0.981,
            "task_text": "find arXiv preprints on selective state space models for sequence modeling",
            "adapted_input": "selective state space Mamba sequence modeling",
            "score": 0.733,
            "redacted": null,
            "output_chars": 20000,
            "truncated": true,
            "created_at": "2026-07-05T09:35:18.168191Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 0.733,
                "rationale": "The tool successfully interpreted the query by adapting it to more effective search terms ('selectiv | The tool returned relevant results related to selective state space models (Mamba), but the canonica | The tool returned relevant structured records on selective state space models for sequence modeling,",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool successfully interpreted the query by adapting it to more effective search terms ('selective state space Mamba sequence modeling'). It returned highly relevant, high-quality results that directly address the user's request for selective state space models (specifically Mamba) for sequence m…",
                    "score": 0.9
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned relevant results related to selective state space models (Mamba), but the canonical Mamba paper (2312.00752) is missing from the top results. The total_results count is implausibly high (1.8M), suggesting a query adaptation or API issue. The output is partially relevant but has sig…",
                    "score": 0.4
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned relevant structured records on selective state space models for sequence modeling, specifically papers on Mamba and related topics, with correct titles, authors, abstracts, and identifiers as per the arXiv API contract. The query was adapted appropriately, and the results align wit…",
                    "score": 0.9
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "The top results are highly relevant, specifically addressing selective state space models (Mamba) in the context of sequence modeling and related tasks.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The top results are highly relevant, specifically addressing selective state space models (Mamba) in the context of sequence modeling and related tasks.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The top result focuses on few-shot class-incremental learning rather than sequence modeling, while the second result is relevant, so the mix of off-topic content makes the results only partially aligned with the query intent.",
                    "label": "partial",
                    "value": 0.5
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The top results are directly about selective state space models like Mamba for sequence modeling, providing relevant and high-quality sources from arXiv.",
                    "label": "excellent",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool provides citations to arXiv preprints, which are primary academic research papers/records in the STEM fields.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides citations to arXiv preprints, which are primary academic research papers/records in the STEM fields.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returns citations to arXiv preprints, which are peer-reviewed academic papers, a primary source.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output provides arXiv preprints, which are primary source scholarly papers.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool output provides explicit URLs (e.g., http://arxiv.org/abs/2407.06136v4) and arXiv IDs for the retrieved papers.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool output provides explicit URLs (e.g., http://arxiv.org/abs/2407.06136v4) and arXiv IDs for the retrieved papers.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool's output includes explicit source references for each result, such as arXiv IDs (e.g., 2407.06136v4) and URLs (e.g., http://arxiv.org/abs/2407.06136v4), which allow a reader to directly access the underlying preprints.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output includes explicit URLs in the results that directly link to arXiv preprint pages, providing clear source references for follow-up.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool returned a structured JSON object containing a list of relevant arXiv preprint results including titles, abstracts, and IDs.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned a structured JSON object containing a list of relevant arXiv preprint results including titles, abstracts, and IDs.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a JSON object with a non-empty results array containing 15 entries, so output was returned.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool output is a non-empty JSON structure with multiple results, including titles and abstracts, confirming that usable output was returned.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"find arXiv preprints on selective state space models for sequence modeling\",\n  \"adapted_query\": \"selective state space Mamba sequence modeling\",\n  \"provider\": \"arXiv (export.arxiv.org)\",\n  \"tool_kind\": \"academic paper search (STEM/CS/physics/math)\",\n  \"total_results\": 1871677,\n  \"returned_results\": 15,\n  \"results\": [\n    {\n      \"arxiv_id\": \"2407.06136v4\",\n      \"title\": \"Mamba-FSCIL: Dynamic Adaptation with Selective State Space Model for Few-Shot Class-Incremental Learning\",\n      \"abstract\": \"Few-shot class-incremental learning (FSCIL) aims to incrementally learn novel classes from limited examples while preserving knowledge of previously learned classes. Existing methods face a critical dilemma: static architectures rely on a constant parameter space to learn from data that arrive sequentially, making them prone to overfitting to the current session, while dynamic architectures continually expand the parameter space, leading to increased complexity. In this study, we explore the potential of Selective State Space Models (SSMs) for FSCIL. Mamba leverages its input-dependent parameters to dynamically adjust its processing patterns and generate content-aware scan patterns without session-wise projector expansion. This enables it to configure distinct processing for base and novel classes, helping preserve existing knowledge while adapting to new ones. To leverage …[truncated]"
          }
        ]
      },
      "evidence_teaser": {
        "task_text": "find recent physics preprints on quantum error correction",
        "verdict": "fail",
        "score": 0.267,
        "similarity": 0.987,
        "n_real": 153
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
      },
      "facets": [
        {
          "name": "capability",
          "kano": "must_be",
          "weight": 1,
          "threshold": 0.5,
          "raw": 0.1523,
          "contribution": 0.0914
        },
        {
          "name": "price",
          "kano": "performance",
          "weight": 0.3,
          "threshold": 0.5,
          "raw": 0.9928,
          "contribution": 0.2978
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
        "n_real": 847,
        "n_near": 24,
        "near_mean": 0.608,
        "dist": [
          1,
          1,
          0,
          0,
          0,
          0,
          0,
          0,
          0.967,
          1,
          0.967,
          0.967,
          0.95,
          0.983,
          0.95,
          0.95,
          0.952,
          0.933,
          0.931,
          0.95,
          0,
          0.5,
          0.333,
          0.267
        ],
        "probes": [
          {
            "probe_id": "obs-5266",
            "similarity": 0.983,
            "task_text": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
            "adapted_input": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
            "score": 1,
            "redacted": null,
            "output_chars": 11599,
            "truncated": false,
            "created_at": "2026-05-21T12:13:33.290511Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "The tool provided the exact canonical source requested in the very first result: 'Highly accurate pr | The tool returned the exact canonical Nature paper as the first result, with the correct title, URL, | The tool returned the canonical Nature paper (https://www.nature.com/articles/s41586-021-03819-2) as",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provided the exact canonical source requested in the very first result: 'Highly accurate protein structure prediction with AlphaFold | Nature' with the correct URL (https://www.nature.com/articles/s41586-021-03819-2). It also provided supplementary results from PubMed and DeepMind that conf…",
                    "score": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned the exact canonical Nature paper as the first result, with the correct title, URL, and relevant snippet. Other results (DeepMind official site, PubMed, Wikipedia) provide diverse authoritative sources. The output perfectly addresses the query and matches the ground truth.",
                    "score": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned the canonical Nature paper (https://www.nature.com/articles/s41586-021-03819-2) as the top result, directly matching the ground truth citation, and provided a diverse set of relevant sources including DeepMind, PubMed, and Wikipedia. All URLs are legitimate and on-topic, fully addr…",
                    "score": 1
                  }
                ]
              },
              {
                "facet": "relevance",
                "verdict": "excellent",
                "score": 1,
                "rationale": "The top result is the exact Nature paper requested, and the subsequent results provide direct confirmation and citations for the specific paper and authors.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The top result is the exact Nature paper requested, and the subsequent results provide direct confirmation and citations for the specific paper and authors.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The top 3 results include the exact Nature paper, DeepMind's official page, and PubMed entry, all directly addressing the query with high-quality sources.",
                    "label": "excellent",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The top results directly include the exact 2021 Nature paper from high-quality sources like Nature and PubMed, immediately answering the query intent.",
                    "label": "excellent",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "source_quality",
                "verdict": "primary",
                "score": 1,
                "rationale": "The tool provides direct links to the peer-reviewed paper in Nature and its corresponding entries in PubMed and PMC, which are primary scientific sources.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool provides direct links to the peer-reviewed paper in Nature and its corresponding entries in PubMed and PMC, which are primary scientific sources.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The output lists the original Nature paper (a peer-reviewed primary source) as the top result, along with other authoritative databases like PubMed.",
                    "label": "primary",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool's output includes direct links to the peer-reviewed Nature paper, which is a primary source.",
                    "label": "primary",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "references_present",
                "verdict": "present",
                "score": 1,
                "rationale": "The tool output provides multiple explicit source references, including URLs, document titles, and specific journal citations.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool output provides multiple explicit source references, including URLs, document titles, and specific journal citations.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool output provides multiple explicit source references including URLs, source names, and citation markers such as 'Nature 2021, 596, 583–589'.",
                    "label": "present",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The output includes multiple explicit URLs and document names for each search result, such as the Nature paper URL, which serve as direct source references.",
                    "label": "present",
                    "value": 1
                  }
                ]
              },
              {
                "facet": "output_was_returned",
                "verdict": "returned",
                "score": 1,
                "rationale": "The tool returned a list of search results containing the requested information, including the specific Nature paper title and citation details.",
                "panel": [
                  {
                    "model": "google/gemma-4-26b-a4b-it",
                    "rationale": "The tool returned a list of search results containing the requested information, including the specific Nature paper title and citation details.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "deepseek/deepseek-v4-flash",
                    "rationale": "The tool returned a list of search results, including the Nature paper, so it provided non-empty output.",
                    "label": "returned",
                    "value": 1
                  },
                  {
                    "model": "xiaomi/mimo-v2.5",
                    "rationale": "The tool returned a non-empty JSON object with multiple search results, providing usable output regardless of correctness.",
                    "label": "returned",
                    "value": 1
                  }
                ]
              }
            ],
            "raw_output": "{\n  \"query\": \"Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.\",\n  \"provider\": \"Brave Search\",\n  \"total_results\": 20,\n  \"api_params\": {\n    \"count\": 20\n  },\n  \"results\": [\n    {\n      \"title\": \"Highly accurate protein structure prediction with AlphaFold | Nature\",\n      \"url\": \"https://www.nature.com/articles/s41586-021-03819-2\",\n      \"snippet\": \"Nature - <strong>AlphaFold predicts protein structures with an accuracy competitive with experimental structures in the majority of cases using a novel deep learning architecture</strong>.\",\n      \"age\": \"July 15, 2021\",\n      \"source\": \"Nature\"\n    },\n    {\n      \"title\": \"AlphaFold \\u2014 Google DeepMind\",\n      \"url\": \"https://deepmind.google/science/alphafold/\",\n      \"snippet\": \"... Nature publishes AlphaFold\\u2019s detailed methodology in the paper \\u201cHighly accurate protein structure prediction with AlphaFold\\u201d and <strong>DeepMind open sources the code along with 60 pages of supplemental information</strong>.\",\n      \"age\": \"\",\n      \"source\": \"Google DeepMind\"\n    },\n    {\n      \"title\": \"Highly accurate protein structure prediction with AlphaFold - PubMed\",\n      \"url\": \"https://pubmed.ncbi.nlm.nih.gov/34265844/\",\n      \"snippet\": \"J.J., R.E., A. Pritzel, T.G., M.F., O.R., R.B., A.B., S.A.A.K., D.R. and A.W.S. have filed non-provisional patent applications 16/7 …[truncated]"
          },
          {
            "probe_id": "obs-32677",
            "similarity": 0.983,
            "task_text": "I'm after the 2026 Advanced Energy Materials paper by Zhang et al. on molecular design and interfacial functions of self-assembled monolayers for perovskite and tandem solar cells. Give me the DOI.",
            "adapted_input": "I'm after the 2026 Advanced Energy Materials paper by Zhang et al. on molecular design and interfacial functions of self-assembled monolayers for perovskite and tandem solar cells. Give me the DOI.",
            "score": 1,
            "redacted": null,
            "output_chars": 12703,
            "truncated": false,
            "created_at": "2026-08-29T10:34:06.623430Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "pass",
                "score": 1,
                "rationale": "Deterministic check — matched 1/1 required string(s).",
                "panel": null
              }
            ],
            "raw_output": "{\n  \"query\": \"I'm after the 2026 Advanced Energy Materials paper by Zhang et al. on molecular design and interfacial functions of self-assembled monolayers for perovskite and tandem solar cells. Give me the DOI.\",\n  \"adapted_query\": \"Zhang 2026 Advanced Energy Materials self-assembled monolayers molecular design interfacial perovskite tandem solar cells DOI\",\n  \"provider\": \"Brave Search\",\n  \"total_results\": 19,\n  \"api_params\": {\n    \"count\": 20\n  },\n  \"results\": [\n    {\n      \"title\": \"Molecular Design and Interfacial Functions of Self\\u2010Assembled Monolayers for Perovskite and Tandem Solar Cells - Zhang - 2026 - Advanced Energy Materials - Wiley Online Library\",\n      \"url\": \"https://advanced.onlinelibrary.wiley.com/doi/10.1002/aenm.70979\",\n      \"snippet\": \"As a potent interfacial platform at the crossroads of molecular engineering and device physics, self-assembled monolayers (SAMs) have been demonstrated to <strong>enable molecular-level control over buried interfaces in perovskite solar cells (PSCs),</strong> whilst ...\",\n      \"age\": \"April 23, 2026\",\n      \"source\": \"Wiley Online Library\"\n    },\n    {\n      \"title\": \"Interface-Engineered Composite Self-Assembled Monolayers Driving Efficient and Stable Wide-Bandgap Perovskite and Tandem Solar Cells | ACS Applied Materials & Interfaces\",\n      \"url\": \"https://pubs.acs.org/doi/10.1021/acsami.5c21997\",\n      \"snippet\": \"In …[truncated]"
          },
          {
            "probe_id": "obs-32796",
            "similarity": 0.982,
            "task_text": "What is the PMID of the 2026 Journal of Clinical Medicine paper by Xu et al. on early precise prediction and severe risk stratification of intrahepatic cholestasis of pregnancy?",
            "adapted_input": "What is the PMID of the 2026 Journal of Clinical Medicine paper by Xu et al. on early precise prediction and severe risk stratification of intrahepatic cholestasis of pregnancy?",
            "score": 0,
            "redacted": null,
            "output_chars": 449,
            "truncated": false,
            "created_at": "2026-08-29T11:40:59.789042Z",
            "judges": [
              {
                "facet": "capability",
                "verdict": "fail",
                "score": 0,
                "rationale": "Deterministic check — matched 0/1 required string(s); missing: 42589990.",
                "panel": null
              }
            ],
            "raw_output": "{\n  \"query\": \"What is the PMID of the 2026 Journal of Clinical Medicine paper by Xu et al. on early precise prediction and severe risk stratification of intrahepatic cholestasis of pregnancy?\",\n  \"adapted_query\": \"Xu 2026 \\\"Journal of Clinical Medicine\\\" intrahepatic cholestasis pregnancy early prediction severe risk stratification PMID\",\n  \"provider\": \"Brave Search\",\n  \"total_results\": 0,\n  \"api_params\": {\n    \"count\": 20\n  },\n  \"results\": []\n}"
          }
        ]
      },
      "evidence_teaser": {
        "task_text": "Find DeepMind's 2021 Nature paper announcing AlphaFold 2 and highly accurate protein structure prediction.",
        "verdict": "present",
        "score": 1,
        "similarity": 0.983,
        "n_real": 847
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
        "pubmed": 0,
        "kagi_search": 1,
        "unpaywall": 1,
        "ddg_search": 1
      }
    },
    {
      "name": "code_due_diligence",
      "label": "Source code reviewed",
      "description": "Stage 2 (specs/30-probing.md): for a tool whose code we run locally (MCP server, package, executable, CLI), the actual on-disk artifact we execute was statically reviewed — read-only, before any execution — and shows no obvious malicious or high-risk behavior: no covert network exfiltration, credential/secret harvesting, install- or load-time code execution, shell-out, obfuscation, or provenance/typosquat mismatch. Mark `na` for hosted APIs whose code we never run, and for a closed compiled binary whose executable cannot be read (its readable wrapper, manifests and install hooks are still reviewed; a finding there is `fail`). Unreadable is not malicious; the tool then rests on safe_distribution and no_machine_harm.",
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
        "pubmed": 0,
        "kagi_search": 0,
        "unpaywall": 0,
        "ddg_search": 1
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
        "pubmed": 0,
        "kagi_search": 1,
        "unpaywall": 1,
        "ddg_search": 1
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
        "pubmed": 1,
        "kagi_search": 1,
        "unpaywall": 1,
        "ddg_search": 0
      }
    },
    {
      "name": "data_retention_limited",
      "label": "Limited retention",
      "description": "Enforces a documented data-retention limit, or offers a zero/short-retention option for user inputs.",
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
        "pubmed": 1,
        "kagi_search": 1,
        "unpaywall": 1,
        "ddg_search": 1
      }
    },
    {
      "name": "dpa_available",
      "label": "DPA available",
      "description": "Offers a Data Processing Agreement (DPA) to customers.",
      "text_source": "authored",
      "scope": "global",
      "kind": "compliance",
      "spread": null,
      "divergent": false,
      "on": false,
      "kano": "attractive",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "kagi_search": 0
      }
    },
    {
      "name": "encrypted_at_rest",
      "label": "Encrypted at rest",
      "description": "Stored user data is encrypted at rest.",
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
        "pubmed": 0,
        "kagi_search": 0,
        "unpaywall": 0,
        "ddg_search": 0
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
        "pubmed": 1,
        "kagi_search": 1,
        "unpaywall": 1,
        "ddg_search": 1
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
        "pubmed": 0,
        "kagi_search": 1,
        "unpaywall": 1,
        "ddg_search": 1
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
      "values": {}
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
        "pubmed": 0,
        "kagi_search": 0,
        "unpaywall": 0,
        "ddg_search": 0
      }
    },
    {
      "name": "least_privilege_credentials",
      "label": "Scoped credentials",
      "description": "API credentials are scope-limited and revocable (least privilege); not a single all-powerful static secret.",
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
        "kagi_search": 1
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
        "pubmed": 1,
        "kagi_search": 1,
        "unpaywall": 1,
        "ddg_search": 1
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
        "pubmed": 1,
        "kagi_search": 1,
        "unpaywall": 1,
        "ddg_search": 1
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
        "pubmed": 1,
        "kagi_search": 1,
        "unpaywall": 1,
        "ddg_search": 1
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
        "pubmed": 1,
        "kagi_search": 1,
        "unpaywall": 1,
        "ddg_search": 1
      }
    },
    {
      "name": "reliability",
      "label": "Reliability",
      "description": "How consistently the tool is up and returns a result.",
      "text_source": "authored",
      "scope": "global",
      "kind": "live",
      "spread": 0.0176,
      "divergent": false,
      "on": false,
      "kano": "must_be",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "pubmed": 0.992,
        "kagi_search": 0.998,
        "unpaywall": 0.981,
        "ddg_search": 0.998
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
        "pubmed": 1,
        "kagi_search": 1,
        "unpaywall": 1,
        "ddg_search": 1
      }
    },
    {
      "name": "soc2",
      "label": "SOC 2",
      "description": "Holds a current SOC 2 (Type II preferred) report from an independent auditor.",
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
        "pubmed": 0,
        "kagi_search": 0,
        "unpaywall": 0,
        "ddg_search": 0
      }
    },
    {
      "name": "subprocessors_disclosed",
      "label": "Subprocessors disclosed",
      "description": "Publicly discloses its sub-processors / fourth parties that may handle user data.",
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
        "pubmed": 1,
        "kagi_search": 1,
        "unpaywall": 0,
        "ddg_search": 0
      }
    },
    {
      "name": "third_party_pentest",
      "label": "Third-party pentest",
      "description": "Has a recent independent penetration test on record.",
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
        "pubmed": 0,
        "kagi_search": 0,
        "unpaywall": 0,
        "ddg_search": 0
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
        "pubmed": 1,
        "kagi_search": 1,
        "unpaywall": 0,
        "ddg_search": 1
      }
    },
    {
      "name": "citation_existence",
      "label": "Real citations",
      "description": "Are the sources it cites real and reachable, not made up or dead?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.3823,
      "divergent": true,
      "on": false,
      "kano": "attractive",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "pubmed": 0.6,
        "kagi_search": 0.922,
        "unpaywall": 0.545,
        "ddg_search": 0.928
      }
    },
    {
      "name": "completeness",
      "label": "Complete coverage",
      "description": "Does the result cover the topic's main angles, not just one?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.1489,
      "divergent": false,
      "on": false,
      "kano": "performance",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "pubmed": 0.469,
        "kagi_search": 0.618,
        "unpaywall": 0.562,
        "ddg_search": 0.511
      }
    },
    {
      "name": "explanation_quality",
      "label": "Clear reasoning",
      "description": "Does it explain its answer in a way you can check against the sources?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.448,
      "divergent": true,
      "on": false,
      "kano": "performance",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "pubmed": 0.467,
        "kagi_search": 0.033,
        "unpaywall": 0.35,
        "ddg_search": 0.019
      }
    },
    {
      "name": "format",
      "label": "Structured output",
      "description": "Is the response cleanly structured so software can read it reliably?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.4932,
      "divergent": true,
      "on": false,
      "kano": "attractive",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "pubmed": 0.5,
        "kagi_search": 0.988,
        "unpaywall": 0.979,
        "ddg_search": 0.993
      }
    },
    {
      "name": "freshness",
      "label": "Up to date",
      "description": "Is the answer based on current information rather than stale data?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.3545,
      "divergent": true,
      "on": false,
      "kano": "performance",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "pubmed": 0.625,
        "kagi_search": 0.939,
        "unpaywall": 0.979,
        "ddg_search": 0.942
      }
    },
    {
      "name": "output_was_returned",
      "label": "Returned an answer",
      "description": "Did the tool return any usable result at all?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.2733,
      "divergent": true,
      "on": false,
      "kano": "must_be",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "pubmed": 0.72,
        "kagi_search": 0.989,
        "unpaywall": 0.979,
        "ddg_search": 0.993
      }
    },
    {
      "name": "references_present",
      "label": "Shows its sources",
      "description": "Does the output include links or references you can follow?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.2922,
      "divergent": true,
      "on": false,
      "kano": "attractive",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "pubmed": 0.679,
        "kagi_search": 0.971,
        "unpaywall": 0.959,
        "ddg_search": 0.969
      }
    },
    {
      "name": "relevance",
      "label": "Relevant results",
      "description": "Are the most useful results surfaced first?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.3757,
      "divergent": true,
      "on": false,
      "kano": "performance",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "pubmed": 0.542,
        "kagi_search": 0.881,
        "unpaywall": 0.697,
        "ddg_search": 0.917
      }
    },
    {
      "name": "safety",
      "label": "Safe responses",
      "description": "Is the response safe to use, and does it decline to invent answers to bogus queries?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.2649,
      "divergent": true,
      "on": false,
      "kano": "must_be",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "pubmed": 0.446,
        "kagi_search": 0.689,
        "unpaywall": 0.484,
        "ddg_search": 0.711
      }
    },
    {
      "name": "snippet_quality",
      "label": "Useful previews",
      "description": "Are the result summaries informative enough to judge without clicking through?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.4726,
      "divergent": true,
      "on": false,
      "kano": "attractive",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "pubmed": 0.5,
        "kagi_search": 0.959,
        "unpaywall": 0.824,
        "ddg_search": 0.973
      }
    },
    {
      "name": "transparency",
      "label": "Transparent",
      "description": "Does it disclose what it searched, its confidence, and what it couldn't verify?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.4302,
      "divergent": true,
      "on": false,
      "kano": "performance",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.5,
      "values": {
        "pubmed": 0.5,
        "kagi_search": 0.07,
        "unpaywall": 0.5,
        "ddg_search": 0.192
      }
    },
    {
      "name": "verdict_accuracy",
      "label": "Correct verdict",
      "description": "Did the fact-check reach the right true/false call?",
      "text_source": "authored",
      "scope": "tool",
      "kind": "quality",
      "spread": 0.3406,
      "divergent": true,
      "on": false,
      "kano": "must_be",
      "weight": 0,
      "default_weight": 0,
      "threshold": 0.6,
      "values": {
        "pubmed": 0.531,
        "kagi_search": 0.738,
        "unpaywall": 0.469,
        "ddg_search": 0.809
      }
    }
  ]
}
```
