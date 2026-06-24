---
title: "outputspace_exploration_lake_model.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/outputspace_exploration_lake_model.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# outputspace\_exploration\_lake\_model.py

```
 1"""An example of using output space exploration on the lake problem.
 2
 3The lake problem itself is adapted from the Rhodium example by Dave Hadka,
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
15    Sample,
16    ScalarOutcome,
17    ema_logging,
18)
19from ema_workbench.em_framework.outputspace_exploration import (
20    OutputSpaceExplorationAlgorithm,
21)
22
23if __name__ == "__main__":
24    ema_logging.log_to_stderr(ema_logging.INFO)
25
26    # instantiate the model
27    lake_model = Model("lakeproblem", function=lake_problem_intertemporal)
28    lake_model.time_horizon = 100
29
30    # specify uncertainties
31    lake_model.uncertainties = [
32        RealParameter("b", 0.1, 0.45),
33        RealParameter("q", 2.0, 4.5),
34        RealParameter("mean", 0.01, 0.05),
35        RealParameter("stdev", 0.001, 0.005),
36        RealParameter("delta", 0.93, 0.99),
37    ]
38
39    # set levers, one for each time step
40    lake_model.levers = [
41        RealParameter(f"l{i}", 0, 0.1) for i in range(lake_model.time_horizon)
42    ]
43
44    # specify outcomes
45    # note that outcomes of kind INFO will be ignored
46    lake_model.outcomes = [
47        ScalarOutcome("max_P", kind=ScalarOutcome.MAXIMIZE),
48        ScalarOutcome("utility", kind=ScalarOutcome.MAXIMIZE),
49        ScalarOutcome("inertia", kind=ScalarOutcome.MAXIMIZE),
50        ScalarOutcome("reliability", kind=ScalarOutcome.MAXIMIZE),
51    ]
52
53    # override some of the defaults of the model
54    lake_model.constants = [Constant("alpha", 0.41), Constant("n_samples", 150)]
55
56    # generate a reference policy
57    reference = Sample(
58        "no_policy", **{l.name: 0.02 for l in lake_model.levers}  # noqa: E741
59    )
60
61    # we are doing output space exploration given a reference
62    # policy, so we are exploring the output space over the uncertainties
63    # grid spec specifies the grid structure imposed on the output space
64    # each tuple is associated with an outcome. It gives the minimum
65    # maximum, and epsilon value.
66    with MultiprocessingEvaluator(lake_model) as evaluator:
67        res, convergence_info = evaluator.optimize(
68            algorithm=OutputSpaceExplorationAlgorithm,
69            grid_spec=[
70                (0, 12, 0.5),
71                (0, 1, 0.05),
72                (0, 1, 0.1),
73                (0, 1, 0.1),
74            ],
75            nfe=1000,
76            searchover="uncertainties",
77            reference=reference,
78            filename="lake_model_output_space_exploration.tar.gz",
79            directory="./data",
80            rng=42,
81        )
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/outputspace_exploration_lake_model.html
