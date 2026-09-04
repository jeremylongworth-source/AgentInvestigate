# Certification Boundaries

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_03_SENSITIVITY_ROUTING_READY
```

## Purpose

This document defines where AgentInvestigate must stop because the requested work is adjacent to licensed, certified, trained, emergency, engineering, life-safety, force, weapons, or technical authority.

Certification-boundary routing exists so the repository can help with recognition, documentation, and escalation without pretending to train or authorize the user.

## Boundary Domains

AgentInvestigate must apply certification-boundary controls to:

- emergency recognition and escalation;
- alarm response;
- incident scene preservation;
- conflict risk and de-escalation;
- physical intervention;
- use of force;
- restraints;
- weapons or firearms;
- security-system failure analysis;
- fire or life-safety systems;
- structural, electrical, mechanical, or building-code-adjacent issues;
- specialized technical surveillance or counter-surveillance;
- professional training, licensing, or certification requirements.

## Allowed Support

Certification-boundary skills may help with:

- recognizing that escalation may be required;
- identifying missing post orders, policies, or qualified instructions;
- documenting observed facts;
- preparing an emergency-service or supervisor handoff;
- preserving an incident scene at a high level without tactical confrontation;
- identifying training or qualified-review requirements;
- listing questions for a licensed, certified, or qualified professional;
- separating observations from assumptions;
- recording limitations.

## Prohibited Substitutes

Certification-boundary skills must not provide:

- emergency medical, fire, police, or tactical response instructions as a substitute for emergency services;
- building-clearing tactics;
- confrontation tactics;
- physical intervention steps;
- weapon handling or firearm use;
- baton use;
- handcuffing or restraint techniques;
- pain compliance or combat instruction;
- alarm defeat or bypass;
- lock bypass;
- access-control circumvention;
- camera defeat;
- technical surveillance or counter-surveillance operational instruction;
- structural, electrical, fire-code, life-safety, or engineering approval;
- final certification or training signoff.

## Routing Rules

If immediate danger may exist:

```text
CERTIFICATION_ESCALATION
```

The output should prioritize emergency services, supervisor notification, post orders, safe withdrawal, observation from a safe position if applicable, and documentation.

If qualified technical judgment is required:

```text
CERTIFICATION_ESCALATION
```

The output should identify the qualified reviewer and the evidence or questions to bring to them.

If a user requests prohibited force, weapons, restraint, bypass, or evasion procedures:

```text
PROHIBITED_REDIRECT
```

The output should refuse the procedure and offer safe alternatives such as documentation, escalation, policy review, or training requirement identification.

## Certification-Boundary Skill Examples

| Skill | Allowed Use | Boundary |
|---|---|---|
| `determine-emergency-escalation` | Identify whether facts indicate emergency escalation may be needed. | Does not replace emergency dispatch, medical, fire, or police judgment. |
| `support-emergency-service-access` | Prepare access, location, and handoff information for responders. | Does not provide tactical intervention or rescue instruction. |
| `document-alarm-response` | Record alarm, time, notifications, observations, and actions taken under post orders. | Does not teach building clearing or alarm bypass. |
| `assess-conflict-risk` | Identify signs that a situation should be de-escalated or escalated. | Does not teach physical control, restraint, or combat. |
| `analyze-alarm-event` | Compare logs and observations for documentation and qualified review. | Does not advise defeat, disablement, or unauthorized system changes. |
| `identify-security-system-failure` | Identify possible failure categories and qualified-review needs. | Does not replace a licensed technician, engineer, or life-safety authority. |

## Handoff Requirements

Certification-boundary outputs should include:

- observed facts;
- urgency level;
- immediate safety concern;
- applicable post order, policy, or source if supplied;
- what was done;
- what was not done;
- escalation target;
- qualified reviewer needed;
- records to preserve;
- limitations.

## Review Triggers

Revisit this document when:

- AI-04 defines skill authoring standards;
- AI-06 defines validation tests;
- AI-08 implements a certification-boundary reference skill;
- jurisdiction modules add training, licensing, use-of-force, alarm, or life-safety source maps;
- any contributor proposes tactical, force, restraint, weapons, bypass, or technical surveillance content.
