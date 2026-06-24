---
title: "robust_optimization_lake_model_dps.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/robust_optimization_lake_model_dps.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# robust\_optimization\_lake\_model\_dps.py

```
  1"""An example of performing robust many objective optimization with the workbench.
  2
  3This example takes the direct policy search formulation of the lake problem as
  4found in Quinn et al (2017), but embeds it in a robust optimization.
  5
  6Quinn, J.D., Reed, P.M., Keller, K. (2017)
  7Direct policy search for robust multi-objective management of deeply
  8uncertain socio-ecological tipping points. Environmental Modelling &
  9Software 92, 125-141.
 10
 11
 12"""
 13
 14import numpy as np
 15from lake_models import lake_problem_dps
 16
 17from ema_workbench import (
 18    Constant,
 19    Model,
 20    MultiprocessingEvaluator,
 21    RealParameter,
 22    ScalarOutcome,
 23    ema_logging,
 24)
 25from ema_workbench.em_framework.samplers import LHSSampler
 26
 27# Created on 1 Jun 2017
 28#
 29# .. codeauthor::jhkwakkel <j.h.kwakkel (at) tudelft (dot) nl>
 30
 31
 32if __name__ == "__main__":
 33    ema_logging.log_to_stderr(ema_logging.INFO)
 34
 35    # instantiate the model
 36    lake_model = Model("lakeproblem", function=lake_problem_dps)
 37    # specify uncertainties
 38    lake_model.uncertainties = [
 39        RealParameter("b", 0.1, 0.45),
 40        RealParameter("q", 2.0, 4.5),
 41        RealParameter("mean", 0.01, 0.05),
 42        RealParameter("stdev", 0.001, 0.005),
 43        RealParameter("delta", 0.93, 0.99),
 44    ]
 45
 46    # set levers
 47    lake_model.levers = [
 48        RealParameter("c1", -2, 2),
 49        RealParameter("c2", -2, 2),
 50        RealParameter("r1", 0, 2),
 51        RealParameter("r2", 0, 2),
 52        RealParameter("w1", 0, 1),
 53    ]
 54
 55    # specify outcomes
 56    lake_model.outcomes = [
 57        ScalarOutcome("max_p"),
 58        ScalarOutcome("utility"),
 59        ScalarOutcome("inertia"),
 60        ScalarOutcome("reliability"),
 61    ]
 62
 63    # override some of the defaults of the model
 64    lake_model.constants = [
 65        Constant("alpha", 0.41),
 66        Constant("n_samples", 100),
 67        Constant("myears", 100),
 68    ]
 69
 70    # setup and execute the robust optimization
 71    def signal_to_noise(data):
 72        """Signal to Noise calculation."""
 73        mean = np.mean(data)
 74        std = np.std(data)
 75        sn = mean / std
 76        return sn
 77
 78    MAXIMIZE = ScalarOutcome.MAXIMIZE  # @UndefinedVariable
 79    MINIMIZE = ScalarOutcome.MINIMIZE  # @UndefinedVariable
 80    robustness_functions = [
 81        ScalarOutcome("mean_p", kind=MINIMIZE, variable_name="max_p", function=np.mean),
 82        ScalarOutcome("std_p", kind=MINIMIZE, variable_name="max_p", function=np.std),
 83        ScalarOutcome(
 84            "sn_reliability",
 85            kind=MAXIMIZE,
 86            variable_name="reliability",
 87            function=signal_to_noise,
 88        ),
 89    ]
 90    n_scenarios = 10
 91    scenarios = LHSSampler().generate_samples(
 92        lake_model.uncertainties, n_scenarios, rng=42
 93    )
 94    nfe = 1000
 95
 96    with MultiprocessingEvaluator(lake_model) as evaluator:
 97        results, convergence_info = evaluator.robust_optimize(
 98            robustness_functions,
 99            scenarios,
100            nfe=nfe,
101            epsilons=[0.1] * len(robustness_functions),
102            population_size=5,
103            filename="lake_model_robust_archive.tar.gz",
104            directory="./data",
105        )
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/robust_optimization_lake_model_dps.html
