---
title: "geopandas.testing.assert_geodataframe_equal"
source: "https://geopandas.org/en/latest/docs/reference/api/geopandas.testing.assert_geodataframe_equal.html"
imported_from: "Python library documentation"
library: "geopandas"
---

# geopandas.testing.assert\_geodataframe\_equal

geopandas.testing.assert\_geodataframe\_equal(*left*, *right*, *check\_dtype=True*, *check\_index\_type='equiv'*, *check\_column\_type='equiv'*, *check\_frame\_type=True*, *check\_like=False*, *check\_less\_precise=False*, *check\_geom\_type=False*, *check\_crs=True*, *normalize=False*)[[source]](https://github.com/geopandas/geopandas/blob/main/geopandas/testing.py#L236-L349)
:   Check that two GeoDataFrames are equal.

    Parameters:
    :   **left, right**two GeoDataFrames

        **check\_dtype**bool, default True
        :   Whether to check the DataFrame dtype is identical.

        **check\_index\_type, check\_column\_type**bool, default ‘equiv’
        :   Check that index types are equal.

        **check\_frame\_type**bool, default True
        :   Check that both are same type (*and* are GeoDataFrames). If False,
            will attempt to convert both into GeoDataFrame.

        **check\_like**bool, default False
        :   If true, ignore the order of rows & columns

        **check\_less\_precise**bool, default False
        :   If True, use geom\_equals\_exact. if False, use geom\_equals.

        **check\_geom\_type**bool, default False
        :   If True, check that all the geom types are equal.

        **check\_crs: bool, default True**
        :   If check\_frame\_type is True, then also check that the
            crs matches.

        **normalize: bool, default False**
        :   If True, normalize the geometries before comparing equality.
            Typically useful with `check_less_precise=True`, which uses
            `geom_equals_exact` and requires exact coordinate order.

On this page

[Show Source](../../../_sources/docs/reference/api/geopandas.testing.assert_geodataframe_equal.rst.txt)

---

Original source: https://geopandas.org/en/latest/docs/reference/api/geopandas.testing.assert_geodataframe_equal.html
