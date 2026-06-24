---
title: "timeseries_clustering_flu.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/timeseries_clustering_flu.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# timeseries\_clustering\_flu.py

```
 1"""Example of time series clustering."""
 2
 3# Created on 11 Apr 2019
 4#
 5# @author: jhkwakkel
 6
 7import matplotlib.pyplot as plt
 8import seaborn as sns
 9
10from ema_workbench import load_results
11from ema_workbench.analysis import Density, clusterer, plotting
12
13experiments, outcomes = load_results("./data/1000 flu cases no policy.tar.gz")
14data = outcomes["infected_fraction_R1"]
15
16# calculate distances
17distances = clusterer.calculate_cid(data)
18
19# plot dedrog
20clusterer.plot_dendrogram(distances)
21
22# do agglomerative clustering on the distances
23clusters = clusterer.apply_agglomerative_clustering(distances, n_clusters=5)
24
25# show the clusters in the output space
26x = experiments.copy()
27x["clusters"] = clusters.astype("object")
28plotting.lines(x, outcomes, group_by="clusters", density=Density.BOXPLOT)
29
30# show the input space
31sns.pairplot(
32    x,
33    hue="clusters",
34    vars=[
35        "infection ratio region 1",
36        "root contact rate region 1",
37        "normal contact rate region 1",
38        "recovery time region 1",
39        "permanent immune population fraction R1",
40    ],
41    plot_kws={"s": 7},
42)
43plt.show()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/timeseries_clustering_flu.html
