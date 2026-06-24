---
title: "sd_prim_wcm.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/sd_prim_wcm.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# sd\_prim\_wcm.py

```
 1"""Example demonstrates the use of PRIM for port of Rotterdam.
 2
 3The dataset was generated using the world container model
 4
 5(Tavasszy et al 2011; https://dx.doi.org/10.1016/j.jtrangeo.2011.05.005)
 6
 7
 8"""
 9
10import matplotlib.pyplot as plt
11
12from ema_workbench import ema_logging, load_results
13from ema_workbench.analysis import prim
14
15# Created on Feb 13, 2014
16
17
18ema_logging.log_to_stderr(ema_logging.INFO)
19
20default_flow = 2.178849944502783e7
21
22
23fn = r"./data/5000 runs WCM.tar.gz"
24x, outcomes = load_results(fn)
25y = (outcomes["throughput_Rotterdam"] / default_flow) < 1
26
27prim_obj = prim.Prim(x, y)
28
29# let's find a first box
30box1 = prim_obj.find_box()
31
32# let's analyze the peeling trajectory
33box1.show_ppt()
34box1.show_tradeoff()
35box1.inspect_tradeoff()
36
37box1.write_ppt_to_stdout()
38
39# based on the peeling trajectory, we pick entry number 44
40box1.select(44)
41
42# show the resulting box
43prim_obj.show_boxes()
44prim_obj.boxes_to_dataframe()
45
46plt.show()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/sd_prim_wcm.html
