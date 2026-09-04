# Wave

AI-01

# Objective

Freeze the professional boundaries of AgentInvestigate.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_01_DOMAIN_CONTRACT_READY
```

# Scope Completed

- Defined private investigation as an authorized fact-finding and evidence-support branch.
- Defined private security as an authorized protection, observation, access, patrol, incident, loss-prevention, and security-risk branch.
- Defined shared professional core material.
- Defined overlap rules.
- Defined professional role boundaries.
- Defined decision-support limits.
- Defined regulated activity boundaries.
- Defined specialist boundaries.
- Defined prohibited-capability boundaries.
- Mapped every roadmap taxonomy family to the domain contract.

# Files Added

- `docs/architecture/domain-contract.md`
- `docs/architecture/scope-boundaries.md`
- `docs/architecture/prohibited-capabilities.md`
- `docs/development/handoffs/AI-01-final-handoff.md`

# Files Modified

- `README.md`
- `CHANGELOG.md`
- `scripts/validate-docs.py`

# Research Performed

AI-01 used a limited current-source scan to verify that the domain contract should avoid universal legal or licensing claims. The scan focused on professional boundary examples, licensing-regulator examples, background-screening obligations, and security/investigation standards.

# Sources

- AgentInvestigate `ROADMAP.md`
- Ontario security guard/private investigator licence guidance: https://www.ontario.ca/page/security-guard-or-private-investigator-licence-individuals
- Ontario Private Security and Investigative Services Act, 2005: https://www.ontario.ca/laws/statute/05p34
- British Columbia Security Services Act: https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/07030_01
- British Columbia security industry licensing guidance: https://www2.gov.bc.ca/gov/content/employment-business/business/security-services/security-industry-licensing
- British Columbia rules for licensed security businesses: https://www2.gov.bc.ca/gov/content/employment-business/business/security-services/security-industry-licensing/businesses/rules
- California Bureau of Security and Investigative Services: https://www.bsis.ca.gov/
- California private investigator license factsheet: https://www.bsis.ca.gov/forms_pubs/pi_fact.shtml
- FTC employer consumer-report guidance: https://www.ftc.gov/business-guidance/resources/using-consumer-reports-what-employers-need-know
- ASIS Investigations Standard overview: https://www.asisonline.org/security-news/standards-guidelines/investigations-standard/
- ASIS Security Risk Assessment Standard overview: https://www.asisonline.org/security-news/standards-guidelines/security-risk-assessment-standard/

# Validation Performed

```powershell
.\scripts\validate-all.ps1
git diff --check
```

# Tests

No behavioral skill tests exist yet because AI-01 creates architecture contracts only. Validation checks required files, required completion tokens, family mapping text, and absence of empty committed directories.

# Safety / Regulatory Review

- No regulated skill procedures were authored.
- No intrusive operational workflow was implemented.
- Jurisdiction-specific rules were not encoded as universal rules.
- Prohibited capabilities were made explicit in a dedicated architecture document.
- The domain contract preserves authority, jurisdiction, privacy, evidence, source, and human-review boundaries.

# Known Limitations

- AI-01 maps taxonomy families from the roadmap because the canonical in-repository master taxonomy is not yet present.
- Source research was enough to establish boundary posture, not enough to author jurisdiction modules.
- AI-03 must still formalize routing for sensitivity, authority, intrusive work, and certification boundaries.
- AI-05 must still define source hierarchy, source metadata, and freshness rules.

# Unresolved Issues

- The full approved `AgentInvestigate Master Taxonomy v1.0` must be recovered or reconstructed with provenance in AI-02.

# Explicitly Not Completed

- No AI-02 taxonomy files.
- No AI-03 routing model.
- No skills.
- No skillsets.
- No specializations.
- No shared templates or schemas.
- No regulatory source maps.
- No evaluation fixtures.

# Recommended Next Wave

AI-02: Master Taxonomy Integration.
