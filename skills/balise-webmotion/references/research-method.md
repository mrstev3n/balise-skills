# Webmotion research method

Load this file for reference research, reproduction from an image/video/site, or an immersive direction that needs temporal evidence. Research to make and build a decision, not to produce a dossier.

## Contents

1. Inputs and depth
2. Capture and reconstruction
3. Compact selection
4. Synthesis
5. Stop conditions

## Inputs and depth

Accept a vague brief, image, screenshot, video, GIF, screen recording, URL, live site, code fragment, or existing prototype.

- Use **lightweight research** for a fast prototype: one or two useful references and immediate implementation.
- Use **focused research** by default: a small complementary set covering direction and feasibility.
- Use **deep research** only for complex immersive work, competing directions, or an explicit moodboard request.

Do not ask the user to supply motion vocabulary. Infer the likely material, spatial, and temporal qualities, state a recommendation, and continue according to the operating mode.

## Capture and reconstruction

Prefer the smallest capture that preserves cause and effect.

### Page or scroll

- Observe initial load, the state before the effect, trigger, complete transition, settled state, and reversal.
- Repeat cached load when entry choreography matters.
- Check mobile when depth, large type, horizontal travel, pinning, pointer input, or heavy media drives the direction.

### Component interaction

- Observe rest, hover/focus, press, transformation, release, settle, and reverse path.
- Trigger rapidly to test interruption and retargeting.
- Check touch and keyboard equivalents when relevant.
- Repeat the interaction; first-use delight can become friction.

### Video or screen recording

- Sample 12–24 frames across the event, adding density around impact or direction changes.
- Extract local frames when useful:

```bash
ffmpeg -i reference.mp4 -vf "fps=6,scale=960:-2" frames/frame-%03d.jpg
```

- Store captures in the active project or a temporary task directory, never in the skill.

### Temporal grammar

Describe the useful mechanism as:

`state A → trigger → anticipation → transformation → impact → settle/regime → exit/reversal`

Extract only what the build needs:

- purpose and frequency;
- primary, secondary, and ambient layers;
- duration, pauses, overlap, stagger, and easing family;
- origin, path, scale, depth, camera, material, and sound;
- control mechanism: time, scroll, pointer, gesture, route, state, data, or ambient;
- interruption, responsive transformation, reduced motion, loading, and fallback;
- plausible implementation route.

Label an implementation route as a hypothesis until code, docs, or a prototype confirms it.

## Compact selection

Retain a reference only when it contributes at least one of these:

- a strong direction or quality bar;
- a reusable prompt, component, snippet, asset, or parameter set;
- a mechanism worth reconstructing;
- technical proof for the chosen route.

Choose complementary roles instead of ranking platforms. A useful focused set may contain one authored experience, one implementation example, and one directly reusable resource.

Do not require author records, consultation dates, exact URLs, provenance tables, or one citation per design decision. Keep a source link only when the user needs to reopen the item or the implementation depends on it.

## Synthesis

- State the motion thesis without naming a source.
- Decide what to copy closely, adapt, combine, generate, or discard.
- Choose the smallest stack and a fallback.
- In guided mode, present up to three coherent directions and recommend one.
- In autonomous or hybrid mode, choose one direction and move immediately into the prototype loop.
- Compare the result to the temporal qualities that mattered, not to a documentation checklist.

## Stop conditions

Stop researching when:

- one direction is strong enough to prototype;
- the needed prompt, code, asset, or mechanism has been found;
- new references repeat existing material;
- the remaining uncertainty requires implementation or performance measurement.

Research is incomplete only when no usable direction exists, a critical behavior has not been observed, or feasibility is being presented as fact without evidence.
