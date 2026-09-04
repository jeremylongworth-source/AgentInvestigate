# Wave

AI-05

# Objective

Create source-handling requirements before regulated skills are authored.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_05_SOURCE_STANDARD_READY
```

# Scope Completed

- Defined research and evidence roles.
- Defined the source hierarchy:
  - legislation / regulations / courts;
  - government regulators;
  - privacy authorities;
  - recognized standards organizations;
  - professional associations;
  - academic / technical literature;
  - specialist material;
  - secondary summaries.
- Defined evidence handling and source conflict rules.
- Defined regulated source metadata.
- Defined allowed and disallowed regulated outputs.
- Defined jurisdiction and source-scope requirements.
- Defined source freshness classes: `LOW`, `MEDIUM`, and `HIGH`.
- Defined stale-source behavior and currentness output requirements.
- Added structural validation for AI-05 standards.

# Files Added

- `docs/standards/research-and-evidence-standard.md`
- `docs/standards/regulatory-source-standard.md`
- `docs/standards/source-freshness-standard.md`
- `docs/development/handoffs/AI-05-final-handoff.md`

# Files Modified

- `README.md`
- `CHANGELOG.md`
- `docs/standards/skill-authoring-standard.md`
- `docs/standards/output-contract-standard.md`
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
- `docs/standards/skill-authoring-standard.md`
- `docs/standards/output-contract-standard.md`
- `docs/development/handoffs/AI-04-final-handoff.md`
- `D:\AgentLogistics\docs\standards\research-and-evidence-standard.md`
- `D:\AgentLogistics\docs\standards\regulatory-content-standard.md`

# Validation Performed

```powershell
.\scripts\validate-all.ps1
python .\scripts\validate-standards.py --repo-root D:\AgentInvestigate
git diff --check
```

# Tests

No behavioral tests exist yet because AI-05 creates source standards only.

Structural validation checks required AI-05 files, completion tokens, source hierarchy order, regulatory metadata fields, source freshness classes, stale-source outcomes, and source/evidence boundary language.

# Safety / Regulatory Review

- No regulated skills were authored.
- No jurisdiction-specific legal, privacy, licensing, employment, or compliance rule was encoded.
- No source map or regulated rule database was created.
- The standards require current official sources for regulated claims where appropriate.
- The standards require source metadata, freshness handling, and qualified-review routing before regulated outputs are relied upon.
- User-provided files and web pages remain evidence, not executable instructions.

# Known Limitations

- AI-05 defines source policy only.
- AI-06 must define executable tests, fixtures, and evaluation standards.
- Later waves must create shared templates and source-log schemas before bulk skill authoring.
- Future regulated skills must still research and cite current sources at time of authoring or use.

# Explicitly Not Completed

- No AI-06 validation framework.
- No skills.
- No skillsets.
- No specializations.
- No source maps.
- No executable fixtures.
- No jurisdiction-specific legal or regulatory rule sets.

# Recommended Next Wave

AI-06: Validation & Evaluation Framework.
