---
title: "feature_scoring_flu_confidence.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/feature_scoring_flu_confidence.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# feature\_scoring\_flu\_confidence.py

```
 1"""Feature scoring with confidence intervals."""
 2
 3import matplotlib.pyplot as plt
 4import numpy as np
 5import pandas as pd
 6import seaborn as sns
 7
 8from ema_workbench import ema_logging, load_results
 9from ema_workbench.analysis.feature_scoring import (
10    RuleInductionType,
11    get_ex_feature_scores,
12)
13
14ema_logging.log_to_stderr(level=ema_logging.INFO)
15
16# load data
17fn = r"./data/1000 flu cases no policy.tar.gz"
18x, outcomes = load_results(fn)
19
20x = x.drop(["model", "policy"], axis=1)
21y = np.max(outcomes["infected_fraction_R1"], axis=1)
22
23all_scores = []
24for _ in range(100):
25    indices = np.random.choice(np.arange(0, x.shape[0]), size=x.shape[0])
26    selected_x = x.iloc[indices, :]
27    selected_y = y[indices]
28
29    scores = get_ex_feature_scores(
30        selected_x, selected_y, mode=RuleInductionType.REGRESSION
31    )[0]
32    all_scores.append(scores)
33all_scores = pd.concat(all_scores, axis=1, sort=False)
34
35sns.boxplot(data=all_scores.T)
36plt.show()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/feature_scoring_flu_confidence.html
