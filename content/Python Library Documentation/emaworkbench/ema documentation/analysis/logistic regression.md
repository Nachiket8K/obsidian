---
title: "logistic_regression"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/logistic_regression.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `logistic_regression`

Logistic regression for scenario discovery.

The module draws its inspiration from Quinn et al (2018) 10.1029/2018WR022743
and Lamontagne et al (2019). The implementation here generalizes their work
and embeds it in a more typical scenario discovery workflow with a posteriori
selection of the appropriate number of dimensions to include. It is modeled
as much as possible on the api used for PRIM and CART.

class ema\_workbench.analysis.logistic\_regression.Logit(*x*, *y*, *threshold=0.95*)
:   Interactive logistic regression using BIC based forward selection.

    Parameters:
    :   - **x** (*DataFrame*)
        - **y** (*numpy Array*)
        - **threshold** (*float*)

    coverage
    :   coverage of currently selected model

        Type:
        :   float

    density
    :   density of currently selected model

        Type:
        :   float

    res\_dim
    :   number of restricted dimensions of currently selected model

        Type:
        :   int

    peeling\_trajectory
    :   stats for each model in peeling trajectory

        Type:
        :   DataFrame

    models
    :   list of models associated with each model on the peeling
        trajectory

        Type:
        :   list

    inspect(*i*, *step=0.1*)
    :   Inspect model i by showing the threshold tradeoff and summary.

        Parameters:
        :   - **i** (*int*)
            - **step** (*float between* *[**0**,* *1**]*)

    plot\_pairwise\_scatter(*i*, *threshold=0.95*)
    :   Plot pairwise scatter plot of data points, with contours as background.

        Parameters:
        :   - **i** (*int*)
            - **threshold** (*float*)

        Return type:
        :   Figure instance

        The lower triangle background is a binary contour based on the
        specified threshold. All axis not shown are set to a default value
        in the middle of their range

        The upper triangle shows a contour map with the conditional
        probability, again setting all non shown dimensions to a default value
        in the middle of their range.

    run(*\*\*kwargs*)
    :   Run logistic regression using forward selection.

        The code uses the Bayesian Information Criterion for selecting
        whether and if so which dimension to add.

        Parameters:
        :   - **details** (*kwargs are passed on to model.fit. For*)
            - **https** (*see*)

    show\_threshold\_tradeoff(*i*, *cmap=<matplotlib.colors.ListedColormap object>*, *step=0.1*)
    :   Visualize the trade-off between coverage and density for model i.

        Parameters:
        :   - **i** (*int*)
            - **cmap** (*valid matplotlib colormap*)
            - **step** (*float**,* *optional*)

        Return type:
        :   a Figure instance

    show\_tradeoff(*cmap=<matplotlib.colors.ListedColormap object>*, *annotated=False*)
    :   Visualize the trade-off between coverage and density.

        Color is used to denote the number of restricted dimensions.

        Parameters:
        :   - **cmap** (*valid matplotlib colormap*)
            - **annotated** (*bool**,* *optional. Shows point labels if True.*)

        Return type:
        :   a Figure instance

    property threshold
    :   Return threshold.

    update(*model*, *selected*)
    :   Helper function.

        It adds a model to the collection of models and
        update the associated attributes.

        Parameters:
        :   - **model** (*statsmodel fitted logit model*)
            - **selected** (*list* *of* *str*)

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/logistic_regression.html
