#!/usr/bin/env python3
"""
verify_docs.py — Documentation Completeness Checker

Verifies that the expected documentation structure exists and that
key files are non-empty. Run from the repository root:

    python scripts/verify_docs.py
"""

import os
import sys
from pathlib import Path

# Expected files and directories relative to repo root
EXPECTED_TOP_LEVEL = [
    "README.md",
    "AGENTS.md",
    "project.brief.md",
    "PLAN_APPROVAL.md",
    "CHANGELOG.md",
]

EXPECTED_RULES = [
    ".agents/rules/accuracy-and-safety.md",
    ".agents/rules/plan-first.md",
    ".agents/rules/agent-naming.md",
]

EXPECTED_AGENTS = [
    ".agents/agents/manager-agent.md",
    ".agents/agents/discovery-agent.md",
    ".agents/agents/frontend-agent.md",
    ".agents/agents/backend-agent.md",
    ".agents/agents/backend-api-agent.md",
    ".agents/agents/backend-domain-agent.md",
    ".agents/agents/backend-infra-agent.md",
    ".agents/agents/data-uml-agent.md",
    ".agents/agents/devops-agent.md",
    ".agents/agents/auditor-agent.md",
    ".agents/agents/config-updater-agent.md",
]

EXPECTED_DOCS = [
    "docs/00-discovery/file-inventory.md",
    "docs/00-discovery/dependency-map.md",
    "docs/01-architecture/c4-context.md",
    "docs/01-architecture/c4-container.md",
    "docs/01-architecture/c4-component.md",
    "docs/02-frontend/component-hierarchy.md",
    "docs/02-frontend/routing-and-auth.md",
    "docs/02-frontend/api-service-layer.md",
    "docs/03-backend/api-reference.md",
    "docs/03-backend/business-logic.md",
    "docs/03-backend/infrastructure.md",
    "docs/03-backend/auth-and-security.md",
    "docs/04-database/schema-reference.md",
    "docs/04-database/er-diagram.md",
    "docs/04-database/query-performance.md",
    "docs/05-devops/local-setup.md",
    "docs/05-devops/environment-variables.md",
    "docs/05-devops/deployment.md",
    "docs/05-devops/onboarding-guide.md",
    "docs/06-audit/verification-report.md",
    "docs/06-audit/security-audit.md",
    "docs/consolidated/full-documentation.odt",
    "docs/consolidated/executive-summary.odt",
]


def check_files(repo_root: Path, file_list: list[str], category: str) -> tuple[int, int]:
    """Check if files exist and are non-empty. Returns (found, total)."""
    found = 0
    total = len(file_list)

    print(f"\n{'=' * 60}")
    print(f"  {category} ({total} expected)")
    print(f"{'=' * 60}")

    for rel_path in file_list:
        full_path = repo_root / rel_path
        if full_path.exists():
            size = full_path.stat().st_size
            if size > 0:
                print(f"  ✅  {rel_path} ({size:,} bytes)")
                found += 1
            else:
                print(f"  ⚠️  {rel_path} (EMPTY)")
        else:
            print(f"  ❌  {rel_path} (MISSING)")

    return found, total


def check_diagrams(repo_root: Path) -> tuple[int, int]:
    """Check for diagram files in docs/diagrams/."""
    diagrams_dir = repo_root / "docs" / "diagrams"
    print(f"\n{'=' * 60}")
    print(f"  Diagrams (docs/diagrams/)")
    print(f"{'=' * 60}")

    if not diagrams_dir.exists():
        print("  ❌  docs/diagrams/ directory MISSING")
        return 0, 1

    mermaid_files = list(diagrams_dir.glob("*.mermaid"))
    drawio_files = list(diagrams_dir.glob("*.drawio"))

    found = 0
    for f in mermaid_files:
        print(f"  ✅  {f.relative_to(repo_root)} ({f.stat().st_size:,} bytes)")
        found += 1
    for f in drawio_files:
        print(f"  ✅  {f.relative_to(repo_root)} ({f.stat().st_size:,} bytes)")
        found += 1

    if found == 0:
        print("  ⚠️  No diagram files found yet")

    return found, max(found, 1)


