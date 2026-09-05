# Licensing And Registration

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_28_ONTARIO_READY
```

## Purpose

This reference supports Ontario issue spotting for investigator licensing, security licensing, dual licences, licensed agencies, licensed corporations, business entities, exemptions, eligibility, and registration questions.

## Source Basis

Freshness: `HIGH`

Use these source IDs from `source-log.yaml`:

- `ontario-psisa-act`
- `ontario-individual-licence-guidance`
- `ontario-agency-corporation-licence-guidance`
- `ontario-clean-criminal-record-regulation`
- `ontario-exemptions-regulation`

Recheck current official Ontario sources before relying on licensing, eligibility, agency, corporation, fee, form, or process claims.

## Ontario Licensing Issue Map

Ontario private investigation and private security work is regulated under the Private Security and Investigative Services Act, 2005 and related regulations. The module must distinguish at least these issue areas:

- licence to act as a private investigator;
- licence to act as a security guard;
- dual individual licence to act as both;
- agency or corporation licence to sell or provide private investigator services;
- agency or corporation licence to sell or provide security guard services;
- eligibility and clean criminal record issue spotting;
- exemption issue spotting;
- employer, agency, business entity, client, and worker role boundaries.

## Intake Questions

Before giving Ontario regulated guidance, collect or flag missing:

- whether the work is physically in Ontario or directed at an Ontario activity, site, subject, employer, client, or record;
- whether the actor is an individual, agency, corporation, employer, client, in-house employee, contractor, loss-prevention worker, security guard, private investigator, supervisor, or manager;
- whether the task is investigation, guarding, patrol, access control, loss prevention, screening, workplace investigation, surveillance, records review, or system monitoring;
- whether the actor claims an Ontario licence, dual licence, agency licence, exemption, or other authority;
- whether federal, municipal, site, contract, collective agreement, privacy, employment, health-information, insurance, or sector rules also apply.

## Allowed Support

The module may help produce:

- licensing research briefs;
- licence-type issue checklists;
- missing-authority questions;
- source-backed summaries of what must be verified with current Ontario sources;
- referral questions for the Ministry, counsel, licensed agency leadership, HR, compliance, privacy officers, or insurers.

## Non-Authority Boundary

This module must not:

- approve an individual, agency, corporation, employer, or contractor to perform Ontario private investigative or security work;
- decide that a person is eligible for a licence;
- decide that an exemption applies;
- complete or submit a licence application;
- replace Ministry review;
- treat federal authority, employer direction, client consent, contract terms, job title, or prior experience as Ontario licensing authority.

## Routing Rule

If Ontario licensing, eligibility, agency/corporation licensing, or exemption status is unresolved, route to:

```text
REGULATED_RESEARCH_ONLY
```

If the request asks how to bypass licensing, impersonate a licensed person, hide unlicensed work, fabricate records, or continue after known noncompliance, route to:

```text
PROHIBITED_REDIRECT
```
