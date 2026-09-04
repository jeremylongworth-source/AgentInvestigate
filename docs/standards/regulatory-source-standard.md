# AgentInvestigate Regulatory Source Standard

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_05_SOURCE_STANDARD_READY
```

## Purpose

AgentInvestigate may support legal, regulatory, licensing, privacy, employment, standards, and compliance research, but it must not claim authority it does not have. This standard defines the metadata and handling requirements for regulated source material.

## Applies To

This standard applies when a skill touches:

- investigation or security licensing;
- privacy, consent, collection, retention, disclosure, or monitoring obligations;
- employment screening or workplace investigation requirements;
- records access or public-record limits;
- court, regulator, tribunal, or administrative material;
- background screening and consumer-report issues;
- private security operations, alarms, patrols, emergency escalation, use-of-force boundaries, weapons, restraints, or training requirements;
- fire, life-safety, structural, electrical, alarm, camera, access-control, or other qualified technical systems;
- professional standards, certification, or qualified-review requirements.

## Allowed Outputs

Skills may produce:

- research briefs;
- issue-spotting summaries;
- source-backed obligation checklists;
- authority and jurisdiction gap lists;
- evidence requests;
- privacy or compliance preparation checklists;
- escalation packets;
- questions for counsel, regulators, privacy officers, HR, licensed investigators, licensed security managers, qualified trainers, engineers, fire/life-safety professionals, insurers, or organizational leadership.

## Disallowed Outputs

Skills must not produce:

- legal conclusions;
- regulatory approval;
- licensing approval;
- privacy compliance certification;
- employment-action approval;
- investigation authorization;
- security authorization;
- emergency-response instructions that replace local procedures or emergency services;
- use-of-force, weapons, restraint, pursuit, confrontation, bypass, evasion, or tactical procedure;
- engineering, fire, life-safety, alarm, camera, or access-control signoff;
- declarations that a person, organization, investigation, screening process, security program, site, system, or action is compliant.

## Source Hierarchy

Regulated claims must use the hierarchy from `docs/standards/research-and-evidence-standard.md`:

```text
1. legislation / regulations / courts
2. government regulators
3. privacy authorities
4. recognized standards organizations
5. professional associations
6. academic / technical literature
7. specialist material
8. secondary summaries
```

Use the highest applicable tier available for the claim. A lower-tier source cannot override an applicable higher-tier source.

## Regulatory Metadata

Every regulated source record must use this metadata shape when recorded in a source log, reference file, skill fixture, or output:

```yaml
source_title:
organization:
jurisdiction:
authority_level:
source_url:
publication_date:
effective_date:
accessed_date:
last_verified:
applicability:
supersession_risk:
used_by:
```

Field rules:

| Field | Requirement |
|---|---|
| `source_title` | Human-readable source name. |
| `organization` | Publisher, regulator, court, standards body, association, or source owner. |
| `jurisdiction` | Country, province, state, municipality, court, regulator scope, or `jurisdiction-neutral`. |
| `authority_level` | Source hierarchy tier and source type. |
| `source_url` | URL or supplied-source identifier. |
| `publication_date` | Publication or issue date when available. |
| `effective_date` | Effective date, amendment date, version, edition, or `unknown` when unavailable. |
| `accessed_date` | Date the source was accessed. |
| `last_verified` | Date the source was last checked for currency and applicability. |
| `applicability` | Short statement of the claim, jurisdiction, role, activity, or scope the source supports. |
| `supersession_risk` | `LOW`, `MEDIUM`, or `HIGH` with a reason. |
| `used_by` | Skill name, reference file, output, or test that depends on the source. |

Do not omit unknown values silently. Use `unknown` and state the review need.

## Jurisdiction And Scope

Regulated outputs must identify:

- jurisdiction;
- user role;
- client or organizational authority when relevant;
- activity or work type;
- subject or affected party class when relevant;
- source date and verification date;
- whether the output is an issue-spotting summary, research brief, preparation checklist, or escalation packet;
- what must be reviewed by a qualified person before use.

If jurisdiction is missing, the skill must ask for it or provide only jurisdiction-neutral research questions and source categories.

## Source Use Rules

- Prefer current official sources for regulated claims.
- Record source metadata before a source is used in a reusable reference or skill.
- Cite the source claim, not only the source URL.
- Identify whether the source supports the whole output or only one issue.
- Separate source text from interpretation.
- Use quoted text sparingly and only when necessary for precision.
- Do not universalize one jurisdiction's rule.
- Do not infer authority from user confidence, job title, or desired outcome.
- Treat private databases, leaked records, credentialed accounts, and unauthorized sources as out of scope unless lawful access and authority are established.

## Supersession And Conflict Rules

Mark `supersession_risk` as `HIGH` when the source may change frequently, has recent amendments, is platform or regulator guidance, concerns emergency/safety operations, or lacks a stable effective date.

When a regulated source may be superseded:

- verify before use;
- prefer official current versions;
- state the verification date;
- preserve the earlier source only as historical context if useful;
- route unresolved conflicts to qualified review.

## Skill Authoring Requirements

Regulated skills must define:

- required jurisdiction;
- required source hierarchy tier;
- required metadata fields;
- source freshness class from `docs/standards/source-freshness-standard.md`;
- allowed output label;
- qualified-review trigger;
- missing-source behavior;
- conflicting-source behavior;
- prohibited outputs.

## Review Gate

A regulated source-dependent skill is ready only when:

- it identifies the regulated scope and jurisdiction need;
- it requires current official sources where appropriate;
- it includes the regulatory metadata contract;
- it preserves legal, privacy, licensing, security, emergency, and certification boundaries;
- it separates evidence, source text, interpretation, and action;
- it defines what happens when current sources are unavailable.

## Validation Notes

AI-05 does not decide jurisdiction-specific requirements. It creates the source contract future skills must use before they summarize or depend on regulated material.
