# Wave

AI-19

# Objective

Build Family 12, Corporate & Workplace Investigations, with an end-to-end allegation-to-report flow and explicit boundaries against deciding discipline, termination, legal liability, or criminal guilt.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_19_WORKPLACE_INVESTIGATIONS_READY
```

# Scope Completed

- Created all 10 `12-corporate-workplace-investigations` skills from the canonical taxonomy.
- Added OpenAI adapter metadata for each corporate and workplace investigation skill.
- Added one scoped reference file for each Family 12 skill.
- Added AI-19 workplace-investigation scenario fixtures with positive and negative-routing coverage for each skill.
- Added the required end-to-end workplace flow from allegation through report.
- Added boundary coverage for discipline, termination, legal liability, and criminal guilt.
- Added validator checks for Family 12 completion, workflow-step coverage, prohibited-decision coverage, and the end-to-end scenario.

# Family 12 Skills

- `classify-workplace-allegation`
- `map-allegation-to-policy`
- `build-allegations-matrix`
- `plan-workplace-investigation`
- `identify-workplace-evidence-sources`
- `prepare-workplace-interview-plan`
- `compare-workplace-statements`
- `assess-evidentiary-support`
- `draft-workplace-finding`
- `prepare-workplace-investigation-report`

# End-To-End Test Flow

- allegation
- scope
- allegations matrix
- policy mapping
- interview planning
- evidence analysis
- statement comparison
- evidentiary support
- findings
- report

# Boundary

The AI does not decide:

- discipline
- termination
- legal liability
- criminal guilt

# Files Added

- `skills/12-corporate-workplace-investigations/*`
- `tests/reference-skills/AI-19-workplace-investigations-scenarios.json`
- `docs/development/handoffs/AI-19-final-handoff.md`
- `scripts/generate-ai19-skill-packages.py`

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
- `docs/development/handoffs/AI-18-final-handoff.md`

# Validation Performed

```powershell
.\scripts\validate-all.ps1
python .\scripts\validate-skills.py --repo-root D:\AgentInvestigate
Get-ChildItem -LiteralPath 'D:\AgentInvestigate\skills\12-corporate-workplace-investigations' -Directory | ForEach-Object { python 'C:\Users\jerem\.codex\skills\.system\skill-creator\scripts\quick_validate.py' $_.FullName }
git diff --check
```

# Tests

AI-19 adds scenario fixtures for all 10 corporate and workplace investigation skills. Each skill has positive routing coverage and negative-routing coverage for prohibited workplace outcome decisions.

The end-to-end scenario covers allegation, scope, allegations matrix, policy mapping, interview planning, evidence analysis, statement comparison, evidentiary support, findings, and report without deciding discipline, termination, legal liability, or criminal guilt.

No live before/after model evaluation was run in AI-19.

# Safety / Regulatory Review

- Family 12 supports allegation classification, policy mapping, allegations matrices, investigation planning, workplace evidence source identification, interview planning, statement comparison, evidentiary support, workplace findings, and workplace investigation reports only.
- Skills route regulated or intrusive workplace work through authority, jurisdiction, privacy, source, and human-review gates.
- Skills refuse or reroute fabricated evidence, coerced witnesses, witness coaching, behavior-only deception inference, retaliation, intimidation, hidden limitations, selective omissions, and forced outcomes.
- Skills do not decide discipline, termination, legal liability, criminal guilt, employment outcomes, legal compliance, admissibility, credibility, or final responsibility.
- Protected classes, harassment, discrimination, retaliation, safety threats, medical information, union issues, surveillance, private records, sensitive personal information, and material consequences require qualified human review.

# Known Limitations

- AI-19 does not perform live workplace investigations, HR decisioning, legal analysis, disciplinary recommendations, or external evidence collection.
- AI-19 does not add jurisdiction-specific employment law, labor law, human-rights law, harassment standard, privacy rule, or policy databases.
- Workplace investigation outputs remain draft support requiring responsible human review before consequential use.

# Explicitly Not Completed

- No AI-20 background screening or due diligence skills.
- No skillsets.
- No specializations.
- No jurisdiction-specific workplace investigation rule database.
- No live before/after evaluation reports.

# Recommended Next Wave

AI-20: Background Screening & Due Diligence.
