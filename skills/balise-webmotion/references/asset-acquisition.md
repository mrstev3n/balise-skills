# Portable still-image asset acquisition

Load this reference whenever the web experience needs a custom subject, texture, environment, background, collage element, raster illustration, or transparent cutout.

## 1. Write the asset contract

Before choosing a provider, define only what production needs:

- narrative and compositional role;
- asset type and intended surface;
- dimensions, ratio, resolution, crop, and responsive variants;
- silhouette, perspective, lighting, material, palette, and negative space;
- relationship to existing identity and reference images;
- native alpha, provider cutout, chroma key, or opaque background;
- negative constraints, including invented text, altered logos, generic gradients, and unwanted shadows;
- final PNG, WebP, AVIF, SVG, or source format and weight budget.

Never regenerate an official logo. Keep text as HTML/SVG when accessibility, localization, or responsiveness matters.

## 2. Inspect capabilities before choosing

Use the first route that can produce an inspectable result at the required quality:

1. existing official or project asset;
2. native image generation or editing exposed by the harness;
3. Magnific MCP already connected;
4. Higgsfield MCP already connected;
5. another exposed skill, MCP, SDK, CLI, or authenticated API;
6. an approved installation or connector setup;
7. local SVG, Canvas, CSS, WebGL, Three.js, procedural texture, or accessible stock;
8. a precise generation brief when execution cannot be authorized.

Delegation is optional. Call available capabilities directly. Never claim a provider, model, operation, account, or credit balance exists until inspected.

## 3. Install the local cutout pipeline when useful

Run a read-only check first:

Resolve the installed `balise-webmotion` directory first; do not assume the project working directory contains the skill. Then run:

```bash
python <balise-webmotion-skill-dir>/scripts/setup_asset_pipeline.py --check --backend auto --scope user
```

When production or workflow setup authorizes reversible user-level installation:

```bash
python <balise-webmotion-skill-dir>/scripts/setup_asset_pipeline.py --install --backend pillow --scope user
```

The setup uses `uv` when available, otherwise `venv` and `pip`. It installs Pillow in an isolated user or project runtime. For ImageMagick, inspect the proposed Homebrew, apt, dnf, pacman, or winget route. Require explicit approval before `--scope system --allow-system`, `sudo`, or an administrator-level action.

Report what was installed, its location, version, verification command, and removal path. Never hide an installation inside an unrelated build command.

## 4. Use providers from live catalogs

### Magnific, formerly Freepik

Treat Magnific as a full creative backend, not a single model. The current MCP may expose model catalogs, raster and SVG generation, stock search/download, variations, relight, resize, camera changes, upscale, background removal, raster-to-SVG, flows, 3D, audio, and video. This iteration uses still-image operations only.

At task time:

1. call the image-model catalog or equivalent;
2. compare recommendations, tags, references, ratios, resolutions, quality, expected time, premium status, and cost;
3. select the model by the asset contract;
4. generate one image;
5. inspect it in the page composition;
6. upscale only after the direction passes;
7. use the provider background-removal operation when a cutout is required.

Current examples include GPT, Seedream, Imagen/Nano Banana, and Flux families. Do not hard-code them as permanent defaults. Use the current catalog and tool schema.

### Higgsfield

The official remote MCP is `https://mcp.higgsfield.ai/mcp`. Authenticate through the account flow when already configured or explicitly approved. Inspect its live image models and editing operations before use. Do not assume the website background remover is exposed through the connected MCP.

### Missing provider

If a useful MCP is absent, give the shortest official setup route and continue with a local, procedural, stock, or brief-based fallback. Connecting an account, adding a connector, or spending credits requires the matching authorization.

## 5. Produce one representative sample

1. Choose the provider and model from live capabilities.
2. Write a prompt from the asset contract.
3. Generate one candidate at draft resolution.
4. Place it in the real hero, section, or transition.
5. Correct the prompt or switch model if the generation is the problem.
6. Approve composition before upscale, cutout, format variants, or batches.
7. Keep prompt, provider, model, useful parameters, seed when available, and final project path for reproducibility.

This production record is not a provenance dossier. Check usage terms only for external material actually integrated or redistributed.

## 6. Create transparent assets safely

Prefer, in order:

1. verified native alpha;
2. a provider `remove_background` or matting operation;
3. local chroma key for a simple opaque subject;
4. specialist matting for hair, fur, feathers, smoke, glass, liquid, translucent material, reflection, or soft shadow.

For chroma generation, use `#00ff00` unless the subject contains green; then use `#ff00ff`. Require a perfectly flat color with no floor, texture, gradient, lighting variation, contact shadow, reflection, or watermark. Keep generous padding and forbid the key color inside the subject.

```bash
python <balise-webmotion-skill-dir>/scripts/remove_chroma_key.py \
  --input source.png \
  --output cutout.png \
  --key auto-border \
  --backend auto \
  --despill \
  --preview cutout-checkerboard.png
```

If neither Pillow nor ImageMagick is available, the script calls the setup check and returns the exact installation command instead of pretending the cutout succeeded.

## 7. Web delivery checks

- Inspect alpha over checkerboard, light, dark, and brand-colored surfaces.
- Check fringes, internal holes, subject detail, crop, and shadow strategy.
- Keep the editable alpha master; derive WebP/AVIF only after validation.
- Define intrinsic dimensions and responsive sizes; do not ship a 4K cutout into a small card.
- Measure decoded size, network weight, LCP impact, and mobile memory.
- Preload only a genuinely critical hero asset.
- Provide a static or lighter fallback when the asset participates in expensive motion.
- Re-test after compression because edge halos may appear only in the delivered format.
