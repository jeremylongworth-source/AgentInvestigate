# Wave

AI-14

# Objective

Build Family 07, Interviewing, Witnesses & Statements, with neutral questioning, statement handling, corroboration planning, and explicit prohibitions on unsupported behavioral deception inference.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_14_INTERVIEWING_READY
```

# Scope Completed

- Created all 10 `07-interviewing-witnesses-statements` skills from the canonical taxonomy.
- Added OpenAI adapter metadata for each interviewing, witness, and statement skill.
- Added one scoped reference file for each Family 07 skill.
- Added AI-14 interviewing scenario fixtures with positive and negative-routing coverage for each skill.
- Added required emphasis coverage for neutral questioning, objectives, sequencing, information gaps, statements, notes, consistency, corroboration, follow-up, and bias.
- Added prohibited-inference coverage for body language, eye contact, nervousness, personality, and unsupported behavioral stereotypes.
- Added validator checks for Family 07 completion, prohibited-inference terms in skill packages, prohibited-inference fixture coverage, and required emphasis fixture coverage.

# Family 07 Skills

- `define-interview-objectives`
- `prepare-neutral-question-set`
- `sequence-interview-topics`
- `identify-interview-information-gaps`
- `prepare-witness-interview-plan`
- `summarize-witness-statement`
- `compare-statement-consistency`
- `identify-corroboration-needs`
- `prepare-follow-up-questions`
- `review-interview-bias-risk`

# Required Emphasis

- neutral questioning
- objectives
- sequencing
- information gaps
- statements
- notes
- consistency
- corroboration
- follow-up
- bias

# Prohibited Inference Boundary

Family 07 skills must not infer deception solely from:

- body language
- eye contact
- nervousness
- personality
- unsupported behavioral stereotypes

# Files Added

- `skills/07-interviewing-witnesses-statements/*`
- `tests/reference-skills/AI-14-interviewing-scenarios.json`
- `docs/development/handoffs/AI-14-final-handoff.md`
- `scripts/generate-ai14-skill-packages.py`

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
- `docs/development/handoffs/AI-13-final-handoff.md`

# Validation Performed

```powershell
.\scripts\validate-all.ps1
python .\scripts\validate-skills.py --repo-root D:\AgentInvestigate
Get-ChildItem -LiteralPath 'D:\AgentInvestigate\skills\07-interviewing-witnesses-statements' -Directory | ForEach-Object { python 'C:\Users\jerem\.codex\skills\.system\skill-creator\scripts\quick_validate.py' $_.FullName }
git diff --check
```

# Tests

AI-14 adds scenario fixtures for all 10 interviewing, witness, and statement skills. Each skill has positive routing coverage and negative-routing coverage for prohibited behavioral-inference and coercive-pressure requests.

No live before/after model evaluation was run in AI-14.

# Safety / Regulatory Review

- Family 07 supports neutral interview preparation, note handling, statement summarization, consistency comparison, corroboration planning, follow-up drafting, and bias review only.
- Skills refuse or reroute coercive interviewing, interrogation tactics, intimidation, deception, impersonation, witness coaching, false statement drafting, and pressure scripts.
- Skills do not infer deception, credibility, intent, culpability, admissibility, liability, employment discipline, or legal consequences.
- Skills preserve supplied facts, statement claims, notes, source references, gaps, inconsistencies, assumptions, unknowns, corroboration needs, and bias risks as separate categories.
- Protected interviews, minors, vulnerable persons, trauma, emergency threats, employment consequences, privacy issues, recording requirements, and jurisdiction-specific rules require qualified human review.

# Known Limitations

- AI-14 does not conduct live interviews or create recording/transcription tooling.
- AI-14 does not add jurisdiction-specific interview law, employment investigation procedure, trauma-informed protocol, or child/vulnerable-person interview databases.
- Interview outputs remain draft planning and analysis aids that require responsible human review before consequential use.

# Explicitly Not Completed

- No AI-15 evidence or chain-of-custody skills.
- No skillsets.
- No specializations.
- No jurisdiction-specific interview rules database.
- No live before/after evaluation reports.

# Recommended Next Wave

AI-15: Evidence & Chain of Custody.
