# Motion quality and production lessons

Use this reference to approve directions, design transitions, diagnose weak motion, and review previews or renders.

## Contents

- Contemporary quality bar and default blocks
- Transition specification and production lessons
- Motion DNA anchors and photosensitivity
- Proof ladder and diagnostic table
- Review protocol and verdicts

## Contemporary quality bar

A strong sequence shows:

- readable hierarchy on a still frame;
- attention distributed through choreography rather than simultaneous movement;
- a limited recurring vocabulary of gestures;
- transitions motivated by form, space, subject, edit, or sound;
- contrast between energy, pause, impact, and resolution;
- typography designed as image and rhythm;
- exits and final states with the same care as entrances;
- assets and materials tied to the subject or identity;
- sound or silence designed intentionally.

Modernity is not a style preset. Flat color, bento grids, gradients, 3D, grain, orbital paths, shaders, elastic easing, and cinematic camera moves can all be contemporary or dated depending on purpose and execution.

## Block by default unless justified

- counters, tickers, timers, numbering, fake metrics, and invented dashboards;
- generic “tech” grids, glows, glass cards, particle fields, and neon filler;
- identical slide-fade entrances on every scene;
- typewriter text, floating labels, and feature lists staged like slides;
- all elements centered, moving at the same amplitude and easing;
- colors, type, or motifs chosen before reading the identity;
- stock backgrounds or AI assets that do not belong to the system;
- transitions that interrupt the narrative to demonstrate an effect;
- uncontrolled mixing of references with no coherent motion system.

These are diagnostic triggers, not permanent bans. A real timer can justify a timer; an editorial jump cut can be stronger than forced continuity.

## Transition specification

For each critical transition define:

1. origin and initial velocity;
2. path or edit logic;
3. acceleration, easing, or physical force;
4. depth, mask, and occlusion behavior;
5. destination and final velocity;
6. relation to typography and sound;
7. appearance, installation, regime, and exit phases.

Remove a mechanical pose when it adds no information and creates a perceptual stop. Overlap causally related actions when strict sequencing feels like slides. Validate occlusion until no unintended fragment remains.

## Lessons from real production

- A rejected visual premise needs a rebuild, not more polish.
- “AI slop” often comes from unearned signs: pseudo-interface, fake data, generic decoration, and references never converted into constraints.
- A complete identity audit prevents approximate assets and incorrect typography.
- Every text element must earn its screen time; remove verbal decoration when the scene already communicates the idea.
- More narrative beats can improve progression while fewer poses improve a continuous gesture. Do not confuse the two.
- Static storyboards validate composition, not acceleration, continuity, occlusion, or physical weight.
- A frame sequence annotated by the user can localize a bad state better than a general request to “make it smoother.”
- Sound added after motion tends to feel ornamental. Design cues with the beat sheet.
- A longer final hold can improve repeated playback but does not create a seamless loop.
- A source change after rendering invalidates the old export, even when the change seems typographic or minor.
- A passing lint, DOM inspection, contrast metric, or audio loudness value does not prove creative quality.
- A renderer or screenshot failure is not proof that the animation itself is wrong.

Do not reuse project-specific solutions such as a 15-second duration, 4.57-second hold, orbital absorption, Figma Sans, triple block wipe, or exact easing as defaults.

## Motion DNA anchors

Define a project palette rather than inventing timing scene by scene. Express values in seconds and frames at the chosen frame rate.

| Role | Starting behavior | What to tune |
| --- | --- | --- |
| Accent or impact | 3–8 frames | Legibility, weight, motion blur, sound sync |
| Short reveal or response | 8–18 frames | Distance, mask, easing, overlap |
| Primary entrance or transition | 12–36 frames | Narrative importance, path, depth, occlusion |
| Overshoot and settle | 4–16 frames after impact | Mass, damping, final precision |
| Narrative transformation | 0.6–2.5 s | Number of phases, camera, reading, sound |
| Readable hold | Driven by actual copy | Language, audience, voice, display size |
| Final resolution | Long enough for comprehension and replay comfort | CTA, platform restart, audio tail |

