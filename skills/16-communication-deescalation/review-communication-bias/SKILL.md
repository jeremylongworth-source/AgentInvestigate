---
name: review-communication-bias
description: Review incident and security communications for bias, unsupported labels, inflammatory wording, and missing context.
license: MIT
---

# Review Communication Bias

## Overview

Reviews communication for bias risk, assumptions, loaded language, protected-status issues, and factual neutrality. This is a `ROUTINE` communication and de-escalation skill for professional security support.

AI-22 incident capabilities:

- `recognition`
- `escalation`
- `notification`
- `scene preservation`
- `emergency-service support`
- `documentation`
- `post-incident review`

AI-22 communication capabilities:

- `conflict avoidance`
- `de-escalation`
- `radio communication`
- `incident notification`
- `audience adaptation`
- `bias review`

Certification boundary: No physical intervention instruction.

## Triggers

- User asks to triage, determine, support, preserve, identify, document, collect, prepare, assess, draft, adapt, review, or communicate communication bias review.
- User supplies incident facts, conflict-risk facts, alarm facts, scene details, emergency-service access needs, notifications, radio-message context, de-escalation notes, audience needs, bias concerns, timeline records, or post-incident review material.
- User needs incident capabilities across recognition, escalation, notification, scene preservation, emergency-service support, documentation, post-incident review.
- User needs communication capabilities across conflict avoidance, de-escalation, radio communication, incident notification, audience adaptation, bias review.
- User needs security-officer, incident-response-coordinator, or security-supervisor support without physical intervention instruction.

## Non-Triggers

- Requests for physical intervention instruction, use of force, restraint techniques, weapons use, tactical confrontation, pursuit, detention, search, seizure, building clearing, or combat route to `PROHIBITED_REDIRECT`.
- Requests to replace emergency services, medical responders, fire services, police, supervisor command, certified training, legal review, or qualified technical judgment route to `CERTIFICATION_ESCALATION`.
- Requests to impersonate emergency services, law enforcement, government, building management, medical staff, fire services, or a supervisor route to `PROHIBITED_REDIRECT`.
- Requests to fabricate, alter, conceal, backdate, sanitize, or selectively omit incident facts, notifications, communications, de-escalation attempts, timelines, scene-preservation limits, or post-incident gaps route to `PROHIBITED_REDIRECT`.
- Requests for final legal, medical, fire, life-safety, use-of-force, disciplinary, liability, criminal, regulatory, licensing, or compliance conclusions route to qualified review.

## Required Inputs

- Security role, site or incident scope, authority basis, jurisdiction when required, post orders or local procedure if supplied, urgency, safety status, and review boundary.
- Supplied facts relevant to communication bias review, including dates, times, locations, people or roles, observations, incident conditions, communications, notifications, actions already taken, records, and open issues where applicable.
- Applicable emergency-service path, supervisor path, client contact, communication channel, reporting format, scene-preservation limits, and records to preserve.
- Known limitations, missing facts, disputed facts, vulnerable people, injuries, threats, hazards, conflict risk, failed communication, bias risk, unresolved issues, and required qualified review.

## Optional Inputs

- Existing occurrence log, alarm record, patrol note, incident timeline, witness or staff account, radio transcript, notification draft, de-escalation plan, scene note, post-incident review, corrective-action list, or supervisor instruction.
- Site map or access point list, responder access route, emergency plan, post orders, visitor log, key-control note, incident category list, contact tree, or evidence labels.
- Known language needs, accessibility needs, audience sensitivity, prior related incidents, environmental hazards, equipment status, or maintenance ticket.
- Preferred output format, audience, urgency labels, chronology format, message length, or case-management destination.

## Assumptions

- Do not invent incident facts, danger status, post orders, emergency-service instructions, supervisor approvals, notifications, communications, scene conditions, witness accounts, corrective actions, or qualified-review decisions.
- Keep recognition, escalation, notification, scene preservation, emergency-service support, documentation, post-incident review, conflict avoidance, de-escalation, radio communication, incident notification, audience adaptation, and bias review visible where relevant.
- Do not convert observations, conflict-risk signals, notifications, de-escalation attempts, or incident timelines into legal, medical, disciplinary, criminal, use-of-force, liability, or compliance conclusions.
- Do not provide physical intervention instruction, use of force, restraint techniques, weapons use, tactical confrontation, pursuit, detention, search.
- Treat outputs as draft incident response and communication support requiring responsible human review before consequential use.

## Dependencies

- Canonical taxonomy dependency: `identify-investigative-bias`.
- Use `triage-security-incident`, `determine-emergency-escalation`, `support-emergency-service-access`, and `preserve-incident-scene` for recognition, escalation, emergency-service support, and scene preservation.
- Use `identify-incident-notification-requirement`, `document-incident-timeline`, `collect-incident-account`, `prepare-post-incident-review`, and `identify-corrective-action` for notification, documentation, accounts, review, and corrective-action workflows.
- Use `assess-conflict-risk`, `prepare-deescalation-communication-plan`, `draft-radio-communication`, `prepare-incident-notification`, `adapt-message-to-audience`, `review-communication-bias`, `document-deescalation-attempt`, and `identify-communication-escalation-need` for communication and de-escalation workflows.
- Use `determine-emergency-escalation` and `identify-communication-escalation-need` when immediate danger, failed de-escalation, vulnerable people, medical, fire, violence, or life-safety indicators appear.
- Use `identify-investigative-bias` and `separate-fact-from-inference` when communications contain unsupported labels, assumptions, stereotypes, inflammatory language, or bias risk.
- Use `docs/foundations/professional-vocabulary.md`.
- Use `docs/foundations/shared-schemas.md`.
- Use `docs/foundations/report-structure-contracts.md`.

