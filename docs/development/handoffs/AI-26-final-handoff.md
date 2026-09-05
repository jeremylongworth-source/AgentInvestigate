# Wave

AI-26

# Objective

Build Family 20, Investigation & Security Program Management, with bounded support for investigative policy, security post orders, procedure review, file audits, program audits, KPIs, training requirements, corrective action, and improvement measurement.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_26_PROGRAM_MANAGEMENT_READY
```

# Scope Completed

- Created all 13 `20-investigation-security-program-management` skills from the canonical taxonomy.
- Added OpenAI adapter metadata for each investigation and security program management skill.
- Added one scoped reference file for each Family 20 skill.
- Added AI-26 program management scenario fixtures with positive and negative-routing coverage for each skill.
- Added program-management element coverage for investigative policy, security post orders, procedure review, file audits, program audits, KPIs, training requirements, corrective action, and improvement measurement.
- Added composition-target coverage for `investigative-case-manager`, `security-supervisor`, `security-operations-manager`, `security-program-manager`, and `corporate-security-manager`.
- Added prohibited-output coverage for legal conclusion, licensing approval, compliance certification, policy approval, disciplinary decision, use-of-force training, weapons training, and fabricated audit.
- Added validator checks for Family 20 completion, program-management elements, composition targets, review boundaries, and prohibited-output boundaries.

# Family 20 Skills

- `draft-investigative-policy`
- `draft-security-post-orders`
- `review-investigative-procedure`
- `review-security-procedure`
- `audit-case-file`
- `audit-security-program`
- `select-investigation-kpis`
- `select-security-kpis`
- `review-training-requirement`
- `track-corrective-action`
- `measure-improvement-result`
- `prepare-program-status-report`
- `identify-program-governance-gap`

# Program Management Elements

- investigative policy
- security post orders
- procedure review
- file audits
- program audits
- KPIs
- training requirements
- corrective action
- improvement measurement

# Composition Targets

- `investigative-case-manager`
- `security-supervisor`
- `security-operations-manager`
- `security-program-manager`
- `corporate-security-manager`

# Prohibited Output Boundaries

- legal conclusion
- licensing approval
- compliance certification
- policy approval
- disciplinary decision
- use-of-force training
- weapons training
- fabricated audit

# Review Boundaries

- management review
- legal review
- HR review
- privacy review
- licensing review
- qualified training review

# Boundary

Investigation and security program management skills must not provide:

- legal conclusions
- licensing approval
- compliance certification
- policy approval
- disciplinary decisions
- use-of-force training
- weapons training
- fabricated audit findings
- final HR decisions
- final management signoff
- regulatory certification
- professional certification

The skills support program drafting, policy/procedure review, audit structure, KPI framing, training-requirement issue spotting, corrective-action tracking, improvement measurement, status reporting, and governance-gap identification. They do not approve policies, certify compliance, certify licensing sufficiency, qualify personnel, authorize discipline, or provide force or weapons instruction.

# Files Added

- `skills/20-investigation-security-program-management/*`
- `tests/reference-skills/AI-26-program-management-scenarios.json`
- `docs/development/handoffs/AI-26-final-handoff.md`
- `scripts/generate-ai26-skill-packages.py`

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
- `docs/architecture/certification-boundaries.md`
- `docs/standards/skill-authoring-standard.md`
- `docs/standards/skill-naming-standard.md`
- `docs/standards/output-contract-standard.md`
- `docs/standards/research-and-evidence-standard.md`
- `docs/standards/testing-standard.md`
- `docs/foundations/professional-vocabulary.md`
- `docs/foundations/shared-schemas.md`
- `docs/development/handoffs/AI-25-final-handoff.md`

# Validation Performed

```powershell
.\scripts\validate-all.ps1
python .\scripts\validate-skills.py --repo-root D:\AgentInvestigate
python .\scripts\validate-docs.py --repo-root D:\AgentInvestigate
Get-ChildItem -LiteralPath 'D:\AgentInvestigate\skills\20-investigation-security-program-management' -Directory | ForEach-Object { python 'C:\Users\jerem\.codex\skills\.system\skill-creator\scripts\quick_validate.py' $_.FullName }
git diff --check
```

# Tests

AI-26 adds scenario fixtures for all 13 investigation and security program management skills. Each skill has positive routing coverage and negative-routing coverage for prohibited output requests.

The program-management elements scenario covers investigative policy, security post orders, procedure review, file audits, program audits, KPIs, training requirements, corrective action, and improvement measurement.

The composition scenario covers `investigative-case-manager`, `security-supervisor`, `security-operations-manager`, `security-program-manager`, and `corporate-security-manager`.

The prohibited-output scenario covers legal conclusion, licensing approval, compliance certification, policy approval, disciplinary decision, use-of-force training, weapons training, and fabricated audit.

No live before/after model evaluation was run in AI-26.

# Safety / Regulatory Review

- Family 20 supports investigative policy drafting, security post order drafting, investigative procedure review, security procedure review, case-file audits, security program audits, investigation KPI selection, security KPI selection, training requirement review, corrective-action tracking, improvement measurement, program status reporting, and governance-gap identification.
- Skills route legal, HR, privacy, licensing, training-certification, compliance, audit-dispute, force, weapons, unclear-authority, and material-consequence work through qualified-review gates.
- Skills refuse or reroute legal conclusions, licensing approval, compliance certification, policy approval, disciplinary decisions, use-of-force training, weapons training, fabricated audits, hidden gaps, and final signoff.
- Skills do not certify compliance, approve licensing sufficiency, approve policies, qualify personnel, authorize discipline, provide force or weapons instruction, or replace management/legal/HR/privacy/licensing/training review.

# Known Limitations

- AI-26 does not provide legal, HR, privacy, licensing, regulatory, training-certification, use-of-force, weapons, compliance, or audit certification.
- AI-26 does not add jurisdiction-specific policy, licensing, employment, privacy, use-of-force, weapons, security-training, or regulatory rule databases.
- Program-management outputs remain draft governance support requiring responsible human review before consequential use.

# Explicitly Not Completed

- No AI-27 Canadian federal regulatory specialization.
- No skillsets.
- No specializations.
- No jurisdiction-specific investigation, security, licensing, employment, privacy, training, or regulatory database.
- No live before/after evaluation reports.

# Recommended Next Wave

AI-27: Canadian Federal Regulatory Foundation.
