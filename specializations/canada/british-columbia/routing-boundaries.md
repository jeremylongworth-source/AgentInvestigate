# Routing Boundaries

Status: `READY`

Completion token:

```text
AGENTINVESTIGATE_AI_29_BRITISH_COLUMBIA_READY
```

## Purpose

This reference defines how the British Columbia specialization affects AgentInvestigate routing. It does not create legal authority, licence status, training status, exemption status, compliance approval, or operational permission.

## BC Routing Rule

The BC module can support:

- security worker licensing issue spotting;
- private investigator licence type issue spotting;
- security guard licence type issue spotting;
- security business licensing issue spotting;
- out-of-province private investigator exemption issue spotting;
- training, experience, and qualification research;
- professional conduct issue spotting;
- permitted authorities and restrictions research;
- privacy interaction research;
- reporting and recordkeeping issue spotting;
- security operations review questions;
- body-armour, equipment, uniform, dog-use, and site-authority issue spotting;
- provincial laws materially relevant to scoped skills;
- escalation and qualified-review questions.

It cannot determine that private investigative or security work is authorized.

When authorization depends on BC security worker licence type, security business licence status, exemption, temporary licence, out-of-province private investigator exemption, incidental-work determination, training, experience, prescribed checks, licence conditions, professional conduct, uniforms, equipment, dogs, body armour, permitted authority, use-of-force limits, post orders, trespass authority, privacy, reporting, retention, employment, workplace safety, or security-operation rules, route to:

```text
REGULATED_RESEARCH_ONLY
```

until current official sources are verified and the responsible qualified reviewer confirms the facts.

## Mandatory Non-Authority Statement

Outputs using this module must include:

```text
British Columbia sources can identify provincial issue areas, but they do not by themselves authorize private investigative or security work without current security worker licence status, security business licence status, role, purpose, authority, and qualified review.
```

If federal issues are also present, add:

```text
Federal privacy, criminal-law, evidence, human-rights, federally regulated workplace, or labour issues may also apply and must be checked against the Canada federal specialization.
```

## Escalation Targets

Use the narrowest responsible escalation path supported by the facts:

- Security Programs Division or Registrar;
- counsel;
- privacy officer;
- HR;
- compliance;
- licensed private investigator;
- licensed security manager;
- qualified trainer;
- security program manager;
- records manager;
- insurer;
- police or emergency services when immediate safety or criminal-risk facts require it.

## Prohibited Routing

Route to `PROHIBITED_REDIRECT` for:

- licensing bypass;
- licence impersonation;
- using another person's licence;
- training-record fabrication;
- hidden unlicensed work;
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
- police, peace-officer, sheriff, special-constable, government, or by-law enforcement impersonation;
- coercive interrogation;
- physical coercion;
- detention tactics;
- search tactics;
- pursuit tactics;
- trespass-removal tactics;
- dog-control tactics;
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
- security worker licence status;
- security business licence status;
- exemption status;
- training completion;
- experience equivalency;
- professional conduct compliance;
- privacy compliance;
- human-rights compliance;
- workplace safety compliance;
- recordkeeping compliance;
- security-operation compliance;
- dog-use authorization;
- body-armour permit status;
- use-of-force, restraint, weapons, emergency-response, alarm, camera, access-control, or life-safety readiness.

## Intrusive Task Boundary

Route to `INTRUSIVE_GATE_REQUIRED` when BC facts involve:

- surveillance or monitoring;
- video surveillance deployment or review;
- location tracking;
- biometric information;
- sensitive workplace allegations;
- employee monitoring;
- third-party incidental capture;
- high-impact background screening;
- covert or persistent observation.

The intrusive gate must preserve jurisdiction, authority, necessity, proportionality, minimization, documentation, and human-review requirements.

## Verification Rule

Freshness: `HIGH`

Recheck official sources at time of use before relying on BC licensing, training, conduct, privacy, reporting, records, workplace, trespass, equipment, uniform, dog-use, body-armour, or security-operation claims. If current verification is not available, label the output as an issue-spotting summary or research brief and route consequential decisions to qualified review.
