# Authority, Restrictions, And Security Operations

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_29_BRITISH_COLUMBIA_READY
```

## Purpose

This reference supports BC issue spotting for permitted authorities, restrictions, security operations, post orders, uniforms, equipment, dogs, body armour, site authority, and operational escalation.

## Source Basis

Freshness: `HIGH`

Use these source IDs from `source-log.yaml`:

- `bc-security-services-act`
- `bc-security-services-regulation`
- `bc-security-business-rules-guidance`
- `bc-body-armour-control-act`
- `bc-body-armour-control-regulation`
- `bc-body-armour-possession-guidance`
- `bc-trespass-act`
- `bc-workers-compensation-act`
- `bc-ohs-regulation`

Recheck current BC sources before using any operational, equipment, uniform, dog, body-armour, trespass, workplace-safety, or response claim.

## Required Coverage

This module covers:

- permitted authorities
- restrictions
- security operations
- reporting
- provincial laws materially relevant to scoped skills

## BC Authority Framing

The BC module may help identify whether a task implicates:

- security worker licensing;
- private investigator work;
- security guard service work;
- security business work;
- in-house employer-directed work;
- self-employed contractor work;
- loss-prevention work;
- door security, bodyguard, alarm, locksmith, CCTV, electronic locking device, armoured car, or body-armour sales work;
- site-specific security operations;
- post orders, patrols, access control, observation, alarms, incident documentation, and supervisor notification;
- equipment, uniform, dog, body-armour, identification, advertising, vehicle, and public-representation rules.

It must not treat BC private security or investigation roles as police, peace-officer, sheriff, special-constable, by-law, search, seizure, or detention authority.

## Security Operations Support

Allowed operational outputs are planning and documentation oriented:

- post-order review questions;
- shift-brief and patrol-documentation checklists;
- access-event documentation fields;
- incident reporting fields;
- supervisor-notification triggers;
- licence, authority, privacy, safety, and escalation gaps;
- questions for site leadership, licensed security managers, counsel, HR, privacy officers, insurers, Security Programs Division, or regulators.

## BC Restrictions And Escalation

Do not provide instructions for:

- physical intervention;
- use of force;
- restraining device, weapon, baton, firearm, or body-armour use;
- dog-control tactics;
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
- police, peace-officer, sheriff, special-constable, or government impersonation.

BC equipment, uniform, dog, body-armour, and site-authority questions are always fact-specific. The module can flag that BC regulations and body-armour law may apply, but it must route safety-sensitive or authority-dependent action to qualified review.

## Routing Rule

Use:

```text
REGULATED_RESEARCH_ONLY
```

for BC security-operation research, post-order review, uniform/equipment/dog/body-armour issue spotting, site-authority questions, or trespass issue spotting where the user is not asking for tactical or coercive steps.

Use:

```text
CERTIFICATION_ESCALATION
```

for requests seeking safety, restraint, weapons, force, emergency-response, dog-handler, body-armour, trainer, regulator, insurer, fire/life-safety, or compliance signoff.

Use:

```text
PROHIBITED_REDIRECT
```

for requests seeking bypass, evasion, impersonation, unlawful entry, physical coercion, tactical detention, tactical search, tactical dog handling, or tactical force instructions.
