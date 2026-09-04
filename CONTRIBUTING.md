# Contributing

AgentInvestigate is early in setup. Contributions should follow the active roadmap wave and avoid adding speculative skill content before the architecture and validation gates are closed.

## Contribution Rules

- Work from `ROADMAP.md` and the latest handoff.
- Keep changes scoped to the active wave.
- Do not create empty folders to mirror the provisional architecture.
- Do not add regulated or intrusive claims without authoritative sources and verification dates.
- Do not add procedural content for prohibited capabilities.
- Keep skills atomic when skill authoring begins.
- Put professional role composition in `skillsets/`, not inside broad skills.

## Validation

Run:

```powershell
.\scripts\validate-all.ps1
```

Before opening a pull request, document:

- roadmap wave;
- files changed;
- validation performed;
- source evidence for regulated or safety-sensitive claims;
- known limitations.
