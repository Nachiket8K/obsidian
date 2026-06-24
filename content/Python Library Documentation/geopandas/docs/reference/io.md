---
title: "Input/output"
source: "https://geopandas.org/en/latest/docs/reference/io.html"
imported_from: "Python library documentation"
library: "geopandas"
---

# Input/output

## GIS vector files

|  |  |
| --- | --- |
| [`list_layers`](api/geopandas.list_layers.html#geopandas.list_layers "geopandas.list_layers")(filename) | List layers available in a file. |
| [`read_file`](api/geopandas.read_file.html#geopandas.read_file "geopandas.read_file")(filename[, bbox, mask, columns, ...]) | Return a GeoDataFrame from a file or URL. |
| [`GeoDataFrame.to_file`](api/geopandas.GeoDataFrame.to_file.html#geopandas.GeoDataFrame.to_file "geopandas.GeoDataFrame.to_file")(filename[, driver, ...]) | Write the `GeoDataFrame` to a file. |

## PostGIS

|  |  |
| --- | --- |
| [`read_postgis`](api/geopandas.read_postgis.html#geopandas.read_postgis "geopandas.read_postgis")(sql, con[, geom\_col, crs, ...]) | Return a GeoDataFrame corresponding to the result of the query string, which must contain a geometry column in WKB representation. |
| [`GeoDataFrame.to_postgis`](api/geopandas.GeoDataFrame.to_postgis.html#geopandas.GeoDataFrame.to_postgis "geopandas.GeoDataFrame.to_postgis")(name, con[, schema, ...]) | Upload GeoDataFrame into PostGIS database. |

## Feather

|  |  |
| --- | --- |
| [`read_feather`](api/geopandas.read_feather.html#geopandas.read_feather "geopandas.read_feather")(path[, columns, to\_pandas\_kwargs]) | Load a Feather object from the file path, returning a GeoDataFrame. |
| [`GeoDataFrame.to_feather`](api/geopandas.GeoDataFrame.to_feather.html#geopandas.GeoDataFrame.to_feather "geopandas.GeoDataFrame.to_feather")(path[, index, ...]) | Write a GeoDataFrame to the Feather format. |

## Parquet

|  |  |
| --- | --- |
| [`read_parquet`](api/geopandas.read_parquet.html#geopandas.read_parquet "geopandas.read_parquet")(path[, columns, ...]) | Load a Parquet object from the file path, returning a GeoDataFrame. |
| [`GeoDataFrame.to_parquet`](api/geopandas.GeoDataFrame.to_parquet.html#geopandas.GeoDataFrame.to_parquet "geopandas.GeoDataFrame.to_parquet")(path[, index, ...]) | Write a GeoDataFrame to the Parquet format. |

On this page

[Show Source](../../_sources/docs/reference/io.rst.txt)

---

Original source: https://geopandas.org/en/latest/docs/reference/io.html
