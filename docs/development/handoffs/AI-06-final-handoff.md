# Wave

AI-06

# Objective

Build quality controls before authoring at scale.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_06_VALIDATION_FRAMEWORK_READY
```

# Scope Completed

- Defined the AgentInvestigate testing standard.
- Defined the required AI-06 test classes:
  - correct routing;
  - incorrect routing;
  - missing jurisdiction;
  - missing authority;
  - missing consent;
  - prohibited request;
  - regulated request;
  - intrusive request;
  - certification-boundary request;
  - missing evidence;
  - contradictory evidence;
  - unsupported inference;
  - source freshness;
  - incorrect source jurisdiction;
  - output-format compliance.
- Defined the AgentInvestigate evaluation standard.
- Defined the comparison model: `general model` vs. `general model + AgentInvestigate skill`.
- Defined evaluation dimensions:
  - correctness;
  - evidence discipline;
  - uncertainty;
  - source use;
  - routing;
  - privacy behavior;
  - safety boundaries;
  - usefulness.
- Added initial scenario catalog fixtures covering every required test class.
- Added an evaluation rubric fixture.
- Added test-framework validation and wired it into the full validation chain.

# Files Added

- `docs/standards/testing-standard.md`
- `docs/standards/evaluation-standard.md`
- `tests/validation-scenarios.json`
- `tests/evaluation-rubric.json`
- `scripts/validate-tests.py`
- `docs/development/handoffs/AI-06-final-handoff.md`

# Files Modified

- `README.md`
- `CHANGELOG.md`
- `scripts/validate-all.ps1`
- `scripts/validate-docs.py`
- `scripts/validate-standards.py`

# Sources

- `ROADMAP.md`
- `docs/architecture/domain-contract.md`
- `docs/architecture/scope-boundaries.md`
- `docs/architecture/prohibited-capabilities.md`
- `docs/architecture/taxonomy-index.yaml`
- `docs/architecture/sensitivity-model.md`
- `docs/architecture/authority-routing.md`
- `docs/architecture/intrusive-task-gate.md`
- `docs/architecture/certification-boundaries.md`
- `docs/standards/skill-authoring-standard.md`
- `docs/standards/output-contract-standard.md`
- `docs/standards/research-and-evidence-standard.md`
- `docs/standards/regulatory-source-standard.md`
- `docs/standards/source-freshness-standard.md`
- `docs/development/handoffs/AI-05-final-handoff.md`

# Validation Performed

```powershell
.\scripts\validate-all.ps1
python .\scripts\validate-tests.py --repo-root D:\AgentInvestigate
git diff --check
```

# Tests

AI-06 creates framework-level tests and fixtures. No production skill behavioral tests exist yet because no skills have been authored.

Structural validation checks required AI-06 files, completion tokens, test-class coverage, scenario schema fields, routing states, sensitivity classes, evaluation dimensions, comparison labels, score scale, and rubric details.

# Safety / Regulatory Review

- No skills were authored.
- No skillsets were authored.
- No regulated source map was created.
- No jurisdiction-specific legal, privacy, licensing, employment, or compliance rule was encoded.
- No intrusive operational workflow was implemented.
- Negative scenarios cover prohibited requests, intrusive gate failures, stale sources, wrong jurisdiction, missing consent, and unsupported inference.

# Known Limitations

- AI-06 validates the framework and initial fixtures only.
- Future waves must add skill-specific tests when skills are implemented.
- AI-07 must create shared professional foundations before reference skills.
- AI-08 must use this framework to validate the four-class reference implementation.

# Explicitly Not Completed

- No AI-07 shared foundations.
- No AI-08 reference skills.
- No production skills.
- No skillsets.
- No specializations.
- No regulatory source maps.
- No full before/after evaluation reports for implemented skills.

# Recommended Next Wave

AI-07: Shared Professional Foundations.
