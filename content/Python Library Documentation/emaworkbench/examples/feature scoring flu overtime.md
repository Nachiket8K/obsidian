---
title: "feature_scoring_flu_overtime.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/feature_scoring_flu_overtime.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# feature\_scoring\_flu\_overtime.py

```
 1"""Feature scoring over time."""
 2
 3import matplotlib.pyplot as plt
 4import pandas as pd
 5import seaborn as sns
 6
 7from ema_workbench import ema_logging, load_results
 8from ema_workbench.analysis import RuleInductionType, get_ex_feature_scores
 9
10ema_logging.log_to_stderr(level=ema_logging.INFO)
11
12# load data
13fn = r"./data/1000 flu cases no policy.tar.gz"
14
15x, outcomes = load_results(fn)
16x = x.drop(["model", "policy"], axis=1)
17
18y = outcomes["deceased_population_region_1"]
19
20all_scores = []
21
22# we only want to show those uncertainties that are in the top 5
23# most sensitive parameters at any time step
24top_5 = set()
25for i in range(2, y.shape[1], 8):
26    data = y[:, i]
27    scores = get_ex_feature_scores(x, data, mode=RuleInductionType.REGRESSION)[0]
28    # add the top five for this time step to the set of top5s
29    top_5 |= set(scores.nlargest(5, 1).index.values)
30    scores = scores.rename(columns={1: outcomes["TIME"][0, i]})
31    all_scores.append(scores)
32
33all_scores = pd.concat(all_scores, axis=1, sort=False)
34all_scores = all_scores.loc[top_5, :]
35
36fig, ax = plt.subplots()
37sns.heatmap(all_scores, ax=ax, cmap="viridis")
38plt.show()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/feature_scoring_flu_overtime.html
