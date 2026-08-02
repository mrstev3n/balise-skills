# Quality rubric — "Awwwards-level" bar

Load this file before self-review, when defining acceptance criteria, or when handing the work to an independent reviewer. Without this rubric, "award-level quality" is a slogan; with it, the bar is measurable.

## General criteria (modeled on the Awwwards jury)

| Criterion | Question to ask |
| --- | --- |
| Design | Do composition, typography, material, and depth stand comparison with recently awarded sites — or only with templates? |
| Usability | Does motion help users understand, orient, and confirm — or does it slow access to content? |
| Creativity | Is there a recognizable signature, an unseen combination, a moment of surprise? |
| Content | Does motion serve the narrative and message, or merely decorate them? |

## Motion-specific criteria

Score each 0 (absent or counterproductive), 1 (correct), 2 (remarkable). An award-level project targets ≥ 80% of the applicable maximum, with **no 0 on any robustness criterion**.

| Criterion | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Loading choreography | Content appears without intention | Clean but generic reveal | The first 3 seconds are a brand moment: justified preloader, orchestrated entry sequence, treated typography |
| Scroll narrative | Scroll unrelated to content | Coherent scroll reveals | Scroll builds a narrative: thresholds, pinning, scrub, and breathing room serve a progression |
| Motion physics | Linear or default easings | Consistent curved easings | Springs, inertia, magnetic hover, physical drag — material feels like it has mass |
| Typographic reveals | Text fades in as a block | Reveal by line/word | Choreographed split-text (line, word, character) with intentional masks and staggers |
| WebGL/shader moment (if the direction calls for it) | Gratuitous decorative shader | Justified 3D scene | A material or spatial moment impossible in the DOM, with fallback |
| Cursor interactions | None, or generic cursor follower | Well-crafted hover states | The pointer is an actor: magnetism, distortion, anticipation, press feedback |
| Page/route transitions | Hard cut | Clean transition | Spatial continuity between views (FLIP, view-transitions, choreographed exit → entrance) |
| Micro-interactions | Browser default states | Micro-interactions present | A coherent micro-interaction system, applied with restraint and consistency |
| Easter eggs | None | A token wink | Surprises that reward exploration without ever blocking usage (see easter-eggs.md) |
| Sound (optional) | Intrusive autoplay | — | Opt-in audio feedback that strengthens timing and state |
| Robustness — reduced motion | Ignored or blanket-off | Generic fade fallback | Designed alternative: information and hierarchy survive without movement |
| Robustness — performance | Visible jank, layout thrash | 60 fps on desktop | 60 fps including mid-range mobile, GPU budget respected and measured |
| Robustness — repetition | First-use delight becomes friction | Tolerable in use | Designed for real frequency: frequent animations are discreet, spectacular ones rare |

## Usage protocol

- **Direction mode:** each proposed direction declares which criteria it targets and which it deliberately sacrifices.
- **Production mode:** the rubric is the self-review gate before delivery. List unmet criteria with their reason (constraint, choice, or open).
- **Handoff:** the filled rubric travels with the built code to an independent reviewer, together with intent criteria, comparison references, and the declared motion budget. When independent review is unavailable, label the verdict as self-review rather than self-certifying it as independent.
