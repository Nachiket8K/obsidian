---
title: Kernels and Density Estimation
aliases:
  - "[AM-03-008] Kernels and Density Estimation"
  - AM-03-008
category: source
source_type: living-textbook-topic
book: "GIS&T Body of Knowledge"
topic_code: AM-03-008
domain_code: AM
domain_name: Analytics and Modeling
raw_source_path: "GIS&T Body of Knowledge/AM Analytics and Modeling/AM-03-008 Kernels and Density Estimation.md"
tags:
  - source
  - giscience
  - geospatial
  - active
  - review
  - simulation
  - decision-support
---

# Kernels and Density Estimation

## Upward links
- [[GIS&T Body of Knowledge - Source]]
- [[current/source/GIS&T Body of Knowledge/UCGIS GIS&T Body of Knowledge|Mirrored GIS&T overview]]
- [[current/source/GIS&T Body of Knowledge/AM Analytics and Modeling/AM Analytics and Modeling|AM Analytics and Modeling]]

## Summary
Kernel density estimation is an important nonparametric technique to estimate density from point-based or line-based data. It has been widely used for various purposes, such as point or line data smoothing, risk mapping, and hot spot detection. It applies a kernel function on each observation (point or line) and spreads the observation over the kernel window. The kernel density estimate at a location will be the sum of the fractions of all observations at that location. In a GIS environment, kernel density estimation usually results in a density surface where each cell is rendered based on the kernel density estimated at the cell center. The result of kernel density estimation could vary substantially depending on the choice of kernel function or kernel bandwidth, with the latter having a greater impact. When applying a fixed kernel bandwidth over all of the observations, undersmoothing of density may occur in areas with only sparse observation while oversmoothing may be found in other areas. To solve this issue, adaptive or variable bandwidth approaches have been suggested.

## Downward links
- Learning outcome: 196 - Create density maps from point datasets using kernels and density estimation techniques using standard software
- Learning outcome: 585 - Describe the limitations of planar kernel density estimation methods for network point data
- Learning outcome: 1016 - Explain how density estimation transforms point data or line data into a field representation
- Learning outcome: 1240 - Explain why kernel density is needed
- Learning outcome: 1255 - Explain why, in some cases, an adaptive kernel might be employed

## Related GIS&T topics
- [AM-02-009] Classification and Clustering
- [AM-03-007] Point Pattern Analysis
- [AM-03-010] Spatial Interaction
- [AM-03-012] Cartographic Modeling
- [AM-03-013] Multi-Criteria Evaluation

## Lateral links
- None added yet.

## Traceability
- Raw note: [[GIS&T Body of Knowledge/AM Analytics and Modeling/AM-03-008 Kernels and Density Estimation|Raw GIS&T topic]]
- Mirrored from: `GIS&T Body of Knowledge/AM Analytics and Modeling/AM-03-008 Kernels and Density Estimation.md`
- Topic code: `AM-03-008`