These are anchors, not rules. Fast motion can use a long readable regime; slow motion can contain sharp impacts. Changing frame rate requires retesting cadence and easing rather than mechanically preserving frame counts.

Declare a small family of forces:

- decisive exit or cut acceleration;
- standard authored move;
- user- or object-like spring when physical response matters;
- soft settle or lockup;
- ambient drift, if any, with deliberate phase and amplitude.

Use custom curves or springs because the material demands them, not to satisfy a quota. Review anticipation, acceleration, impact, overshoot, settle, and exit separately.

## Photosensitivity

Avoid content that flashes more than three times in any one-second period. Treat saturated-red flashes and large high-contrast luminance changes with particular caution. The simpler strict rule is preferred; if a sequence relies on faster flashing, require a recognized flash-threshold analysis rather than visual intuition.

Count a flash as a pair of opposing light/dark or color transitions. Inspect the actual final render at normal speed; timeline intent does not prove the encoded result is safe. Replace unsafe flashing with slower pulses, spatial wipes, lower-contrast changes, texture motion, or non-reversing transitions.

## Proof ladder

1. **Facts and identity:** content, claims, copy, tokens, and assets verified.
2. **Hero frames:** hierarchy, typography, composition, and material approved.
3. **Contact sheet:** states, temporal density, and suspect moments located.
4. **Timed preview:** rhythm, acceleration, physics, cuts, and sound observed.
5. **Final export:** actual media decoded and inspected.

Each level answers different questions. Never substitute a lower level for a higher one.

## Diagnostic table

| Symptom | Likely cause | Correction | Proof |
| --- | --- | --- | --- |
| Looks like AI slop | Generic signs and no explicit anti-reference | Reduce vocabulary; rebuild from brand and references | Hero-frame comparison and creative approval |
| Looks flat | Weak hierarchy, depth, material, or cadence | Change scale, rhythm, matter, parallax, camera, or asset route | Normal-speed preview in context |
| Feels like slides | Unrelated serial entrances and exits | Build causal continuity or use an intentional editorial cut | Timeline and playback |
| Text feels unnecessary | Scene is over-explained | Remove it or give it a unique narrative job | Silent comprehension and reading-time test |
| Transition stutters | Extra pose or velocity discontinuity | Remove the dead state; use a continuous path or overlap | Dense frame sample plus normal speed |
| Objects remain visible | Incomplete mask, depth, or destination | Correct occlusion and convergence | Terminal frames at full resolution |
| Exit is weaker than entrance | Exit treated as opacity cleanup | Give it path, force, edit logic, or resolution | Separate exit review |
| Sound feels flat | Cues added after the animation | Recompose audio and motion on one grid | Synchronized A/B listening |
| Replay is aggressive | Final state is too short | Add a measured hold or redesign the loop | Three repeated plays in target context |
| Checks pass but motion is weak | Technical and creative verdicts conflated | Add independent motion review and user acceptance | Three separate verdicts |

## Review protocol

Review at normal speed, reduced speed, by scrub, and frame-by-frame around critical moments. Inspect copy and composition without sound, then sound without watching, then the combined sequence.

Issue three verdicts:

- **Technical:** file, layout, decode, timing, and media checks pass or fail.
- **Motion:** hierarchy, narrative, timing, transition, physics, typography, and sound reach the intended bar.
- **Creative:** in guided mode, the user explicitly accepts the direction and remaining compromises; in autonomous or hybrid mode, record a provisional self-review and leave explicit acceptance open.

Return separate verdicts. Technical and motion can reach `GO` in autonomous production while creative acceptance remains pending. Never label creative acceptance as passed without the user. Return `NO-GO` with the smallest corrective action and proof required for re-review.
