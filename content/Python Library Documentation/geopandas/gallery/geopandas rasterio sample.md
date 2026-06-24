---
title: "Using GeoPandas with Rasterio to sample point data"
source: "https://geopandas.org/en/latest/gallery/geopandas_rasterio_sample.html"
imported_from: "Python library documentation"
library: "geopandas"
---

This page was generated from [gallery/geopandas\_rasterio\_sample.ipynb](https://github.com/geopandas/geopandas/blob/main/doc/source/gallery/geopandas_rasterio_sample.ipynb).

Interactive online version: [![Binder badge](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/geopandas/geopandas/main?urlpath=lab/tree/doc/source/gallery/geopandas_rasterio_sample.ipynb)

# Using GeoPandas with Rasterio to sample point data

This example shows how to use GeoPandas with Rasterio. [Rasterio](https://rasterio.readthedocs.io/en/latest/index.html) is a package for reading and writing raster data.

In this example a set of vector points is used to sample raster data at those points.

The raster data used is Copernicus Sentinel data 2018 for Sentinel data.

```
[1]:
```

```
import geopandas
import rasterio
import matplotlib.pyplot as plt
from shapely.geometry import Point
```

# Create example vector data

Generate a geodataframe from a set of points

```
[2]:
```

```
# Create sampling points
points = [
    Point(625466, 5621289),
    Point(626082, 5621627),
    Point(627116, 5621680),
    Point(625095, 5622358),
]
gdf = geopandas.GeoDataFrame([1, 2, 3, 4], geometry=points, crs=32630)
```

The `GeoDataFrame` looks like this:

```
[3]:
```

```
gdf.head()
```

```
[3]:
```

|  | 0 | geometry |
| --- | --- | --- |
| 0 | 1 | POINT (625466 5621289) |
| 1 | 2 | POINT (626082 5621627) |
| 2 | 3 | POINT (627116 5621680) |
| 3 | 4 | POINT (625095 5622358) |

# Open the raster data

Use `rasterio` to open the raster data to be sampled

```
[4]:
```

```
src = rasterio.open("s2a_l2a_fishbourne.tif")
```

Let’s see the raster data with the point data overlaid.

```
[5]:
```

```
from rasterio.plot import show

fig, ax = plt.subplots()

# transform rasterio plot to real world coords
extent = [src.bounds[0], src.bounds[2], src.bounds[1], src.bounds[3]]
ax = rasterio.plot.show(src, extent=extent, ax=ax, cmap="pink")

gdf.plot(ax=ax)
```

```
[5]:
```

```
<Axes: xlabel='Easting [metre]', ylabel='Northing [metre]'>
```

![../_images/gallery_geopandas_rasterio_sample_9_1.png](../_images/gallery_geopandas_rasterio_sample_9_1.png)

# Sampling the data

Rasterio requires a list of the coordinates in x,y format rather than as the points that are in the geomentry column.

This can be achieved using the code below

```
[6]:
```

```
coord_list = [(x, y) for x, y in zip(gdf["geometry"].x, gdf["geometry"].y)]
```

Carry out the sampling of the data and store the results in a new column called `value`. Note that if the image has more than one band, a value is returned for each band.

```
[7]:
```

```
gdf["value"] = [x for x in src.sample(coord_list)]
gdf.head()
```

```
[7]:
```

|  | 0 | geometry | value |
| --- | --- | --- | --- |
| 0 | 1 | POINT (625466 5621289) | [684.0, 1005.0, 707.0, 265.0] |
| 1 | 2 | POINT (626082 5621627) | [999.0, 1105.0, 1115.0, 1340.0] |
| 2 | 3 | POINT (627116 5621680) | [284.0, 713.0, 310.0, 5405.0] |
| 3 | 4 | POINT (625095 5622358) | [237.0, 564.0, 250.0, 3680.0] |

On this page

[Show Source](../_sources/gallery/geopandas_rasterio_sample.ipynb.txt)

---

Original source: https://geopandas.org/en/latest/gallery/geopandas_rasterio_sample.html
