---
title: "feature_scoring_flu.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/feature_scoring_flu.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# feature\_scoring\_flu.py

```
 1"""Basic feature scoring example."""
 2
 3import matplotlib.pyplot as plt
 4import numpy as np
 5import seaborn as sns
 6
 7from ema_workbench import ema_logging, load_results
 8from ema_workbench.analysis import feature_scoring
 9
10ema_logging.log_to_stderr(level=ema_logging.INFO)
11
12# load data
13fn = r"./data/1000 flu cases with policies.tar.gz"
14x, outcomes = load_results(fn)
15
16# we have timeseries so we need scalars
17y = {
18    "deceased population": outcomes["deceased_population_region_1"][:, -1],
19    "max. infected fraction": np.max(outcomes["infected_fraction_R1"], axis=1),
20}
21
22scores = feature_scoring.get_feature_scores_all(x, y)
23sns.heatmap(scores, annot=True, cmap="viridis")
24plt.show()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/feature_scoring_flu.html
