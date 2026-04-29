# Personal AI Memory Schema — IP Specification
**Version:** 0.1.0  
**Created:** 2026-04-29  
**Author:** Richard Lofthouse / TSN Media  
**Status:** Draft — Confidential

---

## Overview

This document specifies the Personal Memory Schema (PMS) — the structured data model that captures a user's cognitive identity for use as persistent context in AI systems.

The schema is the core IP of a personalised AI platform. It is distinct from:
- Simple fact storage (OpenAI Memory style: "User's name is Richard")
- Document retrieval (RAG: finding relevant chunks from a corpus)
- Conversation history (replay of past messages)

**What PMS captures:** the user's *mental model* — their active theories, committed decisions, rejected options, working frameworks, and epistemic state — updated continuously and used to ground every AI interaction.

---

## Design Principles

1. **Compounding** — every interaction enriches the model; the system gets better with use
2. **Structured, not narrative** — queryable JSON, not prose summaries
3. **Confidence-aware** — every belief has an associated confidence level that changes over time
4. **Contradiction-handling** — the schema tracks belief revisions, not just current state
5. **Timestamped** — all entries have creation and last-updated timestamps for decay/recency weighting
6. **Privacy-first** — designed for local-first storage; cloud sync optional and encrypted
7. **Model-agnostic** — works with any LLM via prompt injection; not tied to a specific provider

---

## Schema Definition (JSON)

```json
{
  "$schema": "https://pms.tsnmedia.org/schema/v0.1.0",
  "version": "0.1.0",
  "user_id": "string (UUID)",
  "created_at": "ISO8601",
  "last_updated": "ISO8601",
  "schema_version": "0.1.0",

  "identity": { ... },
  "working_theories": [ ... ],
  "committed_decisions": [ ... ],
  "rejected_options": [ ... ],
  "active_projects": [ ... ],
  "domain_expertise": { ... },
  "cognitive_style": { ... },
  "relationships": [ ... ],
  "open_questions": [ ... ],
  "belief_history": [ ... ]
}
```

---

## Section 1: Identity

```json
"identity": {
  "display_name": "Richard",
  "timezone": "Europe/London",
  "language": "en-GB",
  "primary_domains": ["crypto", "AI infrastructure", "content publishing", "bioinformatics"],
  "communication_preferences": {
    "verbosity": "concise",
    "tone": "direct, no filler",
    "technical_depth": "high",
    "preferred_format": "structured with headings",
    "dislikes": ["generic openers", "excessive caveats", "obvious statements"]
  },
  "role_context": "independent content publisher, investor, AI builder",
  "goals": [
    {
      "id": "goal-001",
      "goal": "Build tsnmedia.org into a leading AI + crypto publication",
      "horizon": "12 months",
      "status": "active",
      "created_at": "2026-03-09"
    }
  ]
}
```

---

## Section 2: Working Theories

The most important section. Captures the user's active hypotheses — what they currently believe to be true about the world, with confidence levels and supporting evidence.

