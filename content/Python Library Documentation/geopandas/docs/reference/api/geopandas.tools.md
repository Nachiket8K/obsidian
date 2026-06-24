---
title: "geopandas.tools.collect"
source: "https://geopandas.org/en/latest/docs/reference/api/geopandas.tools.collect.html"
imported_from: "Python library documentation"
library: "geopandas"
---

# geopandas.tools.collect

geopandas.tools.collect(*x*, *multi=False*)[[source]](https://github.com/geopandas/geopandas/blob/main/geopandas/tools/util.py#L13-L44)
:   Collect single part geometries into their Multi\* counterpart.

    Parameters:
    :   **x**an iterable or Series of Shapely geometries, a GeoSeries, or
        :   a single Shapely geometry

        **multi**boolean, default False
        :   if True, force returned geometries to be Multi\* even if they
            only have one component.

On this page

[Show Source](../../../_sources/docs/reference/api/geopandas.tools.collect.rst.txt)

---

Original source: https://geopandas.org/en/latest/docs/reference/api/geopandas.tools.collect.html
