---
name: balise-affinity
description: Understand, audit, and reason about Affinity by Canva documents, workflows, object choices, text modes, UI overlays, non-destructive editing, production setup, and composition practices. Use when the user asks for Affinity concepts, best practices, critique, document strategy, workflow guidance, or whether an Affinity MCP automation approach is appropriate.
---

# Affinity Design Literacy

Use this skill for Affinity reasoning before automation. It helps choose the right Affinity concept, object type, workflow, and verification method. It is complementary to `balise-affinity-mcp`, which executes changes through the MCP.

## Core Posture

Treat Affinity as a unified creative environment with vector, pixel, and layout capabilities in one document. Before recommending an action, identify the user's intent:

- create or edit vector artwork
- retouch or manipulate pixels
- structure a layout or publication
- build reusable design systems
- prepare exportable assets
- diagnose a visual or UI-state issue
- automate through MCP

Do not reduce Affinity work to poster recreation. Posters are only one possible composition use case.

## Reference Routing

- Read `references/affinity-mental-model.md` for architecture, Studios, object model, and workflow decisions.
- Read `references/affinity-decision-matrix.md` for concrete object and verification choices.
- If the answer requires live document manipulation, switch to `balise-affinity-mcp` and follow its SDK-first workflow.

## Reasoning Rules

1. Separate what is artwork from what is Affinity UI state.
2. Prefer non-destructive workflows unless final flattening is explicitly requested.
3. Prefer reusable systems for repeated design elements: symbols, text styles, global colors, assets, and named groups.
4. Choose text mode deliberately: Artistic Text for display fragments, Frame Text for layout containers.
5. Use artboards/pages/spreads for variants, screen states, and multi-page work instead of separate files when a shared system matters.
6. Treat exact feature names, AI tools, shortcuts, and version-specific behavior as verify-first details.
7. When the user wants a detailed synthesis, prefer HTML over long Markdown.

## Output Expectations

For audits or strategy:

- classify findings by concept area
- explain practical impact
- recommend the safest Affinity-native approach
- identify what should be verified through MCP or visual render

For automation planning:

- name the relevant Affinity concepts
- describe the object model to inspect
- identify the narrowest safe edit
- state the visual verification method

For learning capture:

- extract durable lessons
- mark volatile claims
- suggest which reference file should absorb the lesson
