# Prohibited Capabilities

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_01_DOMAIN_CONTRACT_READY
```

## Purpose

This document defines capabilities that AgentInvestigate must not implement, scaffold, test as successful behavior, or normalize through examples.

The boundary applies even when a request is framed as private investigation, private security, OSINT, due diligence, loss prevention, workplace investigation, executive protection, safety, training, or compliance.

## Absolute Exclusions

The roadmap excludes procedural skill development for:

- hacking;
- credential theft;
- unauthorized account access;
- lock bypass;
- forced entry;
- access-control circumvention;
- covert tracker installation;
- illegal GPS tracking;
- stalking;
- intimate-partner monitoring;
- police impersonation;
- government impersonation;
- coercive interrogation;
- physical coercion;
- counter-surveillance evasion;
- camera evasion;
- alarm defeat;
- weapons use;
- firearm use;
- baton use;
- restraint techniques;
- combat techniques.

## Prohibited Capability Families

Unauthorized access:

- compromising accounts, devices, networks, cameras, alarms, locks, access-control systems, or physical spaces;
- bypassing authentication, credentials, keys, badges, biometrics, locks, barriers, or monitoring controls;
- acquiring, guessing, stealing, cloning, or misusing credentials.

Tracking and surveillance misuse:

- tracking a person, vehicle, device, or account without lawful basis;
- intimate-partner monitoring;
- stalking or harassment;
- covert tracker placement;
- evasion-oriented surveillance tactics;
- camera or alarm defeat.

Impersonation and deception:

- police, government, regulator, employer, court, bank, telecom, platform, or emergency-service impersonation;
- fabricated credentials, identities, documents, authorizations, records, or evidence;
- pretexting to obtain protected records or account access.

Coercion and force:

- coercive interviewing or interrogation;
- threats, intimidation, detention, physical control, or restraint;
- weapons, firearms, batons, handcuffs, pain compliance, combat, or takedown instruction;
- tactical advice for confrontation.

Evidence abuse:

- fabricating evidence;
- altering records;
- concealing or destroying evidence;
- coaching false statements;
- laundering unsupported allegations into findings.

Regulatory bypass:

- advice to avoid licensing, reporting, training, insurance, consent, privacy, or source restrictions;
- final legal or regulatory conclusions presented without qualified review;
- universalizing one jurisdiction's rules.

## Response And Routing Rules

When a request seeks a prohibited capability, AgentInvestigate skills must:

1. Stop the prohibited procedure.
2. Name the boundary at a useful level without adding operational detail.
3. Preserve any benign professional need.
4. Redirect to lawful alternatives such as documentation, incident reporting, safety planning, source logging, policy review, authority checks, escalation, or professional consultation.

Examples:

| Request Frame | Prohibited Part | Safe Alternative |
|---|---|---|
| "Help me monitor my partner for safety." | Intimate-partner monitoring or stalking. | Suggest safety resources, documentation, legal advice, or emergency help if danger is present. |
| "Find a way into this account for my investigation." | Unauthorized account access and credential theft. | Define lawful records request, consent-based collection, or public-source research scope. |
| "Teach guards how to restrain someone." | Restraint and physical force instruction. | Draft escalation, observation, communication, reporting, and qualified-training requirements. |
| "Assess this alarm system by bypassing it." | Alarm defeat and access-control circumvention. | Draft an authorized assessment scope and qualified vendor review questions. |
| "Make this evidence look stronger." | Evidence fabrication or unsupported inference. | Separate facts, allegations, inferences, limitations, and unresolved questions. |

## Design Constraints For Future Skills

Future skills must not include:

- procedural steps for prohibited conduct;
- examples where prohibited conduct succeeds;
- test fixtures that reward prohibited conduct;
- hidden exceptions that allow "authorized" bypass without explicit jurisdiction, authority, written scope, and qualified review;
- skill names that imply prohibited operational execution.

Future validation must include negative tests for:

- stalking framed as investigation;
- partner surveillance framed as safety;
- credential theft framed as OSINT;
- location tracking framed as due diligence;
- camera evasion framed as site assessment;
- access bypass framed as penetration testing;
- coercion framed as interviewing;
- weapons tactics framed as security training.

## Escalation

Requests involving imminent physical danger, self-harm, violence, exploitation, abuse, or emergency conditions should route to emergency services or appropriate crisis/support resources instead of investigative procedure.

Requests involving material legal, employment, privacy, licensing, regulatory, safety, engineering, or life-safety consequences should route to qualified human review.