```json
"working_theories": [
  {
    "id": "theory-001",
    "title": "Constraint-Shift Pattern",
    "thesis": "Solutions don't eliminate constraints — they shift bottlenecks to the next layer. Every system that solves one constraint reveals the next one beneath it.",
    "confidence": 87,
    "confidence_history": [
      {"date": "2026-01-31", "value": 75, "trigger": "first observed in AI hardware analysis"},
      {"date": "2026-02-05", "value": 82, "trigger": "confirmed in Tesla dry electrode analysis"},
      {"date": "2026-04-29", "value": 87, "trigger": "confirmed again in genome sequencing / Apple M4 story"}
    ],
    "evidence": [
      "Open source AI won → hardware layer (HBM) became the constraint",
      "MinION sequencer solved biology bottleneck → Apple M4 compute became constraint → now consumables",
      "Tesla dry electrode solved battery design → lithium input is now the constraint",
      "Decentralised crypto succeeded → regulatory capture emerged as new constraint"
    ],
    "domains": ["AI", "infrastructure", "biology", "energy", "crypto"],
    "predictive_value": "high — use to identify next bottleneck in any system undergoing rapid change",
    "related_theories": ["theory-003"],
    "status": "active",
    "created_at": "2026-01-31",
    "last_updated": "2026-04-29",
    "source_signals": ["HBMBottleneck-RohanPaul", "Tesla-LG-Energy-Deal", "Oxford-Nanopore-Apple-M4"]
  },
  {
    "id": "theory-002",
    "title": "Personalised AI Outperforms Generic AI",
    "thesis": "AI systems grounded in individual user knowledge graphs and structured memory models will dramatically outperform generic AI for expert-level tasks. The performance gap widens with user expertise and system usage time.",
    "confidence": 90,
    "confidence_history": [
      {"date": "2026-04-29", "value": 90, "trigger": "first formalised after building vault RAG system"}
    ],
    "evidence": [
      "OpenAI Memory users report ~22% relevance improvement",
      "Enterprise RAG consistently outperforms generic ChatGPT on company-specific queries",
      "Personal RAG test on own vault produced directly relevant results vs generic AI",
      "Compounding feedback loop creates widening moat over time"
    ],
    "domains": ["AI", "product", "knowledge management"],
    "predictive_value": "high — identifies next AI product category",
    "status": "active",
    "created_at": "2026-04-29",
    "last_updated": "2026-04-29",
    "source_signals": ["vault-rag-build-2026-04-29", "personalised-rag-article"]
  },
  {
    "id": "theory-003",
    "title": "Infrastructure Layer = Real Moat",
    "thesis": "In AI and crypto, the real long-term moats are at the infrastructure layer (compute, energy, memory, connectivity), not the application layer. Application layer gets commoditised; infrastructure retains pricing power.",
    "confidence": 83,
    "confidence_history": [
      {"date": "2026-02-01", "value": 78},
      {"date": "2026-03-17", "value": 83, "trigger": "NVIDIA GTC analysis confirmed"}
    ],
    "evidence": [
      "NVIDIA retained 70%+ AI chip margins despite model commoditisation",
      "HBM vendors (Samsung, SK Hynix) maintain monopoly pricing",
      "Energy utilities gaining leverage as AI compute scales",
      "SpaceX orbital data centres — infrastructure play for AI at scale"
    ],
    "domains": ["AI", "crypto", "investing"],
    "predictive_value": "high — informs investment allocation",
    "status": "active",
    "created_at": "2026-02-01",
    "last_updated": "2026-03-17"
  }
]
```

---

## Section 3: Committed Decisions

Things the user has decided and doesn't need to reconsider unless explicitly prompted.

```json
"committed_decisions": [
  {
    "id": "decision-001",
    "decision": "Bitcoin self-custody only — no exchange holdings",
    "category": "financial",
    "reasoning": "Counterparty risk elimination, sovereignty, long-term conviction",
    "constraints": null,
    "reversibility": "low",
    "created_at": "2026-01-31",
    "last_reaffirmed": "2026-04-29",
    "status": "active"
  },
  {
    "id": "decision-002",
    "decision": "tsnmedia.org content strategy: AI + crypto convergence focus",
    "category": "business",
    "reasoning": "Underserved niche, high search intent, compound authority building",
    "constraints": "minimum 2000 words, HTML format, cyberpunk images",
    "reversibility": "medium",
    "created_at": "2026-03-09",
    "last_reaffirmed": "2026-04-29",
    "status": "active"
  },
  {
    "id": "decision-003",
    "decision": "Obsidian as primary knowledge management system",
    "category": "tooling",
    "reasoning": "Local-first, markdown, extensible, graph view",
    "reversibility": "medium",
    "created_at": "2026-01-31",
    "status": "active"
  }
]
```

---

## Section 4: Rejected Options

Things explicitly considered and ruled out. Prevents re-litigating closed decisions.

```json
"rejected_options": [
  {
    "id": "rejected-001",
    "option": "Affiliate marketing for crypto exchanges",
    "category": "business",
    "reason": "UK regulatory risk under FCA rules — deferred indefinitely",
    "considered_at": "2026-03-09",
    "reopen_condition": "if FCA regulatory framework clarifies in favour",
    "status": "deferred"
  },
  {
    "id": "rejected-002",
    "option": "Cloud-hosted personal AI (OpenAI Memory, Claude Projects) as primary system",
    "category": "tooling",
    "reason": "Data sovereignty — personal context should not be owned by provider",
    "considered_at": "2026-04-29",
    "reopen_condition": "if end-to-end encrypted local-sync option becomes available",
    "status": "rejected"
  }
]
```

