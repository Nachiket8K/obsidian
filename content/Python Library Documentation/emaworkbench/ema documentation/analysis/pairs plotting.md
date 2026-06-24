---
title: "pairs_plotting"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/pairs_plotting.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `pairs_plotting`

R-style pairs plotting functionality.

ema\_workbench.analysis.pairs\_plotting.pairs\_density(*experiments: DataFrame*, *outcomes: dict[str, ndarray]*, *outcomes\_to\_show: list[str] | None = None*, *group\_by: str | None = None*, *grouping\_specifiers=None*, *ylabels: dict[str, str] | None = None*, *point\_in\_time: int = -1*, *log: bool = True*, *gridsize: int = 50*, *colormap: str = 'coolwarm'*, *filter\_scalar: bool = True*) → tuple[Figure, dict[str, Axes]]
:   Generate a pairs hexbin density multiplot.

    In case of time-series data, the end states are used.

    hexbin makes hexagonal binning plot of x versus y, where x, y are 1-D
    sequences of the same length, N. If C is None (the default), this is a
    histogram of the number of occurrences of the observations at (x[i],y[i]).
    For further detail see [matplotlib on hexbin](https://matplotlib.sourceforge.net/api/pyplot_api.html#matplotlib.pyplot.hexbin)

    Parameters:
    :   - **experiments** (*DataFrame*)
        - **outcomes** (*dict*)
        - **outcomes\_to\_show** (*list* *of* *str**,* *optional*) – list of outcome of interest you want to plot.
        - **group\_by** (*str**,* *optional*) – name of the column in the cases array to group results by.
          Alternatively, index can be used to use indexing arrays as the
          basis for grouping.
        - **grouping\_specifiers** (*dict**,* *optional*) – dict of categories to be used as a basis for grouping
          by. Grouping\_specifiers is only meaningful if
          group\_by is provided as well. In case of grouping by
          index, the grouping specifiers should be in a
          dictionary where the key denotes the name of the
          group.
        - **ylabels** (*dict**,* *optional*) – ylabels is a dictionary with the outcome names as keys, the
          specified values will be used as labels for the y axis.
        - **point\_in\_time** (*float**,* *optional*) – the point in time at which the scatter is to be made. If
          None is provided (default), the end states are used.
          point\_in\_time should be a valid value on time
        - **log** (*bool**,* *optional*) – indicating whether density should be log scaled. Defaults to True.
        - **gridsize** (*int**,* *optional*) – controls the gridsize for the hexagonal bining. (default = 50)
        - **cmap** (*str*) – color map that is to be used in generating the hexbin. For details
          on the available maps, see [pylab](https://matplotlib.sourceforge.net/examples/pylab_examples/show_colormaps.html#pylab-examples-show-colormaps).
          (Defaults = coolwarm)
        - **filter\_scalar** (*bool**,* *optional*) – remove the non-time-series outcomes. Defaults to True.

    Returns:
    :   - *fig* – the figure instance
        - *dict* – key is tuple of names of outcomes, value is associated axes
          instance

ema\_workbench.analysis.pairs\_plotting.pairs\_lines(*experiments: DataFrame*, *outcomes: dict[str, ndarray]*, *outcomes\_to\_show: list[str] | None = None*, *group\_by: str | None = None*, *grouping\_specifiers=None*, *ylabels: dict[str, str] | None = None*, *legend: bool = True*, *\*\*kwargs*) → tuple[Figure, dict[str, Axes]]
:   Generate a pairs lines multiplot.

    It shows the behavior of two outcomes over time against
    each other. The origin is denoted with a circle and the end is denoted
    with a ‘+’.

    Parameters:
    :   - **experiments** (*DataFrame*)
        - **outcomes** (*dict*)
        - **outcomes\_to\_show** (*list* *of* *str**,* *optional*) – list of outcome of interest you want to plot.
        - **group\_by** (*str**,* *optional*) – name of the column in the cases array to group results by.
          Alternatively, index can be used to use indexing arrays as the
          basis for grouping.
        - **grouping\_specifiers** (*dict**,* *optional*) – dict of categories to be used as a basis for grouping
          by. Grouping\_specifiers is only meaningful if
          group\_by is provided as well. In case of grouping by
          index, the grouping specifiers should be in a
          dictionary where the key denotes the name of the
          group.
        - **ylabels** (*dict**,* *optional*) – ylabels is a dictionary with the outcome names as keys, the
          specified values will be used as labels for the y axis.
        - **legend** (*bool**,* *optional*) – if true, and group\_by is given, show a legend.
        - **point\_in\_time** (*float**,* *optional*) – the point in time at which the scatter is to be made. If
          None is provided (default), the end states are used.
          point\_in\_time should be a valid value on time

    Returns:
    :   - *fig* – the figure instance
        - *dict* – key is tuple of names of outcomes, value is associated axes
          instance

ema\_workbench.analysis.pairs\_plotting.pairs\_scatter(*experiments: DataFrame*, *outcomes: dict[str, ndarray]*, *outcomes\_to\_show: list[str] | None = None*, *group\_by: str | None = None*, *grouping\_specifiers=None*, *ylabels: dict[str, str] | None = None*, *legend: bool = True*, *point\_in\_time: int = -1*, *filter\_scalar: bool = False*, *\*\*kwargs*) → tuple[Figure, dict[str, Axes]]
:   Generate a pairs scatter multiplot.

    In case of time-series data, the end states are used.

    Parameters:
    :   - **experiments** (*DataFrame*)
        - **outcomes** (*dict*)
        - **outcomes\_to\_show** (*list* *of* *str**,* *optional*) – list of outcome of interest you want to plot.
        - **group\_by** (*str**,* *optional*) – name of the column in the cases array to group results by.
          Alternatively, index can be used to use indexing arrays as the
          basis for grouping.
        - **grouping\_specifiers** (*dict**,* *optional*) – dict of categories to be used as a basis for grouping
          by. Grouping\_specifiers is only meaningful if
          group\_by is provided as well. In case of grouping by
          index, the grouping specifiers should be in a
          dictionary where the key denotes the name of the
          group.
        - **ylabels** (*dict**,* *optional*) – ylabels is a dictionary with the outcome names as keys, the
          specified values will be used as labels for the y axis.
        - **legend** (*bool**,* *optional*) – if true, and group\_by is given, show a legend.
        - **point\_in\_time** (*float**,* *optional*) – the point in time at which the scatter is to be made. If
          None is provided (default), the end states are used.
          point\_in\_time should be a valid value on time
        - **filter\_scalar** (*bool**,* *optional*) – remove the non-time-series outcomes. Defaults to True.

    Returns:
    :   - **fig** (*Figure instance*) – the figure instance
        - **axes** (*dict*) – key is tuple of names of outcomes, value is associated axes
          instance
        - *.. note:: the current implementation is limited to seven different* – categories in case of column, categories, and/or
          discretesize. This limit is due to the colors specified
          in COLOR\_LIST.

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/pairs_plotting.html
