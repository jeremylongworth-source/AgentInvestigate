# Wave

AI-22

# Objective

Build Families 15 and 16, Incident Response and Communication & De-escalation, with incident capabilities, communication capabilities, and the certification boundary against physical intervention instruction.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_22_INCIDENT_COMMUNICATION_READY
```

# Scope Completed

- Created or updated all 9 `15-incident-response` skills from the canonical taxonomy.
- Created all 8 `16-communication-deescalation` skills from the canonical taxonomy.
- Updated `determine-emergency-escalation` from the reference implementation into the AI-22 family format while preserving its `references/emergency-escalation-checklist.md` path.
- Added OpenAI adapter metadata for each incident response and communication skill.
- Added one scoped reference file for each Family 15 and Family 16 skill.
- Added AI-22 incident and communication scenario fixtures with positive and negative-routing coverage for each skill.
- Added incident capability coverage for recognition, escalation, notification, scene preservation, emergency-service support, documentation, and post-incident review.
- Added communication capability coverage for conflict avoidance, de-escalation, radio communication, incident notification, audience adaptation, and bias review.
- Added validator checks for Family 15 and Family 16 completion, capability coverage, and the no-physical-intervention certification boundary.

# Family 15 Skills

- `triage-security-incident`
- `determine-emergency-escalation`
- `support-emergency-service-access`
- `preserve-incident-scene`
- `identify-incident-notification-requirement`
- `document-incident-timeline`
- `collect-incident-account`
- `prepare-post-incident-review`
- `identify-corrective-action`

# Family 16 Skills

- `assess-conflict-risk`
- `prepare-deescalation-communication-plan`
- `draft-radio-communication`
- `prepare-incident-notification`
- `adapt-message-to-audience`
- `review-communication-bias`
- `document-deescalation-attempt`
- `identify-communication-escalation-need`

# Incident Capabilities

- recognition
- escalation
- notification
- scene preservation
- emergency-service support
- documentation
- post-incident review

# Communication Capabilities

- conflict avoidance
- de-escalation
- radio communication
- incident notification
- audience adaptation
- bias review

# Certification Boundary

No physical intervention instruction.

The AI does not provide:

- physical intervention instruction
- use of force
- restraint techniques
- weapons use
- tactical confrontation
- pursuit
- detention
- search
- seizure
- emergency-service substitution

# Files Added

- `skills/15-incident-response/*`
- `skills/16-communication-deescalation/*`
- `tests/reference-skills/AI-22-incident-communication-scenarios.json`
- `docs/development/handoffs/AI-22-final-handoff.md`
- `scripts/generate-ai22-skill-packages.py`

# Files Modified

- `README.md`
- `CHANGELOG.md`
- `scripts/validate-docs.py`
- `scripts/validate-skills.py`
- `skills/15-incident-response/determine-emergency-escalation/SKILL.md`
- `skills/15-incident-response/determine-emergency-escalation/agents/openai.yaml`
- `skills/15-incident-response/determine-emergency-escalation/references/emergency-escalation-checklist.md`

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
- `docs/development/handoffs/AI-21-final-handoff.md`

# Validation Performed

```powershell
.\scripts\validate-all.ps1
python .\scripts\validate-skills.py --repo-root D:\AgentInvestigate
Get-ChildItem -LiteralPath 'D:\AgentInvestigate\skills\15-incident-response' -Directory | ForEach-Object { python 'C:\Users\jerem\.codex\skills\.system\skill-creator\scripts\quick_validate.py' $_.FullName }
Get-ChildItem -LiteralPath 'D:\AgentInvestigate\skills\16-communication-deescalation' -Directory | ForEach-Object { python 'C:\Users\jerem\.codex\skills\.system\skill-creator\scripts\quick_validate.py' $_.FullName }
git diff --check
```

# Tests

AI-22 adds scenario fixtures for all 17 incident response and communication/de-escalation skills. Each skill has positive routing coverage and negative-routing coverage for prohibited physical intervention requests.

The incident capability scenario covers recognition, escalation, notification, scene preservation, emergency-service support, documentation, and post-incident review.

The communication capability scenario covers conflict avoidance, de-escalation, radio communication, incident notification, audience adaptation, and bias review.

No live before/after model evaluation was run in AI-22.

# Safety / Regulatory Review

- Family 15 supports incident triage, emergency escalation recognition, emergency-service access handoff, scene-preservation notes, notification requirement issue spotting, incident timelines, incident account collection, post-incident review, and corrective-action identification.
- Family 16 supports conflict-risk assessment, de-escalation communication planning, radio communication drafting, incident notification drafting, audience adaptation, communication bias review, de-escalation attempt documentation, and communication escalation triage.
- Skills route emergency-adjacent, medical, fire, life-safety, use-of-force, scene-preservation, regulated notification, licensing, unclear-authority, and unsafe work through emergency, supervisor, qualified-review, source, and documentation gates.
- Skills refuse or reroute physical intervention instruction, use of force, restraint techniques, weapons use, tactical confrontation, pursuit, detention, search, emergency-service substitution, fabricated records, hidden gaps, and impersonation.
- Skills do not decide legal, medical, fire, life-safety, criminal, disciplinary, liability, compliance, use-of-force, or enforcement outcomes.

# Known Limitations

- AI-22 does not provide live emergency response, emergency dispatch, medical advice, fire response, physical intervention, use-of-force training, restraint training, weapons training, tactical de-escalation training, police instruction, or life-safety certification.
- AI-22 does not add jurisdiction-specific notification, emergency-response, use-of-force, security licensing, privacy, fire, medical, or life-safety law databases.
- Incident response and communication outputs remain draft support requiring responsible human review before consequential use.

# Explicitly Not Completed

- No AI-23 physical security or risk assessment skills.
- No skillsets.
- No specializations.
- No jurisdiction-specific incident response or communication law database.
- No live before/after evaluation reports.

# Recommended Next Wave

AI-23: Physical Security & Risk Assessment.
