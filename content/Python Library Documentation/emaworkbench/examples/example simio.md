---
title: "example_simio.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/example_simio.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# example\_simio.py

```
 1"""A demonstrationo of using the workbench with Simio."""
 2
 3from ema_workbench import (
 4    CategoricalParameter,
 5    MultiprocessingEvaluator,
 6    ScalarOutcome,
 7    ema_logging,
 8)
 9from ema_workbench.connectors.simio_connector import SimioModel
10
11# Created on 27 Jun 2019
12#
13# @author: jhkwakkel
14
15if __name__ == "__main__":
16    ema_logging.log_to_stderr(ema_logging.INFO)
17
18    model = SimioModel(
19        "simioDemo",
20        wd="./model_bahareh",
21        model_file="SupplyChainV3.spfx",
22        main_model="Model",
23    )
24
25    model.uncertainties = [
26        CategoricalParameter("DemandDistributionParameter", (20, 30, 40, 50, 60)),
27        CategoricalParameter(
28            "DemandInterarrivalTime", (0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2)
29        ),
30    ]
31
32    model.levers = [
33        CategoricalParameter("InitialInventory", (500, 600, 700, 800, 900)),
34        CategoricalParameter("ReorderPoint", (100, 200, 300, 400, 500)),
35        CategoricalParameter("OrderUpToQuantity", (500, 600, 700, 800, 900)),
36        CategoricalParameter("ReviewPeriod", (3, 4, 5, 6, 7)),
37    ]
38
39    model.outcomes = [
40        ScalarOutcome("AverageInventory"),
41        ScalarOutcome("AverageServiceLevel"),
42    ]
43
44    n_scenarios = 10
45    n_policies = 2
46
47    with MultiprocessingEvaluator(model) as evaluator:
48        results = evaluator.perform_experiments(n_scenarios, n_policies)
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/example_simio.html
