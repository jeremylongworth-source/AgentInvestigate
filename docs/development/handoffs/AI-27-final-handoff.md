# Wave

AI-27

# Objective

Create the first jurisdiction specialization: the Canada Federal Regulatory Foundation at `specializations/canada/federal/`.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_27_CANADA_FEDERAL_READY
```

# Scope Completed

- Created the Canada federal specialization module at `specializations/canada/federal/`.
- Added HIGH-freshness source metadata in `source-log.yaml`.
- Added federal privacy and information-handling reference coverage.
- Added federal Criminal Code interaction and prohibited-conduct routing coverage.
- Added Canada Evidence Act issue-spotting and evidence/records boundaries.
- Added federal human-rights and federally regulated organization issue spotting.
- Added routing boundaries that preserve the rule that federal sources alone do not authorize private investigative or security work.
- Added AI-27 regulatory fixture coverage.
- Added `scripts/validate-specializations.py` and wired it into `scripts/validate-all.ps1`.
- Updated README, changelog, and docs validation for AI-27.

# Module Files

- `specializations/canada/federal/README.md`
- `specializations/canada/federal/source-log.yaml`
- `specializations/canada/federal/privacy-and-information-handling.md`
- `specializations/canada/federal/criminal-law-interaction.md`
- `specializations/canada/federal/evidence-and-records.md`
- `specializations/canada/federal/human-rights-and-federal-organizations.md`
- `specializations/canada/federal/routing-boundaries.md`

# Research Areas Covered

- federal privacy
- criminal-law interaction
- evidence-related federal concepts
- federal human-rights considerations
- information handling
- federally regulated organizations
- federal criminal prohibitions relevant to investigative/security work

# Source Basis

AI-27 used official Canadian sources verified on 2026-09-05:

- Justice Laws Website: Personal Information Protection and Electronic Documents Act
- Justice Laws Website: Privacy Act
- Office of the Privacy Commissioner of Canada: PIPEDA private-sector privacy guidance
- Justice Laws Website: Criminal Code
- Justice Laws Website: Canada Evidence Act
- Justice Laws Website: Canadian Human Rights Act
- Canadian Human Rights Commission
- Government of Canada: federally regulated industries and workplaces
- Justice Laws Website: Canada Labour Code

Freshness: `HIGH`

Future outputs must recheck current official sources before relying on federal legal, privacy, human-rights, labour, evidence, or criminal-law claims.

# Critical Boundary

Federal rules alone do not determine whether private investigative or security work is authorized.

Occupational licensing is often provincial or territorial. AI-27 can identify federal issue areas, but it does not answer whether a private investigator, security guard, security agency, employer, loss-prevention team, or corporate security program is authorized to perform work in a province or territory.

# Routing Boundary

Use AI-27 for:

- federal privacy issue spotting;
- criminal-law interaction issue spotting;
- evidence-related federal concept spotting;
- federal human-rights issue spotting;
- information-handling checklists;
- federally regulated organization issue spotting;
- escalation and qualified-review questions.

Route to `REGULATED_RESEARCH_ONLY` when authorization depends on:

- provincial or territorial private investigator licensing;
- provincial or territorial security guard licensing;
- agency licensing;
- guard licensing;
- training;
- uniforms;
- permitted authorities;
- use-of-force limits;
- post orders;
- reporting;
- province-specific privacy, employment, security, or operational law.

Route to `PROHIBITED_REDIRECT` for hacking, credential theft, unauthorized account access, lock bypass, forced entry, access-control circumvention, covert tracker installation, illegal GPS tracking, stalking, intimate-partner monitoring, police or government impersonation, coercive interrogation, physical coercion, detention tactics, search tactics, pursuit tactics, camera evasion, alarm defeat, weapons use, restraint techniques, fabricated records, altered evidence, or concealed source gaps.

# Files Added

- `specializations/canada/federal/*`
- `tests/regulatory/AI-27-canada-federal-specialization.json`
- `scripts/validate-specializations.py`
- `docs/development/handoffs/AI-27-final-handoff.md`

# Files Modified

- `README.md`
- `CHANGELOG.md`
- `scripts/validate-all.ps1`
- `scripts/validate-docs.py`

# Sources

- `ROADMAP.md`
- `docs/architecture/domain-contract.md`
- `docs/architecture/scope-boundaries.md`
- `docs/architecture/prohibited-capabilities.md`
- `docs/architecture/authority-routing.md`
- `docs/architecture/intrusive-task-gate.md`
- `docs/standards/regulatory-source-standard.md`
- `docs/standards/source-freshness-standard.md`
- `docs/development/handoffs/AI-26-final-handoff.md`
- Official Canadian sources listed in `specializations/canada/federal/source-log.yaml`

# Validation Performed

```powershell
python .\scripts\validate-specializations.py --repo-root D:\AgentInvestigate
python .\scripts\validate-docs.py --repo-root D:\AgentInvestigate
.\scripts\validate-all.ps1
git diff --check
```

# Tests

AI-27 adds `tests/regulatory/AI-27-canada-federal-specialization.json` with routing tests for:

- federal privacy and information handling;
- federal criminal prohibitions and prohibited redirects;
- evidence-related federal concepts, federal human-rights considerations, and federally regulated organization issue spotting.

No live before/after model evaluation was run in AI-27.

# Safety / Regulatory Review

- AI-27 is issue-spotting and source-metadata infrastructure only.
- It does not create skills, skillsets, provincial modules, or operational legal rules.
- It does not provide legal conclusions, licensing approval, privacy compliance certification, human-rights compliance certification, evidence admissibility conclusions, criminal guilt conclusions, investigative authorization, security authorization, employment-action approval, law-enforcement referral approval, or operational enforcement instructions.
- It preserves the non-authority boundary for federal law and requires provincial or territorial review where occupational licensing, private security authority, private investigation authority, training, conduct, privacy, employment, or operational requirements may apply.

# Known Limitations

- AI-27 does not contain a full Canadian legal database.
- AI-27 does not encode province-specific occupational licensing rules.
- AI-27 does not resolve federal/provincial overlap, statutory interpretation, regulator guidance conflicts, or case-law application.
- AI-27 does not provide final legal, privacy, human-rights, employment, evidence, criminal-law, licensing, compliance, or security-operation conclusions.

# Explicitly Not Completed

- No AI-28 Ontario investigation and security module.
- No British Columbia or Alberta modules.
- No skillsets.
- No specializations beyond Canada federal.
- No live before/after evaluation reports.

# Recommended Next Wave

AI-28: Ontario Investigation & Security Module.
