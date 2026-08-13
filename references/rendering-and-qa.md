# Rendering and QA

Use this reference after choosing the illustration job and composition.

## Contents

- Choose a renderer
- Raster workflow
- SVG workflow
- Single-image QA
- Batch QA
- Failure behavior

## Choose a renderer

Use raster image generation for:

- heroes and covers
- atmospheric interludes
- expressive summaries
- artwork that depends on material edges, pigment behavior, or subtle geometric tension

Use editable SVG for:

- correctness-sensitive explanatory figures
- precise labels, equations, and typography
- mathematical, logical, or technical relationships
- diagrams that need deterministic layout or later editing

Choose SVG for a precision-sensitive figure even when raster generation is available. If a raster draft contains broken text or ambiguous relations, switch to SVG instead of repeatedly prompting around the failure.

## Raster workflow

1. Read only the language-appropriate standalone prompt.
2. Adapt it to the source, illustration job, aspect ratio, and Visual DNA.
3. Generate the artwork rather than returning the prompt when generation is available and requested.
4. Inspect the result at sufficient detail.
5. Revise the smallest failed variable: relation, crop, density, palette, text, or semantic distance.

For a batch, use an approved earlier image or a contact sheet as a visual reference when the tool supports references. Reuse text-only Visual DNA when image references are unavailable.

## SVG workflow

- use a clean `viewBox`
- define palette and typography near the top
- group elements by semantic role
- prefer editable primitives over arbitrary path clouds
- use local or system fonts without embedded font files
- use no remote URLs
- validate XML
- render a preview when a local renderer is available
- inspect the preview before delivery

Default canvases when no platform requirement exists:

```text
hero: 1600 × 800
inline: 1440 × 960
```

## Single-image QA

Confirm:

- the result is an authored illustration, not prose mechanically converted into visible objects
- the dominant relation matches the source without demanding one-to-one depiction
- no data, causal direction, label, or object was invented
- Anchor, Trace, Void, and Echo act as compositional roles rather than diagram labels
- text is legible, correctly spelled, and appropriate to the image job
- the requested aspect ratio is exact
- important content remains inside likely crop-safe regions
- edges, texture, and contrast survive normal display size
- no accidental glyphs, pseudo-labels, or generation artifacts appear

For raster images containing necessary text, inspect the visible text manually or with OCR when available. If exact text cannot be trusted, remove it or rebuild the figure as SVG.

## Batch QA

Compare all figures together, preferably in a contact sheet or side-by-side preview. Confirm:

- shared background, ink, primary accent, mark family, and recurring motif
- job-appropriate semantic distance for every figure
- visibly different layouts rather than template repetition
- the hero is the most iconic
- explanatory figures are the clearest
- atmospheric figures are the quietest
- no single figure drifts into another visual language

## Failure behavior

- If an explanatory raster remains ambiguous, rebuild it as SVG.
- If an image becomes generic or literal, return to the source tension and remove unsupported objects.
- If no available tool can render an atmospheric request convincingly, deliver a complete generation prompt and label it as unrendered.
- Do not claim an artifact was verified unless its rendered output was inspected.
