---
title: "example_vensim_advanced_flu.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/example_vensim_advanced_flu.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# example\_vensim\_advanced\_flu.py

```
 1"""A more advanced illustration of using the workbench with vensim.
 2
 3The underlying case is the same as used in example_flu.py
 4
 5"""
 6
 7import numpy as np
 8
 9from ema_workbench import (
10    MultiprocessingEvaluator,
11    Sample,
12    ScalarOutcome,
13    TimeSeriesOutcome,
14    ema_logging,
15    save_results,
16)
17from ema_workbench.connectors.vensim import VensimModel
18from ema_workbench.em_framework.parameters import parameters_from_csv
19
20# Created on 20 May, 2011
21#
22# .. codeauthor:: jhkwakkel <j.h.kwakkel (at) tudelft (dot) nl>
23#                 epruyt <e.pruyt (at) tudelft (dot) nl>
24
25
26def time_of_max(infected_fraction, time):
27    """Returns the time of the maximum infected fraction."""
28    index = np.where(infected_fraction == np.max(infected_fraction))
29    timing = time[index][0]
30    return timing
31
32
33if __name__ == "__main__":
34    ema_logging.log_to_stderr(ema_logging.INFO)
35
36    model = VensimModel("flu", wd="./models/flu", model_file="FLUvensimV1basecase.vpm")
37
38    # outcomes
39    model.outcomes = [
40        TimeSeriesOutcome(
41            "deceased_population_region_1", variable_name="deceased population region 1"
42        ),
43        TimeSeriesOutcome("infected_fraction_R1", variable_name="infected fraction R1"),
44        ScalarOutcome(
45            "max_infection_fraction",
46            variable_name="infected fraction R1",
47            function=np.max,
48        ),
49        ScalarOutcome(
50            "time_of_max",
51            variable_name=["infected fraction R1", "TIME"],
52            function=time_of_max,
53        ),
54    ]
55
56    # create uncertainties based on csv
57    # FIXME csv is missing
58    model.uncertainties = parameters_from_csv("./models/flu/flu_uncertainties.csv")
59
60    # add policies
61    policies = [
62        Sample("no policy", model_file="FLUvensimV1basecase.vpm"),
63        Sample("static policy", model_file="FLUvensimV1static.vpm"),
64        Sample("adaptive policy", model_file="FLUvensimV1dynamic.vpm"),
65    ]
66
67    with MultiprocessingEvaluator(model, n_processes=-1) as evaluator:
68        results = evaluator.perform_experiments(1000, policies=policies)
69
70    save_results(results, "./data/1000 flu cases with policies.tar.gz")
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/example_vensim_advanced_flu.html
