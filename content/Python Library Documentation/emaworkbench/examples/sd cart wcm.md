---
title: "sd_cart_wcm.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/sd_cart_wcm.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# sd\_cart\_wcm.py

```
 1"""Simple CART example."""
 2
 3# Created on May 26, 2015
 4#
 5# @author: jhkwakkel
 6
 7
 8import matplotlib.pyplot as plt
 9
10import ema_workbench.analysis.cart as cart
11from ema_workbench import ema_logging, load_results
12
13ema_logging.log_to_stderr(level=ema_logging.INFO)
14
15default_flow = 2.178849944502783e7
16
17# load data
18fn = "./data/5000 runs WCM.tar.gz"
19results = load_results(fn)
20x, outcomes = results
21
22x = x.drop(["scenario", "model", "policy"], axis=1)
23
24ooi = "throughput_Rotterdam"
25outcome = outcomes[ooi] / default_flow
26y = outcome < 1
27
28cart_alg = cart.CART(x, y)
29cart_alg.build_tree()
30
31# print cart to std_out
32print(cart_alg.stats_to_dataframe())
33print(cart_alg.boxes_to_dataframe())
34
35# visualize
36cart_alg.show_boxes(together=False)
37cart_alg.show_tree()
38plt.show()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/sd_cart_wcm.html
