# Privacy, Reporting, And Records

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_28_ONTARIO_READY
```

## Purpose

This reference supports Ontario issue spotting for privacy interaction, reporting, complaints, registrar notices, recordkeeping, retention, surveillance records, health information, public-sector privacy, and federal overlap.

## Source Basis

Freshness: `HIGH`

Use these source IDs from `source-log.yaml`:

- `ontario-recordkeeping-regulation`
- `ontario-information-to-registrar-regulation`
- `ontario-fippa`
- `ontario-mfippa`
- `ontario-phipa`
- `ontario-ipc-video-surveillance`
- `ontario-psisa-act`

Recheck current official Ontario and IPC sources before using privacy, complaint, reporting, retention, disclosure, surveillance, or registrar-notification claims.

## Required Coverage

This module covers:

- privacy interaction
- reporting
- restrictions
- security operations
- provincial laws materially relevant to scoped skills

## Privacy Interaction Map

Ontario investigation and security work may involve:

- public-sector personal information under FIPPA or MFIPPA;
- personal health information under PHIPA;
- video surveillance, access-control, alarm, incident, patrol, visitor, and case records;
- workplace investigation records;
- third-party information captured incidentally;
- retention, notice, access, disclosure, and law-enforcement disclosure questions;
- federal privacy overlap, including private-sector PIPEDA analysis where applicable.

The Information and Privacy Commissioner of Ontario video surveillance guidance checked for AI-28 states that FIPPA and MFIPPA changes from Bill 97 have amendments in force on 2026-07-01, 2026-09-15, and 2027-01-01, and that some IPC guidance is under review and subject to change. Because the current repository verification date is 2026-09-05, any use near or after 2026-09-15 must recheck IPC, FIPPA, and MFIPPA sources before relying on the guidance.

Use the IPC video surveillance guidance as a source pointer only after currentness is checked.

## Reporting And Records Map

Ontario issue spotting should distinguish:

- incident reports;
- occurrence logs;
- patrol logs;
- access-control records;
- video-surveillance records;
- equipment issuance records;
- employer or agency records;
- complaint records;
- regulator or Registrar notification triggers;
- investigation, inspection, court, or administrative proceeding retention issues.

The module may identify recordkeeping and reporting issues, but it must not decide that records are complete, compliant, admissible, privileged, or sufficient for discipline, prosecution, termination, civil litigation, tribunal proceedings, regulator filings, or insurance claims.

## Allowed Support

Allowed outputs include:

- privacy and records issue checklists;
- source-backed research briefs;
- retention and disclosure questions;
- complaint and notification issue lists;
- federal/provincial overlap notes;
- questions for counsel, privacy officers, HR, compliance, licensed agency leadership, records managers, regulators, or insurers.

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

for surveillance, monitoring, location, biometric, health-information, sensitive workplace, or third-party capture questions that may be intrusive.

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
