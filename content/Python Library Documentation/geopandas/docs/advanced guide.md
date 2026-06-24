---
title: "Advanced guide"
source: "https://geopandas.org/en/latest/docs/advanced_guide.html"
imported_from: "Python library documentation"
library: "geopandas"
---

# Advanced guide

The advanced guide covers advanced usage of GeoPandas. Each page focuses on a single
topic and outlines how it is implemented in GeoPandas, with reproducible examples.

If you don’t know anything about GeoPandas, start with the [Introduction to
GeoPandas](../getting_started/introduction.html).

Basic topics can be found in the [User guide](user_guide.html) and further
specification in the [API reference](reference.html).

This section is currently work in progress. See the available pages below.

- [Spatial indexing](user_guide/spatial_indexing.html)
  - [R-tree principle](user_guide/spatial_indexing.html#R-tree-principle)
  - [Querying the index](user_guide/spatial_indexing.html#Querying-the-index)
- [Missing and empty geometries](user_guide/missing_empty.html)
  - [Changes since GeoPandas v0.6.0](user_guide/missing_empty.html#changes-since-geopandas-v0-6-0)
- [Re-projecting using GDAL with Rasterio and Fiona](user_guide/reproject_fiona.html)
  - [Fiona example](user_guide/reproject_fiona.html#fiona-example)
  - [Rasterio example](user_guide/reproject_fiona.html#rasterio-example)
- [Migration from PyGEOS geometry backend to Shapely 2.0](user_guide/pygeos_to_shapely.html)
  - [Migration period](user_guide/pygeos_to_shapely.html#migration-period)
  - [How to prepare your code for transition](user_guide/pygeos_to_shapely.html#how-to-prepare-your-code-for-transition)
- [Migration from the Fiona to the Pyogrio read/write engine](user_guide/fiona_to_pyogrio.html)
  - [Write an attribute table to a file](user_guide/fiona_to_pyogrio.html#write-an-attribute-table-to-a-file)
  - [No support for `schema` parameter to write files](user_guide/fiona_to_pyogrio.html#no-support-for-schema-parameter-to-write-files)
  - [Writing EMPTY geometries](user_guide/fiona_to_pyogrio.html#writing-empty-geometries)

[Show Source](../_sources/docs/advanced_guide.rst.txt)

---

Original source: https://geopandas.org/en/latest/docs/advanced_guide.html
