# Implementation Plan

[Overview]
Integrate the GIS&T textbook into the vault by preserving the raw `GIS&T Body of Knowledge/` folder, generating a mirrored `current/source/GIS&T Body of Knowledge/` source subtree, and surfacing reusable notes into `current/` in line with the Constitution and Knowledge Graph Design Standards.

The current vault already has an established pattern for high-value sources: raw imports remain preserved, canonical source hubs live under `current/source`, and reusable ideas are promoted into `current/concept`, `current/method`, and `current/application`. The GIS&T material partially follows this pattern today. The raw textbook folder is extensive and useful, and there is already a top-level `current/source/GIS&T Body of Knowledge - Source.md` plus a small number of curated bridge notes such as `GIS-based computational modeling`, `Geospatial knowledge graphs`, `Spatial decision support`, and `Geospatial analysis in Python`. However, there is no mirrored structured source subtree under `current/source/GIS&T Body of Knowledge/`, and several important cross-book GIS&T ideas still exist only as raw textbook pages.

The user has clarified that the desired outcome is both preservation and integration: the raw textbook folder must remain canonical and untouched, while a structured mirror should be created inside the note system so GIS&T can participate in the same chapter/topic/source graph that already exists for DMDU, System Dynamics, Simulation in Practice, GeoPandas, and Mesa. That means the implementation should not move or delete the raw `GIS&T Body of Knowledge/` files. Instead, it should create a vault-native source layer that points back to the raw material, provides upward/downward/lateral links, and makes the GIS&T content navigable from inside `current/source`.

Because the GIS&T textbook contains hundreds of topic pages, the implementation should be automated rather than fully manual. The best fit for this vault is a Python generator that reads the raw GIS&T markdown files, extracts topic metadata and summary content, writes mirrored source notes into `current/source/GIS&T Body of Knowledge/`, and then applies a curation map to either enrich existing canonical notes or create a focused set of new reusable notes where the graph currently has gaps. This approach matches the Constitution’s single-source-of-truth rule, the Knowledge Graph Design Standards’ emphasis on links over folders, and the existing use of Python helpers and tests for repeatable note-generation workflows.

[Types]
The implementation needs a small Python data model for GIS&T topic generation plus explicit markdown schemas for mirrored source notes and curated reusable notes.

1. **Mirrored GIS&T source note frontmatter schema** for files under `current/source/GIS&T Body of Knowledge/**/*.md`
   - `title: str`
     - Human-readable topic title without losing the canonical GIS&T wording.
     - Validation: must not be empty.
   - `aliases: list[str]`
     - Includes the bracketed raw heading form (for example `[AM-06-081] GIS-Based Computational Modeling`) and topic-code-only alias (for example `AM-06-081`).
     - Validation: must include at least one alias containing `topic_code`.
   - `category: "source"`
     - Validation: fixed literal.
   - `source_type: "living-textbook-topic" | "living-textbook-domain" | "living-textbook-index"`
     - Topic notes use `living-textbook-topic`, domain hubs use `living-textbook-domain`, and mirrored overview/index notes use `living-textbook-index`.
   - `book: "GIS&T Body of Knowledge"`
     - Validation: fixed literal.
   - `topic_code: str | null`
     - Required for topic and domain notes when a GIS&T code exists.
     - Validation: for topic notes must match patterns like `AM-06-081`, `GS-02-025`, `DM-01-092`, or domain codes like `AM`, `DM`, `GS`.
   - `domain_code: str`
     - One of `UCGIS`, `AM`, `CP`, `CV`, `DA`, `DC`, `DM`, `FC`, `GS`, `KE`, `PD`.
   - `domain_name: str`
     - Human-readable domain name, for example `Analytics and Modeling`.
   - `raw_source_path: str`
     - Vault-relative path to the preserved raw note in `GIS&T Body of Knowledge/...`.
     - Validation: must point to an existing raw markdown file.
   - `tags: list[str]`
     - Must include `source`, `giscience`, `active`, `review`, plus domain-relevant tags such as `geospatial`, `simulation`, `decision-support`, `knowledge-graphs`, or `python-gis`.
   - Required body sections:
     - `# <Title>`
     - `## Upward links`
     - `## Summary`
     - `## Downward links`
     - `## Related GIS&T topics`
     - `## Lateral links`
     - `## Traceability`

