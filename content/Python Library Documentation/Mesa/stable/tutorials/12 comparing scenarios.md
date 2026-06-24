---
title: "Comparing Scenarios"
source: "https://mesa.readthedocs.io/stable/tutorials/12_comparing_scenarios.html"
imported_from: "Python library documentation"
library: "Mesa"
---

# Comparing Scenarios

## The Boltzmann Wealth Model

If you want to get straight to the tutorial checkout these environment providers:  
(with Google Account) [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mesa/mesa/blob/main/docs/tutorials/12_comparing_scenarios.ipynb)  
(No Google Account) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mesa/mesa/main?labpath=docs%2Ftutorials%2F12_comparing_scenarios.ipynb) (This can take 30 seconds to 5 minutes to load)

*If you are running locally, please ensure you have the latest Mesa version installed.*

## Tutorial Description

This tutorial extends the Boltzmann wealth model from the [Batch Run tutorial](11_batch_run.html), by showing some ways in which users can analyze `batch_run` results.

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

The below provides the base model from which we conduct a parameter sweep by altering the population parameter and running each variation for 5 scenarios.

This is from the [Batch Run tutorial](11_batch_run.html) tutorial. If you have any questions about it functionality please review that tutorial.

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
params = {"width": 10, "height": 10, "n": range(5, 105, 5)}

