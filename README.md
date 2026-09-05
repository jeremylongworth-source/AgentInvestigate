# AgentInvestigate

AgentInvestigate is an open-source AI skill repository for lawful professional investigation and private security support work.

It helps agents produce bounded, reviewable outputs for intake, lawful-purpose checks, authority review, source handling, evidence organization, interviews, investigative analysis, reporting, security operations, incident response, physical security, loss prevention, program management, professional skillset composition, integration evaluation, adversarial safety evaluation, and future specialist-module planning.

Public readiness token:

```text
AGENTINVESTIGATE_AI_36_PUBLIC_READINESS_READY
```

Core principles:

```text
AUTHORITY BEFORE ACTION
EVIDENCE BEFORE CONCLUSION
HUMAN CONTROL BEFORE INTRUSIVE WORK
```

AgentInvestigate does not confer investigator licensing, security licensing, law-enforcement authority, legal authority, regulatory approval, use-of-force qualification, weapons qualification, emergency-response certification, engineering approval, fire or life-safety approval, privacy compliance certification, or professional certification.

## Who It Is For

AgentInvestigate is for:

- maintainers building and reviewing investigative or security-oriented AI skills;
- evaluators testing routing, safety, evidence discipline, and privacy behavior;
- contributors adding roadmap-scoped skills, fixtures, validators, and documentation;
- organizations that need reusable skill patterns for lawful investigation, case management, security operations, reporting, and escalation support.

It is not a substitute for counsel, regulators, licensed investigators, licensed security managers, privacy officers, HR, emergency services, qualified trainers, forensic experts, engineers, fire/life-safety professionals, or other qualified reviewers.

## Supported Domains

Current repository coverage includes:

- private investigation and investigative research;
- case intake, planning, scope, authority, and lawful-purpose review;
- OSINT and public-records research within lawful source boundaries;
- identity, entity, timeline, and evidence analysis;
- interviewing, witness statements, findings, and case presentation;
- evidence logs, chain of custody, and source provenance;
- corporate and workplace investigations;
- background screening and due diligence;
- private security operations, patrol, access, and incident response;
- communication, de-escalation, and escalation documentation;
- physical security and risk assessment;
- security systems and technology governance;
- loss prevention and asset protection;
- investigation and security program management;
- Canadian federal, Ontario, British Columbia, and Alberta regulatory specialization foundations;
- professional role composition through skillsets;
- multi-skill integration and adversarial safety evaluation;
- specialization planning for future domains such as fraud, digital evidence, retail loss prevention, insurance investigations, and event security.

## Skill Examples

Atomic skills live under `skills/<family>/<skill>/SKILL.md`. Examples include:

- `classify-request-type`
- `assess-lawful-purpose`
- `validate-investigative-authority`
- `plan-open-source-research`
- `record-source-provenance`
- `prepare-neutral-question-set`
- `create-evidence-log`
- `build-evidence-matrix`
- `prepare-findings-summary`
- `triage-security-incident`
- `document-alarm-response`
- `assess-camera-coverage-gap`
- `identify-control-gaps`
- `prepare-compliance-escalation`

Professional skillsets compose existing atomic skills and live in `skillsets/professional-skillsets.json`. Examples include `private-investigator`, `workplace-investigator`, `background-screening-specialist`, `security-officer`, `security-supervisor`, `physical-security-analyst`, `incident-response-coordinator`, and `corporate-security-manager`.

## Sensitivity Model

AgentInvestigate uses six global routing states:

- `PROCEED_ROUTINE`: routine work has enough scope and inputs.
- `CLARIFY_SCOPE`: material facts are missing.
- `REGULATED_RESEARCH_ONLY`: law, licensing, privacy, employment, records, or compliance issues require source-backed framing and no final determination.
- `INTRUSIVE_GATE_REQUIRED`: surveillance, monitoring, screening, identity, personal information, or similar sensitive work must stop before operational execution until authority, privacy, necessity, proportionality, and human approval are satisfied.
- `CERTIFICATION_ESCALATION`: emergency, force, weapons, restraints, alarm response, engineering, life safety, or qualified technical work may receive recognition, documentation, and escalation support only.
- `PROHIBITED_REDIRECT`: prohibited requests are refused at the procedural level and redirected toward lawful alternatives.

Core routing references:

- `docs/architecture/sensitivity-model.md`
- `docs/architecture/authority-routing.md`
- `docs/architecture/intrusive-task-gate.md`
- `docs/architecture/certification-boundaries.md`
- `docs/architecture/prohibited-capabilities.md`

## Jurisdiction Model

Jurisdiction is required when work depends on licensing, privacy, employment screening, workplace investigation, recording or monitoring, access to records, evidence handling rules, security authority, emergency boundaries, alarm response, use of force, weapons, restraints, fire, life safety, or other regulated requirements.

Canadian specialization foundations currently exist for:

