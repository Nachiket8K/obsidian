---
title: Local Measures of Spatial Association
aliases:
  - "[AM-03-023] Local Measures of Spatial Association"
  - AM-03-023
category: source
source_type: living-textbook-topic
book: "GIS&T Body of Knowledge"
topic_code: AM-03-023
domain_code: AM
domain_name: Analytics and Modeling
raw_source_path: "GIS&T Body of Knowledge/AM Analytics and Modeling/AM-03-023 Local Measures of Spatial Association.md"
tags:
  - source
  - giscience
  - geospatial
  - active
  - review
  - simulation
  - python-gis
---

# Local Measures of Spatial Association

## Upward links
- [[GIS&T Body of Knowledge - Source]]
- [[current/source/GIS&T Body of Knowledge/UCGIS GIS&T Body of Knowledge|Mirrored GIS&T overview]]
- [[current/source/GIS&T Body of Knowledge/AM Analytics and Modeling/AM Analytics and Modeling|AM Analytics and Modeling]]

## Summary
Local measures of spatial association are statistics used to detect variations of a variable of interest across space when the spatial relationship of the variable is not constant across the study region, known as spatial non-stationarity or spatial heterogeneity. Unlike global measures that summarize the overall spatial autocorrelation of the study area in one single value, local measures of spatial association identify local clusters (observations nearby have similar attribute values) or spatial outliers (observations nearby have different attribute values). Like global measures, local indicators of spatial association (LISA), including local Moran’s I and local Geary’s C, incorporate both spatial proximity and attribute similarity. Getis-Ord Gi\*, another popular local statistic, identifies spatial clusters at various significance levels, known as hot spots (unusually high values) and cold spots (unusually low values). This so-called “hot spot analysis” has been extended to examine spatiotemporal trends in data. Bivariate local Moran’s I describes the statistical relationship between one variable at a location and a spatially lagged second variable at neighboring locations, and geographically weighted regression (GWR) allows regression coefficients to vary at each observation location. Visualization of local measures of spatial association is critical, allowing researchers of various disciplines to easily identify local pockets of interest for future examination.

## Downward links
- Learning outcome: 82 - Compare and contrast global and local statistics and their uses.
- Learning outcome: 152 - Compute the Getis-Ord Gi\* statistic.
- Learning outcome: 224 - Decompose Moran's I and Geary's C into local measures of spatial association.
- Learning outcome: 1029 - Explain how geographically weighted regression provides local variability in the regression analysis.

## Related GIS&T topics
- [AM-03-019] Exploratory Spatial Data Analysis (ESDA)
- [AM-03-022] Global Measures of Spatial Association
- [AM-03-032] Spatial Autoregressive Models

## Lateral links
- None added yet.

## Traceability
- Raw note: [[GIS&T Body of Knowledge/AM Analytics and Modeling/AM-03-023 Local Measures of Spatial Association|Raw GIS&T topic]]
- Mirrored from: `GIS&T Body of Knowledge/AM Analytics and Modeling/AM-03-023 Local Measures of Spatial Association.md`
- Topic code: `AM-03-023`
