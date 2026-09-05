---
name: log-security-occurrence
description: Log security occurrences from supplied observations, access events, alarm details, notifications, actions, and handoff needs.
license: MIT
---

# Log Security Occurrence

## Overview

Creates security occurrence logs that preserve facts, chronology, notifications, actions, limits, and escalation needs. This is a `ROUTINE` security operations, access, and patrol skill for professional security support.

AI-21 representative operational lifecycle:

- `post orders`
- `shift plan`
- `patrol`
- `observation`
- `access event`
- `alarm`
- `occurrence`
- `handoff`
- `log review`

AI-21 composition targets:

- `security-officer`
- `mobile-patrol-officer`

Security operations skills must support post orders through log review without physical intervention, use of force, access-control bypass, alarm defeat, or law-enforcement impersonation.

## Triggers

- User asks to review, build, plan, document, log, verify, triage, record, prepare, or identify security occurrence.
- User supplies post orders, shift plan details, patrol notes, observations, access-event facts, visitor records, key-control records, alarm facts, occurrence logs, handoff notes, or security logs.
- User needs the AI-21 lifecycle organized across post orders, shift plan, patrol, observation, access event, alarm, occurrence, handoff, log review.
- User needs support for security-officer or mobile-patrol-officer workflows without tactical intervention, enforcement, bypass, or impersonation.

## Non-Triggers

- Requests for physical intervention, use of force, restraint techniques, weapons use, access-control bypass, lock bypass, alarm defeat, law-enforcement impersonation, pursuit, detention, search, seizure, or building-clearing tactics route to `PROHIBITED_REDIRECT`.
- Requests to bypass badges, keys, credentials, locks, barriers, alarms, cameras, visitor controls, or access logs route to `PROHIBITED_REDIRECT`.
- Requests to impersonate police, government, emergency services, building management, a vendor, an employee, or an authorized visitor route to `PROHIBITED_REDIRECT`.
- Requests for emergency response, alarm response, fire, medical, use-of-force, life-safety, legal, licensing, regulatory, or security-service authority conclusions route to qualified review or `CERTIFICATION_ESCALATION`.
- Requests to fabricate, alter, conceal, backdate, sanitize, or selectively omit patrol records, access events, alarm facts, key-control events, occurrences, handoffs, or log gaps route to `PROHIBITED_REDIRECT`.

## Required Inputs

- Security role, site or post scope, jurisdiction when required, authority basis, supplied post orders, supervisor or client instructions, and review boundary.
- Supplied facts relevant to security occurrence, including dates, times, locations, people or roles, access points, alarm zones, patrol points, visitor details, key identifiers, notifications, actions taken, and open issues where applicable.
- Applicable escalation paths, emergency-service trigger guidance, communication channel, reporting format, and records to preserve.
- Known limitations, missing facts, disputed facts, safety concerns, unresolved issues, and required supervisor or qualified review.

## Optional Inputs

- Existing shift plan, patrol route, visitor log, access log, alarm panel note, occurrence report, key-control log, handoff note, security log, post-order gap list, or operations brief.
- Site map or zone list, checkpoint list, staffing roster, client contact, supervisor contact, radio protocol, incident category list, or evidence labels.
- Known hazards, equipment status, access exceptions, visitor exceptions, alarm history, maintenance ticket, camera reference, or prior related occurrence.
- Preferred output format, audience, urgency labels, chronology format, or case-management destination.

## Assumptions

- Do not invent post orders, authority, supervisor approvals, visitor authorization, access records, key custody, alarm facts, observations, notifications, or emergency-service instructions.
- Keep post orders, shift plan, patrol, observation, access event, alarm, occurrence, handoff, and log review visible and separate.
- Do not convert security observations, access exceptions, alarm activations, or log gaps into legal, disciplinary, criminal, or enforcement conclusions.
- Do not provide physical intervention, use of force, restraint techniques, weapons use, access-control bypass, lock bypass, alarm defeat, law-enforcement impersonation.
- Treat outputs as draft security operations support requiring responsible human review before consequential use.

## Dependencies

- Canonical taxonomy dependency: `document-patrol-observation`.
- Use `validate-security-service-authority` and `review-post-orders` before operational security support when authority, licensing, site scope, or post orders are unclear.
- Use `build-shift-plan`, `plan-patrol-route`, `document-patrol-observation`, and `log-security-occurrence` for shift, patrol, observation, and occurrence workflows.
- Use `verify-access-event`, `triage-access-control-event`, `document-visitor-management-issue`, and `record-key-control-event` for access, visitor, and key-control workflows.
- Use `document-alarm-response` only for alarm documentation and escalation; do not provide emergency, building-clearing, alarm-bypass, or technical defeat instructions.
- Use `prepare-shift-handoff`, `review-security-log`, `identify-post-order-gap`, `prepare-security-operations-brief`, and `identify-supervisor-notification-need` for handoff, review, gaps, briefs, and supervisor notifications.
- Use `docs/foundations/professional-vocabulary.md`.
- Use `docs/foundations/shared-schemas.md`.
- Use `docs/foundations/report-structure-contracts.md`.

