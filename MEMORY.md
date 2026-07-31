# Project memory

Purpose: preserve the durable product, architecture, compatibility, and publication decisions for this public Agent Skills marketplace.

Last reviewed: 2026-07-31

## Current workflow

- Research, define, execute, verify, then deliver.
- Keep the private internal Skills repository separate and preserve its uncommitted work.
- Copy only explicitly approved original skills into this repository; never move their internal source folders.
- Do not publish, push, or create a remote without explicit authorization and a verified GitHub target.

## Architecture and data model

- `skills/<skill-id>/SKILL.md` is the canonical source for every skill.
- `catalog/marketplace.json` is the canonical marketplace index and is validated by JSON Schema.
- A category is a primary discovery classification and is not installable.
- Tags are transversal discovery filters.
- A collection is an ordered, versioned, installable group of skills and may span categories.
- `category:legal` and `collection:legal` are separate namespaces.

## Product direction

- The marketplace is global and multi-domain. Legal is its first collection, not its total scope.
- The initial release contains only `ohada-legal-practice` and `website-legal-compliance`.
- Lawve, `legal-contract-review`, `evolsb-contract-review`, and all other third-party or adapted skills are excluded from the initial public catalogue.

## Implementation notes

- Keep canonical skill instructions harness-neutral.
- Isolate Claude Code, Codex/OpenAI, Cursor, and other harness packaging in adapters or generated artefacts.
- Do not require users to install an excluded skill for a published skill to function.
- Preserve richer cross-skill routing in the private internal versions when it benefits private usage; maintain an autonomous public edition here.
- The public skills live under `skills/`; OpenAI interface metadata lives under `adapters/codex-openai/overlays/`.
- The public `website-legal-compliance` edition handles EU and French applicability directly from official sources and contains no Lawve dependency.

## Deployment and verification

- Validate every canonical skill against the Agent Skills specification.
- Validate catalogue and collection manifests against their JSON Schemas.
- Test documentation commands from a clean clone.
- Distinguish format validation, installation testing, and runtime testing in compatibility claims.
- Both public skills were runtime-invoked successfully with Codex CLI `0.145.0` on 2026-07-31; Claude Code and Cursor remain installation-tested only.
- The intended GitHub repository is public, displayed as `Skill Market`, with the GitHub slug `Skill-Market`; the owner and remote must be verified before publication.

## Security constraints

- Reject secrets, absolute private paths, unsafe executable behaviour, and undeclared external dependencies.
- Audit all bundled files and external-source references before release.
- Keep legal version and jurisdiction checks visible; do not present static reference material as proof of current law.

## Next durable decisions

- Confirm the GitHub owner when authentication is restored.
- Record tested harness versions only after live verification.
- Decide whether a Claude Code plugin adapter is warranted after canonical installation tests.

## Update rule

Maintain this file as a compact description of current durable state. Replace obsolete facts instead of appending a chronological changelog.
