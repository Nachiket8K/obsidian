---
title: "sd_logit_flu_example.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/sd_logit_flu_example.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# sd\_logit\_flu\_example.py

```
 1"""Example of using logit regression with the workbench."""
 2
 3import matplotlib.pyplot as plt
 4import seaborn as sns
 5
 6import ema_workbench.analysis.logistic_regression as logistic_regression
 7from ema_workbench import load_results
 8
 9# Created on 14 Mar 2019
10#
11# .. codeauthor:: jhkwakkel <j.h.kwakkel (at) tudelft (dot) nl>
12
13
14experiments, outcomes = load_results("./data/1000 flu cases no policy.tar.gz")
15
16x = experiments.drop(["model", "policy", "scenario"], axis=1)
17y = outcomes["deceased_population_region_1"][:, -1] > 1000000
18
19logit = logistic_regression.Logit(x, y)
20logit.run()
21
22logit.show_tradeoff()
23
24# when we change the default threshold, the tradeoff curve is
25# recalculated
26logit.threshold = 0.8
27logit.show_tradeoff()
28
29# we can also look at the tradeoff across threshold values
30# for a given model
31logit.show_threshold_tradeoff(3)
32
33# inspect shows the threshold tradeoff for the model
34# as well as the statistics of the model
35logit.inspect(3)
36
37# we can also visualize the performance of the model
38# using a pairwise scatter plot
39sns.set_style("white")
40logit.plot_pairwise_scatter(3)
41
42plt.show()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/sd_logit_flu_example.html
