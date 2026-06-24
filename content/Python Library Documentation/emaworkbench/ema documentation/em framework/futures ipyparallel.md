---
title: "futures_ipyparallel"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/futures_ipyparallel.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `futures_ipyparallel`

Functionality for combining the EMA workbench with IPython parallel.

class ema\_workbench.em\_framework.futures\_ipyparallel.IpyparallelEvaluator(*msis*, *client*, *\*\*kwargs*)
:   evaluator for using an ipypparallel pool.

    evaluate\_experiments(*experiments: Iterable[[Experiment](points.html#ema_workbench.em_framework.points.Experiment "ema_workbench.em_framework.points.Experiment")]*, *callback: Callable*, *\*\*kwargs*)
    :   Evaluate experiments.

    finalize()
    :   Finalize the pool.

    initialize()
    :   Initialize the pool.

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/futures_ipyparallel.html
