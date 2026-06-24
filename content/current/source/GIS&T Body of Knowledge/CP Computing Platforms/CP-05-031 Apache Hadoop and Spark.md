---
title: Apache Hadoop and Spark
aliases:
  - "[CP-05-031] Apache Hadoop and Spark"
  - CP-05-031
category: source
source_type: living-textbook-topic
book: "GIS&T Body of Knowledge"
topic_code: CP-05-031
domain_code: CP
domain_name: Computing Platforms
raw_source_path: "GIS&T Body of Knowledge/CP Computing Platforms/CP-05-031 Apache Hadoop and Spark.md"
tags:
  - source
  - giscience
  - geospatial
  - active
  - review
  - python-gis
---

# Apache Hadoop and Spark

## Upward links
- [[GIS&T Body of Knowledge - Source]]
- [[current/source/GIS&T Body of Knowledge/UCGIS GIS&T Body of Knowledge|Mirrored GIS&T overview]]
- [[current/source/GIS&T Body of Knowledge/CP Computing Platforms/CP Computing Platforms|CP Computing Platforms]]

## Summary
*Apache Hadoop* and *Apache Spark* are two leading frameworks for distributed big data processing that have significantly impacted geospatial analytics. Both systems use clusters of commodity hardware in a shared-nothing architecture to scale out horizontally, allowing massive spatial datasets to be processed in parallel. Hadoop popularized the MapReduce programming model and excels at batch processing of very large files. Spark is a newer engine that builds on some of Hadoop’s concepts but introduces in-memory data processing and a more flexible execution model, often yielding faster performance for many tasks. This entry focuses on the differences between Hadoop’s disk-based MapReduce approach and Spark’s in-memory approach, especially in the context of spatial (vector and raster) data processing. We also highlight several systems that extend Hadoop or Spark specifically for spatial data, and discuss emerging trends toward integrating big data frameworks with higher-level query processing.

## Downward links
- Learning outcome: 1999 - Distinguish Hadoop and Spark architectures by explaining the differences between Hadoop’s disk-based MapReduce model and Spark’s in-memory DAG execution model.
- Learning outcome: 2000 - Describe how spatial partitioning in distributed shared-nothing systems can be used to optimize geospatial queries in these systems.
- Learning outcome: 2001 - Describe the functional programming constraints in Hadoop/Spark and identify the challenges of implementing some GIS operations using it.

## Related GIS&T topics
- [CP-04-007] Spatial MapReduce
- [CP-05-023] Google Earth Engine
- [CP-05-027] GIS&T and Computational Notebooks

## Lateral links
- None added yet.

## Traceability
- Raw note: [[GIS&T Body of Knowledge/CP Computing Platforms/CP-05-031 Apache Hadoop and Spark|Raw GIS&T topic]]
- Mirrored from: `GIS&T Body of Knowledge/CP Computing Platforms/CP-05-031 Apache Hadoop and Spark.md`
- Topic code: `CP-05-031`
