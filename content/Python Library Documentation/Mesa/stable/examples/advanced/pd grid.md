---
title: "Demographic Prisoner’s Dilemma on a Grid"
source: "https://mesa.readthedocs.io/stable/examples/advanced/pd_grid.html"
imported_from: "Python library documentation"
library: "Mesa"
---

# Demographic Prisoner’s Dilemma on a Grid

## Summary

The Demographic Prisoner’s Dilemma is a family of variants on the classic two-player [Prisoner’s Dilemma]. The model consists of agents, each with a strategy of either Cooperate or Defect. Each agent’s payoff is based on its strategy and the strategies of its spatial neighbors. After each step of the model, the agents adopt the strategy of their neighbor with the highest total score.

The model payoff table is:

|  | Cooperate | Defect |
| --- | --- | --- |
| **Cooperate** | 1, 1 | 0, D |
| **Defect** | D, 0 | 0, 0 |

Where *D* is the defection bonus, generally set higher than 1. In these runs, the defection bonus is set to $D=1.6$.

The Demographic Prisoner’s Dilemma demonstrates how simple rules can lead to the emergence of widespread cooperation, despite the Defection strategy dominating each individual interaction game. However, it is also interesting for another reason: it is known to be sensitive to the activation regime employed in it.

## How to Run

To run the model interactively, in this directory, run the following command

```
    $ solara run app.py
```

## Files

- `agents.py`: contains the agent class.
- `model.py`: contains the model class; the model takes a `activation_order` string as an argument, which determines in which order agents are activated: Sequential, Random or Simultaneous.
- `app.py`: contains the interactive visualization server.
- `Demographic Prisoner's Dilemma Activation Schedule.ipynb`: Jupyter Notebook for running the scheduling experiment. This runs the model three times, one for each activation type, and demonstrates how the activation regime drives the model to different outcomes.

## Further Reading

This model is adapted from:

Wilensky, U. (2002). NetLogo PD Basic Evolutionary model. http://ccl.northwestern.edu/netlogo/models/PDBasicEvolutionary. Center for Connected Learning and Computer-Based Modeling, Northwestern University, Evanston, IL.

The Demographic Prisoner’s Dilemma originates from:

[Epstein, J. Zones of Cooperation in Demographic Prisoner’s Dilemma. 1998.](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.8.8629&amp;rep=rep1&amp;type=pdf)

## Agents

```
from mesa.discrete_space import CellAgent

class PDAgent(CellAgent):
    """Agent member of the iterated, spatial prisoner's dilemma model."""

    def __init__(self, model, starting_move=None, cell=None):
        """
        Create a new Prisoner's Dilemma agent.

        Args:
            model: model instance
            starting_move: If provided, determines the agent's initial state:
                           C(ooperating) or D(efecting). Otherwise, random.
        """
        super().__init__(model)
        self.score = 0
        self.cell = cell
        if starting_move:
            self.move = starting_move
        else:
            self.move = self.random.choice(["C", "D"])
        self.next_move = None

    @property
    def is_cooroperating(self):
        return self.move == "C"

    def step(self):
        """Get the best neighbor's move, and change own move accordingly
        if better than own score."""

        # neighbors = self.model.grid.get_neighbors(self.pos, True, include_center=True)
        neighbors = [*list(self.cell.neighborhood.agents), self]
        best_neighbor = max(neighbors, key=lambda a: a.score)
        self.next_move = best_neighbor.move

    def advance(self):
        self.move = self.next_move
        self.score += self.increment_score()

    def increment_score(self):
        neighbors = self.cell.neighborhood.agents
        if self.model.activation_order == "Simultaneous":
            moves = [neighbor.next_move for neighbor in neighbors]
        else:
            moves = [neighbor.move for neighbor in neighbors]
        return sum(self.model.payoff[(self.move, move)] for move in moves)
```

## Model

