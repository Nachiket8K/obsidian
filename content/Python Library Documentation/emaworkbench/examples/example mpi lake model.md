---
title: "example_mpi_lake_model.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/example_mpi_lake_model.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# example\_mpi\_lake\_model.py

```
  1"""An example of the lake problem using the ema workbench with the MPI evaluator.
  2
  3The model itself is adapted from the Rhodium example by Dave Hadka,
  4see https://gist.github.com/dhadka/a8d7095c98130d8f73bc
  5
  6"""
  7
  8import os
  9import sys
 10
 11sys.path.insert(1, os.path.abspath("../../"))
 12
 13import math
 14import time
 15
 16import numpy as np
 17from scipy.optimize import brentq
 18
 19from ema_workbench import (
 20    Constant,
 21    Model,
 22    MPIEvaluator,
 23    RealParameter,
 24    ScalarOutcome,
 25    ema_logging,
 26    save_results,
 27)
 28
 29
 30def lake_problem(
 31    b=0.42,  # decay rate for P in lake (0.42 = irreversible)
 32    q=2.0,  # recycling exponent
 33    mean=0.02,  # mean of natural inflows
 34    stdev=0.001,  # future utility discount rate
 35    delta=0.98,  # standard deviation of natural inflows
 36    alpha=0.4,  # utility from pollution
 37    nsamples=100,  # Monte Carlo sampling of natural inflows
 38    **kwargs,
 39):
 40    """Intertemporal version of the lake problem."""
 41    try:
 42        decisions = [kwargs[str(i)] for i in range(100)]
 43    except KeyError:
 44        decisions = [0] * 100
 45        print("No valid decisions found, using 0 water release every year as default")
 46
 47    n_vars = len(decisions)
 48    decisions = np.array(decisions)
 49
 50    # Calculate the critical pollution level ({_crit)
 51    p_crit = brentq(lambda x: x**q / (1 + x**q) - b * x, 0.01, 1.5)
 52
 53    # Generate natural inflows using lognormal distribution
 54    natural_inflows = np.random.lognormal(
 55        mean=math.log(mean**2 / math.sqrt(stdev**2 + mean**2)),
 56        sigma=math.sqrt(math.log(1.0 + stdev**2 / mean**2)),
 57        size=(nsamples, n_vars),
 58    )
 59
 60    # Initialize the pollution level matrix X
 61    x = np.zeros((nsamples, n_vars))
 62
 63    # Loop through time to compute the pollution levels
 64    for t in range(1, n_vars):
 65        x[:, t] = (
 66            (1 - b) * x[:, t - 1]
 67            + (x[:, t - 1] ** q / (1 + x[:, t - 1] ** q))
 68            + decisions[t - 1]
 69            + natural_inflows[:, t - 1]
 70        )
 71
 72    # Calculate the average daily pollution for each time step
 73    average_daily_p = np.mean(x, axis=0)
 74
 75    # Calculate the reliability (probability of the pollution level being below {_crit)
 76    reliability = np.sum(p_crit > x) / float(nsamples * n_vars)
 77
 78    # Calculate the maximum pollution level (max_p)
 79    max_p = np.max(average_daily_p)
 80
 81    # Calculate the utility by discounting the decisions using the discount factor (delta)
 82    utility = np.sum(alpha * decisions * np.power(delta, np.arange(n_vars)))
 83
 84    # Calculate the inertia (the fraction of time steps with changes larger than 0.02)
 85    inertia = np.sum(np.abs(np.diff(decisions)) > 0.02) / float(n_vars - 1)
 86
 87    return max_p, utility, inertia, reliability
 88
 89
 90if __name__ == "__main__":
 91    import ema_workbench
 92
 93    # run with env MPI4PY_FUTURES_MAX_WORKERS=4 mpiexec -n 1 python example_mpi_lake_model.py
 94    starttime = time.perf_counter()
 95
 96    ema_logging.log_to_stderr(ema_logging.INFO, pass_root_logger_level=True)
 97    ema_logging.get_rootlogger().info(f"{ema_workbench.__version__}")
 98
 99    # instantiate the model
100    lake_model = Model("lakeproblem", function=lake_problem)
101    lake_model.time_horizon = 100
102
103    # specify uncertainties
104    lake_model.uncertainties = [
105        RealParameter("b", 0.1, 0.45),
106        RealParameter("q", 2.0, 4.5),
107        RealParameter("mean", 0.01, 0.05),
108        RealParameter("stdev", 0.001, 0.005),
109        RealParameter("delta", 0.93, 0.99),
110    ]
111
112    # set levers, one for each time step
113    lake_model.levers = [
114        RealParameter(str(i), 0, 0.1) for i in range(lake_model.time_horizon)
115    ]
116
117    # specify outcomes
118    lake_model.outcomes = [
119        ScalarOutcome("max_P"),
120        ScalarOutcome("utility"),
121        ScalarOutcome("inertia"),
122        ScalarOutcome("reliability"),
123    ]
124
125    # override some of the defaults of the model
126    lake_model.constants = [Constant("alpha", 0.41), Constant("n_samples", 150)]
127
128    # generate some random policies by sampling over levers
129    n_scenarios = 10000
130    n_policies = 4
131
132    with MPIEvaluator(lake_model) as evaluator:
133        res = evaluator.perform_experiments(n_scenarios, n_policies, chunksize=250)
134
135    save_results(res, f"mpi_{n_scenarios}-scen-{n_policies}-policies-results.tar.gz")
136
137    print(time.perf_counter() - starttime)
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/example_mpi_lake_model.html
