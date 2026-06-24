---
title: "example_netlogo.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/example_netlogo.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# example\_netlogo.py

```
 1"""Illustration of using netlogo models with the workbench.
 2
 3Note that this example uses the NetLogo 6 version of the predator prey model that
 4comes with NetLogo. This works fine also with NetLogo 7.
 5
 6If you are using NetLogo 5, replace the model file with the one that comes with NetLogo.
 7
 8"""
 9
10import numpy as np
11
12from ema_workbench import (
13    MultiprocessingEvaluator,
14    RealParameter,
15    ScalarOutcome,
16    TimeSeriesOutcome,
17    ema_logging,
18)
19from ema_workbench.connectors.netlogo import NetLogoModel
20
21# Created on 20 mrt. 2013
22#
23# .. codeauthor::  jhkwakkel
24
25
26if __name__ == "__main__":
27    # turn on logging
28    ema_logging.log_to_stderr(ema_logging.INFO)
29
30    model = NetLogoModel(
31        "predprey",
32        wd="./models/predatorPreyNetlogo",
33        model_file="Wolf Sheep Predation.nlogo",
34    )
35    model.run_length = 100
36    model.replications = 10
37
38    model.uncertainties = [
39        RealParameter("grass-regrowth-time", 1, 99),
40        RealParameter("initial-number-sheep", 50, 100),
41        RealParameter("initial-number-wolves", 50, 100),
42        RealParameter("sheep-reproduce", 5, 10),
43        RealParameter("wolf-reproduce", 5, 10),
44    ]
45
46    model.outcomes = [
47        ScalarOutcome("sheep", variable_name="count sheep", function=np.mean),
48        TimeSeriesOutcome("wolves"),
49        TimeSeriesOutcome("grass"),
50    ]
51
52    # perform experiments
53    n = 10
54
55    with MultiprocessingEvaluator(
56        model, n_processes=-1, maxtasksperchild=4
57    ) as evaluator:
58        results = evaluator.perform_experiments(n)
59
60    print()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/example_netlogo.html
