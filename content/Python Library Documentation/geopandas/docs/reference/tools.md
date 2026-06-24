---
title: "Tools"
source: "https://geopandas.org/en/latest/docs/reference/tools.html"
imported_from: "Python library documentation"
library: "geopandas"
---

# Tools

|  |  |
| --- | --- |
| [`sjoin`](api/geopandas.sjoin.html#geopandas.sjoin "geopandas.sjoin")(left\_df, right\_df[, how, predicate, ...]) | Spatial join of two GeoDataFrames. |
| [`sjoin_nearest`](api/geopandas.sjoin_nearest.html#geopandas.sjoin_nearest "geopandas.sjoin_nearest")(left\_df, right\_df[, how, ...]) | Spatial join of two GeoDataFrames based on the distance between their geometries. |
| [`overlay`](api/geopandas.overlay.html#geopandas.overlay "geopandas.overlay")(df1, df2[, how, keep\_geom\_type, ...]) | Perform spatial overlay between two GeoDataFrames. |
| [`clip`](api/geopandas.clip.html#geopandas.clip "geopandas.clip")(gdf, mask[, keep\_geom\_type, sort]) | Clip points, lines, or polygon geometries to the mask extent. |
| [`tools.geocode`](api/geopandas.tools.geocode.html#geopandas.tools.geocode "geopandas.tools.geocode")(strings[, provider]) | Geocode a set of strings and get a GeoDataFrame of the resulting points. |
| [`tools.reverse_geocode`](api/geopandas.tools.reverse_geocode.html#geopandas.tools.reverse_geocode "geopandas.tools.reverse_geocode")(points[, provider]) | Reverse geocode a set of points and get a GeoDataFrame of the resulting addresses. |
| [`tools.collect`](api/geopandas.tools.collect.html#geopandas.tools.collect "geopandas.tools.collect")(x[, multi]) | Collect single part geometries into their Multi\* counterpart. |
| [`points_from_xy`](api/geopandas.points_from_xy.html#geopandas.points_from_xy "geopandas.points_from_xy")(x, y[, z, crs]) | Generate GeometryArray of shapely Point geometries from x, y(, z) coordinates. |

[Show Source](../../_sources/docs/reference/tools.rst.txt)

---

Original source: https://geopandas.org/en/latest/docs/reference/tools.html
