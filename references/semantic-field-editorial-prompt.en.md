# Semantic Field Editorial Prompt (Standalone English Version)

Use the article, chapter, essay, newsletter, report, blog draft, or long-form text supplied by the user as the **sole semantic source** for an original editorial illustration or a coherent set of illustrations.

The finished result must first read as a complete, independent editorial illustration with a distinctive aesthetic—not as prose converted sentence by sentence into a flowchart, concept map, infographic, literal scene, or noun collage. Let the document work backstage by supplying the central tension, motion, rhythm, and emotional temperature. Use metaphor, omission, compression, and recomposition; visual elements do not need one-to-one correspondence with every point in the text. Move into direct explanation only when the user explicitly requests a mechanism or relationship to be clarified.

Do not merely find a "related picture." Do not draw every noun in the article. Read the invisible structure of the writing — its claims, relations, hierarchy, tension, movement, rhythm, turns, and emotional pressure — and translate those structures into a restrained contemporary editorial visual language.

This visual language is called:

# Semantic Field

Its signature is:

> **ONE ANCHOR + ONE TRACE + ONE VOID + ONE ECHO**

- **Anchor**: one dominant visual mass, form, glyph, or bounded field representing the most important concept or proposition.
- **Trace**: one directional path, arc, axis, cut, flow, or sequence representing causality, time, transformation, argument, or relation.
- **Void**: deliberate negative space, aperture, gap, interruption, or unfilled region representing distance, uncertainty, contrast, boundary, or missing information.
- **Echo**: restrained repetition of dots, bars, blocks, steps, bands, nodes, or related marks representing iteration, accumulation, feedback, plurality, or after-effect.

Do not mechanically force all four into every image, but most compositions should naturally contain at least three.

Do not imitate the signature illustration style of any company or named living artist. Use the explicit visual rules below to produce an original and recognizable Semantic Field aesthetic.

## 1. Input

The user may provide only the document, or may also specify image type, platform, count, and aspect ratio.

If no structured request is provided, infer it from natural language.

```text
[DOCUMENT]
User-provided article or section
[/DOCUMENT]

[REQUEST]
type: auto | header | chapter-summary | explanatory | atmosphere
count: 1 or requested number
aspect_ratio: user-defined; infer from image type if omitted
platform: blog | newsletter | wechat | article | other
language: follow the source document unless specified otherwise
must_preserve: required concepts, equations, keywords, or objects
avoid: user-defined exclusions
[/REQUEST]
```

## 2. Read before drawing

Internally read the whole document first.

Do not output this analysis unless the user requests it.

Identify:

1. the real central question or thesis
2. the 3–7 most important semantic units
3. their relations
4. whether the argument accumulates, disperses, converges, diverges, compresses, expands, recurses, loops, opposes, or shifts level
5. what changes
6. what remains stable
7. the most important conceptual turn
8. which passages explain and which passages reflect
9. the emotional temperature
10. recurring motifs, actions, metaphors, or structural patterns

Prefer **semantic operations** over noun lists:

```text
accumulate
disperse
converge
diverge
compress
expand
recurse
loop
oscillate
layer
embed
filter
split
merge
erode
reveal
conceal
cross a threshold
stabilize
drift
rupture
align
oppose
mirror
invert
exchange
preserve
decay
amplify
translate
```

Weak extraction:

```text
AI, company, user, capital
```

Better extraction:

```text
centralized force
→ distributed adoption
→ feedback loop
→ value reconcentrates
```

The second form gives the artwork a compositional grammar.

## 3. Give each image one job

### Header / Hero

Purpose:

Express the article's visual thesis, not a miniature explanation of the whole document.

Behavior:

- relatively abstract
- one strong anchor
- one major trace or axis
- one meaningful void
- one small echo cluster
- generous negative space
- little or no text
- never compress every section into an infographic

Default semantic distance:

```text
3 / 5
```

Default aspect ratio when unspecified:

```text
2:1
```

### Chapter Summary

Purpose:

Compress a section into one visual proposition.

Behavior:

- 3–5 semantic units
- one visible but non-mechanical reading direction
- hierarchy expressed through scale and distance
- minimal labels only when useful
- should still feel like editorial illustration, not a slide

Default semantic distance:

```text
2.5 / 5
```

Default ratio:

```text
3:2 or 16:10
```

### Explanatory Illustration

Purpose:

Clarify a mechanism, process, system, comparison, causal chain, technical structure, or abstract relationship.

Behavior:

- lowest abstraction
- precise relational geometry
- controlled arrows, traces, layers, and boundaries
- labels only where exact reading matters
- never invent data
- never create decorative pseudo-charts
- correctness outranks atmosphere

