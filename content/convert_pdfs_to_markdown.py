import argparse
import re
from pathlib import Path

from markitdown import MarkItDown

ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "PDF Markdown Imports"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def safe_filename(text: str) -> str:
    text = re.sub(r"[\\/:*?\"<>|]", "", text)
    text = re.sub(r"\s+", " ", text).strip().strip(".")
    return text[:180] or "untitled"


def resolve_pdf_path(path_str: str) -> Path:
    pdf_path = Path(path_str)
    if not pdf_path.is_absolute():
        pdf_path = ROOT / pdf_path
    return pdf_path.resolve()


def markdown_path_for(pdf_path: Path) -> Path:
    return OUT_DIR / f"{safe_filename(pdf_path.stem)}.md"


def convert_pdf(pdf_path: Path) -> Path:
    converter = MarkItDown()
    result = converter.convert(str(pdf_path))
    out_path = markdown_path_for(pdf_path)

    title = pdf_path.stem.replace('"', '\\"')
    source_pdf = pdf_path.name.replace('"', '\\"')
    content = f"""---
title: \"{title}\"
source_pdf: \"{source_pdf}\"
converted_with: \"markitdown\"
tags:
  - pdf-import
---

{result.text_content}
"""
    out_path.write_text(content, encoding="utf-8")
    return out_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Convert one PDF to Markdown with MarkItDown.")
    parser.add_argument("pdf", help="PDF file path relative to the vault root or absolute path.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    pdf_path = resolve_pdf_path(args.pdf)

    if not pdf_path.exists():
        raise SystemExit(f"PDF not found: {pdf_path}")
    if pdf_path.suffix.lower() != ".pdf":
        raise SystemExit(f"Not a PDF file: {pdf_path}")

    out_path = markdown_path_for(pdf_path)
    if out_path.exists():
        print(f"Skipped existing: {out_path.name}")
        return

    try:
        convert_pdf(pdf_path)
        print(f"Converted: {pdf_path.name}")
        print(f"Saved to: {out_path}")
    except Exception as exc:
        raise SystemExit(f"Failed to convert {pdf_path.name}: {exc}")


if __name__ == "__main__":
    main()
