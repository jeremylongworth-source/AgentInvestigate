# Wave

AI-17

# Objective

Build Family 11, Reporting, Findings & Case Presentation, with investigative reports, incident reports, chronologies, evidence summaries, findings matrices, executive summaries, report QA, case presentations, testimony-support outlines, and limitation review.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_17_REPORTING_READY
```

# Scope Completed

- Created all 10 `11-reporting-findings-case-presentation` skills from the canonical taxonomy.
- Added OpenAI adapter metadata for each reporting, findings, and case-presentation skill.
- Added one scoped reference file for each Family 11 skill.
- Added AI-17 reporting scenario fixtures with positive and negative-routing coverage for each skill.
- Added the required report-field gate for facts, sources, evidence, inference, limitations, unresolved questions, and confidence.
- Added testimony-support boundary coverage for witness coaching, false testimony, cross-examination evasion, and material weakness suppression.
- Added validator checks for Family 11 completion, report-field coverage, required output coverage, and testimony-boundary scenario coverage.

# Family 11 Skills

- `write-investigative-report`
- `write-incident-report`
- `prepare-case-chronology`
- `summarize-evidence`
- `prepare-findings-matrix`
- `write-executive-summary`
- `review-report-quality`
- `prepare-case-presentation`
- `prepare-testimony-support-outline`
- `identify-report-limitations`

# Required Report Fields

- facts
- sources
- evidence
- inference
- limitations
- unresolved questions
- confidence

# Required Outputs

- investigative reports
- incident reports
- chronology
- evidence summaries
- findings matrices
- executive summaries
- report QA
- case presentations
- testimony-support outlines
- report limitations

# Gate

Reports must identify facts, sources, evidence, inference, limitations, unresolved questions, and confidence.

# Files Added

- `skills/11-reporting-findings-case-presentation/*`
- `tests/reference-skills/AI-17-reporting-scenarios.json`
- `docs/development/handoffs/AI-17-final-handoff.md`
- `scripts/generate-ai17-skill-packages.py`

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
- `docs/development/handoffs/AI-16-final-handoff.md`

# Validation Performed

```powershell
.\scripts\validate-all.ps1
python .\scripts\validate-skills.py --repo-root D:\AgentInvestigate
Get-ChildItem -LiteralPath 'D:\AgentInvestigate\skills\11-reporting-findings-case-presentation' -Directory | ForEach-Object { python 'C:\Users\jerem\.codex\skills\.system\skill-creator\scripts\quick_validate.py' $_.FullName }
git diff --check
```

# Tests

AI-17 adds scenario fixtures for all 10 reporting, findings, and case-presentation skills. Each skill has positive routing coverage and negative-routing coverage for report field omission or forced certainty.

The gate scenario requires report QA to identify missing facts, sources, evidence, inference, limitations, unresolved questions, and confidence. The testimony scenario requires refusal of testimony coaching and misleading testimony support.

No live before/after model evaluation was run in AI-17.

# Safety / Regulatory Review

- Family 11 supports report drafting, incident reporting, chronologies, evidence summaries, findings matrices, executive summaries, report QA, case presentations, testimony-support outlines, and limitation identification only.
- Skills refuse or reroute fabricated reports, hidden weaknesses, selective omissions, unsupported findings, false testimony, testimony coaching, cross-examination evasion, and material weakness suppression.
- Skills do not decide legal, employment, disciplinary, licensing, privacy, liability, guilt, admissibility, privilege, compliance, forensic, or final professional conclusions.
- Skills preserve facts, sources, evidence, inferences, allegations, findings, limitations, unresolved questions, confidence, contradictions, and reviewer needs as separate categories.
- Testimony, legal process, protected records, forensic claims, employment outcomes, regulated screening, sensitive personal information, safety risk, and jurisdiction-specific reporting requirements require qualified human review.

# Known Limitations

- AI-17 does not generate final signed reports, live presentations, legal pleadings, testimony scripts, or certified forensic opinions.
- AI-17 does not add jurisdiction-specific court reporting rules, expert testimony standards, report admissibility standards, employment report standards, or legal-review workflows.
- Reporting outputs remain draft support requiring responsible human review before consequential use.

# Explicitly Not Completed

- No AI-18 observation or surveillance governance skills.
- No skillsets.
- No specializations.
- No jurisdiction-specific report rule database.
- No live before/after evaluation reports.

# Recommended Next Wave

AI-18: Observation & Surveillance Governance.
