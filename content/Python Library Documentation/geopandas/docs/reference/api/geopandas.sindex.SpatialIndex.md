---
title: "geopandas.sindex.SpatialIndex.valid_query_predicates"
source: "https://geopandas.org/en/latest/docs/reference/api/geopandas.sindex.SpatialIndex.valid_query_predicates.html"
imported_from: "Python library documentation"
library: "geopandas"
---

# geopandas.sindex.SpatialIndex.valid\_query\_predicates

property SpatialIndex.valid\_query\_predicates[[source]](https://github.com/geopandas/geopandas/blob/main/geopandas/sindex.py#L36-L53)
:   Returns valid predicates for the spatial index.

    Returns:
    :   set
        :   Set of valid predicates for this spatial index.

    Examples

    ```
    >>> from shapely.geometry import Point
    >>> s = geopandas.GeoSeries([Point(0, 0), Point(1, 1)])
    >>> s.sindex.valid_query_predicates
    {None, "contains", "contains_properly", "covered_by", "covers", "crosses", "dwithin", "intersects", "overlaps", "touches", "within"}
    ```

On this page

[Show Source](../../../_sources/docs/reference/api/geopandas.sindex.SpatialIndex.valid_query_predicates.rst.txt)

---

Original source: https://geopandas.org/en/latest/docs/reference/api/geopandas.sindex.SpatialIndex.valid_query_predicates.html
