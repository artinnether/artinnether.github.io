"""Render the original PDF figures recorded in paper_thumbnails.json.

Requires pdfplumber (including its PDFium renderer) and Pillow.
Coordinates are PDF points from the top-left; page numbers are one-based.
Shared crops contain mathematical notation without language-specific prose.
"""

import json
from pathlib import Path

import pdfplumber

ROOT = Path(__file__).resolve().parents[1]


def main():
    papers = json.loads((ROOT / "tools/paper_thumbnails.json").read_text())
    for paper in papers:
        for variant in paper["variants"].values():
            with pdfplumber.open(ROOT / variant["pdf"]) as pdf:
                page = pdf.pages[variant["page"] - 1]
                crop = page.crop(tuple(variant["bbox"]))
                image = crop.to_image(resolution=200, antialias=True).original
                output = ROOT / variant["image"]
                output.parent.mkdir(parents=True, exist_ok=True)
                image.save(output, optimize=True)
                print(output.relative_to(ROOT))


if __name__ == "__main__":
    main()
