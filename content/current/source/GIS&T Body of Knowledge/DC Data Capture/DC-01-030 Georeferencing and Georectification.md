---
title: Georeferencing and Georectification
aliases:
  - "[DC-01-030] Georeferencing and Georectification"
  - DC-01-030
category: source
source_type: living-textbook-topic
book: "GIS&T Body of Knowledge"
topic_code: DC-01-030
domain_code: DC
domain_name: Data Capture
raw_source_path: "GIS&T Body of Knowledge/DC Data Capture/DC-01-030 Georeferencing and Georectification.md"
tags:
  - source
  - giscience
  - geospatial
  - active
  - review
  - decision-support
---

# Georeferencing and Georectification

## Upward links
- [[GIS&T Body of Knowledge - Source]]
- [[current/source/GIS&T Body of Knowledge/UCGIS GIS&T Body of Knowledge|Mirrored GIS&T overview]]
- [[current/source/GIS&T Body of Knowledge/DC Data Capture/DC Data Capture|DC Data Capture]]

## Summary
Georeferencing is the recording of the absolute location of a data point or data points. Georectification refers to the removal of geometric distortions between sets of data points, most often the removal of terrain, platform, and sensor induced distortions from remote sensing imagery. Georeferencing is a requisite task for all spatial data, as spatial data cannot be positioned in space or evaluated with respect to other data that are without being assigned a spatial coordinate within a defined coordinate system. Many data are implicitly georeferenced (i.e., are labeled with spatial reference information), such as points collected from a global navigation satellite system (GNSS). Data that are not labeled with spatial reference information can be georeferenced using a number of approaches, the most commonly applied of which are described in this article. The majority of approaches employ known reference locations (i.e., Ground Control Points) drawn from a reliable source (e.g., GNSS, orthophotography) to calibrate georeferencing models. Regardless of georeferencing approach, positional error is present. The accuracy of georeferencing (i.e., amount of positional error) should be quantified, typically by the root mean squared error between ground control points from a reference source and the georeferenced data product.

## Downward links
- Learning outcome: 156 - Conduct positional accuracy assessments, including interpretation of results
- Learning outcome: 958 - Evaluate the suitability of reference sources for calibration and validation of georeferencing models
- Learning outcome: 1127 - Explain the difference between geometric warping and resampling
- Learning outcome: 1128 - Explain the difference between georeferencing and georectification
- Learning outcome: 1300 - Identify appropriate georeferencing techniques for a given application

## Related GIS&T topics
- [DC-02-036] Historical Maps in GIS

## Lateral links
- None added yet.

## Traceability
- Raw note: [[GIS&T Body of Knowledge/DC Data Capture/DC-01-030 Georeferencing and Georectification|Raw GIS&T topic]]
- Mirrored from: `GIS&T Body of Knowledge/DC Data Capture/DC-01-030 Georeferencing and Georectification.md`
- Topic code: `DC-01-030`
