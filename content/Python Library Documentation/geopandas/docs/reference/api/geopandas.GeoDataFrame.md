---
title: "geopandas.GeoDataFrame.iterfeatures"
source: "https://geopandas.org/en/latest/docs/reference/api/geopandas.GeoDataFrame.iterfeatures.html"
imported_from: "Python library documentation"
library: "geopandas"
---

# geopandas.GeoDataFrame.iterfeatures

GeoDataFrame.iterfeatures(*na='null'*, *show\_bbox=False*, *drop\_id=False*)[[source]](https://github.com/geopandas/geopandas/blob/main/geopandas/geodataframe.py#L1112-L1212)
:   Return an iterator that yields feature dictionaries that comply with
    \_\_geo\_interface\_\_.

    Parameters:
    :   **na**str, optional
        :   Options are {‘null’, ‘drop’, ‘keep’}, default ‘null’.
            Indicates how to output missing (NaN) values in the GeoDataFrame

            - null: output the missing entries as JSON null
            - drop: remove the property from the feature. This applies to each feature individually so that features may have different properties
            - keep: output the missing entries as NaN

        **show\_bbox**bool, optional
        :   Include bbox (bounds) in the geojson. Default False.

        **drop\_id**bool, default: False
        :   Whether to retain the index of the GeoDataFrame as the id property
            in the generated GeoJSON. Default is False, but may want True
            if the index is just arbitrary row numbers.

    Examples

    ```
    >>> from shapely.geometry import Point
    >>> d = {'col1': ['name1', 'name2'], 'geometry': [Point(1, 2), Point(2, 1)]}
    >>> gdf = geopandas.GeoDataFrame(d, crs="EPSG:4326")
    >>> gdf
        col1     geometry
    0  name1  POINT (1 2)
    1  name2  POINT (2 1)
    ```

    ```
    >>> feature = next(gdf.iterfeatures())
    >>> feature
    {'id': '0', 'type': 'Feature', 'properties': {'col1': 'name1'}, 'geometry': {'type': 'Point', 'coordinates': (1.0, 2.0)}}
    ```

On this page

[Show Source](../../../_sources/docs/reference/api/geopandas.GeoDataFrame.iterfeatures.rst.txt)

---

Original source: https://geopandas.org/en/latest/docs/reference/api/geopandas.GeoDataFrame.iterfeatures.html
