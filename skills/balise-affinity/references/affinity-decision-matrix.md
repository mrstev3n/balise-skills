# Affinity Decision Matrix

Use this matrix to choose the right concept before suggesting an Affinity action or MCP script.

## Text

| User intent | Prefer | Check |
| --- | --- | --- |
| Title, logo word, short label, number | Artistic Text | Does it need rotation, scaling, or tight bounds? |
| Paragraph or caption block | Frame Text | Does the frame size, inset, or overflow matter? |
| Long document typography | Text styles | Are paragraph and character styles needed? |
| Text appears boxed in UI | Render spread before editing | Is it only a selection/frame overlay? |

## Shapes And Paths

| User intent | Prefer | Check |
| --- | --- | --- |
| Simple rectangle, ellipse, star, etc. | Shape primitive | Does editability of primitive controls matter? |
| Custom outline | Curve or polycurve | Are nodes, joins, and closed paths correct? |
| Combine shapes editably | Compound boolean if available | Must original shapes remain editable? |
| Final static icon | Expanded curves may be acceptable | Has the user asked for finalization? |

## Images And Pixels

| User intent | Prefer | Check |
| --- | --- | --- |
| Hide part of an image | Mask or clipping | Can source pixels stay intact? |
| Retouch photo | Pixel tools or live filters | Is a destructive edit avoidable? |
| Place image in layout | Picture frame or placed image | Does crop need to remain adjustable? |
| Background removal or subject selection | Built-in AI/ML if available | Is the command allowed in current settings? |

## Reuse And Systems

| User intent | Prefer | Check |
| --- | --- | --- |
| Repeated component | Symbol | Should all instances update together? |
| Theme color | Global color or swatch | Does the color need central control? |
| Repeated typography | Text style | Is this paragraph-level or character-level? |
| UI variants | Artboards | Is each state/export target distinct? |

## Verification

| Claim to verify | Prefer | Why |
| --- | --- | --- |
| Document exists and is editable | Document JSON probe | Fast and non-visual. |
| One object changed correctly | Render selection | Focused feedback. |
| Whole composition looks right | Render spread | Avoids selection overlays. |
| Export output is correct | Export then inspect output | Required for file-format claims. |
| Text boxes are real artwork | Render spread | Separates UI containers from output. |

## Automation Safety

Default to:

- inspect first
- read SDK docs before command use
- edit selected objects when possible
- tag generated nodes with descriptions
- delete only explicitly identified nodes
- report dirty state and verification status

Avoid:

- broad deletes
- flattening/rasterizing without request
- treating UI overlays as document objects
- assuming a UI feature exists in the MCP SDK
- using unverified exact shortcuts or version claims
