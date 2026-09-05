# Training And Conduct

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_29_BRITISH_COLUMBIA_READY
```

## Purpose

This reference supports BC issue spotting for training, experience, qualification, licence conditions, and professional conduct in private investigation and private security contexts.

## Source Basis

Freshness: `HIGH`

Use these source IDs from `source-log.yaml`:

- `bc-security-services-regulation`
- `bc-security-worker-training-guidance`
- `bc-security-worker-rules-guidance`
- `bc-licensing-process-policies`

BC training and qualification requirements depend on the licence type and facts. Government guidance checked for AI-29 identifies security guard and private investigator training categories, and the Security Services Regulation includes qualification rules, prescribed checks, licence conditions, and code-of-conduct conditions. Recheck the official pages before using details because approved training, experience alternatives, forms, fees, and licence conditions can change.

## Required Coverage

This module covers:

- training
- professional conduct
- security worker licensing
- private investigator licence types
- security guard licence types
- restrictions
- reporting

## Training And Qualification Boundaries

The module may identify training, experience, and qualification as issue areas, summarize current official source claims when verified, and ask whether a candidate has evidence of required training or experience for the intended licence type.

The module must not:

- certify training completion;
- approve a training provider;
- provide licence exam answer keys;
- guarantee eligibility, suitability, licence issuance, renewal, conditions, or results;
- certify a person as qualified for use-of-force, restraint, weapons, dog handling, body armour, first aid, emergency response, privacy, accessibility, or other regulated or safety-sensitive functions;
- substitute for Registrar, Security Programs Division, trainer, employer, counsel, insurer, or regulator review.

## Conduct Issue Map

BC Security Services Regulation Code of Conduct issue spotting may include:

- honesty and integrity;
- compliance with federal, provincial, and municipal laws;
- respectful and equal treatment of people;
- discrimination concerns;
- privacy and confidentiality concerns;
- property and equipment use;
- unnecessary-force boundaries;
- prohibited behaviour;
- escalation where complaints, inspections, investigations, licence conditions, or discipline may arise.

## Allowed Support

Allowed outputs include:

- conduct issue checklists;
- training and qualification source summaries;
- licence-condition research briefs;
- questions for candidates, employers, licensed businesses, supervisors, trainers, counsel, HR, compliance, Security Programs Division, and regulators;
- non-adjudicative review notes for post orders, policy drafts, or investigation files.

## Routing Rule

Use:

```text
REGULATED_RESEARCH_ONLY
```

when training, experience, licence status, licence conditions, conduct obligations, or complaint exposure may affect whether a person can perform the work.

Use:

```text
CERTIFICATION_ESCALATION
```

when the request asks for training certification, qualification signoff, compliance certification, use-of-force qualification, weapons qualification, dog-handler approval, body-armour permit approval, or regulated professional approval.

Use:

```text
PROHIBITED_REDIRECT
```

when the request asks for coercive questioning, intimidation, evasion, concealed misconduct, fabricated training records, licence impersonation, dog-control tactics, or tactical force instructions.
