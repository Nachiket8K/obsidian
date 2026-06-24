---
title: "Installation"
source: "https://geopandas.org/en/latest/getting_started/install.html"
imported_from: "Python library documentation"
library: "geopandas"
---

# Installation

GeoPandas depends for its spatial functionality on a large geospatial, open
source stack of libraries ([GEOS](https://geos.osgeo.org), [GDAL](https://www.gdal.org/), [PROJ](https://proj.org/)). See the
[Dependencies](#dependencies) section below for more details. Those base C
libraries can sometimes be a challenge to install. Therefore, we advise you
to closely follow the recommendations below to avoid installation problems.

## Installing with Anaconda / conda

To install GeoPandas and all its dependencies, we recommend to use the [conda](https://conda.io/en/latest/)
package manager. This can be obtained by installing the
[Anaconda Distribution](https://www.anaconda.com/distribution/) (a free Python distribution for data science), or
through [miniconda](https://docs.conda.io/en/latest/miniconda.html) (minimal distribution only containing Python and the
[conda](https://conda.io/en/latest/) package manager). See also the [Conda installation docs](https://conda.io/docs/user-guide/install/download.html) for more information
on how to install Anaconda or miniconda locally.

The advantage of using the [conda](https://conda.io/en/latest/) package manager is that it provides
pre-built binaries for all the required and optional dependencies of GeoPandas
for all platforms (Windows, Mac, Linux).

To install the latest version of GeoPandas, you can then do:

```
conda install geopandas
```

### Using the conda-forge channel

[conda-forge](https://conda-forge.org/) is a community effort that provides conda packages for a wide
range of software. It provides the *conda-forge* package channel for conda from
which packages can be installed, in addition to the “*defaults*” channel
provided by Anaconda.
Depending on what other packages you are working with, the *defaults* channel
or *conda-forge* channel may be better for your needs (e.g. some packages are
available on *conda-forge* and not on *defaults*). Generally, *conda-forge* is
more up to date with the latest versions of geospatial python packages.

GeoPandas and all its dependencies are available on the *conda-forge*
channel, and can be installed as:

```
conda install --channel conda-forge geopandas
```

We strongly recommend to either install everything from the *defaults*
channel, or everything from the *conda-forge* channel. Ending up with a
mixture of packages from both channels for the dependencies of GeoPandas
can lead to import problems.
See the [conda-forge section on using multiple channels](http://conda-forge.org/docs/user/tipsandtricks.html#using-multiple-channels)
for more details.

### Creating a new environment

Creating a new environment is not strictly necessary, but given that installing
other geospatial packages from different channels may cause dependency conflicts
(as mentioned in the note above), it can be good practice to install the geospatial
stack in a clean environment starting fresh.

The following commands create a new environment with the name `geo_env`,
configures it to install packages always from conda-forge, and installs
GeoPandas in it:

```
conda create -n geo_env
conda activate geo_env
conda config --env --add channels conda-forge
conda config --env --set channel_priority strict
conda install python=3 geopandas
```

## Installing with pip

GeoPandas can also be installed with pip, if all dependencies can be installed
as well:

```
pip install geopandas
```

When using pip to install GeoPandas, you need to make sure that all dependencies are
installed correctly.

Our main dependencies ([shapely](https://shapely.readthedocs.io), [pyproj](https://github.com/pyproj4/pyproj), [pyogrio](https://pyogrio.readthedocs.io)) provide binary
wheels with dependencies included for Mac, Linux, and Windows.

However, depending on your platform or Python version, there might be no
pre-compiled wheels available, and then you need to compile and install their C
dependencies manually. We refer to the individual packages for more details on
installing those. Using conda (see above) avoids the need to compile the
dependencies yourself.

Optional runtime dependencies can also be installed all at once:

```
pip install 'geopandas[all]'
```

## Installing from source

You may install the latest development version by cloning the
GitHub repository and using pip to install from the local directory:

```
git clone https://github.com/geopandas/geopandas.git
cd geopandas
pip install .
```

Development dependencies can be installed using the `dev` dependency group:

```
pip install -e . --group dev
```

It is also possible to install the latest development version
directly from the GitHub repository with:

```
pip install git+git://github.com/geopandas/geopandas.git
```

For installing GeoPandas from source, the same [note](#install-deps) on
the need to have all dependencies correctly installed applies. But, those
dependencies can also be installed independently with conda before installing
GeoPandas from source:

```
conda install pandas pyogrio shapely pyproj
```

See the [section on conda](#install-conda) above for more details on
getting running with Anaconda.

## Dependencies

Required dependencies:

- [numpy](http://www.numpy.org)
- [pandas](http://pandas.pydata.org) (version 2.2 or later)
- [shapely](https://shapely.readthedocs.io) (interface to [GEOS](https://geos.osgeo.org); version 2.1 or later)
- [pyogrio](https://pyogrio.readthedocs.io) (interface to [GDAL](https://www.gdal.org/); version 0.8 or later)
- [pyproj](https://github.com/pyproj4/pyproj) (interface to [PROJ](https://proj.org/); version 3.7.0 or later)
- [packaging](https://packaging.pypa.io/en/latest/)

Further, optional dependencies are:

- [fiona](https://fiona.readthedocs.io) (optional; slower alternative to pyogrio)
- [psycopg](https://pypi.python.org/pypi/psycopg) (optional; for PostGIS connection)
- [psycopg2](https://pypi.python.org/pypi/psycopg2) (optional; for PostGIS connection - older version of psycopg library)
- [GeoAlchemy2](https://geoalchemy-2.readthedocs.io/) (optional; for writing to PostGIS)
- [geopy](https://github.com/geopy/geopy) (optional; for geocoding)
- [pointpats](https://pysal.org/pointpats/) (optional; for advanced point sampling)
- [scipy](https://docs.scipy.org/doc/scipy/) (optional; for sparse output of spatial indexing)

For plotting, these additional packages may be used:

- [matplotlib](http://matplotlib.org) (>= 3.9.0)
- [mapclassify](http://pysal.org/mapclassify) (>= 2.7.0)
- [folium](https://python-visualization.github.io/folium/latest/) (for interactive plotting)

On this page

[Show Source](../_sources/getting_started/install.rst.txt)

---

Original source: https://geopandas.org/en/latest/getting_started/install.html
