# Wave

AI-03

# Objective

Implement the architectural feature that distinguishes AgentInvestigate from ordinary knowledge repositories: sensitivity, authority, intrusive-work, certification-boundary, and prohibited-activity routing.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_03_SENSITIVITY_ROUTING_READY
```

# Scope Completed

- Defined the four sensitivity classes:
  - `ROUTINE`
  - `REGULATED`
  - `INTRUSIVE`
  - `CERTIFICATION_BOUNDARY`
- Defined classification precedence and reclassification triggers.
- Defined routing states:
  - `PROCEED_ROUTINE`
  - `CLARIFY_SCOPE`
  - `REGULATED_RESEARCH_ONLY`
  - `INTRUSIVE_GATE_REQUIRED`
  - `CERTIFICATION_ESCALATION`
  - `PROHIBITED_REDIRECT`
- Defined routing rules for:
  - jurisdiction;
  - licensing;
  - lawful purpose;
  - privacy;
  - information collection;
  - human approval;
  - prohibited activity;
  - escalation.
- Defined the intrusive-task gate and fail-closed conditions.
- Defined certification-boundary allowed support and prohibited substitutes.
- Added representative paper routing scenarios for all four sensitivity classes.
- Added validation for AI-03 routing artifacts.

# Files Added

- `docs/architecture/sensitivity-model.md`
- `docs/architecture/authority-routing.md`
- `docs/architecture/intrusive-task-gate.md`
- `docs/architecture/certification-boundaries.md`
- `docs/development/handoffs/AI-03-final-handoff.md`
- `scripts/validate-routing.py`

# Files Modified

- `README.md`
- `CHANGELOG.md`
- `scripts/validate-all.ps1`
- `scripts/validate-docs.py`

# Research Performed

AI-03 used current source checks to support the architecture posture that licensing, privacy, employment screening, investigation, and security risk assessment content must not be treated as universal or timeless. The sources were used for boundary/routing design, not jurisdiction-specific rule authoring.

# Sources

- `ROADMAP.md`
- `docs/architecture/domain-contract.md`
- `docs/architecture/scope-boundaries.md`
- `docs/architecture/prohibited-capabilities.md`
- `docs/architecture/taxonomy-index.yaml`
- `docs/development/handoffs/AI-02-final-handoff.md`
- Ontario Private Security and Investigative Services Act, 2005: https://www.ontario.ca/laws/statute/05p34
- British Columbia security worker licence guidance: https://www2.gov.bc.ca/gov/content/employment-business/business/security-services/security-industry-licensing/workers
- FTC employer consumer-report guidance: https://www.ftc.gov/business-guidance/resources/using-consumer-reports-what-employers-need-know
- ASIS Investigations Standard overview: https://www.asisonline.org/security-news/standards-guidelines/investigations-standard/
- ASIS Security Risk Assessment Standard overview: https://www.asisonline.org/security-news/standards-guidelines/security-risk-assessment-standard/

# Validation Performed

```powershell
.\scripts\validate-all.ps1
python .\scripts\validate-routing.py --repo-root D:\AgentInvestigate
git diff --check
```

# Tests

No behavioral skill tests exist yet because AI-03 creates architecture contracts only.

Paper routing validation covers:

- routine evidence-matrix work;
- regulated licensing issue spotting;
- intrusive employee-observation planning;
- certification-boundary alarm/emergency escalation.

Structural validation checks required AI-03 files, completion token, routing states, sensitivity class labels, intrusive gate chain, certification-boundary support/substitute language, and the paper-validation statement.

# Safety / Regulatory Review

- No regulated skill procedures were authored.
- No intrusive operational workflow was implemented.
- No jurisdiction-specific rule was encoded as universal law.
- The intrusive gate fails closed when jurisdiction, authority, privacy basis, collection basis, necessity, proportionality, alternatives, or human approval are missing.
- Certification-boundary content is limited to recognition, documentation, handoff, and escalation.
- Prohibited capabilities route to `PROHIBITED_REDIRECT`, not to approval workflows.

# Known Limitations

- AI-03 defines architecture and routing on paper only.
- AI-04 must define the full skill authoring standard before any skill is implemented.
- AI-05 must define source metadata and freshness rules before regulated content is authored.
- AI-06 must convert these routing rules into executable tests and fixtures.
- AI-02 taxonomy does not yet include standalone generic `assess-necessity-proportionality` or `assess-less-intrusive-alternative` skills; AI-03 records this as a future taxonomy refinement need.

# Unresolved Issues

- Decide during AI-04 or AI-06 whether general intrusive-gate skills should be added to the taxonomy, or whether domain-specific necessity/proportionality skills are sufficient.

# Explicitly Not Completed

- No AI-04 skill authoring standard.
- No AI-05 source standard.
- No executable routing tests.
- No skills.
- No skillsets.
- No specializations.
- No shared templates or schemas.
- No regulatory source maps.
- No evaluation fixtures.

# Recommended Next Wave

AI-04: Skill Authoring Standard.
