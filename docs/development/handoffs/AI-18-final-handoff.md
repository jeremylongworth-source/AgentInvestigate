# Wave

AI-18

# Objective

Build Family 10, Observation & Surveillance Governance, as a controlled high-sensitivity wave with intrusive classification, jurisdiction gates, human review gates, and no operational surveillance tactics.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_18_OBSERVATION_GOVERNANCE_READY
```

# Scope Completed

- Preserved and upgraded the existing `assess-observation-proportionality` reference implementation for Family 10.
- Created the remaining seven `10-observation-surveillance-governance` skills from the canonical taxonomy.
- Added OpenAI adapter metadata for each new observation-governance skill.
- Added one scoped reference file for each new Family 10 skill.
- Added AI-18 observation-governance scenario fixtures with positive and negative-routing coverage for each implemented skill.
- Added mandatory property coverage for `sensitivity: INTRUSIVE`, `jurisdiction_required: true`, and `human_review_required: true`.
- Added prohibited operational coverage for avoiding detection, following targets covertly, counter-surveillance defeat, tracking-device installation, and security evasion.
- Added validator checks for Family 10 completion, mandatory properties, prohibited operational terms, and operational-surveillance-tactics boundaries.

# Family 10 Skills

- `assess-observation-authorization`
- `assess-observation-necessity`
- `assess-observation-proportionality`
- `define-observation-purpose`
- `plan-lawful-observation-assignment`
- `record-field-observation`
- `minimize-third-party-information`
- `review-observation-record-for-compliance`

# Mandatory Properties

- sensitivity: INTRUSIVE
- jurisdiction_required: true
- human_review_required: true

# Explicitly Prohibited Operational Skills

- avoiding detection
- following targets covertly
- counter-surveillance defeat
- tracking-device installation
- security evasion

# Files Added

- `skills/10-observation-surveillance-governance/assess-observation-authorization/*`
- `skills/10-observation-surveillance-governance/assess-observation-necessity/*`
- `skills/10-observation-surveillance-governance/define-observation-purpose/*`
- `skills/10-observation-surveillance-governance/plan-lawful-observation-assignment/*`
- `skills/10-observation-surveillance-governance/record-field-observation/*`
- `skills/10-observation-surveillance-governance/minimize-third-party-information/*`
- `skills/10-observation-surveillance-governance/review-observation-record-for-compliance/*`
- `tests/reference-skills/AI-18-observation-governance-scenarios.json`
- `docs/development/handoffs/AI-18-final-handoff.md`
- `scripts/generate-ai18-skill-packages.py`

# Files Modified

- `README.md`
- `CHANGELOG.md`
- `scripts/validate-docs.py`
- `scripts/validate-skills.py`
- `skills/10-observation-surveillance-governance/assess-observation-proportionality/SKILL.md`
- `skills/10-observation-surveillance-governance/assess-observation-proportionality/references/observation-proportionality-checklist.md`

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
- `docs/development/handoffs/AI-17-final-handoff.md`

# Validation Performed

```powershell
.\scripts\validate-all.ps1
python .\scripts\validate-skills.py --repo-root D:\AgentInvestigate
Get-ChildItem -LiteralPath 'D:\AgentInvestigate\skills\10-observation-surveillance-governance' -Directory | ForEach-Object { python 'C:\Users\jerem\.codex\skills\.system\skill-creator\scripts\quick_validate.py' $_.FullName }
git diff --check
```

# Tests

AI-18 adds scenario fixtures for all eight implemented observation-governance skills. Each skill has positive intrusive-gate coverage and negative-routing coverage for prohibited operational surveillance requests.

The mandatory-properties scenario requires `sensitivity: INTRUSIVE`, `jurisdiction_required: true`, and `human_review_required: true`, and confirms missing jurisdiction or human review blocks operational planning.

No live before/after model evaluation was run in AI-18.

# Safety / Regulatory Review

- Family 10 supports authorization review, necessity review, proportionality review, purpose definition, non-operational assignment briefing, field observation record structure, third-party minimization, and compliance review only.
- Skills route missing jurisdiction, authority, lawful purpose, privacy basis, necessity, proportionality, minimization, or human review to `INTRUSIVE_GATE_REQUIRED`.
- Skills refuse or reroute avoiding detection, following targets covertly, counter-surveillance defeat, tracking-device installation, security evasion, routes, schedules, concealment tactics, tracker placement, camera defeat, alarm defeat, access-control bypass, stalking, intimate-partner monitoring, confrontation tactics, and live pursuit instructions.
- Skills do not authorize observation, certify legality, decide privacy compliance, approve employment action, replace counsel, replace a licensed investigator, conduct surveillance, or provide operational tactics.
- Legal, privacy, employment, licensing, compliance, minors, vulnerable persons, emergency threats, weapons, confrontation, law-enforcement powers, and use-of-force issues require qualified human review or escalation.

# Known Limitations

- AI-18 does not perform live observation, generate surveillance routes, provide covert-following tactics, install tracking devices, or integrate with field operations systems.
- AI-18 does not add jurisdiction-specific surveillance law, licensing rules, employment monitoring rules, or privacy-law databases.
- Observation outputs remain governance, gate, documentation, minimization, and review support requiring responsible human control.

# Explicitly Not Completed

- No AI-19 corporate or workplace investigation skills.
- No skillsets.
- No specializations.
- No jurisdiction-specific surveillance rule database.
- No live before/after evaluation reports.

# Recommended Next Wave

AI-19: Corporate & Workplace Investigations.
