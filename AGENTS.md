# AGENTS.md — Multi-Agent Documentation System Configuration

This file is the central configuration reference for the multi-agent documentation system.  
Every agent MUST read this file (and `project.brief.md`) before starting work.

---

## Agent Registry

All agents use their exact hyphenated `-agent` names below. Users address agents by these names, and agents refer to each other by these names in all communication.

### Primary Agents

| # | Agent Name | Role | Config File |
|---|---|---|---|
| 1 | `manager-agent` | Main coordinator; user-facing entry point | `.agents/agents/manager-agent.md` |
| 2 | `discovery-agent` | Repo scanning, file inventory, dependency map | `.agents/agents/discovery-agent.md` |
| 3 | `frontend-agent` | Frontend analysis (React, routing, auth, API) | `.agents/agents/frontend-agent.md` |
| 4 | `backend-agent` | Backend lead; coordinates sub-agents | `.agents/agents/backend-agent.md` |
| 5 | `data-uml-agent` | DB models, diagrams (ER/C4/UML), `.odt` files | `.agents/agents/data-uml-agent.md` |
| 6 | `devops-agent` | Setup, env vars, deploy, onboarding | `.agents/agents/devops-agent.md` |
| 7 | `auditor-agent` | Verification, consistency, security audit | `.agents/agents/auditor-agent.md` |
| 8 | `config-updater-agent` | Meta-agent: edits configs, rules, agents | `.agents/agents/config-updater-agent.md` |

### Backend Sub-Agents (coordinated by `backend-agent`)

| # | Agent Name | Role | Config File |
|---|---|---|---|
| 4a | `backend-api-agent` | FastAPI routers, endpoints, schemas, auth, middleware | `.agents/agents/backend-api-agent.md` |
| 4b | `backend-domain-agent` | Business logic, ticket lifecycle, calculations, jobs | `.agents/agents/backend-domain-agent.md` |
| 4c | `backend-infra-agent` | DB sessions, AWS S3, email, Gemini/ChromaDB, reliability | `.agents/agents/backend-infra-agent.md` |

---

## Interaction Rules

1. **Name-based addressing**: Users address agents by exact name (e.g., `manager-agent, ...`). Agents respond in-role and collaborate using these exact names.
2. **Plan-first workflow**: When the user tells `manager-agent` to "start the document process as planned," `manager-agent` MUST first produce a plan in `PLAN_APPROVAL.md` and pause for user review before generating documentation.
3. **Delegation**: `manager-agent` delegates to specialist agents. `backend-agent` coordinates its three sub-agents. Agents report results back to their coordinator.
4. **Config changes**: Any request to change settings, modify agent behavior, add functionality, or edit agents/rules is routed to `config-updater-agent`.

---

## Global Rules (apply to ALL agents)

All rules in `.agents/rules/` are binding for every agent:

| Rule File | Summary |
|---|---|
| `.agents/rules/accuracy-and-safety.md` | Read-only inspection; no fabrication; no secrets; cite sources |
| `.agents/rules/plan-first.md` | Plan → Review → Execute workflow |
| `.agents/rules/agent-naming.md` | Exact `-agent` name usage; role boundaries |

### Key Constraints

- **Read-only**: Never modify target project source code, production configs, or databases.
- **No fabrication**: Only document what actually exists in code. Distinguish implementation from README claims or planned features. Mark unverifiable items as `UNKNOWN` or `NOT VERIFIED`.
- **No secrets**: Never expose API keys, tokens, passwords, connection strings, or PII.
- **Cite sources**: Include file paths, class/function names, and line numbers wherever possible.
- **Genuine `.odt`**: Produce real OpenDocument `.odt` files (not renamed Markdown/HTML).
- **Mermaid + Draw.io**: Provide diagram sources in both Mermaid (inline) and Draw.io (`.drawio` XML) formats.

---

## Documentation Output Structure

All generated documentation goes into `docs/`:

```
docs/
├── 00-discovery/
│   ├── file-inventory.md
│   └── dependency-map.md
├── 01-architecture/
│   ├── c4-context.md
│   ├── c4-container.md
│   ├── c4-component.md
│   └── diagrams/
├── 02-frontend/
│   ├── component-hierarchy.md
│   ├── routing-and-auth.md
│   ├── api-service-layer.md
│   └── screens/
├── 03-backend/
│   ├── api-reference.md
│   ├── business-logic.md
│   ├── infrastructure.md
│   └── auth-and-security.md
├── 04-database/
│   ├── schema-reference.md
│   ├── er-diagram.md
│   └── query-performance.md
├── 05-devops/
│   ├── local-setup.md
│   ├── environment-variables.md
│   ├── deployment.md
│   └── onboarding-guide.md
├── 06-audit/
│   ├── verification-report.md
│   └── security-audit.md
├── consolidated/
│   ├── full-documentation.odt
│   └── executive-summary.odt
└── diagrams/
    ├── *.mermaid
    └── *.drawio
```

---

## Workflow Summary

```
User → manager-agent → PLAN_APPROVAL.md → User reviews
                                         ↓ (approved)
manager-agent delegates:
  ├── discovery-agent      → docs/00-discovery/
  ├── frontend-agent       → docs/02-frontend/
  ├── backend-agent        → docs/03-backend/
  │   ├── backend-api-agent
  │   ├── backend-domain-agent
  │   └── backend-infra-agent
  ├── data-uml-agent       → docs/01-architecture/ + docs/04-database/ + docs/consolidated/
  ├── devops-agent         → docs/05-devops/
  └── auditor-agent        → docs/06-audit/
                                         ↓
manager-agent → Final report to user
```
