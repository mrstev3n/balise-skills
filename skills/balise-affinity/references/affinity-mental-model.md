# Affinity Mental Model

Affinity is best understood as a unified creative workspace where vector, pixel, and layout objects can coexist in one document. The user may describe this through older product names, newer Studio or Persona names, or practical tasks such as logo design, photo retouching, or page layout.

## Architecture

- Vector work focuses on scalable paths, shapes, typography, icons, UI assets, and illustration.
- Pixel work focuses on raster images, selection, retouching, painting, adjustments, and compositing.
- Layout work focuses on pages, spreads, text frames, picture frames, tables, master-like structures, and export for print or digital documents.

The active Studio changes the visible tools and panels. It should not be treated as proof that the document contains only one kind of content.

## Document Objects

Affinity documents can contain:

- vector shapes and curves
- text nodes
- pixel layers and placed images
- masks and clipping structures
- adjustment and live filter layers
- groups and nested groups
- symbols and reusable components
- artboards, pages, spreads, and picture frames

For MCP work, inspect the live document model instead of relying only on interface descriptions.

## Non-Destructive Philosophy

Affinity rewards reversible composition:

- use masks instead of erasing source pixels
- use live filters instead of destructive effects
- preserve editable vectors when possible
- keep repeated elements linked or systematically named
- delay flattening, rasterizing, and broad export-only conversions until the user asks

This matters for automation because reversible structures give future scripts stable targets.

## System Design Features

For reusable design:

- Global colors support theme-level color changes.
- Symbols support repeated components and motifs.
- Text styles support typography consistency.
- Assets support reusable libraries.
- Constraints support responsive behavior inside parent containers.
- Artboards support variants, screen states, and export units.

Use these when the design is expected to evolve.

## Production Thinking

Before export, clarify the target:

- web or app asset
- transparent raster image
- SVG or scalable vector
- print PDF
- multipage publication
- handoff file for another designer

The target controls color model, DPI, bleed, slicing, page/spread handling, and whether an export check is required.

## Verify-First Areas

Some information is time-sensitive or context-sensitive:

- exact version number and feature availability
- AI tool access and account restrictions
- keyboard shortcuts
- precise names of Studios or Personas in the user's installed version
- whether a UI command is exposed by the MCP SDK
