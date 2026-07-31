# Codex/OpenAI adapter

The `overlays/` tree mirrors the relative location of optional OpenAI interface metadata inside a packaged skill. Applying an overlay copies only `agents/openai.yaml` into the corresponding canonical skill bundle.

The canonical `SKILL.md` files do not depend on this adapter. Claude Code, Cursor, and other Agent Skills clients can consume them without OpenAI metadata.

Runtime evidence for the canonical skills is recorded in [`../../docs/verification.md`](../../docs/verification.md).
