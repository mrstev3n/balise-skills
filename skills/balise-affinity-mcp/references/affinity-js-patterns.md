# Affinity JavaScript Patterns

These snippets are starting points for scripts executed through the Affinity MCP `execute_script` capability. A harness may expose a qualified tool name. Always read the SDK `preamble` and relevant docs first.

## Inspect Current Document

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
    selectedCount: doc.selection.nodes.length,
    currentSpreadBox: doc.currentSpread.baseBox
  }, null, 2));
}
```

## Add A Filled Rectangle

```javascript
const {Document} = require('/document');
const {ShapeNodeDefinition} = require('/nodes');
const {ShapeRectangle} = require('/shapes');
const {RGBA8} = require('/colours');
const {FillDescriptor} = require('/fills');

const doc = Document.current;
const def = ShapeNodeDefinition.createDefault();
def.setShape(ShapeRectangle.create());
def.setBoundingRectangle({x: 100, y: 100, width: 240, height: 160});
doc.addNode(def, doc.currentSpread);
doc.setBrushFillDescriptor(FillDescriptor.createSolid(RGBA8(0, 122, 255, 255)), doc.selection);
doc.setPenFillDescriptor(FillDescriptor.createNone(), doc.selection);
doc.selection.nodes.first.userDescription = 'Created by Affinity MCP automation';
console.log(JSON.stringify({ok: true, sessionUuid: doc.sessionUuid}));
```

## Add A Polygon Or Triangle

```javascript
const {Document} = require('/document');
const {PolyCurveNodeDefinition} = require('/nodes');
const {CurveBuilder, PolyCurve} = require('/geometry');
const {RGBA8} = require('/colours');
const {FillDescriptor} = require('/fills');

const doc = Document.current;
const builder = CurveBuilder.create();
builder.beginXY(100, 100);
builder.lineToXY(320, 100);
builder.lineToXY(100, 260);
builder.close();

const poly = PolyCurve.create();
poly.addCurve(builder.createCurve());

const def = PolyCurveNodeDefinition.createDefault();
def.setCurves(poly);
doc.addNode(def, doc.currentSpread);
doc.setBrushFillDescriptor(FillDescriptor.createSolid(RGBA8(237, 164, 180, 255)), doc.selection);
doc.setPenFillDescriptor(FillDescriptor.createNone(), doc.selection);
console.log(JSON.stringify({ok: true, sessionUuid: doc.sessionUuid}));
```

## Add Frame Text

```javascript
const {Document} = require('/document');
const {FrameTextNodeDefinition} = require('/nodes');
const {StoryBuilder} = require('/storybuilder');
const {ParagraphLeadingType, ParagraphAlignXType} = require('/paragraphatts');
const {Font, FontWeight, FontWidth} = require('/fonts');
const {RGBA8} = require('/colours');
const {FillDescriptor} = require('/fills');

const doc = Document.current;
const sb = StoryBuilder.create();
sb.setToFrameTextDefaultStyle(doc.dpi, doc.format);

const ga = sb.glyphAtts;
ga.font = Font.create('Arial', FontWeight.Bold, false, FontWidth.Normal);
ga.height = 72;
ga.brushFill = FillDescriptor.createSolid(RGBA8(42, 43, 48, 255));
sb.setGlyphAtts(ga);

const pa = sb.paragraphAtts;
pa.alignXType = ParagraphAlignXType.Left;
pa.leadingType = ParagraphLeadingType.Absolute;
pa.absoluteLeading = 64;
sb.setParagraphAtts(pa);

for (const [i, line] of ['AFFINITY', 'MCP', 'TEST'].entries()) {
  if (i > 0) sb.addParagraphBreak();
  sb.addText(line);
}

const def = FrameTextNodeDefinition.createFromStoryBuilder(
  {x: 100, y: 100, width: 500, height: 260},
  sb
);
doc.addNode(def, doc.currentSpread);
console.log(JSON.stringify({ok: true, sessionUuid: doc.sessionUuid}));
```


## Add And Rotate Artistic Text

```javascript
const {Document} = require('/document');
const {ArtTextNodeDefinition} = require('/nodes');
const {StoryBuilder} = require('/storybuilder');
const {Selection} = require('/selections');
const {DocumentCommand, AddChildNodesCommandBuilder, NodeChildType} = require('/commands');
const {Transform} = require('/geometry');
const {Font, FontWeight, FontWidth} = require('/fonts');
const {RGBA8} = require('/colours');
const {FillDescriptor} = require('/fills');

const doc = Document.current;
const sb = StoryBuilder.create();
sb.setToArtisticTextDefaultStyle(doc.dpi, doc.format);

const ga = sb.glyphAtts;
ga.font = Font.create('Arial', FontWeight.Bold, false, FontWidth.Normal);
ga.height = 72;
ga.brushFill = FillDescriptor.createSolid(RGBA8(42, 43, 48, 255));
// characterSpacing is em-like. Keep values small: -0.02, 0, 0.03.
ga.characterSpacing = -0.02;
sb.setGlyphAtts(ga);
sb.addText('JULIO');

const def = ArtTextNodeDefinition.createFromStoryBuilder({x: 0, y: 0}, sb);
const builder = AddChildNodesCommandBuilder.create();
builder.addNode(def);
const cmd = builder.createCommand(true, NodeChildType.Main);
doc.executeCommand(cmd);

const node = cmd.newNodes[0] || doc.selection.firstNode;
node.userDescription = 'Rotated artistic text';
const selection = Selection.create(doc, node, true);

const box = node.spreadVisibleBox;
const cx = box.x + box.width / 2;
const cy = box.y + box.height / 2;
const rotate = Transform.createTranslate(cx, cy)
  .multiply(Transform.createRotate(-90 * Math.PI / 180))
  .multiply(Transform.createTranslate(-cx, -cy));
doc.executeCommand(DocumentCommand.createTransform(selection, rotate, {mergeable: false, correctChildren: true}));

const afterRotate = node.spreadVisibleBox;
const move = Transform.createTranslate(300 - afterRotate.x, 300 - afterRotate.y);
doc.executeCommand(DocumentCommand.createTransform(selection, move, {mergeable: false, correctChildren: true}));
console.log(JSON.stringify({ok: true, box: node.spreadVisibleBox, sessionUuid: doc.sessionUuid}));
```

## Visual Verification

For one object, leave the target node selected and call:

```json
{"document_session_uuid":"<doc.sessionUuid>"}
```

with the Affinity MCP `render_selection` capability.

For a full composition, prefer the Affinity MCP `render_spread` capability:

```json
{"document_session_uuid":"<doc.sessionUuid>","spread_index":0}
```

This avoids selecting all objects just to inspect the design. It is especially useful with Frame Text, because selected text frames can make UI boxes look like exported artwork even when the exported spread is clean.
