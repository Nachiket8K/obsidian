import argparse
import re
import time
from collections import deque
from pathlib import Path
from urllib.parse import urljoin, urlsplit, urlunsplit, unquote

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md
from tqdm import tqdm

VAULT_PATH = Path(__file__).resolve().parent
OUT_DIR = VAULT_PATH / "Python Library Documentation"
OUT_DIR.mkdir(parents=True, exist_ok=True)

LIBRARIES = {
    "simpy": {
        "name": "SimPy",
        "start_url": "https://simpy.readthedocs.io/en/latest/",
        "allowed_prefixes": ["https://simpy.readthedocs.io/en/"],
    },
    "mesa": {
        "name": "Mesa",
        "start_url": "https://mesa.readthedocs.io/latest/",
        "allowed_prefixes": ["https://mesa.readthedocs.io/"],
    },
    "pandas": {
        "name": "pandas",
        "start_url": "https://pandas.pydata.org/docs/",
        "allowed_prefixes": ["https://pandas.pydata.org/docs/"],
    },
}

SKIP_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico",
    ".pdf", ".zip", ".tar", ".gz", ".tgz", ".bz2", ".xml", ".txt",
    ".css", ".js", ".json", ".woff", ".woff2", ".ttf", ".eot",
}

SKIP_URL_PATTERNS = [
    r"/search\.html$",
    r"/genindex\.html$",
    r"/py-modindex\.html$",
    r"/_sources/",
    r"/_static/",
    r"/_images/",
    r"/_downloads/",
]

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0 personal Obsidian documentation import; contact: your-email@example.com"
})


def safe_filename(text: str) -> str:
    text = re.sub(r"[\\/:*?\"<>|]", "", text)
    text = re.sub(r"\s+", " ", text).strip().strip(".")
    return text[:180] or "untitled"


def normalize_url(url: str) -> str:
    parts = urlsplit(url)
    path = parts.path or "/"
    return urlunsplit((parts.scheme, parts.netloc, path, "", ""))


def candidate_start_urls(library: str) -> list[str]:
    slug = library.lower().strip()
    return [
        f"https://{slug}.readthedocs.io/en/latest/",
        f"https://{slug}.readthedocs.io/latest/",
        f"https://{slug}.readthedocs.io/",
        f"https://{slug}.pydata.org/docs/",
        f"https://{slug}.org/documentation/stable/",
        f"https://{slug}.org/docs/",
        f"https://docs.{slug}.org/",
    ]


def allowed_prefixes_for(url: str) -> list[str]:
    parts = urlsplit(normalize_url(url))
    path = parts.path.rstrip("/")
    prefix = urlunsplit((parts.scheme, parts.netloc, f"{path}/" if path else "/", "", ""))
    return [prefix]


def probe_start_url(url: str) -> str | None:
    try:
        response = session.get(url, timeout=20, allow_redirects=True)
        response.raise_for_status()
    except requests.RequestException:
        return None

    content_type = response.headers.get("Content-Type", "").lower()
    if "html" not in content_type:
        return None

    return normalize_url(response.url)


def resolve_library_config(args) -> tuple[str, str, list[str]]:
    key = args.library.lower()

    if key in LIBRARIES:
        config = LIBRARIES[key]
        return config["name"], config["start_url"], config["allowed_prefixes"]

    if args.start_url:
        return args.library, args.start_url, args.allowed_prefixes or [args.start_url]

    tried_urls = []
    for candidate in candidate_start_urls(args.library):
        tried_urls.append(candidate)
        resolved_url = probe_start_url(candidate)
        if resolved_url:
            return args.library, resolved_url, allowed_prefixes_for(resolved_url)

    tried = "\n".join(f"- {url}" for url in tried_urls)
    raise SystemExit(
        "Could not auto-detect a documentation root for "
        f"'{args.library}'. Try again with --start-url.\nChecked:\n{tried}"
    )


def should_visit(url: str, allowed_prefixes: list[str]) -> bool:
    normalized = normalize_url(url)
    if not any(normalized.startswith(prefix.rstrip("/")) for prefix in allowed_prefixes):
        return False

    lowered = normalized.lower()
    if any(re.search(pattern, lowered) for pattern in SKIP_URL_PATTERNS):
        return False
    if any(lowered.endswith(suffix) for suffix in SKIP_SUFFIXES):
        return False
    return True


def get_soup(url: str) -> BeautifulSoup:
    response = session.get(url, timeout=30)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def content_root(soup: BeautifulSoup):
    selectors = [
        "main",
        "article",
        "div[role='main']",
        ".bd-article",
        ".bd-main .bd-content",
        ".document",
        ".rst-content",
        ".content",
    ]
    for selector in selectors:
        node = soup.select_one(selector)
        if node:
            return node
    return soup.body or soup


