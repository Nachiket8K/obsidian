---
title: "regional_sa"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/regional_sa.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `regional_sa`

Module offers support for performing basic regional sensitivity analysis.

Th module can be used to perform regional sensitivity analysis on all
uncertainties specified in the experiment array, as well as the ability to
zoom in on any given uncertainty in more detail.

ema\_workbench.analysis.regional\_sa.plot\_cdfs(*x*, *y*, *ccdf=False*)
:   Plot cumulative density functions for each column in x.

    Based on the classification specified in y.

    Parameters:
    :   - **x** (*DataFrame*) – the experiments to use in the cdfs
        - **y** (*ndaray*) – the categorization for the data
        - **ccdf** (*bool**,* *optional*) – if true, plot a complementary cdf instead of a normal cdf.

    Return type:
    :   a matplotlib Figure instance

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/regional_sa.html
