# Wave

AI-16

# Objective

Build Family 09, Investigative Analysis, with evidence-bounded hypotheses, alternative explanations, contradictions, chronologies, source weight, finding confidence, unresolved questions, and draft findings.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_16_INVESTIGATIVE_ANALYSIS_READY
```

# Scope Completed

- Preserved and upgraded the existing `build-evidence-matrix` reference implementation for Family 09.
- Created the remaining 10 `09-investigative-analysis` skills from the canonical taxonomy.
- Added OpenAI adapter metadata for each new investigative-analysis skill.
- Added one scoped reference file for each new Family 09 skill.
- Added AI-16 investigative-analysis scenario fixtures with positive and negative-routing coverage for each Family 09 skill.
- Added the required hard reasoning rule: `FACT ≠ INFERENCE ≠ ALLEGATION ≠ FINDING`.
- Added the required gate coverage for plausible but incorrect hypotheses and disconfirming evidence.
- Added validator checks for Family 09 completion, reasoning-rule coverage, reasoning-category coverage, and disconfirming-evidence scenario coverage.

# Family 09 Skills

- `build-evidence-matrix`
- `generate-investigative-hypotheses`
- `test-investigative-hypothesis`
- `compare-alternative-explanations`
- `identify-evidence-contradiction`
- `construct-event-chronology`
- `analyze-pattern-of-events`
- `assess-source-weight`
- `assess-finding-confidence`
- `identify-unresolved-question`
- `draft-investigative-finding`

# Hard Reasoning Rule

```text
FACT ≠ INFERENCE ≠ ALLEGATION ≠ FINDING
```

# Gate

Integration tests must include plausible but incorrect hypotheses, and the agent must consider disconfirming evidence.

# Files Added

- `skills/09-investigative-analysis/generate-investigative-hypotheses/*`
- `skills/09-investigative-analysis/test-investigative-hypothesis/*`
- `skills/09-investigative-analysis/compare-alternative-explanations/*`
- `skills/09-investigative-analysis/identify-evidence-contradiction/*`
- `skills/09-investigative-analysis/construct-event-chronology/*`
- `skills/09-investigative-analysis/analyze-pattern-of-events/*`
- `skills/09-investigative-analysis/assess-source-weight/*`
- `skills/09-investigative-analysis/assess-finding-confidence/*`
- `skills/09-investigative-analysis/identify-unresolved-question/*`
- `skills/09-investigative-analysis/draft-investigative-finding/*`
- `tests/reference-skills/AI-16-investigative-analysis-scenarios.json`
- `docs/development/handoffs/AI-16-final-handoff.md`
- `scripts/generate-ai16-skill-packages.py`

# Files Modified

- `README.md`
- `CHANGELOG.md`
- `scripts/validate-docs.py`
- `scripts/validate-skills.py`
- `skills/09-investigative-analysis/build-evidence-matrix/SKILL.md`
- `skills/09-investigative-analysis/build-evidence-matrix/references/evidence-matrix-reference.md`

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
- `docs/development/handoffs/AI-15-final-handoff.md`

# Validation Performed

```powershell
.\scripts\validate-all.ps1
python .\scripts\validate-skills.py --repo-root D:\AgentInvestigate
Get-ChildItem -LiteralPath 'D:\AgentInvestigate\skills\09-investigative-analysis' -Directory | ForEach-Object { python 'C:\Users\jerem\.codex\skills\.system\skill-creator\scripts\quick_validate.py' $_.FullName }
git diff --check
```

# Tests

AI-16 adds scenario fixtures for all 11 investigative-analysis skills. Each skill has positive routing coverage and negative-routing coverage for forced-conclusion or disconfirming-evidence suppression requests.

The representative gate scenario tests a plausible but incorrect hypothesis against disconfirming evidence and requires facts, inferences, allegations, and findings to remain separate.

No live before/after model evaluation was run in AI-16.

# Safety / Regulatory Review

- Family 09 supports evidence matrices, hypotheses, hypothesis testing, alternative explanations, contradiction identification, chronologies, pattern analysis, source weight, finding confidence, unresolved questions, and draft findings only.
- Skills refuse or reroute requests to fabricate, alter, conceal, overstate, or selectively ignore evidence.
- Skills refuse or reroute requests to force a preferred conclusion, suppress plausible alternatives, or ignore disconfirming evidence.
- Skills do not decide legal, employment, disciplinary, licensing, privacy, liability, guilt, admissibility, forensic, or final professional conclusions.
- Skills preserve supplied facts, evidence records, source references, allegations, hypotheses, contradictions, disconfirming evidence, limitations, confidence limits, and unresolved questions as separate categories.

# Known Limitations

- AI-16 does not perform live evidence collection, forensic analysis, external investigation, or automated truth determination.
- AI-16 does not add jurisdiction-specific legal standards, employment investigation standards, evidentiary rules, or finding thresholds.
- Analysis outputs remain draft investigative support requiring responsible human review before consequential use.

# Explicitly Not Completed

- No AI-17 reporting, findings, or case presentation skills.
- No skillsets.
- No specializations.
- No jurisdiction-specific finding or proof-standard database.
- No live before/after evaluation reports.

# Recommended Next Wave

AI-17: Reporting, Findings & Case Presentation.
