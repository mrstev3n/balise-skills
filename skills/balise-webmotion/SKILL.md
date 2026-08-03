---
name: balise-webmotion
description: Research, direct, collect resources for, and build Awwwards-level web motion. Use for motion inspiration, moodboards, reference or competitor research, interaction reproduction, animation direction, scroll storytelling, page transitions, micro-interactions, easter eggs, animated assets, or a fast motion prototype; also use before building an ambitious landing page, portfolio, hero, microsite, campaign, or product surface, and when existing motion feels generic, flat, or dated. Guide users who want to arbitrate, and autonomously choose tools, acquire or generate assets, and prototype when the user asks for speed, delegates decisions, or lacks motion expertise.
---

# Webmotion

Set an award-level motion direction, then carry it into a working prototype. Research and production are one loop: inspect, choose, collect, build, compare, refine. Do not stop at advice when the user expects execution.

## Load only what the task needs

- [references/research-method.md](references/research-method.md) — image/video/live capture, temporal decomposition, compact research, and stop conditions. Load for reference research or reproduction.
- [references/source-strategy.md](references/source-strategy.md) — source roles, platforms, and Browser/Computer Use/MCP/CLI collection routes. Load before external research or asset acquisition.
- [references/asset-acquisition.md](references/asset-acquisition.md) — portable image generation, provider routing, dependency setup, chroma key, transparency, and web delivery. Load before creating, acquiring, installing tooling for, or cutting out still-image assets.
- [references/autonomous-production.md](references/autonomous-production.md) — capability inventory, tool choice, asset acquisition, and prototype loop. Load for autonomous or hybrid production.
- [references/quality-rubric.md](references/quality-rubric.md) — measurable Awwwards-level quality gate. Load before acceptance criteria, self-review, or final review.
- [references/micro-interactions.md](references/micro-interactions.md) — compact micro-interaction catalog.
- [references/easter-eggs.md](references/easter-eggs.md) — optional surprise layer and its constraints.
- [assets/webmotion-reference-brief.md](assets/webmotion-reference-brief.md) — optional compact handoff template. Use only when a durable brief is useful.

## Choose the operating mode

Inspect the project, stack, brand, code, and assets before asking anything. Ask at most three questions, only when the answers would materially change or block the work.

1. **Guided mode.** Use when the user asks for options, research, a moodboard, or wants to arbitrate. Present up to three distinct directions, recommend one, and wait only at the explicit decision gate.
2. **Autonomous mode.** Use when the user asks for a fast prototype, says to choose, provides a vague brief, or clearly lacks motion vocabulary. Choose the direction, sources, stack, assets, fallbacks, and prototype scope; explain decisions after making progress.
3. **Hybrid mode — default.** Recommend one direction, explain it briefly, and begin the smallest useful implementation. Surface alternatives only when they represent a meaningful tradeoff.

Explicit user intent overrides inference. Never make a novice design the process through a long questionnaire.

## Creative doctrine: capter → adapter → transformer → surpasser

Treat public references as creative material. Choose either route, or combine them:

- **Rendered artifact:** inspect an image, video, screen recording, or live site; reconstruct timing, easing, layering, state, camera, and interaction.
- **Accessible source:** copy a public prompt, snippet, component, shader, or boilerplate; adapt its code and behavior to the project.

A faithful reprise is acceptable when requested. Otherwise improve the result through context, combination, or execution. Check asset usage terms only when integrating or redistributing the asset; do not turn that check into a research dossier.

## Core workflow

### 1. Inspect and frame

- Determine the surface, user action, narrative goal, desired feeling, stack, devices, and constraints from available evidence.
- State one motion thesis tying behavior to brand or narrative.
- Choose guided, autonomous, or hybrid mode.

### 2. Choose source roles

- Name the material needed: quality reference, prompt, code component, interaction pattern, shader/material, video, vector animation, sound, or technical proof.
- Select complementary sources by role, not by a permanent ranking. No platform is the default source.
- Load [references/source-strategy.md](references/source-strategy.md) and choose the cheapest viable collection route.

### 3. Collect or reconstruct

