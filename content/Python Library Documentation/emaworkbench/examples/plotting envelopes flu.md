---
title: "plotting_envelopes_flu.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/plotting_envelopes_flu.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# plotting\_envelopes\_flu.py

```
 1"""Envelope plot example."""
 2
 3# Created on Jul 8, 2014
 4#
 5# @author: jhkwakkel@tudelft.net
 6
 7import matplotlib.pyplot as plt
 8
 9from ema_workbench import ema_logging, load_results
10from ema_workbench.analysis import Density, envelopes
11
12ema_logging.log_to_stderr(ema_logging.INFO)
13
14file_name = r"./data/1000 flu cases with policies.tar.gz"
15experiments, outcomes = load_results(file_name)
16
17# the plotting functions return the figure and a dict of axes
18fig, axes = envelopes(
19    experiments, outcomes, group_by="policy", density=Density.KDE, fill=True
20)
21
22# we can access each of the axes and make changes
23for key, value in axes.items():
24    # the key is the name of the outcome for the normal plot
25    # and the name plus '_density' for the endstate distribution
26    if key.endswith("_density"):
27        value.set_xscale("log")
28
29plt.show()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/plotting_envelopes_flu.html
