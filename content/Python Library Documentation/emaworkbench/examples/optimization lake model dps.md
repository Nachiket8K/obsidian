---
title: "optimization_lake_model_dps.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/optimization_lake_model_dps.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# optimization\_lake\_model\_dps.py

```
  1"""An example of using the workbench for many objective optimization.
  2
  3This example replicates Quinn, J.D., Reed, P.M., Keller, K. (2017)
  4Direct policy search for robust multi-objective management of deeply
  5uncertain socio-ecological tipping points. Environmental Modelling &
  6Software 92, 125-141.
  7
  8It also showcases how the workbench can be used to apply the MORDM extension
  9suggested by Watson, A.A., Kasprzyk, J.R. (2017) Incorporating deeply uncertain
 10factors into the many objective search process. Environmental Modelling &
 11Software 89, 159-171.
 12
 13"""
 14
 15import random
 16
 17from lake_models import lake_problem_dps
 18
 19from ema_workbench import (
 20    Constant,
 21    Model,
 22    MultiprocessingEvaluator,
 23    RealParameter,
 24    Sample,
 25    ScalarOutcome,
 26    ema_logging,
 27)
 28from ema_workbench.em_framework import LHSSampler
 29from ema_workbench.em_framework.optimization import GenerationalBorg
 30
 31# Created on 1 Jun 2017
 32#
 33# .. codeauthor::jhkwakkel <j.h.kwakkel (at) tudelft (dot) nl>
 34
 35
 36if __name__ == "__main__":
 37    ema_logging.log_to_stderr(ema_logging.INFO)
 38
 39    # instantiate the model
 40    lake_model = Model("lakeproblem", function=lake_problem_dps)
 41    # specify uncertainties
 42    lake_model.uncertainties = [
 43        RealParameter("b", 0.1, 0.45),
 44        RealParameter("q", 2.0, 4.5),
 45        RealParameter("mean", 0.01, 0.05),
 46        RealParameter("stdev", 0.001, 0.005),
 47        RealParameter("delta", 0.93, 0.99),
 48    ]
 49
 50    # set levers
 51    lake_model.levers = [
 52        RealParameter("c1", -2, 2),
 53        RealParameter("c2", -2, 2),
 54        RealParameter("r1", 0.00000001, 2),
 55        RealParameter("r2", 0.00000001, 2),
 56        RealParameter("w1", 0, 1),
 57    ]
 58    # specify outcomes
 59    lake_model.outcomes = [
 60        ScalarOutcome("max_p", kind=ScalarOutcome.MINIMIZE),
 61        ScalarOutcome("utility", kind=ScalarOutcome.MAXIMIZE),
 62        ScalarOutcome("inertia", kind=ScalarOutcome.MAXIMIZE),
 63        ScalarOutcome("reliability", kind=ScalarOutcome.MAXIMIZE),
 64    ]
 65
 66    # override some of the defaults of the model
 67    lake_model.constants = [
 68        Constant("alpha", 0.41),
 69        Constant("n_samples", 100),
 70        Constant("myears", 100),
 71    ]
 72
 73    # reference is optional, but can be used to implement search for
 74    # various user specified scenarios along the lines suggested by
 75    # Watson and Kasprzyk (2017)
 76    reference = Sample("reference", b=0.4, q=2, mean=0.02, stdev=0.01)
 77
 78    population = LHSSampler().generate_samples(lake_model.levers, 20)
 79
 80    random.seed(42)
 81    seeds = [random.randint(0, 1000) for _ in range(5)]
 82
 83    with MultiprocessingEvaluator(lake_model) as evaluator:
 84        all_results = evaluator.optimize(
 85            searchover="levers",
 86            algorithm=GenerationalBorg,
 87            nfe=150000,
 88            convergence_freq=5000,
 89            epsilons=[0.05] * len(lake_model.outcomes),
 90            reference=reference,
 91            filename="lake_model_dps_archive.tar.gz",
 92            directory="./data/convergences",
 93            rng=seeds,
 94            initial_population=population,
 95        )
 96
 97    for (result, convergence_info), seed in zip(all_results, seeds):
 98        result.to_csv(f"./data/convergences/{seed}_final_archive.csv")
 99        convergence_info.to_csv(
100            f"./data/convergences/{seed}_runtime_convergence_info.csv"
101        )
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/optimization_lake_model_dps.html
