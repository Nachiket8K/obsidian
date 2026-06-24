---
title: Brain Repository Guide
---

# Brain Repository Guide

This repository publishes an Obsidian knowledge graph with Quartz to GitHub Pages.

The **actual published site content** lives in [`../content/`](../content/), while this `docs/` page acts as a GitHub-facing guide to the main locations in the vault.

## Top-level locations in `content/`

This page points to every top-level location currently present in `content/`.

### Public notes and files
- [`../content/index.md`](../content/index.md) — published homepage / root map of the vault
- [`../content/Constitution.md`](../content/Constitution.md) — guiding principles for the vault
- [`../content/KnowledgeDesignStandards.md`](../content/KnowledgeDesignStandards.md) — note design and structure standards
- [`../content/convert_pdfs_to_markdown.py`](../content/convert_pdfs_to_markdown.py) — supporting conversion script stored alongside vault content

### Public content directories
- [`../content/current/`](../content/current/)
- [`../content/PDF Markdown Imports/`](../content/PDF%20Markdown%20Imports/)
- [`../content/Python Library Documentation/`](../content/Python%20Library%20Documentation/)

### Private local-only directories
- `content/.obsidian/` — local Obsidian workspace and plugin configuration, intentionally excluded from Git and publishing
- `content/.smart-env/` — local environment/config data, intentionally excluded from Git and publishing

## What gets published

Quartz builds the public site from the Markdown files in [`../content/`](../content/).

That means:
- notes in `content/` are part of the public knowledge graph unless excluded
- private workspace/config folders like `.obsidian` should stay out of Git and out of publication
- local environment/config data like `.smart-env` should also remain untracked

## GitHub Pages deployment notes

- GitHub Pages should deploy from the Quartz build output in `public/`
- The configured site URL is `nachiket8k.github.io/obsidian`
- The repo uses Quartz to transform `content/` into the published site

## Recommended reading order

1. Start with [`../content/index.md`](../content/index.md)
2. Review [`../content/KnowledgeDesignStandards.md`](../content/KnowledgeDesignStandards.md)
3. Review [`../content/Constitution.md`](../content/Constitution.md)
4. Explore the larger collections in [`../content/Python Library Documentation/`](../content/Python%20Library%20Documentation/) and [`../content/PDF Markdown Imports/`](../content/PDF%20Markdown%20Imports/)

## Private folders intentionally excluded from GitHub publishing and Git tracking

- `content/.obsidian/`
- `content/.smart-env/`

These stay local so workspace state, plugin config, and any secret-bearing environment data are not exposed.
