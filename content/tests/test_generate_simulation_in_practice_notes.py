from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from Obsidian.generate_simulation_in_practice_notes import (
    clean_heading,
    extract_chapter_title,
    generate_section_summary,
    infer_section_level,
    match_numbered_heading,
    merge_existing_note,
    parse_section_nodes,
    unique_preserve,
    ChapterContext,
)


class TestGenerateSimulationInPracticeNotes(unittest.TestCase):
    def test_clean_heading_removes_markdown_and_footnotes(self) -> None:
        self.assertEqual(clean_heading("## **Chapter 16[1]** "), "Chapter 16")
        self.assertEqual(clean_heading("## _6.1 Introduction_ "), "6.1 Introduction")

    def test_extract_chapter_title_handles_dual_heading(self) -> None:
        text = "\n".join(
            [
                "## **Chapter 6**",
                "## **The Workstation**",
                "## _6.1 Introduction_",
            ]
        )
        self.assertEqual(extract_chapter_title(text, "07 Chapter 6"), (6, "The Workstation"))

    def test_match_numbered_heading_supports_nested_and_appendix_formats(self) -> None:
        self.assertEqual(
            match_numbered_heading("## 6.3.3.1 Analytic Model of a Single Workstation"),
            ("6.3.3.1", "Analytic Model of a Single Workstation"),
        )
        self.assertEqual(
            match_numbered_heading("## **A.2. AutoMod Modeling Elements**"),
            ("A.2", "AutoMod Modeling Elements"),
        )
        self.assertEqual(
            match_numbered_heading("## **A-3. Tutorial – Model Building**"),
            ("A-3", "Tutorial - Model Building"),
        )

    def test_infer_section_level_uses_number_depth(self) -> None:
        self.assertEqual(infer_section_level("6.3"), 1)
        self.assertEqual(infer_section_level("6.3.3"), 2)
        self.assertEqual(infer_section_level("6.3.3.1"), 3)
        self.assertEqual(infer_section_level("A.2"), 1)
        self.assertEqual(infer_section_level("A-3"), 1)

    def test_parse_section_nodes_slices_nested_sections(self) -> None:
        text = "\n".join(
            [
                "## **Chapter 6**",
                "## **The Workstation**",
                "## _6.3 The Case Study_",
                "Overview paragraph.",
                "## 6.3.1 Define the Issues and Solution Objective",
                "Issue paragraph.",
                "## 6.3.3 Identify Root Causes and Assess Initial Alternatives",
                "Assess paragraph.",
                "## 6.3.3.1 Analytic Model of a Single Workstation",
                "Analytic paragraph.",
                "## 6.3.3.2 Simulation Analysis of the Single Workstation",
                "Simulation paragraph.",
                "## 6.3.4 Review and Extend Previous Work",
                "Review paragraph.",
            ]
        )
        nodes = parse_section_nodes(text, 6, Path("chapter6.md"))
        labels = [node.number_label for node in nodes]
        self.assertEqual(labels, ["6.3", "6.3.1", "6.3.3", "6.3.3.1", "6.3.3.2", "6.3.4"])
        parents = {node.number_label: node.parent_label for node in nodes}
        self.assertIsNone(parents["6.3"])
        self.assertEqual(parents["6.3.1"], "6.3")
        self.assertEqual(parents["6.3.3.1"], "6.3.3")
        analytic = next(node for node in nodes if node.number_label == "6.3.3.1")
        self.assertEqual(analytic.level, 3)
        self.assertIn("Analytic paragraph.", analytic.content)
        self.assertNotIn("Simulation paragraph.", analytic.content)

    def test_unique_preserve_deduplicates_without_reordering(self) -> None:
        self.assertEqual(unique_preserve(["a", "b", "a", "c", "b"]), ["a", "b", "c"])

    def test_generate_section_summary_uses_repeated_case_study_template(self) -> None:
        chapter = ChapterContext(
            number=6,
            part="Basic Organizations for Systems",
            chapter_title="The Workstation",
            chapter_aliases=["The Workstation"],
            source_path=Path("chapter6.md"),
            summary="",
            tags=[],
            bridge_links=[],
            application_links=[],
            section_nodes=[],
        )
        node = parse_section_nodes(
            "\n".join(
                [
                    "## 6.3.1 Define the Issues and Solution Objective",
                    "A lean team has been studying the operation of a particular workstation.",
                ]
            ),
            6,
            Path("chapter6.md"),
        )[0]
        summary = generate_section_summary(node, chapter)
        self.assertIn("operational problem", summary.lower())

    def test_merge_existing_note_updates_links_and_tags(self) -> None:
        original = "\n".join(
            [
                "---",
                'title: "Verification and validation"',
                "category: \"concept\"",
                "tags:",
                "  - concept",
                "  - validation",
                "---",
                "",
                "# Verification and validation",
                "",
                "## Downward links",
                "- [[Existing Note]]",
                "",
                "## Lateral links",
                "- [[Another Note]]",
                "",
            ]
        )
        with tempfile.TemporaryDirectory() as tmpdir:
            path = Path(tmpdir) / "Verification and validation.md"
            path.write_text(original, encoding="utf-8")
            merge_existing_note(
                path,
                ["[[Existing Note]]", "[[New Source Section]]"],
                ["[[Another Note]]", "[[New Related Note]]"],
                ["concept", "validation", "simulation", "active"],
            )
            merged = path.read_text(encoding="utf-8")
        self.assertIn("  - simulation", merged)
        self.assertIn("  - active", merged)
        self.assertIn("- [[New Source Section]]", merged)
        self.assertIn("- [[New Related Note]]", merged)
        self.assertEqual(merged.count("[[Existing Note]]"), 1)


if __name__ == "__main__":
    unittest.main()