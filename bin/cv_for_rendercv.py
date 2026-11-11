"""Convert the site CV data (`_data/cv.yml`) to the schema expected by RenderCV 2.x.

The al-folio CV page reads `label`, `image` and `summary` from `cv.yml`, while
RenderCV 2.x expects `headline` and no `image`/`summary` (the summary becomes a
regular section). Skill groups, languages and the education `studyType` field are
also mapped to RenderCV entry types, and the design file is embedded. This script writes a RenderCV-compatible copy next to the
source file, so relative paths in `assets/rendercv/settings.yaml` keep working.
"""

import argparse
from pathlib import Path
from typing import Any, Dict, List, Union

import yaml


def convert_skills(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Turn site skill groups (name/icon/keywords) into RenderCV one-line entries."""
    return [{"label": entry["name"], "details": entry.get("keywords", "")} for entry in entries]


def convert_languages(entries: List[Dict[str, Any]]) -> List[str]:
    """Collapse the language list into a single line of text."""
    parts = [f"{entry['name']} ({entry['summary']})" if entry.get("summary") else entry["name"] for entry in entries]
    return [" · ".join(parts)]


def convert_education(entries: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Show the site-only `studyType` field as a highlight under the entry."""
    converted: List[Dict[str, Any]] = []
    for entry in entries:
        entry = dict(entry)
        study_type: Union[str, None] = entry.pop("studyType", None)
        if study_type:
            entry["highlights"] = [study_type] + list(entry.get("highlights", []))
        converted.append(entry)
    return converted


def convert(data: Dict[str, Any], design_path: Union[Path, None] = None) -> Dict[str, Any]:
    cv: Dict[str, Any] = data["cv"]

    label = cv.pop("label", None)
    if label:
        cv["headline"] = label

    cv.pop("image", None)

    summary = cv.pop("summary", None)
    sections: Dict[str, Any] = cv.get("sections", {})

    if "Skills" in sections:
        sections["Skills"] = convert_skills(sections["Skills"])
    if "Languages" in sections:
        sections["Languages"] = convert_languages(sections["Languages"])
    if "Education" in sections:
        sections["Education"] = convert_education(sections["Education"])

    if summary:
        cv["sections"] = {"Summary": [summary], **sections}

    # Embed the design directly: it is the most reliable way to make RenderCV apply it.
    if design_path is not None and design_path.exists():
        with design_path.open(encoding="utf-8") as f:
            design = yaml.safe_load(f) or {}
        if "design" in design:
            data["design"] = design["design"]

    return data


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("_data/cv.yml"))
    parser.add_argument("--output", type=Path, default=Path("_data/.cv_rendercv.yml"))
    parser.add_argument("--design", type=Path, default=Path("assets/rendercv/design.yaml"))
    args = parser.parse_args()

    with args.source.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)

    with args.output.open("w", encoding="utf-8") as f:
        yaml.safe_dump(convert(data, args.design), f, sort_keys=False, allow_unicode=True)

    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
