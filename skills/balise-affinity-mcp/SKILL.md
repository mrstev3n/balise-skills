---
name: balise-affinity-mcp
description: Automate Affinity by Canva through the Affinity MCP and JavaScript SDK for manipulating open documents, selected objects, layers/nodes, geometry, text, fills, line styles, document commands, exports, and visual verification. Use when an agent needs to test or use the Affinity MCP, edit the current Affinity file, inspect or modify objects or selections, create or adjust Affinity elements, automate Affinity features, or capture reusable Affinity SDK lessons.
---

# Affinity MCP Automation

Use the Affinity MCP as a live application-control surface. Work from the open document, inspect before editing, prefer small reversible commands, and verify visual results.

## Standard Workflow

1. Load Affinity tools if they are not already present.
2. Read SDK documentation in this order:
   - Always read `preamble` first.
   - Call `list_sdk_documentation`.
   - Read only the topics needed for the task, such as `application.js`, `document.js`, `nodes.js`, `commands.js`, `geometry.js`, `colours.js`, `fills.js`, `linestyle.js`, `storybuilder.js`, `glyphatts.js`, `paragraphatts.js`, or `exportconfig.js`.
3. Inspect the current document before making changes.
4. Choose the narrowest edit: selected object first, current spread next, whole document only when requested.
5. Execute scripts with the Affinity MCP `execute_script` capability; a harness may expose a qualified tool name. Use `console.log(JSON.stringify(...))` for observable output.
6. Verify with `render_selection(document_session_uuid)` whenever the result is visual.
7. Do not save, export, flatten, delete broad selections, or resize the spread unless the user asked for that kind of change.

## Document Inspection

Use this baseline probe before editing:

```javascript
const {Document} = require('/document');
const doc = Document.current;
if (!doc) {
  console.log(JSON.stringify({ok: false, reason: 'NO_CURRENT_DOCUMENT'}));
} else {
  console.log(JSON.stringify({
    ok: true,
    title: doc.title,
    path: doc.path,
    sessionUuid: doc.sessionUuid,
    isReadOnly: doc.isReadOnly,
    isDirty: doc.isDirty,
    needsSaving: doc.needsSaving,
    pageCount: doc.pageCount,
    spreadCount: doc.spreadCount,
    selectedCount: doc.selection.nodes.length,
    currentSpreadBox: doc.currentSpread.baseBox
  }, null, 2));
}
```

Stop cleanly if `Document.current` is null or `doc.isReadOnly` is true.

## Object Operations

Use node operations for visible document objects:

- `doc.selection` returns the current selection.
- `doc.selection.nodes` gives selected nodes.
- `node.userDescription = '...'` is useful for naming automation-created objects.
- `doc.selectAll(false)` selects all document objects; use it deliberately because it changes selection.
- `doc.deleteSelection(selection)` deletes selected objects; only use when the user wants replacement or cleanup.
- `doc.setVisible(visible, selection)`, `doc.lockSelection(selection)`, and `doc.unlockSelection(selection)` operate through document commands.
- For new nodes, `doc.addNode(def, doc.currentSpread)` adds to the current spread and selects the new object.

Use descriptions and final selection intentionally so the user can inspect or undo the right thing.

## Geometry And Appearance

For basic shapes:

- Create a `ShapeNodeDefinition`.
- Set a shape, such as `ShapeRectangle.create()` or `ShapeEllipse.create()`.
- Set the bounding rectangle.
- Add it to the current spread.
- Apply fill and stroke to the resulting selection.

For exact freeform shapes:

- Build a closed path with `CurveBuilder`.
- Add it to a `PolyCurve`.
- Put it into `PolyCurveNodeDefinition`.
- Add it to the document.

For appearance:

- Use `RGBA8(r,g,b,a)` from `/colours`.
- Use `FillDescriptor.createSolid(colour)` for brush or pen fill.
- Use `FillDescriptor.createNone()` to remove fill or stroke.
- Use `/linestyle` and `doc.setLineStyleDescriptor(...)` when stroke weight, caps, joins, or alignment matter.