If a dependency output is unavailable, identify the missing dependency and continue only with bounded issue spotting, draft structure, documentation, or escalation notes.

## Core Procedure

1. Confirm role, site scope, authority, jurisdiction if required, post orders, supervisor instructions, urgency, safety concerns, and reviewer boundary.
2. Place the work in the AI-21 lifecycle: post orders, shift plan, patrol, observation, access event, alarm, occurrence, handoff, or log review.
3. Check for requests involving physical intervention, use of force, restraint techniques, weapons use, access-control bypass, lock bypass, alarm defeat, law-enforcement impersonation, fabricated logs, hidden gaps, or tactical confrontation.
4. Separate supplied facts, times, locations, roles, records, observations, actions taken, notifications, unresolved issues, and assumptions.
5. Identify missing post orders, unclear access authority, visitor or key-control gaps, alarm-response escalation needs, occurrence-log gaps, handoff issues, and supervisor notification needs.
6. Route regulated, certification-boundary, emergency-adjacent, or unclear-authority work to the appropriate authority, jurisdiction, supervisor, emergency, qualified-review, and documentation gates.
7. Return bounded security operations support without deciding legal authority, use of force, detention, search, criminal guilt, liability, discipline, or final enforcement outcomes.

## Evidence Requirements

Use only supplied post orders, site instructions, shift plans, patrol observations, access logs, visitor records, key-control records, alarm records, occurrence logs, handoff notes, security logs, supervisor instructions, and source material. Do not invent records, approvals, observations, notifications, actions taken, or reviewer decisions.

## Source Requirements

External sources are optional for routine organization of supplied security operations material. Licensing, use-of-force, emergency, alarm, fire, life-safety, access-control, privacy, labor, or jurisdiction-specific requirements need AI-05 source standards and qualified review.

## Jurisdiction Requirements

Jurisdiction is required for regulated security-service authority, key control, alarm response, emergency-adjacent work, use-of-force implications, licensing, privacy, reporting duties, legal process, and any material compliance implication. Unknown jurisdiction remains an open gate for regulated or certification-boundary work.

## Authority Checks

Confirm security-service authority, user role, site assignment, post orders, client or organizational authority, supervisor instructions, access rights, key-control authorization, alarm-response authority, reporting duties, and human approval where needed. Missing authority routes to `REGULATED_RESEARCH_ONLY`, `CERTIFICATION_ESCALATION`, or `PROHIBITED_REDIRECT` depending on the request.

## Sensitivity Handling

Default class: `ROUTINE`. Upgrade to `REGULATED`, `INTRUSIVE`, or `CERTIFICATION_BOUNDARY` when security operations work involves emergency conditions, alarm response, fire or life-safety systems, access credentials, key custody, private areas, sensitive personal information, video or monitoring records, suspected criminal activity, confrontation risk, use-of-force implications, licensing, or material consequences.

## Output Contract

Return:

- routing state;
- security role, site scope, jurisdiction, authority, post-order, and reviewer status;
- AI-21 lifecycle status for post orders, shift plan, patrol, observation, access event, alarm, occurrence, handoff, and log review;
- supplied facts, chronology, locations, access points, visitor records, key-control records, alarm facts, observations, actions taken, notifications, unresolved issues, and limitations;
- gaps, contradictions, missing records, unclear authority, escalation needs, supervisor notification needs, and qualified-review questions;
- prohibited operational content check for physical intervention, use of force, restraint techniques, weapons use, access-control bypass, lock bypass, alarm defeat, and law-enforcement impersonation;
- escalation or reviewer target;
- limitations and safe next steps.

Do not provide physical intervention, use of force, restraint techniques, weapons use, access-control bypass, lock bypass, alarm defeat, law-enforcement impersonation, tactical confrontation, detention, search, seizure, or final enforcement outcomes.

## Limitations

This skill does not replace counsel, compliance, licensing authority, security manager, supervisor, emergency services, certified trainer, alarm technician, fire or life-safety authority, or qualified reviewer judgment. It does not confer security authority, authorize access, direct physical intervention, approve use of force, provide alarm bypass instructions, or decide legal, criminal, disciplinary, liability, or enforcement outcomes.

## Escalation

Escalate to supervisor, security manager, client authority, emergency services, counsel, compliance, licensing authority, alarm technician, fire or life-safety authority, HR, police, medical, or another qualified reviewer when facts involve immediate danger, emergency conditions, alarm response, access denial disputes, key loss, unauthorized access, suspected crime, confrontation risk, use-of-force implications, legal process, missing authority, unclear post orders, or material consequences.

## References

- Read `references/log-security-occurrence-reference.md` when preparing security occurrence outputs.
- Use shared schemas and report structure contracts for post orders, shifts, patrols, observations, access events, visitor issues, key control, alarms, occurrences, handoffs, log review, gaps, notifications, confidence, and escalation fields.

## Testing

Must pass AI-21 scenarios for the representative operational lifecycle from post orders to log review, composition targets security-officer and mobile-patrol-officer, and boundary checks against physical intervention, use of force, restraint techniques, weapons use, access-control bypass, lock bypass, alarm defeat, and law-enforcement impersonation.
