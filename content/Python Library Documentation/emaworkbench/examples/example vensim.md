---
title: "example_vensim.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/example_vensim.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# example\_vensim.py

```
 1"""Basic example of how to connect a Vensim model to the ema_workbench."""
 2
 3# Created on 3 Jan. 2011
 4#
 5# This file illustrated the use the EMA classes for a contrived vensim
 6# example
 7
 8from ema_workbench import (
 9    RealParameter,
10    TimeSeriesOutcome,
11    ema_logging,
12    perform_experiments,
13)
14from ema_workbench.connectors.vensim import VensimModel
15
16if __name__ == "__main__":
17    # turn on logging
18    ema_logging.log_to_stderr(ema_logging.INFO)
19
20    # instantiate a model
21    wd = "./models/vensim example"
22    vensim_model = VensimModel("simple_model", wd=wd, model_file="model.vpm")
23    vensim_model.uncertainties = [
24        RealParameter("x11", 0, 2.5),
25        RealParameter("x12", -2.5, 2.5),
26    ]
27
28    vensim_model.outcomes = [TimeSeriesOutcome("a")]
29
30    results = perform_experiments(vensim_model, 1000)
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/example_vensim.html
