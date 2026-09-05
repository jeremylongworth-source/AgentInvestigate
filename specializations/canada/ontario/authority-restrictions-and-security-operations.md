# Authority, Restrictions, And Security Operations

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_28_ONTARIO_READY
```

## Purpose

This reference supports Ontario issue spotting for permitted authorities, restrictions, security operations, post orders, uniforms, equipment, site authority, and operational escalation.

## Source Basis

Freshness: `HIGH`

Use these source IDs from `source-log.yaml`:

- `ontario-psisa-act`
- `ontario-requirements-individuals-guidance`
- `ontario-uniforms-regulation`
- `ontario-equipment-regulation`
- `ontario-trespass-to-property-act`
- `ontario-ohsa`

Recheck current Ontario sources before using any operational, equipment, uniform, trespass, workplace-safety, or response claim.

## Required Coverage

This module covers:

- permitted authorities
- restrictions
- security operations
- reporting
- provincial laws materially relevant to scoped skills

## Ontario Authority Framing

The Ontario module may help identify whether a task implicates:

- security guard work;
- private investigator work;
- dual-licence work;
- licensed agency or corporation work;
- in-house employer-directed work;
- loss-prevention work;
- site-specific security operations;
- post orders, patrols, access control, observation, alarms, incident documentation, and supervisor notification;
- equipment, uniform, identification, and public-representation rules.

It must not treat Ontario private security or investigation roles as police, peace-officer, by-law enforcement, search, seizure, or detention authority.

## Security Operations Support

Allowed operational outputs are planning and documentation oriented:

- post-order review questions;
- shift-brief and patrol-documentation checklists;
- access-event documentation fields;
- incident reporting fields;
- supervisor-notification triggers;
- authority, licensing, privacy, safety, and escalation gaps;
- questions for site leadership, licensed security managers, counsel, HR, privacy officers, insurers, or regulators.

## Restrictions And Escalation

Do not provide instructions for:

- physical intervention;
- use of force;
- handcuffing, restraint, baton, firearm, or dog-handling technique;
- pursuit;
- search;
- detention;
- trespass removal;
- intimidation;
- surveillance evasion;
- alarm defeat;
- access-control bypass;
- lock bypass;
- forced entry;
- police or government impersonation.

Equipment, uniform, and site-authority questions are always fact-specific. The module can flag that Ontario equipment and uniform regulations may apply, but it must route any safety-sensitive or authority-dependent action to qualified review.

## Routing Rule

Use:

```text
REGULATED_RESEARCH_ONLY
```

for Ontario security-operation research, post-order review, uniform/equipment issue spotting, site-authority questions, or trespass issue spotting where the user is not asking for tactical or coercive steps.

Use:

```text
CERTIFICATION_ESCALATION
```

for requests seeking safety, restraint, weapons, force, emergency-response, trainer, regulator, insurer, fire/life-safety, or compliance signoff.

Use:

```text
PROHIBITED_REDIRECT
```

for requests seeking bypass, evasion, impersonation, unlawful entry, physical coercion, tactical detention, tactical search, or tactical force instructions.
