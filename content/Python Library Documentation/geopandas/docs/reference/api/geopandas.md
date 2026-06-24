---
title: "geopandas.points_from_xy"
source: "https://geopandas.org/en/latest/docs/reference/api/geopandas.points_from_xy.html"
imported_from: "Python library documentation"
library: "geopandas"
---

# geopandas.points\_from\_xy

geopandas.points\_from\_xy(*x*, *y*, *z=None*, *crs=None*)[[source]](https://github.com/geopandas/geopandas/blob/main/geopandas/array.py#L293-L343)
:   Generate GeometryArray of shapely Point geometries from x, y(, z) coordinates.

    In case of geographic coordinates, it is assumed that longitude is captured by
    `x` coordinates and latitude by `y`.

    Parameters:
    :   **x, y, z**iterable

        **crs**value, optional
        :   Coordinate Reference System of the geometry objects. Can be anything accepted by
            [`pyproj.CRS.from_user_input()`](https://pyproj4.github.io/pyproj/stable/api/crs/crs.html#pyproj.crs.CRS.from_user_input "(in pyproj v3.7.2)"),
            such as an authority string (eg “EPSG:4326”) or a WKT string.

    Returns:
    :   **output**GeometryArray

    Examples

    ```
    >>> import pandas as pd
    >>> df = pd.DataFrame({'x': [0, 1, 2], 'y': [0, 1, 2], 'z': [0, 1, 2]})
    >>> df
       x  y  z
    0  0  0  0
    1  1  1  1
    2  2  2  2
    >>> geometry = geopandas.points_from_xy(x=[1, 0], y=[0, 1])
    >>> geometry = geopandas.points_from_xy(df['x'], df['y'], df['z'])
    >>> gdf = geopandas.GeoDataFrame(
    ...     df, geometry=geopandas.points_from_xy(df['x'], df['y']))
    ```

    Having geographic coordinates:

    ```
    >>> df = pd.DataFrame({'longitude': [-140, 0, 123], 'latitude': [-65, 1, 48]})
    >>> df
       longitude  latitude
    0       -140       -65
    1          0         1
    2        123        48
    >>> geometry = geopandas.points_from_xy(df.longitude, df.latitude, crs="EPSG:4326")
    ```

On this page

[Show Source](../../../_sources/docs/reference/api/geopandas.points_from_xy.rst.txt)

---

Original source: https://geopandas.org/en/latest/docs/reference/api/geopandas.points_from_xy.html
