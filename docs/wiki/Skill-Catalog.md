# Skill Catalog

AgentInvestigate currently validates 212 atomic skill packages. Each package lives at:

```text
skills/<family>/<skill>/SKILL.md
```

## Skill Families

| Branch | Families |
| --- | --- |
| Shared professional foundation | Professional Core & Ethics |
| Private investigation | Intake, Scope & Authority; Law, Licensing, Privacy & Compliance; Investigation Planning & Case Management; Research, OSINT & Public Records; Identity, Entity & Timeline Analysis; Interviewing, Witnesses & Statements; Evidence & Chain of Custody; Investigative Analysis; Observation & Surveillance Governance; Reporting, Findings & Case Presentation; Corporate & Workplace Investigations; Background Screening & Due Diligence |
| Private security | Security Operations, Access & Patrol; Incident Response; Communication & De-escalation; Physical Security & Risk Assessment; Security Systems & Technology; Loss Prevention & Asset Protection; Investigation & Security Program Management |

The branches share selected foundations, but they are not interchangeable.

## Representative Skills

| Need | Example |
| --- | --- |
| Route a request | `classify-request-type`, `identify-jurisdiction` |
| Check authority and purpose | `assess-lawful-purpose`, `validate-investigative-authority` |
| Research public sources | `plan-open-source-research`, `record-source-provenance` |
| Organize evidence | `create-evidence-log`, `build-evidence-matrix` |
| Support interviews and findings | `prepare-neutral-question-set`, `prepare-findings-summary` |
| Support security operations | `triage-security-incident`, `document-alarm-response` |
| Review controls | `assess-camera-coverage-gap`, `identify-control-gaps` |
| Escalate regulated concerns | `prepare-compliance-escalation` |

## How To Select A Skill

1. Start with routing and prohibited-capability checks when the request is new or ambiguous.
2. Prefer the narrowest skill that matches the requested output.
3. Read the skill's `SKILL.md`, dependencies, references, and test scenarios.
4. Confirm the required jurisdiction, authority, privacy, source, and human-review gates.
5. Preserve the skill's limitations in the resulting output.

## Source Of Truth

The canonical taxonomy is `docs/architecture/taxonomy-index.yaml`. Run:

```powershell
python scripts\validate-taxonomy.py --repo-root .
python scripts\validate-skills.py --repo-root .
```

Do not create broad omnibus skills. A new package must be lawful, bounded, testable, non-prohibited, and absent from the existing taxonomy.
