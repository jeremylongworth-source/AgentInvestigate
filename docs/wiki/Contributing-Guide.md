# Contributing Guide

Contributions must follow the active roadmap wave and latest handoff. Repository quality depends on keeping scope, evidence, and safety boundaries explicit.

## Before You Change A File

1. Read `ROADMAP.md` and the latest handoff.
2. Verify the current repository and branch state.
3. Define the bounded change and its acceptance criteria.
4. Identify sensitivity, jurisdiction, authority, source freshness, and safety implications.
5. Check whether an existing skill or shared asset already covers the need.

Do not create empty placeholder folders or silently implement a future roadmap wave.

## Skill Authoring

A new skill must:

- remain atomic and bounded;
- use valid frontmatter and the repository authoring standard;
- state triggers and non-triggers;
- define inputs, assumptions, dependencies, procedure, evidence, sources, authority checks, sensitivity handling, output contract, limitations, and escalation;
- avoid prohibited procedural content;
- include routing, negative, and output-format scenarios where applicable.

Professional roles belong in `skillsets/`, not in broad procedural skills.

## Documentation And Sources

Use authoritative sources for regulated or safety-sensitive claims. Record source title, organization, jurisdiction, URL, publication and effective dates when available, access date, verification date, applicability, supersession risk, and consuming skills.

Current-source verification is required before relying on high-supersession material.

## Validation

```powershell
.\scripts\validate-all.ps1
```

Run the full gate before opening a pull request.

## Pull Request Content

Describe:

- roadmap wave and bounded objective;
- files added or changed;
- behavior or documentation impact;
- validation performed;
- source evidence;
- known limitations;
- unresolved issues and release risk.

Preserve the private investigation/private security distinction and all authority, privacy, human-review, certification, and prohibited-capability gates.
