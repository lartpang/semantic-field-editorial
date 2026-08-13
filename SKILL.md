---
name: semantic-field-editorial
description: Turn a user-provided article, essay, chapter, newsletter, public-account post, report, or long-form draft into a coherent system of original editorial illustrations. Use when asked to plan, create, draw, generate, or revise article artwork such as blog headers, covers, chapter images, conceptual illustrations, explanatory editorial figures, or atmospheric interludes. Read the document first and let its meaning guide an independent visual composition; do not directly depict, diagram, or summarize the prose unless the user explicitly requests explanation. Do not use for ordinary data charts, UI mockups, photorealistic product renders, or unrelated decoration.
---

# Semantic Field Editorial

Create original editorial illustrations informed by writing.

The finished work must read first as an illustration with its own composition, atmosphere, and recognizable aesthetic—not as the article converted directly into a diagram, scene, noun collage, or visual summary. Use semantic analysis backstage: let the document determine the central tension, movement, rhythm, and emotional temperature, then make an independent visual proposition from them.

Treat the source document as the semantic source of truth. Do not add factual claims. Do not require every sentence, object, or section to have a visible counterpart. Only enter a more direct explanatory mode when the user explicitly requests a mechanism, relationship, comparison, or technical explanation.

Use the house signature:

> **ONE ANCHOR + ONE TRACE + ONE VOID + ONE ECHO**

- **Anchor**: one dominant idea expressed as a dense mass, focal form, glyph, or bounded field.
- **Trace**: a path, axis, arc, cut, or sequence expressing relation, time, causality, or transformation.
- **Void**: a meaningful gap, aperture, interruption, missing region, or unfilled counterform.
- **Echo**: a restrained repeated rhythm expressing plurality, iteration, residue, or feedback.

Usually include at least three roles, but relax this default when the source or composition requires another solution. Treat these as compositional roles, never as a four-part diagram template.

## Resource routing

Load only what the current task needs:

- Before composing or rendering, read `references/visual-language.md` for the palette, mark grammar, spatial rules, semantic mappings, typography, and anti-slop constraints.
- Before choosing a renderer or verifying assets, read `references/rendering-and-qa.md`.
- For raster generation in Chinese, read `references/semantic-field-editorial-prompt.zh-CN.md`; for English, read `references/semantic-field-editorial-prompt.en.md`. Adapt only the matching prompt to the source and illustration job.
- When delivering a standalone prompt for another image workflow, also read `references/prompt-usage.md`.
- For a multi-image local workflow, create `visual-dna.json` from `references/visual-dna.schema.json`, then run `scripts/validate_visual_dna.py <path-to-visual-dna.json>`.
- When maintaining this package, run `scripts/validate_package.py`.

Do not read raster-generation prompts for planning-only or SVG-only work.

## Core workflow

Use this pipeline:

```text
READ
→ DISTILL
→ MAP RELATIONS
→ SELECT ILLUSTRATION POINTS
→ BUILD VISUAL DNA
→ ASSIGN JOBS
→ COMPOSE
→ RENDER
→ VERIFY
```

Keep semantic analysis internal unless the user asks to see it.

## 1. Read and distill

Read a complete document before illustrating its first obvious paragraph. Infer:

- the central thesis or question
- the 3–7 most important semantic units
- causal, temporal, hierarchical, comparative, recursive, spatial, or oppositional relations
- what changes, what remains stable, and where the argument turns
- recurring motifs and the emotional temperature
- dense sections that would benefit from visual relief
- simple or repetitive sections that do not need an image

Treat headings as structural hints, not the only measure of importance. If only a section is supplied, analyze it deeply and infer only the minimum surrounding context.

Extract operations before objects. Prefer a structure such as:

```text
centralized force → distributed adoption → feedback loop → uneven capture of value
```

Useful operations include accumulate, disperse, converge, diverge, compress, expand, recurse, loop, layer, split, merge, erode, reveal, cross a threshold, stabilize, drift, rupture, align, oppose, invert, preserve, decay, and amplify.

For each image, retain only 3–6 decisive visual facts: a dominant relationship, direction, opposition, hierarchy, rhythm, transformation, gap, pressure, or meaningful exception. Use them to shape the artwork; do not encode them as a checklist of visible symbols.

## 2. Select illustration points

Illustrate selectively. Favor a section when it is conceptually central, relationally complex, difficult to imagine, introduces a major turn, or provides useful relief within dense prose.

Skip a section when it merely restates an idea, is already a short list, contains only a simple definition, or would be repeated rather than enriched by an image.

For an unspecified full-article request:

1. rank candidates by conceptual centrality, relational complexity, visual leverage, uniqueness, and reading rhythm
2. choose a restrained set
3. assign one primary job to each image
4. avoid using several images for essentially the same idea

A strong default for a substantial article is:

```text
1 × Header
1–2 × Chapter Summary or Explanatory
0–1 × Atmospheric Interlude
```

Treat this as a compositional default, not a quota.

## 3. Build Visual DNA

For more than one illustration, establish article-level Visual DNA before rendering. Keep these properties stable:

```text
background and ink
primary and optional secondary accent
anchor, trace, and echo families
void and texture behavior
default density and semantic distance
recurring motif
```

