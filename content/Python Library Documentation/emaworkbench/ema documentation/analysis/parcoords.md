---
title: "parcoords"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/parcoords.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `parcoords`

A general purpose matplotlib-based parallel coordinate plotting Class.

class ema\_workbench.analysis.parcoords.ParallelAxes(*limits: DataFrame*, *formatter: dict[str, str] | None = None*, *fontsize: int = 14*, *rot: float = 90*)
:   Base class for creating a parallel axis plot.

    Parameters:
    :   - **limits** (*DataFrame*) – A DataFrame specifying the limits for each dimension in the
          data set. For categorical data, the first cell should contain all
          categories. See get\_limits for more details.
        - **formattter** (*dict* *,* *optional*) – dict with precision format strings for minima and maxima, use
          column name as key. If column is not present, or no formatter
          dict is provided, precision formatting defaults to .2f
        - **fontsize** (*int**,* *optional*) – fontsize for defaults text items
        - **rot** (*float**,* *optional*) – rotation of axis labels

    limits
    :   A DataFrame specifying the limits for each dimension in the
        data set. For categorical data, the first cell should contain all
        categories.

        Type:
        :   DataFrame

    recoding
    :   non numeric columns are converting to integer variables

        Type:
        :   dict

    flipped\_axes
    :   set of Axes that are to be shown flipped

        Type:
        :   set

    axis\_labels
    :   Type:
        :   list of str

    fontsize
    :   Type:
        :   int

    fig
    :   Type:
        :   a matplotlib Figure instance

    axes
    :   Type:
        :   list of matplotlib Axes instances

    ticklabels
    :   Type:
        :   list of str

    datalabels
    :   labels associated with lines

        Type:
        :   list of str

    Notes

    The basic setup of the Parallel Axis plot is a row of mpl Axes instances, with all whitespace
    in between removed. The number of Axes is the number of columns - 1.

    invert\_axis(*axis: str | list[str]*) → None
    :   Flip direction for specified axis.

        Parameters:
        :   **axis** (*str* *or* *list* *of* *str*)

    legend() → None
    :   Add a legend to the figure.

    plot(*data: DataFrame | Series*, *color=None*, *label: str | None = None*, *\*\*kwargs*) → None
    :   Plot data on parallel axes.

        Parameters:
        :   - **data** (*DataFrame* *or* *Series*)
            - **color** (*valid mpl color**,* *optional*)
            - **label** (*str**,* *optional*)
            - **plot** (*any additional kwargs will be passed to matplotlib's*)
            - **method.**
            - **initializing** (*Data is normalized using the limits specified when*)
            - **ParallelAxis.**

ema\_workbench.analysis.parcoords.get\_limits(*data: DataFrame*) → DataFrame
:   Helper function to get limits of a FataFrame that can serve as input to ParallelAxis.

    Parameters:
    :   **data** (*DataFrame*)

    Return type:
    :   DataFrame

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/parcoords.html
