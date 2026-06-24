---
title: "plotting_lines_flu.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/plotting_lines_flu.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# plotting\_lines\_flu.py

```
 1"""Basic example of lines plot based on Flu model."""
 2
 3# Created on Jul 8, 2014
 4#
 5# @author: jhkwakkel@tudelft.net
 6
 7
 8import matplotlib.pyplot as plt
 9
10from ema_workbench import ema_logging, load_results
11from ema_workbench.analysis import Density, lines
12
13ema_logging.log_to_stderr(ema_logging.INFO)
14
15file_name = r"./data/1000 flu cases no policy.tar.gz"
16experiments, outcomes = load_results(file_name)
17
18# the plotting functions return the figure and a dict of axes
19fig, axes = lines(experiments, outcomes, density=Density.VIOLIN)
20
21# we can access each of the axes and make changes
22for key, value in axes.items():
23    # the key is the name of the outcome for the normal plot
24    # and the name plus '_density' for the endstate distribution
25    if key.endswith("_density"):
26        value.set_xscale("log")
27
28plt.show()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/plotting_lines_flu.html
