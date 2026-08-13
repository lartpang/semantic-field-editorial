#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = ROOT.name
REQUIRED = {
    "SKILL.md", "README.md", "LICENSE.md", "agents/openai.yaml",
    "references/prompt-usage.md", "references/rendering-and-qa.md",
    "references/semantic-field-editorial-prompt.en.md",
    "references/semantic-field-editorial-prompt.zh-CN.md",
    "references/visual-dna.schema.json", "references/visual-language.md",
    "scripts/validate_package.py", "scripts/validate_visual_dna.py",
}
errors = []

for relative_path in sorted(REQUIRED):
    if not (ROOT / relative_path).is_file():
        errors.append(f"Missing required file: {relative_path}")

skill_path = ROOT / "SKILL.md"
skill_text = ""
if skill_path.is_file():
    skill_text = skill_path.read_text(encoding="utf-8")
    lines = skill_text.splitlines()
    if len(lines) > 500:
        errors.append(f"SKILL.md has {len(lines)} lines; keep it at or below 500")
    if not lines or lines[0] != "---":
        errors.append("SKILL.md must start with YAML frontmatter")
    else:
        try:
            closing = lines.index("---", 1)
        except ValueError:
            errors.append("SKILL.md frontmatter has no closing delimiter")
        else:
            fields = {}
            for line in lines[1:closing]:
                match = re.fullmatch(r"([a-z_]+):\s*(.+)", line)
                if not match:
                    errors.append(f"Malformed frontmatter line: {line}")
                    continue
                fields[match.group(1)] = match.group(2).strip()
            if set(fields) != {"name", "description"}:
                errors.append("SKILL.md frontmatter must contain only name and description")
            if fields.get("name") != SKILL_NAME:
                errors.append("Frontmatter name must match the skill directory name")
            if not fields.get("description"):
                errors.append("Frontmatter description must not be empty")

    references = set(re.findall(r"`((?:references|scripts)/[^`\s]+)`", skill_text))
    for relative_path in sorted(references):
        if not (ROOT / relative_path).is_file():
            errors.append(f"SKILL.md references a missing file: {relative_path}")

if not re.fullmatch(r"[a-z0-9-]{1,64}", SKILL_NAME):
    errors.append("Skill directory name must be 1-64 lowercase letters, digits, or hyphens")

openai_path = ROOT / "agents" / "openai.yaml"
if openai_path.is_file():
    openai_text = openai_path.read_text(encoding="utf-8")
    def quoted_field(name):
        match = re.search(rf'^\s*{name}:\s*"([^"]*)"\s*$', openai_text, re.MULTILINE)
        return match.group(1) if match else None

    display_name = quoted_field("display_name")
    short_description = quoted_field("short_description")
    default_prompt = quoted_field("default_prompt")
    if not display_name:
        errors.append("agents/openai.yaml display_name must be a quoted non-empty string")
    if short_description is None or not 25 <= len(short_description) <= 64:
        errors.append("agents/openai.yaml short_description must be quoted and 25-64 characters")
    if default_prompt is None or f"${SKILL_NAME}" not in default_prompt:
        errors.append("agents/openai.yaml default_prompt must be quoted and mention the skill")

if errors:
    print("Semantic Field Editorial package validation failed:")
    for error in errors:
        print(" -", error)
    raise SystemExit(1)

print("Semantic Field Editorial package validation: OK")
