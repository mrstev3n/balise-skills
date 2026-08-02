# Sound, loops, and delivery

Use this reference when a sequence includes music, voice, sound effects, captions, a loop, a final hold, or a rendered deliverable.

## Design sound early

Decide during intake whether the role is:

- music-led pacing;
- voice-led explanation;
- sound effects reinforcing motion;
- ambient texture;
- intentional silence;
- a combination with clear priority.

Put temporary audio into the animatic when it influences timing. Mark cues for hooks, entrances, impacts, accelerations, transitions, reveals, and resolution. Avoid adding a generic track after the visual edit is locked.

Design a comprehensible silent experience. When voice carries essential meaning, provide captions and verify their timing, contrast, line length, safe zones, and reading speed.

## Usage rights for integrated audio

For every music or sound asset actually integrated or redistributed, keep only what delivery needs:

- title and creator;
- exact source URL;
- acquisition date;
- license and commercial-use status;
- attribution text and placement;
- required attribution, edits, and usage limits.

Do not create a provenance record for mood references that are never used in the output.

Use streaming services only as mood references unless their terms explicitly permit acquisition and reuse. Verify the individual asset, not only a platform-level marketing statement.

## Audio checks

- file exists and decodes completely;
- sample rate, channels, and duration match the deliverable;
- start, cuts, fades, and final tail are intentional;
- cues align perceptually with the rendered motion;
- no clipping, unintended silence, abrupt truncation, or encoding artifact;
- voice and music remain intelligible together;
- delivery loudness follows the actual channel specification when one exists.

Metrics such as LUFS and true peak prove level, not taste, richness, or synchronization.

## Loop versus repeated playback

Choose explicitly:

- **Seamless loop:** the last state and motion join the first without a perceptible reset.
- **Comfortable replay:** a hold, fade, or resolved lockup gives enough breathing room before the platform restarts playback.
- **Finite ending:** the sequence closes and is not expected to repeat.

Test a seamless loop through at least three repetitions. Test repeated playback in the target feed or player. A hold or fade is not evidence of a seamless loop.

## Final media proof

Inspect the exported artifact and record:

- codec and container;
- pixel dimensions and aspect ratio;
- frame rate, duration, and frame count where relevant;
- audio codec, sample rate, channels, and duration;
- full decode result;
- first frame, final frame, hero frames, and critical transitions;
- text, accents, logo integrity, safe zones, and visible artifacts;
- loop, hold, or final fade behavior;
- source-to-render synchronization.

If any source, copy, asset, timing, or audio changes after export, render again and repeat the relevant proof. Do not deliver a stale render beside newer source files.

Load [export-and-codecs.md](export-and-codecs.md) for codec recommendations, frame-rate decisions, alpha delivery, and `ffprobe`/`ffmpeg` proof commands.