- Prefer an available MCP or existing CLI when it returns inspectable material efficiently.
- Use Browser or Computer Use for visual search, filters, previews, copy buttons, downloads, and sites that expose no suitable API.
- Copy useful prompts, snippets, code, assets, or URLs; adapt them immediately rather than building a source archive.
- Reconstruct the observable mechanism when the original material cannot be acquired.
- When a custom still image is needed, load [references/asset-acquisition.md](references/asset-acquisition.md), inspect live capabilities, and install the reversible local cutout runtime when authorized and useful.

### 4. Build

- Load [references/autonomous-production.md](references/autonomous-production.md).
- Select the smallest combination that can deliver the chosen choreography.
- Build the signature moment first, then the necessary interaction system and responsive/reduced-motion variants.
- Use available specialist capabilities when they help, but remain able to continue with direct implementation when they are absent.

### 5. Compare and refine

- Compare the prototype against the useful temporal and visual properties of the references.
- Test interruption, repeat use, touch, keyboard, responsive behavior, reduced motion, and target-device performance where relevant.
- Load the quality rubric, correct material gaps, generic timing, dead sections, and weak fallbacks.
- Request an independent animation review when such a capability is available. Otherwise apply the bundled quality rubric, report that the review was self-performed, and keep independent review as an open follow-up.

## Research depth

- **Lightweight:** one thesis, one signature behavior, one implementation route. Use for opportunistic activation and fast prototypes.
- **Focused:** inspect a few complementary references and acquire only the material needed for the current surface. This is the default.
- **Deep:** use temporal capture, multiple directions, and a durable brief only for complex immersive work or when explicitly requested.

Do not require a reference for every decision. Stop researching when the next uncertainty is best resolved by a prototype.

## Capability routing

Choose behavior first, then route it through capabilities actually available in the harness.

| Need | Preferred capability | Fallback or source |
| --- | --- | --- |
| Tweens, timelines, stagger | GSAP | Native Web Animations API or CSS keyframes |
| Scroll choreography | ScrollTrigger or native scroll timelines | Intersection Observer and CSS scroll-driven animations |
| React springs, layout, gestures | Motion | Framework-native transitions or direct pointer handling |
| 3D, shaders, particles, camera | Three.js, R3F, GLSL | Inspectable demos or a minimal WebGL implementation |
| Interactive vector state machine | Rive | Rive runtime/community, connector if available |
| Vector sequence or loop | Lottie | LottieFiles, Lottie runtime |
| Components, prompts, snippets | Component platforms | 21st.dev, MotionSites, Magic UI, BuouUI, Kinetics |
| Animated backgrounds or footage | Asset platforms | MotionSites, Videezy, generated media |
| Custom imagery, textures, environments | Live image capability inventory | Native generation, Magnific, Higgsfield, another available image capability, or local fabrication |
| Reconstruct a visible effect | Browser capture and local implementation | Temporal decomposition from screenshots or recordings |
| Sound feedback | Opt-in web audio | Native Web Audio API with a silent fallback |
| Performance and accessibility | Measurement and fallbacks | Browser profiling, reduced motion, keyboard and touch checks |

If a preferred capability is absent, use an existing CLI, official runtime or documentation, browser inspection, or direct local implementation. Offer an official connector or the packaged local image pipeline only when it materially improves the work and the required authorization is available. Never claim to have used a tool that was not exposed.

## Craft invariants

- Declare 2–4 project easing curves; do not leak inconsistent library defaults.
- Treat duration bands as starting points: micro 100–300 ms, UI 200–500 ms, narrative 600 ms–2 s, spectacle 1–4 s, ambient continuous and pausable.
- Use deliberate overlap and origin-aware stagger; avoid mechanical reveal queues.
- Define a motion budget: simultaneous elements, spectacle moments, animated asset weight, and mobile GPU tolerance.
- Measure performance rather than assuming it. Prefer transform/opacity and design fallbacks for expensive media or 3D.
- Design reduced motion as an alternative that preserves information and hierarchy.
- Use preloaders only for real loading. Never autoplay audio.
- Keep frequent interactions fast and restrained; reserve spectacle for rare moments.

## Deliver without bureaucracy

Match the deliverable to the work completed. Default to:

1. motion thesis and chosen direction;
2. resources actually used, without author or provenance log;
3. stack and asset decisions;
4. prototype or implementation produced;
5. verification performed and remaining risks.

Add comparison boards, detailed motion maps, or the handoff template only when they materially help the user or another implementer.