def extract_title(root, url: str) -> str:
    heading = root.find(["h1", "h2"])
    if heading:
        return heading.get_text(" ", strip=True)

    title_tag = root.find("title")
    if title_tag:
        return title_tag.get_text(" ", strip=True)

    return urlsplit(url).path.rsplit("/", 1)[-1] or "index"


def clean_markdown(text: str) -> str:
    text = re.sub(r"\[¶\]\([^\)]*\)", "", text)
    text = re.sub(r"\[#\]\([^\)]*\)", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def extract_page(url: str) -> tuple[str, str, list[str]]:
    soup = get_soup(url)
    root = content_root(soup)

    for tag in root.select("script, style, nav, footer, header, aside, form, button"):
        tag.decompose()

    for tag in root.select(".headerlink, .toc-backref, .copybtn, .copy, .sidebar, .admonition-title"):
        tag.decompose()

    title = extract_title(root, url)
    markdown = clean_markdown(md(str(root), heading_style="ATX", bullets="-"))

    links = []
    for anchor in soup.find_all("a", href=True):
        full_url = normalize_url(urljoin(url, anchor["href"]))
        links.append(full_url)

    return title, markdown, links


def url_to_note_path(url: str, start_url: str, library_dir: Path) -> Path:
    start_parts = urlsplit(start_url)
    page_parts = urlsplit(url)

    base_path = start_parts.path.rstrip("/")
    page_path = page_parts.path

    if page_path.startswith(base_path):
        relative = page_path[len(base_path):].strip("/")
    else:
        relative = page_path.strip("/")

    if relative.endswith(".html"):
        relative = relative[:-5]

    if relative.endswith("/index"):
        relative = relative[:-6].strip("/")

    if not relative:
        parts = ["Home"]
    else:
        parts = [safe_filename(unquote(part).replace("_", " ")) for part in relative.split("/") if part]

    return library_dir.joinpath(*parts).with_suffix(".md")


def obsidian_link(path: Path, root: Path) -> str:
    return str(path.relative_to(root).with_suffix("")).replace("\\", "/")


def library_index_path(library_dir: Path, name: str) -> Path:
    return library_dir / f"{safe_filename(name)} Documentation.md"


def crawl_library(name: str, start_url: str, allowed_prefixes: list[str], delay: float, max_pages: int | None):
    library_dir = OUT_DIR / safe_filename(name)
    library_dir.mkdir(parents=True, exist_ok=True)
    index_path = library_index_path(library_dir, name)

    queue = deque([normalize_url(start_url)])
    seen = set()
    saved_paths = []

    progress = tqdm(total=max_pages, desc=f"Importing {name}", unit="page")

    while queue and (max_pages is None or len(seen) < max_pages):
        url = queue.popleft()
        if url in seen or not should_visit(url, allowed_prefixes):
            continue

        seen.add(url)

        try:
            title, markdown, links = extract_page(url)
            note_path = url_to_note_path(url, start_url, library_dir)
            note_path.parent.mkdir(parents=True, exist_ok=True)

            frontmatter = f"""---
title: \"{title.replace('"', '\\"')}\"
source: \"{url}\"
imported_from: \"Python library documentation\"
library: \"{name}\"
---

"""

            note = frontmatter + markdown + f"\n\n---\n\nOriginal source: {url}\n"
            note_path.write_text(note, encoding="utf-8")
            saved_paths.append(note_path)

            for link in links:
                if link not in seen and should_visit(link, allowed_prefixes):
                    queue.append(link)

            progress.update(1)
            time.sleep(delay)
        except Exception as exc:
            print(f"Failed: {url} -> {exc}")

    progress.close()

    index_lines = [
        f"# {name} Documentation",
        "",
        f"Source root: {start_url}",
        f"Imported pages: {len(saved_paths)}",
        "",
    ]

    for path in sorted(saved_paths):
        index_lines.append(f"- [[{obsidian_link(path, library_dir)}]]")

    index_path.write_text("\n".join(index_lines) + "\n", encoding="utf-8")
    return library_dir, len(saved_paths)


def parse_args():
    parser = argparse.ArgumentParser(description="Import Python library documentation into the Obsidian vault.")
    parser.add_argument("library", help="Known library key like 'simpy' or 'mesa', or a custom label.")
    parser.add_argument("--start-url", help="Documentation root URL for custom imports.")
    parser.add_argument("--allowed-prefix", action="append", dest="allowed_prefixes", help="Allowed URL prefix. Can be repeated.")
    parser.add_argument("--delay", type=float, default=0.2, help="Delay between requests in seconds.")
    parser.add_argument("--max-pages", type=int, default=None, help="Optional cap for imported pages.")
    return parser.parse_args()


def main():
    args = parse_args()
    name, start_url, allowed_prefixes = resolve_library_config(args)

    library_dir, imported_pages = crawl_library(
        name=name,
        start_url=start_url,
        allowed_prefixes=allowed_prefixes,
        delay=args.delay,
        max_pages=args.max_pages,
    )

    print(f"Imported {imported_pages} pages into: {library_dir}")


if __name__ == "__main__":
    main()
