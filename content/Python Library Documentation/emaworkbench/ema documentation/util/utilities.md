---
title: "utilities"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/util/utilities.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `utilities`

Convenience functions and classes used throughout the package.

ema\_workbench.util.utilities.load\_results(*file\_name: str*) → tuple[DataFrame, dict[str, ndarray]]
:   Load the specified tar.gz file.

    the file is assumed to be saves using save\_results.

    Parameters:
    :   **file\_name** (*str*) – the path to the file

    Raises:
    :   **IOError if file not found** –

ema\_workbench.util.utilities.merge\_results(*results1: tuple[DataFrame, dict[str, ndarray]]*, *results2: tuple[DataFrame, dict[str, ndarray]]*) → tuple[DataFrame, dict[str, ndarray]]
:   Convenience function for merging results from the workbench.

    The function merges results2 with results1. For the experiments,
    it generates an empty array equal to the size of the sum of the
    experiments. As dtype is uses the dtype from the experiments in results1.
    The function assumes that the ordering of dtypes and names is identical in
    both results.

    A typical use case for this function is in combination with
    `experiments_to_cases()`. Using `experiments_to_cases()`
    one extracts the cases from a first set of experiments. One then
    performs these cases on a different model or policy, and then one wants to
    merge these new results with the old result for further analysis.

    Parameters:
    :   - **results1** (*tuple*) – first results to be merged
        - **results2** (*tuple*) – second results to be merged

    Return type:
    :   the merged results

ema\_workbench.util.utilities.process\_replications(*data: dict[str, ~numpy.ndarray] | tuple[~pandas.DataFrame, dict[str, ~numpy.ndarray]], aggregation\_func: ~collections.abc.Callable[[...], ~numpy.ndarray] = <function mean>*) → dict[str, ndarray] | tuple[DataFrame, dict[str, ndarray]]
:   Convenience function for processing the replications of a stochastic model outcomes.

    The default behavior is to take the mean of the replications. This reduces
    the dimensionality of the outcomes from
    (experiments \* replications \* outcome\_shape) to
    (experiments \* outcome\_shape), where outcome\_shape is 0-d for scalars,
    1-d for time series, and 2-d for arrays.

    The function can take either the outcomes (dictionary: keys are outcomes
    of interest, values are arrays of data) or the results (tuple: experiments
    as DataFrame, outcomes as dictionary) of a set of simulation experiments.

    Parameters:
    :   - **data** (*dict**,* *tuple*) – outcomes or results of a set of experiments
        - **aggregation\_func** (*callabale**,* *optional*) – aggregation function to be applied, defaults to np.mean.

    Return type:
    :   dict, tuple

ema\_workbench.util.utilities.save\_results(*results: tuple[DataFrame, dict[str, ndarray]]*, *file\_name: str*) → None
:   Save the results to the specified tar.gz file.

    The way in which results are stored depends. Experiments are saved
    as csv. Outcomes depend on the outcome type. Scalar, and <3D arrays are
    saved as csv files. Higher dimensional arrays are stored as .npy files.

    Parameters:
    :   - **results** (*tuple*) – the return of perform\_experiments
        - **file\_name** (*str*) – the path of the file

    Raises:
    :   **IOError if file not found** –

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/util/utilities.html
