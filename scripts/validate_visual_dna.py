#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

if len(sys.argv) != 2:
    print("Usage: validate_visual_dna.py <visual-dna.json>")
    raise SystemExit(2)

try:
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
except (OSError, json.JSONDecodeError) as exc:
    print(f"Could not read valid JSON: {exc}")
    raise SystemExit(1)

if not isinstance(data, dict):
    print("Visual DNA must be a JSON object")
    raise SystemExit(1)

required = {
    "style", "background", "ink", "primary_accent", "anchor_family",
    "trace_family", "echo_family", "void_behavior", "texture", "density",
    "semantic_distance", "recurring_motif",
}
optional = {"secondary_accent", "job_semantic_distance", "notes"}
errors = []

missing = sorted(required - data.keys())
unknown = sorted(data.keys() - required - optional)
if missing:
    errors.append("Missing keys: " + ", ".join(missing))
if unknown:
    errors.append("Unknown keys: " + ", ".join(unknown))
if data.get("style") != "semantic-field":
    errors.append("style must be semantic-field")

hex_re = re.compile(r"^#[0-9A-Fa-f]{6}$")
for key in ("background", "ink", "primary_accent"):
    value = data.get(key)
    if not isinstance(value, str) or not hex_re.fullmatch(value):
        errors.append(f"{key} must be a 6-digit hex color")

secondary = data.get("secondary_accent")
if secondary is not None and (
    not isinstance(secondary, str) or not hex_re.fullmatch(secondary)
):
    errors.append("secondary_accent must be null or a 6-digit hex color")

for key in (
    "anchor_family", "trace_family", "echo_family", "void_behavior",
    "texture", "recurring_motif",
):
    value = data.get(key)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{key} must be a non-empty string")

if data.get("density") not in {"very-low", "low", "medium", "high"}:
    errors.append("density must be very-low, low, medium, or high")

def valid_distance(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and 1 <= value <= 5

if not valid_distance(data.get("semantic_distance")):
    errors.append("semantic_distance must be a number between 1 and 5")

job_distances = data.get("job_semantic_distance")
allowed_jobs = {"header", "chapter_summary", "explanatory", "atmosphere"}
if job_distances is not None:
    if not isinstance(job_distances, dict):
        errors.append("job_semantic_distance must be an object")
    else:
        extra_jobs = sorted(job_distances.keys() - allowed_jobs)
        if extra_jobs:
            errors.append("Unknown job_semantic_distance keys: " + ", ".join(extra_jobs))
        for job, value in job_distances.items():
            if job in allowed_jobs and not valid_distance(value):
                errors.append(f"job_semantic_distance.{job} must be between 1 and 5")

if "notes" in data and not isinstance(data["notes"], str):
    errors.append("notes must be a string")

if errors:
    print("Visual DNA validation failed:")
    for error in errors:
        print(" -", error)
    raise SystemExit(1)

print("Visual DNA validation: OK")
