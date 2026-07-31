# Skill Market

Public, multi-harness catalogue for portable Agent Skills.

This repository treats [`SKILL.md`](https://agentskills.io/specification) as the canonical skill format. Harness-specific packaging belongs in isolated adapters and must not alter the canonical instructions.

## Initial scope

The first release is intentionally limited to two original skills:

- `ohada-legal-practice`
- `website-legal-compliance`

They form the initial installable `legal` collection. Legal is one collection and discovery category within a global marketplace; it is not the repository's total scope.

No Lawve skill, `legal-contract-review`, `evolsb-contract-review`, or other third-party or adapted skill is included in the initial catalogue.

## Catalogue model

- **Category:** primary discovery classification; not installable.
- **Tag:** transversal discovery filter.
- **Collection:** ordered, versioned, installable set of skills.

`category:legal` and `collection:legal` are distinct. Legal is the first collection and active category in a marketplace designed to support future domains such as design, typography, and security.

## Repository layout

```text
catalog/       Machine-readable marketplace index and JSON Schemas
collections/   Installable collection manifests
skills/        Canonical, harness-neutral Agent Skills
adapters/      Optional harness-specific metadata and packaging
docs/          Metadata and compatibility policies
scripts/       Deterministic repository validation
```

## Install

Replace `<owner>` with the GitHub owner after the public repository is created.

List the available skills:

```bash
npx skills add <owner>/Skill-Market --list
```

Install one skill:

```bash
npx skills add <owner>/Skill-Market --skill ohada-legal-practice
```

Install the `legal` collection:

```bash
npx skills add <owner>/Skill-Market \
  --skill ohada-legal-practice \
  --skill website-legal-compliance
```

The installer selects project or global destinations and supported harnesses. See [compatibility policy](docs/compatibility.md) before interpreting support claims.

## Validate

Run the deterministic local checks:

```bash
npm run validate
```

CI also validates the JSON manifests against their schemas and runs the official Agent Skills reference validator on both skills.

## Release status

The catalogue is at `0.1.0` pre-publication. Both skills are installation-tested for Claude Code, Codex, and Cursor. Both are runtime-tested with Codex CLI `0.145.0`; Claude Code and Cursor runtime claims remain pending.

## Licence

Apache License 2.0. See `LICENSE`.
