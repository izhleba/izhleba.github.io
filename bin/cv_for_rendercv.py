"""Convert the site CV data (`_data/cv.yml`) to the schema expected by RenderCV 2.x.

The al-folio CV page reads `label`, `image` and `summary` from `cv.yml`, while
RenderCV 2.x expects `headline` and no `image`/`summary` (the summary becomes a
regular section). This script writes a RenderCV-compatible copy next to the
source file, so relative paths in `assets/rendercv/settings.yaml` keep working.
"""

import argparse
from pathlib import Path
from typing import Any, Dict

import yaml


def convert(data: Dict[str, Any]) -> Dict[str, Any]:
    cv: Dict[str, Any] = data["cv"]

    label = cv.pop("label", None)
    if label:
        cv["headline"] = label

    cv.pop("image", None)

    summary = cv.pop("summary", None)
    sections: Dict[str, Any] = cv.get("sections", {})
    if summary:
        cv["sections"] = {"Summary": [summary], **sections}

    return data


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=Path("_data/cv.yml"))
    parser.add_argument("--output", type=Path, default=Path("_data/.cv_rendercv.yml"))
    args = parser.parse_args()

    with args.source.open(encoding="utf-8") as f:
        data = yaml.safe_load(f)

    with args.output.open("w", encoding="utf-8") as f:
        yaml.safe_dump(convert(data), f, sort_keys=False, allow_unicode=True)

    print(f"Wrote {args.output}")


if __name__ == "__main__":
    main()
