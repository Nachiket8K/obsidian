---
title: "example_pysd_teacup.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/example_pysd_teacup.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# example\_pysd\_teacup.py

```
 1"""A simple pysd example."""
 2
 3# Created on Jul 23, 2016
 4#
 5# .. codeauthor::jhkwakkel <j.h.kwakkel (at) tudelft (dot) nl>
 6
 7from ema_workbench import (
 8    RealParameter,
 9    TimeSeriesOutcome,
10    ema_logging,
11    perform_experiments,
12)
13from ema_workbench.connectors.pysd_connector import PysdModel
14
15if __name__ == "__main__":
16    ema_logging.log_to_stderr(ema_logging.INFO)
17
18    mdl_file = "./models/pysd/Teacup.mdl"
19
20    model = PysdModel("teacup", mdl_file=mdl_file)
21
22    model.uncertainties = [
23        RealParameter("room_temperature", 33, 120, variable_name="Room Temperature")
24    ]
25    model.outcomes = [
26        TimeSeriesOutcome("teacup_temperature", variable_name="Teacup Temperature")
27    ]
28
29    perform_experiments(model, 100)
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/example_pysd_teacup.html
