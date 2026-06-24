---
title: "BatchRunner"
source: "https://mesa.readthedocs.io/stable/tutorials/11_batch_run.html"
imported_from: "Python library documentation"
library: "Mesa"
---

# BatchRunner

## The Boltzmann Wealth Model

If you want to get straight to the tutorial checkout these environment providers:  
(with Google Account) [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mesa/mesa/blob/main/docs/tutorials/7_batch_run.ipynb)  
(No Google Account) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mesa/mesa/main?labpath=docs%2Ftutorials%2F7_batch_run.ipynb) (This can take 30 seconds to 5 minutes to load)

*If you are running locally, please ensure you have the latest Mesa version installed.*

## Tutorial Description

This tutorial extends the Boltzmann wealth model from the [Collecting Data tutorial](5_collecting_data.html), by showing how users can use `batch_run` to conduct parameter sweeps of their models.

*If you are starting here please see the [Running Your First Model tutorial](0_first_model.html) for dependency and start-up instructions*

### IN COLAB? - Run the next cell

### Import Dependencies

This includes importing of dependencies needed for the tutorial.

```
# Has multi-dimensional arrays and matrices.
# Has a large collection of mathematical functions to operate on these arrays.
import numpy as np

# Data manipulation and analysis.
import pandas as pd

# Data visualization tools.
import seaborn as sns

import mesa

# Import Cell Agent and OrthogonalMooreGrid
from mesa.discrete_space import CellAgent, OrthogonalMooreGrid
```

## Base Model

The below provides the base model from which we will add batch\_run functionality. Of note, this is the same as the [collecting data tutorial](5_collecting_data.html) but we add one agent reporter that counts if money is not given to that agent during a time step.

We also added `self.running=True` in the `MoneyModel` class. This allows users to provide a conditional stop attribute (e.g. all sheep and wolves die) as opposed to a step count.)

This is from the [Running Your First Model tutorial](0_first_model.html) tutorial. If you have any questions about it functionality please review that tutorial.

```
def compute_gini(model):
    agent_wealths = [agent.wealth for agent in model.agents]
    x = sorted(agent_wealths)
    n = model.num_agents
    B = sum(xi * (n - i) for i, xi in enumerate(x)) / (n * sum(x))
    return 1 + (1 / n) - 2 * B

class MoneyAgent(CellAgent):
    """An agent with fixed initial wealth."""

    def __init__(self, model, cell):
        super().__init__(model)
        self.cell = cell
        self.wealth = 1
        self.steps_not_given = 0

    def move(self):
        self.cell = self.cell.neighborhood.select_random_cell()

    def give_money(self):
        cellmates = [a for a in self.cell.agents if a is not self]

        if len(cellmates) > 0 and self.wealth > 0:
            other = self.random.choice(cellmates)
            other.wealth += 1
            self.wealth -= 1
            self.steps_not_given = 0
        else:
            self.steps_not_given += 1

class MoneyModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, n, width, height, seed=None):
        super().__init__(seed=seed)
        self.num_agents = n
        self.grid = OrthogonalMooreGrid((width, height), torus=True, random=self.random)
        # Instantiate DataCollector
        self.datacollector = mesa.DataCollector(
            model_reporters={"Gini": compute_gini},
            agent_reporters={"Wealth": "wealth", "Steps_not_given": "steps_not_given"},
        )
        self.running = True

        # Create agents
        agents = MoneyAgent.create_agents(
            self,
            self.num_agents,
            self.random.choices(self.grid.all_cells.cells, k=self.num_agents),
        )

    def step(self):
        # Collect data each step
        self.datacollector.collect(self)
        self.agents.shuffle_do("move")
        self.agents.do("give_money")
```

```
model = MoneyModel(100, 10, 10)
for _ in range(100):
    model.step()

gini = model.datacollector.get_model_vars_dataframe()
g = sns.lineplot(data=gini)
g.set(title="Gini Coefficient over Time", ylabel="Gini Coefficient");
```

![../_images/f602fe26a80bd31174159075b6bdfa9a9aa75745118b5ff40b1b1a6629a9c24d.png](../_images/f602fe26a80bd31174159075b6bdfa9a9aa75745118b5ff40b1b1a6629a9c24d.png)

