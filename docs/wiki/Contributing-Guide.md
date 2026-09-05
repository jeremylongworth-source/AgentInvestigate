# Contributing Guide

Contributions must follow the active roadmap wave and the latest handoff.

## Basic Rules

- Work from `ROADMAP.md` and the latest handoff.
- Keep changes scoped to the active wave.
- Do not create empty placeholder folders.
- Keep private investigation and private security structurally distinct.
- Do not add regulated or intrusive claims without authoritative sources and verification dates.
- Do not add procedural content for prohibited capabilities.
- Keep skills atomic.
- Put professional role composition in `skillsets/`, not inside broad skills.
- Update fixtures and validators with behavior changes.

## Before Opening A Pull Request

Run:

```powershell
.\scripts\validate-all.ps1
```

Document:

- roadmap wave;
- files changed;
- validation performed;
- source evidence for regulated or safety-sensitive claims;
- known limitations;
- any release-risk acceptance required from a maintainer.

## Skill Authoring

A new skill must include a `SKILL.md` with valid frontmatter and bounded instructions.

Do not duplicate procedures already covered by an existing atomic skill.

Do not add scripts with broad shell permissions unless the script is reviewed, necessary, and safe.
