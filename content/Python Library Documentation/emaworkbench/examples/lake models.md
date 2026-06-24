---
title: "lake_models.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/lake_models.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# lake\_models.py

```
  1"""dps and intertemporal version of the shallow lake problem."""
  2
  3import math
  4
  5import numpy as np
  6from scipy.optimize import brentq
  7
  8__all__ = [
  9    "lake_problem_dps",
 10    "lake_problem_intertemporal",
 11]
 12
 13
 14def lake_problem_intertemporal(
 15    b: float = 0.42,  # decay rate for P in lake (0.42 = irreversible)
 16    q: float = 2.0,  # recycling exponent
 17    mean: float = 0.02,  # mean of natural inflows
 18    stdev: float = 0.001,  # future utility discount rate
 19    delta: float = 0.98,  # standard deviation of natural inflows
 20    alpha: float = 0.4,  # utility from pollution
 21    n_samples: int = 100,  # Monte Carlo sampling of natural inflows
 22    rng: int | None = 42,
 23    decisions: np.ndarray | None = None,
 24):
 25    """Run the intertemporal version of the shallow lake model."""
 26    if decisions is None:
 27        decisions = [0] * 100
 28        print("No valid decisions found, using 0 pollution release per year as default")
 29
 30    rng = np.random.default_rng(rng)
 31
 32    nvars = len(decisions)
 33    decisions = np.array(decisions)
 34
 35    # Calculate the critical pollution level (p_crit)
 36    p_crit = brentq(lambda x: x**q / (1 + x**q) - b * x, 0.01, 1.5)
 37
 38    # Generate natural inflows using lognormal distribution
 39    natural_inflows = rng.lognormal(
 40        mean=math.log(mean**2 / math.sqrt(stdev**2 + mean**2)),
 41        sigma=math.sqrt(math.log(1.0 + stdev**2 / mean**2)),
 42        size=(n_samples, nvars),
 43    )
 44
 45    # Initialize the pollution level matrix X
 46    X = np.zeros((n_samples, nvars))  # noqa: N806
 47
 48    # Loop through time to compute the pollution levels
 49    for t in range(1, nvars):
 50        X[:, t] = (
 51            (1 - b) * X[:, t - 1]
 52            + (X[:, t - 1] ** q / (1 + X[:, t - 1] ** q))
 53            + decisions[t - 1]
 54            + natural_inflows[:, t - 1]
 55        )
 56
 57    # Calculate the average daily pollution for each time step
 58    average_daily_p = np.mean(X, axis=0)
 59
 60    # Calculate the reliability (probability of the pollution level being below Pcrit)
 61    reliability = np.sum(p_crit > X) / float(n_samples * nvars)
 62
 63    # Calculate the maximum pollution level (max_P)
 64    max_p = np.max(average_daily_p)
 65
 66    # Calculate the utility by discounting the decisions using the discount factor (delta)
 67    utility = np.sum(alpha * decisions * np.power(delta, np.arange(nvars)))
 68
 69    # Calculate the inertia (the fraction of time steps with changes larger than 0.02)
 70    inertia = np.sum(np.abs(np.diff(decisions)) > 0.02) / float(nvars - 1)
 71
 72    return max_p, utility, inertia, reliability
 73
 74
 75def get_antropogenic_release(
 76    xt: float, c1: float, c2: float, r1: float, r2: float, w1: float
 77):
 78    """Return anthropogenic release at xt.
 79
 80    Parameters
 81    ----------
 82    xt : float
 83         pollution in lake at time t
 84    c1 : float
 85         center rbf 1
 86    c2 : float
 87         center rbf 2
 88    r1 : float
 89         radius rbf 1
 90    r2 : float
 91         radius rbf 2
 92    w1 : float
 93         weight of rbf 1
 94
 95    note:: w2 = 1 - w1
 96
 97    """
 98    rule = w1 * (abs(xt - c1) / r1) ** 3 + (1 - w1) * (abs(xt - c2) / r2) ** 3
 99    at1 = max(rule, 0.01)
100    at = min(at1, 0.1)
101
102    return at
103
104
105def lake_problem_dps(
106    b=0.42,  # decay rate for P in lake (0.42 = irreversible)
107    q=2.0,  # recycling exponent
108    mean=0.02,  # mean of natural inflows
109    stdev=0.001,  # future utility discount rate
110    delta=0.98,  # standard deviation of natural inflows
111    alpha=0.4,  # utility from pollution
112    n_samples=100,  # Monte Carlo sampling of natural inflows
113    myears=1,  # the runtime of the simulation model
114    c1=0.25,
115    c2=0.25,
116    r1=0.5,
117    r2=0.5,
118    w1=0.5,
119    rng=42,
120):
121    """DPS version of the lake problem."""
122    p_crit = brentq(lambda x: x**q / (1 + x**q) - b * x, 0.01, 1.5)
123
124    rng = np.random.default_rng(rng)
125
126    X = np.zeros(myears)  # noqa: N806
127    average_daily_p = np.zeros(myears)
128    reliability = 0.0
129    inertia = 0
130    utility = 0
131
132    for _ in range(n_samples):
133        X[0] = 0.0
134        decision = 0.1
135
136        decisions = np.zeros(myears)
137        decisions[0] = decision
138
139        natural_inflows = rng.lognormal(
140            math.log(mean**2 / math.sqrt(stdev**2 + mean**2)),
141            math.sqrt(math.log(1.0 + stdev**2 / mean**2)),
142            size=myears,
143        )
144
145        for t in range(1, myears):
146            # here we use the decision rule
147            decision = get_antropogenic_release(X[t - 1], c1, c2, r1, r2, w1)
148            decisions[t] = decision
149
150            X[t] = (
151                (1 - b) * X[t - 1]
152                + X[t - 1] ** q / (1 + X[t - 1] ** q)
153                + decision
154                + natural_inflows[t - 1]
155            )
156            average_daily_p[t] += X[t] / n_samples
157
158        reliability += np.sum(p_crit > X) / (n_samples * myears)
159        inertia += np.sum(np.absolute(np.diff(decisions) < 0.02)) / (n_samples * myears)
160        utility += (
161            np.sum(alpha * decisions * np.power(delta, np.arange(myears))) / n_samples
162        )
163    max_p = np.max(average_daily_p)
164
165    return max_p, utility, inertia, reliability
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/lake_models.html