---

## Section 5: Active Projects

```json
"active_projects": [
  {
    "id": "project-001",
    "name": "tsnmedia.org Content Pipeline",
    "status": "active",
    "phase": "scaling",
    "current_cadence": "2 articles per day",
    "next_action": "continue AI infrastructure + genomics content cluster",
    "blockers": [],
    "metrics": {
      "articles_published": 150,
      "avg_word_count": 2000,
      "categories": ["AI", "Bitcoin", "Tech", "Crypto News"]
    },
    "last_updated": "2026-04-29"
  },
  {
    "id": "project-002",
    "name": "Obsidian Vault RAG System",
    "status": "active",
    "phase": "MVP built",
    "current_state": "628 chunks indexed, semantic search working",
    "next_action": "wire vault query into agent pre-prompt injection",
    "last_updated": "2026-04-29"
  },
  {
    "id": "project-003",
    "name": "Personalised AI Platform (IP concept)",
    "status": "ideation",
    "phase": "spec",
    "current_state": "architecture designed, memory schema v0.1 drafted",
    "next_action": "build MVP memory update loop, assess market timing",
    "last_updated": "2026-04-29"
  }
]
```

---

## Section 6: Domain Expertise

Captures what the user knows deeply vs. superficially — prevents over-explaining known concepts.

```json
"domain_expertise": {
  "expert": [
    "Bitcoin fundamentals and custody",
    "AI agent architectures",
    "Content publishing and SEO",
    "Crypto market dynamics",
    "Data analysis"
  ],
  "proficient": [
    "Bioinformatics concepts",
    "Python scripting",
    "WordPress/WP-CLI",
    "RAG and vector search",
    "Macro investing frameworks"
  ],
  "familiar": [
    "Genomic sequencing technology",
    "Quantum computing basics",
    "Semiconductor supply chains"
  ],
  "learning": [
    "Personal AI platform architecture",
    "Multi-tenant SaaS design",
    "Knowledge graph design (Neo4j)"
  ]
}
```

---

## Section 7: Cognitive Style

How the user processes and prefers to receive information.

```json
"cognitive_style": {
  "reasoning_preference": "first-principles then pattern-matching",
  "information_processing": "frameworks over facts — give me the mental model, not just the data",
  "decision_making": "high conviction, decisive — doesn't need to explore all options once direction is clear",
  "uncertainty_tolerance": "high — comfortable acting on 70% confidence",
  "contrarian_tendency": "high — actively looks for non-consensus positions",
  "time_horizon": "medium-term (1-3 years primary), long-term (10+ years awareness)",
  "output_preferences": {
    "length": "comprehensive but not padded",
    "structure": "headers and bullets for reference material, prose for analysis",
    "actionability": "always end with a clear next action or decision"
  }
}
```

---

## Section 8: Open Questions

Active unresolved questions the user is working through.

```json
"open_questions": [
  {
    "id": "oq-001",
    "question": "Does regulated crypto (BlackRock ETFs, Genius Act) represent decentralisation victory or co-option?",
    "domain": "crypto",
    "current_lean": "co-option — institutions capture the rails",
    "confidence_in_lean": 60,
    "evidence_needed": "watch BTC ETF outflow patterns during regulatory pressure",
    "created_at": "2026-01-31",
    "priority": "medium"
  },
  {
    "id": "oq-002",
    "question": "Is the personalised AI platform a 12-month window or a 3-year opportunity?",
    "domain": "business",
    "current_lean": "12-18 months before platforms absorb it",
    "confidence_in_lean": 65,
    "evidence_needed": "watch OpenAI Memory and Claude Projects feature velocity",
    "created_at": "2026-04-29",
    "priority": "high"
  }
]
```

---

## Section 9: Belief History

Audit log of significant belief changes — enables the system to understand *how* the user's thinking evolves, not just where it currently is.

