# Engine routing

Use this reference only after the common direction, beat sheet, asset strategy, and proof plan exist.

## Engine-neutral contract

Before implementation, define format, duration, frame rate, variants, scene ranges, hero frames, assets, Motion DNA, transitions, audio/captions, and validation gates. The engine implements this contract; it does not redefine the direction.

## HyperFrames route

Prefer HyperFrames for deterministic HTML/GSAP composition, seekable timelines, web-native layout, and SVG-heavy work.

Inspect actual exposure. When available, load the HyperFrames plugin skills `hyperframes` and `hyperframes-cli`; add `hyperframes-registry`, `gsap`, or other exposed companion skills only when the task needs them. `create-hyperframes-launch` may help structure a launch artifact but does not replace engine authoring guidance.

Map scenes to clips or composition sections, beats to seekable positions, hero frames to timecodes, audio to explicit cues, transitions to dense frame inspection, and final proof to the available lint/validate/preview/render/decode workflow.

Treat engine defaults as implementation constraints, not universal taste. Do not force every element to enter, ban cuts, require a fixed number of easings, or animate merely because the engine can.

## Remotion route

Prefer Remotion for React components, reusable sequences, data-driven variants, programmatic composition, or batch rendering.

Inspect actual exposure. Start with `remotion-best-practices`, then load only what is needed: `remotion-create`, `remotion-render`, `remotion-multimedia`, `remotion-captions`, `remotion-docs`, or another exposed specialist.

Map scenes to compositions and deterministic sequences, beats to frame ranges, motion to frame-derived values, assets/copy to explicit props or data, and audio/captions to frame-aligned components. Test representative variants and extreme content before final render.

Do not introduce browser-clock, `requestAnimationFrame`, or runtime-only animation without proving deterministic output at arbitrary frames. Seed pseudo-random variation. Treat Motion.dev examples as craft references, not automatically safe Remotion primitives.

## Other engines

Use the same contract and load the engine's own skill or primary documentation. Verify renderer availability, determinism, media support, and evidence surfaces. If no engine is available, deliver the approved brief and exact handoff rather than pretending a render exists.

## Comparison rule

When the engine choice is consequential and unclear, build the same small scene or transition in each realistic candidate. Compare visual fidelity, temporal control, determinism, asset/audio support, iteration cost, render reliability, maintenance, and variants. Do not declare one engine generally superior from a single success.

## Boundary with Webmotion

Route to an interactive web-motion workflow when the primary outcome depends on user input, scroll, navigation, hover, gestures, runtime interruption, interactive performance, or interactive accessibility. Three.js belongs here only for deterministic rendered footage; an interactive scene belongs in the web experience. Lottie belongs here as a produced or consumed sequence; state-driven UI belongs in the interactive implementation.

The research doctrine differs only at delivery: neither skill needs provenance records for inspiration. Motion Graphic records usage terms for external assets and audio actually integrated into a redistributed render; Webmotion applies the same check only when an external asset is integrated or redistributed.
