---
title: "sample_jointly_lake_model.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/sample_jointly_lake_model.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# sample\_jointly\_lake\_model.py

```
  1"""An example of the lake problem using the ema workbench.
  2
  3This example illustrated how you can control more finely how samples are being
  4generated. In this particular case, we want to apply Sobol analysis over both the
  5uncertainties and levers at the same time.
  6
  7"""
  8
  9import pandas as pd
 10from lake_models import lake_problem_dps
 11from SALib.analyze import sobol
 12
 13from ema_workbench import (
 14    Constant,
 15    Model,
 16    MultiprocessingEvaluator,
 17    RealParameter,
 18    ScalarOutcome,
 19    ema_logging,
 20)
 21from ema_workbench.em_framework import (
 22    SobolSampler,
 23    get_SALib_problem,
 24)
 25
 26
 27def analyze(results, ooi):
 28    """Analyze results using SALib sobol, returns a dataframe."""
 29    _, outcomes = results
 30
 31    parameters = lake_model.uncertainties.copy() + lake_model.levers.copy()
 32
 33    problem = get_SALib_problem(parameters)
 34    y = outcomes[ooi]
 35    sobol_indices = sobol.analyze(problem, y)
 36    sobol_stats = {
 37        key: sobol_indices[key] for key in ["ST", "ST_conf", "S1", "S1_conf"]
 38    }
 39    sobol_stats = pd.DataFrame(sobol_stats, index=problem["names"])
 40    sobol_stats.sort_values(by="ST", ascending=False)
 41    s2 = pd.DataFrame(
 42        sobol_indices["S2"], index=problem["names"], columns=problem["names"]
 43    )
 44    s2_conf = pd.DataFrame(
 45        sobol_indices["S2_conf"], index=problem["names"], columns=problem["names"]
 46    )
 47
 48    return sobol_stats, s2, s2_conf
 49
 50
 51if __name__ == "__main__":
 52    ema_logging.log_to_stderr(ema_logging.INFO)
 53
 54    # instantiate the model
 55    lake_model = Model("lakeproblem", function=lake_problem_dps)
 56    # specify uncertainties
 57    lake_model.uncertainties = [
 58        RealParameter("b", 0.1, 0.45),
 59        RealParameter("q", 2.0, 4.5),
 60        RealParameter("mean", 0.01, 0.05),
 61        RealParameter("stdev", 0.001, 0.005),
 62        RealParameter("delta", 0.93, 0.99),
 63    ]
 64
 65    # set levers
 66    lake_model.levers = [
 67        RealParameter("c1", -2, 2),
 68        RealParameter("c2", -2, 2),
 69        RealParameter("r1", 0, 2),
 70        RealParameter("r2", 0, 2),
 71        RealParameter("w1", 0, 1),
 72    ]
 73    # specify outcomes
 74    lake_model.outcomes = [
 75        ScalarOutcome("max_P", kind=ScalarOutcome.MINIMIZE),
 76        # @UndefinedVariable
 77        ScalarOutcome("utility", kind=ScalarOutcome.MAXIMIZE),
 78        # @UndefinedVariable
 79        ScalarOutcome("inertia", kind=ScalarOutcome.MAXIMIZE),
 80        # @UndefinedVariable
 81        ScalarOutcome("reliability", kind=ScalarOutcome.MAXIMIZE),
 82    ]  # @UndefinedVariable
 83
 84    # override some of the defaults of the model
 85    lake_model.constants = [
 86        Constant("alpha", 0.41),
 87        Constant("n_samples", 100),
 88        Constant("myears", 100),
 89    ]
 90
 91    # combine parameters and uncertainties prior to sampling
 92    n_scenarios = 1024
 93    parameters = lake_model.uncertainties + lake_model.levers
 94    scenarios = SobolSampler().generate_samples(
 95        parameters, n_scenarios, 42, calc_second_order=True
 96    )
 97
 98    with MultiprocessingEvaluator(lake_model) as evaluator:
 99        results = evaluator.perform_experiments(scenarios)
100
101    sobol_stats, s2, s2_conf = analyze(results, "max_P")
102    print(sobol_stats)
103    print(s2)
104    print(s2_conf)
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/sample_jointly_lake_model.html
