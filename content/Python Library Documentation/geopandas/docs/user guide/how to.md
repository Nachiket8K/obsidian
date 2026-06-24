---
title: "How to…"
source: "https://geopandas.org/en/latest/docs/user_guide/how_to.html"
imported_from: "Python library documentation"
library: "geopandas"
---

# How to…

## Drop duplicate geometry in all situations

Using the standard Pandas [`drop_duplicates()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html#pandas.DataFrame.drop_duplicates "(in pandas v3.0.3)") function on a geometry column can lead to some duplicate
geometries not being dropped, in certain circumstances. When used on a geometry column, the Pandas function compares the
WKB of each geometry object. This is sensitive to the orders of various components of the geometry - for example, a line
with coordinates in the order left-to-right should be equal to a line with the same coordinates in the order right-to-left,
but the WKB representations will be different. The same applies for the order of rings of polygons and parts in multipart
geometries.

To deal with this problem, use the [`normalize()`](../reference/api/geopandas.GeoSeries.normalize.html#geopandas.GeoSeries.normalize "geopandas.GeoSeries.normalize") method first to order the coordinates in a canonincal form,
and then use the standard [`drop_duplicates()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html#pandas.DataFrame.drop_duplicates "(in pandas v3.0.3)") method:

```
gdf["geometry"] = gdf.normalize()
gdf.drop_duplicates()
```

The effect of the [`normalize()`](../reference/api/geopandas.GeoSeries.normalize.html#geopandas.GeoSeries.normalize "geopandas.GeoSeries.normalize") method can be seen in the following example:

```
>>> geopandas.GeoSeries([
...     shapely.LineString([(0, 0), (1, 0), (2, 0)]),
...     shapely.LineString([(2, 0), (1, 0), (0, 0)]),
... ]).normalize().to_wkt()
0    LINESTRING (0 0, 1 0, 2 0)
1    LINESTRING (0 0, 1 0, 2 0)
dtype: object
```

On this page

[Show Source](../../_sources/docs/user_guide/how_to.rst.txt)

---

Original source: https://geopandas.org/en/latest/docs/user_guide/how_to.html
