---
title: Splines and Radial Basis Functions Interpolation
aliases:
  - "[AM-04-071] Splines and Radial Basis Functions Interpolation"
  - AM-04-071
category: source
source_type: living-textbook-topic
book: "GIS&T Body of Knowledge"
topic_code: AM-04-071
domain_code: AM
domain_name: Analytics and Modeling
raw_source_path: "GIS&T Body of Knowledge/AM Analytics and Modeling/AM-04-071 Splines and Radial Basis Functions Interpolation.md"
tags:
  - source
  - giscience
  - geospatial
  - active
  - review
  - simulation
---

# Splines and Radial Basis Functions Interpolation

## Upward links
- [[GIS&T Body of Knowledge - Source]]
- [[current/source/GIS&T Body of Knowledge/UCGIS GIS&T Body of Knowledge|Mirrored GIS&T overview]]
- [[current/source/GIS&T Body of Knowledge/AM Analytics and Modeling/AM Analytics and Modeling|AM Analytics and Modeling]]

## Summary
Spatial interpolation methods use the measured values at given locations to estimate the values at unsampled locations, for example, in computing raster digital elevation models from scattered measured elevations. Since this problem does not have a unique solution, many approaches have been developed to accomplish this task. Methods based on linear superposition of radial basis functions (RBF) centered at the data points include multivariate splines that simultaneously minimize the sum of the deviations from the measured points and the smoothness seminorm referred to also as a roughness penalty. The thin plate spline minimizes the 2D surface curvature and mimics a thin steel plate forced to pass through the data points: its equilibrium shape minimizes the bending energy which is closely related to the surface curvature. There are many generalizations such as spline with tension that controls the plate stiffness, while regularized spline enables direct calculations of surface gradients and curvatures making it effective for terrain modeling with simultaneous topographic analysis. Trivariate splines are used to interpolate meteorological variables with influence of topography. The RBF splines are related to universal kriging with the choice of the covariance function determined by the smoothness seminorm. Multiquadric RBF methods are similar in formulation and performance to splines.

## Downward links
- Learning outcome: 1901 - Explain the concept of variational approach to interpolation.
- Learning outcome: 1902 - Describe the impact of tension parameters on an interpolated surface.
- Learning outcome: 1903 - Explain the role of smoothing when interpolating noisy data
- Learning outcome: 1904 - Assess the predictive accuracy of interpolation.
- Learning outcome: 1905 - Describe the implications of selecting multivariate spline for atmospheric data.

## Related GIS&T topics
- [AM-04-029] Kriging Interpolation
- [AM-04-055] Digital Terrain Models and Terrain Metrics
- [AM-04-064] Modeling Surfaces
- [AM-04-067] Gridding, Interpolation, and Contouring
- [AM-04-070] Inverse Distance Weighting
- [AM-04-101] 3D Parametric Surfaces

## Lateral links
- None added yet.

## Traceability
- Raw note: [[GIS&T Body of Knowledge/AM Analytics and Modeling/AM-04-071 Splines and Radial Basis Functions Interpolation|Raw GIS&T topic]]
- Mirrored from: `GIS&T Body of Knowledge/AM Analytics and Modeling/AM-04-071 Splines and Radial Basis Functions Interpolation.md`
- Topic code: `AM-04-071`
