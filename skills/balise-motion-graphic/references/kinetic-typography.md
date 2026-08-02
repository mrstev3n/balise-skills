# Kinetic typography

Use this reference when typography carries the narrative, rhythm, identity, captions, or a signature transition.

## Choose the animation unit

| Unit | Good use | Main risk |
| --- | --- | --- |
| Block | Editorial cuts, posters, strong hierarchy | Slide-deck feeling |
| Line | Readable reveals, sentence rhythm | Mechanical line queues |
| Phrase or word | Emphasis, sync to speech or beat | Too many competing accents |
| Syllable | Phonetic or music-led timing | Gimmick without audio logic |
| Character or glyph | Logos, short titles, texture, transformation | Noise, unreadability, broken shaping |

Do not split by character by default. Preserve grapheme clusters, ligatures, accents, shaping, and reading order. Test the actual language and font; a code-point split can break visible characters.

## Direct reading and rhythm

- Give each text event one job: read, announce, label, punctuate, transform, or resolve.
- Measure exposure using the actual copy and a normal-speed playback. Allow at least two comfortable reads for essential standalone copy when no voice carries it.
- Treat roughly 140 words/minute as a comfortable caption reference and 180–200 words/minute as a high-density ceiling that needs careful review; language, audience, line breaks, font, and composition can require slower timing.
- For very short subtitle events, start near one second rather than flashing text for only a few frames. Align captions to speech and shots, then watch the full sequence.
- Do not reveal a punchline or key word before its spoken or visual event unless anticipation is intentional.
- Keep essential copy understandable without sound and keep captions clear of prescribed safe areas.

## Choreograph type as matter

Specify:

- reveal origin and mask logic;
- tracking, leading, scale, width, weight, baseline, and axis changes;
- entry, readable regime, transformation, exit, and final lockup;
- relationship to image, depth, occlusion, camera, beat, voice, and sound effect;
- stagger origin, overlap, acceleration, and interruption by editorial cuts;
- behavior across long names, accents, numerals, dates, and localized copy.

Use opacity as support, not the whole idea. Prefer transformations that reinforce the typographic structure: line masks, baseline travel, width/weight interpolation, crop, extrusion, displacement, or editorial cuts. Avoid random per-letter offsets that turn language into particles without narrative purpose.

## Caption relationship

- Separate designed on-screen typography from accessibility captions when both are necessary.
- Do not make animated display text carry dialogue captions unless readability and timing remain robust.
- Preserve two-line limits and language-specific line-breaking guidance when the destination imposes them.
- Check contrast, collisions, shot changes, audio sync, and legibility after platform scaling or compression.

## Acceptance checks

- The text can be read at normal speed on the target display.
- Typographic motion follows the identity and the Motion DNA.
- Essential text receives enough stable exposure.
- Accents, ligatures, shaping, and localization survive the implementation.
- Voice, captions, sound cues, and typographic impacts agree temporally.
- The sequence still communicates when muted.
- Dense frame inspection reveals no accidental glyph clipping, mask residue, or unreadable transient state.
