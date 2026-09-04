# Wave

AI-12

# Objective

Build Family 05, Research, OSINT & Public Records, with hard boundaries for lawful access, source provenance, and protected-record handling.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_12_RESEARCH_OSINT_READY
```

# Scope Completed

- Created all 14 `05-research-osint-public-records` skills.
- Added OpenAI adapter metadata for each research, OSINT, and public-records skill.
- Added one scoped reference file for each research skill.
- Added AI-12 research and OSINT scenario fixtures with positive and negative-routing coverage for each skill.
- Added hard-boundary scenario coverage for unauthorized database access, credential acquisition, private-account compromise, and protected-record acquisition through deception.
- Extended skill validation to enforce AI-12 family completion from the canonical taxonomy.

# Family 05 Skills

- `build-research-plan`
- `identify-public-record-sources`
- `plan-open-source-research`
- `research-corporate-records`
- `research-court-records`
- `research-regulatory-records`
- `assess-source-reliability`
- `record-source-provenance`
- `corroborate-open-source-information`
- `resolve-source-conflict`
- `research-organization-profile`
- `research-property-context`
- `research-litigation-history`
- `write-research-summary`

# Hard Boundary Tests

- unauthorized database access
- credential acquisition
- private-account compromise
- protected-record acquisition through deception

# Files Added

- `skills/05-research-osint-public-records/*`
- `tests/reference-skills/AI-12-research-osint-scenarios.json`
- `docs/development/handoffs/AI-12-final-handoff.md`
- `scripts/generate-ai12-skill-packages.py`

# Files Modified

- `README.md`
- `CHANGELOG.md`
- `scripts/validate-docs.py`
- `scripts/validate-skills.py`

# Sources

- `ROADMAP.md`
- `docs/architecture/taxonomy-index.yaml`
- `docs/architecture/sensitivity-model.md`
- `docs/architecture/authority-routing.md`
- `docs/architecture/prohibited-capabilities.md`
- `docs/architecture/intrusive-task-gate.md`
- `docs/standards/skill-authoring-standard.md`
- `docs/standards/skill-naming-standard.md`
- `docs/standards/output-contract-standard.md`
- `docs/standards/research-and-evidence-standard.md`
- `docs/standards/regulatory-source-standard.md`
- `docs/standards/source-freshness-standard.md`
- `docs/standards/testing-standard.md`
- `docs/foundations/professional-vocabulary.md`
- `docs/foundations/shared-schemas.md`
- `docs/foundations/report-structure-contracts.md`
- `docs/development/handoffs/AI-11-final-handoff.md`

# Validation Performed

```powershell
.\scripts\validate-all.ps1
python .\scripts\validate-skills.py --repo-root D:\AgentInvestigate
Get-ChildItem -LiteralPath 'D:\AgentInvestigate\skills\05-research-osint-public-records' -Directory | ForEach-Object { python 'C:\Users\jerem\.codex\skills\.system\skill-creator\scripts\quick_validate.py' $_.FullName }
git diff --check
```

# Tests

AI-12 adds scenario fixtures for all 14 research, OSINT, and public-records skills. Each skill has positive routing coverage and negative-routing hard-boundary coverage.

No live before/after model evaluation was run in AI-12.

# Safety / Regulatory Review

- Skills refuse or reroute unauthorized database access, credential acquisition, private-account compromise, protected-record acquisition through deception, access-control bypass, doxxing, stalking, and coercive collection.
- Regulated public-record skills provide source-backed research framing and issue spotting, not legal, privacy, licensing, employment, compliance, admissibility, or liability conclusions.
- Skills require authority, jurisdiction, lawful access basis, source provenance, and source freshness where the research depends on regulated or protected records.
- Source conflicts, gaps, assumptions, and unresolved claims are preserved rather than forced into findings.

# Known Limitations

- AI-12 does not add live source connectors, web-scraping tools, or jurisdiction-specific public-record source maps.
- Current source verification must happen at use time for regulated claims.
- Future role composition should route OSINT and public-records work through AI-09 professional-core, AI-10 authority/compliance, and AI-11 case-management gates.

# Explicitly Not Completed

- No AI-13 identity, entity, or timeline analysis skills.
- No skillsets.
- No specializations.
- No jurisdiction-specific source database.
- No live before/after evaluation reports.

# Recommended Next Wave

AI-13: Identity, Entity & Timeline Analysis.
