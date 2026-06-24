---
title: "plotting_pairsplot_flu.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/plotting_pairsplot_flu.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# plotting\_pairsplot\_flu.py

```
 1"""Basic example pairplot.."""
 2
 3# Created on 20 sep. 2011
 4#
 5# .. codeauthor:: jhkwakkel <j.h.kwakkel (at) tudelft (dot) nl>
 6
 7import matplotlib.pyplot as plt
 8import numpy as np
 9
10from ema_workbench import ema_logging, load_results
11from ema_workbench.analysis.pairs_plotting import (
12    pairs_density,
13    pairs_lines,
14    pairs_scatter,
15)
16
17ema_logging.log_to_stderr(level=ema_logging.DEFAULT_LEVEL)
18
19# load the data
20fh = "./data/1000 flu cases no policy.tar.gz"
21experiments, outcomes = load_results(fh)
22
23# transform the results to the required format
24# that is, we want to know the max peak and the casualties at the end of the
25# run
26tr = {}
27
28# get time and remove it from the dict
29time = outcomes.pop("TIME")
30
31for key, value in outcomes.items():
32    if key == "deceased_population_region_1":
33        tr[key] = value[:, -1]  # we want the end value
34    else:
35        # we want the maximum value of the peak
36        max_peak = np.max(value, axis=1)
37        tr["max peak"] = max_peak
38
39        # we want the time at which the maximum occurred
40        # the code here is a bit obscure, I don't know why the transpose
41        # of value is needed. This however does produce the appropriate results
42        logical = np.max(value, axis=1) == value.T
43        tr["time of max"] = time[logical.T]
44
45pairs_scatter(experiments, tr, filter_scalar=False)
46pairs_lines(experiments, outcomes)
47pairs_density(experiments, tr, filter_scalar=False)
48plt.show()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/plotting_pairsplot_flu.html
