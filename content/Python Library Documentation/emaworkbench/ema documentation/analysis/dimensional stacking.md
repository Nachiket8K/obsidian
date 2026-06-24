---
title: "dimensional_stacking"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/dimensional_stacking.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `dimensional_stacking`

Functionality for dimensional stacking based scenario discovery.

It is inspired by the work reported [here](https://www.onepetro.org/conference-paper/SPE-174774-MS)
with one deviation. Rather than using association rules to identify the
uncertain factors to use, this code uses random forest based feature scoring
instead. It is also possible to use the code provided here in combination
with any other feature scoring or factor prioritization technique instead, or
by simply selecting uncertain factors in some other manner.

ema\_workbench.analysis.dimensional\_stacking.create\_pivot\_plot(*x*, *y*, *nr\_levels=3*, *labels=True*, *categories=True*, *nbins=3*, *bin\_labels=False*)
:   Convenience function for easily creating a pivot plot.

    Parameters:
    :   - **x** (*DataFrame*)
        - **y** (*1d ndarray*)
        - **nr\_levels** (*int**,* *optional*) – the number of levels in the pivot table. The number of
          uncertain factors included in the pivot table is two
          times the number of levels.
        - **labels** (*bool**,* *optional*) – display names of uncertain factors
        - **categories** (*bool**,* *optional*) – display category names for each uncertain factor
        - **nbins** (*int**,* *optional*) – number of bins to use when discretizing continuous uncertain
          factors
        - **bin\_labels** (*bool**,* *optional*) – if True show bin interval / name, otherwise show
          only a number

    Return type:
    :   Figure

    This function performs feature scoring using random forests, selects
    a number of high scoring factors based on the specified number of
    levels, creates a pivot table, and visualizes the table. This is a
    convenience function. For more control over the process, use the
    code in this function as a template.

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/dimensional_stacking.html
