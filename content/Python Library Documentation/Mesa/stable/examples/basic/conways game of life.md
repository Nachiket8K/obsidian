---
title: "Conway’s Game Of “Life”"
source: "https://mesa.readthedocs.io/stable/examples/basic/conways_game_of_life.html"
imported_from: "Python library documentation"
library: "Mesa"
---

# Conway’s Game Of “Life”

## Summary

[The Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life), also known simply as “Life”, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.

The “game” is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input by a human. One interacts with the Game of “Life” by creating an initial configuration and observing how it evolves, or, for advanced “players”, by creating patterns with particular properties.

## How to Run

To run the model interactively, in this directory, run the following command

```
    $ solara run app.py
```

## Files

- `agents.py`: Defines the behavior of an individual cell, which can be in two states: DEAD or ALIVE.
- `model.py`: Defines the model itself, initialized with a random configuration of alive and dead cells.
- `app.py`: Defines an interactive visualization using solara.
- `st_app.py`: Defines an interactive visualization using Streamlit.

## Optional

- For the streamlit version, you need to have streamlit installed (can be done via pip install streamlit)

## Further Reading

[Conway’s Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)

## Agents

```
from mesa.discrete_space import FixedAgent

class Cell(FixedAgent):
    """Represents a single ALIVE or DEAD cell in the simulation."""

    DEAD = 0
    ALIVE = 1

    @property
    def x(self):
        return self.cell.coordinate[0]

    @property
    def y(self):
        return self.cell.coordinate[1]

    def __init__(self, model, cell, init_state=DEAD):
        """Create a cell, in the given state, at the given x, y position."""
        super().__init__(model)
        self.cell = cell
        self.state = init_state
        self._next_state = None

    @property
    def is_alive(self):
        return self.state == self.ALIVE

    @property
    def neighbors(self):
        return self.cell.neighborhood.agents

    def determine_state(self):
        """Compute if the cell will be dead or alive at the next tick.  This is
        based on the number of alive or dead neighbors.  The state is not
        changed here, but is just computed and stored in self._nextState,
        because our current state may still be necessary for our neighbors
        to calculate their next state.
        """
        # Get the neighbors and apply the rules on whether to be alive or dead
        # at the next tick.
        live_neighbors = sum(neighbor.is_alive for neighbor in self.neighbors)

        # Assume nextState is unchanged, unless changed below.
        self._next_state = self.state
        if self.is_alive:
            if live_neighbors < 2 or live_neighbors > 3:
                self._next_state = self.DEAD
        else:
            if live_neighbors == 3:
                self._next_state = self.ALIVE

    def assume_state(self):
        """Set the state to the new computed state -- computed in step()."""
        self.state = self._next_state
```

## Model

```
from mesa import Model
from mesa.discrete_space import OrthogonalMooreGrid
from mesa.examples.basic.conways_game_of_life.agents import Cell

class ConwaysGameOfLife(Model):
    """Represents the 2-dimensional array of cells in Conway's Game of Life."""

    def __init__(self, width=50, height=50, initial_fraction_alive=0.2, rng=None):
        """Create a new playing area of (width, height) cells."""
        super().__init__(rng=rng)
        # Use a simple grid, where edges wrap around.
        self.grid = OrthogonalMooreGrid(
            (width, height), capacity=1, random=self.random, torus=True
        )

        # Place a cell at each location, with some initialized to
        # ALIVE and some to DEAD.
        for cell in self.grid.all_cells:
            Cell(
                self,
                cell,
                init_state=Cell.ALIVE
                if self.random.random() < initial_fraction_alive
                else Cell.DEAD,
            )

        self.running = True

    def step(self):
        """Perform the model step in two stages:
        - First, all cells assume their next state (whether they will be dead or alive)
        - Then, all cells change state to their next state.
        """
        self.agents.do("determine_state")
        self.agents.do("assume_state")
```

## App

```
from mesa.examples.basic.conways_game_of_life.model import ConwaysGameOfLife
from mesa.visualization import (
    SolaraViz,
    SpaceRenderer,
)
from mesa.visualization.components import AgentPortrayalStyle

def agent_portrayal(agent):
    return AgentPortrayalStyle(
        color="white" if agent.state == 0 else "black",
        marker="s",
        size=30,
    )

def post_process(ax):
    ax.set_aspect("equal")
    ax.set_xticks([])
    ax.set_yticks([])

model_params = {
    "rng": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed",
    },
    "width": {
        "type": "SliderInt",
        "value": 50,
        "label": "Width",
        "min": 5,
        "max": 60,
        "step": 1,
    },
    "height": {
        "type": "SliderInt",
        "value": 50,
        "label": "Height",
        "min": 5,
        "max": 60,
        "step": 1,
    },
    "initial_fraction_alive": {
        "type": "SliderFloat",
        "value": 0.2,
        "label": "Cells initially alive",
        "min": 0,
        "max": 1,
        "step": 0.01,
    },
}

# Create initial model instance
model1 = ConwaysGameOfLife()

renderer = SpaceRenderer(model1, backend="matplotlib").setup_agents(agent_portrayal)
# In this case the renderer only draws the agents because we just want to observe
# the state of the agents, not the structure of the grid.
renderer.draw_agents()
renderer.post_process = post_process

# Create the SolaraViz page. This will automatically create a server and display the
# visualization elements in a web browser.
# Display it using the following command in the example directory:
# solara run app.py
# It will automatically update and display any changes made to this file
page = SolaraViz(
    model1,
    renderer,
    model_params=model_params,
    name="Game of Life",
)
page  # noqa
```

On this page

### This Page

- [Show Source](../../_sources/examples/basic/conways_game_of_life.md.txt)

---

Original source: https://mesa.readthedocs.io/stable/examples/basic/conways_game_of_life.html
