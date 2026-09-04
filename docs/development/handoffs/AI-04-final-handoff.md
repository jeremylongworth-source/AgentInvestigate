# Wave

AI-04

# Objective

Define how every AgentInvestigate skill is authored.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_04_SKILL_STANDARD_READY
```

# Scope Completed

- Defined the required AgentInvestigate skill package layout.
- Defined required `SKILL.md` frontmatter.
- Defined description requirements.
- Defined required skill sections for:
  - triggers;
  - non-triggers;
  - inputs;
  - assumptions;
  - dependencies;
  - procedure;
  - evidence requirements;
  - source requirements;
  - jurisdiction requirements;
  - authority checks;
  - sensitivity handling;
  - outputs;
  - limitations;
  - escalation;
  - references;
  - testing requirements.
- Defined skill naming rules, approved verb rules, path rules, specialization naming, and disallowed naming patterns.
- Defined output contract requirements for facts, allegations, inferences, sources, authority, jurisdiction, limitations, escalation, and testing.
- Added structural validation for AI-04 standards.

# Files Added

- `docs/standards/skill-authoring-standard.md`
- `docs/standards/skill-naming-standard.md`
- `docs/standards/output-contract-standard.md`
- `docs/development/handoffs/AI-04-final-handoff.md`
- `scripts/validate-standards.py`

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
- `docs/architecture/taxonomy-index.yaml`
- `docs/architecture/sensitivity-model.md`
- `docs/architecture/authority-routing.md`
- `docs/architecture/intrusive-task-gate.md`
- `docs/architecture/certification-boundaries.md`
- `docs/development/handoffs/AI-03-final-handoff.md`
- `D:\AgentLogistics\docs\standards\skill-authoring-standard.md`
- `D:\AgentLogistics\docs\standards\skill-naming-standard.md`
- `D:\CodexProject\AgentSkills\docs\authoring-guide.md`
- `D:\CodexProject\AgentSkills\docs\skill-quality-bar.md`
- `D:\CodexProject\AgentSkills\docs\compatibility.md`
- `D:\CodexProject\AgentSkills\docs\evaluation\evaluation-method.md`

# Validation Performed

```powershell
.\scripts\validate-all.ps1
python .\scripts\validate-standards.py --repo-root D:\AgentInvestigate
git diff --check
```

# Tests

No behavioral skill tests exist yet because AI-04 creates authoring standards only.

Structural validation checks required AI-04 files, completion tokens, required authoring terms, required skill section order, naming contract terms, output contract terms, and sensitivity class coverage.

# Safety / Regulatory Review

- No skills were authored.
- No skillsets were authored.
- No intrusive operational workflow was implemented.
- No jurisdiction-specific legal, privacy, licensing, employment, or compliance rule was encoded.
- The skill authoring standard requires future intrusive skills to fail closed when gates are missing.
- The output contract standard requires facts, allegations, inferences, unknowns, limitations, and source posture to remain distinguishable.
- The naming standard blocks names that imply prohibited capabilities, certification substitutes, or hidden intrusive work.

# Known Limitations

- AI-04 defines standards only.
- AI-05 must define the detailed legal, regulatory, evidence-source hierarchy and freshness metadata before regulated content is authored.
- AI-06 must define executable testing, fixtures, and evaluation standards before mass skill authoring.
- AI-07 through AI-10 must create shared foundations before reference skills and bulk skill implementation.

# Explicitly Not Completed

- No AI-05 source standard.
- No AI-06 testing standard.
- No skills.
- No skillsets.
- No specializations.
- No shared templates or schemas.
- No regulatory source maps.
- No evaluation fixtures.

# Recommended Next Wave

AI-05: Legal, Regulatory & Evidence Source Standard.
