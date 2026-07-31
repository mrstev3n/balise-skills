# Verification evidence

Date: 2026-07-31

## Repository invariants

Command:

```bash
npm run validate
```

Result: two canonical skills discovered; private dependency allowlist, frontmatter, paths, links, catalogue, adapters, and collection invariants passed.

## JSON Schema

Tool: `check-jsonschema==0.37.4`

Result: `catalog/marketplace.json` and `collections/legal.json` passed their Draft 2020-12 schemas.

## Agent Skills reference validator

Tool source: `agentskills/agentskills`, commit `38a2ff82958afee88dadf4831509e6f7e9d8ef4e`.

Result:

```text
Valid skill: skills/ohada-legal-practice
Valid skill: skills/website-legal-compliance
```

## Multi-harness installation

Command shape:

```bash
npx --yes skills@1.5.9 add <local-repository> \
  --agent claude-code codex cursor \
  --skill ohada-legal-practice website-legal-compliance \
  --copy --yes
```

Result: the CLI found exactly two skills and installed both into isolated Claude Code, Codex, and Cursor project locations. Recursive comparisons against the canonical source returned no differences.

This proves format and installation compatibility.

## Runtime invocation

Codex CLI `0.145.0` was run in ephemeral, read-only mode against the isolated installation.

- `ohada-legal-practice` was explicitly invoked, read its installed `SKILL.md`, and returned `SKILL_OK references/jurisdiction-router.md`.
- `website-legal-compliance` was explicitly invoked, read its installed `SKILL.md`, and returned `SKILL_OK references/applicability-router.md`.

Claude Code `2.1.201` could not be runtime-tested because the local client was not authenticated. Cursor Agent `2026.06.15` was authenticated, but two read-only attempts returned HTTP 503. These harnesses remain installation-tested only and are not listed under `runtimeTested`.