2. **Curated reusable note schema** for files under `current/concept/*.md`, `current/method/*.md`, and any new GIS&T-driven reusable notes
   - `title: str`
   - `category: "concept" | "method" | "application"`
   - `tags: list[str]`
     - Must include the category tag and existing vault vocabulary such as `giscience`, `decision-support`, `geospatial`, `dmdu`, `simulation`, or `python-gis`.
   - Required body sections follow existing vault conventions:
     - Concept notes: `Upward links`, `Summary`, `Downward links`, `Key points`, `Lateral links`, `Reuse note`
     - Method notes: `Upward links`, `Summary`, `Downward links`, `Core ideas`, `Lateral links`, `Reuse note`
   - Validation rules:
     - If a canonical note already exists, it must be enriched rather than duplicated.
     - Each reusable note must stay atomic and must not simply restate an entire raw GIS&T topic page.

3. **Python dataclass: `GistTopic`** in `generate_gist_textbook_notes.py`
   - Fields:
     - `raw_path: Path`
     - `relative_raw_path: Path`
     - `mirrored_path: Path`
     - `title: str`
     - `raw_heading: str`
     - `topic_code: str | None`
     - `domain_code: str`
     - `domain_name: str`
     - `summary: str`
     - `body: str`
     - `related_topics: list[str]`
     - `learning_outcomes: list[str]`
     - `tags: list[str]`
   - Relationships:
     - One `GistTopic` maps one raw markdown file to one mirrored source note.
     - A `GistTopic` may optionally map to one curated reusable note via `ReusableNoteSpec`.
   - Validation:
     - `relative_raw_path` must stay inside `GIS&T Body of Knowledge/`.
     - `mirrored_path` must stay inside `current/source/GIS&T Body of Knowledge/`.

4. **Python dataclass: `DomainIndex`** in `generate_gist_textbook_notes.py`
   - Fields:
     - `domain_code: str`
     - `domain_name: str`
     - `raw_index_path: Path | None`
     - `output_path: Path`
     - `topics: list[GistTopic]`
   - Purpose:
     - Represents one domain-level grouping such as `AM Analytics and Modeling` or `DM Data Management`.
   - Validation:
     - `topics` must be sorted deterministically by topic code and title before rendering.

5. **Python dataclass: `ReusableNoteSpec`** in `generate_gist_textbook_notes.py`
   - Fields:
     - `topic_code: str`
     - `title: str`
     - `note_path: Path`
     - `category: Literal["concept", "method", "application"]`
     - `aliases: list[str]`
     - `base_tags: list[str]`
     - `upward_links: list[str]`
     - `lateral_links: list[str]`
     - `merge_mode: Literal["create", "enrich"]`
   - Purpose:
     - Encodes the curation map for topics that should become canonical reusable notes.
   - Validation:
     - `merge_mode="enrich"` requires `note_path` to already exist.
     - `merge_mode="create"` requires `note_path` not to collide with an existing canonical note unless the implementation explicitly falls back to merge.

6. **Curation enum / mapping rules**
   - Existing note enrichment targets:
     - `AM-06-081` -> `current/concept/GIS-based computational modeling.md`
     - `DM-01-092` -> `current/concept/Geospatial knowledge graphs.md`
     - `GS-02-025` -> `current/concept/Spatial decision support.md`
     - `PD-05-011` -> `current/concept/Geospatial analysis in Python.md` and new `current/concept/Python for GIS.md`
     - `AM-07-079` -> `current/concept/Agent-based modeling.md`
   - New canonical note creation targets:
     - `GS-02-029` -> `current/concept/GIS Participatory Modeling.md`
     - `PD-05-011` -> `current/concept/Python for GIS.md`
     - `AM-03-013` -> `current/method/Multi-Criteria Evaluation.md`
     - `AM-05-046` -> `current/method/Location-allocation modeling.md`
   - Validation:
     - The mapping must be explicit and auditable in code rather than inferred from fuzzy string matching alone.

[Files]
The implementation will add an automated GIS&T generator, create a mirrored source subtree under `current/source/GIS&T Body of Knowledge/`, and create or enrich a focused set of reusable notes in `current/`.

Detailed breakdown:

