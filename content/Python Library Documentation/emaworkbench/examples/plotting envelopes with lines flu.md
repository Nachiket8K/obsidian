---
title: "plotting_envelopes_with_lines_flu.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/plotting_envelopes_with_lines_flu.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# plotting\_envelopes\_with\_lines\_flu.py

```
 1"""Basic example of envelope with lines plot based on Flu model."""
 2
 3# Created on Jul 8, 2014
 4#
 5# @author: jhkwakkel@tudelft.net
 6
 7import matplotlib.pyplot as plt
 8import numpy as np
 9
10from ema_workbench import ema_logging, load_results
11from ema_workbench.analysis import Density, lines
12
13ema_logging.log_to_stderr(ema_logging.INFO)
14
15file_name = r"./data/1000 flu cases with policies.tar.gz"
16experiments, outcomes = load_results(file_name)
17
18# let's specify a few scenarios that we want to show for
19# each of the policies
20scenario_ids = np.arange(0, 1000, 100)
21experiments_to_show = experiments["scenario_id"].isin(scenario_ids)
22
23# the plotting functions return the figure and a dict of axes
24fig, axes = lines(
25    experiments,
26    outcomes,
27    group_by="policy",
28    density=Density.KDE,
29    show_envelope=True,
30    experiments_to_show=experiments_to_show,
31)
32
33# we can access each of the axes and make changes
34for key, value in axes.items():
35    # the key is the name of the outcome for the normal plot
36    # and the name plus '_density' for the endstate distribution
37    if key.endswith("_density"):
38        value.set_xscale("log")
39
40plt.show()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/plotting_envelopes_with_lines_flu.html
