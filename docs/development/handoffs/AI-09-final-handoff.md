# Wave

AI-09

# Objective

Build Family 01, Professional Core & Ethics, as the first full roadmap family of AgentInvestigate skills.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_09_PROFESSIONAL_CORE_READY
```

# Scope Completed

- Created all nine `01-professional-core-ethics` skills.
- Added OpenAI adapter metadata for each professional-core skill.
- Added one scoped reference file for each professional-core skill.
- Added AI-09 scenario fixtures with positive and negative-routing coverage for each skill.
- Extended skill validation to cover both AI-08 reference skills and AI-09 professional-core skills.
- Added documentation validation for the AI-09 scenario fixture and handoff.

# Professional Core Skills

| Skill | Sensitivity | Boundary |
|---|---|---|
| `define-professional-role-boundaries` | `ROUTINE` | Clarifies role, authority, and exclusions without conferring legal, licensing, or law-enforcement authority. |
| `assess-conflict-of-interest` | `ROUTINE` | Spots conflict indicators and review needs without granting waivers or final legal conclusions. |
| `apply-ethical-decision-framework` | `ROUTINE` | Structures ethical decision review without justifying prohibited conduct or replacing responsible human judgment. |
| `identify-investigative-bias` | `ROUTINE` | Identifies bias risks while preserving contrary facts and avoiding evidence manipulation. |
| `separate-fact-from-inference` | `ROUTINE` | Labels facts, allegations, inferences, assumptions, and unknowns without strengthening unsupported evidence. |
| `assess-duty-of-care` | `ROUTINE` | Identifies care, safety, and escalation considerations without legal or certification determinations. |
| `protect-confidential-information` | `ROUTINE` | Flags confidentiality handling needs without authorizing disclosure or certifying privacy compliance. |
| `identify-escalation-requirement` | `ROUTINE` | Identifies escalation triggers and review owners without bypassing qualified review. |
| `document-professional-decision` | `ROUTINE` | Records decisions with facts, reasoning, limitations, and review needs without fabrication, backdating, or omission. |

# Files Added

- `skills/01-professional-core-ethics/define-professional-role-boundaries/SKILL.md`
- `skills/01-professional-core-ethics/define-professional-role-boundaries/agents/openai.yaml`
- `skills/01-professional-core-ethics/define-professional-role-boundaries/references/role-boundary-checklist.md`
- `skills/01-professional-core-ethics/assess-conflict-of-interest/SKILL.md`
- `skills/01-professional-core-ethics/assess-conflict-of-interest/agents/openai.yaml`
- `skills/01-professional-core-ethics/assess-conflict-of-interest/references/conflict-check-reference.md`
- `skills/01-professional-core-ethics/apply-ethical-decision-framework/SKILL.md`
- `skills/01-professional-core-ethics/apply-ethical-decision-framework/agents/openai.yaml`
- `skills/01-professional-core-ethics/apply-ethical-decision-framework/references/ethical-decision-reference.md`
- `skills/01-professional-core-ethics/identify-investigative-bias/SKILL.md`
- `skills/01-professional-core-ethics/identify-investigative-bias/agents/openai.yaml`
- `skills/01-professional-core-ethics/identify-investigative-bias/references/bias-review-reference.md`
- `skills/01-professional-core-ethics/separate-fact-from-inference/SKILL.md`
- `skills/01-professional-core-ethics/separate-fact-from-inference/agents/openai.yaml`
- `skills/01-professional-core-ethics/separate-fact-from-inference/references/fact-inference-reference.md`
- `skills/01-professional-core-ethics/assess-duty-of-care/SKILL.md`
- `skills/01-professional-core-ethics/assess-duty-of-care/agents/openai.yaml`
- `skills/01-professional-core-ethics/assess-duty-of-care/references/duty-of-care-reference.md`
- `skills/01-professional-core-ethics/protect-confidential-information/SKILL.md`
- `skills/01-professional-core-ethics/protect-confidential-information/agents/openai.yaml`
- `skills/01-professional-core-ethics/protect-confidential-information/references/confidentiality-handling-reference.md`
- `skills/01-professional-core-ethics/identify-escalation-requirement/SKILL.md`
- `skills/01-professional-core-ethics/identify-escalation-requirement/agents/openai.yaml`
- `skills/01-professional-core-ethics/identify-escalation-requirement/references/escalation-routing-reference.md`
- `skills/01-professional-core-ethics/document-professional-decision/SKILL.md`
- `skills/01-professional-core-ethics/document-professional-decision/agents/openai.yaml`
- `skills/01-professional-core-ethics/document-professional-decision/references/professional-decision-record-reference.md`
- `tests/reference-skills/AI-09-professional-core-scenarios.json`
- `docs/development/handoffs/AI-09-final-handoff.md`

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
- `docs/foundations/foundation-catalog.md`
- `docs/foundations/professional-vocabulary.md`
- `docs/foundations/shared-schemas.md`
- `docs/foundations/report-structure-contracts.md`
- `docs/development/handoffs/AI-08-final-handoff.md`

# Validation Performed

```powershell
.\scripts\validate-all.ps1
python .\scripts\validate-skills.py --repo-root D:\AgentInvestigate
Get-ChildItem -LiteralPath 'D:\AgentInvestigate\skills\01-professional-core-ethics' -Directory | ForEach-Object { python 'C:\Users\jerem\.codex\skills\.system\skill-creator\scripts\quick_validate.py' $_.FullName }
git diff --check
```

# Tests

AI-09 adds scenario fixtures for all professional-core skills. Each skill has at least one positive routing scenario and one negative-routing scenario.

No live before/after model evaluation was run in AI-09. The scenario suite is ready for future evaluation reports.

# Safety / Regulatory Review

- No skill confers private-investigator, private-security, law-enforcement, legal, privacy-compliance, employment, emergency-response, or technical certification authority.
- No jurisdiction-specific legal or regulatory rule was encoded as universal.
- Conflict, care, confidentiality, escalation, and decision-record work is framed as issue spotting and professional documentation support.
- Negative-routing scenarios cover impersonation, coercion, conflict concealment, evidence manipulation, covert tracking justification, unsupported fact conversion, threat disregard, unauthorized disclosure, escalation bypass, and backdating.

# Known Limitations

- The professional-core family is initial implementation content, not a substitute for organization-specific policy, legal review, or qualified professional judgment.
- These skills are all `ROUTINE` by taxonomy, but each declares when to upgrade to `REGULATED`, `INTRUSIVE`, or `CERTIFICATION_BOUNDARY`.
- Future skillset composition should route other families through professional-core checks where applicable.

# Explicitly Not Completed

- No AI-10 intake, authority, law, or privacy skills.
- No skillsets.
- No specializations.
- No jurisdiction-specific source maps.
- No full before/after evaluation reports.

# Recommended Next Wave

AI-10: Intake, Authority, Law & Privacy.
