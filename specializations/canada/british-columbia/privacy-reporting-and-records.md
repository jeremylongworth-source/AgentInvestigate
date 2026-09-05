# Privacy, Reporting, And Records

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_29_BRITISH_COLUMBIA_READY
```

## Purpose

This reference supports BC issue spotting for privacy interaction, reporting, complaints, Registrar notices, recordkeeping, retention, surveillance records, employee monitoring, public-sector privacy, private-sector privacy, and federal overlap.

## Source Basis

Freshness: `HIGH`

Use these source IDs from `source-log.yaml`:

- `bc-security-services-act`
- `bc-security-services-regulation`
- `bc-security-business-rules-guidance`
- `bc-security-licensing-enforcement`
- `bc-pipa`
- `bc-fippa`
- `bc-oipc-overt-video-private-sector`
- `bc-oipc-public-sector-surveillance`
- `bc-oipc-employee-privacy`

Recheck current official BC Laws, Government of BC, and OIPC sources before using privacy, complaint, reporting, retention, disclosure, surveillance, worker-notification, business-notification, or Registrar-notification claims.

## Required Coverage

This module covers:

- privacy interaction
- reporting
- restrictions
- security operations
- provincial laws materially relevant to scoped skills

## Privacy Interaction Map

BC investigation and security work may involve:

- private-sector personal information under PIPA;
- public-sector personal information under FIPPA;
- video surveillance, access-control, alarm, incident, patrol, visitor, vehicle, body-armour, dog, and case records;
- workplace investigation and employee monitoring records;
- third-party information captured incidentally;
- retention, notice, access, correction, disclosure, safeguards, and law-enforcement disclosure questions;
- federal privacy overlap, including PIPEDA analysis where applicable.

Use the OIPC private-sector overt video surveillance guidance, OIPC public-sector surveillance guidelines, and employee privacy guidance as source pointers only after currentness is checked.

## Reporting And Records Map

BC issue spotting should distinguish:

- security worker reporting requirements;
- security business reporting requirements;
- change-of-address, charge, conviction, ownership, management, licence-condition, and security-business reporting issues;
- incident reports;
- occurrence logs;
- patrol logs;
- access-control records;
- video-surveillance records;
- dog and dog-handler training/certification records;
- equipment, vehicle, advertising, and body-armour records;
- complaint records;
- inspection, investigation, court, administrative proceeding, and regulator records.

The module may identify recordkeeping and reporting issues, but it must not decide that records are complete, compliant, admissible, privileged, or sufficient for discipline, prosecution, termination, civil litigation, tribunal proceedings, regulator filings, or insurance claims.

## Allowed Support

Allowed outputs include:

- privacy and records issue checklists;
- source-backed research briefs;
- retention and disclosure questions;
- complaint and notification issue lists;
- federal/provincial overlap notes;
- questions for counsel, privacy officers, HR, compliance, licensed business leadership, records managers, Security Programs Division, regulators, or insurers.

## Routing Rule

Use:

```text
REGULATED_RESEARCH_ONLY
```

for privacy, reporting, recordkeeping, complaint, retention, and disclosure research.

Use:

```text
INTRUSIVE_GATE_REQUIRED
```

for surveillance, monitoring, location, biometric, sensitive workplace, employee monitoring, or third-party capture questions that may be intrusive.

Use:

```text
CERTIFICATION_ESCALATION
```

when the request asks for privacy compliance certification, regulator filing approval, record admissibility conclusion, breach determination, or final retention/disclosure approval.

Use:

```text
PROHIBITED_REDIRECT
```

when the request asks to conceal records, fabricate records, destroy records to avoid review, evade surveillance notice obligations, access private accounts, obtain protected records deceptively, or bypass privacy controls.
