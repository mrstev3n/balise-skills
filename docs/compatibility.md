# Compatibility policy

Skill Market uses the open Agent Skills directory format as its portability boundary:

```text
skill-name/
├── SKILL.md
├── references/
├── scripts/
└── assets/
```

Only `SKILL.md` is required. Canonical instructions must use relative paths and must not rely on harness-specific invocation syntax, environment variables, hooks, or hidden skills.

## Evidence levels

- `format-valid`: the skill passes the repository validator and the Agent Skills reference validator.
- `install-tested`: the repository has been discovered and installed into an isolated target for the named harness.
- `runtime-tested`: the installed skill has been discovered and invoked in the named harness.

The catalogue records `runtime-tested` claims only when backed by an observed invocation.

Installation tests use isolated destinations and compare the installed directories with their canonical sources. See [verification evidence](verification.md).

Codex CLI `0.145.0` discovered and invoked both installed skills in ephemeral, read-only sessions.

## Harness strategy

- Claude Code consumes the canonical skill. Plugin packaging, if added, belongs in a Claude-specific adapter.
- Codex/OpenAI consumes the canonical skill and may receive optional `agents/openai.yaml` metadata through the isolated adapter.
- Cursor consumes the canonical skill without an adapter unless a verified Cursor-only requirement appears.
- Other compatible harnesses receive the same canonical directory through an Agent Skills installer.
