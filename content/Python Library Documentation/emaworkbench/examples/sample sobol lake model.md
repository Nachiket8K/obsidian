---
title: "sample_sobol_lake_model.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/sample_sobol_lake_model.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# sample\_sobol\_lake\_model.py

```
 1"""An example of the lake problem using the ema workbench.
 2
 3The model itself is adapted from the Rhodium example by Dave Hadka,
 4see https://gist.github.com/dhadka/a8d7095c98130d8f73bc
 5
 6"""
 7
 8import pandas as pd
 9from lake_models import lake_problem_intertemporal
10from SALib.analyze import sobol
11
12from ema_workbench import (
13    Constant,
14    Model,
15    MultiprocessingEvaluator,
16    RealParameter,
17    Sample,
18    ScalarOutcome,
19    ema_logging,
20)
21from ema_workbench.em_framework import get_SALib_problem
22from ema_workbench.em_framework.evaluators import Samplers
23
24
25def analyze(results, ooi):
26    """Analyze results using SALib sobol, returns a dataframe."""
27    _, outcomes = results
28
29    problem = get_SALib_problem(lake_model.uncertainties)
30    y = outcomes[ooi]
31    sobol_indices = sobol.analyze(problem, y)
32    sobol_stats = {
33        key: sobol_indices[key] for key in ["ST", "ST_conf", "S1", "S1_conf"]
34    }
35    sobol_stats = pd.DataFrame(sobol_stats, index=problem["names"])
36    sobol_stats.sort_values(by="ST", ascending=False)
37    s2 = pd.DataFrame(
38        sobol_indices["S2"], index=problem["names"], columns=problem["names"]
39    )
40    s2_conf = pd.DataFrame(
41        sobol_indices["S2_conf"], index=problem["names"], columns=problem["names"]
42    )
43
44    return sobol_stats, s2, s2_conf
45
46
47if __name__ == "__main__":
48    ema_logging.log_to_stderr(ema_logging.INFO)
49
50    # instantiate the model
51    lake_model = Model("lakeproblem", function=lake_problem_intertemporal)
52    lake_model.time_horizon = 100
53
54    # specify uncertainties
55    lake_model.uncertainties = [
56        RealParameter("b", 0.1, 0.45),
57        RealParameter("q", 2.0, 4.5),
58        RealParameter("mean", 0.01, 0.05),
59        RealParameter("stdev", 0.001, 0.005),
60        RealParameter("delta", 0.93, 0.99),
61    ]
62
63    # set levers, one for each time step
64    lake_model.levers = [
65        RealParameter(f"l{i}", 0, 0.1) for i in range(lake_model.time_horizon)
66    ]
67
68    # specify outcomes
69    lake_model.outcomes = [
70        ScalarOutcome("max_p"),
71        ScalarOutcome("utility"),
72        ScalarOutcome("inertia"),
73        ScalarOutcome("reliability"),
74    ]
75
76    # override some of the defaults of the model
77    lake_model.constants = [Constant("alpha", 0.41), Constant("n_samples", 150)]
78
79    # generate sa single default no release policy
80    policy = Sample("no release", **{f"l{i}": 0.1 for i in range(100)})
81
82    n_scenarios = 1000
83
84    with MultiprocessingEvaluator(lake_model, n_processes=4) as evaluator:
85        results = evaluator.perform_experiments(
86            n_scenarios,
87            policy,
88            uncertainty_sampling=Samplers.SOBOL,
89            uncertainty_sampling_kwargs={"calc_second_order": True},
90        )
91
92    sobol_stats, s2, s2_conf = analyze(results, "max_p")
93    print(sobol_stats)
94    print(s2)
95    print(s2_conf)
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/sample_sobol_lake_model.html
