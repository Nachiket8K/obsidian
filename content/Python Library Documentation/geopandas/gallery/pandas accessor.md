---
title: "Using GeoPandas via the pandas “geo” accessor"
source: "https://geopandas.org/en/latest/gallery/pandas_accessor.html"
imported_from: "Python library documentation"
library: "geopandas"
---

This page was generated from [gallery/pandas\_accessor.ipynb](https://github.com/geopandas/geopandas/blob/main/doc/source/gallery/pandas_accessor.ipynb).

Interactive online version: [![Binder badge](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/geopandas/geopandas/main?urlpath=lab/tree/doc/source/gallery/pandas_accessor.ipynb)

# Using GeoPandas via the pandas “geo” accessor

GeoPandas can be used from pandas with the “geo” accessor, which is registered on `pandas.Series` when `geopandas.accessors` is first imported.

```
[1]:
```

```
# Import geopandas.accessors to register the "geo" accessor.
import geopandas.accessors  # noqa # pylint: disable=unused-import
import pandas as pd
from shapely import Point
```

## Using the Series.geo accessor

Construct a Series using the GeometryDtype.

```
[2]:
```

```
s = pd.Series(
    [Point(1, 2), Point(3, 4), Point(5, 6)],
    dtype='geometry',
)
s
```

```
[2]:
```

```
0    POINT (1 2)
1    POINT (3 4)
2    POINT (5 6)
dtype: geometry
```

All GeoSeries methods and properties are available via the “geo” accessor.

```
[3]:
```

```
s.geo.x
```

```
[3]:
```

```
0    1.0
1    3.0
2    5.0
dtype: float64
```

```
[4]:
```

```
s2 = pd.Series(
    [Point(-1, -2), Point(-3, -4), Point(-5, -6)],
    dtype='geometry',
)
s.geo.distance(s2)
```

```
[4]:
```

```
0     4.472136
1    10.000000
2    15.620499
dtype: float64
```

On this page

[Show Source](../_sources/gallery/pandas_accessor.ipynb.txt)

---

Original source: https://geopandas.org/en/latest/gallery/pandas_accessor.html