Default semantic distance:

```text
1–2 / 5
```

Default ratio:

```text
4:3 or 3:2
```

### Atmospheric Interlude

Purpose:

Carry the philosophical, emotional, or psychological pressure of the prose without explaining it literally.

Suitable for:

- essays
- reflection
- transitions
- uncertainty
- distance
- anticipation
- pressure
- nostalgia
- stillness
- awe
- imbalance
- release

Behavior:

- no explanatory labels
- no infographic arrows
- strong use of void, scale, rhythm, edge, and asymmetry
- visual metaphor may be used when grounded in the text
- avoid generic dreamy imagery

Default semantic distance:

```text
4 / 5
```

Default ratio:

```text
3:2
```

### AUTO

If type is `auto`, infer the appropriate image job.

If the user asks for illustrations across an entire document, do not illustrate every section.

Prefer a restrained set such as:

- one Header
- one or two high-value Chapter Summary / Explanatory images
- optionally one Atmospheric Interlude

The number must follow the document's actual visual needs, not a quota.

## 4. Establish article-level Visual DNA

When multiple images are required, create a shared Visual DNA internally before rendering.

Define:

```text
background
structural ink
primary accent
optional secondary accent
Anchor family
Trace family
Echo family
Void behavior
texture behavior
line character
default density
recurring micro-motif
typographic attitude
```

Keep these stable across the article.

Allow each image to vary in:

- anchor placement
- trace direction
- element scale
- void size
- local rhythm
- composition

Do not suddenly switch to an unrelated palette or material language.

## 5. Semantic Field base aesthetic

### Background

Default to a quiet warm mineral ivory:

```text
#F3EFE7
```

Small shifts are allowed when the article demands a different temperature.

Keep the ground mostly flat and calm.

Avoid default use of:

- scanned paper
- vintage beige filters
- full-canvas grain
- watercolor washes
- dramatic gradients
- glow
- fog
- vignettes

### Structural ink

Default:

```text
#1E1E1B
```

A soft near-black for structural lines, major edges, important type, and traces.

### Accent bank

Usually choose one primary accent based on semantic temperature:

```text
Ember       #D56845
energy, friction, urgency, rupture, warmth, action

Mineral     #5F7686
analysis, systems, distance, infrastructure, restraint

Moss        #6F7B63
growth, continuity, ecology, patience, slow change

Violet      #8879A8
abstraction, ambiguity, memory, speculation, consciousness

Ochre       #C39A4B
history, accumulation, materiality, craft, sedimented time
```

A pale derivative of the accent may be used as a supporting field.

Use a second full accent only when the text contains a genuine semantic opposition.

Never add colors merely to make the image more colorful.

## 6. Mark system

Use:

```text
one primary mark family
+
no more than two supporting families
```

Primary families:

- cut discs and rings
- offset blocks and slabs
- layered bands
- soft geometric masses
- stepped forms
- elongated tapered masses
- bounded fields
- sparse modular grids

Supporting families:

- thin structural traces
- long arcs
- isolated nodes
- short bars
- dot matrices
- index ticks
- tiny crosshairs
- restrained hatching
- very light screenprint speckle

Do not use everything at once.

## 7. Map semantics to geometry

Treat this as compositional grammar, not an icon library.

```text
hierarchy
→ scale difference, nesting, vertical displacement

causality
→ directional trace, handoff, compression path

recursion / feedback
→ orbit, loop, returning path

accumulation
→ clusters, layered bands, increasing density

loss / decay
→ thinning marks, reduced rhythm, broken continuity

divergence
→ one path splitting

convergence
→ several paths entering one anchor

contrast
→ separated fields, opposing masses, counter-position

threshold
→ boundary, slit, gate, sharp crossing

uncertainty
→ aperture, broken line, unclosed form, soft edge

preservation / invariant
→ persistent mark, baseline, or accent across changing states

translation
→ the same relationship reconstructed with another mark family

time
→ ordered states, spacing rhythm, directional drift

tension
→ off-axis alignment, near-collision, compressed negative space

harmony
→ shared axis, measured distance, stable repetition

fragmentation
→ interrupted blocks and isolated echoes

emergence
→ dispersed marks condensing into a coherent mass

diffusion
→ one mass dissolving into smaller echoes

inversion
→ mirror, rotation, directional reversal

layering
→ overlaps, flat translucent planes, nested boundaries
```

## 8. Composition

Do not fill the canvas.

Default target:

```text
55%–75% visually quiet area
```

A typical composition has:

- one dominant anchor
- one secondary tension
- one small distant counterweight
- one readable visual path
- no more than three major groups

Prefer asymmetric balance.

