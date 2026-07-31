# Affinity Concepts And Nuances

Use this reference when an Affinity MCP task requires judgment before execution. Keep the operational snippets in `affinity-js-patterns.md`; this file is for deciding what kind of object, workflow, or verification is appropriate.

## Skill Boundary

`balise-affinity-mcp` should answer: how do I safely do this in the open Affinity document through MCP?

It should not become a general Affinity handbook. General knowledge belongs in the complementary `balise-affinity` skill, then only durable action rules should be copied back here.

## Studios And Context

Affinity combines vector, pixel, and layout work in one environment. The active Studio or Persona changes which tools and panels are visible, but it does not necessarily imply a separate file or separate document model.

Automation rule:

- Inspect the document and selected nodes rather than assuming the visible UI mode fully describes the file.
- When a user describes a UI tool, map it to the closest SDK operation only after reading the relevant SDK docs.
- Treat exact Studio names, shortcuts, and AI feature availability as version-sensitive.

## Object Type Choices

Choose the object type based on the intended behavior:

| Need | Prefer | Why |
| --- | --- | --- |
| Short label, headline, number, decorative word | Artistic Text | The object hugs content and transforms predictably. |
| Paragraph, fixed text area, columns, threaded copy | Frame Text | The frame is part of the layout model. |
| Simple editable shape | Shape node | Keeps primitive shape controls when available. |
| Exact custom outline | Curve or polycurve | Gives precise path control. |
| Repeated UI element or motif | Symbol or named group | Preserves reuse and future global edits. |
| Reusable color system | Global color or document swatch when SDK supports it | Keeps theming editable. |
| Cropped visual region | Mask, clipping, or picture frame | Preserves source content better than destructive crop. |

## Text Nuances

Frame Text and Artistic Text are not interchangeable.

- Use Frame Text when the box matters.
- Use Artistic Text when the text itself is the graphic object.
- Frame Text may show a visible container in the editing UI; verify with `render_spread` before treating that box as artwork.
- For rotated labels, prefer Artistic Text. Create it, retrieve the node, rotate around its center, measure `spreadVisibleBox`, then translate.
- Use `StoryBuilder` for text creation. In current tested usage, text definition `createDefault()` helpers are not reliable.
- Keep `glyph.characterSpacing` small. Values like `-1` or `-4` can collapse glyph advance.

## Selection And Overlay Nuances

Selection changes the visual state of the Affinity UI. It can also confuse interpretation if the user is judging the live canvas.

- `render_selection` is good for checking one edited object.
- `render_spread` is better for checking an entire composition.
- Avoid selecting all objects just to verify the design when a spread render is available.
- If the user reports boxes around text, render the spread before changing the document.

## Non-Destructive Preference

Prefer reversible structures unless the user explicitly asks for final flattening:

- Masks or clipping before erasing pixels.
- Live filters before destructive raster filters.
- Compound booleans before destructive shape operations when editability matters.
- Linked or named reusable assets before duplicated untracked copies.
- Groups, symbols, `userDescription`, and clear layer naming before anonymous generated objects.

## Layer Hygiene For Automation

A file is easier to automate when its structure is legible.

- Give generated nodes useful `userDescription` values.
- Use stable prefixes for automation-created elements.
- Filter by node type and description before cleanup.
- Preserve user-created content unless the deletion target is explicit.
- Leave meaningful selections after edits so the user can inspect or undo the right object.

## Verification Ladder

Use the cheapest verification that proves the claim:

1. Console JSON for document state, counts, IDs, boxes, and dirty state.
2. Object render for a single changed selection.
3. Spread render for composition, text overlay, and export-like visual checks.
4. Export check when file output, transparency, bleed, color, or format is the point of the task.

Report uncertainty clearly when the SDK cannot expose a UI-only feature.

## Volatile Details

Verify before relying on:

- Exact keyboard shortcuts.
- Current AI feature names or permissions.
- Whether a given UI operation has an SDK command helper.
- Version-specific Studio naming.
- Claims about file format interchangeability.
