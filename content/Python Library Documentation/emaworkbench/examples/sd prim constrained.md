---
title: "sd_prim_constrained.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/sd_prim_constrained.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# sd\_prim\_constrained.py

```
 1"""A short example on how to use the constrained prim function.
 2
 3For more details, see Kwakkel (2019) A generalized many objective optimization
 4approach for scenario discovery, doi: https://doi.org/10.1002/ffo2.8
 5
 6"""
 7
 8import matplotlib.pyplot as plt
 9import pandas as pd
10
11from ema_workbench.analysis import prim
12from ema_workbench.util import ema_logging
13
14ema_logging.log_to_stderr(ema_logging.INFO)
15
16data = pd.read_csv("./data/bryant et al 2010 data.csv", index_col=False)
17x = data.iloc[:, 2:11]
18y = data.iloc[:, 15].values
19
20box = prim.run_constrained_prim(x, y, peel_alpha=0.1)
21
22box.show_tradeoff()
23box.inspect(35)
24box.inspect(35, style="graph")
25
26plt.show()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/sd_prim_constrained.html