If a dependency output is unavailable, identify the missing dependency and continue only with bounded recognition, documentation, communication drafting, or escalation notes.

## Core Procedure

1. Confirm role, site or incident scope, authority, jurisdiction if required, post orders or local procedure, urgency, immediate safety concern, and reviewer boundary.
2. Identify applicable incident capabilities: recognition, escalation, notification, scene preservation, emergency-service support, documentation, and post-incident review.
3. Identify applicable communication capabilities: conflict avoidance, de-escalation, radio communication, incident notification, audience adaptation, and bias review.
4. Check for physical intervention instruction, use of force, restraint techniques, weapons use, tactical confrontation, pursuit, detention, search, fabricated records, hidden gaps, or emergency-service substitution.
5. Separate supplied facts, times, locations, roles, observations, communications, actions already taken, notifications, records to preserve, assumptions, unresolved issues, and reviewer questions.
6. Route emergency-adjacent, certification-boundary, regulated, unclear-authority, or unsafe work to emergency services, supervisor, qualified review, source standards, and documentation gates.
7. Return bounded incident response or communication support without physical intervention instruction or final legal, medical, fire, life-safety, criminal, disciplinary, liability, or compliance conclusions.

## Evidence Requirements

Use only supplied incident facts, observations, post orders, local procedures, occurrence logs, access logs, alarm records, timelines, notifications, communications, accounts, scene notes, post-incident reviews, corrective-action notes, and source material. Do not invent facts, danger status, statements, notifications, actions taken, approvals, or reviewer decisions.

## Source Requirements

External sources are optional for routine organization of supplied incident and communication material. Emergency, medical, fire, life-safety, use-of-force, licensing, reporting, privacy, labor, or jurisdiction-specific requirements need AI-05 source standards and qualified review.

## Jurisdiction Requirements

Jurisdiction is required for regulated notification duties, emergency-adjacent work, use-of-force implications, security licensing, privacy, reporting duties, legal process, scene-preservation obligations, and material compliance implications. Missing jurisdiction does not block immediate emergency escalation recognition.

## Authority Checks

Confirm security-service authority, user role, site assignment, post orders, local procedure, supervisor path, emergency-service path, notification authority, communication authority, scene-preservation authority, and human approval where needed. Missing authority routes to `CERTIFICATION_ESCALATION`, `REGULATED_RESEARCH_ONLY`, or `PROHIBITED_REDIRECT` depending on the request.

## Sensitivity Handling

Default class: `ROUTINE`. Upgrade to `REGULATED`, `INTRUSIVE`, or `CERTIFICATION_BOUNDARY` when incident response or communication work involves immediate danger, injuries, threats, medical issues, fire or life-safety issues, vulnerable people, conflict escalation, alarm response, emergency-service support, scene preservation, suspected crime, use-of-force implications, protected characteristics, sensitive personal information, privacy, reporting duties, licensing, or material consequences.

## Output Contract

Return:

- routing state;
- security role, incident scope, site scope, jurisdiction, authority, post-order, procedure, urgency, and reviewer status;
- incident capability status for recognition, escalation, notification, scene preservation, emergency-service support, documentation, and post-incident review;
- communication capability status for conflict avoidance, de-escalation, radio communication, incident notification, audience adaptation, and bias review;
- supplied facts, chronology, locations, involved roles, observations, communications, notifications, actions already taken, records to preserve, unresolved issues, and limitations;
- gaps, contradictions, missing records, unclear authority, emergency or supervisor escalation needs, communication risks, bias risks, and qualified-review questions;
- prohibited physical intervention check for physical intervention instruction, use of force, restraint techniques, weapons use, tactical confrontation, pursuit, detention, and search;
- escalation or reviewer target;
- limitations and safe next steps.

Do not provide physical intervention instruction, use of force, restraint techniques, weapons use, tactical confrontation, pursuit, detention, search, seizure, emergency-service substitution, or final legal, medical, fire, life-safety, criminal, disciplinary, liability, or compliance conclusions.

## Limitations

This skill does not replace emergency services, supervisor command, counsel, compliance, licensing authority, security manager, certified trainer, medical responders, fire or life-safety authority, police, or qualified reviewer judgment. It does not authorize intervention, train de-escalation, approve use of force, provide tactical instructions, certify safety, or decide legal, criminal, disciplinary, liability, medical, fire, life-safety, or enforcement outcomes.

## Escalation

Escalate to emergency services, supervisor, security command, client authority, counsel, compliance, licensing authority, medical responders, fire or life-safety authority, police, HR, or another qualified reviewer when facts involve immediate danger, injury, threats, fire, medical concerns, vulnerable people, violence, alarm response, scene preservation, access disputes, failed de-escalation, suspected crime, use-of-force implications, legal process, missing authority, unclear post orders, or material consequences.

## References

- Read `references/review-communication-bias-reference.md` when preparing communication bias review outputs.
- Use shared schemas and report structure contracts for incidents, timelines, notifications, communications, de-escalation attempts, scene notes, post-incident reviews, corrective actions, confidence, and escalation fields.

## Testing

Must pass AI-22 scenarios for incident capabilities, communication capabilities, and the certification boundary: No physical intervention instruction.
