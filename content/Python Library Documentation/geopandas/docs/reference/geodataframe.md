---
title: "GeoDataFrame"
source: "https://geopandas.org/en/latest/docs/reference/geodataframe.html"
imported_from: "Python library documentation"
library: "geopandas"
---

# GeoDataFrame

A `GeoDataFrame` is a tabular data structure that contains at least
one `GeoSeries` column storing geometry.

## Constructor

|  |  |
| --- | --- |
| [`GeoDataFrame`](api/geopandas.GeoDataFrame.html#geopandas.GeoDataFrame "geopandas.GeoDataFrame")([data, geometry, crs]) | A GeoDataFrame object is a pandas.DataFrame that has one or more columns containing geometry. |

## Serialization / IO / conversion

|  |  |
| --- | --- |
| [`GeoDataFrame.from_file`](api/geopandas.GeoDataFrame.from_file.html#geopandas.GeoDataFrame.from_file "geopandas.GeoDataFrame.from_file")(filename, \*\*kwargs) | Alternate constructor to create a `GeoDataFrame` from a file. |
| [`GeoDataFrame.from_features`](api/geopandas.GeoDataFrame.from_features.html#geopandas.GeoDataFrame.from_features "geopandas.GeoDataFrame.from_features")(features[, crs, ...]) | Alternate constructor to create GeoDataFrame from an iterable of features or a feature collection. |
| [`GeoDataFrame.from_postgis`](api/geopandas.GeoDataFrame.from_postgis.html#geopandas.GeoDataFrame.from_postgis "geopandas.GeoDataFrame.from_postgis")(sql, con[, ...]) | Alternate constructor to create a `GeoDataFrame` from a sql query containing a geometry column in WKB representation. |
| [`GeoDataFrame.from_arrow`](api/geopandas.GeoDataFrame.from_arrow.html#geopandas.GeoDataFrame.from_arrow "geopandas.GeoDataFrame.from_arrow")(table[, geometry, ...]) | Construct a GeoDataFrame from an Arrow table object based on GeoArrow extension types. |
| [`GeoDataFrame.to_file`](api/geopandas.GeoDataFrame.to_file.html#geopandas.GeoDataFrame.to_file "geopandas.GeoDataFrame.to_file")(filename[, driver, ...]) | Write the `GeoDataFrame` to a file. |
| [`GeoDataFrame.to_json`](api/geopandas.GeoDataFrame.to_json.html#geopandas.GeoDataFrame.to_json "geopandas.GeoDataFrame.to_json")([na, show\_bbox, ...]) | Return a GeoJSON representation of the `GeoDataFrame` as a string. |
| [`GeoDataFrame.to_geo_dict`](api/geopandas.GeoDataFrame.to_geo_dict.html#geopandas.GeoDataFrame.to_geo_dict "geopandas.GeoDataFrame.to_geo_dict")([na, show\_bbox, ...]) | Return a python feature collection representation of the GeoDataFrame as a dictionary with a list of features based on the `__geo_interface__` GeoJSON-like specification. |
| [`GeoDataFrame.to_parquet`](api/geopandas.GeoDataFrame.to_parquet.html#geopandas.GeoDataFrame.to_parquet "geopandas.GeoDataFrame.to_parquet")(path[, index, ...]) | Write a GeoDataFrame to the Parquet format. |
| [`GeoDataFrame.to_arrow`](api/geopandas.GeoDataFrame.to_arrow.html#geopandas.GeoDataFrame.to_arrow "geopandas.GeoDataFrame.to_arrow")(\*[, index, ...]) | Encode a GeoDataFrame to GeoArrow format. |
| [`GeoDataFrame.to_feather`](api/geopandas.GeoDataFrame.to_feather.html#geopandas.GeoDataFrame.to_feather "geopandas.GeoDataFrame.to_feather")(path[, index, ...]) | Write a GeoDataFrame to the Feather format. |
| [`GeoDataFrame.to_postgis`](api/geopandas.GeoDataFrame.to_postgis.html#geopandas.GeoDataFrame.to_postgis "geopandas.GeoDataFrame.to_postgis")(name, con[, schema, ...]) | Upload GeoDataFrame into PostGIS database. |
| [`GeoDataFrame.to_wkb`](api/geopandas.GeoDataFrame.to_wkb.html#geopandas.GeoDataFrame.to_wkb "geopandas.GeoDataFrame.to_wkb")([hex]) | Encode all geometry columns in the GeoDataFrame to WKB. |
| [`GeoDataFrame.to_wkt`](api/geopandas.GeoDataFrame.to_wkt.html#geopandas.GeoDataFrame.to_wkt "geopandas.GeoDataFrame.to_wkt")(\*\*kwargs) | Encode all geometry columns in the GeoDataFrame to WKT. |

## Projection handling

|  |  |
| --- | --- |
| [`GeoDataFrame.crs`](api/geopandas.GeoDataFrame.crs.html#geopandas.GeoDataFrame.crs "geopandas.GeoDataFrame.crs") | The Coordinate Reference System (CRS) represented as a `pyproj.CRS` object. |
| [`GeoDataFrame.set_crs`](api/geopandas.GeoDataFrame.set_crs.html#geopandas.GeoDataFrame.set_crs "geopandas.GeoDataFrame.set_crs")([crs, epsg, inplace, ...]) | Set the Coordinate Reference System (CRS) of the `GeoDataFrame`. |
| [`GeoDataFrame.to_crs`](api/geopandas.GeoDataFrame.to_crs.html#geopandas.GeoDataFrame.to_crs "geopandas.GeoDataFrame.to_crs")([crs, epsg, inplace]) | Transform geometries to a new coordinate reference system. |
| [`GeoDataFrame.estimate_utm_crs`](api/geopandas.GeoDataFrame.estimate_utm_crs.html#geopandas.GeoDataFrame.estimate_utm_crs "geopandas.GeoDataFrame.estimate_utm_crs")([datum\_name]) | Return the estimated UTM CRS based on the bounds of the dataset. |

## Active geometry handling

|  |  |
| --- | --- |
| [`GeoDataFrame.rename_geometry`](api/geopandas.GeoDataFrame.rename_geometry.html#geopandas.GeoDataFrame.rename_geometry "geopandas.GeoDataFrame.rename_geometry")(col[, inplace]) | Rename the GeoDataFrame geometry column to the specified name. |
| [`GeoDataFrame.set_geometry`](api/geopandas.GeoDataFrame.set_geometry.html#geopandas.GeoDataFrame.set_geometry "geopandas.GeoDataFrame.set_geometry")(col[, drop, ...]) | Set the GeoDataFrame geometry using either an existing column or the specified input. |
| [`GeoDataFrame.active_geometry_name`](api/geopandas.GeoDataFrame.active_geometry_name.html#geopandas.GeoDataFrame.active_geometry_name "geopandas.GeoDataFrame.active_geometry_name") | Return the name of the active geometry column. |

## Aggregating and exploding

|  |  |
| --- | --- |
| [`GeoDataFrame.dissolve`](api/geopandas.GeoDataFrame.dissolve.html#geopandas.GeoDataFrame.dissolve "geopandas.GeoDataFrame.dissolve")([by, aggfunc, ...]) | Dissolve geometries within groupby into single observation. |
| [`GeoDataFrame.explode`](api/geopandas.GeoDataFrame.explode.html#geopandas.GeoDataFrame.explode "geopandas.GeoDataFrame.explode")([column, ignore\_index, ...]) | Explode multi-part geometries into multiple single geometries. |

## Spatial joins

|  |  |
| --- | --- |
| [`GeoDataFrame.sjoin`](api/geopandas.GeoDataFrame.sjoin.html#geopandas.GeoDataFrame.sjoin "geopandas.GeoDataFrame.sjoin")(df[, how, predicate, ...]) | Spatial join of two GeoDataFrames. |
| [`GeoDataFrame.sjoin_nearest`](api/geopandas.GeoDataFrame.sjoin_nearest.html#geopandas.GeoDataFrame.sjoin_nearest "geopandas.GeoDataFrame.sjoin_nearest")(right[, how, ...]) | Spatial join of two GeoDataFrames based on the distance between their geometries. |

## Overlay operations

|  |  |
| --- | --- |
| [`GeoDataFrame.clip`](api/geopandas.GeoDataFrame.clip.html#geopandas.GeoDataFrame.clip "geopandas.GeoDataFrame.clip")(mask[, keep\_geom\_type, sort]) | Clip points, lines, or polygon geometries to the mask extent. |
| [`GeoDataFrame.overlay`](api/geopandas.GeoDataFrame.overlay.html#geopandas.GeoDataFrame.overlay "geopandas.GeoDataFrame.overlay")(right[, how, ...]) | Perform spatial overlay between GeoDataFrames. |

## Plotting

|  |  |
| --- | --- |
| [`GeoDataFrame.explore`](api/geopandas.GeoDataFrame.explore.html#geopandas.GeoDataFrame.explore "geopandas.GeoDataFrame.explore")(\*args, \*\*kwargs) | Explore data in interactive map based on GeoPandas and folium/leaflet.js. |

|  |  |
| --- | --- |
| [`GeoDataFrame.plot`](api/geopandas.GeoDataFrame.plot.html#geopandas.GeoDataFrame.plot "geopandas.GeoDataFrame.plot") |  |

## Spatial index

|  |  |
| --- | --- |
| [`GeoDataFrame.sindex`](api/geopandas.GeoDataFrame.sindex.html#geopandas.GeoDataFrame.sindex "geopandas.GeoDataFrame.sindex") | Generate the spatial index. |
| [`GeoDataFrame.has_sindex`](api/geopandas.GeoDataFrame.has_sindex.html#geopandas.GeoDataFrame.has_sindex "geopandas.GeoDataFrame.has_sindex") | Check the existence of the spatial index without generating it. |

## Indexing

|  |  |
| --- | --- |
| [`GeoDataFrame.cx`](api/geopandas.GeoDataFrame.cx.html#geopandas.GeoDataFrame.cx "geopandas.GeoDataFrame.cx") | Coordinate based indexer to select by intersection with bounding box. |

## Interface

|  |  |
| --- | --- |
| [`GeoDataFrame.__geo_interface__`](api/geopandas.GeoDataFrame.__geo_interface__.html#geopandas.GeoDataFrame.__geo_interface__ "geopandas.GeoDataFrame.__geo_interface__") | Returns a `GeoDataFrame` as a python feature collection. |
| [`GeoDataFrame.iterfeatures`](api/geopandas.GeoDataFrame.iterfeatures.html#geopandas.GeoDataFrame.iterfeatures "geopandas.GeoDataFrame.iterfeatures")([na, show\_bbox, ...]) | Return an iterator that yields feature dictionaries that comply with \_\_geo\_interface\_\_. |

All pandas `DataFrame` methods are also available, although they may
not operate in a meaningful way on the `geometry` column. All methods
listed in [GeoSeries](geoseries) work directly on an active geometry column of GeoDataFrame.

On this page

[Show Source](../../_sources/docs/reference/geodataframe.rst.txt)

---

Original source: https://geopandas.org/en/latest/docs/reference/geodataframe.html
