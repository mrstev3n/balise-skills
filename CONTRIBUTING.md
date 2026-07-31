# Contributing

Skill Market currently accepts only maintainer-approved original skills. Opening the repository to external submissions is out of scope for the initial release.

For an approved change:

1. Keep the canonical skill under `skills/<skill-id>/`.
2. Keep `SKILL.md` frontmatter limited to `name` and `description`.
3. Put detailed material in directly linked `references/` files.
4. Keep harness-specific metadata under `adapters/`.
5. Update catalogue and collection manifests when discovery metadata changes.
6. Run `npm run validate` and the Agent Skills reference validator before review.

Do not add per-skill README, changelog, licence, private path, secret, undeclared dependency, or third-party material without a provenance and licence review.
