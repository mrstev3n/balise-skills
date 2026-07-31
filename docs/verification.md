# Verification evidence

Date: 2026-07-31

## Repository invariants

Command:

```bash
npm run validate
```

Result: two canonical skills discovered; frontmatter, paths, links, catalogue, adapters, and collection invariants passed.

## JSON Schema

Tool: `check-jsonschema==0.37.4`

Result: `catalog/marketplace.json` and `collections/legal.json` passed their Draft 2020-12 schemas.

## Agent Skills reference validator

Tool source: `agentskills/agentskills`, commit `38a2ff82958afee88dadf4831509e6f7e9d8ef4e`.

Result:

```text
Valid skill: skills/balise-ohada
Valid skill: skills/balise-web-legal
```

## Multi-harness installation

Command shape:

```bash
npx --yes skills@1.5.9 add <local-repository> \
  --agent claude-code codex cursor \
  --skill balise-ohada balise-web-legal \
  --copy --yes
```

Result: the CLI found exactly two skills and installed both into isolated Claude Code, Codex, and Cursor project locations. Recursive comparisons against the canonical source returned no differences.

This proves format and installation compatibility.

## Runtime invocation

Codex CLI `0.145.0` was run in ephemeral, read-only mode against the isolated installation.

- `balise-ohada` was explicitly invoked, read its installed `SKILL.md`, and returned `SKILL_OK references/jurisdiction-router.md`.
- `balise-web-legal` was explicitly invoked, read its installed `SKILL.md`, and returned `SKILL_OK references/applicability-router.md`.
