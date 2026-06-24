---
title: "example_python.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/example_python.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# example\_python.py

```
 1"""An illustrationo of how to use the workbench with models in python."""
 2
 3from ema_workbench import (
 4    Model,
 5    RealParameter,
 6    ScalarOutcome,
 7    ema_logging,
 8    perform_experiments,
 9)
10
11# Created on 20 dec. 2010
12#
13# .. codeauthor:: jhkwakkel <j.h.kwakkel (at) tudelft (dot) nl>
14
15
16def some_model(x1=None, x2=None, x3=None):
17    """Some model."""
18    return {"y": x1 * x2 + x3}
19
20
21if __name__ == "__main__":
22    ema_logging.LOG_FORMAT = "[%(name)s/%(levelname)s/%(processName)s] %(message)s"
23    ema_logging.log_to_stderr(ema_logging.INFO)
24
25    model = Model("simpleModel", function=some_model)  # instantiate the model
26
27    # specify uncertainties
28    model.uncertainties = [
29        RealParameter("x1", 0.1, 10),
30        RealParameter("x2", -0.01, 0.01),
31        RealParameter("x3", -0.01, 0.01),
32    ]
33    # specify outcomes
34    model.outcomes = [ScalarOutcome("y")]
35
36    results = perform_experiments(model, 100)
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/example_python.html
