# Project Brief — Ticksy by Futurense

> **This file describes the target project to be documented.**  
> Replace this content to point the agent system at a different project.

---

## Project Identity

| Field | Value |
|---|---|
| **Name** | Ticksy |
| **Organization** | Futurense |
| **Type** | Internal helpdesk / ticketing platform |
| **Status** | Production |

---

## Technology Stack

### Frontend

| Layer | Technology |
|---|---|
| Framework | React 18 (Create React App) |
| UI Library | Material UI (MUI) |
| Utility CSS | Tailwind CSS |
| HTTP Client | Axios (with interceptors) |
| Routing | React Router |
| Charts | Recharts |
| Auth | JWT (stored client-side), Moodle SSO integration |
| Hosting | Firebase Hosting |

### Backend

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| ORM | SQLAlchemy |
| Database | PostgreSQL (AWS RDS) |
| Validation | Pydantic |
| Scheduler | APScheduler |
| Server | Uvicorn |
| Auth | JWT, Moodle SSO |
| AI/ML | Google Gemini API |
| Vector DB | ChromaDB |
| Object Storage | AWS S3 (attachments) |
| Email | IMAP (inbound), SMTP (outbound) |
| Compute | AWS (EC2 or equivalent) |

### Infrastructure

| Component | Service |
|---|---|
| Frontend Hosting | Firebase Hosting |
| Backend Compute | AWS |
| Database | AWS RDS (PostgreSQL) |
| Object Storage | AWS S3 |
| DNS/CDN | (to be discovered) |

---

## Key Functional Domains

1. **Ticket Management** — creation, assignment, lifecycle/state transitions, priority, SLA tracking
2. **User & Role Management** — RBAC, role-based navigation, protected routes
3. **Authentication** — JWT-based auth, Moodle SSO integration
4. **Email Integration** — IMAP polling for inbound tickets, SMTP for notifications
5. **Dashboards & Analytics** — agent performance, FRT, SLA compliance, Recharts visualizations
6. **AI Features** — Gemini-powered suggestions, ChromaDB knowledge base
7. **File Attachments** — AWS S3 upload/download with pre-signed URLs
8. **Background Jobs** — APScheduler tasks (email polling, SLA checks, cleanup)
9. **Notifications** — in-app and email notifications

---

## Target Repository

> **Path**: _(Set this to the absolute path or URL of the Ticksy repository before starting documentation)_
>
> Example:
> ```
> target_repo: /path/to/ticksy
> ```

---

## Documentation Deliverables

### Markdown Documentation (`docs/`)

| Section | Content |
|---|---|
| `00-discovery/` | File inventory, dependency map |
| `01-architecture/` | C4 diagrams (Context, Container, Component), system overview |
| `02-frontend/` | Component hierarchy, routing, auth contexts, API service layer, screen-by-screen behavior, frontend-to-backend API mapping |
| `03-backend/` | API reference (every endpoint), business logic, ticket lifecycle, calculations (FRT, SLA, priority, delays, agent performance), auth & security, middleware, background jobs |
| `04-database/` | Schema reference (every table/column), ER diagram, relationships, indexes, query performance notes |
| `05-devops/` | Local development setup, environment variables catalog, build/deployment configs, health checks, troubleshooting, developer onboarding guide |
| `06-audit/` | Verification report, security/performance audit |

### Diagrams

| Format | Deliverable |
|---|---|
| Mermaid | Inline in Markdown + standalone `.mermaid` files in `docs/diagrams/` |
| Draw.io | `.drawio` XML files in `docs/diagrams/` |

### OpenDocument Deliverables (`docs/consolidated/`)

| File | Content |
|---|---|
| `full-documentation.odt` | Consolidated documentation with all sections, diagrams, and tables |
| `executive-summary.odt` | High-level overview for stakeholders |

> **Note**: `.odt` files must be genuine OpenDocument format, not renamed Markdown or HTML.

---

## Adapting This Brief for Another Project

To use this agent system for a different project:

1. Replace the **Project Identity** section with the new project's name and org.
2. Update the **Technology Stack** tables to match the new stack.
3. Update **Key Functional Domains** to reflect the new project's features.
4. Set the **Target Repository** path.
5. Adjust **Documentation Deliverables** if the new project needs different outputs.
6. Optionally ask `config-updater-agent` to adjust agent prompts for the new stack.
