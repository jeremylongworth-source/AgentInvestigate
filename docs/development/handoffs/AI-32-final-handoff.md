# Wave

AI-32

# Objective

Compose existing atomic skills into role-level professional systems.

# Verdict

READY

# Completion Token

```text
AGENTINVESTIGATE_AI_32_PROFESSIONAL_SKILLSETS_READY
```

# Scope Completed

- Added the AI-32 professional skillset architecture document at `docs/architecture/professional-skillset-composition.md`.
- Added the canonical skillset registry at `skillsets/professional-skillsets.json`.
- Added the skillset layer README at `skillsets/README.md`.
- Added all 19 roadmap professional skillsets.
- Populated `included_skills` from `docs/architecture/taxonomy-index.yaml` where direct `professional_skillsets` tags already existed.
- Added explicit derived memberships for `loss-prevention-officer`, `security-operations-manager`, and `corporate-security-manager`.
- Added role-level purpose, routing triggers, dependencies, jurisdiction requirements, authority requirements, sensitivity limits, escalation rules, expected outputs, and excluded responsibilities for every skillset.
- Added AI-32 skillset composition fixture coverage.
- Added `scripts/generate-ai32-skillsets.py` for reproducible registry generation from the taxonomy.
- Added `scripts/validate-skillsets.py` and wired it into `scripts/validate-all.ps1`.
- Updated README and changelog.

# Skillsets Added

Investigation:

```text
private-investigator
investigative-analyst
investigative-case-manager
corporate-investigator
workplace-investigator
background-screening-specialist
loss-prevention-investigator
```

Security:

```text
security-officer
mobile-patrol-officer
loss-prevention-officer
security-supervisor
security-operations-manager
physical-security-analyst
security-risk-assessor
incident-response-coordinator
security-program-manager
```

Hybrid:

```text
corporate-security-investigator
asset-protection-specialist
corporate-security-manager
```

# Composition Rule

```text
Skillsets compose skills.
They must not duplicate underlying procedures.
```

AI-32 does not create new atomic skills. It creates role-level composition definitions that point to existing `skills/<family>/<skill>/SKILL.md` packages.

# Derived Membership Decisions

Most role memberships come directly from `professional_skillsets` in `docs/architecture/taxonomy-index.yaml`.

The following roadmap roles are derived from validated adjacent family and composition-target coverage:

- `loss-prevention-officer`: derives from Family 19 loss-prevention and asset-protection skills.
- `security-operations-manager`: derives from `security-supervisor` tagged skills plus Family 20 program-management skills.
- `corporate-security-manager`: derives from `security-program-manager`, `security-supervisor`, `corporate-investigator`, `asset-protection-specialist`, and Family 20 program-management skills.

These are AI-32 composition decisions only. They do not rewrite the taxonomy.

# Routing Boundary

Every AI-32 skillset inherits the global routing states:

```text
PROCEED_ROUTINE
CLARIFY_SCOPE
REGULATED_RESEARCH_ONLY
INTRUSIVE_GATE_REQUIRED
CERTIFICATION_ESCALATION
PROHIBITED_REDIRECT
```

Skillsets must preserve jurisdiction, authority, lawful purpose, privacy, consent, source-access, evidence, role, sensitivity, and human-review gates before sequencing included atomic skills.

# Files Added

- `docs/architecture/professional-skillset-composition.md`
- `skillsets/README.md`
- `skillsets/professional-skillsets.json`
- `tests/skillsets/AI-32-professional-skillset-composition.json`
- `scripts/generate-ai32-skillsets.py`
- `scripts/validate-skillsets.py`
- `docs/development/handoffs/AI-32-final-handoff.md`

# Files Modified

- `README.md`
- `CHANGELOG.md`
- `scripts/validate-all.ps1`
- `scripts/validate-docs.py`

# Validation Performed

```powershell
python -m py_compile scripts\generate-ai32-skillsets.py scripts\validate-skillsets.py scripts\validate-docs.py
python scripts\generate-ai32-skillsets.py
python scripts\validate-skillsets.py --repo-root D:\AgentInvestigate
python scripts\validate-docs.py --repo-root D:\AgentInvestigate
.\scripts\validate-all.ps1
git diff --check
```

# Safety / Regulatory Review

- AI-32 does not duplicate underlying skill procedures.
- AI-32 does not create new regulated content, jurisdiction modules, source maps, legal determinations, licensing approvals, compliance certifications, post orders, operational tactics, force instruction, weapons instruction, restraint techniques, engineering approvals, fire-code approvals, life-safety approvals, or emergency-response certifications.
- Skillsets preserve the existing routing states and must route regulated, intrusive, certification-boundary, and prohibited requests through existing controls.
- Role names must not be treated as proof of licence, authority, training, certification, employment authority, site authority, client authority, regulator approval, or professional eligibility.

# Known Limitations

- The taxonomy does not directly tag `loss-prevention-officer`, `security-operations-manager`, or `corporate-security-manager`; AI-32 derives those memberships from existing validated family and composition-target coverage.
- AI-32 does not run live model before/after evaluation.
- AI-32 does not produce runtime packaging for skillsets.
- AI-32 does not create per-role prompt bundles beyond the canonical registry.

# Explicitly Not Completed

- No AI-33 Multi-Skill Integration Evaluation.
- No AI-34 Adversarial Safety & Misuse Resistance Evaluation.
- No public packaging or release readiness work.

# Recommended Next Wave

AI-33: Multi-Skill Integration Evaluation.
