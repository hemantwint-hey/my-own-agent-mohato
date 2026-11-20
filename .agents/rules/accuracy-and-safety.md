# Rule: Accuracy and Safety

> **Scope**: ALL agents  
> **Priority**: CRITICAL — these rules override any conflicting instructions.

---

## Read-Only Inspection

- **NEVER** modify target project source code, configuration files, production databases, or deployment configs.
- Treat the target repository as **read-only**. You may read, search, and analyze files, but never write to, delete, or rename any file in the target project.
- The only writable locations are within this `company-docs-agents` repository (primarily `docs/`, `PLAN_APPROVAL.md`, and `CHANGELOG.md`).

## No Fabrication

- **NEVER** invent endpoints, classes, functions, database tables, columns, or features that do not exist in the actual codebase.
- **Distinguish clearly** between:
  - What is **implemented in code** (verified by reading source files)
  - What is **claimed in README/docs** but may not be implemented
  - What is **planned or optional** but not yet built
- If you cannot verify something from the source code, mark it as:
  - `UNKNOWN` — information could not be determined from available sources
  - `NOT VERIFIED` — the claim exists but could not be confirmed in code

## Cite Sources

- Include **file paths** (relative to the target repo root) wherever possible.
- Include **class names**, **function names**, and **line numbers** when referencing specific code.
- Format: `path/to/file.py:ClassName.method_name (L42-L67)`

## No Secret Exposure

- **NEVER** output, log, or include in documentation:
  - API keys, tokens, or secrets
  - Passwords or connection strings with credentials
  - Personal information (emails, names, phone numbers) unless they are public team contacts
  - Private URLs with embedded auth tokens
- If you encounter secrets in the codebase, note their **location** (file and variable name) but replace the value with `<REDACTED>`.

## Genuine File Formats

- `.odt` files MUST be genuine OpenDocument Text format, created with proper ODF XML structure.
- Never produce a Markdown or HTML file and rename it to `.odt`.
- Mermaid diagrams must use valid Mermaid syntax.
- Draw.io files must be valid `.drawio` XML.

## Security Findings Classification

When reporting security or performance issues, classify severity as:

| Severity | Description |
|---|---|
| **Critical** | Exploitable vulnerability with high impact (e.g., SQL injection, auth bypass) |
| **High** | Significant security risk or major performance issue |
| **Medium** | Moderate risk, recommended to fix |
| **Low** | Minor issue, best-practice improvement |
| **Informational** | Observation or suggestion, no direct risk |
