# Wave

AI-31

# Objective

Define how additional provinces and territories are added without rewriting core architecture.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_31_CANADA_EXPANSION_FRAMEWORK_READY
```

# Scope Completed

- Added the Canadian jurisdiction expansion contract at `docs/architecture/canadian-jurisdiction-roadmap.md`.
- Canonicalized candidate jurisdiction slugs for Quebec, Manitoba, Saskatchewan, Nova Scotia, New Brunswick, Newfoundland and Labrador, Prince Edward Island, Northwest Territories, Nunavut, and Yukon.
- Defined the future Canadian module path contract: `specializations/canada/<jurisdiction-slug>/`.
- Defined the eight baseline files required for future provincial and territorial modules.
- Defined HIGH-freshness source metadata expectations for future Canadian jurisdiction modules.
- Defined required coverage for investigator licensing, security worker or guard licensing, security business or agency licensing, training, examinations, professional conduct, authorities, restrictions, privacy, reporting, security operations, local laws, and federal overlap.
- Preserved the global routing vocabulary: `PROCEED_ROUTINE`, `CLARIFY_SCOPE`, `REGULATED_RESEARCH_ONLY`, `INTRUSIVE_GATE_REQUIRED`, `CERTIFICATION_ESCALATION`, and `PROHIBITED_REDIRECT`.
- Added the federal overlap contract requiring AI-27 checks where federal privacy, criminal-law, evidence, human-rights, federally regulated workplace, or labour issues may apply.
- Added AI-31 regulatory framework fixture coverage.
- Extended specialization and documentation validation for AI-31.
- Updated README and changelog.

# Artifact Added

- `docs/architecture/canadian-jurisdiction-roadmap.md`

# Fixture Added

- `tests/regulatory/AI-31-canadian-jurisdiction-framework.json`

# Framework Decisions

Decision:

```text
Add each Canadian province or territory as a standalone specialization module.
```

Decision:

```text
Keep Canadian jurisdiction modules source-backed and HIGH freshness by default.
```

Decision:

```text
Use one global routing vocabulary across all Canadian modules.
```

# Candidate Jurisdictions

```text
quebec
manitoba
saskatchewan
nova-scotia
new-brunswick
newfoundland-and-labrador
prince-edward-island
northwest-territories
nunavut
yukon
```

# Baseline Module Files

Future full modules must include:

- `README.md`
- `source-log.yaml`
- `licensing-and-registration.md`
- `training-examination-and-conduct.md`
- `authority-restrictions-and-security-operations.md`
- `privacy-reporting-and-records.md`
- `provincial-laws-map.md`
- `routing-boundaries.md`

# Required Coverage

Future modules must independently verify and document:

- investigator licensing
- security worker or security guard licensing
- security business or agency licensing
- training
- examinations, tests, or competency requirements
- professional conduct
- permitted authorities
- restrictions
- privacy interaction
- reporting
- security operations
- provincial or territorial laws materially relevant to scoped skills
- federal overlap through AI-27

# Routing Boundary

Future Canadian jurisdiction modules must inherit existing AgentInvestigate routing states. They must not create jurisdiction-specific routing states.

Use `REGULATED_RESEARCH_ONLY` when authorization depends on licensing, registration, privacy, employment, records, public-sector access, private security authority, investigative authority, body armour, equipment, uniform, business licence, training, examination, source currentness, or similar regulated facts.

Use `INTRUSIVE_GATE_REQUIRED` when facts involve surveillance, monitoring, location, biometrics, health information, high-impact screening, sensitive workplace allegations, covert observation, persistent observation, or third-party incidental capture.

Use `CERTIFICATION_ESCALATION` when the user asks AgentInvestigate to certify, approve, sign off, guarantee, or substitute for a regulator, counsel, trainer, licensed professional, privacy officer, HR, insurer, engineer, fire/life-safety professional, or emergency authority.

Use `PROHIBITED_REDIRECT` when the request asks for bypass, evasion, impersonation, unauthorized access, lock bypass, forced entry, unlawful tracking, stalking, coercive questioning, physical intervention tactics, detention tactics, search tactics, use-of-force instruction, weapon instruction, patrol-dog tactics, evidence alteration, fabricated records, or concealment.

# Validation Performed

```powershell
python -m py_compile scripts\validate-specializations.py scripts\validate-docs.py
python scripts\validate-specializations.py --repo-root D:\AgentInvestigate
python scripts\validate-docs.py --repo-root D:\AgentInvestigate
.\scripts\validate-all.ps1
git diff --check
```

# Safety / Regulatory Review

- AI-31 creates an extension framework only.
- AI-31 does not create Quebec, Manitoba, Saskatchewan, Nova Scotia, New Brunswick, Newfoundland and Labrador, Prince Edward Island, Northwest Territories, Nunavut, or Yukon modules.
- AI-31 does not claim source verification for any future jurisdiction module.
- AI-31 does not resolve factual licence eligibility, training requirements, privacy compliance, security authority, investigative authority, exemptions, professional conduct, or operational permission in future jurisdictions.
- Future jurisdiction modules must independently verify official sources before making local regulated claims.

# Known Limitations

- The framework does not decide which candidate jurisdiction is next.
- The framework does not solve bilingual review requirements for Quebec.
- The framework does not add municipal by-law modules.
- The framework does not add a structured `jurisdiction-profile.json`; it leaves that as a future stabilization option.

# Explicitly Not Completed

- No AI-32 Professional Skillset Composition.
- No additional provincial or territorial modules beyond Ontario, British Columbia, and Alberta.
- No full Canadian coverage claim.
- No live before/after model evaluation report.

# Recommended Next Wave

AI-32: Professional Skillset Composition.
