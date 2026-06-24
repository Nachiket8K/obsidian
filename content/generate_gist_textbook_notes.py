from __future__ import annotations

import argparse
import re
import textwrap
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Iterable, Literal

import yaml


WIKI_LINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


VAULT_ROOT = Path(__file__).resolve().parent
RAW_ROOT = VAULT_ROOT / "GIS&T Body of Knowledge"
MIRROR_ROOT = VAULT_ROOT / "current" / "source" / "GIS&T Body of Knowledge"
TOP_SOURCE_HUB_PATH = VAULT_ROOT / "current" / "source" / "GIS&T Body of Knowledge - Source.md"

ROOT_RAW_FILENAMES = {
    "00 GIS Index.md",
    "UCGIS GIS&T Body of Knowledge.md",
}

DOMAIN_FOLDERS: dict[str, tuple[str, str]] = {
    "AM Analytics and Modeling": ("AM", "Analytics and Modeling"),
    "CP Computing Platforms": ("CP", "Computing Platforms"),
    "CV Cartography and Visualization": ("CV", "Cartography and Visualization"),
    "DA Domain Applications": ("DA", "Domain Applications"),
    "DC Data Capture": ("DC", "Data Capture"),
    "DM Data Management": ("DM", "Data Management"),
    "FC Foundational Concepts": ("FC", "Foundational Concepts"),
    "GS GIS&T and Society": ("GS", "GIS&T and Society"),
    "KE Knowledge Economy": ("KE", "Knowledge Economy"),
    "PD Programming and Development": ("PD", "Programming and Development"),
}
DOMAIN_CODE_TO_FOLDER = {code: (folder, name) for folder, (code, name) in DOMAIN_FOLDERS.items()}


@dataclass
class GistTopic:
    raw_path: Path
    relative_raw_path: Path
    mirrored_path: Path
    title: str
    raw_heading: str
    topic_code: str | None
    domain_code: str
    domain_name: str
    summary: str
    body: str
    related_topics: list[str]
    learning_outcomes: list[str]
    tags: list[str]

    def canonical_heading(self) -> str:
        return self.title

    def raw_obsidian_link(self, alias: str | None = None) -> str:
        return obsidian_link(vault_relative(self.raw_path), alias or self.title)

    def mirrored_obsidian_link(self, alias: str | None = None) -> str:
        return obsidian_link(vault_relative(self.mirrored_path), alias or self.title)


@dataclass
class DomainIndex:
    domain_code: str
    domain_name: str
    raw_index_path: Path | None
    output_path: Path
    topics: list[GistTopic]

    def sorted_topics(self) -> list[GistTopic]:
        return sorted(self.topics, key=lambda topic: ((topic.topic_code or "ZZZ"), topic.title.lower()))

    def domain_obsidian_link(self, alias: str | None = None) -> str:
        return obsidian_link(self.output_path.relative_to(VAULT_ROOT), alias or f"{self.domain_code} {self.domain_name}")


@dataclass
class ReusableNoteSpec:
    topic_code: str
    title: str
    note_path: Path
    category: Literal["concept", "method", "application"]
    aliases: list[str]
    base_tags: list[str]
    upward_links: list[str]
    lateral_links: list[str]
    merge_mode: Literal["create", "enrich"]

    def should_create(self) -> bool:
        return self.merge_mode == "create"

    def should_enrich(self) -> bool:
        return self.merge_mode == "enrich"

    def target_obsidian_link(self) -> str:
        return f"[[{self.title}]]"


def vault_relative(path: Path) -> Path:
    candidate = path if path.is_absolute() else (VAULT_ROOT / path)
    return candidate.resolve().relative_to(VAULT_ROOT.resolve())


def parse_frontmatter(markdown: str) -> tuple[dict[str, object], str]:
    if not markdown.startswith("---"):
        return {}, markdown
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n?", markdown, re.DOTALL)
    if not match:
        return {}, markdown
    frontmatter = yaml.safe_load(match.group(1)) or {}
    body = markdown[match.end() :]
    return frontmatter, body


