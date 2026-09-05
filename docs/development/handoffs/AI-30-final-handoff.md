# Wave

AI-30

# Objective

Create the Alberta Investigation & Security Module at `specializations/canada/alberta/`.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_30_ALBERTA_READY
```

# Scope Completed

- Created the independently verified Alberta provincial specialization module at `specializations/canada/alberta/`.
- Added HIGH-freshness source metadata in `source-log.yaml`.
- Added Alberta investigator, security service worker, security business, registry, training licence, dual licence, eligibility, and records-check issue spotting.
- Added Alberta training, provincial examination, approved-provider, baton training, licence-condition, and professional conduct boundaries.
- Added Alberta permitted-authority, restriction, uniform, equipment, baton, patrol-dog, body-armour, locksmith-adjacent, post-order, and security-operation boundaries.
- Added Alberta privacy, access, reporting, complaint, licence-update, recordkeeping, employee monitoring, private-sector, public-sector, health-information, and surveillance-currentness coverage.
- Added Alberta provincial law map for SSIA, SSIA regulations, PIPA, PIPA Regulation, POPA, ATIA, HIA, Alberta Human Rights Act, OHS Act, Employment Standards Code, Trespass to Premises Act, Petty Trespass Act, Body Armour Control Act, and Body Armour Control Regulation sources.
- Added routing boundaries preserving non-authority, intrusive-task, certification, and prohibited-output gates.
- Added AI-30 regulatory fixture coverage.
- Extended specialization and documentation validation for AI-30.
- Updated README and changelog.

# Module Files

- `specializations/canada/alberta/README.md`
- `specializations/canada/alberta/source-log.yaml`
- `specializations/canada/alberta/licensing-and-registration.md`
- `specializations/canada/alberta/training-examination-and-conduct.md`
- `specializations/canada/alberta/authority-restrictions-and-security-operations.md`
- `specializations/canada/alberta/privacy-reporting-and-records.md`
- `specializations/canada/alberta/provincial-laws-map.md`
- `specializations/canada/alberta/routing-boundaries.md`

# Research Areas Covered

- investigator licensing
- security service worker licensing
- security business licensing
- training
- provincial examinations
- professional conduct
- permitted authorities
- restrictions
- privacy interaction
- reporting
- security operations
- body armour
- provincial laws materially relevant to scoped skills

# Source Basis

AI-30 used official Alberta and Alberta privacy authority sources verified on 2026-09-05:

- Open Government Alberta: Security Services and Investigators Act, Security Services and Investigators Regulation, and Security Services and Investigators (Ministerial) Regulation
- Government of Alberta: security licences and permits, security service worker licence, investigator licence, participating registries, business resources, and body armour permit guidance
- Open Government Alberta: Security Programs policy manual, approved training courses, provincial examination process, code-of-conduct guidance, and training-course licensing guidance
- Open Government Alberta and Alberta.ca: PIPA, PIPA Regulation, POPA, ATIA, HIA, and privacy/access guidance
- Office of the Information and Privacy Commissioner of Alberta: video surveillance, privacy laws overview, and privacy impact assessment guidance
- Open Government Alberta and Alberta.ca: Alberta Human Rights Act, Alberta Human Rights Commission, OHS Act, OHS Act/regulation/code guidance, Employment Standards Code, employment standards guidance, Trespass to Premises Act, Petty Trespass Act, Body Armour Control Act, and Body Armour Control Regulation

Freshness: `HIGH`

Future outputs must recheck current official sources before relying on Alberta licensing, training, examinations, conduct, privacy, access, reporting, records, workplace, trespass, equipment, uniform, baton, patrol-dog, body-armour, locksmith-adjacent, or security-operation claims.

# Critical Boundary

Alberta sources can identify provincial issue areas, but they do not by themselves authorize private investigative or security work without current individual licence status, business licence status, role, purpose, authority, and qualified review.

Federal, municipal, site-specific, employer, client, contract, collective agreement, Indigenous governance, insurance, and sector requirements may still apply. Use AI-27 where federal privacy, criminal-law, evidence, human-rights, federally regulated workplace, or labour issues are present.

# Routing Boundary

Use AI-30 for:

- Alberta investigator licensing issue spotting;
- Alberta security service worker licensing issue spotting;
- Alberta security business licensing issue spotting;
- training, approved-provider, and provincial examination research;
- professional conduct issue spotting;
- permitted authorities and restrictions research;
- privacy interaction research;
- public-sector access issue spotting;
- reporting and recordkeeping issue spotting;
- security operations review questions;
- body-armour, baton, patrol-dog, equipment, uniform, locksmith-adjacent, and site-authority issue spotting;
- provincial law issue spotting;
- escalation and qualified-review questions.

Route to `REGULATED_RESEARCH_ONLY` when authorization depends on Alberta individual licence type, business licence status, dual licence, training licence, registry temporary licence, exemption, approved training, provincial examination result, examination challenge, equivalent training, prior-experience recognition, records checks, licence conditions, professional conduct, uniforms, equipment, baton training, patrol dogs, body armour, permitted authority, post orders, trespass authority, privacy, public-sector access, reporting, retention, employment, workplace safety, or security-operation rules.

Route to `INTRUSIVE_GATE_REQUIRED` when Alberta facts involve surveillance, monitoring, video surveillance, location tracking, biometric information, health information, sensitive workplace allegations, employee monitoring, third-party incidental capture, high-impact background screening, covert observation, or persistent observation.

Route to `CERTIFICATION_ESCALATION` when the request asks for licensing, training, approved provider, provincial examination, experience equivalency, privacy, human-rights, workplace safety, recordkeeping, security-operation, baton, patrol-dog, body-armour, locksmith, automotive lock bypass, use-of-force, restraint, weapons, emergency-response, alarm, camera, access-control, or life-safety approval.

Route to `PROHIBITED_REDIRECT` for licensing bypass, licence impersonation, using another person's licence, training-record fabrication, provincial examination cheating, hidden unlicensed work, hacking, credential theft, unauthorized account access, lock bypass, automotive lock bypass, restricted locksmith tool misuse, forced entry, access-control circumvention, covert tracker installation, illegal GPS tracking, stalking, intimate-partner monitoring, police or government impersonation, coercive interrogation, physical coercion, detention tactics, search tactics, pursuit tactics, trespass-removal tactics, patrol-dog control tactics, baton tactics, body-armour bypass or permit evasion, camera evasion, alarm defeat, weapons use, restraint techniques, fabricated records, altered evidence, concealed source gaps, or destroying records to avoid review.

# Files Added

- `specializations/canada/alberta/*`
- `tests/regulatory/AI-30-alberta-specialization.json`
- `docs/development/handoffs/AI-30-final-handoff.md`

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
- `docs/development/handoffs/AI-29-final-handoff.md`
- Official Alberta and OIPC sources listed in `specializations/canada/alberta/source-log.yaml`

# Validation Performed

```powershell
python .\scripts\validate-specializations.py --repo-root D:\AgentInvestigate
python .\scripts\validate-docs.py --repo-root D:\AgentInvestigate
.\scripts\validate-all.ps1
git diff --check
```

# Tests

AI-30 adds `tests/regulatory/AI-30-alberta-specialization.json` with routing tests for:

- Alberta individual and business licensing;
- Alberta training, provincial examinations, licence conditions, baton training, and conduct;
- Alberta privacy, access, reporting, records, private-sector, public-sector, health-information, and surveillance interactions;
- Alberta security operations, post orders, equipment, uniforms, baton, patrol dogs, body armour, trespass, and restrictions;
- certification-boundary escalation;
- prohibited bypass and impersonation requests;
- Alberta/federal overlap with AI-27.

No live before/after model evaluation was run in AI-30.

# Safety / Regulatory Review

- AI-30 is issue-spotting and source-metadata infrastructure only.
- It does not create skills, skillsets, forms, licence applications, post orders, operational tactics, or compliance determinations.
- It does not provide legal conclusions, licensing approval, training certification, provincial examination approval, privacy compliance certification, human-rights compliance certification, investigative authorization, security authorization, employment-action approval, police authority, baton qualification, use-of-force qualification, weapons qualification, patrol-dog-handler approval, body-armour permit approval, locksmith approval, automotive lock bypass approval, or security-operation approval.
- It preserves the Alberta non-authority boundary and requires current official source verification for final regulated claims.

# Known Limitations

- AI-30 does not contain a full Alberta legal database.
- AI-30 does not resolve factual licence eligibility, licence conditions, exemption status, registry temporary licence criteria, training equivalency, provincial examination challenges, conduct complaints, privacy compliance, employment decisions, baton qualification, patrol-dog authorization, body-armour permit status, locksmith status, automotive lock bypass status, or security-operation approval.
- AI-30 does not resolve federal/provincial overlap, statutory interpretation, regulator guidance conflicts, case-law application, Indigenous governance questions, or municipal by-law issues.
- Alberta public-sector privacy and access law recently transitioned to POPA and ATIA on 2025-06-11, so Alberta privacy/access outputs require immediate current-source verification.

# Explicitly Not Completed

- No AI-31 Canadian Jurisdiction Expansion Framework.
- No additional provincial or territorial modules beyond Ontario, British Columbia, and Alberta.
- No municipal by-law specialization.
- No skillsets.
- No live before/after evaluation reports.

# Recommended Next Wave

AI-31: Canadian Jurisdiction Expansion Framework.
