# Authority, Restrictions, And Security Operations

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_30_ALBERTA_READY
```

## Purpose

This reference supports Alberta issue spotting for permitted authorities, restrictions, security operations, post orders, uniforms, equipment, batons, patrol dogs, body armour, site authority, locksmith-adjacent restrictions, and operational escalation.

## Source Basis

Freshness: `HIGH`

Use these source IDs from `source-log.yaml`:

- `alberta-ssia-act`
- `alberta-ssia-regulation`
- `alberta-ssia-ministerial-regulation`
- `alberta-security-service-worker-licence-guidance`
- `alberta-investigator-licence-guidance`
- `alberta-security-investigation-locksmith-business-resources`
- `alberta-body-armour-permit-guidance`
- `alberta-body-armour-control-act`
- `alberta-body-armour-control-regulation`
- `alberta-trespass-to-premises-act`
- `alberta-petty-trespass-act`
- `alberta-ohs-act`
- `alberta-ohs-act-regulation-code-guidance`

Recheck current Alberta sources before using any operational, equipment, uniform, baton, patrol-dog, body-armour, trespass, workplace-safety, lock-related, or response claim.

## Required Coverage

This module covers:

- permitted authorities
- restrictions
- security operations
- body armour
- reporting
- provincial laws materially relevant to scoped skills

## Alberta Authority Framing

The Alberta module may help identify whether a task implicates:

- investigator licensing;
- security service worker licensing;
- security guard, loss prevention worker, alarm responder, bodyguard, patrol dog handler, or private investigator licence classes;
- security business licensing;
- in-house services business licensing;
- training business licensing;
- employer-directed work;
- contract security or investigative services;
- post orders, patrols, access control, observation, alarms, incident documentation, and supervisor notification;
- body armour, baton training, uniforms, equipment, identification, advertising, vehicle, registry, and public-representation rules;
- locksmith or automotive lock bypass boundaries where lock access, restricted tools, or vehicle-entry requests are present.

It must not treat Alberta private security, loss prevention, bodyguard, patrol dog, or investigation roles as police, peace-officer, sheriff, special-constable, by-law, search, seizure, or detention authority.

## Security Operations Support

Allowed operational outputs are planning and documentation oriented:

- post-order review questions;
- shift-brief and patrol-documentation checklists;
- access-event documentation fields;
- incident reporting fields;
- supervisor-notification triggers;
- licence, authority, privacy, safety, body-armour, baton, patrol-dog, and escalation gaps;
- questions for site leadership, licensed security managers, counsel, HR, privacy officers, insurers, Security Programs, registry agents, or regulators.

## Alberta Restrictions And Escalation

Do not provide instructions for:

- physical intervention;
- use of force;
- baton technique;
- restraining device, weapon, firearm, or body-armour use;
- patrol-dog control tactics;
- pursuit;
- search;
- detention;
- trespass removal;
- intimidation;
- surveillance evasion;
- alarm defeat;
- access-control bypass;
- lock bypass;
- automotive lock bypass;
- forced entry;
- police, peace-officer, sheriff, special-constable, or government impersonation.

Alberta equipment, uniform, baton, patrol-dog, body-armour, locksmith, automotive lock bypass, and site-authority questions are always fact-specific. The module can flag that Alberta SSIA, Body Armour Control Act, trespass, and OHS sources may apply, but it must route safety-sensitive or authority-dependent action to qualified review.

## Routing Rule

Use:

```text
REGULATED_RESEARCH_ONLY
```

for Alberta security-operation research, post-order review, uniform/equipment/baton/patrol-dog/body-armour issue spotting, site-authority questions, or trespass issue spotting where the user is not asking for tactical or coercive steps.

Use:

```text
CERTIFICATION_ESCALATION
```

for requests seeking safety, restraint, weapons, force, emergency-response, baton, patrol-dog, body-armour, trainer, regulator, insurer, fire/life-safety, registry, or compliance signoff.

Use:

```text
PROHIBITED_REDIRECT
```

for requests seeking bypass, evasion, impersonation, unlawful entry, physical coercion, tactical detention, tactical search, tactical dog handling, baton tactics, locksmith bypass, automotive lock bypass, or tactical force instructions.
