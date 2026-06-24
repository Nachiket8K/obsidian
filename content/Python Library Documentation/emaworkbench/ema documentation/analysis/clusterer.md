---
title: "clusterer"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/clusterer.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `clusterer`

Time series clustering functionality using complex invariant distance.

For details see [Steinmann et al (2020)](https://doi.org/10.1016/j.techfore.2020.120052)

ema\_workbench.analysis.clusterer.apply\_agglomerative\_clustering(*distances*, *n\_clusters*, *metric='precomputed'*, *linkage='average'*)
:   Apply agglomerative clustering to the distances.

    Parameters:
    :   - **distances** (*ndarray*)
        - **n\_clusters** (*int*)
        - **metric** (*str**,* *optional. The distance metric to use. The default is 'precomputed'. For a list* *of* *available metrics**,* *see the documentation* *of* *scipy.spatial.distance.pdist.*)
        - **linkage** (*{'average'**,* *'complete'**,* *'single'}*)

    Return type:
    :   1D ndarray with cluster assignment

ema\_workbench.analysis.clusterer.calculate\_cid(*data*, *condensed\_form=False*)
:   Calculate the complex invariant distance between all rows.

    Parameters:
    :   - **data** (*2d ndarray*)
        - **condensed\_form** (*bool**,* *optional*)

    Returns:
    :   a 2D ndarray with the distances between all time series, or condensed
        form similar to scipy.spatial.distance.pdist¶

    Return type:
    :   distances

ema\_workbench.analysis.clusterer.plot\_dendrogram(*distances*)
:   Plot dendrogram for distances.

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/clusterer.html
