---
title: Kriging Interpolation
aliases:
  - "[AM-04-029] Kriging Interpolation"
  - AM-04-029
category: source
source_type: living-textbook-topic
book: "GIS&T Body of Knowledge"
topic_code: AM-04-029
domain_code: AM
domain_name: Analytics and Modeling
raw_source_path: "GIS&T Body of Knowledge/AM Analytics and Modeling/AM-04-029 Kriging Interpolation.md"
tags:
  - source
  - giscience
  - geospatial
  - active
  - review
  - simulation
---

# Kriging Interpolation

## Upward links
- [[GIS&T Body of Knowledge - Source]]
- [[current/source/GIS&T Body of Knowledge/UCGIS GIS&T Body of Knowledge|Mirrored GIS&T overview]]
- [[current/source/GIS&T Body of Knowledge/AM Analytics and Modeling/AM Analytics and Modeling|AM Analytics and Modeling]]

## Summary
Kriging is an interpolation method that makes predictions at unsampled locations using a linear combination of observations at nearby sampled locations. The influence of each observation on the kriging prediction is based on several factors: 1) its geographical proximity to the unsampled location, 2) the spatial arrangement of all observations (i.e., data configuration, such as clustering of observations in oversampled areas), and 3) the pattern of spatial correlation of the data. The development of kriging models is meaningful only when data are spatially correlated.. Kriging has several advantages over traditional interpolation techniques, such as inverse distance weighting or nearest neighbor: 1) it provides a measure of uncertainty attached to the results (i.e., kriging variance); 2) it accounts for direction-dependent relationships (i.e., spatial anisotropy); 3) weights are assigned to observations based on the spatial correlation of data instead of assumptions made by the analyst for IDW; 4) kriging predictions are not constrained to the range of observations used for interpolation, and 5) data measured over different spatial supports can be combined and change of support, such as downscaling or upscaling, can be conducted.

## Downward links
- Learning outcome: 65 - Compare and contrast block-kriging with areal interpolation using proportional area weighting
- Learning outcome: 621 - Describe the relationship between the semi-variogram and kriging
- Learning outcome: 1010 - Explain how block-kriging and its variants can be used to combine data sets with different spatial resolution (support)
- Learning outcome: 1116 - Explain the concept of the kriging variance, and describe some of its shortcomings
- Learning outcome: 1239 - Explain why it is important to have a good model of the semi-variogram in kriging

## Related GIS&T topics
- [AM-03-026] Spatial Sampling for Spatial Analysis

## Lateral links
- None added yet.

## Traceability
- Raw note: [[GIS&T Body of Knowledge/AM Analytics and Modeling/AM-04-029 Kriging Interpolation|Raw GIS&T topic]]
- Mirrored from: `GIS&T Body of Knowledge/AM Analytics and Modeling/AM-04-029 Kriging Interpolation.md`
- Topic code: `AM-04-029`
