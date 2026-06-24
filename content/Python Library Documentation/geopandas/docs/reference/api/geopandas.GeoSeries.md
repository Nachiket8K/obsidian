---
title: "geopandas.GeoSeries.__geo_interface__"
source: "https://geopandas.org/en/latest/docs/reference/api/geopandas.GeoSeries.__geo_interface__.html"
imported_from: "Python library documentation"
library: "geopandas"
---

# geopandas.GeoSeries.\_\_geo\_interface\_\_

property GeoSeries.\_\_geo\_interface\_\_[[source]](https://github.com/geopandas/geopandas/blob/main/geopandas/geoseries.py#L664-L688)
:   Returns a `GeoSeries` as a python feature collection.

    Implements the geo\_interface. The returned python data structure
    represents the `GeoSeries` as a GeoJSON-like `FeatureCollection`.
    Note that the features will have an empty `properties` dict as they
    don’t have associated attributes (geometry only).

    Examples

    ```
    >>> from shapely.geometry import Point
    >>> s = geopandas.GeoSeries([Point(1, 1), Point(2, 2), Point(3, 3)])
    >>> s.__geo_interface__
    {'type': 'FeatureCollection', 'features': [{'id': '0', 'type': 'Feature', 'properties': {}, 'geometry': {'type': 'Point', 'coordinates': (1.0, 1.0)}, 'bbox': (1.0, 1.0, 1.0, 1.0)}, {'id': '1', 'type': 'Feature', 'properties': {}, 'geometry': {'type': 'Point', 'coordinates': (2.0, 2.0)}, 'bbox': (2.0, 2.0, 2.0, 2.0)}, {'id': '2', 'type': 'Feature', 'properties': {}, 'geometry': {'type': 'Point', 'coordinates': (3.0, 3.0)}, 'bbox': (3.0, 3.0, 3.0, 3.0)}], 'bbox': (1.0, 1.0, 3.0, 3.0)}
    ```

On this page

[Show Source](../../../_sources/docs/reference/api/geopandas.GeoSeries.__geo_interface__.rst.txt)

---

Original source: https://geopandas.org/en/latest/docs/reference/api/geopandas.GeoSeries.__geo_interface__.html
