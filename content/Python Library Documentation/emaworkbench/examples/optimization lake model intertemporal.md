---
title: "optimization_lake_model_intertemporal.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/optimization_lake_model_intertemporal.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# optimization\_lake\_model\_intertemporal.py

```
 1"""An example of the lake problem using the ema workbench.
 2
 3The model itself is adapted from the Rhodium example by Dave Hadka,
 4see https://gist.github.com/dhadka/a8d7095c98130d8f73bc
 5
 6"""
 7
 8from lake_models import lake_problem_intertemporal
 9
10from ema_workbench import (
11    Constraint,
12    Model,
13    MultiprocessingEvaluator,
14    RealParameter,
15    ScalarOutcome,
16    ema_logging,
17)
18
19if __name__ == "__main__":
20    ema_logging.log_to_stderr(ema_logging.INFO)
21
22    # instantiate the model
23    lake_model = Model("lakeproblem", function=lake_problem_intertemporal)
24    lake_model.time_horizon = 100  # used to specify the number of timesteps
25
26    # specify uncertainties
27    lake_model.uncertainties = [
28        RealParameter("mean", 0.01, 0.05),
29        RealParameter("stdev", 0.001, 0.005),
30        RealParameter("b", 0.1, 0.45),
31        RealParameter("q", 2.0, 4.5),
32        RealParameter("delta", 0.93, 0.99),
33    ]
34
35    # set levers, one for each time step
36    lake_model.levers = [
37        RealParameter("decisions", 0, 0.1, shape=(100,))
38    ]
39
40    # specify outcomes
41    lake_model.outcomes = [
42        ScalarOutcome("max_p", kind=ScalarOutcome.MINIMIZE),
43        ScalarOutcome("utility", kind=ScalarOutcome.MAXIMIZE),
44        ScalarOutcome("inertia", kind=ScalarOutcome.MAXIMIZE),
45        ScalarOutcome("reliability", kind=ScalarOutcome.MAXIMIZE),
46    ]
47
48    constraints = [
49        Constraint(
50            "max_pollution", outcome_names="max_p", function=lambda x: max(0, x - 5)
51        )
52    ]
53
54    with MultiprocessingEvaluator(lake_model) as evaluator:
55        results, convergence_info = evaluator.optimize(
56            nfe=5000,
57            searchover="levers",
58            epsilons=[0.125, 0.05, 0.01, 0.01],
59            constraints=constraints,
60            rng=42,
61            filename="lake_model_intertemporal_archive.tar.gz",
62            directory="./data",
63        )
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/optimization_lake_model_intertemporal.html