## Batch Run

Modelers typically won’t run a model just once, but multiple times, with fixed parameters to find the overall distributions the model generates, and with varying parameters to analyze how these variables drive the model’s outputs and behaviors. This is commonly referred to as parameter sweeps. Instead of needing to write nested for-loops for each model, Mesa provides a [`batch_run`](https://mesa.readthedocs.io/latest/apis/batchrunner.html) function which automates parameter sweeps and allows the model variants to run on multiple processors.

### Batch run parameters

We call `batch_run` with the following arguments:

- `model_cls`
  The model class that is used for the batch run.
- `parameters`
  A dictionary containing all the parameters of the model class and desired values to use for the batch run as key-value pairs. Each value can either be fixed ( e.g. `{"height": 10, "width": 10}`) or an iterable (e.g. `{"n": range(10, 500, 10)}`). `batch_run` will then generate all possible parameter combinations based on this dictionary and run the model `iterations` times for each combination.
- `number_processes`
  If not specified, defaults to 1. Set it to `None` to use all the available processors.
  Note: Multiprocessing does make debugging challenging. If your parameter sweeps are resulting in unexpected errors set `number_processes=1`.
- `rng`
  a valid value or iterable of values for seeding the random number generator in the model. Defaults to a single None value meaning the model is ran once.
- `data_collection_period`
  The length of the period (number of steps) after which the model and agent reporters collect data. Optional. If not specified, defaults to -1, i.e. only at the end of each episode.
- `max_steps`
  The maximum number of time steps after which the model halts. An episode does either end when `self.running` of the model class is set to `False` or when `model.steps == max_steps` is reached. Optional. If not specified, defaults to 1000.
- `display_progress`
  Display the batch run progress. Optional. If not specified, defaults to `True`.

In the following example, we hold the height and width fixed, and vary the number of agents. We tell the batch runner to run 5 instantiations of the model with each number of agents, and to run each for 100 steps.

We want to keep track of

1. The Gini coefficient value at each time step
2. The individual agent’s wealth development and steps without giving money.

**Important:** Since for the latter, changes at each time step might be interesting, we set `data_collection_period=1`. By default, it only collects data at the end of each episode.

Note: The total number of runs is 100 (20 different populations \* 5 iterations per population).

```
import sys

rng = np.random.default_rng(42)
seed_values = rng.integers(0, sys.maxsize, size=(5,))
```

```
params = {"width": 10, "height": 10, "n": range(5, 105, 5)}

results = mesa.batch_run(
    MoneyModel,
    parameters=params,
    rng=seed_values.tolist(),
    max_steps=100,
    number_processes=1,
    data_collection_period=1,
    display_progress=True,
)
```

```
/home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/stable/lib/python3.14/site-packages/mesa/mesa_logging.py:112: FutureWarning: The use of the `seed` keyword argument is deprecated, use `rng` instead. No functional changes.
  res = func(*args, **kwargs)
```

To further analyze the return of the `batch_run` function, we convert the list of dictionaries to a Pandas DataFrame and print its keys.

### Batch Run Analysis and Visualization

```
results_df = pd.DataFrame(results)
print(f"The results have {len(results)} rows.")
print(f"The columns of the data frame are {list(results_df.keys())}.")
```

```
The results have 525000 rows.
The columns of the data frame are ['RunId', 'iteration', 'Step', 'width', 'height', 'n', 'seed', 'Gini', 'AgentID', 'Wealth', 'Steps_not_given'].
```

First, we want to take a closer look at how the Gini coefficient at the end of each episode changes as we increase the size of the population. For this, we filter our results to only contain the data of one agent (the Gini coefficient will be the same for the entire population at any time) at the 100th step of each episode and then scatter-plot the values for the Gini coefficient over the the number of agents. Notice there are five values for each population size since we set `iterations=5` when calling the batch run.

```
# Filter the results to only contain the data of one agent
# The Gini coefficient will be the same for the entire population at any time
results_filtered = results_df[(results_df.AgentID == 1) & (results_df.Step == 100)]
results_filtered[["iteration", "n", "Gini"]].reset_index(
    drop=True
).head()  # Create a scatter plot
g = sns.scatterplot(data=results_filtered, x="n", y="Gini")
g.set(
    xlabel="number of agents",
    ylabel="Gini coefficient",
    title="Gini coefficient vs. Number of Agents",
);
```

![../_images/e4326c072c0cf9f55cf2977dc754b81961b382dd9917f6edb51d1b1a006be90e.png](../_images/e4326c072c0cf9f55cf2977dc754b81961b382dd9917f6edb51d1b1a006be90e.png)

We can create different kinds of plot from this filtered DataFrame. For example, a point plot with error bars.

```
# Create a point plot with error bars
g = sns.pointplot(data=results_filtered, x="n", y="Gini", linestyle="None")
g.figure.set_size_inches(8, 4)
g.set(
    xlabel="number of agents",
    ylabel="Gini coefficient",
    title="Gini coefficient vs. number of agents",
);
```

![../_images/0d22d28b7241e15c08e4cf34141a12f69da193c7fb64dab33b06d7cf8a52773f.png](../_images/0d22d28b7241e15c08e4cf34141a12f69da193c7fb64dab33b06d7cf8a52773f.png)

Secondly, we want to display the agent’s wealth at each time step of one specific episode. To do this, we again filter our large data frame, this time with a fixed number of agents and only for a specific iteration of that population.
To print the results, we convert the filtered data frame to a string specifying the desired columns to print.

Pandas has built-in functions to convert to a lot of different data formats. For example, to display as a table in a Jupyter, we can use the `to_html()` function which takes the same arguments as `to_string()` (see commented lines).

```
# First, we filter the results
one_episode_wealth = results_df[(results_df.n == 10) & (results_df.iteration == 2)]
# Then, print the columns of interest of the filtered data frame
print(
    one_episode_wealth.to_string(
        index=False, columns=["Step", "AgentID", "Wealth"], max_rows=10
    )
)
# For a prettier display we can also convert the data frame to html
# Uncomment the two lines below to test in Jupyter
# from IPython.display import display, HTML
# display(HTML(one_episode_wealth.to_html(index=False, columns=['Step',
# 'AgentID', 'Wealth'], max_rows=25)))
```

```
 Step  AgentID  Wealth
  1.0        1       1
  1.0        2       1
  1.0        3       1
  1.0        4       1
  1.0        5       1
  ...      ...     ...
100.0        6       1
100.0        7       1
100.0        8       1
100.0        9       2
100.0       10       0
```

Lastly, we want to take a look at the development of the Gini coefficient over the course of one iteration. Filtering and printing looks almost the same as above, only this time we choose a different episode.

```
results_one_episode = results_df[
    (results_df.n == 10) & (results_df.iteration == 1) & (results_df.AgentID == 1)
]
print(results_one_episode.to_string(index=False, columns=["Step", "Gini"], max_rows=10))
```

```
 Step  Gini
  1.0  0.00
  2.0  0.00
  3.0  0.00
  4.0  0.00
  5.0  0.00
  ...   ...
 96.0  0.18
 97.0  0.18
 98.0  0.18
 99.0  0.18
100.0  0.18
```

## Next Steps

Check out the [comparing scenarios tutorial](12_comparing_scenarios.html) on analyzing `batch_run` results.

[Comer2014] Comer, Kenneth W. “Who Goes First? An Examination of the Impact of Activation on Outcome Behavior in AgentBased Models.” George Mason University, 2014. http://mars.gmu.edu/bitstream/handle/1920/9070/Comer\_gmu\_0883E\_10539.pdf

[Dragulescu2002] Drăgulescu, Adrian A., and Victor M. Yakovenko. “Statistical Mechanics of Money, Income, and Wealth: A Short Survey.” arXiv Preprint Cond-mat/0211175, 2002. http://arxiv.org/abs/cond-mat/0211175.

On this page

### This Page

- [Show Source](../_sources/tutorials/11_batch_run.ipynb.txt)

---

Original source: https://mesa.readthedocs.io/stable/tutorials/11_batch_run.html