- **New files to be created**
  - `generate_gist_textbook_notes.py`
    - Python automation entry point for GIS&T mirroring and curation.
    - Purpose: parse raw GIS&T markdown, generate mirrored source notes, build domain hubs, and create/enrich selected reusable notes.
  - `tests/test_generate_gist_textbook_notes.py`
    - Unit tests for metadata extraction, mirror path generation, summary extraction, tag inference, curation mapping, and merge behavior.
  - `current/source/GIS&T Body of Knowledge/00 GIS Index.md`
    - Mirrored index note for the raw textbook index, rewritten into vault-native source-note structure.
  - `current/source/GIS&T Body of Knowledge/UCGIS GIS&T Body of Knowledge.md`
    - Mirrored overview note for the textbook root page.
  - `current/source/GIS&T Body of Knowledge/AM Analytics and Modeling/AM Analytics and Modeling.md`
  - `current/source/GIS&T Body of Knowledge/CP Computing Platforms/CP Computing Platforms.md`
  - `current/source/GIS&T Body of Knowledge/CV Cartography and Visualization/CV Cartography and Visualization.md`
  - `current/source/GIS&T Body of Knowledge/DA Domain Applications/DA Domain Applications.md`
  - `current/source/GIS&T Body of Knowledge/DC Data Capture/DC Data Capture.md`
  - `current/source/GIS&T Body of Knowledge/DM Data Management/DM Data Management.md`
  - `current/source/GIS&T Body of Knowledge/FC Foundational Concepts/FC Foundational Concepts.md`
  - `current/source/GIS&T Body of Knowledge/GS GIS&T and Society/GS GIS&T and Society.md`
  - `current/source/GIS&T Body of Knowledge/KE Knowledge Economy/KE Knowledge Economy.md`
  - `current/source/GIS&T Body of Knowledge/PD Programming and Development/PD Programming and Development.md`
    - Domain-level mirrored source hubs for each GIS&T top-level domain.
  - Mirrored topic notes for the raw textbook topic files, using the same relative path convention as the raw source folder, for example:
    - `current/source/GIS&T Body of Knowledge/AM Analytics and Modeling/AM-06-081 GIS-Based Computational Modeling.md`
    - `current/source/GIS&T Body of Knowledge/DM Data Management/DM-01-092 Geospatial Knowledge Graphs.md`
    - `current/source/GIS&T Body of Knowledge/GS GIS&T and Society/GS-02-025 Spatial Decision Support.md`
    - `current/source/GIS&T Body of Knowledge/GS GIS&T and Society/GS-02-029 GIS Participatory Modeling.md`
    - `current/source/GIS&T Body of Knowledge/PD Programming and Development/PD-05-011 Python for GIS.md`
    - and the same mirrored-path rule for the rest of the raw GIS&T topic set.
  - `current/concept/GIS Participatory Modeling.md`
    - New reusable concept note bridging GIS participation, stakeholder-oriented spatial decision support, and policy/process work already present in the vault.
  - `current/concept/Python for GIS.md`
    - New reusable concept note focused on Python as a GIS implementation layer, distinct from but linked to `Geospatial analysis in Python`.
  - `current/method/Multi-Criteria Evaluation.md`
    - New reusable method note to support `Spatial decision support` and other GIS&T decision-analysis links.
  - `current/method/Location-allocation modeling.md`
    - New reusable method note for a core spatial decision-support technique referenced by GIS&T topics.

- **Existing files to be modified**
  - `implementation_plan.md`
    - Replaced with the GIS&T-specific plan document defined here.
  - `current/source/GIS&T Body of Knowledge - Source.md`
    - Add explicit links to the new mirrored source subtree, domain hubs, and curated reusable-note set.
    - Update the source-artifact/navigation sections so the mirrored structure is discoverable from the canonical top-level source note.
  - `current/concept/GIS-based computational modeling.md`
    - Enrich upward/downward/lateral links so the existing canonical note points to the new mirrored GIS&T topic note in `current/source/...` rather than only the raw topic.
  - `current/concept/Geospatial knowledge graphs.md`
    - Add mirrored-source links and any new lateral links created by the GIS&T mirror.
  - `current/concept/Spatial decision support.md`
    - Add mirrored-source links plus curated method links such as `Multi-Criteria Evaluation` and `Location-allocation modeling`.
  - `current/concept/Geospatial analysis in Python.md`
    - Add or refine links to the mirrored `PD-05-011 Python for GIS` source note and the new canonical `Python for GIS` note.
  - `current/concept/Agent-based modeling.md`
    - Add mirrored GIS&T source linkage for `AM-07-079 Agent-based Modeling` if that link is not already present through existing lateral structure.

- **Files to be preserved but not moved**
  - `GIS&T Body of Knowledge/**/*.md`
    - Remains the untouched raw canonical source layer.
    - The implementation must treat this folder as read-only input for generation.

