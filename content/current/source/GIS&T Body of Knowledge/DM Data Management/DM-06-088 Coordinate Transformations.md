---
title: Coordinate Transformations
aliases:
  - "[DM-06-088] Coordinate Transformations"
  - DM-06-088
category: source
source_type: living-textbook-topic
book: "GIS&T Body of Knowledge"
topic_code: DM-06-088
domain_code: DM
domain_name: Data Management
raw_source_path: "GIS&T Body of Knowledge/DM Data Management/DM-06-088 Coordinate Transformations.md"
tags:
  - source
  - giscience
  - geospatial
  - active
  - review
  - simulation
  - python-gis
  - data-management
---

# Coordinate Transformations

## Upward links
- [[GIS&T Body of Knowledge - Source]]
- [[current/source/GIS&T Body of Knowledge/UCGIS GIS&T Body of Knowledge|Mirrored GIS&T overview]]
- [[current/source/GIS&T Body of Knowledge/DM Data Management/DM Data Management|DM Data Management]]

## Summary
Coordinate transformations are needed to align multiple GIS datasets to one coordinate system when they use multiple coordinate systems. To transform coordinates, the properties of the source and target coordinate systems such as datums, projection methods, and their measurement origins and units should be identified carefully. Implemented in most GIS software and GIS data viewers, the on-the-fly projection technology projects GIS datasets automatically without the need for manual coordinate transformations by users. The coordinate transformation mechanisms for vector and raster datasets are different because the raster datasets require pixel value resampling during coordinate transformations. As a case study, eight GIS datasets were downloaded from multiple websites and were reprojected to a coordinate system in QGIS.

## Downward links
- Learning outcome: 144 - Compare the implementations of coordinates in vector and raster datasets.
- Learning outcome: 534 - Describe the coordinates and coordinate systems that are used in GIS datasets.
- Learning outcome: 1177 - Explain the mechanism of the On-The-Fly projection.
- Learning outcome: 1501 - Perform coordinate transformations with QGIS.

## Related GIS&T topics
- [CV-03-006] Map Projections
- [DM-05-044] Earth's Shape, Sea Level, and the Geoid
- [DM-05-048] Planar Coordinate Systems and the U. S. National Grid
- [DM-05-052] Horizontal (Geometric) Datums
- [DM-06-086] Vector-to-Raster and Raster-to-Vector Conversions
- [DM-06-087] Raster resampling

## Lateral links
- None added yet.

## Traceability
- Raw note: [[GIS&T Body of Knowledge/DM Data Management/DM-06-088 Coordinate Transformations|Raw GIS&T topic]]
- Mirrored from: `GIS&T Body of Knowledge/DM Data Management/DM-06-088 Coordinate Transformations.md`
- Topic code: `DM-06-088`
