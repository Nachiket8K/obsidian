---
title: "sd_prim_flu.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/sd_prim_flu.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# sd\_prim\_flu.py

```
 1"""A basic example of using PRIM for scenario discovery.
 2
 3The data was generated using a system dynamics models implemented in Vensim.
 4See flu_example.py for the code.
 5
 6"""
 7
 8# .. codeauthor:: jhkwakkel <j.h.kwakkel (at) tudelft (dot) nl>
 9#                 chamarat <c.hamarat  (at) tudelft (dot) nl>
10
11import matplotlib.pyplot as plt
12
13import ema_workbench.analysis.prim as prim
14from ema_workbench import ema_logging, load_results
15
16ema_logging.log_to_stderr(level=ema_logging.INFO)
17
18
19# load data
20fn = "./data/1000 flu cases no policy.tar.gz"
21x, outcomes = load_results(fn)
22y = outcomes["deceased_population_region_1"][:, -1] > 1000000
23
24# perform prim on modified results tuple
25prim_obj = prim.Prim(x, y)
26
27box_1 = prim_obj.find_box()
28box_1.show_ppt()
29box_1.show_tradeoff()
30# box_1.inspect([5, 6], style="graph", boxlim_formatter="{: .2f}")
31
32fig, axes = plt.subplots(nrows=2, ncols=1)
33
34box_1.inspect([5, 6], style="graph", boxlim_formatter="{: .2f}", ax=axes)
35plt.show()
36
37box_1.inspect(5)
38box_1.select(5)
39box_1.write_ppt_to_stdout()
40box_1.show_pairs_scatter(5)
41
42# print prim to std_out
43print(prim_obj.stats_to_dataframe())
44print(prim_obj.boxes_to_dataframe())
45
46# visualize
47prim_obj.show_boxes()
48plt.show()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/sd_prim_flu.html
