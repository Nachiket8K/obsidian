---
title: Triangular Irregular Network (TIN) Models
aliases:
  - "[DM-02-010] Triangular Irregular Network (TIN) Models"
  - DM-02-010
category: source
source_type: living-textbook-topic
book: "GIS&T Body of Knowledge"
topic_code: DM-02-010
domain_code: DM
domain_name: Data Management
raw_source_path: "GIS&T Body of Knowledge/DM Data Management/DM-02-010 Triangular Irregular Network (TIN) Models.md"
tags:
  - source
  - giscience
  - geospatial
  - active
  - review
  - simulation
  - data-management
---

# Triangular Irregular Network (TIN) Models

## Upward links
- [[GIS&T Body of Knowledge - Source]]
- [[current/source/GIS&T Body of Knowledge/UCGIS GIS&T Body of Knowledge|Mirrored GIS&T overview]]
- [[current/source/GIS&T Body of Knowledge/DM Data Management/DM Data Management|DM Data Management]]

## Summary
A Triangular Irregular Network (TIN) is a way of storing continuous surfaces. It is vector based, and works in such a way that it connects known data points with straight lines to create triangles, often called facets. These facets are planes that have the same slope and aspect over the facet. Collectively, these hypothetical lines form a network covering the whole surface. TINs are efficient when storing heterogeneous surfaces, since homogenous areas are stored using few data points, while areas with more variability are stored in detail using a larger number of data points. In other words, a TIN can be more detailed where the surface is complex (high variation) by using smaller facets, and less detailed where the surface is more homogeneous by using larger facets. TINs also have a high modelling potential, e.g. in topography and hydrology. However, the unique way of storing data an a TIN often makes it difficult to combine with other spatial data formats. Instead, the TIN data would usually be converted to other suitable formats.

## Downward links
- Learning outcome: 437 - Describe how TINs are constructed and stored
- Learning outcome: 719 - Develop awareness around the various applications of TINs in research
- Learning outcome: 756 - Differentiate between the various ways of representing continuous surfaces
- Learning outcome: 1210 - Explain the underlying concepts behind various algorithms for selecting points to be used in constructing TIN models
- Learning outcome: 1439 - List the advantages and disadvantages of using TIN model

## Related GIS&T topics
- [DM-02-007] The Raster Data Model
- [DM-02-009] The Hexagonal Model
- [DM-02-011] Hierarchical Data Models

## Lateral links
- None added yet.

## Traceability
- Raw note: [[GIS&T Body of Knowledge/DM Data Management/DM-02-010 Triangular Irregular Network (TIN) Models|Raw GIS&T topic]]
- Mirrored from: `GIS&T Body of Knowledge/DM Data Management/DM-02-010 Triangular Irregular Network (TIN) Models.md`
- Topic code: `DM-02-010`
