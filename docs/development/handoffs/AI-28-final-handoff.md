# Wave

AI-28

# Objective

Create the Ontario Investigation & Security Module at `specializations/canada/ontario/`.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_28_ONTARIO_READY
```

# Scope Completed

- Created the first provincial specialization module at `specializations/canada/ontario/`.
- Added HIGH-freshness source metadata in `source-log.yaml`.
- Added Ontario investigator licensing, security licensing, dual-licence, agency/corporation licensing, eligibility, and exemption issue spotting.
- Added Ontario training, testing, and professional conduct boundaries.
- Added Ontario permitted-authority, restriction, equipment, uniform, post-order, and security-operation boundaries.
- Added Ontario privacy, reporting, complaint, Registrar-notification, recordkeeping, and surveillance-currentness coverage.
- Added Ontario provincial law map for PSISA, privacy, human rights, workplace safety, trespass, employment standards, and accessibility sources.
- Added routing boundaries preserving non-authority, intrusive-task, certification, and prohibited-output gates.
- Added AI-28 regulatory fixture coverage.
- Extended specialization and documentation validation for AI-28.
- Updated README and changelog.

# Module Files

- `specializations/canada/ontario/README.md`
- `specializations/canada/ontario/source-log.yaml`
- `specializations/canada/ontario/licensing-and-registration.md`
- `specializations/canada/ontario/training-testing-and-conduct.md`
- `specializations/canada/ontario/authority-restrictions-and-security-operations.md`
- `specializations/canada/ontario/privacy-reporting-and-records.md`
- `specializations/canada/ontario/provincial-laws-map.md`
- `specializations/canada/ontario/routing-boundaries.md`

# Research Areas Covered

- investigator licensing
- security licensing
- training
- professional conduct
- permitted authorities
- restrictions
- privacy interaction
- reporting
- security operations
- provincial laws materially relevant to scoped skills

# Source Basis

AI-28 used official Ontario and Ontario privacy authority sources verified on 2026-09-05:

- Ontario e-Laws: Private Security and Investigative Services Act, 2005
- Government of Ontario: individual, agency, training, testing, and requirement guidance
- Ontario e-Laws: PSISA regulations for training/testing, code of conduct, recordkeeping, Registrar information, uniforms, equipment, clean criminal record, and exemptions
- Ontario e-Laws: FIPPA, MFIPPA, PHIPA, Human Rights Code, OHSA, Trespass to Property Act, Employment Standards Act, and AODA
- Information and Privacy Commissioner of Ontario: video surveillance guidance

Freshness: `HIGH`

Future outputs must recheck current official sources before relying on Ontario licensing, training, conduct, privacy, reporting, records, workplace, accessibility, trespass, or security-operation claims.

# Critical Boundary

Ontario sources can identify provincial issue areas, but they do not by themselves authorize private investigative or security work without current licensing, authority, role, purpose, and qualified review.

Federal, municipal, site-specific, employer, client, contract, collective agreement, insurance, and sector requirements may still apply. Use AI-27 where federal privacy, criminal-law, evidence, human-rights, federally regulated workplace, or labour issues are present.

# Routing Boundary

Use AI-28 for:

- Ontario investigator licensing issue spotting;
- Ontario security licensing issue spotting;
- training and testing research;
- professional conduct issue spotting;
- permitted authorities and restrictions research;
- privacy interaction research;
- reporting and recordkeeping issue spotting;
- security operations review questions;
- provincial law issue spotting;
- escalation and qualified-review questions.

Route to `REGULATED_RESEARCH_ONLY` when authorization depends on Ontario licence type, licence status, agency/corporation licence, exemption, training, testing, conduct, uniforms, equipment, permitted authority, post orders, trespass authority, privacy, reporting, retention, employment, workplace safety, accessibility, or security-operation rules.

Route to `INTRUSIVE_GATE_REQUIRED` when Ontario facts involve surveillance, monitoring, video surveillance, location tracking, biometric information, personal health information, sensitive workplace allegations, third-party incidental capture, high-impact background screening, covert observation, or persistent observation.

Route to `CERTIFICATION_ESCALATION` when the request asks for licensing, training, privacy, human-rights, workplace safety, accessibility, recordkeeping, security-operation, use-of-force, restraint, weapons, emergency-response, alarm, camera, access-control, or life-safety approval.

Route to `PROHIBITED_REDIRECT` for licensing bypass, licence impersonation, training-record fabrication, hidden unlicensed work, hacking, credential theft, unauthorized account access, lock bypass, forced entry, access-control circumvention, covert tracker installation, illegal GPS tracking, stalking, intimate-partner monitoring, police or government impersonation, coercive interrogation, physical coercion, detention tactics, search tactics, pursuit tactics, trespass-removal tactics, camera evasion, alarm defeat, weapons use, restraint techniques, fabricated records, altered evidence, concealed source gaps, or destroying records to avoid review.

# Files Added

- `specializations/canada/ontario/*`
- `tests/regulatory/AI-28-ontario-specialization.json`
- `docs/development/handoffs/AI-28-final-handoff.md`

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
- `docs/development/handoffs/AI-27-final-handoff.md`
- Official Ontario and IPC sources listed in `specializations/canada/ontario/source-log.yaml`

# Validation Performed

```powershell
python .\scripts\validate-specializations.py --repo-root D:\AgentInvestigate
python .\scripts\validate-docs.py --repo-root D:\AgentInvestigate
.\scripts\validate-all.ps1
git diff --check
```

# Tests

AI-28 adds `tests/regulatory/AI-28-ontario-specialization.json` with routing tests for:

- Ontario licensing, training, and conduct;
- Ontario privacy, reporting, records, and video surveillance;
- Ontario security operations, post orders, equipment, uniforms, trespass, and restrictions;
- certification-boundary escalation;
- prohibited bypass and impersonation requests;
- Ontario/federal overlap with AI-27.

No live before/after model evaluation was run in AI-28.

# Safety / Regulatory Review

- AI-28 is issue-spotting and source-metadata infrastructure only.
- It does not create skills, skillsets, forms, licence applications, post orders, operational tactics, or compliance determinations.
- It does not provide legal conclusions, licensing approval, training certification, privacy compliance certification, human-rights compliance certification, investigative authorization, security authorization, employment-action approval, police authority, use-of-force qualification, weapons qualification, or security-operation approval.
- It preserves the Ontario non-authority boundary and requires current official source verification for final regulated claims.

# Known Limitations

- AI-28 does not contain a full Ontario legal database.
- AI-28 does not resolve factual licence eligibility, exemption status, conduct complaints, privacy compliance, employment decisions, or security-operation approval.
- AI-28 does not resolve federal/provincial overlap, statutory interpretation, regulator guidance conflicts, or case-law application.
- IPC video surveillance guidance was under review on 2026-09-05 due to Bill 97 FIPPA/MFIPPA amendments with further dates on 2026-09-15 and 2027-01-01, so surveillance/privacy outputs require immediate recheck.

# Explicitly Not Completed

- No AI-29 British Columbia investigation and security module.
- No Alberta or other provincial modules.
- No municipal by-law specialization.
- No skillsets.
- No live before/after evaluation reports.

# Recommended Next Wave

AI-29: British Columbia Investigation & Security Module.
