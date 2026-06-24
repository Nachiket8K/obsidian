---
title: "Directed search"
source: "https://emaworkbench.readthedocs.io/en/latest/indepth_tutorial/directed-search.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# Directed search

This is the third turial in a series showcasing the functionality of the Exploratory Modeling workbench. Exploratory modeling entails investigating the way in which uncertainty and/or policy levers map to outcomes. To investigate these mappings, we can either use sampling based strategies (open exploration) or optimization based strategies (directed search).

In this tutorial, I will demonstrate in more detail how to use the workbench for directed search. We are using the same example as in the previous tutorials. When using optimization, it is critical that you specify for each Scalar Outcome the direction in which it should move. There are three possibilities: info which is ignored, maximize, and minimize. If the `kind` keyword argument is not specified, it defaults to info.

```
[1]:
```

```
from dps_lake_model import lake_model

from ema_workbench import Constant, Model, RealParameter, ScalarOutcome

model = Model("lakeproblem", function=lake_model)

# specify uncertainties
model.uncertainties = [
    RealParameter("b", 0.1, 0.45),
    RealParameter("q", 2.0, 4.5),
    RealParameter("mean", 0.01, 0.05),
    RealParameter("stdev", 0.001, 0.005),
    RealParameter("delta", 0.93, 0.99),
]

# set levers
model.levers = [
    RealParameter("c1", -2, 2),
    RealParameter("c2", -2, 2),
    RealParameter("r1", 0, 2),
    RealParameter("r2", 0, 2),
    RealParameter("w1", 0, 1),
]

# specify outcomes
model.outcomes = [
    ScalarOutcome("max_P", ScalarOutcome.MINIMIZE),
    ScalarOutcome("utility", ScalarOutcome.MAXIMIZE),
    ScalarOutcome("inertia", ScalarOutcome.MAXIMIZE),
    ScalarOutcome("reliability", ScalarOutcome.MAXIMIZE),
]

# override some of the defaults of the model
model.constants = [
    Constant("alpha", 0.41),
    Constant("nsamples", 150),
    Constant("myears", 100),
]
```

