---
title: "plotting_kdeovertime_flu.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/plotting_kdeovertime_flu.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# plotting\_kdeovertime\_flu.py

```
 1"""Basic example of kde over time plot based on Flu model."""
 2
 3# Created on Jul 8, 2014
 4#
 5# @author: jhkwakkel@tudelft.net
 6
 7import matplotlib.pyplot as plt
 8
 9from ema_workbench import ema_logging, load_results
10from ema_workbench.analysis.plotting import kde_over_time
11
12ema_logging.log_to_stderr(ema_logging.INFO)
13
14# file_name = r'./data/1000 runs scarcity.tar.gz'
15file_name = "./data/1000 flu cases no policy.tar.gz"
16experiments, outcomes = load_results(file_name)
17
18# the plotting functions return the figure and a dict of axes
19fig, axes = kde_over_time(experiments, outcomes, log=True)
20
21plt.show()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/plotting_kdeovertime_flu.html
