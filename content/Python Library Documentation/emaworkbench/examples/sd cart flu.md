---
title: "sd_cart_flu.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/sd_cart_flu.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# sd\_cart\_flu.py

```
 1"""Scenario discovery using CART."""
 2
 3# Created on May 26, 2015
 4#
 5# @author: jhkwakkel
 6import matplotlib.pyplot as plt
 7
 8import ema_workbench.analysis.cart as cart
 9from ema_workbench import ema_logging, load_results
10
11ema_logging.log_to_stderr(level=ema_logging.INFO)
12
13
14# load data
15fn = "./data/1000 flu cases with policies.tar.gz"
16results = load_results(fn)
17experiments, outcomes = results
18
19# extract results for 1 policy
20logical = experiments["policy"] == "no policy"
21new_experiments = experiments[logical]
22new_outcomes = {}
23for key, value in outcomes.items():
24    new_outcomes[key] = value[logical]
25
26x = new_experiments
27y = new_outcomes["deceased_population_region_1"][:, -1] > 1000000
28
29cart_alg = cart.CART(x, y, mass_min=0.05)
30cart_alg.build_tree()
31
32# print cart to std_out
33print(cart_alg.stats_to_dataframe())
34print(cart_alg.boxes_to_dataframe())
35
36# visualize
37cart_alg.show_boxes(together=False)
38cart_alg.show_tree()
39plt.show()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/sd_cart_flu.html
