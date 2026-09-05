# Licensing And Registration

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_30_ALBERTA_READY
```

## Purpose

This reference supports Alberta issue spotting for investigator licensing, security service worker licensing, security business licensing, registry processing, training licences, dual security service and investigator licences, eligibility, records checks, business requirements, and locksmith-adjacent boundaries.

## Source Basis

Freshness: `HIGH`

Use these source IDs from `source-log.yaml`:

- `alberta-ssia-act`
- `alberta-ssia-regulation`
- `alberta-ssia-ministerial-regulation`
- `alberta-security-licences-permits-guidance`
- `alberta-security-service-worker-licence-guidance`
- `alberta-investigator-licence-guidance`
- `alberta-security-licences-registries-guidance`
- `alberta-security-investigation-locksmith-business-resources`
- `alberta-ssia-policy-manual`

Recheck current official Alberta sources before relying on licensing, eligibility, registry, business, worker, fee, form, records-check, or process claims.

## Alberta Licensing Issue Map

Alberta regulates security, investigation, locksmith, and related business activity under the Security Services and Investigators Act, regulations, policy, and Security Programs guidance. The module must distinguish at least these issue areas:

- investigator licensing
- security service worker licensing
- security business licensing
- security guard, patrol dog handler, alarm responder, loss prevention worker, bodyguard, and private investigator licence classes;
- dual security service and investigator licensing;
- business licences for security, investigation, locksmith, automotive lock bypass, training, and in-house services;
- training licence issue spotting;
- registry-agent temporary licence processing;
- records checks, vulnerable sector searches, local police database searches, eligibility, English fluency, and work authorization issue spotting;
- locksmith, locksmith equipment sales worker, and automotive lock bypass worker boundaries where a request touches lock bypass, restricted tools, or adjacent security work.

## Alberta-Specific Intake Questions

Before giving Alberta regulated guidance, collect or flag missing:

- whether the work is physically in Alberta or directed at an Alberta activity, site, subject, employer, client, business, training provider, permit, or record;
- whether the actor is an investigator, in-house investigator, security service worker, security guard, loss prevention worker, patrol dog handler, alarm responder, bodyguard, business owner, training provider, registry applicant, locksmith, locksmith equipment sales worker, automotive lock bypass worker, employee, contractor, supervisor, or manager;
- which individual licence class, business licence class, training licence, registry process, or body-armour permit is involved;
- whether the person or business claims an exemption, temporary licence, dual licence, training licence, equivalent training, prior law-enforcement experience, or out-of-province credential;
- whether federal, municipal, site, contract, collective agreement, privacy, employment, workplace safety, Indigenous governance, insurance, or sector rules also apply.

## Allowed Support

The module may help produce:

- investigator licence research briefs;
- security service worker licence research briefs;
- security business licence issue checklists;
- licence-class and role-boundary questions;
- training licence and registry process checklists;
- missing-authority questions;
- source-backed summaries of what must be verified with current Alberta sources;
- referral questions for Security Programs, registry agents, counsel, licensed business leadership, HR, compliance, privacy officers, or insurers.

## Non-Authority Boundary

This module must not:

- approve an individual or business to perform Alberta security or investigative work;
- decide that a person is eligible for an investigator, security service worker, security guard, patrol dog handler, alarm responder, loss prevention, bodyguard, locksmith, automotive lock bypass, or dual licence;
- decide that a business is eligible for a security, investigation, locksmith, automotive lock bypass, training, or in-house services licence;
- decide that an exemption, temporary licence, training licence, equivalent training, prior-experience recognition, registry criterion, or out-of-province credential applies;
- complete or submit a licence application;
- replace Security Programs, registry agent, Registrar, or Ministry review;
- treat federal authority, employer direction, client consent, contract terms, job title, out-of-province licence, or prior experience as Alberta licensing authority.

## Routing Rule

If Alberta licensing, licence status, business licence status, eligibility, licence class, records checks, registry processing, training licence, dual licence, exemption, equivalent training, prior-experience recognition, or out-of-province credential status is unresolved, route to:

```text
REGULATED_RESEARCH_ONLY
```

If the request asks how to bypass licensing, impersonate a licence holder, use someone else's licence, hide unlicensed work, fabricate records, bypass locksmith restrictions, or continue after known noncompliance, route to:

```text
PROHIBITED_REDIRECT
```
