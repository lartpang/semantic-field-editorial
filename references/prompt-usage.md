# Prompt Usage

The two standalone prompts can be used outside Codex, including in ChatGPT image-generation workflows.

## Contents

- Choose the standalone prompt
- Use it in ChatGPT on the web
- Chinese template
- English template
- Generate a coherent series
- Revise an existing image
- Troubleshoot manual generation

## Choose the standalone prompt

Start with exactly one language-matched prompt:

- Chinese source: `semantic-field-editorial-prompt.zh-CN.md`
- English source: `semantic-field-editorial-prompt.en.md`

Paste the selected standalone prompt before the source document and request block. Do not combine both language prompts.

## Use it in ChatGPT on the web

ChatGPT can create images from a conversational request, accept uploaded reference images, and edit generated or uploaded images. Depending on the current interface, start in a normal conversation or choose the image-creation entry point.

Recommended workflow:

1. Start a new conversation.
2. Paste the language-matched standalone prompt.
3. Paste the complete article inside `[DOCUMENT]`, or upload the article and identify it as the sole semantic source.
4. Append a `[REQUEST]` block.
5. Ask for an illustration plan and Visual DNA before rendering when you want to review the direction.
6. Generate the hero first.
7. After approving the hero, generate each remaining asset separately in the same conversation.
8. Use the approved hero as a style reference, not as an edit target.
9. Revise one variable at a time.

To upload a file or visual reference, use the attachment control in the prompt area, drag the file into the conversation, or paste an image when supported. If the article is long or contains critical formulas, include the decisive passages in the message as well so the image is not based on a partial extraction.

## Chinese template

Append this after the full Chinese prompt:

```text
[DOCUMENT]

# 文章标题

这里粘贴完整文章或章节正文。

[/DOCUMENT]

[REQUEST]
type: header
count: 1
aspect_ratio: 2:1
platform: blog
language: zh-CN
must_preserve:
- 核心概念 A
- 核心关系 B
avoid:
- 人物
- 具象产品
[/REQUEST]

请直接生成最终图片。
```

For automatic article illustration planning:

```text
[REQUEST]
type: auto
count: auto
platform: wechat
language: zh-CN
[/REQUEST]

请阅读完整文章，只选择真正有视觉价值的位置，并建立统一 Visual DNA。
输出一套适合公众号长文的插图。
```

For an uploaded Chinese article:

```text
Treat the uploaded file "文章标题.md" as the complete and sole semantic source.
Read it fully before selecting illustration points.

[REQUEST]
type: auto
count: auto
platform: wechat
language: zh-CN
must_preserve:
- 核心概念 A
- A 与 B 的方向关系
avoid:
- 人物
- 大脑
- 嵌入文字
[/REQUEST]

First return the illustration jobs, ratios, and shared Visual DNA.
Do not generate until I confirm.
```

## English template

Append this after the English standalone prompt:

```text
[DOCUMENT]

# Article title

Paste the full article or section here.

[/DOCUMENT]

[REQUEST]
type: atmosphere
count: 1
aspect_ratio: 3:2
platform: blog
language: en
must_preserve:
- uncertainty
- slow convergence
avoid:
- people
- literal screens
[/REQUEST]

Generate the finished image directly.
```

## Generate a coherent series

Generate one distinct asset per turn rather than asking for all unrelated compositions in one image-generation request.

After approving the hero, use:

```text
The attached/previous hero is a style reference, not an edit target.
Reuse its background, ink, primary accent, principal mark family,
texture restraint, and recurring index motif.

Create a new 3:2 chapter illustration for the section below.
Give it a visibly different composition and a lower semantic distance.
Do not repeat the hero layout.
```

For the next asset, restate its single job and the variables that must remain stable. If style begins to drift, attach the approved hero again or attach a contact sheet of approved images.

Recommended series order:

```text
plan and Visual DNA
→ approve hero
→ generate summaries or explanatory figures one by one
→ compare the full series
→ revise only the drifting asset
```

## Revise an existing image

### Useful revision requests

```text
Keep the same Visual DNA, but increase semantic distance from 2 to 3.
```

```text
Keep the same composition family, remove all embedded text, and increase negative space.
```

```text
Make the figure more explanatory without turning it into a slide or card-based infographic.
```

```text
Preserve Anchor and Void, but change the Trace from a loop to a one-way drift because the article describes irreversible change rather than feedback.
```

Use explicit invariants for localized edits:

```text
Remove only the arrowhead at the right end and replace it with a smooth tapered line ending.
Keep the composition, colors, texture, nodes, negative space, and aspect ratio unchanged.
```

```text
Change only the primary accent from Mineral #5F7686 to Moss #6F7B63.
Do not change any shape, spacing, crop, background, or line geometry.
```

If exact text, formulas, or relation geometry remains unreliable after one focused revision, stop iterating the raster image and rebuild that figure as SVG.

## Troubleshoot manual generation

- **The model illustrates the first paragraph immediately:** require a full-document read and request planning only before rendering.
- **The series drifts:** generate one image per turn and reattach an approved hero or contact sheet as a style reference.
- **The result looks like an infographic:** increase semantic distance and remove cards, labels, arrows, and one-to-one noun mapping.
- **The mechanism is unclear:** lower semantic distance; if correctness matters, request SVG.
- **The aspect ratio is wrong:** set the ratio in the image UI when available and state `exact 2:1` or `exact 3:2` at both the beginning and end of the request.
- **Pseudo-text appears:** state `no text, no letters, no numbers`; if text is required, minimize it and verify it manually.
- **The uploaded article was only partially understood:** paste the decisive section and formulas into the message, then ask the model to restate the source-grounded relation before generating.