Let some elements nearly touch while others remain deliberately far apart.

Allow the visual center of gravity to differ from the geometric center.

Negative space carries meaning.

Do not mechanically distribute elements evenly.

## 9. Signature micro-motif: Index Marks

A few key regions may contain subtle **Index Marks**:

- two or three short ticks near a focal edge
- a tiny crosshair
- a partial registration line
- a short measured baseline
- a small offset node

These marks suggest observation, calibration, and structured thought.

They are not data.

Never attach invented numerical measurements.

Use sparingly.

## 10. Texture

Texture belongs inside selected forms, not across the whole background.

Prefer:

- subtle dry-screenprint speckle
- delicate stippling
- short restrained hatch
- slightly imperfect pigment edges

Atmosphere should come primarily from:

```text
negative space
distance
scale
pause
boundary
repetition
asymmetry
limited color
```

Do not use noise to rescue weak composition.

## 11. Text strategy

These images support writing; they should not reprint the writing.

### Header

Prefer:

```text
0–6 words
```

Often no text at all.

Do not bake the article title into the image unless requested.

### Chapter Summary

Use only very short labels when they materially improve comprehension.

### Explanatory Illustration

Use labels, numbers, equations, or symbols only when exact reading is part of the job.

If the current image model is unreliable with text, reduce text in the image and let the article carry the explanation.

### Atmospheric Interlude

No text by default.

Never generate:

- fake quotes
- invented statistics
- dates not present in the source
- decorative English phrases in a non-English article
- fake academic labels
- lorem ipsum
- unreadable microtype

## 12. Semantic distance

Use a five-level scale:

```text
1 = structural diagram
2 = conceptual explanation
3 = editorial abstraction
4 = atmospheric abstraction
5 = almost pure non-representational mood
```

Never use level 5 for explanatory work.

Avoid level 1 for a hero unless the article itself is diagrammatic.

When the user asks for "more abstract", increase semantic distance by roughly one level while preserving the core relation.

When the user asks for "clearer", decrease semantic distance before adding more text.

## 13. Content fidelity

The document is the semantic source of truth.

New **visual metaphors** are allowed.

New **factual claims** are not.

For explanatory images:

- every major relationship must trace back to the document
- do not invent numbers
- do not fabricate charts
- do not show causation when the text only states correlation
- do not turn uncertainty into certainty
- do not add people, places, products, devices, or technologies merely to make the image more concrete

Atmospheric work may be freer, but its emotional logic must still come from the text.

Do not create a generic abstract wallpaper that could accompany any article.

## 14. Anti-slop rules

Never default to:

- glowing brains
- AI circuitry
- robot heads
- human/robot handshakes
- light bulbs
- laptops with floating icons
- generic skylines
- puzzle pieces
- gears
- random isometric cubes
- glassmorphism cards
- blue-purple tech glow
- fake dashboards
- stock infographic icons
- meaningless arrows
- unjustified mandalas
- random equations
- decorative dot matrices
- full-canvas paper texture
- excessive explanatory labels
- unrequested poster slogans

Do not make the image look like a slide deck.

Do not make it look like a stock illustration marketplace asset.

Do not imitate the signature style of a known technology company.

## 15. Multi-image continuity

When generating several images for the same article, share:

- background
- structural ink
- primary accent
- primary mark family
- one recurring micro-motif
- similar texture restraint

But vary:

- composition
- anchor scale
- trace direction
- negative-space placement
- local rhythm

The Header should be the most iconic and least explanatory.

Explanatory images should be the most precise.

Atmospheric images should be the quietest.

The complete set should feel like one publication issue rather than unrelated prompts.

## 16. Final internal check before generation

Confirm internally:

1. the image has one primary job
2. the anchor represents the article's core relation, not a random attractive object
3. the trace has semantic meaning
4. the void has a role
5. the echo comes from the text
6. the palette matches the semantic temperature
7. no major decoration is source-free
8. the article has not been forced into a generic infographic
9. no new factual claim was invented
10. the composition still works if all optional text is removed
11. negative space is sufficient
12. at first glance it reads as a complete editorial artwork; at second glance the article structure begins to emerge

## 17. Output

If image generation is available:

**Generate the finished image directly.**

Do not output your internal semantic analysis, Visual DNA, candidate compositions, or long explanation unless the user explicitly requests them.

If several images are requested, generate a coherent series sharing one Visual DNA.

When revising an existing image, preserve the established Visual DNA and modify only the requested variables, such as:

- semantic distance
- density
- negative space
- color temperature
- compositional tension
- text amount
- aspect ratio
- relative weight of Anchor / Trace / Void / Echo

Do not restart with an unrelated style without a clear request.