results = mesa.batch_run(
    MoneyModel,
    parameters=params,
    iterations=5,
    max_steps=100,
    number_processes=1,
    data_collection_period=1,
    display_progress=True,
)
```

```
/tmp/ipykernel_667/3699662278.py:3: DeprecationWarning: The `iterations` keyword argument is deprecated. Use `rng` instead (e.g. `iterations=5` is equivalent to `rng=[None] * 5`). See https://mesa.readthedocs.io/latest/migration_guide.html#batch-run
  results = mesa.batch_run(
```

We will now extract the results into a pandas dataframe.

```
results_df = pd.DataFrame(results)
print(f"The results have {len(results)} rows.")
print(f"The columns of the data frame are {list(results_df.keys())}.")
```

```
The results have 525000 rows.
The columns of the data frame are ['RunId', 'iteration', 'Step', 'width', 'height', 'n', 'seed', 'Gini', 'AgentID', 'Wealth', 'Steps_not_given'].
```

### Analyzing model reporters: Comparing 5 scenarios

Other insights might be gathered when we compare the Gini coefficient of different scenarios. For example, we can compare the Gini coefficient of a population with 25 agents to the Gini coefficient of a population with 400 agents. While doing this, we increase the number of iterations to 25 to get a better estimate of the Gini coefficient for each population size and get usable error estimations.

As we look varying the parameters to see the impact on model outcomes, it is critical to again point out that users can set the random seed. Due to the often inherent randomness with ABMs the seed becomes crucial for:

- **Reproducibility** - Being able to replicate the ABM results
- **Sensitivity Analysis** - Identifying how sensitive/robust your model results are to random fluctuations

Treating the seed as an additional parameter and running numerous scenarios allows us to see the impact of randomness on this model.

```
params = {"seed": None, "width": 10, "height": 10, "n": [5, 10, 20, 40, 80]}

results_5s = mesa.batch_run(
    MoneyModel,
    parameters=params,
    iterations=25,
    max_steps=100,
    number_processes=1,
    data_collection_period=1,  # Need to collect every step
    display_progress=True,
)

results_5s_df = pd.DataFrame(results_5s)
```

```
/tmp/ipykernel_667/3791477233.py:3: DeprecationWarning: The `iterations` keyword argument is deprecated. Use `rng` instead (e.g. `iterations=5` is equivalent to `rng=[None] * 5`). See https://mesa.readthedocs.io/latest/migration_guide.html#batch-run
  results_5s = mesa.batch_run(
```

We filter the results to only contain the data of one agent

```
# The Gini coefficient will be the same for the entire population at any time.
results_5s_df_filtered = results_5s_df[(results_5s_df.AgentID == 1)]
results_5s_df_filtered.head(3)
```

|  | RunId | iteration | Step | seed | width | height | n | Gini | AgentID | Wealth | Steps\_not\_given |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 1.0 | None | 10 | 10 | 5 | 0.0 | 1 | 1 | 0 |
| 5 | 0 | 0 | 2.0 | None | 10 | 10 | 5 | 0.0 | 1 | 1 | 1 |
| 10 | 0 | 0 | 3.0 | None | 10 | 10 | 5 | 0.0 | 1 | 1 | 2 |

```
# Create a lineplot with error bars
g = sns.lineplot(
    data=results_5s_df,
    x="Step",
    y="Gini",
    hue="n",
    errorbar=("ci", 95),
    palette="tab10",
)
g.figure.set_size_inches(8, 4)
plot_title = (
    "Gini coefficient for different population sizes\n"
    "(mean over 100 runs, with 95% confidence interval)"
)
g.set(title=plot_title, ylabel="Gini coefficient");
```

![../_images/43ff3d6e7cb02656a07ef1f3c2fe36b3ca21c0b053a87165f54f259a4ac86a16.png](../_images/43ff3d6e7cb02656a07ef1f3c2fe36b3ca21c0b053a87165f54f259a4ac86a16.png)

In this case it looks like the Gini coefficient increases slower for smaller populations. This can be because of different things, either because the Gini coefficient is a measure of inequality and the smaller the population, the more likely it is that the agents are all in the same wealth class, or because there are less interactions between agents in smaller populations, which means that the wealth of an agent is less likely to change.

### Exercise:

Treat the seed as a parameter and see the impact on the Gini Coefficient

You can also plot the seeds against the Gini Coefficient by changing the “hue” parameter in sns.lineplot function.

### Analyzing agent reporters: Comparing 5 scenarios

From the agents we collected the wealth and the number of consecutive rounds without a transaction. We can compare the 5 different population sizes by plotting the average number of consecutive rounds without a transaction for each population size.

Note that we’re aggregating multiple times here: First we take the average of all agents for each single replication. Then we plot the averages for all replications, with the error band showing the 95% confidence interval of that first average (over all agents). So this error band is representing the uncertainty of the mean value of the number of consecutive rounds without a transaction for each population size.

```
# Calculate the mean of the wealth and the number of consecutive rounds
# for all agents in each episode.
agg_results_df = (
    results_5s_df.groupby(["iteration", "n", "Step"])
    .agg({"Wealth": "mean", "Steps_not_given": "mean"})
    .reset_index()
)
agg_results_df.head(3)
```

|  | iteration | n | Step | Wealth | Steps\_not\_given |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | 5 | 1.0 | 1.0 | 0.0 |
| 1 | 0 | 5 | 2.0 | 1.0 | 1.0 |
| 2 | 0 | 5 | 3.0 | 1.0 | 2.0 |

```
# Create a line plot with error bars
g = sns.lineplot(
    data=agg_results_df, x="Step", y="Steps_not_given", hue="n", palette="tab10"
)
g.figure.set_size_inches(8, 4)
g.set(
    title="Average number of consecutive rounds without a transaction for "
    "different population sizes\n(mean with 95% confidence interval)",
    ylabel="Consecutive rounds without a transaction",
);
```

![../_images/14666c4f4bd6fe73817eaf4d4c7f0e43621ddb9ac61a883424dc9f8fcd2f660f.png](../_images/14666c4f4bd6fe73817eaf4d4c7f0e43621ddb9ac61a883424dc9f8fcd2f660f.png)

It can be clearly seen that the lower the number of agents, the higher the number of consecutive rounds without a transaction. This is because the agents have fewer interactions with each other and therefore the wealth of an agent is less likely to change.

### General steps for analyzing results

Many other analysis are possible based on the policies, scenarios and uncertainties that you might be interested in. In general, you can follow these steps to do your own analysis:

1. Determine which metrics you want to analyse. Add these as model and agent reporters to the datacollector of your model.
2. Determine the input parameters you want to vary. Add these as parameters to the batch\_run function, using ranges or lists to test different values.
3. Determine the hyperparameters of the batch\_run function. Define the number of iterations, the number of processes, the number of steps, the data collection period, etc.
4. Run the batch\_run function and save the results.
5. Transform, filter and aggregate the results to get the data you want to analyze. Make sure it’s in long format, so that each row represents a single value.
6. Choose a plot type, what to plot on the x and y axis, which columns to use for the hue. Seaborn also has an amazing [Example Gallery](https://seaborn.pydata.org/examples/index.html).
7. Plot the data and analyze the results.

### Exercise:

Update the model in some new way (e.g. a new agent attribute, a new model reporter), conduct a batch run with a parameter sweep and visualize your results

## That is it you have successfully completed Mesa’s Introductory Tutorial!

### More Mesa

If you are looking for other Mesa models or tools here are some additional resources.

- Example ABMs: Find canonical examples and examples of ABMs demonstrating highlighted features in the [Examples Tab](https://mesa.readthedocs.io/stable/examples.html)
- Expanded Examples: Want to integrate Reinforcement Learning or work on the Traveling Salesman Problem? Checkout [Mesa Examples](https://github.com/mesa/mesa-examples/)
- Mesa-Geo: If you need an ABM with Geographic Information Systems (GIS) checkout [Mesa-Geo](https://mesa-geo.readthedocs.io/latest/)
- Mesa Frames: Have a large complex model that you need to speed up, check out [Mesa Frames](https://github.com/mesa/mesa-frames)

## Happy Modeling!

This document is a work in progress. If you see any errors, exclusions or have any problems please contact [us](https://github.com/mesa/mesa/issues).

[Comer2014] Comer, Kenneth W. “Who Goes First? An Examination of the Impact of Activation on Outcome Behavior in AgentBased Models.” George Mason University, 2014. http://mars.gmu.edu/bitstream/handle/1920/9070/Comer\_gmu\_0883E\_10539.pdf

[Dragulescu2002] Drăgulescu, Adrian A., and Victor M. Yakovenko. “Statistical Mechanics of Money, Income, and Wealth: A Short Survey.” arXiv Preprint Cond-mat/0211175, 2002. http://arxiv.org/abs/cond-mat/0211175.

On this page

### This Page

- [Show Source](../_sources/tutorials/12_comparing_scenarios.ipynb.txt)

---

Original source: https://mesa.readthedocs.io/stable/tutorials/12_comparing_scenarios.html