- **Files to be deleted or moved**
  - None.
  - The Constitution explicitly discourages destructive cleanup, and the user asked to preserve the raw folder while also creating an integrated mirror.

- **Configuration file updates**
  - None expected.
  - The implementation should rely on existing Python dependencies and vault structure.

[Functions]
The implementation requires a new Python generator with explicit parsing, rendering, and merge functions rather than ad hoc manual editing.

Detailed breakdown:

- **New functions** in `generate_gist_textbook_notes.py`
  - `parse_frontmatter(markdown: str) -> tuple[dict[str, object], str]`
    - Parse YAML frontmatter from raw GIS&T markdown and return metadata plus body content.
  - `clean_raw_heading(heading: str) -> str`
    - Normalize bracketed GIS&T headings into stable human-readable titles while preserving codes for aliases.
  - `parse_gist_topic(raw_path: Path, raw_root: Path, mirror_root: Path) -> GistTopic`
    - Convert one raw GIS&T markdown file into a structured `GistTopic` record.
  - `infer_domain(relative_raw_path: Path, frontmatter: dict[str, object]) -> tuple[str, str]`
    - Resolve `domain_code` and `domain_name` from folder structure and/or `topic_code`.
  - `extract_summary_paragraphs(body: str) -> str`
    - Extract the best short summary from the first explanatory paragraphs of a raw topic page.
  - `extract_related_topics(body: str) -> list[str]`
    - Parse the `## Related topics` section into normalized links or topic-code/title strings.
  - `extract_learning_outcomes(body: str) -> list[str]`
    - Parse the `## Learning outcomes` section for optional source-note downward links or traceability sections.
  - `infer_tags(topic: GistTopic) -> list[str]`
    - Derive stable source tags from topic code, domain, and title keywords.
  - `topic_output_path(topic: GistTopic, mirror_root: Path) -> Path`
    - Build the mirrored vault path in `current/source/GIS&T Body of Knowledge/...`.
  - `build_topic_source_note(topic: GistTopic) -> str`
    - Render a mirrored topic note using the required source-note schema.
  - `build_domain_hub(domain_index: DomainIndex) -> str`
    - Render each domain-level hub note with upward/downward/lateral structure.
  - `build_root_index(raw_index_path: Path, topics: list[GistTopic]) -> str`
    - Render the mirrored root index or overview note for the source subtree.
  - `curation_specs() -> dict[str, ReusableNoteSpec]`
    - Return the explicit topic-to-canonical-note mapping.
  - `resolve_existing_note(note_path: Path) -> bool`
    - Determine whether a curated target should be created or enriched.
  - `build_reusable_note(spec: ReusableNoteSpec, topic: GistTopic) -> str`
    - Render the body of a newly created canonical concept or method note.
  - `merge_existing_note(note_path: Path, upward_links: list[str], downward_links: list[str], lateral_links: list[str], tags: list[str]) -> None`
    - Enrich an existing note without duplicating links or tags and without disturbing its existing narrative structure.
  - `write_mirror_tree(topics: list[GistTopic], mirror_root: Path) -> None`
    - Create directories and write mirrored topic/domain/root notes.
  - `apply_curation(topics: list[GistTopic], specs: dict[str, ReusableNoteSpec]) -> None`
    - Create missing canonical notes and enrich existing ones.
  - `main() -> None`
    - CLI entry point to run the full workflow.

- **Modified functions**
  - None are required in existing scripts such as `convert_pdfs_to_markdown.py` or `import_python_library_docs.py`.
  - The GIS&T workflow should be isolated in its own script to avoid coupling unrelated import pipelines.

- **Removed functions**
  - None.

[Classes]
The implementation benefits from a small set of focused Python dataclasses that make the generator deterministic, testable, and easy to extend.

Detailed breakdown:

- **New classes** in `generate_gist_textbook_notes.py`
  - `class GistTopic`
    - File path: `generate_gist_textbook_notes.py`
    - Purpose: represent one raw GIS&T topic/page together with its mirrored-source metadata and parsed content.
    - Key methods:
      - `canonical_heading() -> str`
      - `raw_obsidian_link() -> str`
      - `mirrored_obsidian_link() -> str`
    - Inheritance: standard `@dataclass`, no custom inheritance.
  - `class DomainIndex`
    - File path: `generate_gist_textbook_notes.py`
    - Purpose: group topics into domain-level hubs such as `AM`, `DM`, or `GS`.
    - Key methods:
      - `sorted_topics() -> list[GistTopic]`
      - `domain_obsidian_link() -> str`
    - Inheritance: standard `@dataclass`, no custom inheritance.
  - `class ReusableNoteSpec`
    - File path: `generate_gist_textbook_notes.py`
    - Purpose: define how a GIS&T topic should map into a canonical reusable note in `current/`.
    - Key methods:
      - `should_create() -> bool`
      - `should_enrich() -> bool`
      - `target_obsidian_link() -> str`
    - Inheritance: standard `@dataclass`, no custom inheritance.