```
import typing

import mesa
from mesa.discrete_space import OrthogonalMooreGrid
from mesa.examples.advanced.pd_grid.agents import PDAgent

class PdGrid(mesa.Model):
    """Model class for iterated, spatial prisoner's dilemma model."""

    activation_regimes: typing.ClassVar[list[str]] = [
        "Sequential",
        "Random",
        "Simultaneous",
    ]

    # This dictionary holds the payoff for this agent,
    # keyed on: (my_move, other_move)

    payoff: typing.ClassVar[dict[tuple[str, str], float]] = {
        ("C", "C"): 1,
        ("C", "D"): 0,
        ("D", "C"): 1.6,
        ("D", "D"): 0,
    }

    def __init__(
        self, width=50, height=50, activation_order="Random", payoffs=None, rng=None
    ):
        """
        Create a new Spatial Prisoners' Dilemma Model.

        Args:
            width, height: Grid size. There will be one agent per grid cell.
            activation_order: Can be "Sequential", "Random", or "Simultaneous".
                           Determines the agent activation regime.
            payoffs: (optional) Dictionary of (move, neighbor_move) payoffs.
        """
        super().__init__(rng=rng)
        self.activation_order = activation_order
        self.grid = OrthogonalMooreGrid((width, height), torus=True, random=self.random)

        if payoffs is not None:
            self.payoff = payoffs

        PDAgent.create_agents(
            self, len(self.grid.all_cells.cells), cell=self.grid.all_cells.cells
        )

        self.datacollector = mesa.DataCollector(
            {
                "Cooperating_Agents": lambda m: len(
                    [a for a in m.agents if a.move == "C"]
                )
            }
        )

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        # Activate all agents, based on the activation regime
        match self.activation_order:
            case "Sequential":
                self.agents.do(lambda a: (a.step(), a.advance()))
            case "Random":
                self.agents.shuffle_do(lambda a: (a.step(), a.advance()))
            case "Simultaneous":
                self.agents.do("step").do("advance")
            case _:
                raise ValueError(f"Unknown activation order: {self.activation_order}")

        # Collect data
        self.datacollector.collect(self)

    def run(self, n):
        """Run the model for n steps."""
        for _ in range(n):
            self.step()
```

## App

```
"""
Solara-based visualization for the Spatial Prisoner's Dilemma Model.
"""

from mesa.examples.advanced.pd_grid.model import PdGrid
from mesa.visualization import (
    Slider,
    SolaraViz,
    SpaceRenderer,
    make_plot_component,
)
from mesa.visualization.components import AgentPortrayalStyle

def pd_agent_portrayal(agent):
    """
    Portrayal function for rendering PD agents in the visualization.
    """
    return AgentPortrayalStyle(
        color="blue" if agent.move == "C" else "red", marker="s", size=25
    )

# Model parameters
model_params = {
    "rng": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed",
    },
    "width": Slider("Grid Width", value=50, min=10, max=100, step=1),
    "height": Slider("Grid Height", value=50, min=10, max=100, step=1),
    "activation_order": {
        "type": "Select",
        "value": "Random",
        "values": PdGrid.activation_regimes,
        "label": "Activation Regime",
    },
}

# Create plot for tracking cooperating agents over time
plot_component = make_plot_component("Cooperating_Agents", backend="altair", grid=True)

# Initialize model
initial_model = PdGrid()
# Create grid and agent visualization component using Altair
renderer = (
    SpaceRenderer(initial_model, backend="altair")
    .setup_agents(pd_agent_portrayal)
    .render()
)

# Create visualization with all components
page = SolaraViz(
    model=initial_model,
    renderer=renderer,
    components=[plot_component],
    model_params=model_params,
    name="Spatial Prisoner's Dilemma",
)
page  # noqa B018
```

On this page

### This Page

- [Show Source](../../_sources/examples/advanced/pd_grid.md.txt)

---

Original source: https://mesa.readthedocs.io/stable/examples/advanced/pd_grid.html
