---
title: "Spatial index"
source: "https://geopandas.org/en/latest/docs/reference/sindex.html"
imported_from: "Python library documentation"
library: "geopandas"
---

# Spatial index

GeoPandas will use the STRtree implementation provided by the Shapely
(`shapely.STRtree`)

`GeoSeries.sindex` creates a spatial index, which can use the methods and
properties documented below.

See the User Guide page [Spatial indexing](../user_guide/spatial_indexing.html) for more.

## Constructor

|  |  |
| --- | --- |
| [`GeoSeries.sindex`](api/geopandas.GeoSeries.sindex.html#geopandas.GeoSeries.sindex "geopandas.GeoSeries.sindex") | Generate the spatial index. |

## Spatial index object

The spatial index object returned from [`GeoSeries.sindex`](api/geopandas.GeoSeries.sindex.html#geopandas.GeoSeries.sindex "geopandas.GeoSeries.sindex") has the following
methods:

|  |  |
| --- | --- |
| [`intersection`](api/geopandas.sindex.SpatialIndex.intersection.html#geopandas.sindex.SpatialIndex.intersection "geopandas.sindex.SpatialIndex.intersection")(coordinates) | Compatibility wrapper for rtree.index.Index.intersection, use `query` instead. |
| [`is_empty`](api/geopandas.sindex.SpatialIndex.is_empty.html#geopandas.sindex.SpatialIndex.is_empty "geopandas.sindex.SpatialIndex.is_empty") | Check if the spatial index is empty. |
| [`nearest`](api/geopandas.sindex.SpatialIndex.nearest.html#geopandas.sindex.SpatialIndex.nearest "geopandas.sindex.SpatialIndex.nearest")(geometry[, return\_all, ...]) | Return the nearest geometry in the tree for each input geometry in `geometry`. |
| [`query`](api/geopandas.sindex.SpatialIndex.query.html#geopandas.sindex.SpatialIndex.query "geopandas.sindex.SpatialIndex.query")(geometry[, predicate, sort, distance, ...]) | Return the indices of tree geometries that satisfy the given query. |
| [`size`](api/geopandas.sindex.SpatialIndex.size.html#geopandas.sindex.SpatialIndex.size "geopandas.sindex.SpatialIndex.size") | Size of the spatial index. |
| [`valid_query_predicates`](api/geopandas.sindex.SpatialIndex.valid_query_predicates.html#geopandas.sindex.SpatialIndex.valid_query_predicates "geopandas.sindex.SpatialIndex.valid_query_predicates") | Returns valid predicates for the spatial index. |

The spatial index offers the full capability of [`shapely.STRtree`](https://shapely.readthedocs.io/en/stable/strtree.html#shapely.STRtree "(in Shapely)").

On this page

[Show Source](../../_sources/docs/reference/sindex.rst.txt)

---

Original source: https://geopandas.org/en/latest/docs/reference/sindex.html
