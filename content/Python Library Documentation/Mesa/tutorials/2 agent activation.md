---
title: "Agent Activation"
source: "https://mesa.readthedocs.io/latest/tutorials/2_agent_activation.html"
imported_from: "Python library documentation"
library: "Mesa"
---

# Agent Activation

## The Boltzmann Wealth Model

**Important:**

- If you are just exploring Mesa and want the fastest way to execute the code we recommend executing this tutorial online in a Colab notebook. [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mesa/mesa/blob/main/docs/tutorials/2_agent_activation.ipynb) or if you do not have a Google account you can use [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mesa/mesa/main?labpath=docs%2Ftutorials%2F2_agent_activation.ipynb) (This can take 30 seconds to 5 minutes to load)
- If you are running locally, please ensure you have the latest Mesa version installed.

## Tutorial Description

In the [previous tutorial](1_agentset.html)
you learned how to query, filter, and group agents using AgentSet. Now we’ll cover how
to make agents actually **do** things — and why the *order* and *pattern* of activation
matters.
By the end of this tutorial you will know how to:

- Activate agents sequentially (`do`) and in random order (`shuffle_do`)
- Collect return values with `map`
- Combine `select` with activation for conditional execution
- Implement common activation patterns: simultaneous, staged, and type-based
- Understand why activation order affects model outcomes

### IN COLAB? - Run the next cell

```
# %pip install --quiet mesa[rec]
```

### Import Dependencies

```
import numpy as np
import seaborn as sns

import mesa
```

## `do` and `shuffle_do`: The Core Activation Methods

AgentSet provides two primary methods for activating agents:

- **`do(method)`** — Calls the named method on each agent, in the current order of the set.
- **`shuffle_do(method)`** — Randomly reorders agents, then calls the method on each.
  Both accept a method name (string) or a callable. Additional arguments are passed
  through to each agent’s method.
  Let’s see these in action with a minimal model.

```
class MoneyAgent(mesa.Agent):
    """An agent with fixed initial wealth."""

    def __init__(self, model):
        super().__init__(model)
        self.wealth = 1

    def exchange(self):
        if self.wealth > 0:
            other = self.random.choice(self.model.agents)
            other.wealth += 1
            self.wealth -= 1

class MoneyModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, n=10):
        super().__init__()
        MoneyAgent.create_agents(model=self, n=n)

    def step(self):
        # Random activation — each agent acts in a random order
        self.agents.shuffle_do("exchange")
```

```
model = MoneyModel(10)
model.run_for(30)

wealth = model.agents.get("wealth")
print(f"Wealth distribution: {sorted(wealth, reverse=True)}")
print(f"Total wealth: {sum(wealth)} (should be {len(model.agents)})")
```

```
Wealth distribution: [3, 2, 2, 1, 1, 1, 0, 0, 0, 0]
Total wealth: 10 (should be 10)
```

## Why Activation Order Matters

The order in which agents act can significantly affect model outcomes. Consider a
simple scenario: if Agent A gives money to Agent B, and then Agent B gives money away,
Agent B now has more to give. If the order were reversed — B acts first, then A gives
to B — the outcome differs.
This is a well-studied phenomenon in agent-based modeling. Comer (2014) showed that
activation order can materially impact emergent behavior.
Let’s demonstrate this by comparing `do` (fixed order) with `shuffle_do` (random order).

```
# Fixed order — same agent always goes first
class FixedOrderModel(mesa.Model):
    def __init__(self, n=10):
        super().__init__()
        MoneyAgent.create_agents(model=self, n=n)

    def step(self):
        self.agents.do("exchange")  # Same order every step

# Random order — different every step
class RandomOrderModel(mesa.Model):
    def __init__(self, n=10):
        super().__init__()
        MoneyAgent.create_agents(model=self, n=n)

    def step(self):
        self.agents.shuffle_do("exchange")

# Run both multiple times and compare Gini coefficients
def gini(model):
    x = sorted(model.agents.get("wealth"))
    n = len(x)
    B = sum(xi * (n - i) for i, xi in enumerate(x)) / (n * sum(x))
    return 1 + (1 / n) - 2 * B

fixed_ginis = []
random_ginis = []
for _ in range(50):
    m = FixedOrderModel(50)
    m.run_for(100)
    fixed_ginis.append(gini(m))

    m = RandomOrderModel(50)
    m.run_for(100)
    random_ginis.append(gini(m))

print(
    f"Fixed order  — mean Gini: {np.mean(fixed_ginis):.3f} (std: {np.std(fixed_ginis):.3f})"
)
print(
    f"Random order — mean Gini: {np.mean(random_ginis):.3f} (std: {np.std(random_ginis):.3f})"
)
```

```
Fixed order  — mean Gini: 0.621 (std: 0.054)
Random order — mean Gini: 0.607 (std: 0.047)
```

