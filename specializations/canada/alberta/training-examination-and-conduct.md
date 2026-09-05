# Training, Examination, And Conduct

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_30_ALBERTA_READY
```

## Purpose

This reference supports Alberta issue spotting for training, approved courses, provincial examinations, rewrites, challenges, training licences, baton training, experience, licence conditions, and professional conduct in private investigation and private security contexts.

## Source Basis

Freshness: `HIGH`

Use these source IDs from `source-log.yaml`:

- `alberta-ssia-regulation`
- `alberta-ssia-ministerial-regulation`
- `alberta-security-service-worker-licence-guidance`
- `alberta-investigator-licence-guidance`
- `alberta-ssia-policy-manual`
- `alberta-approved-training-courses`
- `alberta-provincial-examination-process`
- `alberta-guidelines-code-conduct`
- `alberta-guidelines-licensing-training-courses`

Alberta guidance checked for AI-30 says security service workers and investigators must complete approved training and score 80% or higher on the provincial final exam, with specific approved course pathways and possible Security Programs review for prior law-enforcement or equivalent training. Recheck the official pages before using details because training providers, course licensing, examination, rewrite, challenge, equivalency, and application rules can change.

## Required Coverage

This module covers:

- training
- provincial examinations
- professional conduct
- investigator licensing
- security service worker licensing
- restrictions
- reporting

## Training And Examination Boundaries

The module may identify training, provincial examination, rewrite, challenge, course-provider, and qualification as issue areas, summarize current official source claims when verified, and ask whether a candidate has evidence of required training or experience for the intended licence class.

The module must not:

- certify training completion;
- approve a training provider;
- provide provincial examination answer keys;
- guarantee exam eligibility, challenge approval, rewrite approval, pass results, training certificates, licence issuance, renewal, conditions, or suitability;
- certify a person as qualified for baton use, use-of-force, restraint, weapons, patrol dog handling, body armour, first aid, emergency response, privacy, accessibility, or other regulated or safety-sensitive functions;
- substitute for Security Programs, Registrar, registry agent, trainer, employer, counsel, insurer, or regulator review.

## Conduct Issue Map

Alberta conduct issue spotting may include:

- professional conduct and business code-of-conduct expectations;
- compliance with Security Services and Investigators Act requirements, regulations, licence conditions, and Security Programs policies;
- honesty, integrity, and competence;
- respectful and non-discriminatory treatment of people;
- privacy and confidentiality concerns;
- property and equipment use;
- unnecessary-force, baton, patrol-dog, body-armour, and safety-sensitive boundaries;
- escalation where complaints, inspections, investigations, licence conditions, or discipline may arise.

## Baton Training Boundary

Alberta security service worker and investigator guidance checked for AI-30 identifies approved 40-hour baton use-of-force training and employer approval as issues for carrying a baton, with re-certification every 36 months. This module may flag those as current-source issues only. It must not teach baton tactics, approve baton carriage, certify force readiness, or provide use-of-force instruction.

## Allowed Support

Allowed outputs include:

- conduct issue checklists;
- training and provincial examination source summaries;
- approved-provider and licence-condition research briefs;
- questions for candidates, employers, licensed businesses, supervisors, trainers, counsel, HR, compliance, Security Programs, registry agents, and regulators;
- non-adjudicative review notes for post orders, policy drafts, or investigation files.

## Routing Rule

Use:

```text
REGULATED_RESEARCH_ONLY
```

when training, provincial examinations, rewrites, challenges, course providers, licence status, licence conditions, conduct obligations, baton training, or complaint exposure may affect whether a person can perform the work.

Use:

```text
CERTIFICATION_ESCALATION
```

when the request asks for training certification, provincial examination approval, qualification signoff, compliance certification, baton qualification, use-of-force qualification, weapons qualification, patrol-dog-handler approval, body-armour permit approval, or regulated professional approval.

Use:

```text
PROHIBITED_REDIRECT
```

when the request asks for coercive questioning, intimidation, evasion, concealed misconduct, fabricated training records, licence impersonation, provincial examination cheating, patrol-dog tactics, baton tactics, or tactical force instructions.
