# Wave

AI-11

# Objective

Build Family 04, Investigation Planning & Case Management, as the foundation for private-investigator and investigative-case-manager composition.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_11_CASE_MANAGEMENT_READY
```

# Scope Completed

- Created all 13 `04-investigation-planning-case-management` skills.
- Added OpenAI adapter metadata for each case-management skill.
- Added one scoped reference file for each case-management skill.
- Added AI-11 case-management scenario fixtures with positive and negative-routing coverage for each skill.
- Added scenario topic coverage for investigation plans, investigative questions, timelines, leads, resources, milestones, case logs, notes, status, retention, review, gaps, and closure.
- Extended skill validation to enforce AI-11 family completion from the canonical taxonomy.

# Family 04 Skills

- `build-investigation-plan`
- `define-investigative-question`
- `create-case-timeline`
- `prioritize-investigative-leads`
- `estimate-investigative-resources`
- `define-case-milestones`
- `maintain-case-action-log`
- `write-case-notes`
- `prepare-case-status-update`
- `review-case-retention-needs`
- `conduct-case-file-review`
- `identify-case-gaps`
- `prepare-case-closure-summary`

# Composition Target

- `private-investigator`
- `investigative-case-manager`

# Files Added

- `skills/04-investigation-planning-case-management/*`
- `tests/reference-skills/AI-11-case-management-scenarios.json`
- `docs/development/handoffs/AI-11-final-handoff.md`
- `scripts/generate-ai11-skill-packages.py`

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
- `docs/standards/skill-authoring-standard.md`
- `docs/standards/skill-naming-standard.md`
- `docs/standards/output-contract-standard.md`
- `docs/standards/testing-standard.md`
- `docs/foundations/professional-vocabulary.md`
- `docs/foundations/shared-schemas.md`
- `docs/foundations/report-structure-contracts.md`
- `docs/development/handoffs/AI-10-final-handoff.md`

# Validation Performed

```powershell
.\scripts\validate-all.ps1
python .\scripts\validate-skills.py --repo-root D:\AgentInvestigate
Get-ChildItem -LiteralPath 'D:\AgentInvestigate\skills\04-investigation-planning-case-management' -Directory | ForEach-Object { python 'C:\Users\jerem\.codex\skills\.system\skill-creator\scripts\quick_validate.py' $_.FullName }
git diff --check
```

# Tests

AI-11 adds scenario fixtures for all 13 case-management skills. Each skill has positive routing coverage and negative-routing coverage for prohibited record manipulation.

No live before/after model evaluation was run in AI-11.

# Safety / Regulatory Review

- Case-management skills do not approve investigative action, surveillance, screening, record access, or regulated compliance action.
- Skills preserve authority and jurisdiction gates from AI-10.
- Skills separate planned work, completed work, facts, assumptions, inferences, unknowns, gaps, and review needs.
- Negative-routing scenarios cover attempts to fabricate, backdate, alter, conceal, overstate, or sanitize case records.

# Known Limitations

- AI-11 does not create role-level skillsets yet.
- AI-11 does not add jurisdiction-specific law libraries, regulatory source maps, or retention schedules.
- Future role composition should route case-management work through AI-09 professional-core and AI-10 authority/compliance checks.

# Explicitly Not Completed

- No AI-12 research, OSINT, or public-records skills.
- No skillsets.
- No specializations.
- No jurisdiction-specific rule database.
- No full before/after evaluation reports.

# Recommended Next Wave

AI-12: Research, OSINT & Public Records.
