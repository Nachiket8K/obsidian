---
title: "futures_multiprocessing"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/futures_multiprocessing.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `futures_multiprocessing`

support for using the multiprocessing library in combination with the workbench.

class ema\_workbench.em\_framework.futures\_multiprocessing.MultiprocessingEvaluator(*msis*, *n\_processes=None*, *maxtasksperchild=None*, *\*\*kwargs*)
:   Evaluator for experiments using a multiprocessing pool.

    Parameters:
    :   - **msis** (*collection* *of* [*models*](../analysis/logistic_regression.html#ema_workbench.analysis.logistic_regression.Logit.models "ema_workbench.analysis.logistic_regression.Logit.models"))
        - **n\_processes** (*int* *(**optional**)*) – A negative number can be inputted to use the number of logical cores minus the negative cores.
          For example, on a 12 thread processor, -2 results in using 10 threads.
        - **max\_tasks** (*int* *(**optional**)*)

    note that the maximum number of available processes is either multiprocessing.cpu\_count()
    and in case of windows, this never can be higher then 61

    evaluate\_experiments(*experiments: Iterable[[Experiment](points.html#ema_workbench.em_framework.points.Experiment "ema_workbench.em_framework.points.Experiment")]*, *callback: Callable*, *\*\*kwargs*)
    :   Evaluate experiments.

    finalize()
    :   Finalize the pool.

    initialize()
    :   Initialize the multiprocessing pool.

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/futures_multiprocessing.html
