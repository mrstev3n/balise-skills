# Localization and Unicode Stress

Use this reference for Global tests, pseudo-localization, RTL, mixed-direction content, regional formats, plural-sensitive UI, or font fallback.

## Contents

- Pseudo-localization
- Plurals and grammar
- Regional formats
- RTL and bidirectional strings
- Unicode segmentation
- Font coverage and fallback
- Evidence boundaries

## Pseudo-localization

Pseudo-localization is a structural test, not a translation.

Use a combination of:

- visible opening and closing delimiters to reveal clipped boundaries;
- controlled padding or expanded wording;
- accented or alternate-script characters;
- an RTL pseudo-locale when direction matters.

Use it to expose:

- rigid widths and heights;
- hardcoded or unexposed strings;
- concatenated fragments that cannot be reordered;
- labels embedded in imagery;
- incorrect assumptions about Latin characters;
- missing mirroring or direction handling.

Do not apply a universal expansion percentage. A 30–40% case can be useful, but real languages vary through word length, word count, density, grammar, writing system, and format.

## Plurals and Grammar

Do not model localization as singular versus plural only.

Depending on the locale, plural categories may include:

- zero;
- one;
- two;
- few;
- many;
- other.

Test values that may select different forms:

- 0, 1, and 2;
- teens;
- values ending in different digits;
- decimals;
- values such as 1 and 1.0 when the formatting pipeline distinguishes them;
- numeric ranges.

Do not generate linguistically authoritative strings without verified locale data or qualified review. When only layout is being tested, label the case accordingly.

## Regional Formats

Choose formats relevant to the product and markets:

- grouping and decimal separators;
- plus and minus signs;
- currency symbol, code, order, and spacing;
- unit names and abbreviations;
- percentages and compact notation;
- date order and month-name length;
- short, medium, long, and full date styles;
- 12-hour versus 24-hour cycles;
- time zones and daylight-saving labels;
- alternative calendars when genuinely supported;
- postal addresses and personal names without forcing a Western structure.

Check both width and meaning. `10.000`, `10,000`, and `10 000` can represent different conventions, not stylistic alternatives.

## RTL and Bidirectional Strings

Test whole-layout direction separately from mixed-direction content.

Inspect:

- reading and navigation order;
- alignment and anchoring;
- start/end behavior rather than left/right assumptions;
- directional icons such as arrows, progress, undo, and media controls;
- punctuation and paired characters;
- numbers, URLs, file extensions, account codes, and Latin identifiers embedded in RTL text;
- truncation that preserves the identifying segment;
- correct isolation of inserted values in implementation.

Static design can reveal visual ordering problems. Source or runtime inspection is required to confirm direction metadata, bidi isolation, DOM order, and assistive-technology behavior.

## Unicode Segmentation

A user-perceived character may contain multiple Unicode code points.

Include cases with:

- base letters plus combining marks;
- emoji plus skin-tone modifiers;
- emoji joined into one visual sequence;
- flags and other multi-code-point symbols;
- scripts whose shaping depends on neighboring characters;
- text without spaces between words.

When implementation code truncates by character count, inspect whether it uses grapheme-aware segmentation. Do not recommend cutting at an arbitrary code point or UTF-16 unit.

Visual ellipsis should signal omission and preserve a useful identifying portion. For file paths, references, hashes, and extensions, middle truncation may preserve more identity than end truncation.

## Font Coverage and Fallback

Do not assume the primary font supports every required script.

Check:

- missing glyphs or tofu;
- fallback family selection;
- changes in character width and line breaks;
- taller ascenders, descenders, or line boxes;
- baseline and vertical alignment beside icons;
- weight or style availability in the fallback family;
- fallback behavior inside exported or web-rendered assets.

A string can fail without becoming longer because the fallback font has different metrics.

## Evidence Boundaries

Label findings accurately:

- **Static evidence**: visible clipping, order, alignment, fallback, or layout change.
- **Source evidence**: locale APIs, direction attributes, formatters, segmentation, or translation-key structure.
- **Runtime evidence**: rendered locale, responsive reflow, keyboard behavior, and actual fallback.
- **Expert validation**: translation quality, cultural appropriateness, terminology, and legal meaning.

Never describe pseudo-localized text as a translation or a successful visual test as localization readiness.
