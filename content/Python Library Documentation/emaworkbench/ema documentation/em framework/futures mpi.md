---
title: "futures_mpi"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/futures_mpi.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `futures_mpi`

Support for MPI evaluators.

class ema\_workbench.em\_framework.futures\_mpi.MPIEvaluator(*msis*, *n\_processes=None*, *\*\*kwargs*)
:   Evaluator for experiments using MPI Pool Executor from mpi4py.

    evaluate\_experiments(*experiments: Iterable[[Experiment](points.html#ema_workbench.em_framework.points.Experiment "ema_workbench.em_framework.points.Experiment")]*, *callback: Callable*, *\*\*kwargs*)
    :   Evaluate experiments using MPIPoolExecutor.

    finalize()
    :   Finalize the MPIPoolExecutor.

    initialize()
    :   Initialize the MPI pool.

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/futures_mpi.html
