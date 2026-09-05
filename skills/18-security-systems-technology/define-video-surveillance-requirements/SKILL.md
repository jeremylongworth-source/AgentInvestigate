---
name: define-video-surveillance-requirements
description: Define video-surveillance requirements from supplied privacy, authority, site, coverage, and retention context.
license: MIT
---

# Define Video Surveillance Requirements

## Overview

Defines video surveillance requirements while preserving privacy, notice, retention, coverage, and review constraints. This is a `REGULATED` security systems and technology skill for professional security support.

AI-24 system-analysis capabilities:

- `access control`
- `video surveillance`
- `intrusion detection`
- `alarm monitoring`
- `event analysis`
- `coverage`
- `failures`
- `requirements`

AI-24 explicit prohibition tests:

- `alarm bypass`
- `camera defeat`
- `credential cloning`
- `access-control circumvention`
- `monitoring evasion`

Security systems and technology skills support analysis, requirements, documentation, and qualified-review framing only. They do not provide alarm bypass, camera defeat, credential cloning, access-control circumvention, or monitoring evasion.

## Triggers

- User asks to define, analyze, assess, identify, or prepare video-surveillance requirements.
- User supplies access-control context, video surveillance context, intrusion detection context, alarm monitoring records, event logs, coverage notes, failure reports, or requirements material.
- User needs system-analysis skills for access control, video surveillance, intrusion detection, alarm monitoring, event analysis, coverage, failures, requirements.
- User needs physical-security-analyst, security-risk-assessor, or security-program-manager support without bypass, defeat, cloning, circumvention, or evasion guidance.

## Non-Triggers

- Requests for alarm bypass, camera defeat, credential cloning, access-control circumvention, monitoring evasion, lock bypass, badge cloning, exploit steps, sensor avoidance, blind-spot exploitation, or system-disabling instructions route to `PROHIBITED_REDIRECT`.
- Requests to defeat, disable, evade, tamper with, or circumvent alarms, cameras, access controls, badges, locks, sensors, logs, or monitoring controls route to `PROHIBITED_REDIRECT`.
- Requests for installation signoff, repair instructions, wiring instructions, engineering approval, fire-code approval, life-safety certification, privacy compliance certification, or final technical approval route to qualified review.
- Requests for emergency response, building clearing, use of force, restraint, weapons, tactical confrontation, or unauthorized entry route to `CERTIFICATION_ESCALATION` or `PROHIBITED_REDIRECT`.
- Requests to fabricate, alter, conceal, backdate, sanitize, or selectively omit system events, video records, alarm logs, access logs, failures, coverage gaps, privacy limits, or requirements gaps route to `PROHIBITED_REDIRECT`.

## Required Inputs

- Site or system scope, user role, authority basis, jurisdiction when required, assessment or requirements purpose, affected systems, and review boundary.
- Supplied facts relevant to video-surveillance requirements, including access control, video surveillance, intrusion detection, alarm monitoring, event analysis, coverage, failures, and requirements where applicable.
- Existing controls, system records, event logs, alarm records, camera or access-point references, privacy constraints, retention constraints, and qualified-review needs.
- Known limitations, missing facts, disputed facts, sensitive areas, private information, life-safety implications, technical questions, and required human approvals.

## Optional Inputs

- Existing access matrix, event log, video log, camera list, alarm report, intrusion-zone list, monitoring procedure, coverage diagram, failure report, requirements brief, or vendor note.
- Risk assessment, control-gap list, post orders, alarm response record, privacy review note, retention policy, site map excerpt, stakeholder request, or maintenance ticket.
- Known integrations, equipment constraints, service-level expectations, monitoring escalation paths, audit needs, budget constraints, implementation constraints, or owner list.
- Preferred output format, audience, risk labels, table format, assumptions format, or destination system.

## Assumptions

- Do not invent system facts, authority, logs, events, camera views, access records, alarm signals, failures, requirements, privacy approvals, technician findings, or compliance decisions.
- Keep access control, video surveillance, intrusion detection, alarm monitoring, event analysis, coverage, failures, and requirements visible where relevant.
- Do not convert system observations, event logs, coverage gaps, or failure indicators into legal, privacy, life-safety, engineering, criminal, or final technical conclusions.
- Do not provide alarm bypass, camera defeat, credential cloning, access-control circumvention, monitoring evasion.
- Treat outputs as draft security-system analysis support requiring responsible human review before consequential use.

## Dependencies

- Canonical taxonomy dependency: `identify-privacy-obligation`.
- Use `identify-control-gaps`, `define-access-control-requirements`, `define-video-surveillance-requirements`, and `define-intrusion-detection-requirements` before requirements summaries.
- Use `triage-access-control-event`, `analyze-access-control-event`, `document-alarm-response`, and `analyze-alarm-event` for event analysis and alarm monitoring records.
- Use `assess-camera-coverage-gap`, `analyze-video-event-log`, and `identify-security-system-failure` for video surveillance, coverage, failure, and intrusive record analysis.
- Use `identify-privacy-obligation` when video surveillance, monitoring, personal information, retention, notice, or privacy implications appear.
- Use `docs/foundations/professional-vocabulary.md`.
- Use `docs/foundations/shared-schemas.md`.
- Use `docs/foundations/report-structure-contracts.md`.

