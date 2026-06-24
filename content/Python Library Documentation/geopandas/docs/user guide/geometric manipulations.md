---
title: "Geometric manipulations"
source: "https://geopandas.org/en/latest/docs/user_guide/geometric_manipulations.html"
imported_from: "Python library documentation"
library: "geopandas"
---

# Geometric manipulations

GeoPandas makes available all the tools for geometric manipulations in the [Shapely library](http://shapely.readthedocs.io/en/latest/manual.html).

Note that documentation for all set-theoretic tools for creating new shapes using the relationship between two different spatial datasets – like creating intersections, or differences – can be found at [Set operations with overlay](set_operations.html).

## Constructive methods

GeoSeries.buffer(*distance*, *resolution=16*)
:   Returns a [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") of geometries representing all points within a given distance
    of each geometric object.

GeoSeries.boundary
:   Returns a [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") of lower dimensional objects representing
    each geometry’s set-theoretic boundary.

GeoSeries.centroid
:   Returns a [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") of points for each geometric centroid.

GeoSeries.concave\_hull
:   Returns a [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") of geometries representing the smallest
    concave Polygon containing all the points in each object unless the
    number of points in the object is less than three. For two points,
    the concave hull collapses to a LineString; for 1, a Point.

GeoSeries.convex\_hull
:   Returns a [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") of geometries representing the smallest
    convex Polygon containing all the points in each object unless the
    number of points in the object is less than three. For two points,
    the convex hull collapses to a LineString; for 1, a Point.

GeoSeries.constrained\_delaunay\_triangles()
:   Returns a [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") with the constrained Delaunay triangulation
    of polygons. A constrained Delaunay triangulation requires the edges of the input
    polygon(s) to be in the set of resulting triangle edges. An unconstrained
    delaunay triangulation only triangulates based on the vertices, hence triangle
    edges could cross polygon boundaries.

GeoSeries.delaunay\_triangles(*tolerance*, *preserve\_topology=True*)
:   Returns a [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") consisting of polygons (default) or linestrings
    (only\_edges=True) representing the computed Delaunay triangulation around the vertices
    of an input geometry.

GeoSeries.envelope
:   Returns a [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") of geometries representing the point or
    smallest rectangular polygon (with sides parallel to the coordinate
    axes) that contains each object.

GeoSeries.extract\_unique\_points()
:   Returns a [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") of geometries containing all distinct
    vertices of each input geometry as a multipoint.

GeoSeries.offset\_curve(*distance*, *quad\_segs=8*, *join\_style='round'*, *mitre\_limit=5.0*)
:   Returns a [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") containing a Linestring or MultiLineString
    geometry at a distance from the object on its right or its left side.

GeoSeries.remove\_repeated\_points()
:   Returns a [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") containing a copy of the input geometry
    with repeated points removed.

GeoSeries.simplify(*tolerance*, *preserve\_topology=True*)
:   Returns a [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") containing a simplified representation of
    each object.

GeoSeries.segmentize(*max\_segment\_length*)
:   Returns a [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") with additional vertices added to line
    segments based on max\_segment\_length.

GeoSeries.union\_all()
:   Return a geometry containing the union of all geometries in the [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries").

## Affine transformations

GeoSeries.affine\_transform(*self*, *matrix*)
:   Transform the geometries of the [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") using an affine transformation matrix

GeoSeries.rotate(*self*, *angle*, *origin='center'*, *use\_radians=False*)
:   Rotate the coordinates of the [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries").

GeoSeries.scale(*self*, *xfact=1.0*, *yfact=1.0*, *zfact=1.0*, *origin='center'*)
:   Scale the geometries of the [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") along each (x, y, z) dimension.

GeoSeries.skew(*self*, *angle*, *origin='center'*, *use\_radians=False*)
:   Shear/Skew the geometries of the [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") by angles along x and y dimensions.

GeoSeries.translate(*self*, *xoff=0.0*, *yoff=0.0*, *zoff=0.0*)
:   Shift the coordinates of the [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries").

## Examples of geometric manipulations

```
>>> import geopandas
>>> from geopandas import GeoSeries
>>> from shapely.geometry import Polygon
>>> p1 = Polygon([(0, 0), (1, 0), (1, 1)])
>>> p2 = Polygon([(0, 0), (1, 0), (1, 1), (0, 1)])
>>> p3 = Polygon([(2, 0), (3, 0), (3, 1), (2, 1)])
>>> g = GeoSeries([p1, p2, p3])
>>> g
0         POLYGON ((0 0, 1 0, 1 1, 0 0))
1    POLYGON ((0 0, 1 0, 1 1, 0 1, 0 0))
2    POLYGON ((2 0, 3 0, 3 1, 2 1, 2 0))
dtype: geometry
```

![../../_images/test.png](../../_images/test.png)

Some geographic operations return normal pandas objects. The [`area`](../reference/api/geopandas.GeoSeries.area.html#geopandas.GeoSeries.area "geopandas.GeoSeries.area") property of a [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") will return a [`pandas.Series`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.html#pandas.Series "(in pandas v3.0.3)") containing the area of each item in the [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries"):

```
>>> print(g.area)
0    0.5
1    1.0
2    1.0
dtype: float64
```

Other operations return GeoPandas objects:

```
>>> g.buffer(0.5)
0    POLYGON ((-0.3535533905932737 0.35355339059327...
1    POLYGON ((-0.5 0, -0.5 1, -0.4975923633360985 ...
2    POLYGON ((1.5 0, 1.5 1, 1.502407636663901 1.04...
dtype: geometry
```

![../../_images/test_buffer.png](../../_images/test_buffer.png)

GeoPandas objects also know how to plot themselves. GeoPandas uses [matplotlib](http://matplotlib.org) for plotting. To generate a plot of a [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries"), use:

```
>>> g.plot()
```

GeoPandas also implements alternate constructors that can read any data format recognized by [Pyogrio](http://pyogrio.readthedocs.io/en/latest/). To read a zip file containing an ESRI shapefile with the [borough boundaries of New York City](https://data.cityofnewyork.us/City-Government/Borough-Boundaries/tqmj-j8zm) (provided by the `geodatasets` package):

```
>>> import geodatasets
>>> nybb_path = geodatasets.get_path('nybb')
>>> boros = geopandas.read_file(nybb_path)
>>> boros.set_index('BoroCode', inplace=True)
>>> boros.sort_index(inplace=True)
>>> boros
               BoroName     Shape_Leng    Shape_Area  \
BoroCode
1             Manhattan  359299.096471  6.364715e+08
2                 Bronx  464392.991824  1.186925e+09
3              Brooklyn  741080.523166  1.937479e+09
4                Queens  896344.047763  3.045213e+09
5         Staten Island  330470.010332  1.623820e+09

                                                   geometry
BoroCode
1         MULTIPOLYGON (((981219.0557861328 188655.31579...
2         MULTIPOLYGON (((1012821.805786133 229228.26458...
3         MULTIPOLYGON (((1021176.479003906 151374.79699...
4         MULTIPOLYGON (((1029606.076599121 156073.81420...
5         MULTIPOLYGON (((970217.0223999023 145643.33221...
```

![../../_images/nyc.png](../../_images/nyc.png)

```
>>> boros['geometry'].convex_hull
BoroCode
1    POLYGON ((977855.4451904297 188082.3223876953,...
2    POLYGON ((1017949.977600098 225426.8845825195,...
3    POLYGON ((988872.8212280273 146772.0317993164,...
4    POLYGON ((1000721.531799316 136681.776184082, ...
5    POLYGON ((915517.6877458114 120121.8812543372,...
dtype: geometry
```

![../../_images/nyc_hull.png](../../_images/nyc_hull.png)

To demonstrate a more complex operation, generate a
[`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") containing 2000 random points:

```
>>> import numpy as np
>>> from shapely.geometry import Point
>>> xmin, xmax, ymin, ymax = 900000, 1080000, 120000, 280000
>>> xc = (xmax - xmin) * np.random.random(2000) + xmin
>>> yc = (ymax - ymin) * np.random.random(2000) + ymin
>>> pts = GeoSeries([Point(x, y) for x, y in zip(xc, yc)])
```

Now draw a circle with fixed radius around each point:

```
>>> circles = pts.buffer(2000)
```

You can collapse these circles into a single [`MultiPolygon`](https://shapely.readthedocs.io/en/stable/manual.html#MultiPolygon "(in Shapely)")
geometry with

```
>>> mp = circles.union_all()
```

To extract the part of this geometry contained in each borough, you can
just use:

```
>>> holes = boros['geometry'].intersection(mp)
```

![../../_images/holes.png](../../_images/holes.png)

and to get the area outside of the holes:

```
>>> boros_with_holes = boros['geometry'].difference(mp)
```

![../../_images/boros_with_holes.png](../../_images/boros_with_holes.png)

Note that this can be simplified a bit, since `geometry` is
available as an attribute on a [`GeoDataFrame`](../reference/api/geopandas.GeoDataFrame.html#geopandas.GeoDataFrame "geopandas.GeoDataFrame"), and the
[`intersection()`](../reference/api/geopandas.GeoSeries.intersection.html#geopandas.GeoSeries.intersection "geopandas.GeoSeries.intersection") and [`difference()`](../reference/api/geopandas.GeoSeries.difference.html#geopandas.GeoSeries.difference "geopandas.GeoSeries.difference") methods are implemented with the
“&” and “-” operators, respectively. For example, the latter could
have been expressed simply as `boros.geometry - mp`.

It’s easy to do things like calculate the fractional area in each
borough that are in the holes:

```
>>> holes.area / boros.geometry.area
BoroCode
1    0.579939
2    0.586833
3    0.608174
4    0.582172
5    0.558075
dtype: float64
```

On this page

[Show Source](../../_sources/docs/user_guide/geometric_manipulations.rst.txt)

---

Original source: https://geopandas.org/en/latest/docs/user_guide/geometric_manipulations.html
