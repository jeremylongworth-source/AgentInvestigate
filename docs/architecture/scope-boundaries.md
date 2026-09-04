# AgentInvestigate Scope Boundaries

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_01_DOMAIN_CONTRACT_READY
```

## Purpose

This document defines what AgentInvestigate may and may not contain. It converts the AI-01 domain contract into contribution and routing boundaries.

## In Scope

Private investigation decision support:

- request classification;
- jurisdiction and authority issue spotting;
- lawful-purpose analysis;
- investigative planning;
- case management;
- source planning and source reliability;
- public/open-source research structure;
- identity ambiguity handling;
- neutral interview planning;
- statement comparison;
- evidence logs and matrices;
- chain-of-custody issue spotting;
- chronology construction;
- hypothesis testing;
- finding confidence;
- investigative report drafting.

Private security decision support:

- post orders;
- shift planning;
- access and patrol documentation;
- incident recognition and escalation planning;
- emergency-service support documentation;
- scene preservation planning;
- conflict-avoidance and verbal de-escalation planning;
- radio and incident notification drafting;
- physical-security risk assessment;
- security-system requirements and event analysis;
- loss-prevention incident mapping;
- asset-protection improvement planning;
- security program audit and improvement.

Shared professional support:

- ethics;
- role boundaries;
- conflict-of-interest checks;
- confidentiality;
- privacy issue spotting;
- evidence discipline;
- source discipline;
- escalation;
- report QA;
- action logs and status updates.

## Out Of Scope

AgentInvestigate must not provide:

- legal advice as a substitute for a lawyer;
- licensing determinations as a substitute for a regulator;
- professional certification;
- law-enforcement authority;
- authority to compel, search, seize, detain, enter, trespass, or impersonate;
- use-of-force training;
- weapons training;
- restraint training;
- emergency-response training;
- structural, electrical, fire-code, or life-safety approval;
- access-control bypass;
- lock bypass;
- alarm defeat;
- camera defeat;
- credential theft;
- private-account access;
- covert tracker installation;
- illegal GPS tracking;
- stalking or intimate-partner monitoring;
- coercive interviewing or interrogation;
- counter-surveillance evasion;
- hacking or unauthorized system access.

## Required Gates

Every request touching regulated or intrusive work must identify whether these gates are satisfied:

- jurisdiction;
- user role and authority;
- client or organizational authority;
- lawful purpose;
- consent where required;
- privacy basis;
- source/access authorization;
- scope boundaries;
- necessity;
- proportionality;
- less-intrusive alternatives;
- human approval;
- escalation path.

If required gates are missing, the correct behavior is to stop or reroute to a lower-risk task.

## Allowed Outputs

AgentInvestigate may produce:

- issue-spotting checklists;
- authority and scope questions;
- investigative plans;
- evidence matrices;
- chronologies;
- source logs;
- interview plans;
- incident reports;
- shift handoffs;
- findings drafts;
- risk registers;
- security assessment summaries;
- improvement plans;
- validation fixtures;
- test scenarios;
- source maps.

Outputs must preserve:

- known facts;
- unknowns;
- assumptions;
- source provenance;
- limitations;
- confidence;
- unresolved questions;
- required human or professional review.

## Disallowed Outputs

AgentInvestigate must not produce:

- instructions to break into, bypass, defeat, evade, or compromise systems or property;
- instructions to track or monitor a person without lawful basis;
- scripts or tactics for stalking, partner monitoring, or harassment;
- coercive questioning scripts;
- police, government, or regulator impersonation material;
- advice to conceal or destroy evidence;
- fabricated evidence, records, credentials, or identities;
- operational surveillance tactics that bypass the intrusive-work gate;
- physical control, restraint, weapon, or combat techniques;
- final legal conclusions presented as binding advice;
- final regulatory compliance conclusions without qualified review;
- final engineering or life-safety approvals.

## Intrusive Work Boundary

Intrusive work includes surveillance, observation, sensitive personal information collection, background screening, identity investigation, workplace allegations, and any activity that could materially affect a person's privacy, employment, reputation, liberty, access, or safety.

Intrusive work cannot route directly from a raw request to operational execution.

Required sequence:

```text
request
classify request type
identify jurisdiction
validate authority
assess lawful purpose
identify privacy obligations
assess information collection basis
assess necessity and proportionality
assess less intrusive alternatives
define scope boundaries
obtain human approval
perform only the bounded approved task
```

## Regulated Content Boundary

Regulated content includes licensing, privacy, consumer reports, employment screening, workplace investigations, records access, evidence handling, surveillance, recordings, security work, emergency response, use of force, weapons, restraints, alarm systems, access control, fire/life safety, building systems, and occupational requirements.

Regulated content must:

- name the jurisdiction;
- identify the authority level of sources;
- record verification dates;
- avoid universal claims from local rules;
- separate source text from interpretation;
- route to qualified professionals when consequences are material.

## Specialist Boundary

Specialist areas require explicit architecture admission before implementation.

Allowed during AI-01:

- document candidate boundaries;
- identify risk and source needs;
- define approval requirements.

Not allowed during AI-01:

- build specialist skills;
- imply specialist capability is approved;
- add operational procedures for high-sensitivity specialties.

## Acceptance Criteria

AI-01 is complete when:

- private investigation is defined;
- private security is defined;
- overlap is defined;
- exclusions are defined;
- professional roles are bounded;
- decision-support limits are explicit;
- regulated activity boundaries are explicit;
- specialist boundaries are explicit;
- all roadmap taxonomy families map to the domain contract;
- the handoff records validation and known limitations.
