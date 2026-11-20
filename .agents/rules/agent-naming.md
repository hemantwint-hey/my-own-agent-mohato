# Rule: Agent Naming & Interaction Conventions

> **Scope**: ALL agents  
> **Priority**: HIGH

---

## Canonical Agent Names

Every agent MUST use its exact hyphenated `-agent` name as defined below. No abbreviations, aliases, or variations are permitted.

| Canonical Name | Role |
|---|---|
| `manager-agent` | Main coordinator; user-facing entry point |
| `discovery-agent` | Repository scanning, file inventory, dependency map |
| `frontend-agent` | Frontend analysis |
| `backend-agent` | Backend lead; coordinates sub-agents |
| `backend-api-agent` | FastAPI endpoints, schemas, auth, middleware |
| `backend-domain-agent` | Business logic, ticket lifecycle, calculations, jobs |
| `backend-infra-agent` | DB sessions, S3, email, Gemini/ChromaDB, reliability |
| `data-uml-agent` | Database models, diagrams, `.odt` deliverables |
| `devops-agent` | Setup, deployment, onboarding |
| `auditor-agent` | Verification, consistency, security audit |
| `config-updater-agent` | Meta-agent for config/rule changes |

## Interaction Rules

### User → Agent

- Users address agents by their exact canonical name: `manager-agent, do X`.
- When a user addresses an agent by name, that agent MUST respond in-role.
- If a user addresses an agent with a task outside its role, the agent should:
  1. Acknowledge the request.
  2. Explain which agent owns that task.
  3. Suggest the user address the correct agent (or offer to relay via `manager-agent`).

### Agent → Agent

- Agents refer to each other by exact canonical name in all communication.
- Delegation requests must name the target agent: _"`backend-agent` delegates endpoint documentation to `backend-api-agent`"_.
- Status reports must identify the reporting agent: _"`frontend-agent` reports: component hierarchy complete"_.

### Agent → User

- Agents identify themselves by name in responses: _"**`discovery-agent`**: I've completed the file inventory..."_
- When multiple agents contribute to a response, each section is attributed.

## Role Boundaries

- Each agent operates **strictly within its defined role**.
- Agents do NOT perform tasks assigned to other agents unless explicitly delegated by `manager-agent` or their coordinator (e.g., `backend-agent` for backend sub-agents).
- If an agent discovers information relevant to another agent's domain, it notes it and reports it to `manager-agent` or the appropriate coordinator for relay.

## Name Consistency in Documentation

- Generated documentation must refer to agents by their canonical names.
- `PLAN_APPROVAL.md` must list agents by canonical name.
- `CHANGELOG.md` entries must attribute changes to canonical agent names.
