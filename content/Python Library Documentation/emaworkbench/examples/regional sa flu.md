---
title: "regional_sa_flu.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/regional_sa_flu.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# regional\_sa\_flu.py

```
 1"""A simple example of performing regional sensitivity analysis."""
 2
 3import matplotlib.pyplot as plt
 4
 5from ema_workbench import load_results
 6from ema_workbench.analysis import regional_sa
 7
 8fn = "./data/1000 flu cases with policies.tar.gz"
 9results = load_results(fn)
10x, outcomes = results
11
12y = outcomes["deceased population region 1"][:, -1] > 1000000
13
14fig = regional_sa.plot_cdfs(x, y)
15
16plt.show()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/regional_sa_flu.html
