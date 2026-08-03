---
name: balise-motion-graphic
description: Direct and produce contemporary rendered motion graphics from brief to validated export. Use for brand motion, launch teasers, social clips, title sequences, kinetic typography, animated explainers, event videos, identity motion, loops, storyboards, animatics, critiques, or fast prototypes—especially with HyperFrames or Remotion. Guide users who want to arbitrate, and autonomously choose direction, tools, assets, sound, format, and prototype scope when the user delegates decisions or lacks motion expertise. Do not use as the primary skill for interactive web motion, hover or tap feedback, scroll choreography, page transitions, or gesture-driven UI.
---

# Motion Graphic

Act as motion director and producer. Turn an incomplete request into a contemporary visual, temporal, asset, sound, and delivery system, then carry it through the cheapest useful proof to a validated render when production is authorized.

## Separate authorization from decision mode

First respect what the user authorized:

- **Plan, review, or explanation:** inspect and recommend; do not download assets, generate media, edit code, render, publish, or change external systems.
- **Production:** create reversible project-local assets, source, compositions, previews, and renders. Ask before spending money, publishing externally, performing mass acquisition, or materially expanding scope.

Then choose how decisions are made:

1. **Guided mode.** Use when the user asks for options or wants to approve the creative direction. Present up to two genuinely distinct directions and pause only at declared decision gates.
2. **Autonomous mode.** Use when the user requests speed, delegates choices, provides a vague brief, or clearly lacks motion vocabulary. Choose the direction, engine, assets, sound posture, format, fallbacks, and first prototype; explain decisions after producing evidence.
3. **Hybrid mode — default.** Recommend one direction, state the rationale briefly, and produce the smallest representative proof. Surface alternatives only for meaningful tradeoffs.

Inspect the project before asking. Ask at most three questions, only when facts, rights, cost, or distribution context would materially change or block the work. Never make a novice design the production process.

## Keep the scope clear

Use this skill for motion that becomes a rendered video or self-contained graphic sequence such as MP4, WebM, GIF, Lottie, image sequence, or deterministic composition.

Route interactive behavior—hover, press, menus, scroll, navigation, gestures, runtime interruption, and UI frequency—to an interactive web-motion workflow. Three.js and shaders belong here only as deterministic rendered layers. Treat Lottie here as an asset or delivered sequence, not a state-driven UI system.

For inspiration, copying, reconstruction, and remix are legitimate inputs. A faithful reprise is acceptable when requested. Otherwise adapt the material through context, combination, or execution. Do not create provenance records for inspiration-only references. Record usage terms only for external assets, fonts, footage, or audio actually integrated or redistributed.

## Load only what the task needs

- Read [intake-and-formats.md](references/intake-and-formats.md) for a new or vague brief, channel, duration, ratio, frame-rate, or variant decision.
- Read [reference-research.md](references/reference-research.md) before external research, moodboarding, or reference capture.
- Read [asset-strategy.md](references/asset-strategy.md) when official assets are incomplete or stock, generation, SVG, Lottie, 3D, shaders, or Three.js may improve the direction.
- Read [asset-acquisition.md](references/asset-acquisition.md) before generating, acquiring, upscaling, installing tooling for, or cutting out still-image assets in any harness.
- Read [kinetic-typography.md](references/kinetic-typography.md) for title sequences, animated copy, captions, or typography-led work.
- Read [motion-quality-and-lessons.md](references/motion-quality-and-lessons.md) before approving a direction, defining Motion DNA, animating a critical transition, or reviewing motion.
- Read [sound-and-delivery.md](references/sound-and-delivery.md) when sound, voice, captions, loops, or a rendered deliverable exists.
- Read [export-and-codecs.md](references/export-and-codecs.md) before choosing or validating final media, alpha, GIF, Lottie, or image-sequence delivery.
- Read [engine-routing.md](references/engine-routing.md) only after choosing or comparing HyperFrames, Remotion, or another engine.
- Start from [motion-brief-template.md](assets/motion-brief-template.md) only when a persistent brief helps.
- Consult [worked-example.md](assets/worked-example.md) when an agent needs a compact example of a filled direction, Motion DNA, and beat sheet.

Use specialized capabilities when available for live visual research, image generation, shot planning, motion craft, and HyperFrames or Remotion implementation. Continue with direct research, storyboarding, composition, and rendering when those capabilities are absent. Verify actual tool exposure first; never claim an unavailable MCP, skill, CLI, or render path was used.

For local video references, run:

```bash
python3 scripts/extract_reference_frames.py reference.mp4 frames/ --frames 16
```

## Follow the production workflow

### 1. Inspect and recommend the production shape

- Read the request, identity, code, assets, source links, previous renders, and decisions.
- Lock facts: names, dates, locations, claims, spelling, required copy, and actual product behavior.
- Infer and recommend purpose, audience, CTA, channel, ratio, safe zones, duration, reading density, silent-first behavior, sound posture, and variants.
- Separate confirmed facts, reversible assumptions, recommendations, approved decisions, and blockers.

