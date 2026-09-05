# Wave

AI-21

# Objective

Build Family 14, Security Operations, Access & Patrol, with all 15 skills and the representative operational lifecycle from post orders through log review.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_21_SECURITY_OPERATIONS_READY
```

# Scope Completed

- Created all 15 `14-security-operations-access-patrol` skills from the canonical taxonomy.
- Added OpenAI adapter metadata for each security operations, access, and patrol skill.
- Added one scoped reference file for each Family 14 skill.
- Added AI-21 security operations scenario fixtures with positive and negative-routing coverage for each skill.
- Added representative lifecycle coverage for post orders, shift plan, patrol, observation, access event, alarm, occurrence, handoff, and log review.
- Added composition-target coverage for `security-officer` and `mobile-patrol-officer`.
- Added validator checks for Family 14 completion, lifecycle coverage, composition targets, and prohibited operational-content boundaries.

# Family 14 Skills

- `review-post-orders`
- `build-shift-plan`
- `plan-patrol-route`
- `document-patrol-observation`
- `log-security-occurrence`
- `verify-access-event`
- `triage-access-control-event`
- `document-visitor-management-issue`
- `record-key-control-event`
- `document-alarm-response`
- `prepare-shift-handoff`
- `review-security-log`
- `identify-post-order-gap`
- `prepare-security-operations-brief`
- `identify-supervisor-notification-need`

# Representative Operational Lifecycle

- post orders
- shift plan
- patrol
- observation
- access event
- alarm
- occurrence
- handoff
- log review

# Composition Targets

- `security-officer`
- `mobile-patrol-officer`

# Boundary

The AI does not provide:

- physical intervention
- use of force
- restraint techniques
- weapons use
- access-control bypass
- lock bypass
- alarm defeat
- law-enforcement impersonation
- tactical confrontation
- detention
- search
- seizure
- final enforcement outcomes

# Files Added

- `skills/14-security-operations-access-patrol/*`
- `tests/reference-skills/AI-21-security-operations-scenarios.json`
- `docs/development/handoffs/AI-21-final-handoff.md`
- `scripts/generate-ai21-skill-packages.py`

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
- `docs/architecture/certification-boundaries.md`
- `docs/architecture/prohibited-capabilities.md`
- `docs/standards/skill-authoring-standard.md`
- `docs/standards/skill-naming-standard.md`
- `docs/standards/output-contract-standard.md`
- `docs/standards/research-and-evidence-standard.md`
- `docs/standards/testing-standard.md`
- `docs/foundations/professional-vocabulary.md`
- `docs/foundations/shared-schemas.md`
- `docs/development/handoffs/AI-20-final-handoff.md`

# Validation Performed

```powershell
.\scripts\validate-all.ps1
python .\scripts\validate-skills.py --repo-root D:\AgentInvestigate
Get-ChildItem -LiteralPath 'D:\AgentInvestigate\skills\14-security-operations-access-patrol' -Directory | ForEach-Object { python 'C:\Users\jerem\.codex\skills\.system\skill-creator\scripts\quick_validate.py' $_.FullName }
git diff --check
```

# Tests

AI-21 adds scenario fixtures for all 15 security operations, access, and patrol skills. Each skill has positive routing coverage and negative-routing coverage for prohibited operational content.

The lifecycle scenario covers post orders, shift plan, patrol, observation, access event, alarm, occurrence, handoff, and log review.

The composition scenario covers `security-officer` and `mobile-patrol-officer`.

No live before/after model evaluation was run in AI-21.

# Safety / Regulatory Review

- Family 14 supports post-order review, shift planning, patrol route planning, patrol observation documentation, occurrence logging, access-event verification, access-control triage, visitor-issue documentation, key-control records, alarm-response documentation, shift handoffs, log review, post-order gap identification, operations briefs, and supervisor notification triage.
- Skills route regulated security-service authority, key control, alarm response, emergency-adjacent work, licensing, use-of-force implications, and unclear authority through jurisdiction, supervisor, emergency, qualified-review, and documentation gates.
- Skills refuse or reroute physical intervention, use of force, restraint techniques, weapons use, access-control bypass, lock bypass, alarm defeat, law-enforcement impersonation, tactical confrontation, fabricated logs, and hidden gaps.
- `document-alarm-response` is a certification-boundary skill for documentation and escalation only. It does not provide building-clearing, alarm-bypass, emergency, technical defeat, or life-safety instructions.
- Skills do not decide legal authority, criminal guilt, discipline, liability, detention, search, seizure, or final enforcement outcomes.

# Known Limitations

- AI-21 does not provide live security operations, emergency dispatch, physical intervention, use-of-force training, alarm technician guidance, access-control engineering, fire or life-safety approval, or legal/security licensing conclusions.
- AI-21 does not add jurisdiction-specific security-service, use-of-force, alarm, access-control, key-control, or emergency-response law databases.
- Security operations outputs remain draft support requiring responsible human review before consequential use.

# Explicitly Not Completed

- No AI-22 incident response, communication, or de-escalation skills.
- No skillsets.
- No specializations.
- No jurisdiction-specific security operations law database.
- No live before/after evaluation reports.

# Recommended Next Wave

AI-22: Incident Response, Communication & De-escalation.