```json
"belief_history": [
  {
    "id": "bh-001",
    "theory_id": "theory-001",
    "event": "confidence_increase",
    "from_value": 75,
    "to_value": 82,
    "date": "2026-02-05",
    "trigger": "Tesla dry electrode analysis confirmed the pattern in manufacturing domain",
    "trigger_source": "analysis/HerbertOng-2026-02-02-TeslaDryElectrode-ANALYSIS.md"
  },
  {
    "id": "bh-002",
    "theory_id": "theory-002",
    "event": "theory_created",
    "from_value": null,
    "to_value": 90,
    "date": "2026-04-29",
    "trigger": "built and tested vault RAG system, confirmed relevance improvement",
    "trigger_source": "vault-rag/ingest.py build session"
  }
]
```

---

## The Update Mechanism (Core IP)

After every significant session, the following extraction runs automatically:

```
SESSION ENDS
     ↓
LLM EXTRACTION PROMPT:
"Review this conversation. Extract any:
1. New beliefs or hypotheses formed
2. Existing beliefs confirmed or weakened (with evidence)
3. Decisions made (new commitments)
4. Options explicitly rejected
5. Project state changes
6. New open questions raised
7. Domain expertise demonstrated or claimed

Return structured JSON matching the PMS schema.
Flag contradictions with existing memory for human review."
     ↓
DELTA COMPUTED (new entries + confidence updates)
     ↓
CONTRADICTION CHECK:
- Does new belief conflict with existing committed decision?
- Does new evidence significantly change confidence in existing theory?
- Flag for user review if confidence delta > 15 points or direct contradiction
     ↓
MEMORY UPDATED + VERSIONED (git commit)
     ↓
KNOWLEDGE GRAPH UPDATED (new entities + relationships from session)
```

---

## Competitive Differentiation Summary

| Feature | OpenAI Memory | Mem.ai | Personal.ai | **PMS (This)** |
|---|---|---|---|---|
| Structured belief model | ❌ | ❌ | ❌ | ✅ |
| Confidence levels | ❌ | ❌ | ❌ | ✅ |
| Belief history / revision tracking | ❌ | ❌ | ❌ | ✅ |
| Committed decisions vs. open questions | ❌ | ❌ | ❌ | ✅ |
| Rejected options tracking | ❌ | ❌ | ❌ | ✅ |
| Automatic session extraction | ✅ | ❌ | Partial | ✅ |
| Knowledge graph integration | ❌ | ❌ | ❌ | ✅ |
| Local-first / user-owned | ❌ | ❌ | ❌ | ✅ |
| Agentic execution with context injection | ❌ | ❌ | ❌ | ✅ |
| Compounding feedback loop | Partial | ❌ | Partial | ✅ |

---

## MVP Build Order

**Phase 1 (2 weeks): Core schema + manual update**
- Implement schema as above for your own use
- Manual session extraction (you review + approve updates)
- Prove the value before automating

**Phase 2 (2 weeks): Automated extraction**
- End-of-session LLM extraction prompt
- Delta computation + contradiction flagging
- Git versioning of memory file

**Phase 3 (4 weeks): Agent integration**
- Pre-prompt injection: vault query + memory context
- Test: measurable improvement in agent output quality vs. baseline

**Phase 4 (8 weeks): Multi-user architecture**
- Schema generalises to any user (not Richard-specific)
- Per-user isolated storage (Qdrant Cloud namespaces)
- Onboarding flow: connect sources → initial memory bootstrap
- Web interface for memory review + editing

**Phase 5: Product**
- Obsidian plugin (biggest distribution surface for early adopters)
- API for third-party integrations
- Pricing + monetisation

---

## IP Protection Approach

1. **Document everything** — this spec + build dates establish prior art
2. **Copyright** — the schema design and extraction prompt methodology
3. **Trade secret** — the specific contradiction-detection and confidence-weighting algorithms
4. **Speed** — the moat is users + their accumulated memory data, not just the schema
5. **Consideration:** Patent the "compounding memory feedback loop" mechanism specifically — the automated extraction → update → versioning → injection cycle as a unified system

---

*Document status: Draft. For internal use only. Not for distribution.*  
*© 2026 Richard Lofthouse / TSN Media*
