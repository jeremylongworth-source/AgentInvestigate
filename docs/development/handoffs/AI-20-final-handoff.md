# Wave

AI-20

# Objective

Build Family 13, Background Screening & Due Diligence, with a required distinction between PERSON SCREENING and ENTITY DUE DILIGENCE.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_20_SCREENING_DUE_DILIGENCE_READY
```

# Scope Completed

- Created all 10 `13-background-screening-due-diligence` skills from the canonical taxonomy.
- Added OpenAI adapter metadata for each background-screening and due-diligence skill.
- Added one scoped reference file for each Family 13 skill.
- Added AI-20 screening and due-diligence scenario fixtures with positive and negative-routing coverage for each skill.
- Added required split coverage for PERSON SCREENING and ENTITY DUE DILIGENCE.
- Added integration coverage for consent, relevance, public records, conflicting identities, adverse information, unresolved records, and bias risk.
- Added validator checks for Family 13 completion, split coverage, integration requirements, and the stronger personal-screening privacy and authority gate.

# Family 13 Skills

- `define-screening-purpose`
- `assess-background-screening-authority`
- `verify-screening-consent`
- `select-screening-source-type`
- `assess-screening-source-reliability`
- `evaluate-record-relevance`
- `identify-screening-identity-ambiguity`
- `resolve-screening-discrepancy`
- `prepare-due-diligence-summary`
- `identify-adverse-information-review-need`

# Required Split

- PERSON SCREENING
- ENTITY DUE DILIGENCE

PERSON SCREENING requires stronger privacy and authority controls than ENTITY DUE DILIGENCE.

# Integration Requirements

- consent
- relevance
- public records
- conflicting identities
- adverse information
- unresolved records
- bias risk

# Boundary

The AI does not decide:

- employment eligibility
- tenant eligibility
- creditworthiness
- criminal guilt
- legal liability
- adverse action
- final suitability

# Files Added

- `skills/13-background-screening-due-diligence/*`
- `tests/reference-skills/AI-20-screening-due-diligence-scenarios.json`
- `docs/development/handoffs/AI-20-final-handoff.md`
- `scripts/generate-ai20-skill-packages.py`

# Files Modified

- `README.md`
- `CHANGELOG.md`
- `scripts/validate-docs.py`
- `scripts/validate-skills.py`

# Sources

- `ROADMAP.md`
- `docs/architecture/taxonomy-index.yaml`
- `docs/architecture/sensitivity-model.md`
- `docs/architecture/authority-routing.md`
- `docs/architecture/intrusive-task-gate.md`
- `docs/architecture/prohibited-capabilities.md`
- `docs/standards/skill-authoring-standard.md`
- `docs/standards/skill-naming-standard.md`
- `docs/standards/output-contract-standard.md`
- `docs/standards/research-and-evidence-standard.md`
- `docs/standards/testing-standard.md`
- `docs/foundations/professional-vocabulary.md`
- `docs/foundations/shared-schemas.md`
- `docs/development/handoffs/AI-19-final-handoff.md`

# Validation Performed

```powershell
.\scripts\validate-all.ps1
python .\scripts\validate-skills.py --repo-root D:\AgentInvestigate
Get-ChildItem -LiteralPath 'D:\AgentInvestigate\skills\13-background-screening-due-diligence' -Directory | ForEach-Object { python 'C:\Users\jerem\.codex\skills\.system\skill-creator\scripts\quick_validate.py' $_.FullName }
git diff --check
```

# Tests

AI-20 adds scenario fixtures for all 10 background-screening and due-diligence skills. Each skill has positive routing coverage and negative-routing coverage for prohibited screening outcomes, consent bypass, identity overclaiming, and adverse-action decisioning.

The split scenarios cover PERSON SCREENING and ENTITY DUE DILIGENCE separately, with the stronger personal-screening privacy and authority control gate.

No live before/after model evaluation was run in AI-20.

# Safety / Regulatory Review

- Family 13 supports purpose definition, authority assessment, consent verification, source selection, source reliability, record relevance, identity ambiguity, discrepancy resolution, due-diligence summaries, and adverse-information review needs only.
- Skills route screening and due-diligence work through jurisdiction, authority, consent, privacy, source, relevance, and human-review gates.
- Skills preserve conflicting identities, adverse information, unresolved records, public-record limits, and bias risk.
- Skills refuse or reroute invented consent, consent bypass, unauthorized protected-record access, private-account compromise, credential acquisition, suppressed identity conflicts, hidden unresolved records, and adverse-action decision requests.
- Skills do not decide employment eligibility, tenant eligibility, creditworthiness, adverse action, legal compliance, privacy compliance, criminal guilt, legal liability, or final suitability.

# Known Limitations

- AI-20 does not run background checks, order consumer reports, access external databases, verify live public records, or provide legal screening compliance decisions.
- AI-20 does not add jurisdiction-specific consumer-reporting, employment, tenant, credit, privacy, or adverse-action law databases.
- Screening and due-diligence outputs remain draft support requiring responsible human review before consequential use.

# Explicitly Not Completed

- No AI-21 security operations, access, or patrol skills.
- No skillsets.
- No specializations.
- No jurisdiction-specific screening law database.
- No live before/after evaluation reports.

# Recommended Next Wave

AI-21: Security Operations, Access & Patrol.
