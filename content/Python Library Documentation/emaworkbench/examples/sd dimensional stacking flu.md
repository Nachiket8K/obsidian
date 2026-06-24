---
title: "sd_dimensional_stacking_flu.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/sd_dimensional_stacking_flu.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# sd\_dimensional\_stacking\_flu.py

```
 1"""Dimensional stacking for scenario discovery."""
 2
 3import matplotlib.pyplot as plt
 4
 5from ema_workbench import ema_logging, load_results
 6from ema_workbench.analysis import dimensional_stacking
 7
 8ema_logging.log_to_stderr(level=ema_logging.INFO)
 9
10# load data
11fn = "./data/1000 flu cases no policy.tar.gz"
12x, outcomes = load_results(fn)
13
14y = outcomes["deceased_population_region_1"][:, -1] > 1000000
15
16fig = dimensional_stacking.create_pivot_plot(x, y, 2, bin_labels=True)
17
18plt.show()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/sd_dimensional_stacking_flu.html