**General guidance:** Use `shuffle_do` unless your model specifically requires a fixed
activation order. Random activation avoids systematic biases where early-acting agents
have an inherent advantage.

## Using Callables with `do`

Instead of passing a method name as a string, you can pass a callable function directly.
The function receives each agent as its first argument:

```
# Using a callable instead of a method name
def tax_agent(agent):
    """Take 10% tax from agents with wealth > 5."""
    if agent.wealth > 5:
        tax = agent.wealth // 10
        agent.wealth -= tax

model = MoneyModel(50)
model.run_for(100)

print(f"Max wealth before tax: {model.agents.agg('wealth', max)}")
model.agents.do(tax_agent)
print(f"Max wealth after tax: {model.agents.agg('wealth', max)}")
```

```
Max wealth before tax: 4
Max wealth after tax: 4
```

## Collecting Results with `map`

While `do` calls a method and discards the return values, `map` calls a method and
**returns the results** as a list. Use `map` when each agent computes something you
need to collect.

```
class ReportingAgent(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)
        self.wealth = 1
        self.age = self.random.randint(18, 80)

    def report_status(self):
        return {"id": self.unique_id, "wealth": self.wealth, "age": self.age}

    def exchange(self):
        if self.wealth > 0:
            other = self.random.choice(self.model.agents)
            other.wealth += 1
            self.wealth -= 1

class ReportingModel(mesa.Model):
    def __init__(self, n=10):
        super().__init__()
        ReportingAgent.create_agents(model=self, n=n)

    def step(self):
        self.agents.shuffle_do("exchange")

model = ReportingModel(10)
model.run_for(20)

# Collect status reports from all agents
reports = model.agents.map("report_status")
print("Agent reports:")
for r in reports[:5]:
    print(f"  {r}")
```

```
Agent reports:
  {'id': 1, 'wealth': 0, 'age': 76}
  {'id': 2, 'wealth': 2, 'age': 54}
  {'id': 3, 'wealth': 0, 'age': 80}
  {'id': 4, 'wealth': 0, 'age': 73}
  {'id': 5, 'wealth': 5, 'age': 76}
```

You can also use `map` with a callable:

```
# Calculate each agent's wealth-to-age ratio
ratios = model.agents.map(lambda a: a.wealth / a.age)
print(f"Wealth/age ratios (first 5): {[f'{r:.3f}' for r in ratios[:5]]}")
```

```
Wealth/age ratios (first 5): ['0.000', '0.037', '0.000', '0.000', '0.066']
```

## Conditional Activation with `select` + `do`

One of the most powerful patterns in Mesa is combining `select` with activation.
By filtering agents first, you can activate only those that meet specific criteria.
In many real-world models, not all agents act every step. Maybe only agents with
sufficient energy can move, only living agents can reproduce, or only wealthy agents
pay taxes.

```
class MoneyAgent(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)
        self.wealth = 1

    def exchange(self):
        if self.wealth > 0:
            other = self.random.choice(self.model.agents)
            other.wealth += 1
            self.wealth -= 1

    def donate(self, recipients):
        """Give 1 unit to a random recipient."""
        if self.wealth > 0 and len(recipients) > 0:
            recipient = self.random.choice(recipients)
            recipient.wealth += 1
            self.wealth -= 1

class PolicyModel(mesa.Model):
    """A model where only rich agents donate to poor agents."""

    def __init__(self, n=100):
        super().__init__()
        MoneyAgent.create_agents(model=self, n=n)

    def step(self):
        # First: normal exchanges
        self.agents.shuffle_do("exchange")

        # Then: redistribution policy — rich donate to poor
        rich = self.agents.select(lambda a: a.wealth >= 5)
        poor = self.agents.select(lambda a: a.wealth == 0)
        if len(rich) > 0 and len(poor) > 0:
            rich.shuffle_do("donate", poor)

model = PolicyModel(100)
model.run_for(100)

broke = len(model.agents.select(lambda a: a.wealth == 0))
rich = len(model.agents.select(lambda a: a.wealth >= 5))
print(f"After redistribution policy: {broke} broke agents, {rich} rich agents")
```

```
After redistribution policy: 43 broke agents, 0 rich agents
```

## Common Activation Patterns

Before Mesa 3.0, activation patterns were hard-coded into “scheduler” classes
(RandomActivation, SimultaneousActivation, etc.). Now, you compose them directly
from AgentSet methods. This is more flexible — you can mix and match any combination.
Here are the most common patterns:

### Sequential Activation

Agents act in a fixed order. The simplest pattern, but can introduce systematic bias.

```
self.agents.do("step")
```

### Random Activation

Agents act in a new random order each step. The most common default.

```
self.agents.shuffle_do("step")
```

### Simultaneous Activation

All agents first compute their next state, then all advance at once. This prevents
early-acting agents from influencing later ones within the same step. Classic examples
include Conway’s Game of Life and Schelling’s segregation model.