Using directed search with the ema\_workbench requires [platypus-opt](https://github.com/Project-Platypus/Platypus). Please check the installation suggestions provided in the readme of the github repository. I personally either install from github directly

```
pip git+https://github.com/Project-Platypus/Platypus.git
```

or through pip

```
pip install platypus-opt
```

One note of caution: don’t install platypus, but platypus-opt. There exists a python package on pip called platypus, but that is quite a different kind of library.

There are three ways in which we can use optimization in the workbench:

1. Search over the decision levers, conditional on a reference scenario
2. Search over the uncertain factors, conditional on a reference policy
3. Search over the decision levers given a set of scenarios

## Search over levers

Directed search is most often used to search over the decision levers in order to find good candidate strategies. This is for example the first step in the [Many Objective Robust Decision Making process](https://www.sciencedirect.com/science/article/pii/S1364815212003131). This is straightforward to do with the workbench using the optimize method.

Note that I have kept the number of functional evaluations (nfe) very low. In real applications this should be substantially higher and be based on convergence considerations which are demonstrated below.

```
[2]:
```

```
from ema_workbench import MultiprocessingEvaluator, ema_logging

ema_logging.log_to_stderr(ema_logging.INFO)

with MultiprocessingEvaluator(model) as evaluator:
    results, convergence_info = evaluator.optimize(
        nfe=250, searchover="levers", epsilons=[0.1] * len(model.outcomes),
        filename="archives.tar.gz", directory="./archives", rng=42
    )
```

```
[MainProcess/INFO] pool started with 10 workers
300it [00:03, 94.28it/s]
[MainProcess/INFO] optimization completed, found 5 solutions
[MainProcess/INFO] terminating pool
```

The results from optimize is a DataFrame with the decision variables and outcomes of interest. This dataframe contains both the decision variables (c1-w1) and the outcomes (max\_P-reliability). Each row is thus a single unique solution.

Note also that there might be a difference between the specified number of nfe (250 in this case) and the actual number of nfe. The default algorithm is population based and the nfe-based stopping condition is only checked after evaluating an entire generation.

```
[3]:
```

```
results
```

```
[3]:
```

|  | c1 | c2 | r1 | r2 | w1 | max\_P | utility | inertia | reliability |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0.714726 | 1.951570 | 0.820303 | 1.900079 | 0.984769 | 0.421131 | 1.502431 | 0.9900 | 1.0000 |
| 1 | 0.198240 | 1.317619 | 1.237040 | 1.723414 | 0.577352 | 2.819185 | 2.229967 | 0.9802 | 0.2744 |
| 2 | -0.323100 | 0.398352 | 1.045565 | 1.869413 | 0.204259 | 0.184076 | 0.632827 | 0.9900 | 1.0000 |
| 3 | 1.611222 | 0.462060 | 1.059661 | 1.093856 | 0.017233 | 0.257652 | 1.162073 | 0.9900 | 1.0000 |
| 4 | 1.625386 | 0.021719 | 1.669190 | 1.165019 | 0.148094 | 2.819290 | 2.542458 | 0.9900 | 0.1268 |

### Specifying constraints

It is possible to specify a constrained optimization problem. A model can have one or more constraints. A constraint can be applied to the model input parameters (both uncertainties and levers), and/or outcomes. A constraint is essentially a function that should return the distance from the feasibility threshold. The distance should be 0 if the constraint is met.

In the example below, we add a constrait saying that the value of the outcome `max_P` should be below 1. Given that this is a very simple constrain, I chose to use a lambda function to implement it. For more complicated constraints, you can also define your own function and pass that instead.

```
[4]:
```

```
from ema_workbench import Constraint

constraints = [
    Constraint("max pollution", outcome_names="max_P", function=lambda x: max(0, x - 1))
]
```

```
[5]:
```

```
from ema_workbench import MultiprocessingEvaluator, ema_logging

ema_logging.log_to_stderr(ema_logging.INFO)

with MultiprocessingEvaluator(model) as evaluator:
    results, convergence_info = evaluator.optimize(
        nfe=250,
        searchover="levers",
        epsilons=[0.1] * len(model.outcomes),
        constraints=constraints,
        filename="archives_constraints.tar.gz", directory="./archives",
        rng=42
    )
```

```
[MainProcess/INFO] pool started with 10 workers
300it [00:03, 91.35it/s]
[MainProcess/INFO] optimization completed, found 4 solutions
[MainProcess/INFO] terminating pool
```

```
[6]:
```

```
results
```

```
[6]:
```

|  | c1 | c2 | r1 | r2 | w1 | max\_P | utility | inertia | reliability |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 1.050043 | 0.177888 | 1.557253 | 1.420728 | 0.000572 | 0.095435 | 0.116777 | 0.99 | 1.0 |
| 1 | 0.827864 | 0.712511 | 1.345591 | 0.407015 | 0.784793 | 0.461046 | 1.133771 | 0.99 | 1.0 |
| 2 | 1.611222 | 0.462060 | 1.250183 | 1.095874 | 0.000406 | 0.154939 | 0.411175 | 0.99 | 1.0 |
| 3 | 0.850479 | 0.231193 | 1.242358 | 1.298042 | 0.602699 | 0.294705 | 0.900368 | 0.99 | 1.0 |

The new results with this simple constraint contains only a few solutions. This suggests that it is difficult to find solutions that are able to meet this constraint.

### Seed analysis

Genetic algorithms rely on randomness in the search process. This implies that a single run of the algorithm does not tell you that much because the results might be due to randomness. It is thus best practice to allways repeat the optimization for several different seeds and next merge the results across the different optimizations. This is supported by the workbench. We first need to run multiple optimization like this:

```
[7]:
```

```
import random

random.seed(42)
seeds = [random.randint(0, 1000) for _ in range(5)]  # we want to run 5 seeds

with MultiprocessingEvaluator(model) as evaluator:
    results = evaluator.optimize(
        nfe=25000, searchover="levers", epsilons=[0.05] * len(model.outcomes),
        filename="archives_seeds.tar.gz", directory="./archives", rng=seeds
    )
```

```
[MainProcess/INFO] pool started with 10 workers
25020it [01:43, 241.07it/s]
[MainProcess/INFO] optimization completed, found 6 solutions
25003it [01:36, 257.98it/s]
[MainProcess/INFO] optimization completed, found 9 solutions
25016it [01:35, 261.05it/s]
[MainProcess/INFO] optimization completed, found 9 solutions
25035it [01:35, 261.54it/s]
[MainProcess/INFO] optimization completed, found 9 solutions
25015it [01:36, 257.89it/s]
[MainProcess/INFO] optimization completed, found 11 solutions
[MainProcess/INFO] terminating pool
```

We now have the results for each of the five different runs of the optimization. The next step is to combine these into a singe comprehensive set. Since by default the workbench uses [ε-NSGAII](https://link.springer.com/chapter/10.1007/978-3-540-31880-4_27), it makes sense to also merge the results across the seeds using an ε-nondominated sort.

```
[8]:
```

```
from ema_workbench.em_framework.optimization import epsilon_nondominated, Problem

data = [r[0] for r in results]
problem = Problem("levers", model.levers, model.outcomes)
epsilons = [0.05] * len(model.outcomes)
merged_archives = epsilon_nondominated(data, epsilons, problem)
```

```
[9]:
```

```
merged_archives.shape
```

```
[9]:
```

```
(7, 9)
```

As can be seen, the new merged archive contains 6 solutions. Which is is quite a bit smaller than the sum of solutions across the 5 seeds. This implies that many of the solutions found in each seed land in the same ε-gridcell.

### Tracking convergence

An important part of using many-objective evolutionary algorithms is to carefully monitor whether they have converged to the best possible solutions. Various different metrics can be used for this. Some of these metrics must be collected at runtime, such as [ε-progress](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.469.9675&rep=rep1&type=pdf). Others, like [hypervolume](https://www.sciencedirect.com/science/article/pii/S0309170816300896?via%3Dihub#sec0007), are better
calculated after the optimization has been completed. The metrics that are better calculated after the optimization require, however, storing the state of the archive over the course of the optimization. Both types of metrics are supported by the workbench.

```
[10]:
```

```
fig, ax = plt.subplots()

for _ ,runtime_info in results:
    ax.plot(runtime_info.nfe, runtime_info.epsilon_progress)

ax.set_xlabel("nfe")
ax.set_ylabel("epsilon improvements")
plt.show()
```

![../_images/indepth_tutorial_directed-search_19_0.png](../_images/indepth_tutorial_directed-search_19_0.png)

Varous metrics are provied by platypus. For details on these metrics see *e.g.*, [Zatarain-Salazar et al (2016)](https://doi.org/10.1016/j.advwatres.2016.04.006) and [Gupta et al (2020)](https://doi.org/10.1016/j.advwatres.2020.103718) for hypervolume, generational distance and additive \(\epsilon\)-indicator; [Hadka and Reed (2012)](https://dl-acm-org.tudelft.idm.oclc.org/doi/pdf/10.1162/EVCO_a_00053?accessTab=true) for spacing; and [Hadka and Reed
(2013)](https://ieeexplore.ieee.org/document/6793867) for \(\epsilon\)-pgrogress. To use these metrics, we first need to load the archives into memory. Next, these metrics need a set of platypus solutions, instead of the dataframes that the workbench has stored. Moreover, most of these metrics need a reference set. The reference set, typically, is the union of best solutions found across the seeds and next filtered using an ε-nondominated sort. All these steps are supported by the
workbench as shown below.

```
[11]:
```

```
from ema_workbench import load_archives

all_archives = [load_archives('./archives/25_archives_seeds.tar.gz'),
                load_archives('./archives/114_archives_seeds.tar.gz'),
                load_archives('./archives/281_archives_seeds.tar.gz'),
                load_archives('./archives/654_archives_seeds.tar.gz'),
                load_archives('./archives/759_archives_seeds.tar.gz')]
```

```
[12]:
```

```
from ema_workbench import SpacingMetric

fig, ax = plt.subplots()
metric = SpacingMetric(merged_archives, problem)

for entry in all_archives:
    scores = []
    for nfe, archive in entry:
        score = metric.calculate(archive)
        scores.append((nfe, score))

    scores = np.asarray(scores)

    ax.plot(scores[:, 0], scores[:, 1])
ax.set_ylabel("spacing")
ax.set_xlabel("nfe")

plt.show()
```

![../_images/indepth_tutorial_directed-search_22_0.png](../_images/indepth_tutorial_directed-search_22_0.png)

### Changing the reference scenario

The workbench offers control over the reference scenario or policy under which you are performing the optimization. This makes it easy to apply multi-scenario MORDM ([Watson & Kasprzyk, 2017](https://www.sciencedirect.com/science/article/pii/S1364815216310593);[Eker & Kwakkel, 2018](https://doi.org/10.1016/j.envsoft.2018.03.029);[Bartholomew & Kwakkel, 2020](https://doi.org/10.1016/j.envsoft.2020.104699)). Alternatively, you can also use it to change the policy for which you are
applying worst case scenario discovery (see below).

```
reference = Sample('reference', b=0.4, q=2, mean=0.02, stdev=0.01)

with MultiprocessingEvaluator(lake_model) as evaluator:
    results = evaluator.optimize(searchover='levers', nfe=1000,
                       epsilons=[0.1, ]*len(lake_model.outcomes),
                       reference=reference)
```

## Search over uncertainties: worst case discovery

Up till now, the focus has been on applying search to find promising candidate strategies. That is, we search through the lever space. However, there might also be good reasons to search through the uncertainty space. For example to search for worst case scenarios [(Halim et al, 2015)](https://www.sciencedirect.com/science/article/pii/S0016328715001342). This is easily achieved as shown below. We change the kind attribute on each outcome so that we search for the worst outcome and specify
that we would like to search over the uncertainties instead of the levers.

Any of the foregoing additions such as constraints or convergence works as shown above. Note that if you would like to to change the reference policy, reference should be a Policy object rather than a Scenario object.

```
[13]:
```

```
from ema_workbench import Sample

# change outcomes so direction is undesirable
minimize = ScalarOutcome.MINIMIZE
maximize = ScalarOutcome.MAXIMIZE

for outcome in model.outcomes:
    if outcome.kind == minimize:
        outcome.kind = maximize
    else:
        outcome.kind = minimize

reference = Sample("no_release", decisions=np.zeros(100,))

with MultiprocessingEvaluator(model) as evaluator:
    results, convergencce_info = evaluator.optimize(
        nfe=5000, searchover="uncertainties", epsilons=[0.05] * len(model.outcomes),
        reference=reference,
        filename="archives_uncertainties.tar.gz", directory="./archives", rng=42
    )
```

```
[MainProcess/INFO] pool started with 10 workers
100%|█████████████████████████████████████| 5000/5000 [00:22<00:00, 220.59it/s]
[MainProcess/INFO] optimization completed, found 12 solutions
[MainProcess/INFO] terminating pool
```

## Parallel coordinate plots

The workbench comes with support for making parallel axis plots through the parcoords module. This module offers a parallel axes object on which we can plot data.

The typical workflow is to first instantiate this parallel axes object given a pandas dataframe with the upper and lower limits for each axes. Next, one or more datasets can be plotted on this axes. Any dataframe passed to the plot method will be normalized using the limits passed first. We can also invert any of the axes to ensure that the desirable direction is the same for all axes.

```
[14]:
```

```
from ema_workbench.analysis import parcoords

data = results.loc[:, [o.name for o in model.outcomes]]

# get the minimum and maximum values as present in the dataframe
limits = parcoords.get_limits(data)

# we know that the lowest possible value for all objectives is 0
limits.loc[0, ["utility", "inertia", "reliability", "max_P"]] = 0
# inertia and reliability are defined on unit interval, so their theoretical maximum is 1
limits.loc[1, ["inertia", "reliability"]] = 1

paraxes = parcoords.ParallelAxes(limits)
paraxes.plot(data)
paraxes.invert_axis("max_P")
plt.show()
```

![../_images/indepth_tutorial_directed-search_27_0.png](../_images/indepth_tutorial_directed-search_27_0.png)

The above parallel coordinate plot shows the results from the worst case discovery. The worst possible solution would be a straight line at the bottom. A key insight from this result is that there seems to be a trade-off between max\_P and utility. This can be inferred from the crossing lines between these two axes.

## Robust Search

In the foregoing, we have been using optimization over levers or uncertainties, while assuming a reference scenario or policy. However, we can also formulate a robust many objective optimization problem ([Kwakkel et al. 2015](https://doi.org/10.1007/s10584-014-1210-4); [Bartholomew et al. 2020](https://doi.org/10.1016/j.envsoft.2020.104699)), where we are going to search over the levers for solutions that have robust performance over a set of scenarios. To do this with the workbench, there
are several steps that one has to take.

First, we need to specify our robustness metrics. A robustness metric takes as input the performance of a candidate policy over a set of scenarios and returns a single robustness score. For a more in depth overview, see [McPhail et al. (2018)](https://agupubs.onlinelibrary.wiley.com/doi/full/10.1002/2017EF000649). In case of the workbench, we can use the ScalarOutcome class for this. We need to specify the name of the robustness metric a function that takes as input a numpy array and returns
a single number, and the model outcome to which this function should be applied.

Below, we use a percentile based robustness metric, which we apply to each model outcome.

```
[15]:
```

```
import functools

# our robustness functions
percentile10 = functools.partial(np.percentile, q=10)
percentile90 = functools.partial(np.percentile, q=90)

# convenient short hands
MAXIMIZE = ScalarOutcome.MAXIMIZE
MINIMIZE = ScalarOutcome.MINIMIZE

robustnes_functions = [
    ScalarOutcome(
        "90th percentile max_p",
        kind=MINIMIZE,
        variable_name="max_P",
        function=percentile90,
    ),
    ScalarOutcome(
        "10th percentile reliability",
        kind=MAXIMIZE,
        variable_name="reliability",
        function=percentile10,
    ),
    ScalarOutcome(
        "10th percentile inertia",
        kind=MAXIMIZE,
        variable_name="inertia",
        function=percentile10,
    ),
    ScalarOutcome(
        "10th percentile utility",
        kind=MAXIMIZE,
        variable_name="utility",
        function=percentile10,
    ),
]
```

Next, we have to generate the scenarios we want to use. Below we generate 10 scenarios, which we will keep fixed over the optimization. The exact number of scenarios to use is to be established through trial and error. Typically it involves balancing computational costs of more scenarios, with the stability of the robustness metric over the number of scenarios

```
[21]:
```

```
from ema_workbench.em_framework import LHSSampler

n_scenarios = 20
scenarios = LHSSampler().generate_samples(
    model.uncertainties, n_scenarios, rng=42
)
```

With the robustness metrics specified, and the scenarios, sampled, we can now perform robust many-objective optimization. Below is the code that one would run. Note that this is computationally very expensive since each candidate solution is going to be run for ten scenarios before we can calculate the robustness for each outcome of interest.

```
nfe = int(5e4)
with MultiprocessingEvaluator(model) as evaluator:
    robust_results, convergence_info = evaluator.robust_optimize(
        robustnes_functions,
        scenarios,
        nfe=nfe,
        epsilons=[0.025,] * len(robustnes_functions),
        filename="archive_robust.tar.gz",
        directory="./archives",
    )
```

```
[ ]:
```

```
nfe = int(5e4)
with MultiprocessingEvaluator(model) as evaluator:
    robust_results, convergence_info = evaluator.robust_optimize(
        robustnes_functions,
        scenarios,
        nfe=nfe,
        epsilons=[0.025,] * len(robustnes_functions),
        filename="archive_robust.tar.gz",
        directory="./archives",
    )
```

```
[MainProcess/INFO] pool started with 10 workers
  3%|█                                    | 1400/50000 [01:29<50:24, 16.07it/s]
```

We can now again visualize the results using a parallel coordinate plot. Note that we are visualizing the robustness scores rather than the outcomes of interest as specified in the underlying model.

```
[ ]:
```

```
from ema_workbench.analysis import parcoords

data = robust_results.loc[:, [o.name for o in robustnes_functions]]
limits = parcoords.get_limits(data)

paraxes = parcoords.ParallelAxes(limits)
paraxes.plot(data)
paraxes.invert_axis("90th percentile max_p")
plt.show()
```

What we can see in this parallel axis plot is that there is a clear tradeoff between robust high reliability and robsut low maximum polution. Likewise with inertia and utility. This can be seen from the crossing lines between these respective axes.

```
[ ]:
```

```

```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/indepth_tutorial/directed-search.html