def check_odt_validity(repo_root: Path) -> None:
    """Basic check that .odt files are genuine ZIP/ODF files."""
    import zipfile

    print(f"\n{'=' * 60}")
    print(f"  ODT Validity Check")
    print(f"{'=' * 60}")

    odt_files = [
        "docs/consolidated/full-documentation.odt",
        "docs/consolidated/executive-summary.odt",
    ]

    for rel_path in odt_files:
        full_path = repo_root / rel_path
        if not full_path.exists():
            print(f"  ⏭️  {rel_path} — not yet created")
            continue

        try:
            with zipfile.ZipFile(full_path, "r") as zf:
                names = zf.namelist()
                if "mimetype" in names and "content.xml" in names:
                    print(f"  ✅  {rel_path} — valid ODF structure")
                else:
                    missing = []
                    if "mimetype" not in names:
                        missing.append("mimetype")
                    if "content.xml" not in names:
                        missing.append("content.xml")
                    print(f"  ⚠️  {rel_path} — ZIP but missing: {', '.join(missing)}")
        except zipfile.BadZipFile:
            print(f"  ❌  {rel_path} — NOT a valid ZIP/ODF file (possibly renamed text)")
        except Exception as e:
            print(f"  ❌  {rel_path} — Error: {e}")


def main():
    # Find repo root (script is in scripts/)
    script_dir = Path(__file__).resolve().parent
    repo_root = script_dir.parent

    # Allow override via argument
    if len(sys.argv) > 1:
        repo_root = Path(sys.argv[1]).resolve()

    print(f"Verifying documentation in: {repo_root}")

    total_found = 0
    total_expected = 0

    # Check each category
    for file_list, category in [
        (EXPECTED_TOP_LEVEL, "Top-Level Files"),
        (EXPECTED_RULES, "Agent Rules (.agents/rules/)"),
        (EXPECTED_AGENTS, "Agent Definitions (.agents/agents/)"),
        (EXPECTED_DOCS, "Documentation Output (docs/)"),
    ]:
        found, expected = check_files(repo_root, file_list, category)
        total_found += found
        total_expected += expected

    # Check diagrams
    d_found, d_expected = check_diagrams(repo_root)
    total_found += d_found
    total_expected += d_expected

    # Check ODT validity
    check_odt_validity(repo_root)

    # Summary
    print(f"\n{'=' * 60}")
    print(f"  SUMMARY")
    print(f"{'=' * 60}")
    pct = (total_found / total_expected * 100) if total_expected > 0 else 0
    print(f"  Files found: {total_found}/{total_expected} ({pct:.0f}%)")

    config_found = 0
    config_total = len(EXPECTED_TOP_LEVEL) + len(EXPECTED_RULES) + len(EXPECTED_AGENTS)
    for f in EXPECTED_TOP_LEVEL + EXPECTED_RULES + EXPECTED_AGENTS:
        if (repo_root / f).exists() and (repo_root / f).stat().st_size > 0:
            config_found += 1
    print(f"  Config/setup files: {config_found}/{config_total}")

    docs_found = 0
    for f in EXPECTED_DOCS:
        if (repo_root / f).exists() and (repo_root / f).stat().st_size > 0:
            docs_found += 1
    print(f"  Documentation files: {docs_found}/{len(EXPECTED_DOCS)}")

    if docs_found == 0:
        print("\n  💡 Documentation not yet generated.")
        print("     Ask manager-agent to start the documentation process.")
    elif docs_found < len(EXPECTED_DOCS):
        print(f"\n  ⚠️  Documentation partially complete ({docs_found}/{len(EXPECTED_DOCS)}).")
    else:
        print("\n  🎉 All documentation files present!")

    # Exit code
    if config_found < config_total:
        print("\n  ❌ FAIL — Missing configuration files.")
        sys.exit(1)
    else:
        print("\n  ✅ PASS — All configuration files present.")
        sys.exit(0)


if __name__ == "__main__":
    main()