Vary composition, scale, rhythm, and local emphasis rather than replacing the art direction. Store job-specific semantic distance as an override, not as a new house style.

When producing local assets, save `visual-dna.json` and validate it with the bundled script. Do not create a manifest for one casual image unless it helps the task.

## 4. Assign one illustration job

### Header / Hero

Create an iconic editorial proposition that carries the article's central tension without summarizing its contents. Favor a dominant anchor, strong negative space, and minimal or no text.

```text
semantic distance: 3 / 5
default ratio: 2:1
text: normally none; 0–6 words maximum when necessary
```

### Chapter Summary

Create an editorial image that compresses a section into one proposition. Preserve illustrative autonomy; do not turn the section into a slide, card layout, or exhaustive concept map. Use short labels only when they materially improve comprehension.

```text
semantic distance: 2.5 / 5
default ratio: 3:2 or 16:10
```

### Explanatory Illustration

Clarify a mechanism, causal chain, comparison, transformation, technical relationship, or layered model. Use exact relation geometry and only necessary labels. This is the explicit exception where direct semantic mapping is appropriate, but it must still retain the Semantic Field editorial language. Correctness outranks atmosphere.

```text
semantic distance: 1–2 / 5
default ratio: 4:3 or 3:2
```

### Atmospheric Interlude

Carry emotional or philosophical pressure without literal explanation. Use void, scale, rhythm, material edge, and asymmetry. Avoid labels, diagram arrows, and generic dreamy imagery.

```text
semantic distance: 4 / 5
default ratio: 3:2
```

Obey a platform or repository crop specification over these defaults.

## 5. Control semantic distance

Use this scale:

```text
1 structural diagram
2 conceptual explanation
3 editorial abstraction
4 atmospheric abstraction
5 nearly non-representational mood
```

Never use level 5 for an explanatory figure. Never use level 1 for a hero unless the user explicitly requests a diagrammatic hero.

When asked for greater abstraction, increase distance by about one level while preserving the core relation. When asked for greater clarity, decrease distance before adding text.

## 6. Compose

Read `references/visual-language.md`, then build one obvious reading path and no more than three major visual groups unless the source requires more. Favor asymmetric balance, relational distance, substantial quiet space, one primary mark family, and at most two supporting families.

Ensure the result feels observed and authored. Avoid one-to-one correspondence between article points and visual objects unless the image's assigned job is explanatory. Treat the visual grammar as compositional behavior, not a fixed icon library.

## 7. Choose the rendering path

Read `references/rendering-and-qa.md` and follow its decision rules.

- Use image generation for heroes, atmospheric interludes, and expressive summaries that benefit from material edges or painterly geometric tension.
- Use editable SVG for correctness-sensitive explanatory figures, precise labels, mathematics, technical relationships, and deterministic layouts—even when image generation is available.
- Use an existing repository image-generation script when it clearly belongs to this workflow.
- Do not install heavyweight dependencies without need.
- If atmospheric artwork cannot be synthesized convincingly with available tools, return a complete generation prompt instead of substituting a crude SVG.

If generating raster artwork, use only the language-appropriate standalone prompt. If modifying an existing image, preserve its Visual DNA and include the target image through the available editing workflow.

## 8. Preserve batch continuity

Across one article, reuse the background, ink, primary accent, principal mark family, and one micro-motif. Vary scale, rhythm, direction, and negative-space placement. Make the hero the most iconic, explanatory figures the most precise, and atmospheric figures the quietest.

When the tool supports image references, use an approved earlier figure or contact sheet as a reference for later images. Do not rely on text-only Visual DNA when a visual reference is available.

## 9. Preserve content fidelity

Create visual metaphors, not new factual claims.

For explanatory work:

- map every major object and relation to the source
- do not invent data or fabricate charts
- do not turn correlation into causality
- do not turn uncertainty into certainty
- do not add people, places, products, or technologies merely to make the image concrete

For other illustration jobs, semantic fidelity does not require literal depiction. Allow metaphor, omission, compression, and visual invention while preserving the document's conceptual and emotional logic. Reject clichés that could accompany any article.

## 10. Revise by delta

Identify the requested change, then adjust semantic distance, density, palette role, mark family, text amount, crop safety, or compositional tension. Preserve unaffected Visual DNA and structure. Do not restart in an unrelated art direction unless requested.

## 11. Verify

Inspect final artifacts using `references/rendering-and-qa.md`. At minimum confirm:

- the work reads as an authored editorial illustration, not a direct visualization of the prose
- one clear job and a source-grounded dominant relation
- no invented claims, broken labels, or misleading causal direction
- coherent Anchor/Trace/Void/Echo roles without formulaic decoration
- correct aspect ratio, safe crop, sharp output, and valid SVG when applicable
- coherent Visual DNA and non-duplicated layouts across a batch

Do not claim completion from a prompt alone when the user requested generated assets and a suitable rendering tool is available.

## 12. Deliver

Generate or save actual artifacts whenever possible. Use stable descriptive names such as:

```text
article-slug--hero
article-slug--section-02-summary
article-slug--mechanism
article-slug--atmosphere
```

Keep the handoff concise:

```text
job:
source:
rendered:
ratio:
alt:
```

Treat the artwork as the primary deliverable.
