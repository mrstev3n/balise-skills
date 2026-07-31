# Codex/OpenAI adapter

The `overlays/` tree mirrors the relative location of optional OpenAI interface metadata inside a packaged skill. Applying an overlay copies only `agents/openai.yaml` into the corresponding canonical skill bundle.

The canonical `SKILL.md` files do not depend on this adapter. Claude Code, Cursor, and other Agent Skills clients can consume them without OpenAI metadata.

The adapter has not yet been runtime-tested. Do not mark Codex/OpenAI as `runtimeTested` in the catalogue until a packaged installation and invocation have been verified.
