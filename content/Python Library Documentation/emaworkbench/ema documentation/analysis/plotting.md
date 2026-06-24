---
title: "plotting"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/plotting.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `plotting`

Functions for generating some basic figures.

The code can be used as is, or serve as an example for writing your own code.

ema\_workbench.analysis.plotting.envelopes(*experiments: DataFrame*, *outcomes: dict[str, ndarray]*, *outcomes\_to\_show: str | list[str] | None = None*, *group\_by: str | None = None*, *grouping\_specifiers=None*, *density: [Density](plotting_util.html#ema_workbench.analysis.plotting_util.Density "ema_workbench.analysis.plotting_util.Density") | None = None*, *fill: bool = False*, *legend: bool = True*, *titles: dict[str, str] | None = None*, *ylabels: dict[str, str] | None = None*, *log: bool = False*) → tuple[Figure, dict[str, Axes]]
:   Make envelop plots.

    An envelope shows over time the minimum and maximum value for a set
    of runs over time. It is thus to be used in case of time series
    data. The function will try to find a result labeled “TIME”. If this
    is present, these values will be used on the X-axis. In case of
    Vensim models, TIME is present by default.

    Parameters:
    :   - **experiments** (*DataFrame*)
        - **outcomes** (*OutcomesDict*)
        - **outcomes\_to\_show**
        - **str** (*list of*)
        - **str**
        - **optional**
        - **group\_by** (*str**,* *optional*) – name of the column in the experimentsto group results by.
          Alternatively, index can be used to use indexing
          arrays as the basis for grouping.
        - **grouping\_specifiers** (*iterable* *or* *dict**,* *optional*) – set of categories to be used as a basis for
          grouping by. Grouping\_specifiers is only
          meaningful if group\_by is provided as well.
          In case of grouping by index, the grouping
          specifiers should be in a dictionary where
          the key denotes the name of the group.
        - **density** (*{None**,* [*HIST*](plotting_util.html#ema_workbench.analysis.plotting_util.Density.HIST "ema_workbench.analysis.plotting_util.Density.HIST")*,* [*KDE*](plotting_util.html#ema_workbench.analysis.plotting_util.Density.KDE "ema_workbench.analysis.plotting_util.Density.KDE")*,* [*VIOLIN*](plotting_util.html#ema_workbench.analysis.plotting_util.Density.VIOLIN "ema_workbench.analysis.plotting_util.Density.VIOLIN")*,* *BOXPLOT}**,* *optional*)
        - **fill** (*bool**,* *optional*)
        - **legend** (*bool**,* *optional*)
        - **titles** (*dict**,* *optional*) – a way for controlling whether each of the axes should have a
          title. There are three possibilities. If set to None, no title
          will be shown for any of the axes. If set to an empty dict,
          the default, the title is identical to the name of the outcome of
          interest. If you want to override these default names, provide a
          dict with the outcome of interest as key and the desired title as
          value. This dict need only contain the outcomes for which you
          want to use a different title.
        - **ylabels** (*dict**,* *optional*) – way for controlling the ylabels. Works identical to titles.
        - **log** (*bool**,* *optional*) – log scale density plot

    Returns:
    :   - **Figure** (*Figure instance*)
        - **axes** (*dict*) – dict with outcome as key, and axes as value. Density axes’ are
          indexed by the outcome followed by \_density.
        - *Note*
        - *—-*
        - *the current implementation is limited to seven different categories in case*
        - *of group\_by, categories, and/or discretesize. This limit is due to the colors*
        - *specified in COLOR\_LIST.*

    Examples

    ```
    >>> import util as util
    >>> data = util.load_results('1000 flu cases.tar.gz')
    >>> envelopes(data, group_by='policy')
    ```

    will show an envelope for three different policies, for all the
    outcomes of interest. while

    ```
    >>> envelopes(data, group_by='policy', categories=['static policy',
                  'adaptive policy'])
    ```

    will only show results for the two specified policies, ignoring any results
    associated with no policy.

ema\_workbench.analysis.plotting.kde\_over\_time(*experiments: DataFrame*, *outcomes: dict[str, ndarray]*, *outcomes\_to\_show: str | list[str] | None = None*, *group\_by: str | None = None*, *grouping\_specifiers=None*, *colormap: str = 'viridis'*, *log: bool = True*)
:   Plot a KDE over time. The KDE is visualized through a heatmap.

    Parameters:
    :   - **experiments** (*DataFrame*)
        - **outcomes** (*OutcomesDict*)
        - **outcomes\_to\_show** (*list* *of* *str**,* *optional*) – list of outcome of interest you want to plot. If
          empty, all outcomes are plotted.
          **Note**: just names.
        - **group\_by** (*str**,* *optional*) – name of the column in the cases array to group results
          by. Alternatively, index can be used to use indexing
          arrays as the basis for grouping.
        - **grouping\_specifiers** (*iterable* *or* *dict**,* *optional*) – set of categories to be used as a basis for
          grouping by. Grouping\_specifiers is only
          meaningful if group\_by is provided as well.
          In case of grouping by index, the grouping
          specifiers should be in a dictionary where
          the key denotes the name of the group.
        - **colormap** (*str**,* *optional*) – valid matplotlib color map name
        - **log** (*bool**,* *optional*)

    Returns:
    :   - *list of Figure instances* – a figure instance for each group for each outcome
        - *dict* – dict with outcome as key, and axes as value. Density axes’ are
          indexed by the outcome followed by \_density

ema\_workbench.analysis.plotting.lines(*experiments: DataFrame*, *outcomes: dict[str, ndarray]*, *outcomes\_to\_show: str | list[str] | None = None*, *group\_by: str | None = None*, *grouping\_specifiers=None*, *density: [Density](plotting_util.html#ema_workbench.analysis.plotting_util.Density "ema_workbench.analysis.plotting_util.Density") | str = ''*, *legend: bool = True*, *titles: dict[str, str] | None = None*, *ylabels: dict[str, str] | None = None*, *experiments\_to\_show: ndarray | None = None*, *show\_envelope: bool = False*, *log: bool = False*) → tuple[Figure, dict[str, Axes]]
:   Visualize results from experiments as line plots.

    It is thus to be used in case of time
    series data. The function will try to find a result labeled “TIME”. If this
    is present, these values will be used on the X-axis. In case of Vensim
    models, TIME is present by default.

    Parameters:
    :   - **experiments** (*DataFrame*)
        - **outcomes** (*OutcomesDict*)
        - **outcomes\_to\_show** (*list* *of* *str**,* *optional*) – list of outcome of interest you want to plot. If empty,
          all outcomes are plotted. **Note**: just names.
        - **group\_by** (*str**,* *optional*) – name of the column in the cases array to group results by.
          Alternatively, index can be used to use indexing arrays as the
          basis for grouping.
        - **grouping\_specifiers** (*iterable* *or* *dict**,* *optional*) – set of categories to be used as a basis for grouping
          by. Grouping\_specifiers is only meaningful if
          group\_by is provided as well. In case of grouping by
          index, the grouping specifiers should be in a
          dictionary where the key denotes the name of the
          group.
        - **density** (*{None**,* [*HIST*](plotting_util.html#ema_workbench.analysis.plotting_util.Density.HIST "ema_workbench.analysis.plotting_util.Density.HIST")*,* [*KDE*](plotting_util.html#ema_workbench.analysis.plotting_util.Density.KDE "ema_workbench.analysis.plotting_util.Density.KDE")*,* [*VIOLIN*](plotting_util.html#ema_workbench.analysis.plotting_util.Density.VIOLIN "ema_workbench.analysis.plotting_util.Density.VIOLIN")*,* *BOXPLOT}**,* *optional*)
        - **legend** (*bool**,* *optional*)
        - **titles** (*dict**,* *optional*) – a way for controlling whether each of the axes should have a
          title. There are three possibilities. If set to None, no title
          will be shown for any of the axes. If set to an empty dict,
          the default, the title is identical to the name of the outcome of
          interest. If you want to override these default names, provide a
          dict with the outcome of interest as key and the desired title as
          value. This dict need only contain the outcomes for which you
          want to use a different title.
        - **ylabels** (*dict**,* *optional*) – way for controlling the ylabels. Works identical to titles.
        - **experiments\_to\_show** (*ndarray**,* *optional*) – indices of experiments to show lines for,
          defaults to None.
        - **show\_envelope** (*bool**,* *optional*) – show envelope of outcomes. This envelope is the based on
          the minimum at each column and the maximum at each column.
        - **log** (*bool**,* *optional*) – log scale density plot

    Returns:
    :   - **fig** (*Figure instance*)
        - **axes** (*dict*) – dict with outcome as key, and axes as value. Density axes’ are
          indexed by the outcome followed by \_density.
        - *Note*
        - *—-*
        - *the current implementation is limited to seven different categories in case*
        - *of group\_by, categories, and/or discretesize. This limit is due to the colors*
        - *specified in COLOR\_LIST.*

ema\_workbench.analysis.plotting.multiple\_densities(*experiments: DataFrame*, *outcomes: dict[str, ndarray]*, *points\_in\_time: list[float] | None = None*, *outcomes\_to\_show: str | list[str] | None = None*, *group\_by: str | None = None*, *grouping\_specifiers=None*, *density: [Density](plotting_util.html#ema_workbench.analysis.plotting_util.Density "ema_workbench.analysis.plotting_util.Density") = Density.KDE*, *legend: bool = True*, *titles: dict[str, str] | None = None*, *ylabels: dict[str, str] | None = None*, *experiments\_to\_show: ndarray | None = None*, *plot\_type: [PlotType](plotting_util.html#ema_workbench.analysis.plotting_util.PlotType "ema_workbench.analysis.plotting_util.PlotType") = PlotType.ENVELOPE*, *log: bool = False*, *\*\*kwargs*) → tuple[list[Figure], dict[str, dict[str, Axes]]]
:   Make an envelope plot with multiple density plots over the run time.

    Parameters:
    :   - **experiments** (*DataFrame*)
        - **outcomes** (*OutcomesDict*)
        - **points\_in\_time** (*list*) – a list of points in time for which you want to see the
          density. At the moment up to 6 points in time are
          supported
        - **outcomes\_to\_show** (*list* *of* *str**,* *optional*) – list of outcome of interest you want to plot. If empty,
          all outcomes are plotted. **Note**: just names.
        - **group\_by** (*str**,* *optional*) – name of the column in the cases array to group results by.
          Alternatively, index can be used to use indexing arrays as the
          basis for grouping.
        - **grouping\_specifiers** (*iterable* *or* *dict**,* *optional*) – set of categories to be used as a basis for grouping
          by. Grouping\_specifiers is only meaningful if
          group\_by is provided as well. In case of grouping by
          index, the grouping specifiers should be in a
          dictionary where the key denotes the name of the
          group.
        - **density** (*{Density.KDE**,* [*Density.HIST*](plotting_util.html#ema_workbench.analysis.plotting_util.Density.HIST "ema_workbench.analysis.plotting_util.Density.HIST")*,* [*Density.VIOLIN*](plotting_util.html#ema_workbench.analysis.plotting_util.Density.VIOLIN "ema_workbench.analysis.plotting_util.Density.VIOLIN")*,* *Density.BOXPLOT}**,*) – optional
        - **legend** (*bool**,* *optional*)
        - **titles** (*dict**,* *optional*) – a way for controlling whether each of the axes should have a
          title. There are three possibilities. If set to None, no title
          will be shown for any of the axes. If set to an empty dict,
          the default, the title is identical to the name of the outcome of
          interest. If you want to override these default names, provide a
          dict with the outcome of interest as key and the desired title as
          value. This dict need only contain the outcomes for which you
          want to use a different title.
        - **ylabels** (*dict**,* *optional*) – way for controlling the ylabels. Works identical to titles.
        - **experiments\_to\_show** (*ndarray**,* *optional*) – indices of experiments to show lines for,
          defaults to None.
        - **plot\_type** (*{PlotType.ENVELOPE**,* [*PlotType.ENV\_LIN*](plotting_util.html#ema_workbench.analysis.plotting_util.PlotType.ENV_LIN "ema_workbench.analysis.plotting_util.PlotType.ENV_LIN")*,* *PlotType.LINES}**,* *optional*)
        - **log** (*bool**,* *optional*)

    Returns:
    :   - **fig** (*Figure instance*)
        - **axes** (*dict*) – dict with outcome as key, and axes as value. Density axes’ are
          indexed by the outcome followed by \_density.
        - *Note*
        - *—-*
        - *the current implementation is limited to seven different categories*
        - *in case of group\_by, categories, and/or discretesize. This limit is*
        - *due to the colors specified in COLOR\_LIST.*
        - *Note*
        - *—-*
        - *the connection patches are for some reason not drawn if log scaling is*
        - *used for the density plots. This appears to be an issue in matplotlib*
        - *itself.*

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/plotting.html
