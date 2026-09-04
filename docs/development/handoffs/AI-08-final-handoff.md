# Wave

AI-08

# Objective

Prove the repository architecture before bulk authoring by creating one complete reference skill from each sensitivity class.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_08_REFERENCE_SKILLS_READY
```

# Scope Completed

- Created the `ROUTINE` reference skill: `build-evidence-matrix`.
- Created the `REGULATED` reference skill: `identify-licensing-requirement`.
- Created the `INTRUSIVE` reference skill: `assess-observation-proportionality`.
- Created the `CERTIFICATION_BOUNDARY` reference skill: `determine-emergency-escalation`.
- Added OpenAI adapter metadata for each reference skill.
- Added one reference file for each reference skill.
- Added AI-08 scenario fixtures with positive and negative-routing coverage for each skill.
- Added skill validation for:
  - skill package layout;
  - frontmatter;
  - required AI-04 section order;
  - references;
  - OpenAI adapter metadata;
  - taxonomy family and sensitivity alignment;
  - taxonomy dependency checks;
  - positive and negative-routing scenario coverage.
- Wired skill validation into the full validation chain.

# Reference Skills

| Skill | Sensitivity | Family | Boundary |
|---|---|---|---|
| `build-evidence-matrix` | `ROUTINE` | `09-investigative-analysis` | Builds source-linked matrices without inventing facts or making legal/employment findings. |
| `identify-licensing-requirement` | `REGULATED` | `03-law-licensing-privacy-compliance` | Produces licensing issue spotting and source needs, not final licensing determinations. |
| `assess-observation-proportionality` | `INTRUSIVE` | `10-observation-surveillance-governance` | Assesses proportionality only after intrusive gates; no operational surveillance tactics. |
| `determine-emergency-escalation` | `CERTIFICATION_BOUNDARY` | `15-incident-response` | Supports escalation recognition and documentation; no tactical, force, or technical substitute. |

# Files Added

- `skills/09-investigative-analysis/build-evidence-matrix/SKILL.md`
- `skills/09-investigative-analysis/build-evidence-matrix/agents/openai.yaml`
- `skills/09-investigative-analysis/build-evidence-matrix/references/evidence-matrix-reference.md`
- `skills/03-law-licensing-privacy-compliance/identify-licensing-requirement/SKILL.md`
- `skills/03-law-licensing-privacy-compliance/identify-licensing-requirement/agents/openai.yaml`
- `skills/03-law-licensing-privacy-compliance/identify-licensing-requirement/references/licensing-source-checklist.md`
- `skills/10-observation-surveillance-governance/assess-observation-proportionality/SKILL.md`
- `skills/10-observation-surveillance-governance/assess-observation-proportionality/agents/openai.yaml`
- `skills/10-observation-surveillance-governance/assess-observation-proportionality/references/observation-proportionality-checklist.md`
- `skills/15-incident-response/determine-emergency-escalation/SKILL.md`
- `skills/15-incident-response/determine-emergency-escalation/agents/openai.yaml`
- `skills/15-incident-response/determine-emergency-escalation/references/emergency-escalation-checklist.md`
- `tests/reference-skills/AI-08-reference-scenarios.json`
- `scripts/validate-skills.py`
- `docs/development/handoffs/AI-08-final-handoff.md`

# Files Modified

- `README.md`
- `CHANGELOG.md`
- `docs/standards/testing-standard.md`
- `scripts/validate-all.ps1`
- `scripts/validate-docs.py`

# Sources

- `ROADMAP.md`
- `docs/architecture/taxonomy-index.yaml`
- `docs/architecture/sensitivity-model.md`
- `docs/architecture/authority-routing.md`
- `docs/architecture/intrusive-task-gate.md`
- `docs/architecture/certification-boundaries.md`
- `docs/architecture/prohibited-capabilities.md`
- `docs/standards/skill-authoring-standard.md`
- `docs/standards/skill-naming-standard.md`
- `docs/standards/output-contract-standard.md`
- `docs/standards/research-and-evidence-standard.md`
- `docs/standards/regulatory-source-standard.md`
- `docs/standards/source-freshness-standard.md`
- `docs/standards/testing-standard.md`
- `docs/standards/evaluation-standard.md`
- `docs/foundations/foundation-catalog.md`
- `docs/foundations/foundation-consumer-map.json`
- `docs/foundations/professional-vocabulary.md`
- `docs/foundations/shared-schemas.md`
- `docs/foundations/report-structure-contracts.md`
- `docs/development/handoffs/AI-07-final-handoff.md`

# Validation Performed

```powershell
.\scripts\validate-all.ps1
python .\scripts\validate-skills.py --repo-root D:\AgentInvestigate
git diff --check
```

# Tests

AI-08 adds framework-level scenario fixtures for the four reference skills. The validator confirms each reference skill has at least one positive scenario and one negative-routing scenario.

No live before/after model evaluation was run in AI-08. The scenario and rubric framework is ready for future evaluation reports.

# Safety / Regulatory Review

- Mass authoring is not authorized until AI-08 closes `READY`.
- No bulk skill authoring was performed.
- No skillsets were authored.
- No jurisdiction-specific legal, privacy, licensing, employment, or compliance rule was encoded as universal.
- The regulated reference skill is issue-spotting only.
- The intrusive reference skill fails closed when authority, privacy, necessity, proportionality, alternatives, or human approval are missing.
- The certification-boundary reference skill avoids tactical, force, weapons, restraint, clearing, and technical system substitute instructions.
- Negative-routing scenarios cover evidence manipulation, stale or wrong-jurisdiction licensing sources, missing authority, prohibited tracking, and prohibited tactical response.

# Known Limitations

- Reference skills are initial implementations, not the full taxonomy.
- Upstream taxonomy dependencies for the reference skills are not all implemented yet; each skill declares how to handle missing dependencies.
- Future waves must add skill-specific before/after evaluation reports as skills mature.
- AI-09 starts Family 01 only after this reference implementation validates.

# Explicitly Not Completed

- No AI-09 professional core family implementation.
- No mass authoring.
- No skillsets.
- No specializations.
- No regulatory source maps.
- No jurisdiction-specific rule database.
- No full before/after evaluation reports.

# Recommended Next Wave

AI-09: Professional Core & Ethics.
