---
title: "sd_prim_bryant_and_lempert.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/sd_prim_bryant_and_lempert.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# sd\_prim\_bryant\_and\_lempert.py

```
 1"""Replication of scenario discovery results from Bryant et al. 2010."""
 2
 3# Created on 12 Nov 2018
 4#
 5# @author: jhkwakkel
 6
 7import matplotlib.pyplot as plt
 8import pandas as pd
 9
10from ema_workbench.analysis import prim
11from ema_workbench.util import ema_logging
12
13ema_logging.log_to_stderr(ema_logging.INFO)
14
15data = pd.read_csv("./data/bryant et al 2010 data.csv", index_col=False)
16x = data.iloc[:, 2:11]
17y = data.iloc[:, 15].values
18
19prim_alg = prim.Prim(x, y, peel_alpha=0.1)
20box1 = prim_alg.find_box()
21
22box1.show_tradeoff()
23print(box1.resample(21))
24box1.inspect(21)
25box1.inspect(21, style="graph")
26box1.show_pairs_scatter(21)
27
28plt.show()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/sd_prim_bryant_and_lempert.html
