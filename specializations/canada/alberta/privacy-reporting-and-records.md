# Privacy, Reporting, And Records

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_30_ALBERTA_READY
```

## Purpose

This reference supports Alberta issue spotting for privacy interaction, access requests, health information, reporting, complaints, licence updates, recordkeeping, retention, surveillance records, employee monitoring, private-sector privacy, public-sector privacy, and federal overlap.

## Source Basis

Freshness: `HIGH`

Use these source IDs from `source-log.yaml`:

- `alberta-ssia-act`
- `alberta-ssia-regulation`
- `alberta-ssia-policy-manual`
- `alberta-pipa`
- `alberta-pipa-regulation`
- `alberta-popa`
- `alberta-protection-of-privacy-act-guidance`
- `alberta-atia`
- `alberta-access-to-information-act-guidance`
- `alberta-hia`
- `alberta-health-information-act-guidance`
- `alberta-oipc-video-surveillance-private`
- `alberta-oipc-privacy-laws-overview`
- `alberta-oipc-privacy-impact-assessments`

Recheck current official Open Government, Alberta.ca, and OIPC sources before using privacy, access, complaint, reporting, retention, disclosure, surveillance, health-information, worker-notification, business-notification, or licence-update claims.

## Required Coverage

This module covers:

- privacy interaction
- reporting
- restrictions
- security operations
- provincial laws materially relevant to scoped skills

## Privacy Interaction Map

Alberta investigation and security work may involve:

- private-sector personal information under PIPA;
- public-sector personal information under POPA;
- access to records held by public bodies under ATIA;
- health information under HIA;
- video surveillance, access-control, alarm, incident, patrol, visitor, vehicle, body-armour, baton, patrol-dog, and case records;
- workplace investigation and employee monitoring records;
- third-party information captured incidentally;
- retention, notice, access, correction, disclosure, safeguards, privacy impact assessments, privacy incident reporting, and law-enforcement disclosure questions;
- federal privacy overlap, including PIPEDA analysis where applicable.

POPA and ATIA came into force on 2025-06-11 and replaced the former public-sector FOIP structure. Because this is a recent public-sector privacy and access transition, any Alberta public-body privacy or access output must verify POPA, ATIA, regulations, and OIPC guidance at time of use.

Use the OIPC video surveillance private-sector guidance, privacy laws overview, and privacy impact assessment guidance as source pointers only after currentness is checked.

## Reporting And Records Map

Alberta issue spotting should distinguish:

- investigator and security service worker licence update and reporting issues;
- security business licence reporting issues;
- registry temporary licence records;
- training, examination, rewrite, challenge, approved-provider, and training licence records;
- baton training and re-certification records;
- body-armour permit, lost/stolen permit, employer-copy, and exemption records;
- incident reports;
- occurrence logs;
- patrol logs;
- access-control records;
- video-surveillance records;
- complaint, inspection, investigation, court, administrative proceeding, and regulator records.

The module may identify recordkeeping and reporting issues, but it must not decide that records are complete, compliant, admissible, privileged, or sufficient for discipline, prosecution, termination, civil litigation, tribunal proceedings, regulator filings, or insurance claims.

## Allowed Support

Allowed outputs include:

- privacy and records issue checklists;
- source-backed research briefs;
- retention and disclosure questions;
- complaint and notification issue lists;
- federal/provincial overlap notes;
- questions for counsel, privacy officers, HR, compliance, licensed business leadership, records managers, Security Programs, OIPC, regulators, or insurers.

## Routing Rule

Use:

```text
REGULATED_RESEARCH_ONLY
```

for privacy, access, reporting, recordkeeping, complaint, retention, and disclosure research.

Use:

```text
INTRUSIVE_GATE_REQUIRED
```

for surveillance, monitoring, location, biometric, health-information, sensitive workplace, employee monitoring, or third-party capture questions that may be intrusive.

Use:

```text
CERTIFICATION_ESCALATION
```

when the request asks for privacy compliance certification, access response approval, regulator filing approval, record admissibility conclusion, breach determination, privacy impact assessment approval, or final retention/disclosure approval.

Use:

```text
PROHIBITED_REDIRECT
```

when the request asks to conceal records, fabricate records, destroy records to avoid review, evade surveillance notice obligations, access private accounts, obtain protected records deceptively, or bypass privacy controls.
