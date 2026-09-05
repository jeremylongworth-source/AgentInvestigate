# Training, Testing, And Conduct

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_28_ONTARIO_READY
```

## Purpose

This reference supports Ontario issue spotting for training, testing, professional conduct, and conduct-related escalation in private investigation and private security contexts.

## Source Basis

Freshness: `HIGH`

Use these source IDs from `source-log.yaml`:

- `ontario-requirements-individuals-guidance`
- `ontario-basic-training-guidance`
- `ontario-testing-guidance`
- `ontario-training-testing-regulation`
- `ontario-code-of-conduct-regulation`

Ontario's public guidance says new security guards and private investigators must complete basic training and pass the required ministry test before applying for a licence. The Ontario testing guidance describes tests as 60 multiple-choice questions with 75 minutes to complete them. Recheck the official pages before using these details because training providers, testing process, fees, course requirements, and pass requirements can change.

## Required Coverage

This module covers:

- training
- professional conduct
- security licensing
- investigator licensing
- restrictions
- reporting

## Training And Testing Boundaries

The module may identify training and testing as issue areas, summarize current official source claims when verified, and ask whether a candidate has completed the required training and test for the intended licence type.

The module must not:

- certify training completion;
- approve a training provider;
- provide licence exam answer keys;
- guarantee exam eligibility, pass marks, or results;
- certify a person as qualified for use-of-force, restraint, weapons, first aid, emergency response, privacy, accessibility, or other regulated or safety-sensitive functions;
- substitute for Ontario Ministry, testing-provider, trainer, employer, counsel, or regulator review.

## Conduct Issue Map

Ontario Code of Conduct issue spotting may include:

- honesty and integrity;
- compliance with applicable laws;
- respectful and professional treatment of people;
- discrimination and harassment concerns;
- language, intoxication, intimidation, and excessive-force boundaries;
- conflict, privacy, and documentation concerns;
- escalation where conduct complaints, public complaints, regulator issues, or discipline may arise.

## Allowed Support

Allowed outputs include:

- conduct issue checklists;
- training and testing source summaries;
- questions for candidates, employers, licensed agencies, supervisors, trainers, counsel, HR, compliance, and regulators;
- non-adjudicative review notes for post orders, policy drafts, or investigation files.

## Routing Rule

Use:

```text
REGULATED_RESEARCH_ONLY
```

when training, testing, licence status, conduct obligations, or complaint exposure may affect whether a person can perform the work.

Use:

```text
CERTIFICATION_ESCALATION
```

when the request asks for training certification, qualification signoff, compliance certification, use-of-force qualification, weapons qualification, or regulated professional approval.

Use:

```text
PROHIBITED_REDIRECT
```

when the request asks for coercive questioning, intimidation, evasion, concealed misconduct, fabricated training records, licence impersonation, or tactical force instructions.
