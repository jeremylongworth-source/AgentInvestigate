# Routing Boundaries

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_30_ALBERTA_READY
```

## Purpose

This reference defines how the Alberta specialization affects AgentInvestigate routing. It does not create legal authority, licence status, training status, examination status, exemption status, compliance approval, or operational permission.

## Alberta Routing Rule

The Alberta module can support:

- investigator licensing issue spotting;
- security service worker licensing issue spotting;
- security business licensing issue spotting;
- training, approved-provider, and provincial examination research;
- training licence and registry processing issue spotting;
- professional conduct issue spotting;
- permitted authorities and restrictions research;
- privacy interaction research;
- reporting and recordkeeping issue spotting;
- security operations review questions;
- body-armour, baton, patrol-dog, equipment, uniform, locksmith-adjacent, and site-authority issue spotting;
- provincial laws materially relevant to scoped skills;
- escalation and qualified-review questions.

It cannot determine that private investigative or security work is authorized.

When authorization depends on Alberta individual licence type, business licence status, dual licence, training licence, registry temporary licence, exemption, approved training, provincial examination result, examination challenge, equivalent training, prior-experience recognition, records checks, licence conditions, professional conduct, uniforms, equipment, baton training, patrol dogs, body armour, permitted authority, use-of-force limits, post orders, trespass authority, privacy, public-sector access, reporting, retention, employment, workplace safety, or security-operation rules, route to:

```text
REGULATED_RESEARCH_ONLY
```

until current official sources are verified and the responsible qualified reviewer confirms the facts.

## Mandatory Non-Authority Statement

Outputs using this module must include:

```text
Alberta sources can identify provincial issue areas, but they do not by themselves authorize private investigative or security work without current individual licence status, business licence status, role, purpose, authority, and qualified review.
```

If federal issues are also present, add:

```text
Federal privacy, criminal-law, evidence, human-rights, federally regulated workplace, or labour issues may also apply and must be checked against the Canada federal specialization.
```

## Escalation Targets

Use the narrowest responsible escalation path supported by the facts:

- Security Programs;
- participating registry agent;
- Registrar or Ministry;
- counsel;
- privacy officer;
- HR;
- compliance;
- licensed investigator;
- licensed security manager;
- qualified trainer;
- security program manager;
- records manager;
- insurer;
- OIPC;
- police or emergency services when immediate safety or criminal-risk facts require it.

## Prohibited Routing

Route to `PROHIBITED_REDIRECT` for:

- licensing bypass;
- licence impersonation;
- using another person's licence;
- training-record fabrication;
- provincial examination cheating;
- hidden unlicensed work;
- hacking;
- credential theft;
- unauthorized account access;
- lock bypass;
- automotive lock bypass;
- restricted locksmith tool misuse;
- forced entry;
- access-control circumvention;
- covert tracker installation;
- illegal GPS tracking;
- stalking;
- intimate-partner monitoring;
- police, peace-officer, sheriff, special-constable, government, or by-law enforcement impersonation;
- coercive interrogation;
- physical coercion;
- detention tactics;
- search tactics;
- pursuit tactics;
- trespass-removal tactics;
- patrol-dog control tactics;
- baton tactics;
- body-armour bypass or permit evasion;
- camera evasion;
- alarm defeat;
- weapons use;
- restraint techniques;
- fabricated records;
- altered evidence;
- concealed source gaps;
- destroying records to avoid review.

## Certification Boundary

Route to `CERTIFICATION_ESCALATION` when the request asks AgentInvestigate to certify, approve, sign off, or guarantee:

- licence eligibility;
- investigator licence status;
- security service worker licence status;
- security business licence status;
- exemption status;
- training completion;
- approved provider status;
- provincial examination result;
- experience equivalency;
- professional conduct compliance;
- privacy compliance;
- human-rights compliance;
- workplace safety compliance;
- recordkeeping compliance;
- security-operation compliance;
- baton qualification;
- patrol-dog-handler approval;
- body-armour permit status;
- locksmith or automotive lock bypass readiness;
- use-of-force, restraint, weapons, emergency-response, alarm, camera, access-control, or life-safety readiness.

## Intrusive Task Boundary

Route to `INTRUSIVE_GATE_REQUIRED` when Alberta facts involve:

- surveillance or monitoring;
- video surveillance deployment or review;
- location tracking;
- biometric information;
- health information;
- sensitive workplace allegations;
- employee monitoring;
- third-party incidental capture;
- high-impact background screening;
- covert or persistent observation.

The intrusive gate must preserve jurisdiction, authority, necessity, proportionality, minimization, documentation, and human-review requirements.

## Verification Rule

Freshness: `HIGH`

Recheck official sources at time of use before relying on Alberta licensing, training, examinations, conduct, privacy, access, reporting, records, workplace, trespass, equipment, uniform, baton, patrol-dog, body-armour, locksmith-adjacent, or security-operation claims. If current verification is not available, label the output as an issue-spotting summary or research brief and route consequential decisions to qualified review.
