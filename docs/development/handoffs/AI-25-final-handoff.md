# Wave

AI-25

# Objective

Build Family 19, Loss Prevention & Asset Protection, with bounded support for asset risk, loss events, shrink patterns, incident triage, evidence mapping, process-control weaknesses, case summaries, and improvement planning.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_25_LOSS_PREVENTION_READY
```

# Scope Completed

- Created all 8 `19-loss-prevention-asset-protection` skills from the canonical taxonomy.
- Added OpenAI adapter metadata for each loss prevention and asset protection skill.
- Added one scoped reference file for each Family 19 skill.
- Added AI-25 loss prevention scenario fixtures with positive and negative-routing coverage for each skill.
- Added loss-prevention element coverage for asset protection risk, loss event, shrink pattern, loss prevention incident, loss event evidence, process control weakness, case summary, and improvement plan.
- Added composition-target coverage for `loss-prevention-officer`, `loss-prevention-investigator`, and `asset-protection-specialist`.
- Added prohibited-conduct coverage for physical intervention instruction, detention, search, pursuit, restraint techniques, coercive questioning, unsupported theft conclusion, and criminal guilt.
- Added validator checks for Family 19 completion, loss-prevention element coverage, composition targets, review boundaries, and prohibited-conduct boundaries.

# Family 19 Skills

- `assess-asset-protection-risk`
- `analyze-loss-event`
- `analyze-shrink-pattern`
- `triage-loss-prevention-incident`
- `map-loss-event-evidence`
- `identify-process-control-weakness`
- `prepare-loss-prevention-case-summary`
- `build-asset-protection-improvement-plan`

# Loss-Prevention Elements

- asset protection risk
- loss event
- shrink pattern
- loss prevention incident
- loss event evidence
- process control weakness
- case summary
- improvement plan

# Composition Targets

- `loss-prevention-officer`
- `loss-prevention-investigator`
- `asset-protection-specialist`

# Prohibited Conduct Boundaries

- physical intervention instruction
- detention
- search
- pursuit
- restraint techniques
- coercive questioning
- unsupported theft conclusion
- criminal guilt

# Review Boundaries

- manager review
- legal review
- HR review
- law-enforcement referral review

# Boundary

Loss prevention and asset protection skills must not provide:

- physical intervention instruction
- detention instructions
- search instructions
- pursuit instructions
- restraint techniques
- coercive questioning
- forced confession tactics
- unsupported theft conclusions
- criminal guilt conclusions
- final HR decisions
- final legal conclusions
- restitution demands
- law-enforcement charging recommendations

The skills support documentation, analysis, evidence mapping, process-control review, case summaries, and improvement planning. They do not authorize detention, search, pursuit, physical intervention, questioning, discipline, termination, restitution, criminal referral, or legal action.

# Files Added

- `skills/19-loss-prevention-asset-protection/*`
- `tests/reference-skills/AI-25-loss-prevention-scenarios.json`
- `docs/development/handoffs/AI-25-final-handoff.md`
- `scripts/generate-ai25-skill-packages.py`

# Files Modified

- `README.md`
- `CHANGELOG.md`
- `scripts/validate-docs.py`
- `scripts/validate-skills.py`

# Sources

- `ROADMAP.md`
- `docs/architecture/taxonomy-index.yaml`
- `docs/architecture/domain-contract.md`
- `docs/architecture/scope-boundaries.md`
- `docs/architecture/prohibited-capabilities.md`
- `docs/architecture/sensitivity-model.md`
- `docs/architecture/authority-routing.md`
- `docs/architecture/intrusive-task-gate.md`
- `docs/standards/skill-authoring-standard.md`
- `docs/standards/skill-naming-standard.md`
- `docs/standards/output-contract-standard.md`
- `docs/standards/research-and-evidence-standard.md`
- `docs/standards/testing-standard.md`
- `docs/foundations/professional-vocabulary.md`
- `docs/foundations/shared-schemas.md`
- `docs/development/handoffs/AI-24-final-handoff.md`

# Validation Performed

```powershell
.\scripts\validate-all.ps1
python .\scripts\validate-skills.py --repo-root D:\AgentInvestigate
python .\scripts\validate-docs.py --repo-root D:\AgentInvestigate
Get-ChildItem -LiteralPath 'D:\AgentInvestigate\skills\19-loss-prevention-asset-protection' -Directory | ForEach-Object { python 'C:\Users\jerem\.codex\skills\.system\skill-creator\scripts\quick_validate.py' $_.FullName }
git diff --check
```

# Tests

AI-25 adds scenario fixtures for all 8 loss prevention and asset protection skills. Each skill has positive routing coverage and negative-routing coverage for prohibited conduct requests.

The loss-prevention elements scenario covers asset protection risk, loss event, shrink pattern, loss prevention incident, loss event evidence, process control weakness, case summary, and improvement plan.

The composition scenario covers `loss-prevention-officer`, `loss-prevention-investigator`, and `asset-protection-specialist`.

The prohibited-conduct scenario covers physical intervention instruction, detention, search, pursuit, restraint techniques, coercive questioning, unsupported theft conclusion, and criminal guilt.

No live before/after model evaluation was run in AI-25.

# Safety / Regulatory Review

- Family 19 supports asset-protection risk assessment, loss-event analysis, shrink-pattern analysis, loss-prevention incident triage, evidence mapping, process-control weakness identification, case summaries, and improvement planning.
- Skills route legal, HR, privacy, law-enforcement referral, safety, physical intervention, detention, search, pursuit, unclear-authority, and material-consequence work through qualified-review gates.
- Skills refuse or reroute physical intervention instruction, detention, search, pursuit, restraint techniques, coercive questioning, forced confession tactics, unsupported theft conclusions, criminal guilt conclusions, fabricated records, hidden evidence gaps, and final consequential decisions.
- Skills do not determine criminal guilt, make final HR decisions, authorize discipline, authorize restitution, authorize law-enforcement referral, or provide enforcement tactics.

# Known Limitations

- AI-25 does not provide legal, HR, employment, privacy, law-enforcement, use-of-force, detention, search, or physical security authorization.
- AI-25 does not add jurisdiction-specific shopkeeper privilege, detention, search, privacy, employment, restitution, or criminal-law rule databases.
- Loss-prevention outputs remain draft analytical support requiring responsible human review before consequential use.

# Explicitly Not Completed

- No AI-26 investigation and security program management skills.
- No skillsets.
- No specializations.
- No jurisdiction-specific loss-prevention, employment, privacy, detention, search, restitution, or criminal-law database.
- No live before/after evaluation reports.

# Recommended Next Wave

AI-26: Investigation & Security Program Management.
