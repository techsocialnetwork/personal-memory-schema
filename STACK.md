# The Personal AI Stack

**Author:** Richard Lofthouse  
**Date:** 2026-04-29  
**Status:** Specs published, MVP in progress

---

## Overview

Three layers. One coherent architecture for AI that genuinely knows you, manages your communications, and connects you to others — on your terms, with your data owned by you.

```
┌─────────────────────────────────────────────────────────┐
│                  LAYER 3: PMS-CONNECT                    │
│         AI-Native Communication Network                  │
│                                                         │
│  Public JSON feed at /.well-known/pms.json              │
│  User-controlled visibility (public/contacts/private)   │
│  AI-to-AI handshake before message delivery             │
│  Decentralised identity (DIDs)                          │
│  Kill switch: instant on/off                            │
└──────────────────────┬──────────────────────────────────┘
                       │ provides context to / receives from
┌──────────────────────▼──────────────────────────────────┐
│                  LAYER 2: UCIL                           │
│         Unified Communication Intelligence Layer         │
│                                                         │
│  All channels → one AI-filtered stream                  │
│  Priority scoring + intent classification               │
│  Draft-in-your-voice responses                          │
│  Auto-respond / draft+approve / alert / archive         │
└──────────────────────┬──────────────────────────────────┘
                       │ grounded in / feeds back to
┌──────────────────────▼──────────────────────────────────┐
│                  LAYER 1: PMS                            │
│         Personal Memory Schema                           │
│                                                         │
│  Working theories with confidence levels                │
│  Committed decisions + rejected options                 │
│  Belief history — how your thinking evolved             │
│  Cognitive identity + communication style               │
│  Compounding feedback loop                              │
└─────────────────────────────────────────────────────────┘
```

---

## How the Layers Work Together

### Layer 1 grounds everything

PMS is the foundation. Every other layer reads from it and writes back to it.

- UCIL uses PMS to classify messages (your active projects get priority, known contacts get scored accurately, your communication style drives draft tone)
- PMS-Connect uses PMS to populate the public feed (only what you've set to `public` or `contacts` visibility)
- Agents use PMS as pre-prompt context so they act as extensions of your thinking, not generic tools

### Layer 2 manages the surface area

UCIL is the layer that handles the volume — all the incoming signal across channels. Without it, Layer 3 (PMS-Connect) creates more inbound, not less.

With UCIL in place, connecting to more people via PMS-Connect doesn't increase your workload. Your AI handles the volume; you handle the decisions.

### Layer 3 is the network effect

PMS-Connect is what makes the whole thing scale beyond a personal tool. When other people run PMS nodes:

- Your AI can query their preferences before composing messages
- Their AI can query yours — so every interaction starts with mutual context
- Spam drops to near-zero (anonymous senders without PMS nodes get filtered automatically)
- Discovery becomes structured (find people with expertise in X who are open to Y)

Each new node in the network makes every other node more valuable.

---

## The Compounding Loop

```
New interaction
      ↓
UCIL classifies + routes (using PMS context)
      ↓
Agent responds / acts (using PMS + knowledge graph)
      ↓
Outcome updates PMS (new belief, decision, or project state)
      ↓
PMS-Connect feed updates (if relevant section is public)
      ↓
Network sees updated context
      ↓
Next interaction starts with richer context
      ↓
Repeat — system improves monotonically
```

This is the core value proposition: **the system gets better the more you use it**. Generic AI is static. This stack compounds.

---

## Data Ownership

Every layer is designed around user ownership:

| Layer | Where data lives | Who controls it |
|-------|-----------------|-----------------|
| PMS | Local device | You |
| UCIL | Local classifier + local archive | You |
| PMS-Connect public feed | Your domain / your hosting | You |
| PMS-Connect private data | Local device only | You — never exposed |

No layer requires a central server. No provider owns your data. The public feed is served from infrastructure you control. The private memory never leaves your device.

---

## Current Status

| Layer | Spec | Implementation |
|-------|------|---------------|
| PMS (core schema) | ✅ Published | ✅ Working (personal use) |
| PMS (profiles + extensions) | ✅ Published | 🔧 In progress |
| UCIL | ✅ Published | 🔧 MVP design stage |
| PMS-Connect | ✅ Published | ⏳ Planned |

---

## Repositories

| Repo | Contents |
|------|----------|
| [personal-memory-schema](https://github.com/techsocialnetwork/personal-memory-schema) | PMS core spec, profiles, extensions, CLI |
| [ideas](https://github.com/techsocialnetwork/ideas) | All concept specs including UCIL and PMS-Connect |

---

## Contact

**Richard Lofthouse** — tsn@tsnmedia.org  
[tsnmedia.org](https://tsnmedia.org) | [@tsncrypto](https://twitter.com/tsncrypto)

Commercial licensing, collaboration, or implementation enquiries welcome.

---

*© 2026 Richard Lofthouse / TSN Media — CC BY-NC-SA 4.0*
