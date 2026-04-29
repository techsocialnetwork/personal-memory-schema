# PMS Extensions

Extensions add domain-specific sections to the core Personal Memory Schema.
The base schema always stays the same — extensions are additive, optional, and standardised.

Extensions registered here are official. Community extensions can be proposed via PR.

---

## How Extensions Work

The base `memory.json` has 9 core sections (identity, working_theories, committed_decisions, etc.).

Extensions add new top-level sections. A memory file can include any combination:

```json
{
  "$schema": "pms-v0.1.0",
  "version": "0.1.0",
  
  // ── Core sections (always present) ──
  "identity": { ... },
  "working_theories": [ ... ],
  "committed_decisions": [ ... ],
  
  // ── Extensions (optional, additive) ──
  "extensions": {
    "ucil": { ... },       // Unified Communication Intelligence Layer
    "portfolio": { ... },  // Investment/portfolio tracking
    "content": { ... }     // Content publishing context
  }
}
```

Extensions never modify core sections. They only add. This ensures backward compatibility.

---

## Registered Extensions

### `ucil` — Unified Communication Intelligence Layer

Adds communication preferences, relationship graph, and channel routing rules.

**Use case:** When PMS is used to ground an AI that manages your communications across channels.

```json
"extensions": {
  "ucil": {
    "version": "0.1.0",
    "channels": {
      "telegram": {
        "connected": true,
        "default_priority_boost": 0,
        "auto_respond_enabled": false
      },
      "email": {
        "connected": false,
        "account": "tsn@tsnmedia.org",
        "auto_respond_enabled": false
      },
      "twitter_dm": {
        "connected": false,
        "auto_respond_enabled": false
      }
    },
    "classification_rules": [
      {
        "id": "rule-001",
        "condition": "sender in known_contacts AND intent == 'social'",
        "action": "archive",
        "reason": "Social messages from known contacts don't need immediate attention"
      },
      {
        "id": "rule-002",
        "condition": "intent == 'opportunity' AND sender == 'stranger'",
        "action": "draft_approve",
        "reason": "Unknown senders with opportunities need human review"
      }
    ],
    "known_contacts": [
      {
        "id": "contact-001",
        "name": "Display Name",
        "channels": { "telegram": "username", "email": "email@example.com" },
        "relationship": "close | known | acquaintance",
        "priority_boost": 20,
        "notes": "context about this person"
      }
    ],
    "response_style": {
      "default_tone": "direct, friendly",
      "sign_off": "",
      "avoid": ["excessive formality", "corporate language"]
    },
    "digest": {
      "enabled": true,
      "frequency": "daily",
      "time": "09:00",
      "include_archived": false
    }
  }
}
```

---

## Schema Profiles (Expand / Contract)

The same schema works at three levels of depth. Pick the profile that matches your use case.

### Profile: Minimal
For new users or simple use cases. Just the essentials.

```json
{
  "$schema": "pms-v0.1.0",
  "profile": "minimal",
  "identity": {
    "display_name": "Your Name",
    "primary_domains": ["your-domain"],
    "communication_preferences": {
      "tone": "direct"
    }
  },
  "working_theories": [
    {
      "id": "theory-001",
      "title": "Your theory",
      "thesis": "What you believe",
      "confidence": 75
    }
  ],
  "committed_decisions": [],
  "rejected_options": []
}
```

**When to use:** Just starting, testing, or onboarding a new user. Generates useful injection prompts with minimal setup.

---

### Profile: Standard
The default. Full core schema, no extensions.

Includes all 9 core sections: identity, working_theories, committed_decisions, rejected_options, active_projects, domain_expertise, cognitive_style, open_questions, belief_history.

**When to use:** Active personal use. Most individuals will live here permanently.

---

### Profile: Extended
Standard + one or more registered extensions.

```json
{
  "profile": "extended",
  "extensions": ["ucil", "portfolio"]
}
```

**When to use:** When PMS is grounding agents that operate across multiple domains (comms + investments + content).

---

### Profile: Enterprise
Multi-user version. Each user has their own memory.json. A shared `org_context.json` holds organisation-level beliefs and decisions that all users inherit.