```
self.agents.do("compute_next_state")
self.agents.do("advance")
```

### Staged Activation

Agents perform multiple actions per step, in a defined sequence of stages. For example,
agents might first move, then eat, then reproduce.

```
for stage in ["move", "eat", "reproduce"]:
    self.agents.shuffle_do(stage)
```

### Type-Based Activation

In models with multiple agent types, you often want each type to act separately.
For example, predators and prey might take turns. Use `agents_by_type` to access
the AgentSet for each type:

```
for agent_type in self.agent_types:
    self.agents_by_type[agent_type].shuffle_do("step")
```

Or target specific types:

```
self.agents_by_type[Prey].shuffle_do("step")
self.agents_by_type[Predator].shuffle_do("step")
```

### Combining Patterns

The real power is in combining these patterns freely. Here’s an example that uses
staged, type-based, and conditional activation all at once:

```
class Prey(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)
        self.energy = 5

    def move(self):
        self.energy -= 1

    def eat(self):
        self.energy += self.random.randint(0, 2)

    def reproduce(self):
        if self.energy > 8:
            self.energy -= 4
            Prey(self.model)  # New prey is automatically registered

class Predator(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)
        self.energy = 10
        self.kills = 0

    def move(self):
        self.energy -= 2  # Predators use more energy

    def hunt(self):
        prey_agents = self.model.agents_by_type.get(Prey)
        if prey_agents and len(prey_agents) > 0 and self.energy > 0:
            target = self.random.choice(prey_agents)
            target.remove()
            self.energy += 5
            self.kills += 1

class EcosystemModel(mesa.Model):
    def __init__(self, n_prey=50, n_predators=5):
        super().__init__()
        Prey.create_agents(model=self, n=n_prey)
        Predator.create_agents(model=self, n=n_predators)

    def step(self):
        # Stage 1: All agents move (random order within each type)
        for agent_type in self.agent_types:
            self.agents_by_type[agent_type].shuffle_do("move")

        # Stage 2: Type-specific actions
        if Prey in self.agents_by_type:
            self.agents_by_type[Prey].shuffle_do("eat")
        if Predator in self.agents_by_type:
            self.agents_by_type[Predator].shuffle_do("hunt")

        # Stage 3: Only prey with enough energy reproduce
        if Prey in self.agents_by_type:
            fertile = self.agents_by_type[Prey].select(lambda a: a.energy > 8)
            fertile.do("reproduce")

        # Remove dead agents (energy depleted)
        dead = self.agents.select(lambda a: a.energy <= 0)
        for agent in dead:
            agent.remove()

eco = EcosystemModel(50, 5)
eco.run_for(20)

n_prey = len(eco.agents_by_type.get(Prey, []))
n_pred = len(eco.agents_by_type.get(Predator, []))
print(f"After 20 steps: {n_prey} prey, {n_pred} predators, {len(eco.agents)} total")
```

```
After 20 steps: 0 prey, 5 predators, 5 total
```

This example demonstrates several key points:

- **Staged activation**: All agents move first, then type-specific actions happen
- **Type-based activation**: Prey eat while predators hunt
- **Conditional activation**: Only fertile prey reproduce
- **Dynamic agent creation/removal**: Prey reproduce and dead agents are removed
  None of this required any special scheduler class — just `do`, `shuffle_do`, and
  `select`, composed in the order that makes sense for your model.

## Summary

| Method | Purpose | Returns |
| --- | --- | --- |
| `do(method)` | Call method on each agent (fixed order) | The AgentSet |
| `shuffle_do(method)` | Call method on each agent (random order) | The AgentSet |
| `map(method)` | Call method on each agent and collect results | List of results |
| **Key activation patterns:** |  |  |

- **Random**: `agents.shuffle_do("step")` — use this as your default
- **Sequential**: `agents.do("step")` — when order is intentional
- **Simultaneous**: `agents.do("compute")` then `agents.do("advance")`
- **Staged**: loop over stages, calling `do`/`shuffle_do` for each
- **Type-based**: use `agents_by_type[Type].shuffle_do("step")`
- **Conditional**: `agents.select(condition).do("step")`
  Combine these freely to express exactly the activation logic your model needs.

## Next Steps

Check out the [Event Scheduling & Time tutorial](3_event_scheduling.html)
to learn how to schedule events at specific times, create recurring events, and control
how your simulation progresses through time.

[Comer2014] Comer, Kenneth W. “Who Goes First? An Examination of the Impact of Activation on Outcome Behavior in AgentBased Models.” George Mason University, 2014. http://mars.gmu.edu/bitstream/handle/1920/9070/Comer\_gmu\_0883E\_10539.pdf

On this page

[Show Source](../_sources/tutorials/2_agent_activation.ipynb.txt)

---

Original source: https://mesa.readthedocs.io/latest/tutorials/2_agent_activation.html
