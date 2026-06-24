---
title: "sd_boostedtrees_flu.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/sd_boostedtrees_flu.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# sd\_boostedtrees\_flu.py

```
  1"""Using boosted trees with the workbench."""
  2
  3import matplotlib.pyplot as plt
  4import numpy as np
  5import seaborn as sns
  6from matplotlib.collections import CircleCollection
  7from sklearn.ensemble import AdaBoostClassifier
  8from sklearn.tree import DecisionTreeClassifier
  9
 10from ema_workbench import ema_logging, load_results
 11from ema_workbench.analysis import feature_scoring
 12
 13ema_logging.log_to_stderr(ema_logging.INFO)
 14
 15
 16def plot_factormap(x1, x2, ax, bdt, nominal):
 17    """Helper function for plotting a 2d factor map."""
 18    x_min, x_max = x[:, x1].min(), x[:, x1].max()
 19    y_min, y_max = x[:, x2].min(), x[:, x2].max()
 20    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 500), np.linspace(y_min, y_max, 500))
 21
 22    grid = np.ones((xx.ravel().shape[0], x.shape[1])) * nominal
 23    grid[:, x1] = xx.ravel()
 24    grid[:, x2] = yy.ravel()
 25
 26    Z = bdt.predict(grid)  # noqa N806
 27    Z = Z.reshape(xx.shape)  # noqa N806
 28
 29    ax.contourf(xx, yy, Z, cmap=plt.cm.Paired, alpha=0.5)  # @UndefinedVariable
 30
 31    for i in (0, 1):
 32        idx = y == i
 33        ax.scatter(x[idx, x1], x[idx, x2], s=5)
 34    ax.set_xlabel(columns[x1])
 35    ax.set_ylabel(columns[x2])
 36
 37
 38def plot_diag(x1, ax):
 39    """Plot diagonal in pair grid."""
 40    x_min, x_max = x[:, x1].min(), x[:, x1].max()
 41    for i in (0, 1):
 42        idx = y == i
 43        ax.hist(x[idx, x1], range=(x_min, x_max), alpha=0.5)
 44
 45
 46# load data
 47experiments, outcomes = load_results("./data/1000 flu cases with policies.tar.gz")
 48
 49# transform to numpy array with proper recoding of cateogorical variables
 50x, columns = feature_scoring._prepare_experiments(experiments)
 51y = outcomes["deceased_population_region_1"][:, -1] > 1000000
 52
 53# establish mean case for factor maps
 54# this is questionable in particular in case of categorical dimensions
 55minima = x.min(axis=0)
 56maxima = x.max(axis=0)
 57nominal = minima + (maxima - minima) / 2
 58
 59# fit the boosted tree
 60bdt = AdaBoostClassifier(DecisionTreeClassifier(max_depth=3), n_estimators=200)
 61bdt.fit(x, y)
 62
 63# determine which dimensions are most important
 64sorted_indices = np.argsort(bdt.feature_importances_)[::-1]
 65
 66# do the actual plotting
 67# this is a quick hack, tying it to seaborn Pairgrid is probably
 68# the more elegant solution, but is tricky with what arguments
 69# can be passed to the plotting function
 70fig, axes = plt.subplots(ncols=5, nrows=5, figsize=(15, 15))
 71
 72for i, row in enumerate(axes):
 73    for j, ax in enumerate(row):
 74        if i > j:
 75            plot_factormap(sorted_indices[j], sorted_indices[i], ax, bdt, nominal)
 76        elif i == j:
 77            plot_diag(sorted_indices[j], ax)
 78        else:
 79            ax.set_xticks([])
 80            ax.set_yticks([])
 81            ax.axis("off")
 82
 83        if j > 0:
 84            ax.set_yticklabels([])
 85            ax.set_ylabel("")
 86        if i < len(axes) - 1:
 87            ax.set_xticklabels([])
 88            ax.set_xlabel("")
 89
 90# add the legend
 91# Draw a full-figure legend outside the grid
 92handles = [
 93    CircleCollection([10], color=sns.color_palette()[0]),
 94    CircleCollection([10], color=sns.color_palette()[1]),
 95]
 96
 97legend = fig.legend(handles, ["False", "True"], scatterpoints=1)
 98
 99plt.tight_layout()
100plt.show()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/sd_boostedtrees_flu.html