- **Modified classes**
  - None.

- **Removed classes**
  - None.

[Dependencies]
No new external dependencies should be introduced; the implementation should use the existing Python environment and standard-library-first parsing/rendering.

Details of dependency handling:

- Reuse the installed Python runtime already used by the other vault scripts.
- Prefer standard library modules such as `argparse`, `dataclasses`, `pathlib`, `re`, and `collections`.
- If YAML parsing is needed beyond a minimal manual parser, rely on the already-installed `PyYAML` present in `requirements.txt` rather than adding another frontmatter package.
- No network calls are required because all GIS&T source material already exists locally.
- No changes are required to `requirements.txt`.

[Testing]
Testing should verify that the GIS&T mirror is structurally correct, non-destructive, and semantically aligned with the existing knowledge graph.

Test file requirements, modifications, and validation strategy:

- Create `tests/test_generate_gist_textbook_notes.py`.
- Add unit tests for:
  - frontmatter parsing from raw GIS&T pages;
  - topic-code extraction and domain inference;
  - mirrored output-path generation;
  - summary extraction from introductory paragraphs;
  - related-topic extraction;
  - deterministic tag inference;
  - duplicate-safe link merging for existing canonical notes;
  - curation-map behavior for `create` versus `enrich` targets.
- Validate representative mirrored-note rendering for at least:
  - `AM-06-081 GIS-Based Computational Modeling`
  - `DM-01-092 Geospatial Knowledge Graphs`
  - `GS-02-025 Spatial Decision Support`
  - `PD-05-011 Python for GIS`
- Validate that the generator preserves the raw folder unchanged.
- Validate that no duplicate canonical note is created for already-existing notes such as:
  - `current/concept/GIS-based computational modeling.md`
  - `current/concept/Geospatial knowledge graphs.md`
  - `current/concept/Spatial decision support.md`
  - `current/concept/Geospatial analysis in Python.md`
  - `current/concept/Agent-based modeling.md`
- After generation, run targeted repository searches to confirm:
  - mirrored notes exist under `current/source/GIS&T Body of Knowledge/`;
  - the top-level source note points to the mirrored subtree;
  - new reusable notes exist only where expected;
  - existing reusable notes gained GIS&T upward/downward/lateral links without losing prior links.

[Implementation Order]
The implementation should establish the generator and mirrored source structure first, then layer curation on top so reusable-note enrichment always points to stable mirrored-source targets.

1. Create `generate_gist_textbook_notes.py` with the core dataclasses (`GistTopic`, `DomainIndex`, `ReusableNoteSpec`) and CLI scaffolding.
2. Add `tests/test_generate_gist_textbook_notes.py` covering parsing, path generation, summary extraction, and merge logic before writing the full mirror.
3. Implement raw GIS&T parsing and mirror-path generation for overview notes, domain hubs, and topic pages.
4. Generate the mirrored source subtree under `current/source/GIS&T Body of Knowledge/`, preserving the raw relative-path structure and leaving `GIS&T Body of Knowledge/` untouched.
5. Update `current/source/GIS&T Body of Knowledge - Source.md` so it navigates to the new mirror rather than pointing only at the raw folder.
6. Implement the explicit curation map for existing reusable notes and for missing canonical notes (`GIS Participatory Modeling`, `Python for GIS`, `Multi-Criteria Evaluation`, `Location-allocation modeling`).
7. Run the curation layer to enrich existing canonical notes (`GIS-based computational modeling`, `Geospatial knowledge graphs`, `Spatial decision support`, `Geospatial analysis in Python`, `Agent-based modeling`) and create the missing reusable notes.
8. Validate frontmatter, note structure, link integrity, and non-duplication through the new tests and targeted repository searches.
9. Perform a final review against `Constitution.md` and `KnowledgeDesignStandards.md` to confirm raw-source preservation, atomic reusable notes, and a link-first graph structure.