If a dependency output is unavailable, identify the missing dependency and continue only with bounded analysis, draft requirements structure, documentation, or qualified-review notes.

## Core Procedure

1. Confirm site or system scope, role, authority, jurisdiction if required, purpose, affected systems, sensitivity, and reviewer boundary.
2. Identify applicable AI-24 system-analysis capabilities: access control, video surveillance, intrusion detection, alarm monitoring, event analysis, coverage, failures, and requirements.
3. Check for requests to provide alarm bypass, camera defeat, credential cloning, access-control circumvention, monitoring evasion, fabricated records, hidden failures, installation signoff, or qualified technical approval.
4. Separate supplied facts, logs, system records, observations, event timing, coverage notes, failure indicators, assumptions, privacy limits, uncertainty, source limits, and reviewer questions.
5. Preserve system scope, authority status, privacy constraints, coverage gaps, failure indicators, event chronology, requirements gaps, source limits, and confidence.
6. Route regulated, intrusive, certification-boundary, technical, privacy, life-safety, fire, alarm, access-control, or unclear-authority work to licensed technician review, privacy review, life-safety review, security authority review.
7. Return bounded security-system analysis without bypass, defeat, cloning, circumvention, monitoring evasion, final technical approval, or compliance certification.

## Evidence Requirements

Use only supplied access-control records, video event logs, camera lists, alarm records, intrusion detection notes, monitoring procedures, system requirements, coverage notes, failure reports, post orders, incident records, vendor notes, and source material. Do not invent logs, footage, access decisions, alarm causes, failure causes, technical findings, or approvals.

## Source Requirements

External sources are optional for routine organization of supplied system material. Security-system design, alarm monitoring, access control, video surveillance, privacy, fire, life-safety, electrical, technical, legal, licensing, or jurisdiction-specific requirements need AI-05 source standards and qualified review.

## Jurisdiction Requirements

Jurisdiction is required for regulated requirements, video surveillance, privacy, alarm monitoring, intrusion detection, access control, life-safety, fire, electrical, legal, licensing, and compliance implications. Unknown jurisdiction remains an open gate for regulated, intrusive, or certification-boundary work.

## Authority Checks

Confirm user role, site authority, system authority, lawful purpose, access to records, privacy basis, monitoring basis, reviewer role, technician or vendor review needs, and human approval where needed. Missing authority routes to `REGULATED_RESEARCH_ONLY`, `INTRUSIVE_GATE_REQUIRED`, `CERTIFICATION_ESCALATION`, or `PROHIBITED_REDIRECT` depending on the request.

## Sensitivity Handling

Default class: `REGULATED`. Upgrade to `REGULATED`, `INTRUSIVE`, or `CERTIFICATION_BOUNDARY` when security-system work involves video surveillance, personal information, sensitive areas, camera or alarm layouts, access credentials, intrusion detection, alarm monitoring, system failures, emergency response, fire or life-safety systems, electrical questions, suspected crime, privacy issues, or material consequences.

## Output Contract

Return:

- routing state;
- site scope, system scope, role, authority, jurisdiction, purpose, privacy, source, and reviewer status;
- AI-24 capability status for access control, video surveillance, intrusion detection, alarm monitoring, event analysis, coverage, failures, and requirements;
- supplied facts, logs, records, chronology, access events, video events, alarm events, coverage notes, failure indicators, requirements, assumptions, and limitations;
- gaps, contradictions, missing records, unclear authority, privacy constraints, coverage gaps, failure-review needs, technical-review needs, and qualified-review questions;
- explicit prohibition check for alarm bypass, camera defeat, credential cloning, access-control circumvention, and monitoring evasion;
- escalation or qualified-review target;
- limitations and safe next steps.

Do not provide alarm bypass, camera defeat, credential cloning, access-control circumvention, monitoring evasion, lock bypass, exploit instructions, final technical approval, engineering approval, fire-code approval, life-safety certification, privacy compliance certification, or implementation signoff.

## Limitations

This skill does not replace counsel, privacy, compliance, licensing authority, security manager, security-system designer, alarm technician, access-control technician, video surveillance technician, fire or life-safety authority, electrical professional, vendor, or qualified reviewer judgment. It does not certify compliance, approve designs, authorize access, repair systems, defeat systems, or provide bypass instructions.

## Escalation

Escalate to a security manager, client authority, privacy reviewer, counsel, compliance, licensing authority, alarm technician, access-control technician, video surveillance technician, fire or life-safety authority, electrical professional, vendor, emergency services, or another qualified reviewer when facts involve licensed technician review, privacy review, life-safety review, security authority review, system failures, sensitive monitoring, unclear authority, emergency indicators, fire or life-safety issues, privacy implications, or material consequences.

## References

- Read `references/define-video-surveillance-requirements-reference.md` when preparing video-surveillance requirements outputs.
- Use shared schemas and report structure contracts for access control, video surveillance, intrusion detection, alarm monitoring, event analysis, coverage, failures, requirements, assumptions, confidence, and escalation fields.

## Testing

Must pass AI-24 scenarios for access control, video surveillance, intrusion detection, alarm monitoring, event analysis, coverage, failures, requirements, and explicit prohibition tests for alarm bypass, camera defeat, credential cloning, access-control circumvention, and monitoring evasion.
