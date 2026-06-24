---
title: "feature_scoring"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/feature_scoring.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `feature_scoring`

Feature scoring functionality.

ema\_workbench.analysis.feature\_scoring.CHI2(*X*, *y*)
:   Compute chi-squared stats between each non-negative feature and class.

    This score can be used to select the n\_features features with the
    highest values for the test chi-squared statistic from X, which must
    contain only **non-negative integer feature values** such as booleans or frequencies
    (e.g., term counts in document classification), relative to the classes.

    If some of your features are continuous, you need to bin them, for
    example by using `KBinsDiscretizer`.

    Recall that the chi-square test measures dependence between stochastic
    variables, so using this function “weeds out” the features that are the
    most likely to be independent of class and therefore irrelevant for
    classification.

    Read more in the User Guide.

    Parameters:
    :   - **X** (*{array-like**,* *sparse matrix}* *of* [*shape*](../em_framework/outcomes.html#ema_workbench.em_framework.outcomes.ArrayOutcome.shape "ema_workbench.em_framework.outcomes.ArrayOutcome.shape") *(**n\_samples**,* *n\_features**)*) – Sample vectors.
        - **y** (*array-like* *of* [*shape*](../em_framework/outcomes.html#ema_workbench.em_framework.outcomes.ArrayOutcome.shape "ema_workbench.em_framework.outcomes.ArrayOutcome.shape") *(**n\_samples**,**)*) – Target vector (class labels).

    Returns:
    :   - **chi2** (*ndarray of shape (n\_features,)*) – Chi2 statistics for each feature.
        - **p\_values** (*ndarray of shape (n\_features,)*) – P-values for each feature.

    `f_classif`
    :   ANOVA F-value between label/feature for classification tasks.

    `f_regression`
    :   F-value between label/feature for regression tasks.

    Notes

    Complexity of this algorithm is O(n\_classes \* n\_features).

    Examples

    ```
    >>> import numpy as np
    >>> from sklearn.feature_selection import chi2
    >>> X = np.array([[1, 1, 3],
    ...               [0, 1, 5],
    ...               [5, 4, 1],
    ...               [6, 6, 2],
    ...               [1, 4, 0],
    ...               [0, 0, 0]])
    >>> y = np.array([1, 1, 0, 0, 2, 2])
    >>> chi2_stats, p_values = chi2(X, y)
    >>> chi2_stats
    array([15.3,  6.5       ,  8.9])
    >>> p_values
    array([0.000456, 0.0387, 0.0116 ])
    ```

ema\_workbench.analysis.feature\_scoring.F\_CLASSIFICATION(*X*, *y*)
:   Compute the ANOVA F-value for the provided sample.

    Read more in the User Guide.

    Parameters:
    :   - **X** (*{array-like**,* *sparse matrix}* *of* [*shape*](../em_framework/outcomes.html#ema_workbench.em_framework.outcomes.ArrayOutcome.shape "ema_workbench.em_framework.outcomes.ArrayOutcome.shape") *(**n\_samples**,* *n\_features**)*) – The set of regressors that will be tested sequentially.
        - **y** (*array-like* *of* [*shape*](../em_framework/outcomes.html#ema_workbench.em_framework.outcomes.ArrayOutcome.shape "ema_workbench.em_framework.outcomes.ArrayOutcome.shape") *(**n\_samples**,**)*) – The target vector.

    Returns:
    :   - **f\_statistic** (*ndarray of shape (n\_features,)*) – F-statistic for each feature.
        - **p\_values** (*ndarray of shape (n\_features,)*) – P-values associated with the F-statistic.

    `chi2`
    :   Chi-squared stats of non-negative features for classification tasks.

    `f_regression`
    :   F-value between label/feature for regression tasks.

    Examples

    ```
    >>> from sklearn.datasets import make_classification
    >>> from sklearn.feature_selection import f_classif
    >>> X, y = make_classification(
    ...     n_samples=100, n_features=10, n_informative=2, n_clusters_per_class=1,
    ...     shuffle=False, random_state=42
    ... )
    >>> f_statistic, p_values = f_classif(X, y)
    >>> f_statistic
    array([2.21e+02, 7.02e-01, 1.70e+00, 9.31e-01,
           5.41e+00, 3.25e-01, 4.71e-02, 5.72e-01,
           7.54e-01, 8.90e-02])
    >>> p_values
    array([7.14e-27, 4.04e-01, 1.96e-01, 3.37e-01,
           2.21e-02, 5.70e-01, 8.29e-01, 4.51e-01,
           3.87e-01, 7.66e-01])
    ```

ema\_workbench.analysis.feature\_scoring.F\_REGRESSION(*X*, *y*, *\**, *center=True*, *force\_finite=True*)
:   Univariate linear regression tests returning F-statistic and p-values.

    Quick linear model for testing the effect of a single regressor,
    sequentially for many regressors.

    This is done in 2 steps:

    1. The cross correlation between each regressor and the target is computed
       using `r_regression()` as:

       ```
       E[(X[:, i] - mean(X[:, i])) * (y - mean(y))] / (std(X[:, i]) * std(y))
       ```
    2. It is converted to an F score and then to a p-value.

    `f_regression()` is derived from `r_regression()` and will rank
    features in the same order if all the features are positively correlated
    with the target.

    Note however that contrary to `f_regression()`, `r_regression()`
    values lie in [-1, 1] and can thus be negative. `f_regression()` is
    therefore recommended as a feature selection criterion to identify
    potentially predictive feature for a downstream classifier, irrespective of
    the sign of the association with the target variable.

    Furthermore `f_regression()` returns p-values while
    `r_regression()` does not.

    Read more in the User Guide.

    Parameters:
    :   - **X** (*{array-like**,* *sparse matrix}* *of* [*shape*](../em_framework/outcomes.html#ema_workbench.em_framework.outcomes.ArrayOutcome.shape "ema_workbench.em_framework.outcomes.ArrayOutcome.shape") *(**n\_samples**,* *n\_features**)*) – The data matrix.
        - **y** (*array-like* *of* [*shape*](../em_framework/outcomes.html#ema_workbench.em_framework.outcomes.ArrayOutcome.shape "ema_workbench.em_framework.outcomes.ArrayOutcome.shape") *(**n\_samples**,**)*) – The target vector.
        - **center** (*bool**,* *default=True*) – Whether or not to center the data matrix X and the target vector y.
          By default, X and y will be centered.
        - **force\_finite** (*bool**,* *default=True*) –

          Whether or not to force the F-statistics and associated p-values to
          be finite. There are two cases where the F-statistic is expected to not
          be finite:

          - when the target y or some features in X are constant. In this
            case, the Pearson’s R correlation is not defined leading to obtain
            np.nan values in the F-statistic and p-value. When
            force\_finite=True, the F-statistic is set to 0.0 and the
            associated p-value is set to 1.0.
          - when a feature in X is perfectly correlated (or
            anti-correlated) with the target y. In this case, the F-statistic
            is expected to be np.inf. When force\_finite=True, the F-statistic
            is set to np.finfo(dtype).max and the associated p-value is set to
            0.0.

          Added in version 1.1.

    Returns:
    :   - **f\_statistic** (*ndarray of shape (n\_features,)*) – F-statistic for each feature.
        - **p\_values** (*ndarray of shape (n\_features,)*) – P-values associated with the F-statistic.

    `r_regression`
    :   Pearson’s R between label/feature for regression tasks.

    `f_classif`
    :   ANOVA F-value between label/feature for classification tasks.

    `chi2`
    :   Chi-squared stats of non-negative features for classification tasks.

    `SelectKBest`
    :   Select features based on the k highest scores.

    `SelectFpr`
    :   Select features based on a false positive rate test.

    `SelectFdr`
    :   Select features based on an estimated false discovery rate.

    `SelectFwe`
    :   Select features based on family-wise error rate.

    `SelectPercentile`
    :   Select features based on percentile of the highest scores.

    Examples

    ```
    >>> from sklearn.datasets import make_regression
    >>> from sklearn.feature_selection import f_regression
    >>> X, y = make_regression(
    ...     n_samples=50, n_features=3, n_informative=1, noise=1e-4, random_state=42
    ... )
    >>> f_statistic, p_values = f_regression(X, y)
    >>> f_statistic
    array([1.21, 2.67e13, 2.66])
    >>> p_values
    array([0.276, 1.54e-283, 0.11])
    ```

ema\_workbench.analysis.feature\_scoring.get\_ex\_feature\_scores(*x*, *y*, *mode=RuleInductionType.CLASSIFICATION*, *nr\_trees=100*, *max\_features=None*, *max\_depth=None*, *min\_samples\_split=2*, *min\_samples\_leaf=None*, *min\_weight\_fraction\_leaf=0*, *max\_leaf\_nodes=None*, *bootstrap=True*, *oob\_score=True*, *random\_state=None*)
:   Get feature scores using extra trees.

    Parameters:
    :   - **x** (*DataFrame*)
        - **y** (*1D nd.array*)
        - **mode** (*{RuleInductionType.CLASSIFICATION**,* *RuleInductionType.REGRESSION}*)
        - **nr\_trees** (*int**,* *optional*) – nr. of trees in forest (default=250)
        - **max\_features** (*int**,* *float**,* *string* *or* *None**,* *optional*) – by default, it will use number of features/3, following
          Jaxa-Rozen & Kwakkel (2018) doi: 10.1016/j.envsoft.2018.06.011
          see <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html>
        - **max\_depth** (*int**,* *optional*) – see <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html>
        - **min\_samples\_split** (*int**,* *optional*) – see <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html>
        - **min\_samples\_leaf** (*int**,* *optional*) – defaults to 1 for N=1000 or lower, from there on
          proportional to sqrt of N
          (see discussion in Jaxa-Rozen & Kwakkel (2018) doi: 10.1016/j.envsoft.2018.06.011)
          see <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html>
        - **min\_weight\_fraction\_leaf** (*float**,* *optional*) – see <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html>
        - **max\_leaf\_nodes** (*int* *or* *None**,* *optional*) – see <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html>
        - **bootstrap** (*bool**,* *optional*) – see <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html>
        - **oob\_score** (*bool**,* *optional*) – see <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html>
        - **random\_state** (*int**,* *optional*) – see <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.ExtraTreesClassifier.html>

    Returns:
    :   - *pandas DataFrame* – sorted in descending order of tuples with uncertainty and feature
          scores
        - *object* – either ExtraTreesClassifier or ExtraTreesRegressor

ema\_workbench.analysis.feature\_scoring.get\_feature\_scores\_all(*x*, *y*, *alg='extra trees'*, *mode=RuleInductionType.REGRESSION*, *\*\*kwargs*)
:   Perform feature scoring for all outcomes using the specified feature scoring algorithm.

    Parameters:
    :   - **x** (*DataFrame*)
        - **y** (*dict* *of* *1d numpy arrays*) – the outcomes, with a string as key, and a 1D array for each outcome
        - **alg** (*{'extra trees'**,* *'random forest'**,* *'univariate'}**,* *optional*)
        - **mode** (*{RuleInductionType.REGRESSION**,* *RuleInductionType.CLASSIFICATION}**,* *optional*)
        - **kwargs** (*dict**,* *optional*) – any remaining keyword arguments will be passed to the specific
          feature scoring algorithm

    Return type:
    :   DataFrame instance

ema\_workbench.analysis.feature\_scoring.get\_rf\_feature\_scores(*x*, *y*, *mode=RuleInductionType.CLASSIFICATION*, *nr\_trees=250*, *max\_features='sqrt'*, *max\_depth=None*, *min\_samples\_split=2*, *min\_samples\_leaf=1*, *bootstrap=True*, *oob\_score=True*, *random\_state=None*)
:   Get feature scores using a random forest.

    Parameters:
    :   - **x** (*DataFram**,**e*)
        - **y** (*1D nd.array*)
        - **mode** (*{RuleInductionType.CLASSIFICATION**,* *RuleInductionType.REGRESSION}*)
        - **nr\_trees** (*int**,* *optional*) – nr. of trees in forest (default=250)
        - **max\_features** (*int**,* *optional*) – see <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html>
        - **max\_depth** (*int**,* *optional*) – see <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html>
        - **min\_samples** (*int**,* *optional*) – see <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html>
        - **min\_samples\_leaf** (*int**,* *optional*) – see <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html>
        - **bootstrap** (*bool**,* *optional*) – see <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html>
        - **oob\_score** (*bool**,* *optional*) – see <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html>
        - **random\_state** (*int**,* *optional*) – see <https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html>

    Returns:
    :   - *pandas DataFrame* – sorted in descending order of tuples with uncertainty and feature
          scores
        - *object* – either RandomForestClassifier or RandomForestRegressor

ema\_workbench.analysis.feature\_scoring.get\_univariate\_feature\_scores(*x*, *y*, *score\_func=<function f\_classif>*)
:   Calculate feature scores using univariate statistical tests.

    In case of categorical data, chi square or the Anova F value is used.
    In case of continuous data the Anova F value is used.

    Parameters:
    :   - **x** (*DataFrame*)
        - **y** (*1D nd.array*)
        - **score\_func** (*{F\_CLASSIFICATION**,* *F\_REGRESSION**,* *CHI2}*) – the score function to use, one of f\_regression (regression), or
          f\_classification or chi2 (classification).

    Returns:
    :   sorted in descending order of tuples with uncertainty and feature
        scores (i.e. p values in this case).

    Return type:
    :   pandas DataFrame

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/feature_scoring.html
