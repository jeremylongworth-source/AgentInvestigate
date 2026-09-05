# Licensing And Registration

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_29_BRITISH_COLUMBIA_READY
```

## Purpose

This reference supports BC issue spotting for security worker licensing, private investigator licence types, security guard licence types, security business licensing, out-of-province private investigator exemptions, eligibility, prescribed checks, and licence management.

## Source Basis

Freshness: `HIGH`

Use these source IDs from `source-log.yaml`:

- `bc-security-services-act`
- `bc-security-services-regulation`
- `bc-security-worker-licence-guidance`
- `bc-security-worker-application-guidance`
- `bc-security-business-licence-guidance`
- `bc-security-business-application-guidance`
- `bc-licensing-process-policies`

Recheck current official BC sources before relying on licensing, eligibility, exemption, business, worker, fee, form, or process claims.

## BC Licensing Issue Map

British Columbia regulates private investigation and private security work under the Security Services Act and Security Services Regulation. The module must distinguish at least these issue areas:

- security worker licensing
- private investigator licence types
- security guard licence types
- security business licensing
- licence-category or combined-licence questions;
- prescribed checks, identity verification, fingerprints, criminal record check consent, and suitability review;
- out-of-province private investigator exemption issue spotting;
- employee, self-employed contractor, security business, client, manager, supervisor, and in-house role boundaries.

## B.C.-Specific Intake Questions

Before giving BC regulated guidance, collect or flag missing:

- whether the work is physically in British Columbia or directed at a BC activity, site, subject, employer, client, or record;
- whether the actor is an individual security worker, private investigator, security guard, security business, employee, self-employed contractor, in-house worker, manager, supervisor, loss-prevention worker, door security worker, bodyguard, alarm worker, consultant, locksmith, armoured car guard, CCTV installer, electronic locking device installer, or body-armour salesperson;
- which kind of security work the person or business is licensed or applying to perform;
- whether the person or business claims an exemption, temporary licence, out-of-province private investigator exemption, or incidental-work determination;
- whether federal, municipal, site, contract, collective agreement, privacy, employment, workplace safety, Indigenous governance, insurance, or sector rules also apply.

## Allowed Support

The module may help produce:

- security worker licence research briefs;
- security business licence issue checklists;
- licence-category and role-boundary questions;
- missing-authority questions;
- source-backed summaries of what must be verified with current BC sources;
- referral questions for Security Programs Division, counsel, licensed business leadership, HR, compliance, privacy officers, or insurers.

## Non-Authority Boundary

This module must not:

- approve an individual or business to perform BC security work;
- decide that a person is eligible for a security worker licence;
- decide that a business is eligible for a security business licence;
- decide that an exemption, temporary licence, out-of-province investigator exemption, or incidental-work determination applies;
- complete or submit a licence application;
- replace Registrar or Security Programs Division review;
- treat federal authority, employer direction, client consent, contract terms, job title, out-of-province licence, or prior experience as BC licensing authority.

## Routing Rule

If BC licensing, worker licence status, business licence status, eligibility, category, prescribed checks, out-of-province investigator exemption, or incidental-work status is unresolved, route to:

```text
REGULATED_RESEARCH_ONLY
```

If the request asks how to bypass licensing, impersonate a licence holder, use someone else's licence, hide unlicensed work, fabricate records, or continue after known noncompliance, route to:

```text
PROHIBITED_REDIRECT
```