```json
// org_context.json — shared across all users
{
  "org_id": "org-uuid",
  "org_name": "Company Name",
  "shared_theories": [ ... ],      // Org-level beliefs (e.g. "our market is X")
  "shared_decisions": [ ... ],     // Org-level commitments (e.g. "we use Python")
  "shared_rejected": [ ... ]       // Org-level rejected options
}

// Each user's memory.json inherits org context + has personal layer
{
  "user_id": "user-uuid",
  "org_id": "org-uuid",            // Links to org_context.json
  "profile": "enterprise",
  "identity": { ... },             // Personal layer
  "working_theories": [ ... ],     // Personal theories (may override org theories)
  ...
}
```

**When to use:** Teams, companies, or any multi-user deployment. Org context sets the baseline; individual memory layers personalise on top.

---

## Standardisation Approach

### Why standardise?

If PMS becomes widely adopted, different implementations need to interoperate:
- A tool built on PMS should be able to read any valid PMS file
- Extensions should be composable without conflicts
- Profiles should be declared, not inferred

### Version contract

- `pms-v0.x.x` — breaking changes allowed (we are here)
- `pms-v1.x.x` — stable; only additive changes
- `pms-v1.x.x` → `pms-v2.x.x` — migration required

### Validation

A valid PMS file must:
- Declare `$schema` and `version`
- Declare `profile` (minimal | standard | extended | enterprise)
- Include all required fields for the declared profile
- Not modify core section structure in extensions (only add)

### Extension registry

Extensions are registered here (this file). Format:
```
Name: ucil
Version: 0.1.0
Author: Richard Lofthouse
Purpose: Communication intelligence layer
Status: Draft
```

To propose a new extension: open a PR adding the extension spec to this file.

### Registered Extensions

```
Name: ucil
Version: 0.1.0
Author: Richard Lofthouse
Purpose: Unified Communication Intelligence Layer — cross-channel AI inbox
Status: Draft

Name: pms-connect
Version: 0.1.0
Author: Richard Lofthouse
Purpose: AI-native communication protocol — public JSON feed, visibility controls, AI-to-AI handshake
Status: Draft
```

---

### `pms-connect` — AI-Native Communication Protocol

Adds a user-controlled public JSON feed and AI-to-AI handshake protocol to the PMS node.

**Use case:** When you want other AI agents to discover your communication preferences and context before messaging you — and when you want your AI to query recipients' context before sending on your behalf.

**Full spec:** See [ideas repo — PMS-Connect](https://github.com/techsocialnetwork/ideas/blob/master/2026-04-29-pms-connect-protocol.md)

```json
"extensions": {
  "pms_connect": {
    "version": "0.1.0",
    "node_id": "did:web:yourdomain.com",
    "feed_enabled": true,
    "feed_url": "https://yourdomain.com/.well-known/pms.json",
    "visibility": {
      "identity": "public",
      "communication_preferences": "public",
      "working_theories": "contacts",
      "committed_decisions": "private",
      "rejected_options": "private",
      "active_projects": "contacts",
      "domain_expertise": "public",
      "open_questions": "private"
    },
    "handshake_endpoint": "https://yourdomain.com/.well-known/pms-handshake",
    "rate_limit": "10/hour",
    "contacts": []
  }
}
```

**Visibility levels:**

| Level | Who can read |
|-------|-------------|
| `public` | Anyone — AI agents, crawlers, any caller |
| `contacts` | Verified contacts only (mutual or approved) |
| `trusted` | Explicit whitelist |
| `private` | Never exposed — local only |

**Kill switch:** Set `"feed_enabled": false` — endpoint returns 404 instantly. All data stays local.

---

## Roadmap

| Version | Key additions |
|---------|--------------|
| v0.1.0 | Core schema, minimal/standard profiles, UCIL + PMS-Connect extension drafts |
| v0.2.0 | Portfolio extension, content extension, validation tooling |
| v0.3.0 | Enterprise profile, org_context.json spec, migration tooling |
| v0.4.0 | PMS-Connect reference server implementation |
| v1.0.0 | Stable API, full extension registry, JSON Schema validator, Matrix integration |

---

*© 2026 Richard Lofthouse / TSN Media — tsn@tsnmedia.org*
