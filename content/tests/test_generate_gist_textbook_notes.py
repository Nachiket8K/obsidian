from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from generate_gist_textbook_notes import (  # noqa: E402
    GistTopic,
    build_reusable_note,
    build_topic_source_note,
    clean_raw_heading,
    curation_specs,
    discover_topics,
    extract_learning_outcomes,
    extract_related_topics,
    extract_summary_paragraphs,
    infer_domain,
    infer_tags,
    merge_existing_note,
    parse_frontmatter,
    parse_gist_topic,
    topic_output_path,
)


class TestGenerateGistTextbookNotes(unittest.TestCase):
    def test_parse_frontmatter_returns_metadata_and_body(self) -> None:
        text = "\n".join(
            [
                "---",
                'topic_code: "AM-06-081"',
                'source: "https://example.org"',
                "---",
                "",
                "# [AM-06-081] GIS-Based Computational Modeling",
                "Body paragraph.",
            ]
        )
        frontmatter, body = parse_frontmatter(text)
        self.assertEqual(frontmatter["topic_code"], "AM-06-081")
        self.assertIn("Body paragraph.", body)

    def test_clean_raw_heading_removes_code_and_markdown(self) -> None:
        self.assertEqual(clean_raw_heading("# [AM-06-081] GIS-Based Computational Modeling"), "GIS-Based Computational Modeling")
        self.assertEqual(clean_raw_heading("## **[DM-01-092] Geospatial Knowledge Graphs**"), "Geospatial Knowledge Graphs")

    def test_infer_domain_uses_folder_structure(self) -> None:
        relative = Path("DM Data Management/DM-01-092 Geospatial Knowledge Graphs.md")
        self.assertEqual(infer_domain(relative, {"topic_code": "DM-01-092"}), ("DM", "Data Management"))

    def test_extract_summary_related_and_learning_outcomes(self) -> None:
        body = "\n".join(
            [
                "# [GS-02-025] Spatial Decision Support",
                "Spatial decision support helps structure geographic decisions.",
                "",
                "## Related topics",
                "- [[AM-03-013] Multi-Criteria Evaluation](/current/concept/AM-03-013)",
                "",
                "## Learning outcomes",
                "- [**53 - Characterize the role of GIS as a generator for SDSS**](/current/learningoutcome/show/50485)",
                "",
            ]
        )
        self.assertIn("structure geographic decisions", extract_summary_paragraphs(body))
        self.assertEqual(extract_related_topics(body), ["[AM-03-013] Multi-Criteria Evaluation"])
        self.assertEqual(extract_learning_outcomes(body), ["53 - Characterize the role of GIS as a generator for SDSS"])

    def test_topic_output_path_preserves_relative_structure(self) -> None:
        topic = GistTopic(
            raw_path=Path("GIS&T Body of Knowledge/AM Analytics and Modeling/AM-06-081 GIS-Based Computational Modeling.md"),
            relative_raw_path=Path("AM Analytics and Modeling/AM-06-081 GIS-Based Computational Modeling.md"),
            mirrored_path=Path("current/source/GIS&T Body of Knowledge/AM Analytics and Modeling/AM-06-081 GIS-Based Computational Modeling.md"),
            title="GIS-Based Computational Modeling",
            raw_heading="# [AM-06-081] GIS-Based Computational Modeling",
            topic_code="AM-06-081",
            domain_code="AM",
            domain_name="Analytics and Modeling",
            summary="Summary.",
            body="Body.",
            related_topics=[],
            learning_outcomes=[],
            tags=[],
        )
        mirror_root = Path("current/source/GIS&T Body of Knowledge")
        self.assertEqual(topic_output_path(topic, mirror_root), mirror_root / topic.relative_raw_path)

    def test_infer_tags_is_deterministic_for_python_and_knowledge_graph_topics(self) -> None:
        python_topic = GistTopic(
            raw_path=Path("a.md"),
            relative_raw_path=Path("PD Programming and Development/PD-05-011 Python for GIS.md"),
            mirrored_path=Path("b.md"),
            title="Python for GIS",
            raw_heading="# [PD-05-011] Python for GIS",
            topic_code="PD-05-011",
            domain_code="PD",
            domain_name="Programming and Development",
            summary="Python and GeoPandas support GIS workflows.",
            body="GeoPandas and PySAL appear in the Python stack.",
            related_topics=[],
            learning_outcomes=[],
            tags=[],
        )
        kg_topic = GistTopic(
            raw_path=Path("a.md"),
            relative_raw_path=Path("DM Data Management/DM-01-092 Geospatial Knowledge Graphs.md"),
            mirrored_path=Path("b.md"),
            title="Geospatial Knowledge Graphs",
            raw_heading="# [DM-01-092] Geospatial Knowledge Graphs",
            topic_code="DM-01-092",
            domain_code="DM",
            domain_name="Data Management",
            summary="GeoKGs use ontologies and SPARQL.",
            body="Semantic Web standards support graph integration.",
            related_topics=[],
            learning_outcomes=[],
            tags=[],
        )
        self.assertIn("python-gis", infer_tags(python_topic))
        self.assertIn("knowledge-graphs", infer_tags(kg_topic))

    def test_curation_specs_include_create_and_enrich_targets(self) -> None:
        specs = curation_specs()
        self.assertEqual(specs["AM-06-081"][0].merge_mode, "enrich")
        self.assertTrue(any(spec.title == "Python for GIS" and spec.merge_mode == "create" for spec in specs["PD-05-011"]))
        self.assertEqual(specs["AM-03-013"][0].category, "method")

    def test_merge_existing_note_updates_sections_without_duplicates(self) -> None:
        original = "\n".join(
            [
                "---",
                'title: "Spatial decision support"',
                'category: "concept"',
                "tags:",
                "  - concept",
                "  - decision-support",
                "---",
                "",
                "# Spatial decision support",
                "",
                "## Upward links",
                "- [[GIS&T Body of Knowledge - Source]]",
                "",
                "## Downward links",
                "- [[Existing Note]]",
                "- [[GIS&T Body of Knowledge/GS GIS&T and Society/GS-02-025 Spatial Decision Support|GIS&T Spatial Decision Support]]",
                "",
                "## Lateral links",
                "- [[Another Note]]",
                "",
            ]
        )
        with tempfile.TemporaryDirectory() as tmpdir:
            note_path = Path(tmpdir) / "Spatial decision support.md"
            note_path.write_text(original, encoding="utf-8")
            merge_existing_note(
                note_path,
                ["[[GIS&T Body of Knowledge - Source]]", "[[New Source Section]]"],
                ["[[Existing Note]]", "[[New GIS&T Topic]]", "[[current/source/GIS&T Body of Knowledge/GS GIS&T and Society/GS-02-025 Spatial Decision Support|Spatial decision support]]"],
                ["[[Another Note]]", "[[Multi-Criteria Evaluation]]"],
                ["concept", "decision-support", "giscience", "active"],
            )
            merged = note_path.read_text(encoding="utf-8")
        self.assertIn("  - giscience", merged)
        self.assertIn("  - active", merged)
        self.assertIn("- [[New Source Section]]", merged)
        self.assertIn("- [[New GIS&T Topic]]", merged)
        self.assertIn("- [[Multi-Criteria Evaluation]]", merged)
        self.assertIn("[[current/source/GIS&T Body of Knowledge/GS GIS&T and Society/GS-02-025 Spatial Decision Support|GIS&T Spatial Decision Support]]", merged)
        self.assertNotIn("[[GIS&T Body of Knowledge/GS GIS&T and Society/GS-02-025 Spatial Decision Support|GIS&T Spatial Decision Support]]", merged)
        self.assertIn("[[current/source/GIS&T Body of Knowledge/GS GIS&T and Society/GS-02-025 Spatial Decision Support|Spatial decision support]]", merged)
        self.assertEqual(merged.count("[[Existing Note]]"), 1)

    def test_discover_topics_excludes_domain_overview_files(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            raw_root = Path(tmpdir) / "GIS&T Body of Knowledge"
            mirror_root = Path(tmpdir) / "current/source/GIS&T Body of Knowledge"
            domain_dir = raw_root / "AM Analytics and Modeling"
            domain_dir.mkdir(parents=True)
            (domain_dir / "AM Analytics and Modeling.md").write_text(
                "# [AM] Analytics and Modeling\nDomain overview.",
                encoding="utf-8",
            )
            (domain_dir / "AM-06-081 GIS-Based Computational Modeling.md").write_text(
                "\n".join(
                    [
                        "---",
                        'topic_code: "AM-06-081"',
                        "---",
                        "# [AM-06-081] GIS-Based Computational Modeling",
                        "Topic body.",
                    ]
                ),
                encoding="utf-8",
            )
            topics = discover_topics(raw_root, mirror_root)
        self.assertEqual(len(topics), 1)
        self.assertEqual(topics[0].topic_code, "AM-06-081")

    def test_build_topic_source_note_renders_required_sections(self) -> None:
        topic = GistTopic(
            raw_path=REPO_ROOT / "GIS&T Body of Knowledge/GS GIS&T and Society/GS-02-025 Spatial Decision Support.md",
            relative_raw_path=Path("GS GIS&T and Society/GS-02-025 Spatial Decision Support.md"),
            mirrored_path=REPO_ROOT / "current/source/GIS&T Body of Knowledge/GS GIS&T and Society/GS-02-025 Spatial Decision Support.md",
            title="Spatial Decision Support",
            raw_heading="# [GS-02-025] Spatial Decision Support",
            topic_code="GS-02-025",
            domain_code="GS",
            domain_name="GIS&T and Society",
            summary="Spatial decision support connects GIS and structured decision processes.",
            body="Body",
            related_topics=["[AM-03-013] Multi-Criteria Evaluation"],
            learning_outcomes=["Define SDSS"],
            tags=["source", "giscience", "geospatial", "decision-support", "active", "review"],
        )
        note = build_topic_source_note(topic)
        self.assertIn("source_type: living-textbook-topic", note)
        self.assertIn("## Upward links", note)
        self.assertIn("## Summary", note)
        self.assertIn("## Downward links", note)
        self.assertIn("## Related GIS&T topics", note)
        self.assertIn("## Lateral links", note)
        self.assertIn("## Traceability", note)

    def test_build_reusable_note_uses_category_specific_sections(self) -> None:
        topic = GistTopic(
            raw_path=Path("a.md"),
            relative_raw_path=Path("AM Analytics and Modeling/AM-03-013 Multi-Criteria Evaluation.md"),
            mirrored_path=Path("current/source/GIS&T Body of Knowledge/AM Analytics and Modeling/AM-03-013 Multi-Criteria Evaluation.md"),
            title="Multi-Criteria Evaluation",
            raw_heading="# [AM-03-013] Multi-Criteria Evaluation",
            topic_code="AM-03-013",
            domain_code="AM",
            domain_name="Analytics and Modeling",
            summary="MCE evaluates alternatives against multiple criteria.",
            body="Body",
            related_topics=[],
            learning_outcomes=["Compare alternatives using weighted criteria."],
            tags=["source", "giscience", "decision-support", "active", "review"],
        )
        spec = curation_specs()["AM-03-013"][0]
        note = build_reusable_note(spec, topic)
        self.assertIn("category: method", note)
        self.assertIn("## Core ideas", note)
        self.assertNotIn("## Key points", note)

    def test_parse_gist_topic_builds_expected_metadata(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            raw_root = Path(tmpdir) / "GIS&T Body of Knowledge"
            mirror_root = Path(tmpdir) / "current/source/GIS&T Body of Knowledge"
            raw_file = raw_root / "DM Data Management" / "DM-01-092 Geospatial Knowledge Graphs.md"
            raw_file.parent.mkdir(parents=True)
            raw_file.write_text(
                "\n".join(
                    [
                        "---",
                        'source: "https://gistbok-ltb.ucgis.org/current/concept/DM-01-092"',
                        'imported_from: "UCGIS GIS&T Body of Knowledge Living Textbook"',
                        'topic_code: "DM-01-092"',
                        "---",
                        "",
                        "# [DM-01-092] Geospatial Knowledge Graphs",
                        "GeoKGs organize places and relationships in graph form.",
                        "",
                        "## Related topics",
                        "- [[FC-03-001] Foundational Ontologies](/current/concept/FC-03-001)",
                    ]
                ),
                encoding="utf-8",
            )
            topic = parse_gist_topic(raw_file, raw_root, mirror_root)
        self.assertEqual(topic.topic_code, "DM-01-092")
        self.assertEqual(topic.domain_code, "DM")
        self.assertEqual(topic.title, "Geospatial Knowledge Graphs")
        self.assertEqual(topic.related_topics, ["[FC-03-001] Foundational Ontologies"])
        self.assertEqual(topic.mirrored_path, mirror_root / "DM Data Management/DM-01-092 Geospatial Knowledge Graphs.md")


if __name__ == "__main__":
    unittest.main()