- `specializations/canada/federal/`
- `specializations/canada/ontario/`
- `specializations/canada/british-columbia/`
- `specializations/canada/alberta/`

The future Canadian jurisdiction contract is in `docs/architecture/canadian-jurisdiction-roadmap.md`. Future sector specializations are governed by `docs/architecture/specialization-roadmap.md`.

Regulatory, licensing, privacy, evidence, safety, and professional-requirement claims require current source-backed research before implementation or reliance.

## Installation And Use

Clone the repository:

```powershell
git clone https://github.com/jeremylongworth-source/AgentInvestigate.git
cd AgentInvestigate
```

Run validation:

```powershell
.\scripts\validate-all.ps1
```

Use the repository by pointing an AI agent or reviewer at the relevant `SKILL.md`, architecture document, skillset registry, and test fixture for the task. Start with:

- `ROADMAP.md`
- `docs/architecture/domain-contract.md`
- `docs/architecture/authority-routing.md`
- `docs/architecture/prohibited-capabilities.md`
- `skillsets/professional-skillsets.json`
- `tests/evaluation-rubric.json`

When adding work, follow the latest completed handoff and implement only the active roadmap wave.

## Validation

The full repository gate is:

```powershell
.\scripts\validate-all.ps1
```

The suite validates:

- baseline public documentation;
- taxonomy integrity;
- routing, standards, tests, and foundations;
- implemented skill families;
- Canadian regulatory specialization foundations;
- professional skillset composition;
- multi-skill integration scenarios;
- adversarial safety scenarios;
- specialization roadmap candidates.

The latest validated handoff is `docs/development/handoffs/AI-37-final-handoff.md`.

## Limitations

AgentInvestigate is a skill repository and evaluation corpus, not a licensed investigation service, private security company, law firm, regulator, emergency service, forensic lab, HR department, insurer, engineering firm, or training authority.

Repository artifacts are support material. Outputs produced with these skills still require qualified human review when legal, licensing, privacy, employment, safety, emergency, evidence, professional, or operational consequences are present.

Source-sensitive content can become stale. Current-source verification is required before making or relying on regulated claims.

## Prohibited Capabilities

AgentInvestigate must not provide procedural assistance for:

- hacking, credential theft, or unauthorized account access;
- lock bypass, forced entry, access-control circumvention, alarm defeat, or camera evasion;
- covert tracker installation, illegal GPS tracking, stalking, harassment, or intimate-partner monitoring;
- police, government, regulator, employer, court, bank, telecom, platform, or emergency-service impersonation;
- coercive interrogation, threats, intimidation, detention tactics, search tactics, physical control, weapons, firearms, batons, handcuffs, pain compliance, restraint techniques, combat techniques, or takedowns;
- evidence fabrication, evidence alteration, concealed source gaps, or false statement coaching.

When a request seeks prohibited conduct, the correct behavior is to stop the procedure, name the boundary without operational detail, preserve any benign professional need, and redirect to lawful alternatives such as documentation, safety planning, incident reporting, source logging, policy review, authority checks, escalation, or qualified professional consultation.

## Repository Structure

```text
docs/architecture/         Architecture, routing, boundary, and roadmap contracts
docs/development/          Baseline audits and wave handoffs
docs/evaluation/           Evaluation architecture
docs/foundations/          Shared vocabulary, schemas, and report contracts
docs/standards/            Skill, evidence, source, and testing standards
skillsets/                 Professional skillset registry and composition docs
skills/                    Atomic skill packages
specializations/           Jurisdiction specialization foundations
tests/                     Fixtures for validation, evaluation, routing, and safety
scripts/                   Repository validators and generators
```

## Current Status

- Latest completed wave: `AI-37 v1 Release Candidate Audit`
- Current v1 audit verdict: `V1_PARTIALLY_READY`
- Recommended next step: Post-v1 candidate tracks require separate review before roadmap admission.
- Roadmap: `ROADMAP.md`
- v1 release candidate audit: `docs/evaluation/v1-release-candidate-audit.md`
- Latest handoff: `docs/development/handoffs/AI-37-final-handoff.md`
- Changelog: `CHANGELOG.md`

## Contributing

Contributions must follow `CONTRIBUTING.md` and the active roadmap wave.

Before opening a pull request:

- read `ROADMAP.md` and the latest handoff;
- keep changes scoped to the active wave;
- avoid empty placeholder folders;
- preserve private investigation and private security boundaries;
- use source-backed research for regulated or safety-sensitive claims;
- avoid prohibited procedural content;
- update validators and fixtures with the change;
- run `.\scripts\validate-all.ps1`;
- document files changed, validation performed, source evidence, and known limitations.

## Public Files

The public repository file set is:

- `README.md`
- `ROADMAP.md`
- `CONTRIBUTING.md`
- `CHANGELOG.md`
- `LICENSE`
- `SECURITY.md`
- `CODE_OF_CONDUCT.md`

## License

MIT. See `LICENSE`.
