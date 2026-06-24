---
title: "sd_prim_pca_flu.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/sd_prim_pca_flu.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# sd\_prim\_pca\_flu.py

```
 1"""An example of doing PRIM with PCA preprocessing.
 2
 3The data was generated using a system dynamics models implemented in Vensim.
 4See flu_example.py for the code.
 5
 6"""
 7
 8import matplotlib.pyplot as plt
 9
10import ema_workbench.analysis.prim as prim
11from ema_workbench import ema_logging, load_results
12
13#
14# .. codeauthor:: jhkwakkel <j.h.kwakkel (at) tudelft (dot) nl>
15
16ema_logging.log_to_stderr(level=ema_logging.INFO)
17
18# load data
19fn = r"./data/1000 flu cases no policy.tar.gz"
20x, outcomes = load_results(fn)
21
22# specify y
23y = outcomes["deceased_population_region_1"][:, -1] > 1000000
24
25rotated_experiments, rotation_matrix = prim.pca_preprocess(
26    x, y, exclude=["model", "policy", "scenario"]
27)
28
29# perform prim on modified results tuple
30prim_obj = prim.Prim(rotated_experiments, y)
31box = prim_obj.find_box()
32
33box.show_tradeoff()
34box.inspect(22)
35plt.show()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/sd_prim_pca_flu.html
