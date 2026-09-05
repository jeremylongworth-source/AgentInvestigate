# Wave

AI-13

# Objective

Build Family 06, Identity, Entity & Timeline Analysis, with explicit confidence labels and tests that detect identity overclaiming.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_13_ENTITY_ANALYSIS_READY
```

# Scope Completed

- Created all 10 `06-identity-entity-timeline-analysis` skills from the canonical taxonomy.
- Added OpenAI adapter metadata for each identity, entity, and timeline analysis skill.
- Added one scoped reference file for each Family 06 skill.
- Added AI-13 entity-analysis scenario fixtures with positive and negative-routing coverage for each skill.
- Added required capability coverage for identity ambiguity, same-name differentiation, identifier normalization, subject timelines, relationship mapping, association evidence, timeline gaps, and entity contradictions.
- Added the required confidence model: `POSSIBLE`, `PROBABLE`, `CORROBORATED`, `CONFIRMED`, and `UNRESOLVED`.
- Added validator checks for Family 06 completion, confidence labels in skill packages, confidence-model fixture coverage, and identity-overclaiming scenario coverage.

# Family 06 Skills

- `assess-identity-ambiguity`
- `differentiate-same-name-individuals`
- `normalize-person-identifiers`
- `normalize-organization-identifiers`
- `construct-subject-timeline`
- `map-relationship-evidence`
- `assess-association-strength`
- `identify-timeline-gap`
- `resolve-entity-contradiction`
- `state-identity-confidence`

# Required Confidence Model

- `POSSIBLE`
- `PROBABLE`
- `CORROBORATED`
- `CONFIRMED`
- `UNRESOLVED`

# Files Added

- `skills/06-identity-entity-timeline-analysis/*`
- `tests/reference-skills/AI-13-entity-analysis-scenarios.json`
- `docs/development/handoffs/AI-13-final-handoff.md`
- `scripts/generate-ai13-skill-packages.py`

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
- `docs/architecture/intrusive-task-gate.md`
- `docs/architecture/prohibited-capabilities.md`
- `docs/standards/skill-authoring-standard.md`
- `docs/standards/skill-naming-standard.md`
- `docs/standards/output-contract-standard.md`
- `docs/standards/research-and-evidence-standard.md`
- `docs/standards/testing-standard.md`
- `docs/foundations/professional-vocabulary.md`
- `docs/foundations/shared-schemas.md`
- `docs/development/handoffs/AI-12-final-handoff.md`

# Validation Performed

```powershell
.\scripts\validate-all.ps1
python .\scripts\validate-skills.py --repo-root D:\AgentInvestigate
Get-ChildItem -LiteralPath 'D:\AgentInvestigate\skills\06-identity-entity-timeline-analysis' -Directory | ForEach-Object { python 'C:\Users\jerem\.codex\skills\.system\skill-creator\scripts\quick_validate.py' $_.FullName }
git diff --check
```

# Tests

AI-13 adds scenario fixtures for all 10 identity, entity, and timeline analysis skills. Each skill has positive routing coverage and negative-routing coverage for identity overclaiming.

No live before/after model evaluation was run in AI-13.

# Safety / Regulatory Review

- Intrusive identity and person-linking work does not route directly from raw user requests.
- Skills require authority, jurisdiction, human approval, lawful purpose, privacy basis, source provenance, and proportionality before person-linking analysis.
- Skills refuse or reroute requests to identify, locate, track, profile, target, doxx, harass, monitor, or screen a person without required gates.
- Same-name, partial, stale, conflicting, or single-source evidence must not be treated as confirmed identity.
- Source conflicts, gaps, ambiguity, and unresolved alternatives are preserved rather than forced into findings.

# Known Limitations

- AI-13 does not add live identity data connectors or external record-search tooling.
- Identity confidence remains evidence-bounded and requires responsible human review before consequential use.
- Future role composition should route identity work through AI-09 professional-core, AI-10 authority/compliance, AI-11 case-management, and AI-12 research/source gates.

# Explicitly Not Completed

- No AI-14 interviewing, witnesses, or statements skills.
- No skillsets.
- No specializations.
- No jurisdiction-specific identity or screening rule database.
- No live before/after evaluation reports.

# Recommended Next Wave

AI-14: Interviewing, Witnesses & Statements.
