# Export and codecs

Use this reference before selecting or validating final media. Treat profiles as starting points; recheck the target channel and the chosen engine at delivery time.

## Contents

1. Delivery profiles
2. Frame-rate decision
3. Platform strategy
4. Inspection commands
5. Acceptance proof

## Delivery profiles

| Need | Starting profile | Important checks |
| --- | --- | --- |
| Broad web/social delivery | MP4, H.264, `yuv420p`, AAC when audio exists, fast-start metadata | Target limits, color, audio, full decode, recompression preview |
| Web delivery with alpha | WebM with a codec/pixel format that preserves alpha when the target supports it | Actual alpha channel, browser/player support, edge premultiplication |
| High-quality alpha master | MOV with ProRes 4444 or 4444 XQ when the render path supports it | Alpha mode, file size, color space, downstream compatibility |
| High-quality opaque intermediate | ProRes 422 family or another approved mezzanine format | Generation loss, storage, edit-system compatibility |
| Lossless frames or compositing | PNG image sequence; EXR when the pipeline needs HDR or advanced compositing | Complete sequence, numbering, alpha, color management, storage |
| Tiny silent loop with constrained compatibility | GIF only when video is not acceptable | 256-color palette, dithering, one-bit transparency, weight, repeated playback |
| Lightweight vector sequence | Lottie JSON when the design uses supported vector features | Fonts, masks, mattes, gradients, expressions, raster dependencies, renderer parity |

H.264 is not an alpha delivery format. A pixel-format name is not sufficient proof of transparency; inspect the rendered file over light and dark backgrounds. Prefer video over GIF when the destination supports it.

## Frame-rate decision

Choose frame rate from delivery requirements, source cadence, motion language, and render cost.

- **24 fps:** useful starting point for editorial or cinematic cadence and deliberate frame-based animation.
- **25 fps:** use for a 25/50-based broadcast or regional production pipeline.
- **30 fps:** common starting point for general digital, social, presentation, and screen-capture-adjacent work.
- **50/60 fps:** use when high temporal clarity, rapid kinetic motion, UI capture, sport-like movement, or smooth slow-down materially benefits; expect higher render and delivery cost.

Preserve mandated or source-native cadence when conversion would introduce judder. Do not label 24 as automatically premium or 60 as automatically modern. Express critical timings in seconds and frames, and retest easing, stagger, holds, motion blur, and caption gaps when frame rate changes.

## Platform strategy

Keep stable master families instead of a volatile table of platform limits:

- vertical `9:16`;
- portrait feed `4:5`;
- square `1:1`;
- landscape `16:9`;
- custom event, broadcast, signage, or embed dimensions when specified.

At task time, check the official destination documentation for dimensions, maximum duration, file size, codec/container, audio, captions, safe zones, UI overlays, autoplay, looping, and recompression. Record the verified target constraint in the project brief, not permanently in this skill.

## Inspection commands

Use commands only when `ffprobe`/`ffmpeg` are available. Quote real paths.

### Container and streams as JSON

```bash
ffprobe -v error -show_format -show_streams -of json output.mp4
```

### Essential video fields

```bash
ffprobe -v error -select_streams v:0 -show_entries stream=codec_name,profile,pix_fmt,width,height,r_frame_rate,avg_frame_rate,nb_frames,duration,color_space,color_transfer,color_primaries -of json output.mp4
```

### Essential audio fields

```bash
ffprobe -v error -select_streams a:0 -show_entries stream=codec_name,sample_rate,channels,channel_layout,duration -of json output.mp4
```

### Count decoded video frames

```bash
ffprobe -v error -select_streams v:0 -count_frames -show_entries stream=nb_read_frames -of default=noprint_wrappers=1 output.mp4
```

### Full decode check

```bash
ffmpeg -v error -i output.mp4 -f null -
```

### Inspect representative frames

```bash
python3 scripts/extract_reference_frames.py output.mp4 proof-frames/ --frames 16
```

### Generate an efficient GIF palette when GIF is required

```bash
ffmpeg -i input.mp4 -vf "fps=15,scale=960:-2:flags=lanczos,palettegen" palette.png
ffmpeg -i input.mp4 -i palette.png -lavfi "fps=15,scale=960:-2:flags=lanczos[x];[x][1:v]paletteuse=dither=sierra2_4a" output.gif
```

## Acceptance proof

- The chosen profile matches the actual destination and alpha/audio need.
- Container, codecs, dimensions, frame rate, duration, streams, and pixel format are inspected.
- Full decode completes without errors.
- First, last, hero, transition, and text-heavy frames are visually checked.
- Alpha is composited over contrasting backgrounds when required.
- The target platform/player is tested when it recompresses, crops, overlays UI, loops, or strips audio.
- Source changes trigger a new render and the relevant proof is repeated.
