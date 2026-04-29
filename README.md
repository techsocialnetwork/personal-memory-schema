# Personal Memory Schema (PMS)

**A structured data model for persistent AI personalisation**

> Created by [Richard Lofthouse](https://tsnmedia.org) — April 29, 2026

---

## The Problem

Current AI systems treat every user the same. Even tools with "memory" features store shallow facts ("user's name is Richard") rather than the structured cognitive model that makes AI genuinely useful for a specific person:

- What do they currently believe — and how confident are they?
- What decisions have they made and committed to?
- What options have they explicitly rejected, and why?
- What frameworks do they use to process new information?
- How has their thinking evolved over time?

Without this, AI cannot act as a genuine collaborator. It can only answer questions. It cannot think *with* you.

## The Solution

The **Personal Memory Schema (PMS)** is a structured JSON data model that captures a user's cognitive identity — not just facts, but *beliefs with confidence levels*, *committed decisions*, *rejected options*, *active projects*, and *belief history*.

Combined with a personal knowledge graph and agentic AI, PMS creates an AI system that:
- Gets smarter the more you use it (compounding feedback loop)
- Knows your priors and doesn't re-explain things you already know
- Grounds autonomous agent actions in your actual values and decisions
- Belongs to you — local-first, not owned by any AI provider

---

## Schema Overview

```json
{
  "identity": { "communication style, role, goals..." },
  "working_theories": [
    {
      "title": "Your active hypothesis",
      "thesis": "What you currently believe",
      "confidence": 87,
      "confidence_history": [ ... ],
      "evidence": [ "supporting observations..." ]
    }
  ],
  "committed_decisions": [ "Things you've decided — don't re-litigate" ],
  "rejected_options": [ "Things considered and ruled out, with reasons" ],
  "active_projects": [ "Current work and state" ],
  "domain_expertise": { "expert / proficient / familiar / learning" },
  "cognitive_style": { "how you process and prefer information" },
  "open_questions": [ "Active unresolved questions with current lean" ],
  "belief_history": [ "Audit log of how beliefs evolved over time" ]
}
```

The key innovation: **confidence levels that change over time**, tracked in `belief_history`. The system doesn't just store what you believe — it tracks *how your beliefs have evolved* and what caused each change.

---

## What Makes This Different

| Feature | OpenAI Memory | Mem.ai | Personal.ai | **PMS** |
|---|---|---|---|---|
| Structured belief model | ❌ | ❌ | ❌ | ✅ |
| Confidence levels per belief | ❌ | ❌ | ❌ | ✅ |
| Belief revision history | ❌ | ❌ | ❌ | ✅ |
| Committed decisions vs open questions | ❌ | ❌ | ❌ | ✅ |
| Rejected options tracking | ❌ | ❌ | ❌ | ✅ |
| Local-first / user-owned | ❌ | ❌ | ❌ | ✅ |
| Compounding feedback loop | Partial | ❌ | ❌ | ✅ |

---

## Quick Start

### 1. Copy the example schema

```bash
cp memory.example.json memory.json
```

### 2. Edit with your own data

Open `memory.json` and fill in your:
- Working theories (what you currently believe about your domain)
- Committed decisions (what you've already decided)
- Rejected options (what you've considered and ruled out)
- Active projects
- Domain expertise levels

### 3. Use the management script

```bash
# View your memory
python3 update_memory.py --show

# Search your memory
python3 update_memory.py --query "what do I believe about AI infrastructure?"

# Get agent injection prompt (paste into any AI system)
python3 update_memory.py --inject

# Update a theory's confidence
python3 update_memory.py --update-confidence theory-001 89 "new evidence from X"

# Add a committed decision
python3 update_memory.py --add-decision "My new decision" "category" "reasoning"

# View stats
python3 update_memory.py --stats
```

### 4. Inject into AI sessions

Use `--inject` to generate a context block to prepend to any AI prompt:

```
=== PERSONAL CONTEXT ===
User: [Your name]
Working theories: [your beliefs with confidence levels]
Committed decisions: [what you've decided]
Active projects: [where you are]
=== END PERSONAL CONTEXT ===

[Your actual question/task]
```

This grounds any AI system in your personal context without requiring a specialised platform.

---

## The Compounding Loop

The real value of PMS is the feedback loop:

```
Session / Interaction
         ↓
New knowledge, decisions, belief changes emerge
         ↓
Extract structured delta (manually or via LLM)
         ↓
Update memory.json (confidence levels, new entries, belief history)
         ↓
Next session starts with richer context
         ↓
Repeat — system improves with every use
```

After 6 months of active use, the system has a detailed model of how you think, what you've concluded, and what evidence has moved your beliefs. No generic AI has this.

---

## Files

| File | Description |
|------|-------------|
| `memory.example.json` | Example schema with sample data — copy and personalise |
| `update_memory.py` | CLI tool to view, query, and update your memory |
| `SPEC.md` | Full technical specification |
| `EXTENSIONS.md` | Extension specs + schema profiles (minimal / standard / extended / enterprise) |
| `LICENSE` | CC BY-NC-SA 4.0 |

## Schema Profiles

PMS expands and contracts based on your use case:

| Profile | Use case |
|---------|----------|
| `minimal` | New users, quick start — just identity + beliefs |
| `standard` | Default — full core schema, no extensions |
| `extended` | Standard + registered extensions (UCIL, portfolio, content...) |
| `enterprise` | Multi-user — shared org context + individual memory layers |

See [EXTENSIONS.md](EXTENSIONS.md) for full profiles and the extension registry.

---

## Architecture Context

PMS is the foundation of a three-layer personal AI stack:

```
Layer 3: PMS-Connect  — AI-native network (public feed, AI-to-AI handshake, decentralised identity)
Layer 2: UCIL         — unified communication (all channels → AI-filtered stream → draft responses)
Layer 1: PMS          — personal identity (beliefs, decisions, frameworks)  ← this repo
```

See [STACK.md](STACK.md) for the full architecture and how the layers work together.

---

## Status

**Current version:** 0.1.0 (April 2026)  
**Status:** Proof of concept — personal use validated

The schema is in active use on a real knowledge base (350+ documents, tested against live vault semantic search). The management scripts are functional. The multi-user / SaaS architecture is designed but not yet implemented.

---

## Licence

[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International](LICENSE)

**You are free to:**
- Use this for personal and research purposes
- Share and adapt the schema

**Under these conditions:**
- **Attribution** — credit Richard Lofthouse / TSN Media and link to this repository
- **NonCommercial** — commercial use requires explicit written permission
- **ShareAlike** — derivatives must use the same licence

For commercial licensing: tsn@tsnmedia.org

---

## Author

**Richard Lofthouse**  
Creator of TSN Media | AI + crypto publisher | Builder  
[tsnmedia.org](https://tsnmedia.org) | [@tsncrypto](https://twitter.com/tsncrypto)

*First commit: April 29, 2026*

---

## Citation

If you use PMS in research or build on it:

```
Lofthouse, R. (2026). Personal Memory Schema (PMS): A structured data model 
for persistent AI personalisation. GitHub. 
https://github.com/rlofthouse/personal-memory-schema
```
