# Autonomous Webmotion production

Load this file in autonomous or hybrid mode, or whenever the task should continue from direction into a working prototype.

## Contents

1. Capability inventory
2. Decision rules
3. Asset acquisition
4. Prototype loop
5. Verification and failure routes

## Capability inventory

Inspect before choosing:

- current project stack, package manager, scripts, component system, and motion dependencies;
- available skills and MCP tools;
- Browser or Computer Use availability;
- installed official CLIs and authenticated task-relevant services;
- existing assets, design tokens, target routes, and build constraints.

Do not ask the user to enumerate tools that can be discovered. Do not claim an MCP, CLI, account, or runtime is available until verified.

## Decision rules

1. Preserve the existing stack unless the signature behavior requires a missing capability.
2. Choose the smallest combination that can deliver the motion thesis and fallback.
3. Prefer a real reusable component or asset over rebuilding it when adaptation is cheaper and quality remains high.
4. Prefer direct implementation or reconstruction when external tooling adds friction or the behavior is project-specific.
5. In autonomous mode, make reversible decisions and continue. Ask only before spending money, changing external account configuration, publishing, or making a choice that materially changes product scope.
6. In guided mode, provide up to three options and one recommendation at the declared gate.

Suggested routing:

- CSS/WAAPI/View Transitions for small native interactions;
- Motion for React layout, springs, and gestures;
- GSAP for complex timelines, ScrollTrigger, and choreography;
- Three.js/R3F/GLSL for spatial, material, shader, particle, or camera work;
- Rive for authored interactive vector state machines;
- Lottie for lightweight vector sequences;
- video/frame sequences for cinematic playback that does not require procedural interaction.

## Asset acquisition

- Load [asset-acquisition.md](asset-acquisition.md) for still-image generation, provider choice, dependency setup, transparent cutouts, or raster delivery.
- Select the asset role first: subject, texture, environment, loop, overlay, icon sequence, state machine, sound, or shader.
- Search the relevant sources using MCP, CLI, Browser, or Computer Use according to [source-strategy.md](source-strategy.md).
- Use accessible free material when budget and credentials are unknown.
- Use an existing authorized premium account when it is already available and the task permits it.
- Download or install only the candidates needed for the current prototype.
- Generate transparent objects, backgrounds, environments, textures, or motion substrates when stock material is weak.
- Place acquired/generated files in the project’s existing asset structure. Do not create a provenance log.
- Check usage terms only before integrating or redistributing an external asset whose conditions matter.
- If the local cutout backend is missing and a user-level install is authorized by the production request, run the packaged setup. Ask before system installation, administrator privileges, connector configuration, account authentication, or paid generation.

## Prototype loop

### 1. Establish the vertical slice

- Choose one signature moment that proves direction, material, timing, and stack.
- Define its initial state, trigger, transformation, settled state, interruption, mobile behavior, and reduced-motion alternative.
- Set a performance and asset-weight budget appropriate to the project.

### 2. Implement in the existing project

- Reuse design tokens, components, layout, and build scripts.
- Add the smallest dependency only when the existing stack cannot express the behavior robustly.
- Integrate collected snippets/components as project code, adapting imports, tokens, accessibility, responsiveness, and cleanup.
- Integrate or generate the minimum asset set needed to judge the composition.

### 3. Expand the motion system

- Apply shared easings, durations, and interaction physics.
- Add secondary micro-interactions that support the signature.
- Add scroll narrative, ambient layers, sound, or easter eggs only when they strengthen the thesis.
- Ensure the rest of the page does not feel dead beside a spectacular hero.

### 4. Compare and refine

- Compare the working behavior with the reference’s useful timing, layering, material, camera, and response.
- Correct weak spacing, generic easing, abrupt continuity, flat backgrounds, and mismatched assets.
- Prefer a working prototype over additional research once the main uncertainties are executable.

## Verification and failure routes

Verify proportionally to the work:

- desktop and representative mobile viewport;
- pointer, touch, keyboard, interruption, and repeated use where applicable;
- reduced-motion alternative;
- build/runtime errors and cleanup;
- measured frame stability for expensive motion;
- fallback for 3D, video, shader, or unavailable assets.

If a preferred route fails:

- MCP unavailable → use existing CLI or Browser/Computer Use;
- no local image backend → run the packaged capability check, install an isolated Pillow runtime when authorized, or request system approval for ImageMagick;
- authentication or free limit reached → use another source or reconstruct;
- component incompatible → copy the useful mechanism into local code;
- asset unavailable → generate or substitute a faithful proxy;
- performance budget exceeded → reduce layers, resolution, effects, or switch to video/static fallback;
- live reference blocked → work from recording/frames and label unobserved behavior as a prototype choice.

Deliver the prototype, checks completed, and remaining risks. Do not replace progress with a long research report.
