# Skill Catalog

AgentInvestigate currently validates 212 atomic skill packages.

Each package lives at:

```text
skills/<family>/<skill>/SKILL.md
```

Each skill must remain atomic, bounded, and aligned with the repository standards.

## Major Skill Families

- Professional Core & Ethics
- Case Intake, Scope & Authority
- Law, Licensing, Privacy & Compliance
- Investigation Planning & Case Management
- Research, OSINT & Public Records
- Identity, Entity & Timeline Analysis
- Interviewing, Witnesses & Statements
- Evidence & Chain Of Custody
- Investigative Analysis
- Observation & Surveillance Governance
- Reporting, Findings & Case Presentation
- Corporate & Workplace Investigations
- Background Screening & Due Diligence
- Security Operations, Access & Patrol
- Incident Response
- Communication & De-escalation
- Physical Security & Risk Assessment
- Security Systems & Technology
- Loss Prevention & Asset Protection
- Investigation & Security Program Management

## Representative Skills

- `classify-request-type`
- `assess-lawful-purpose`
- `validate-investigative-authority`
- `identify-jurisdiction`
- `identify-privacy-obligation`
- `plan-open-source-research`
- `record-source-provenance`
- `prepare-neutral-question-set`
- `create-evidence-log`
- `build-evidence-matrix`
- `draft-investigative-finding`
- `prepare-findings-summary`
- `triage-security-incident`
- `document-alarm-response`
- `assess-camera-coverage-gap`
- `identify-control-gaps`
- `audit-security-program`
- `prepare-compliance-escalation`

## Catalog Source Of Truth

The canonical taxonomy is:

```text
docs/architecture/taxonomy-index.yaml
```

Run:

```powershell
python scripts\validate-taxonomy.py --repo-root .
python scripts\validate-skills.py --repo-root .
```

## Authoring Rule

Do not create broad omnibus skills. Add a new skill only when the capability is lawful, bounded, testable, non-prohibited, and not already covered by an existing atomic skill.
