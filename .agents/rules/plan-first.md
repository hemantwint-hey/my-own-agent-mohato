# Rule: Plan-First Workflow

> **Scope**: `manager-agent` (primary), all agents (awareness)  
> **Priority**: HIGH

---

## Trigger

When the user addresses `manager-agent` to start the documentation process (e.g., _"manager-agent, start the document process as planned"_ or similar), the plan-first workflow activates.

## Workflow Steps

### Step 1 — Inspect

`manager-agent` reads and analyzes:
1. `AGENTS.md` — agent registry, roles, and global rules
2. `project.brief.md` — target project stack, domains, and deliverables
3. Target project structure (if accessible) — directory tree, key files, entry points

### Step 2 — Plan

`manager-agent` produces a detailed **Execution & Documentation Plan** covering:
- **Agent execution order** using exact `-agent` names
- **Sub-agent coordination** (e.g., `backend-agent` → `backend-api-agent`, `backend-domain-agent`, `backend-infra-agent`)
- **Target `docs/` structure** with specific file names and expected content
- **`.odt` deliverables** and diagram outputs
- **Identified ambiguities** — unclear requirements, missing repo paths, stack questions
- **Dependencies** between agents (what must complete before what)
- **Estimated phases** with clear deliverables per phase

### Step 3 — Save & Pause

`manager-agent` saves the plan to `PLAN_APPROVAL.md` and **stops execution**.  
It informs the user:
> _"The plan is ready in `PLAN_APPROVAL.md`. Please review it and tell me what to change, or approve it to proceed."_

**Do NOT proceed to documentation generation without explicit user approval.**

### Step 4 — Incorporate Feedback

If the user provides feedback:
- `manager-agent` updates `PLAN_APPROVAL.md` with the revised plan.
- If feedback involves changing agent prompts, rules, or settings, `manager-agent` delegates to `config-updater-agent`.
- `manager-agent` presents the updated plan for re-approval if changes were significant.

### Step 5 — Execute

After user approval:
1. `manager-agent` delegates to specialist agents in the planned order.
2. Each agent produces its deliverables in `docs/`.
3. `backend-agent` coordinates its three sub-agents and merges their output.
4. `data-uml-agent` produces diagrams and consolidated `.odt` files.
5. `auditor-agent` verifies all documentation.
6. `manager-agent` reports final status and any issues to the user.

## Key Principles

- **Transparency**: The user always knows what will happen before it happens.
- **User control**: The user can modify any aspect of the plan before execution.
- **Incremental**: Large changes can be re-planned and re-approved.
- **Traceable**: The plan in `PLAN_APPROVAL.md` serves as a record of what was agreed.