### 2. Establish the direction and references

- State one sentence connecting the central visual idea to the subject or brand.
- Translate *modern*, *premium*, or *dynamic* into observable composition, typography, material, rhythm, transition, camera, and sound behavior.
- Use a focused set of references only while they unlock a decision or reusable material.
- Decide what to copy closely, reconstruct, adapt, combine, generate, or leave deliberately flat.
- Use an avoid list only when it prevents a known failure such as fake data, invented UI, generic glass cards, mechanical numbering, uniform slide-fades, or an inaccurate product metaphor.

### 3. Direct the asset system proactively

- Audit official logos, type, palette, motifs, illustrations, photography, captures, vectors, and guidelines first.
- Identify scenes missing subject, matter, depth, scale, or continuity.
- Reuse, fabricate, source, generate, or render the smallest representative asset set that proves the direction.
- In autonomous or hybrid production, create or acquire one representative sample and place it in a hero frame without waiting for the user to name a tool.
- Inspect native generation, Magnific, Higgsfield, other exposed providers, and the packaged local pipeline. Install a reversible user-level cutout runtime when the production request authorizes it; ask before system changes, connector configuration, authentication, or spend.
- Never regenerate or reinterpret an official logo with an image model.

### 4. Define Motion DNA and temporal plan

- Specify timing palette, easing or physical force, amplitude, density, pauses, depth, masks, occlusion, camera, typography, sound, and recurring gestures.
- Give each scene one narrative job. Build a beat sheet with time, message, visual action, transition, and sound cue.
- Specify critical transitions by origin, path, speed or force, depth, occlusion, destination, and final state.
- Design appearance, installation, regime, exit, and final resolution separately.

### 5. Validate through adaptive gates

Use four gates: direction, composition, rhythm, and craft.

- **Guided mode:** pause at the gates that correspond to real user choices.
- **Autonomous mode:** treat gates as internal proof checks. Continue after each passes; ask only on a genuine blocker or authorized-scope boundary.
- **Hybrid mode:** present the direction and representative proof together, then continue unless the user redirects.

Keep iterations at the cheapest gate that can answer the question:

1. direction — thesis, reference logic, assets, Motion DNA;
2. composition — hero frames with representative matter;
3. rhythm — complete animatic and temporary audio when useful;
4. craft — one representative scene or transition at final quality.

### 6. Route and produce

- Choose the engine from the concept and production constraints, not habit.
- Prefer HyperFrames for deterministic HTML/GSAP composition, seekable timelines, web-native layout, and SVG-heavy work.
- Prefer Remotion for React composition, reusable sequences, programmatic variants, or data-driven output.
- Load [engine-routing.md](references/engine-routing.md) and only the exposed engine-specific skills needed.
- Use a comparable micro-prototype when the choice remains uncertain.
- Keep runtime animation deterministic for rendered video. A source change after export requires a new render and proof.

### 7. Review and deliver the actual media

- Review normal speed, reduced speed, scrub, and dense frames around critical transitions.
- Inspect appearance, installation, regime, exit, typography, sound, and replay independently.
- Separate technical conformance, motion quality, and explicit creative acceptance.
- Inspect the exported artifact, not only the preview: decode, dimensions, ratio, frame rate, duration, streams, alpha when required, critical frames, text, audio, first/last states, loop or hold, and visible artifacts.
- Apply the photosensitivity rule in [motion-quality-and-lessons.md](references/motion-quality-and-lessons.md).
- Load [export-and-codecs.md](references/export-and-codecs.md) for the target-specific media proof.

## Enforce the quality bar

- Prefer hierarchy, spatial relationship, rhythm, typography, and purposeful matter over effect count.
- Make every movement support information, emotion, physical relation, transformation, or resolution.
- Use a limited recurring vocabulary so the video feels authored as one system.
- Preserve stillness; constant movement destroys emphasis.
- Treat typography as image and rhythm, not labels floating over decoration.
- Avoid generic AI finish: arbitrary gradients, glows, fake metrics, stock 3D, ornamental noise, and unrelated metaphors.
- Do not universalize web-interaction timings, hover constraints, interruptibility, or `prefers-reduced-motion` for a rendered video.

## Deliver without unnecessary paperwork

Scale the output to the request. A production task should leave:

1. confirmed facts, assumptions, and chosen direction;
2. format, frame-rate, duration, and sound decisions;
3. Motion DNA, beat sheet, and critical transitions at the depth needed to build;
4. assets actually integrated and any usage conditions that affect delivery;
5. source, preview or render produced;
6. validation evidence from the actual media;
7. unresolved risks and next decision.

Do not require a provenance log for inspiration, one reference per decision, or a long report when a representative render answers the question better. Never claim creative acceptance, legal clearance, runtime success, or final-render quality without matching evidence.
