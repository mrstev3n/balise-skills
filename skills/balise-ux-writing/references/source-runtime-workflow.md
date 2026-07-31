# Source and Runtime Workflow

Use this reference before editing source code, localization catalogs, content schemas, component stories, fixtures, or rendered applications.

## Contents

- Repository discovery
- Source-of-truth decisions
- Safe implementation
- Catalog and token integrity
- Rendered verification
- Testing and handoff

## Repository Discovery

Inspect before editing:

- project instructions and working-tree state;
- routes, screens, and component boundaries;
- localization framework and catalog locations;
- content schemas, CMS adapters, feature flags, and design-system components;
- Storybook stories, fixtures, visual tests, and browser tests;
- generated bundles, snapshots, and files that must not be edited directly;
- terminology or style documentation already present.

Use fast scoped search for current strings, translation keys, related actions, and state variants. Avoid broad replacement before understanding each occurrence.

## Choose the Source of Truth

Prefer editing:

1. canonical content or translation catalogs;
2. component properties or content schemas;
3. source templates or screen components;
4. local fixtures or stories when testing only.

Do not edit compiled output, generated translations, caches, or snapshots as the primary change.

When the same visible string exists in several places, determine whether it is intentionally contextual, duplicated debt, or generated from a common source.

## Safe Implementation

- Preserve existing component APIs, keys, imports, types, and formatting.
- Do not rename translation keys merely because visible wording changes unless the project convention requires semantic keys.
- Keep content changes separate from unrelated refactoring.
- Preserve markup and rich-text structure.
- Escape apostrophes, quotes, HTML, Markdown, and control characters according to the target format.
- Maintain test IDs and analytics identifiers unless explicitly in scope.
- Do not bypass content validation or schema constraints.
- Do not add a dependency for a wording-only change.

## Catalog and Token Integrity

For localization resources:

- preserve interpolation tokens exactly;
- compare tokens across source and target strings;
- preserve ICU plural/select branches;
- keep markup tags balanced and supported;
- inspect escaped newlines and whitespace significance;
- verify locale file syntax;
- determine fallback behavior for missing keys;
- avoid placing untranslated source-language copy into production target catalogs without approval.

For dynamic UI copy:

- verify the condition selecting each message;
- distinguish validation, permission, network, empty, loading, and success states;
- ensure the proposed copy is true for every code path using the string;
- split a shared string only when contexts genuinely require different meaning.

## Rendered Verification

When the application can be run safely:

- reproduce the affected state using existing fixtures or test data;
- inspect desktop and supported narrow layouts;
- check wrapping, truncation, overlap, and hierarchy;
- exercise primary, secondary, cancel, retry, and recovery actions;
- verify loading, success, error, empty, and permission states in scope;
- test keyboard focus and dynamic announcement when accessibility behavior is claimed;
- switch locale and direction when relevant;
- capture screenshots or exact steps proportional to the risk.

Do not mutate production data, send external messages, or publish without explicit authorization.

## Tests and Handoff

After source changes, run the relevant subset of:

- catalog or schema validation;
- token parity checks;
- lint and type checking;
- unit or component tests;
- build;
- visual or browser tests;
- searches for obsolete terminology in the authorized scope.

Report:

- canonical files changed;
- states and locales checked;
- exact tests passed;
- visual or runtime evidence collected;
- remaining product, translation, accessibility, analytics, or legal checks.

Do not call implementation verified if only the source text was changed and the interface was not rendered.
