---
title: "cart"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/cart.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `cart`

A scenario discovery oriented implementation of CART.

It essentially is a wrapper around scikit-learn’s version of CART, with some scneario
discovery specific functionality.

class ema\_workbench.analysis.cart.CART(*x: DataFrame*, *y: ndarray[tuple[Any, ...], dtype[\_ScalarT]]*, *mass\_min: float = 0.05*, *mode: [RuleInductionType](scenario_discovery_util.html#ema_workbench.analysis.scenario_discovery_util.RuleInductionType "ema_workbench.analysis.scenario_discovery_util.RuleInductionType") = RuleInductionType.BINARY*)
:   CART algorithm.

    Can be used in a manner similar to PRIM. It provides access
    to the underlying tree, but it can also show the boxes described by the
    tree in a table or graph form similar to prim.

    Parameters:
    :   - **x** (*DataFrame*)
        - **y** (*1D ndarray*)
        - **mass\_min** (*float**,* *optional*) – a value between 0 and 1 indicating the minimum fraction
          of data points in a terminal leaf. Defaults to 0.05,
          identical to prim.
        - **mode** (*{BINARY**,* [*CLASSIFICATION*](scenario_discovery_util.html#ema_workbench.analysis.scenario_discovery_util.RuleInductionType.CLASSIFICATION "ema_workbench.analysis.scenario_discovery_util.RuleInductionType.CLASSIFICATION")*,* *REGRESSION}*) – indicates the mode in which CART is used. Binary indicates
          binary classification, classification is multiclass, and regression
          is regression.

    boxes
    :   list of DataFrame box lims

        Type:
        :   list

    stats
    :   list of dicts with stats

        Type:
        :   list

    Notes

    This class is a wrapper around scikit-learn’s CART algorithm. It provides
    an interface to CART that is more oriented towards scenario discovery, and
    shared some methods with PRIM

    `prim`

    property boxes: list[DataFrame]
    :   Return a list with the box limits for each terminal leaf.

        Return type:
        :   list with boxlims for each terminal leaf

    build\_tree() → None
    :   Train CART on the data.

    show\_tree(*mplfig: bool = True*, *format: str = 'png'*)
    :   Return a png (defaults) or svg of the tree.

        On Windows, graphviz needs to be installed with conda.

        Parameters:
        :   - **mplfig** (*bool**,* *optional*) – if true (default) returns a matplotlib figure with the tree,
              otherwise, it returns the output as bytes
            - **format** (*{'png'**,* *'svg'}**,* *default 'png'*) – Gives a format of the output.

    property stats: list[dict]
    :   Returns list with the scenario discovery statistics for each terminal leaf.

        Return type:
        :   list with scenario discovery statistics for each terminal leaf

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/cart.html
