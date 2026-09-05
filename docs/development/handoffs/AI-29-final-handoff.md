# Wave

AI-29

# Objective

Create the British Columbia Investigation & Security Module at `specializations/canada/british-columbia/`.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_29_BRITISH_COLUMBIA_READY
```

# Scope Completed

- Created the separately sourced BC provincial specialization module at `specializations/canada/british-columbia/`.
- Added HIGH-freshness source metadata in `source-log.yaml`.
- Added BC security worker, private investigator, security guard, security business, eligibility, licence-condition, exemption, out-of-province private investigator, and incidental-work issue spotting.
- Added BC training, experience, qualification, licence-condition, and professional conduct boundaries.
- Added BC permitted-authority, restriction, equipment, uniform, dog, body-armour, post-order, and security-operation boundaries.
- Added BC privacy, reporting, complaint, Registrar-notification, recordkeeping, employee monitoring, public-sector, private-sector, and surveillance-currentness coverage.
- Added BC provincial law map for the Security Services Act, Security Services Regulation, PIPA, FIPPA, Human Rights Code, Workers Compensation Act, Occupational Health and Safety Regulation, Trespass Act, Employment Standards Act, and Body Armour Control Act sources.
- Added routing boundaries preserving non-authority, intrusive-task, certification, and prohibited-output gates.
- Added AI-29 regulatory fixture coverage.
- Extended specialization and documentation validation for AI-29.
- Updated README and changelog.

# Module Files

- `specializations/canada/british-columbia/README.md`
- `specializations/canada/british-columbia/source-log.yaml`
- `specializations/canada/british-columbia/licensing-and-registration.md`
- `specializations/canada/british-columbia/training-and-conduct.md`
- `specializations/canada/british-columbia/authority-restrictions-and-security-operations.md`
- `specializations/canada/british-columbia/privacy-reporting-and-records.md`
- `specializations/canada/british-columbia/provincial-laws-map.md`
- `specializations/canada/british-columbia/routing-boundaries.md`

# Research Areas Covered

- security worker licensing
- private investigator licence types
- security guard licence types
- security business licensing
- training
- professional conduct
- permitted authorities
- restrictions
- privacy interaction
- reporting
- security operations
- provincial laws materially relevant to scoped skills

# Source Basis

AI-29 used official British Columbia and BC privacy authority sources verified on 2026-09-05:

- BC Laws: Security Services Act
- BC Laws: Security Services Regulation
- Government of British Columbia: security worker, security business, training, rules, licensing policies, and enforcement guidance
- BC Laws: Personal Information Protection Act and Freedom of Information and Protection of Privacy Act
- Office of the Information and Privacy Commissioner for British Columbia: private-sector video surveillance, public-sector surveillance, and employee privacy guidance
- BC Laws: Human Rights Code, Workers Compensation Act, Occupational Health and Safety Regulation, Trespass Act, Employment Standards Act, Body Armour Control Act, and Body Armour Control Regulation
- Government of British Columbia: body-armour possession guidance

Freshness: `HIGH`

Future outputs must recheck current official sources before relying on BC licensing, training, conduct, privacy, reporting, records, workplace, trespass, equipment, uniform, dog-use, body-armour, or security-operation claims.

# Critical Boundary

British Columbia sources can identify provincial issue areas, but they do not by themselves authorize private investigative or security work without current security worker licence status, security business licence status, role, purpose, authority, and qualified review.

Federal, municipal, site-specific, employer, client, contract, collective agreement, Indigenous governance, insurance, and sector requirements may still apply. Use AI-27 where federal privacy, criminal-law, evidence, human-rights, federally regulated workplace, or labour issues are present.

# Routing Boundary

Use AI-29 for:

- BC security worker licensing issue spotting;
- BC private investigator licence type issue spotting;
- BC security guard licence type issue spotting;
- BC security business licensing issue spotting;
- training, experience, and qualification research;
- professional conduct issue spotting;
- permitted authorities and restrictions research;
- privacy interaction research;
- reporting and recordkeeping issue spotting;
- security operations review questions;
- body-armour, equipment, uniform, dog-use, and site-authority issue spotting;
- provincial law issue spotting;
- escalation and qualified-review questions.

Route to `REGULATED_RESEARCH_ONLY` when authorization depends on BC security worker licence type, security business licence status, exemption, temporary licence, out-of-province private investigator exemption, incidental-work determination, training, experience, prescribed checks, licence conditions, professional conduct, uniforms, equipment, dogs, body armour, permitted authority, post orders, trespass authority, privacy, reporting, retention, employment, workplace safety, or security-operation rules.

Route to `INTRUSIVE_GATE_REQUIRED` when BC facts involve surveillance, monitoring, video surveillance, location tracking, biometric information, sensitive workplace allegations, employee monitoring, third-party incidental capture, high-impact background screening, covert observation, or persistent observation.

Route to `CERTIFICATION_ESCALATION` when the request asks for licensing, training, experience equivalency, privacy, human-rights, workplace safety, recordkeeping, security-operation, dog-use, body-armour, use-of-force, restraint, weapons, emergency-response, alarm, camera, access-control, or life-safety approval.

Route to `PROHIBITED_REDIRECT` for licensing bypass, licence impersonation, using another person's licence, training-record fabrication, hidden unlicensed work, hacking, credential theft, unauthorized account access, lock bypass, forced entry, access-control circumvention, covert tracker installation, illegal GPS tracking, stalking, intimate-partner monitoring, police or government impersonation, coercive interrogation, physical coercion, detention tactics, search tactics, pursuit tactics, trespass-removal tactics, dog-control tactics, body-armour bypass or permit evasion, camera evasion, alarm defeat, weapons use, restraint techniques, fabricated records, altered evidence, concealed source gaps, or destroying records to avoid review.

# Files Added

- `specializations/canada/british-columbia/*`
- `tests/regulatory/AI-29-british-columbia-specialization.json`
- `docs/development/handoffs/AI-29-final-handoff.md`

# Files Modified

- `README.md`
- `CHANGELOG.md`
- `scripts/validate-docs.py`
- `scripts/validate-specializations.py`

# Sources

- `ROADMAP.md`
- `docs/architecture/domain-contract.md`
- `docs/architecture/scope-boundaries.md`
- `docs/architecture/prohibited-capabilities.md`
- `docs/architecture/authority-routing.md`
- `docs/architecture/intrusive-task-gate.md`
- `docs/architecture/certification-boundaries.md`
- `docs/standards/regulatory-source-standard.md`
- `docs/standards/source-freshness-standard.md`
- `docs/development/handoffs/AI-28-final-handoff.md`
- Official BC and OIPC sources listed in `specializations/canada/british-columbia/source-log.yaml`

# Validation Performed

```powershell
python .\scripts\validate-specializations.py --repo-root D:\AgentInvestigate
python .\scripts\validate-docs.py --repo-root D:\AgentInvestigate
.\scripts\validate-all.ps1
git diff --check
```

# Tests

AI-29 adds `tests/regulatory/AI-29-british-columbia-specialization.json` with routing tests for:

- BC worker and business licensing;
- BC training, experience, licence conditions, and conduct;
- BC privacy, reporting, records, public-sector, private-sector, and surveillance interactions;
- BC security operations, post orders, equipment, uniforms, dogs, body armour, trespass, and restrictions;
- certification-boundary escalation;
- prohibited bypass and impersonation requests;
- BC/federal overlap with AI-27.

No live before/after model evaluation was run in AI-29.

# Safety / Regulatory Review

- AI-29 is issue-spotting and source-metadata infrastructure only.
- It does not create skills, skillsets, forms, licence applications, post orders, operational tactics, or compliance determinations.
- It does not provide legal conclusions, licensing approval, training certification, privacy compliance certification, human-rights compliance certification, investigative authorization, security authorization, employment-action approval, police authority, use-of-force qualification, weapons qualification, dog-handler approval, body-armour permit approval, or security-operation approval.
- It preserves the BC non-authority boundary and requires current official source verification for final regulated claims.

# Known Limitations

- AI-29 does not contain a full BC legal database.
- AI-29 does not resolve factual licence eligibility, licence conditions, exemption status, out-of-province investigator exemptions, conduct complaints, privacy compliance, employment decisions, dog-use authorization, body-armour permit status, or security-operation approval.
- AI-29 does not resolve federal/provincial overlap, statutory interpretation, regulator guidance conflicts, case-law application, Indigenous governance questions, or municipal by-law issues.

# Explicitly Not Completed

- No AI-30 Alberta investigation and security module.
- No other provincial or territorial modules.
- No municipal by-law specialization.
- No skillsets.
- No live before/after evaluation reports.

# Recommended Next Wave

AI-30: Alberta Investigation & Security Module.
