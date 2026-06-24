---
title: "Indexing and selecting data"
source: "https://geopandas.org/en/latest/docs/user_guide/indexing.html"
imported_from: "Python library documentation"
library: "geopandas"
---

# Indexing and selecting data

GeoPandas inherits the standard [pandas](http://pandas.pydata.org/pandas-docs/stable/indexing.html) methods for indexing/selecting data. This includes label based indexing with [`loc`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc "(in pandas v3.0.3)") and integer position based indexing with [`iloc`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc "(in pandas v3.0.3)"), which apply to both [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") and [`GeoDataFrame`](../reference/api/geopandas.GeoDataFrame.html#geopandas.GeoDataFrame "geopandas.GeoDataFrame") objects. For more information on indexing/selecting, see the [pandas](http://pandas.pydata.org/pandas-docs/stable/indexing.html) documentation.

In addition to the standard [pandas](http://pandas.pydata.org/pandas-docs/stable/indexing.html) methods, GeoPandas also provides
coordinate based indexing with the [`cx`](../reference/api/geopandas.GeoDataFrame.cx.html#geopandas.GeoDataFrame.cx "geopandas.GeoDataFrame.cx") indexer, which slices using a bounding
box. Geometries in the [`GeoSeries`](../reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries "geopandas.GeoSeries") or [`GeoDataFrame`](../reference/api/geopandas.GeoDataFrame.html#geopandas.GeoDataFrame "geopandas.GeoDataFrame") that intersect the
bounding box will be returned.

Using the `geoda.chile_labor` dataset, you can use this functionality to quickly select parts
of Chile whose boundaries extend south of the -50 degrees latitude. You can first check the original GeoDataFrame.

```
In [1]: import geodatasets

In [2]: chile = geopandas.read_file(geodatasets.get_path('geoda.chile_labor'))

In [3]: chile.plot(figsize=(8, 8));
```

![../../_images/chile.png](../../_images/chile.png)

And then select only the southern part of the country.

```
In [4]: southern_chile = chile.cx[:, :-50]

In [5]: southern_chile.plot(figsize=(8, 8));
```

![../../_images/chile_southern.png](../../_images/chile_southern.png)

[Show Source](../../_sources/docs/user_guide/indexing.rst.txt)

---

Original source: https://geopandas.org/en/latest/docs/user_guide/indexing.html
