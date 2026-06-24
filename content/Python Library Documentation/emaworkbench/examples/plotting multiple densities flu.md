---
title: "plotting_multiple_densities_flu.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/plotting_multiple_densities_flu.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# plotting\_multiple\_densities\_flu.py

```
 1"""Basic example of multiple densities plot based on Flu model."""
 2
 3# Created on Jul 8, 2014
 4#
 5# @author: jhkwakkel@tudelft.net
 6
 7
 8import math
 9
10import matplotlib.pyplot as plt
11
12from ema_workbench import ema_logging, load_results
13from ema_workbench.analysis import Density, multiple_densities
14
15ema_logging.log_to_stderr(ema_logging.INFO)
16
17file_name = "./data/1000 flu cases with policies.tar.gz"
18experiments, outcomes = load_results(file_name)
19
20# pick points in time for which we want to see a
21# density subplot
22time = outcomes["TIME"][0, :]
23times = time[1 :: math.ceil(time.shape[0] / 6)].tolist()
24
25multiple_densities(
26    experiments,
27    outcomes,
28    log=True,
29    points_in_time=times,
30    group_by="policy",
31    density=Density.KDE,
32    fill=True,
33)
34
35plt.show()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/plotting_multiple_densities_flu.html
