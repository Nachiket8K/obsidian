---
title: "example_lake_model.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/example_lake_model.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# example\_lake\_model.py

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
11    Constant,
12    Model,
13    MultiprocessingEvaluator,
14    RealParameter,
15    ScalarOutcome,
16    ema_logging,
17)
18from ema_workbench.em_framework.evaluators import Samplers
19
20if __name__ == "__main__":
21    ema_logging.log_to_stderr(ema_logging.INFO)
22
23    # instantiate the model
24    lake_model = Model("lake_problem", function=lake_problem_intertemporal)
25    lake_model.time_horizon = 100
26
27    # specify uncertainties
28    lake_model.uncertainties = [
29        RealParameter("b", 0.1, 0.45),
30        RealParameter("q", 2.0, 4.5),
31        RealParameter("mean", 0.01, 0.05),
32        RealParameter("stdev", 0.001, 0.005),
33        RealParameter("delta", 0.93, 0.99),
34    ]
35
36    # set levers, one for each time step
37    lake_model.levers = [
38        RealParameter("decisions", 0, 0.1, shape=(100,)),
39    ]
40
41    # specify outcomes
42    lake_model.outcomes = [
43        ScalarOutcome("max_p"),
44        ScalarOutcome("utility"),
45        ScalarOutcome("inertia"),
46        ScalarOutcome("reliability"),
47    ]
48
49    # override some of the defaults of the model
50    lake_model.constants = [Constant("alpha", 0.41), Constant("n_samples", 150)]
51
52    # generate some random policies by sampling over levers
53    n_scenarios = 100
54    n_policies = 4
55
56    with MultiprocessingEvaluator(lake_model) as evaluator:
57        res = evaluator.perform_experiments(
58            n_scenarios,
59            n_policies,
60            lever_sampling=Samplers.MC,
61            lever_sampling_kwargs={"rng": 42},
62            uncertainty_sampling_kwargs={"rng": 42},
63        )
64
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/example_lake_model.html