Read `references/affinity-js-patterns.md` for tested snippets.
Read `references/affinity-concepts-and-nuances.md` when the task requires choosing between Affinity object types, text modes, non-destructive techniques, or verification methods.

## Text Operations

Do not assume text node defaults exist. In current SDK usage, these fail:

- `FrameTextNodeDefinition.createDefault()`
- `ArtTextNodeDefinition.createDefault()`
- `TextNodeDefinition.createDefault()`

Use `StoryBuilder` plus `FrameTextNodeDefinition.createFromStoryBuilder(frameBox, storyBuilder)` or `ArtTextNodeDefinition.createFromStoryBuilder(point, storyBuilder)`:

- Set defaults with `sb.setToFrameTextDefaultStyle(doc.dpi, doc.format)`.
- For Artistic Text, set defaults with `sb.setToArtisticTextDefaultStyle(doc.dpi, doc.format)`.
- Configure `sb.glyphAtts` for font, height, fill, and optional spacing.
- Configure `sb.paragraphAtts` for alignment and explicit leading.
- Add text line by line.
- Use generous frame bounds, then render-check for clipping.
- Treat `glyph.characterSpacing` as an em-like value. Use small values such as `-0.02`, `0`, or `0.03`; values like `-1` or `-4` can collapse glyph advance and make characters appear stacked.

For existing selected text, read `commands.js` and `storydelta.js` before applying formatting commands such as `doc.formatText(...)`.

### Artistic Text vs Frame Text

Choose the text object type intentionally:

- Use Artistic Text for short display text, labels, numerals, titles, and poster-like fragments where the text box should hug the text content.
- Use Frame Text for paragraphs, fixed-width copy blocks, multi-line text areas, and text that needs a deliberately sized container.
- Frame Text has a container frame in the editing UI. That frame can be visually distracting while designing, but it is not part of the artwork/export unless an actual stroke/fill/decoration has been applied.
- For rotated labels, create Artistic Text first, retrieve the created node, rotate it with `DocumentCommand.createTransform(...)`, then measure `node.spreadVisibleBox` and translate it into place.
- If a user complains about boxes around all text, first check whether objects are selected and render the spread. If `render_spread` shows no boxes, explain that the boxes are UI overlays/text containers, not exported artwork.
- For visual verification of the full composition, prefer `render_spread` over `doc.selectAll(false)` plus `render_selection`, because selecting all objects can make UI selection boxes look like a design problem in the live app.

## Document Features

Prefer documented command helpers over ad hoc state mutation:

- Guides: `DocumentCommand.createAddGuide(...)`.
- Document/spread sizing: `doc.setSpreadSizeWithAnchor(...)`; remember this can affect layout.
- History: `doc.undo()`, `doc.redo()`, `doc.undoDescription`, `doc.redoDescription`.
- Export: read `document.js` and `exportconfig.js`; use `FileExportOptions` and `FileExportArea` intentionally.
- AI or image features: read `commands.js` first. Commands such as generate image, remove background, select subject, and generative edit may be restricted by Affinity settings; report `NOT_ALLOWED` clearly.

## Verification And Reporting

After a meaningful operation, report:

- What changed.
- Whether the current document is dirty or needs saving.
- Whether the result was visually verified.
- Any known limitation, such as text clipping risk, missing selection, restricted feature, or unsaved file.

Use `render_selection` for visual checks. If the task modifies a single object, leave that object selected; if it rebuilds a composition, select all relevant objects before rendering.

For whole-layout verification, use `render_spread` when available. This is the best default for checking whether a composition itself is clean, because selecting everything can introduce UI overlays that are not part of exported artwork.

## Learning Loop

When a new Affinity SDK lesson is discovered:

1. Confirm it with a small script or visual check.
2. If the MCP exposes `add_sdk_hint`, add a concise entry for future sessions.
3. Update this skill only when the lesson is general enough to apply beyond the immediate artifact.

Keep this skill about manipulation of Affinity objects and features. Treat poster or layout recreation as one application of those primitives, not as the center of the skill.