def clean_raw_heading(heading: str) -> str:
    cleaned = re.sub(r"^#+\s*", "", heading).strip()
    cleaned = cleaned.replace("\ufeff", "")
    cleaned = re.sub(r"[*_`#]", "", cleaned)
    cleaned = re.sub(r"^\[[A-Z]{2}(?:-\d{2})?(?:-\d{3})?\]\s*", "", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.strip()


def unique_preserve(items: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        normalized = item.strip()
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        result.append(normalized)
    return result


def infer_domain(relative_raw_path: Path, frontmatter: dict[str, object]) -> tuple[str, str]:
    if len(relative_raw_path.parts) >= 2:
        folder = relative_raw_path.parts[0]
        if folder in DOMAIN_FOLDERS:
            return DOMAIN_FOLDERS[folder]
    topic_code = str(frontmatter.get("topic_code", "")).strip()
    if topic_code:
        domain_code = topic_code.split("-", 1)[0]
        if domain_code in DOMAIN_CODE_TO_FOLDER:
            _, domain_name = DOMAIN_CODE_TO_FOLDER[domain_code]
            return domain_code, domain_name
    if relative_raw_path.name in ROOT_RAW_FILENAMES:
        return "UCGIS", "GIS&T Body of Knowledge"
    raise ValueError(f"Unable to infer domain for {relative_raw_path}")


def extract_summary_paragraphs(body: str) -> str:
    body_without_heading = re.sub(r"\A#.*?\n+", "", body, count=1, flags=re.DOTALL).strip()
    paragraphs = [paragraph.strip() for paragraph in re.split(r"\n\s*\n", body_without_heading) if paragraph.strip()]
    summary_parts: list[str] = []
    for paragraph in paragraphs:
        if paragraph.startswith("## "):
            break
        if paragraph.lower().startswith("original source:"):
            break
        if re.match(r"^(##|###|\*\*\d|\d+\.)", paragraph):
            if summary_parts:
                break
            continue
        if paragraph.startswith("!") or paragraph.startswith("|"):
            continue
        summary_parts.append(re.sub(r"\s+", " ", paragraph))
        if len(" ".join(summary_parts)) >= 650:
            break
    if not summary_parts:
        return "Summary to be refined from the raw GIS&T topic."
    return "\n\n".join(summary_parts[:2])


def normalize_inline_markdown(text: str) -> str:
    normalized = text.strip()
    normalized = normalized.replace("**", "")
    normalized = normalized.replace("\ufeff", "")
    if normalized.startswith("[") and "](" in normalized:
        normalized = normalized[1 : normalized.index("](")]
    normalized = re.sub(r"\[(.*?)\]\([^)]+\)", r"\1", normalized)
    normalized = re.sub(r"\s+", " ", normalized)
    return normalized.strip(" -")


def extract_section_lines(body: str, heading: str) -> list[str]:
    pattern = re.compile(rf"(?ms)^## {re.escape(heading)}.*?\n(.*?)(?=^## |\Z)")
    match = pattern.search(body)
    if not match:
        return []
    lines: list[str] = []
    buffer: list[str] = []
    for raw_line in match.group(1).splitlines():
        line = raw_line.rstrip()
        if not line.strip():
            continue
        if line.lstrip().startswith("- "):
            if buffer:
                lines.append(normalize_inline_markdown(" ".join(buffer)))
                buffer = []
            buffer = [line.lstrip()[2:].strip()]
        elif buffer:
            buffer.append(line.strip())
    if buffer:
        lines.append(normalize_inline_markdown(" ".join(buffer)))
    return unique_preserve(lines)


def extract_related_topics(body: str) -> list[str]:
    return extract_section_lines(body, "Related topics")


def extract_learning_outcomes(body: str) -> list[str]:
    return extract_section_lines(body, "Learning outcomes")


def topic_output_path(topic: GistTopic, mirror_root: Path) -> Path:
    output_path = mirror_root / topic.relative_raw_path
    output_path.relative_to(mirror_root)
    return output_path


def infer_tags(topic: GistTopic) -> list[str]:
    corpus = f"{topic.title} {topic.summary} {topic.body}".lower()
    tags = ["source", "giscience", "geospatial", "active", "review"]
    if any(token in corpus for token in ("simulation", "modeling", "scenario", "agent-based", "cellular automata")):
        tags.append("simulation")
    if any(token in corpus for token in ("decision support", "decision-making", "multi-criteria", "location-allocation", "suitability")):
        tags.append("decision-support")
    if any(token in corpus for token in ("knowledge graph", "semantic web", "ontology", "sparql", "geokg")):
        tags.append("knowledge-graphs")
    if any(token in corpus for token in ("python", "geopandas", "pysal", "jupyter", "arcpy", "qgis")):
        tags.append("python-gis")
    if "participatory" in corpus:
        tags.append("participatory-modeling")
    if "agent-based" in corpus:
        tags.append("agent-based-modeling")
    if topic.domain_code == "DM":
        tags.append("data-management")
    if topic.domain_code == "PD":
        tags.append("programming")
    return unique_preserve(tags)


def obsidian_target(path: Path) -> str:
    return vault_relative(path).as_posix().removesuffix(path.suffix)


def obsidian_link(path: Path, alias: str | None = None) -> str:
    target = obsidian_target(path)
    if alias:
        return f"[[{target}|{alias}]]"
    return f"[[{target}]]"


def canonicalize_link_item(item: str) -> str:
    stripped = item.strip()
    bullet = "- " if stripped.startswith("- ") else ""
    content = stripped[2:] if bullet else stripped
    match = WIKI_LINK_RE.fullmatch(content)
    if not match:
        return f"{bullet}{content}" if bullet else content
    target, alias = match.groups()
    if target.startswith("GIS&T Body of Knowledge/"):
        mirrored_target = f"current/source/{target}"
        if alias:
            return f"{bullet}[[{mirrored_target}|{alias}]]"
        return f"{bullet}[[{mirrored_target}]]"
    if target.startswith(("current/concept/", "current/method/", "current/application/")):
        display = alias or PurePosixPath(target).name
        return f"{bullet}[[{display}]]"
    if alias:
        return f"{bullet}[[{target}|{alias}]]"
    return f"{bullet}[[{target}]]"


def is_self_link_item(item: str, note_title: str) -> bool:
    stripped = item.strip()
    content = stripped[2:] if stripped.startswith("- ") else stripped
    match = WIKI_LINK_RE.fullmatch(content)
    if not match:
        return False
    target, alias = match.groups()
    if target.startswith("current/source/"):
        return False
    target_name = PurePosixPath(target).name
    display_name = alias or target_name
    return target_name == note_title or display_name == note_title


def is_domain_overview_relative_path(relative_raw_path: Path) -> bool:
    return (
        len(relative_raw_path.parts) >= 2
        and relative_raw_path.parts[0] in DOMAIN_FOLDERS
        and relative_raw_path.name == f"{relative_raw_path.parts[0]}.md"
    )


def normalize_section_items(items: list[str], note_title: str) -> list[str]:
    normalized = [canonicalize_link_item(item) for item in items]
    filtered = [item for item in normalized if not is_self_link_item(item, note_title)]
    return unique_preserve(filtered)


def domain_hub_path(domain_code: str, mirror_root: Path) -> Path:
    folder, _ = DOMAIN_CODE_TO_FOLDER[domain_code]
    return mirror_root / folder / f"{folder}.md"


def root_overview_path(mirror_root: Path) -> Path:
    return mirror_root / "UCGIS GIS&T Body of Knowledge.md"


def curated_links_for_topic(topic_code: str | None) -> list[str]:
    if not topic_code:
        return []
    links: list[str] = []
    for spec in curation_specs().get(topic_code, []):
        links.append(spec.target_obsidian_link())
    return unique_preserve(links)


def inferred_lateral_links(topic: GistTopic) -> list[str]:
    links: list[str] = []
    title = topic.title.lower()
    if "decision support" in title or "multi-criteria" in title or "location-allocation" in title:
        links.extend(["[[Spatial decision support]]", "[[Decision-support framework]]"])
    if "knowledge graph" in title:
        links.extend(["[[Geospatial knowledge graphs]]", "[[KnowledgeDesignStandards]]"])
    if "python" in title:
        links.extend(["[[Geospatial analysis in Python]]", "[[GeoPandas]]", "[[pandas]]"])
    if "agent-based" in title:
        links.extend(["[[Agent-based modeling]]", "[[Mesa framework]]"])
    if "computational modeling" in title or "simulation" in title:
        links.extend(["[[GIS-based computational modeling]]", "[[Exploratory modeling]]"])
    if "participatory" in title:
        links.extend(["[[Spatial decision support]]", "[[GIS Participatory Modeling]]"])
    links.extend(curated_links_for_topic(topic.topic_code))
    return unique_preserve(links)


def build_topic_source_note(topic: GistTopic) -> str:
    aliases = unique_preserve(
        [
            topic.raw_heading.replace("# ", "").strip(),
            topic.topic_code or "",
        ]
    )
    downlinks = curated_links_for_topic(topic.topic_code)
    downlinks.extend(f"- Learning outcome: {outcome}" for outcome in topic.learning_outcomes[:5])
    if not downlinks:
        downlinks = ["- None promoted yet."]
    else:
        downlinks = [item if item.startswith("-") else f"- {item}" for item in downlinks]
    related = [f"- {item}" for item in topic.related_topics] or ["- None extracted from the raw topic."]
    laterals = [f"- {item}" for item in inferred_lateral_links(topic)] or ["- None added yet."]
    upward_links = [
        "- [[GIS&T Body of Knowledge - Source]]",
        f"- {obsidian_link(root_overview_path(MIRROR_ROOT).relative_to(VAULT_ROOT), 'Mirrored GIS&T overview')}",
        f"- {obsidian_link(domain_hub_path(topic.domain_code, MIRROR_ROOT).relative_to(VAULT_ROOT), f'{topic.domain_code} {topic.domain_name}')}",
    ]
    frontmatter = {
        "title": topic.title,
        "aliases": aliases,
        "category": "source",
        "source_type": "living-textbook-topic",
        "book": "GIS&T Body of Knowledge",
        "topic_code": topic.topic_code,
        "domain_code": topic.domain_code,
        "domain_name": topic.domain_name,
        "raw_source_path": topic.relative_raw_path.as_posix().join(["GIS&T Body of Knowledge/"]) if False else f"GIS&T Body of Knowledge/{topic.relative_raw_path.as_posix()}",
        "tags": topic.tags,
    }
    traceability = [
        f"- Raw note: {topic.raw_obsidian_link('Raw GIS&T topic')}",
        f"- Mirrored from: `GIS&T Body of Knowledge/{topic.relative_raw_path.as_posix()}`",
    ]
    if topic.topic_code:
        traceability.append(f"- Topic code: `{topic.topic_code}`")
    return render_markdown(frontmatter, topic.title, {
        "Upward links": upward_links,
        "Summary": [topic.summary],
        "Downward links": downlinks,
        "Related GIS&T topics": related,
        "Lateral links": laterals,
        "Traceability": traceability,
    })


def build_domain_hub(domain_index: DomainIndex) -> str:
    topic_links = [f"- {topic.mirrored_obsidian_link(topic.title)}" for topic in domain_index.sorted_topics()]
    curated = unique_preserve(link for topic in domain_index.sorted_topics() for link in curated_links_for_topic(topic.topic_code))
    curated_lines = [f"- {link}" for link in curated] or ["- None curated yet."]
    sibling_domains = [
        obsidian_link(domain_hub_path(code, MIRROR_ROOT).relative_to(VAULT_ROOT), f"{code} {name}")
        for code, (_, name) in DOMAIN_CODE_TO_FOLDER.items()
        if code != domain_index.domain_code
    ]
    frontmatter = {
        "title": f"{domain_index.domain_code} {domain_index.domain_name}",
        "aliases": [domain_index.domain_code],
        "category": "source",
        "source_type": "living-textbook-domain",
        "book": "GIS&T Body of Knowledge",
        "topic_code": domain_index.domain_code,
        "domain_code": domain_index.domain_code,
        "domain_name": domain_index.domain_name,
        "raw_source_path": f"GIS&T Body of Knowledge/{domain_index.output_path.parent.name}",
        "tags": unique_preserve(["source", "giscience", "geospatial", "active", "review"] + [tag for topic in domain_index.topics for tag in topic.tags if tag not in {"source", "active", "review"}]),
    }
    return render_markdown(frontmatter, f"{domain_index.domain_code} {domain_index.domain_name}", {
        "Upward links": [
            "- [[GIS&T Body of Knowledge - Source]]",
            f"- {obsidian_link(root_overview_path(MIRROR_ROOT).relative_to(VAULT_ROOT), 'Mirrored GIS&T overview')}",
        ],
        "Summary": [
            f"This domain hub mirrors the **{domain_index.domain_name}** branch of the GIS&T Body of Knowledge so its topics can participate in the vault’s source graph without altering the preserved raw textbook folder."
        ],
        "Downward links": topic_links,
        "Related GIS&T topics": curated_lines,
        "Lateral links": [f"- {link}" for link in sibling_domains[:6]],
        "Traceability": [f"- Raw domain folder: `GIS&T Body of Knowledge/{domain_index.output_path.parent.name}`"],
    })


def build_root_index(raw_index_path: Path, topics: list[GistTopic]) -> str:
    raw_text = raw_index_path.read_text(encoding="utf-8")
    _, body = parse_frontmatter(raw_text)
    title = clean_raw_heading(next((line for line in body.splitlines() if line.startswith("# ")), raw_index_path.stem))
    summary = extract_summary_paragraphs(body)
    grouped_counts = []
    for folder, (code, name) in DOMAIN_FOLDERS.items():
        count = sum(1 for topic in topics if topic.domain_code == code)
        grouped_counts.append(f"- {obsidian_link(domain_hub_path(code, MIRROR_ROOT).relative_to(VAULT_ROOT), f'{code} {name}')} ({count} topics)")
    frontmatter = {
        "title": title,
        "aliases": [raw_index_path.stem],
        "category": "source",
        "source_type": "living-textbook-index",
        "book": "GIS&T Body of Knowledge",
        "topic_code": None,
        "domain_code": "UCGIS",
        "domain_name": "GIS&T Body of Knowledge",
        "raw_source_path": f"GIS&T Body of Knowledge/{raw_index_path.name}",
        "tags": ["source", "giscience", "geospatial", "active", "review"],
    }
    return render_markdown(frontmatter, title, {
        "Upward links": ["- [[GIS&T Body of Knowledge - Source]]"],
        "Summary": [summary],
        "Downward links": grouped_counts,
        "Related GIS&T topics": [f"- {link}" for link in unique_preserve(link for topic in topics[:12] for link in curated_links_for_topic(topic.topic_code))] or ["- None curated yet."],
        "Lateral links": [
            "- [[Spatial decision support]]",
            "- [[Geospatial analysis in Python]]",
            "- [[GIS-based computational modeling]]",
            "- [[Geospatial knowledge graphs]]",
        ],
        "Traceability": [f"- Raw index note: {obsidian_link(raw_index_path.relative_to(VAULT_ROOT), raw_index_path.stem)}"],
    })


def build_overview_note(raw_path: Path, topics: list[GistTopic]) -> str:
    raw_text = raw_path.read_text(encoding="utf-8")
    _, body = parse_frontmatter(raw_text)
    title = clean_raw_heading(next((line for line in body.splitlines() if line.startswith("# ")), raw_path.stem))
    summary = extract_summary_paragraphs(body)
    high_value_codes = ["AM-06-081", "AM-07-079", "DM-01-092", "GS-02-025", "GS-02-029", "PD-05-011"]
    by_code = {topic.topic_code: topic for topic in topics if topic.topic_code}
    highlights = [f"- {by_code[code].mirrored_obsidian_link(by_code[code].title)}" for code in high_value_codes if code in by_code]
    frontmatter = {
        "title": title,
        "aliases": ["GIS&T Body of Knowledge"],
        "category": "source",
        "source_type": "living-textbook-index",
        "book": "GIS&T Body of Knowledge",
        "topic_code": None,
        "domain_code": "UCGIS",
        "domain_name": "GIS&T Body of Knowledge",
        "raw_source_path": f"GIS&T Body of Knowledge/{raw_path.name}",
        "tags": ["source", "giscience", "geospatial", "active", "review"],
    }
    return render_markdown(frontmatter, title, {
        "Upward links": ["- [[GIS&T Body of Knowledge - Source]]"],
        "Summary": [summary],
        "Downward links": highlights,
        "Related GIS&T topics": [
            f"- {obsidian_link(domain_hub_path(code, MIRROR_ROOT).relative_to(VAULT_ROOT), f'{code} {name}') }"
            for code, (_, name) in DOMAIN_CODE_TO_FOLDER.items()
        ],
        "Lateral links": [
            "- [[DMDU - Source]]",
            "- [[The Delft Method for System Dynamics - Source]]",
            "- [[GeoPandas Documentation - Source]]",
            "- [[Mesa Documentation - Source]]",
        ],
        "Traceability": [f"- Raw overview note: {obsidian_link(raw_path.relative_to(VAULT_ROOT), raw_path.stem)}"],
    })


def curation_specs() -> dict[str, list[ReusableNoteSpec]]:
    current = VAULT_ROOT / "current"
    return {
        "AM-06-081": [
            ReusableNoteSpec(
                topic_code="AM-06-081",
                title="GIS-based computational modeling",
                note_path=current / "concept" / "GIS-based computational modeling.md",
                category="concept",
                aliases=["GIS-Based Computational Modeling"],
                base_tags=["concept", "giscience", "geospatial", "simulation"],
                upward_links=["[[GIS&T Body of Knowledge - Source]]"],
                lateral_links=["[[System dynamics]]", "[[Agent-based modeling]]", "[[Geospatial analysis in Python]]"],
                merge_mode="enrich",
            )
        ],
        "DM-01-092": [
            ReusableNoteSpec(
                topic_code="DM-01-092",
                title="Geospatial knowledge graphs",
                note_path=current / "concept" / "Geospatial knowledge graphs.md",
                category="concept",
                aliases=["GeoKGs"],
                base_tags=["concept", "giscience", "geospatial", "knowledge-graphs"],
                upward_links=["[[GIS&T Body of Knowledge - Source]]"],
                lateral_links=["[[KnowledgeDesignStandards]]", "[[Spatial decision support]]"],
                merge_mode="enrich",
            )
        ],
        "GS-02-025": [
            ReusableNoteSpec(
                topic_code="GS-02-025",
                title="Spatial decision support",
                note_path=current / "concept" / "Spatial decision support.md",
                category="concept",
                aliases=["SDSS"],
                base_tags=["concept", "giscience", "geospatial", "decision-support"],
                upward_links=["[[GIS&T Body of Knowledge - Source]]"],
                lateral_links=["[[Multi-Criteria Evaluation]]", "[[Location-allocation modeling]]", "[[GIS Participatory Modeling]]"],
                merge_mode="enrich",
            )
        ],
        "PD-05-011": [
            ReusableNoteSpec(
                topic_code="PD-05-011",
                title="Geospatial analysis in Python",
                note_path=current / "concept" / "Geospatial analysis in Python.md",
                category="concept",
                aliases=["Python geospatial workflows"],
                base_tags=["concept", "geospatial", "python-gis", "giscience"],
                upward_links=["[[GIS&T Body of Knowledge - Source]]"],
                lateral_links=["[[Python for GIS]]", "[[GeoPandas]]", "[[pandas]]"],
                merge_mode="enrich",
            ),
            ReusableNoteSpec(
                topic_code="PD-05-011",
                title="Python for GIS",
                note_path=current / "concept" / "Python for GIS.md",
                category="concept",
                aliases=["Python GIS"],
                base_tags=["concept", "geospatial", "python-gis", "giscience"],
                upward_links=["[[GIS&T Body of Knowledge - Source]]", "[[GeoPandas Documentation - Source]]"],
                lateral_links=["[[Geospatial analysis in Python]]", "[[GeoPandas]]", "[[pandas]]"],
                merge_mode="create",
            ),
        ],
        "AM-07-079": [
            ReusableNoteSpec(
                topic_code="AM-07-079",
                title="Agent-based modeling",
                note_path=current / "concept" / "Agent-based modeling.md",
                category="concept",
                aliases=["ABM"],
                base_tags=["concept", "agent-based-modeling", "simulation", "giscience"],
                upward_links=["[[GIS&T Body of Knowledge - Source]]"],
                lateral_links=["[[GIS-based computational modeling]]", "[[Mesa framework]]"],
                merge_mode="enrich",
            )
        ],
        "GS-02-029": [
            ReusableNoteSpec(
                topic_code="GS-02-029",
                title="GIS Participatory Modeling",
                note_path=current / "concept" / "GIS Participatory Modeling.md",
                category="concept",
                aliases=["Geospatial participatory modeling"],
                base_tags=["concept", "giscience", "geospatial", "decision-support", "participatory-modeling"],
                upward_links=["[[GIS&T Body of Knowledge - Source]]"],
                lateral_links=["[[Spatial decision support]]", "[[Agent-based modeling]]"],
                merge_mode="create",
            )
        ],
        "AM-03-013": [
            ReusableNoteSpec(
                topic_code="AM-03-013",
                title="Multi-Criteria Evaluation",
                note_path=current / "method" / "Multi-Criteria Evaluation.md",
                category="method",
                aliases=["MCE", "MCDA"],
                base_tags=["method", "giscience", "geospatial", "decision-support"],
                upward_links=["[[GIS&T Body of Knowledge - Source]]"],
                lateral_links=["[[Spatial decision support]]", "[[Location-allocation modeling]]"],
                merge_mode="create",
            )
        ],
        "AM-05-046": [
            ReusableNoteSpec(
                topic_code="AM-05-046",
                title="Location-allocation modeling",
                note_path=current / "method" / "Location-allocation modeling.md",
                category="method",
                aliases=["Location-allocation"],
                base_tags=["method", "giscience", "geospatial", "decision-support"],
                upward_links=["[[GIS&T Body of Knowledge - Source]]"],
                lateral_links=["[[Spatial decision support]]", "[[Multi-Criteria Evaluation]]"],
                merge_mode="create",
            )
        ],
    }


def resolve_existing_note(note_path: Path) -> bool:
    return note_path.exists()


def derive_key_points(topic: GistTopic, maximum: int = 4) -> list[str]:
    if topic.learning_outcomes:
        return [f"- {item.rstrip('.')}" for item in topic.learning_outcomes[:maximum]]
    sentences = re.split(r"(?<=[.!?])\s+", topic.summary)
    points = [sentence.strip() for sentence in sentences if sentence.strip()]
    return [f"- {point}" for point in points[:maximum]] or ["- This note should be further sharpened into an atomic reusable idea."]


def build_reusable_note(spec: ReusableNoteSpec, topic: GistTopic) -> str:
    section_name = "Key points" if spec.category == "concept" else "Core ideas"
    frontmatter = {
        "title": spec.title,
        "category": spec.category,
        "tags": unique_preserve(spec.base_tags + [spec.category, "active", "review"]),
    }
    downward_links = [f"- {topic.mirrored_obsidian_link(topic.title)}"]
    lateral_links = [f"- {link}" for link in unique_preserve(spec.lateral_links + inferred_lateral_links(topic)) if link != spec.target_obsidian_link()]
    return render_markdown(frontmatter, spec.title, {
        "Upward links": [f"- {link}" for link in unique_preserve(spec.upward_links)],
        "Summary": [
            f"{topic.summary} This reusable note promotes the topic into the canonical `{spec.category}` layer so later sources can link here without duplicating the GIS&T source page."
        ],
        "Downward links": downward_links,
        section_name: derive_key_points(topic),
        "Lateral links": lateral_links or ["- None added yet."],
        "Reuse note": [
            f"Use this note when the idea should be referenced as reusable {spec.category}-level knowledge rather than as a GIS&T source-specific reading note."
        ],
    })


def replace_section(body: str, section_name: str, items: list[str]) -> str:
    rendered_items = [item if item.startswith("- ") else f"- {item}" for item in items]
    replacement = f"## {section_name}\n" + "\n".join(rendered_items).rstrip() + "\n\n"
    pattern = re.compile(rf"(?ms)^## {re.escape(section_name)}\n.*?(?=^## |\Z)")
    if pattern.search(body):
        return pattern.sub(replacement, body, count=1)
    body = body.rstrip() + "\n\n"
    return body + replacement


def extract_existing_section_items(body: str, section_name: str) -> list[str]:
    pattern = re.compile(rf"(?ms)^## {re.escape(section_name)}\n(.*?)(?=^## |\Z)")
    match = pattern.search(body)
    if not match:
        return []
    items = [line.strip() for line in match.group(1).splitlines() if line.strip().startswith("- ")]
    return unique_preserve(items)


def merge_existing_note(
    note_path: Path,
    upward_links: list[str],
    downward_links: list[str],
    lateral_links: list[str],
    tags: list[str],
) -> None:
    original = note_path.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(original)
    note_title = str(frontmatter.get("title") or note_path.stem)
    existing_tags = [str(tag) for tag in frontmatter.get("tags", [])]
    frontmatter["tags"] = unique_preserve(existing_tags + tags)
    for section_name, new_items in {
        "Upward links": upward_links,
        "Downward links": downward_links,
        "Lateral links": lateral_links,
    }.items():
        existing_items = extract_existing_section_items(body, section_name)
        combined = normalize_section_items(
            existing_items + [item if item.startswith("- ") else f"- {item}" for item in new_items],
            note_title,
        )
        body = replace_section(body, section_name, combined)
    note_path.write_text(serialize_frontmatter(frontmatter) + "\n" + body.strip() + "\n", encoding="utf-8")


def write_text_if_changed(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    normalized = content.rstrip() + "\n"
    if path.exists() and path.read_text(encoding="utf-8") == normalized:
        return
    path.write_text(normalized, encoding="utf-8")


def write_mirror_tree(topics: list[GistTopic], mirror_root: Path) -> None:
    for topic in topics:
        write_text_if_changed(topic.mirrored_path, build_topic_source_note(topic))
    by_domain: dict[str, list[GistTopic]] = defaultdict(list)
    for topic in topics:
        by_domain[topic.domain_code].append(topic)
    for domain_code, domain_topics in by_domain.items():
        output_path = domain_hub_path(domain_code, mirror_root)
        domain_index = DomainIndex(
            domain_code=domain_code,
            domain_name=domain_topics[0].domain_name,
            raw_index_path=None,
            output_path=output_path,
            topics=domain_topics,
        )
        write_text_if_changed(output_path, build_domain_hub(domain_index))
    write_text_if_changed(mirror_root / "00 GIS Index.md", build_root_index(RAW_ROOT / "00 GIS Index.md", topics))
    write_text_if_changed(mirror_root / "UCGIS GIS&T Body of Knowledge.md", build_overview_note(RAW_ROOT / "UCGIS GIS&T Body of Knowledge.md", topics))


def apply_curation(topics: list[GistTopic], specs: dict[str, list[ReusableNoteSpec]]) -> None:
    topics_by_code = {topic.topic_code: topic for topic in topics if topic.topic_code}
    for topic_code, topic_specs in specs.items():
        topic = topics_by_code.get(topic_code)
        if topic is None:
            continue
        for spec in topic_specs:
            upward_links = unique_preserve(spec.upward_links + ["[[GIS&T Body of Knowledge - Source]]"])
            downward_links = [topic.mirrored_obsidian_link(topic.title)]
            lateral_links = unique_preserve(spec.lateral_links + inferred_lateral_links(topic))
            tags = unique_preserve(spec.base_tags + [spec.category, "active", "review"])
            if spec.should_enrich() and resolve_existing_note(spec.note_path):
                merge_existing_note(spec.note_path, upward_links, downward_links, lateral_links, tags)
            elif spec.should_create() and not resolve_existing_note(spec.note_path):
                write_text_if_changed(spec.note_path, build_reusable_note(spec, topic))
            else:
                merge_existing_note(spec.note_path, upward_links, downward_links, lateral_links, tags)


def build_top_level_source_hub(topics: list[GistTopic]) -> str:
    topic_by_code = {topic.topic_code: topic for topic in topics if topic.topic_code}
    key_codes = ["AM-06-081", "AM-07-079", "GS-02-025", "GS-02-029", "DM-01-092", "PD-05-011"]
    high_value_links = [f"- {topic_by_code[code].mirrored_obsidian_link(topic_by_code[code].title)}" for code in key_codes if code in topic_by_code]
    domain_links = [
        f"- {obsidian_link(domain_hub_path(code, MIRROR_ROOT).relative_to(VAULT_ROOT), f'{code} {name}') }"
        for code, (_, name) in DOMAIN_CODE_TO_FOLDER.items()
    ]
    curated_note_links = unique_preserve(
        spec.target_obsidian_link()
        for topic_specs in curation_specs().values()
        for spec in topic_specs
    )
    frontmatter = {
        "title": "GIS&T Body of Knowledge - Source",
        "aliases": ["UCGIS GIS&T Body of Knowledge", "GIS&T BoK"],
        "source_type": "living-textbook",
        "category": "source",
        "tags": [
            "source",
            "giscience",
            "geospatial",
            "decision-support",
            "simulation",
            "dmdu",
            "system-dynamics",
            "mesa",
            "geopandas",
            "active",
            "review",
        ],
    }
    return render_markdown(frontmatter, "GIS&T Body of Knowledge - Source", {
        "Purpose": [
            "This is the canonical source hub for the **UCGIS GIS&T Body of Knowledge**. It preserves the raw textbook folder as a stable source layer while exposing a mirrored `current/source` subtree and curated reusable notes that connect GIS&T into the wider Obsidian knowledge graph."
        ],
        "Source artifacts": [
            f"- {obsidian_link((RAW_ROOT / 'UCGIS GIS&T Body of Knowledge.md').relative_to(VAULT_ROOT), 'Raw GIS&T BoK overview')}",
            f"- {obsidian_link((RAW_ROOT / '00 GIS Index.md').relative_to(VAULT_ROOT), 'Raw GIS&T index')}",
            f"- {obsidian_link((MIRROR_ROOT / 'UCGIS GIS&T Body of Knowledge.md').relative_to(VAULT_ROOT), 'Mirrored GIS&T BoK overview')}",
            f"- {obsidian_link((MIRROR_ROOT / '00 GIS Index.md').relative_to(VAULT_ROOT), 'Mirrored GIS&T index')}",
        ],
        "Mirrored GIS&T domain hubs": domain_links,
        "High-value GIS&T topic links": high_value_links,
        "Reusable GIS&T bridge notes": [f"- {link}" for link in curated_note_links],
        "Graph bridge links": [
            "- [[DMDU - Source]]",
            "- [[The Delft Method for System Dynamics - Source]]",
            "- [[Mesa Documentation - Source]]",
            "- [[GeoPandas Documentation - Source]]",
            "- [[pandas Documentation - Source]]",
            "- [[Decision-support framework]]",
            "- [[System dynamics]]",
            "- [[Agent-based modeling]]",
            "- [[Exploratory modeling]]",
        ],
        "Linking intent": [
            "- Upward: preserves traceability to the untouched raw GIS&T folder and to the mirrored source subtree.",
            "- Downward: points into mirrored domain/topic notes and the canonical reusable notes promoted from GIS&T topics.",
            "- Lateral: connects GIScience material to DMDU, System Dynamics, Mesa, GeoPandas, and Python workflow notes elsewhere in the vault.",
        ],
    })


def update_top_level_source_hub(topics: list[GistTopic]) -> None:
    write_text_if_changed(TOP_SOURCE_HUB_PATH, build_top_level_source_hub(topics))


def render_markdown(frontmatter: dict[str, object], title: str, sections: dict[str, list[str]]) -> str:
    lines = [serialize_frontmatter(frontmatter).rstrip(), "", f"# {title}", ""]
    for section_name, items in sections.items():
        lines.append(f"## {section_name}")
        if len(items) == 1 and not items[0].startswith("- "):
            lines.append(items[0])
        else:
            lines.extend(items)
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def serialize_frontmatter(frontmatter: dict[str, object]) -> str:
    lines = ["---"]
    for key, value in frontmatter.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            for item in value:
                lines.append(f"  - {item}")
        elif value is None:
            lines.append(f"{key}: null")
        elif isinstance(value, str):
            if any(ch in value for ch in [":", "#", "[", "]", "&", "*"]) or value != value.strip():
                lines.append(f'{key}: "{value}"')
            else:
                lines.append(f"{key}: {value}")
        else:
            lines.append(f"{key}: {value}")
    lines.append("---")
    return "\n".join(lines)


def parse_gist_topic(raw_path: Path, raw_root: Path, mirror_root: Path) -> GistTopic:
    markdown = raw_path.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(markdown)
    relative_raw_path = raw_path.relative_to(raw_root)
    domain_code, domain_name = infer_domain(relative_raw_path, frontmatter)
    heading = next((line for line in body.splitlines() if line.startswith("# ")), raw_path.stem)
    topic_code = str(frontmatter.get("topic_code", "")).strip() or None
    title = clean_raw_heading(heading)
    provisional = GistTopic(
        raw_path=raw_path,
        relative_raw_path=relative_raw_path,
        mirrored_path=mirror_root / relative_raw_path,
        title=title,
        raw_heading=heading.strip(),
        topic_code=topic_code,
        domain_code=domain_code,
        domain_name=domain_name,
        summary=extract_summary_paragraphs(body),
        body=body,
        related_topics=extract_related_topics(body),
        learning_outcomes=extract_learning_outcomes(body),
        tags=[],
    )
    provisional.tags = infer_tags(provisional)
    provisional.mirrored_path = topic_output_path(provisional, mirror_root)
    return provisional


def discover_topics(raw_root: Path, mirror_root: Path) -> list[GistTopic]:
    topics: list[GistTopic] = []
    for raw_path in sorted(raw_root.rglob("*.md")):
        relative_raw_path = raw_path.relative_to(raw_root)
        if raw_path.name in ROOT_RAW_FILENAMES:
            continue
        if len(relative_raw_path.parts) < 2:
            continue
        if is_domain_overview_relative_path(relative_raw_path):
            continue
        topics.append(parse_gist_topic(raw_path, raw_root, mirror_root))
    return topics


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate mirrored GIS&T textbook notes and curated canonical notes.")
    parser.add_argument("--raw-root", type=Path, default=RAW_ROOT)
    parser.add_argument("--mirror-root", type=Path, default=MIRROR_ROOT)
    args = parser.parse_args()

    topics = discover_topics(args.raw_root, args.mirror_root)
    write_mirror_tree(topics, args.mirror_root)
    apply_curation(topics, curation_specs())
    update_top_level_source_hub(topics)


if __name__ == "__main__":
    main()