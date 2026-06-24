---
title: "Visualization - Property Layer Visualization"
source: "https://mesa.readthedocs.io/latest/tutorials/9_visualization_property_layer_visualization.html"
imported_from: "Python library documentation"
library: "Mesa"
---

# Visualization - Property Layer Visualization

## The Boltzmann Wealth Model

If you want to get straight to the tutorial checkout these environment providers:  
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/mesa/mesa/main?labpath=docs%2Ftutorials%2F9_visualization_property_layer_visualization.ipynb) (This can take 30 seconds to 5 minutes to load)

Due to conflict with Colab and Solara there are no colab links for this tutorial

*If you are running locally, please ensure you have the latest Mesa version installed.*

## Tutorial Description

This tutorial builds upon the [Visualization Rendering with SpaceRenderer](8_visualization_rendering_with_space_renderer.html) tutorial. We will explore more advanced features of the SpaceRenderer to create property\_layer and their visualization.

*If you are starting here please see the [Running Your First Model tutorial](0_first_model.html) for dependency and start-up instructions*

### Import Dependencies

This includes importing of dependencies needed for the tutorial.

```
!pip install mesa solara
```

```
Requirement already satisfied: mesa in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (4.0.0a0)
Requirement already satisfied: solara in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (1.57.4)
Requirement already satisfied: numpy in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from mesa) (2.4.6)
Requirement already satisfied: pandas in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from mesa) (3.0.3)
Requirement already satisfied: scipy in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from mesa) (1.17.1)
Requirement already satisfied: tqdm in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from mesa) (4.68.2)
Requirement already satisfied: solara-server==1.57.4 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-server[dev,starlette]==1.57.4->solara) (1.57.4)
Requirement already satisfied: solara-ui==1.57.4 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-ui[all]==1.57.4->solara) (1.57.4)
Requirement already satisfied: click>=7.1.0 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (8.4.1)
Requirement already satisfied: filelock in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (3.29.4)
Requirement already satisfied: ipykernel!=7.0.0,!=7.0.1 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (7.3.0)
Requirement already satisfied: jinja2 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (3.1.6)
Requirement already satisfied: jupyter-client in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (8.9.1)
Requirement already satisfied: nbformat in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (5.10.4)
Requirement already satisfied: rich-click in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (1.9.8)
Requirement already satisfied: watchdog in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-server[dev,starlette]==1.57.4->solara) (6.0.0)
Requirement already satisfied: watchfiles in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-server[dev,starlette]==1.57.4->solara) (1.2.0)
Requirement already satisfied: starlette in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-server[dev,starlette]==1.57.4->solara) (0.52.1)
Requirement already satisfied: uvicorn in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-server[dev,starlette]==1.57.4->solara) (0.49.0)
Requirement already satisfied: websockets in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-server[dev,starlette]==1.57.4->solara) (16.0)
Requirement already satisfied: humanize in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-ui==1.57.4->solara-ui[all]==1.57.4->solara) (4.15.0)
Requirement already satisfied: ipyvue>=1.9.0 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-ui==1.57.4->solara-ui[all]==1.57.4->solara) (1.12.0)
Requirement already satisfied: ipyvuetify>=1.6.10 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-ui==1.57.4->solara-ui[all]==1.57.4->solara) (1.11.3)
Requirement already satisfied: ipywidgets>=7.7 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-ui==1.57.4->solara-ui[all]==1.57.4->solara) (8.1.8)
Requirement already satisfied: reacton>=1.9 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-ui==1.57.4->solara-ui[all]==1.57.4->solara) (1.9.1)
Requirement already satisfied: requests in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-ui==1.57.4->solara-ui[all]==1.57.4->solara) (2.34.2)
Requirement already satisfied: cachetools in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-ui[all]==1.57.4->solara) (7.1.4)
Requirement already satisfied: markdown in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-ui[all]==1.57.4->solara) (3.10.2)
Requirement already satisfied: pillow in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-ui[all]==1.57.4->solara) (12.2.0)
Requirement already satisfied: pygments in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-ui[all]==1.57.4->solara) (2.20.0)
Requirement already satisfied: pymdown-extensions in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from solara-ui[all]==1.57.4->solara) (10.21.3)
Requirement already satisfied: comm>=0.1.1 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (0.2.3)
Requirement already satisfied: debugpy>=1.6.5 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (1.8.21)
Requirement already satisfied: ipython>=7.23.1 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (9.14.1)
Requirement already satisfied: jupyter-core!=6.0.*,>=5.1 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (5.9.1)
```

```
Requirement already satisfied: matplotlib-inline>=0.1 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (0.2.2)
Requirement already satisfied: nest-asyncio2>=1.7.0 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (1.7.2)
Requirement already satisfied: packaging>=22 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (26.2)
Requirement already satisfied: psutil>=5.7 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (7.2.2)
Requirement already satisfied: pyzmq>=25 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (27.1.0)
Requirement already satisfied: tornado>=6.4.1 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (6.5.7)
Requirement already satisfied: traitlets>=5.4.0 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (5.15.1)
Requirement already satisfied: decorator>=5.1.0 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from ipython>=7.23.1->ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (5.3.1)
Requirement already satisfied: ipython-pygments-lexers>=1.0.0 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from ipython>=7.23.1->ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (1.1.1)
Requirement already satisfied: jedi>=0.18.2 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from ipython>=7.23.1->ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (0.20.0)
Requirement already satisfied: pexpect>4.6 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from ipython>=7.23.1->ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (4.9.0)
Requirement already satisfied: prompt_toolkit<3.1.0,>=3.0.41 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from ipython>=7.23.1->ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (3.0.52)
Requirement already satisfied: stack_data>=0.6.0 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from ipython>=7.23.1->ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (0.6.3)
Requirement already satisfied: wcwidth in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from prompt_toolkit<3.1.0,>=3.0.41->ipython>=7.23.1->ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (0.8.1)
Requirement already satisfied: widgetsnbextension~=4.0.14 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from ipywidgets>=7.7->solara-ui==1.57.4->solara-ui[all]==1.57.4->solara) (4.0.15)
Requirement already satisfied: jupyterlab_widgets~=3.0.15 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from ipywidgets>=7.7->solara-ui==1.57.4->solara-ui[all]==1.57.4->solara) (3.0.16)
Requirement already satisfied: parso<0.9.0,>=0.8.6 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from jedi>=0.18.2->ipython>=7.23.1->ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (0.8.7)
Requirement already satisfied: python-dateutil>=2.8.2 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from jupyter-client->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (2.9.0.post0)
Requirement already satisfied: typing-extensions>=4.13.0 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from jupyter-client->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (4.15.0)
Requirement already satisfied: platformdirs>=2.5 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from jupyter-core!=6.0.*,>=5.1->ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (4.10.0)
Requirement already satisfied: ptyprocess>=0.5 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from pexpect>4.6->ipython>=7.23.1->ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (0.7.0)
Requirement already satisfied: six>=1.5 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from python-dateutil>=2.8.2->jupyter-client->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (1.17.0)
```

```
Requirement already satisfied: executing>=1.2.0 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from stack_data>=0.6.0->ipython>=7.23.1->ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (2.2.1)
Requirement already satisfied: asttokens>=2.1.0 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from stack_data>=0.6.0->ipython>=7.23.1->ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (3.0.1)
Requirement already satisfied: pure-eval in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from stack_data>=0.6.0->ipython>=7.23.1->ipykernel!=7.0.0,!=7.0.1->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (0.2.3)
Requirement already satisfied: MarkupSafe>=2.0 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from jinja2->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (3.0.3)
Requirement already satisfied: fastjsonschema>=2.15 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from nbformat->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (2.21.2)
Requirement already satisfied: jsonschema>=2.6 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from nbformat->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (4.26.0)
Requirement already satisfied: attrs>=22.2.0 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from jsonschema>=2.6->nbformat->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (26.1.0)
Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from jsonschema>=2.6->nbformat->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (2025.9.1)
Requirement already satisfied: referencing>=0.28.4 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from jsonschema>=2.6->nbformat->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (0.37.0)
Requirement already satisfied: rpds-py>=0.25.0 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from jsonschema>=2.6->nbformat->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (2026.5.1)
```

```
Requirement already satisfied: pyyaml in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from pymdown-extensions->solara-ui[all]==1.57.4->solara) (6.0.3)
Requirement already satisfied: charset_normalizer<4,>=2 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from requests->solara-ui==1.57.4->solara-ui[all]==1.57.4->solara) (3.4.7)
Requirement already satisfied: idna<4,>=2.5 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from requests->solara-ui==1.57.4->solara-ui[all]==1.57.4->solara) (3.18)
Requirement already satisfied: urllib3<3,>=1.26 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from requests->solara-ui==1.57.4->solara-ui[all]==1.57.4->solara) (2.7.0)
Requirement already satisfied: certifi>=2023.5.7 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from requests->solara-ui==1.57.4->solara-ui[all]==1.57.4->solara) (2026.5.20)
Requirement already satisfied: rich>=12 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from rich-click->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (15.0.0)
Requirement already satisfied: markdown-it-py>=2.2.0 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from rich>=12->rich-click->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (4.2.0)
Requirement already satisfied: mdurl~=0.1 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from markdown-it-py>=2.2.0->rich>=12->rich-click->solara-server==1.57.4->solara-server[dev,starlette]==1.57.4->solara) (0.1.2)
Requirement already satisfied: anyio<5,>=3.6.2 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from starlette->solara-server[dev,starlette]==1.57.4->solara) (4.13.0)
Requirement already satisfied: h11>=0.8 in /home/docs/checkouts/readthedocs.org/user_builds/mesa/envs/latest/lib/python3.14/site-packages (from uvicorn->solara-server[dev,starlette]==1.57.4->solara) (0.16.0)
```

```
# Has multi-dimensional arrays and matrices.
# Has a large collection of mathematical functions to operate on these arrays.
import numpy as np

# Data manipulation and analysis.
import pandas as pd

# Data visualization tools.
import seaborn as sns

import mesa
from mesa.discrete_space import CellAgent, OrthogonalMooreGrid

# Check Mesa version for visualization compatibility
if mesa.__version__.startswith(("3.0", "3.1", "3.2")):
    print(
        f"⚠️  Mesa {mesa.__version__} detected. Visualization features require Mesa 3.3+"
    )
    print("To upgrade: pip install --upgrade mesa")

from mesa.visualization import SolaraViz, SpaceRenderer, make_plot_component
from mesa.visualization.components import AgentPortrayalStyle, PropertyLayerStyle
```

## Basic Model

The following is the base model we’ll use to build the dashboard. It’s an extension of the model introduced in Tutorials 0–3, with an added property\_layer called *Test* to demonstrate property\_layer visualization functionalities.

```
def compute_gini(model):
    agent_wealths = [agent.wealth for agent in model.agents]
    x = sorted(agent_wealths)
    N = model.num_agents
    B = sum(xi * (N - i) for i, xi in enumerate(x)) / (N * sum(x))
    return 1 + (1 / N) - 2 * B

class MoneyAgent(CellAgent):
    """An agent with fixed initial wealth."""

    def __init__(self, model, cell):
        """initialize a MoneyAgent instance.

        Args:
            model: A model instance
        """
        super().__init__(model)
        self.cell = cell
        self.wealth = 1

    def move(self):
        """Move the agent to a random neighboring cell."""
        self.cell = self.cell.neighborhood.select_random_cell()

    def give_money(self):
        """Give 1 unit of wealth to a random agent in the same cell."""
        cellmates = [a for a in self.cell.agents if a is not self]

        if cellmates:  # Only give money if there are other agents present
            other = self.random.choice(cellmates)
            other.wealth += 1
            self.wealth -= 1

    def step(self):
        """do one step of the agent."""
        self.move()
        if self.wealth > 0:
            self.give_money()

class MoneyModel(mesa.Model):
    """A model with some number of agents."""

    def __init__(self, n=10, width=10, height=10, rng=None):
        """Initialize a MoneyModel instance.

        Args:
            N: The number of agents.
            width: Width of the grid.
            height: Height of the grid.
        """
        super().__init__(rng=rng)
        self.num_agents = n
        self.grid = OrthogonalMooreGrid((width, height), random=self.random)

        # Add a test property with random data
        self.grid.add_property_layer(
            "test", np.random.randint(0, 10, size=(width, height))
        )

        # Create agents
        MoneyAgent.create_agents(
            self,
            self.num_agents,
            self.random.choices(self.grid.all_cells.cells, k=self.num_agents),
        )

        self.datacollector = mesa.DataCollector(
            model_reporters={"Gini": compute_gini}, agent_reporters={"Wealth": "wealth"}
        )
        self.datacollector.collect(self)

    def step(self):
        """do one step of the model"""
        self.agents.shuffle_do("step")
        self.datacollector.collect(self)
```

```
# Let's make sure the model works
model = MoneyModel(100, 10, 10)
model.run_for(20)

data = model.datacollector.get_agent_vars_dataframe()
# Use seaborn
g = sns.histplot(data["Wealth"], discrete=True)
g.set(title="Wealth distribution", xlabel="Wealth", ylabel="number of agents");
```

![../_images/a6b5ea394f93b2ba90beed911fec7b384a3bedaf6b7a23d8c402eeb45f01eb9e.png](../_images/a6b5ea394f93b2ba90beed911fec7b384a3bedaf6b7a23d8c402eeb45f01eb9e.png)

### Adding visualization

So far, we’ve built a model, run it, and analyzed some output afterwards. However, one of the advantages of agent-based models is that we can often watch them run step by step, potentially spotting unexpected patterns, behaviors or bugs, or developing new intuitions, hypotheses, or insights. Other times, watching a model run can explain it to an unfamiliar audience better than static explanations. Like many ABM frameworks, Mesa allows you to create an interactive visualization of the model. In this section we’ll walk through creating a visualization using built-in components, and (for advanced users) how to create a new visualization element.

First, a quick explanation of how Mesa’s interactive visualization works. The visualization is done in a browser window or Jupyter instance, using the [Solara](https://solara.dev/) framework, a pure Python, React-style web framework. Running `solara run app.py` will launch a web server, which runs the model, and displays model detail at each step via a plotting library. Alternatively, you can execute everything inside a Jupyter instance and display it inline.

As in the previous tutorial we instantiate the model parameters, some of which are modifiable by user inputs. In this case, the number of agents, N, is specified as a slider of integers.

```
model_params = {
    "n": {
        "type": "SliderInt",
        "value": 50,
        "label": "Number of agents:",
        "min": 10,
        "max": 100,
        "step": 1,
    },
    "width": 10,
    "height": 10,
}
```

Then just like last time we instantiate the visualization object which (by default) displays the grid containing the agents, and timeseries of values computed by the model’s data collector. In this example, we specify the Gini coefficient.

There are 3 buttons:

- the step button, which advances the model by 1 step
- the play button, which advances the model indefinitely until it is paused
- the pause button, which pauses the model

To reset the model, the order of operations are important

1. Stop the model
2. Update the parameters (e.g. move the sliders)
3. Press reset

**Additional Interactive Controls**

In addition to the basic controls (Play, Pause, Step), there are three extra interactive UI elements that give you more control over the simulation and visualization performance:

1. **Play Interval Slider**
   This slider controls the time delay (in milliseconds) between each step of the simulation when it is playing.

   - **Lower values** = faster simulation updates
   - **Higher values** = slower, more observable step-by-step updates
2. **Render Interval Slider**
   This slider determines how frequently the visualization updates, based on the number of steps.

   - For example, if set to `5`, the visualization will update only **after every 5 steps** of the model.
   - ⚠️ Note: This interval is **step-based**, not time-based.
3. **Use Threads Checkbox**
   This checkbox enables threaded execution of the model.

   - When enabled, the visualization runs on a separate thread, allowing the UI to remain responsive even during heavy computations.
   - It also ensures the visualization only updates at fixed intervals, improving performance and responsiveness during rapid simulations.

### Page Tab View

#### **Plot Components**

You can place different components (except the renderer) on separate pages according to your preference. There are no restrictions on page numbering — pages do not need to be sequential or positive. Each page acts as an independent window where components may or may not exist.

The default page is `page=0`. If pages are not sequential (e.g., `page=1` and `page=10`), the system will automatically create the 8 empty pages in between to maintain consistent indexing. To avoid empty pages in your dashboard, use sequential page numbers.

To assign a plot component to a specific page, pass the `page` keyword argument to `make_plot_component`. For example, the following will display the plot component on page 1:

```
plot_comp = make_plot_component("encoding", page=1)
```

#### **Custom Components**

In the next tutorial, you will learn how to create custom components for the Solara dashboard. If you want a custom component to appear on a specific page, you must pass it as a tuple containing the component and the page number.

```
@solara.component
def CustomComponent():
    ...

page = SolaraViz(
    model,
    renderer,
    components=[(CustomComponent, 1)]  # Custom component will appear on page 1
)
```

> ⚠️ **Warning**
> Running the model can be performance-intensive. It is strongly recommended to pause the model in the dashboard before switching pages.

## Visualizing property\_layer

> **⚠️ Important:**
> property\_layer visualization on `HexGrid` is not supported with the `altair` backend; use `matplotlib` instead.

You can visualize **property\_layer** in a way that’s very similar to how agents are visualized—by defining a custom portrayal function. Let’s call this function `property_layer_portrayal`.

Mesa provides a dedicated component for property\_layer styling, called `PropertyLayerStyle` (similar to `AgentPortrayalStyle` for agents). You can import it from `mesa.visualization.components` as shown earlier.

In `PropertyLayerStyle`, you can define:

- `color` or `colormap`: Determines how the values in the property\_layer are visualized
- `alpha`: Controls the transparency (opacity) of the property\_layer
- `colorbar`: A boolean that determines whether a colorbar is shown alongside the visualization
- `vmin` and `vmax`: The minimum and maximum data values to be visualized, controlling the color scale range, these default to the minimum and maximum values in your data respectively if not defined.

The portrayal function receives a `layer` object as an argument, just like how `agent_portrayal` receives an `agent`. If your model includes multiple property\_layer, you can conditionally adjust the visualization logic based on the its name. This allows you to apply different styles to each property\_layer as needed.

Here’s a quick example:

```
def property_layer_portrayal(layer):
    if layer == "WealthDensity":
        return PropertyLayerStyle(
            colormap="viridis",
            alpha=0.6,
            colorbar=True,
            vmin=0,
            vmax=10,
        )
    elif layer == "Temperature":
        return PropertyLayerStyle(
            colormap="coolwarm",
            alpha=0.5,
            colorbar=False,
            vmin=-1,
            vmax=1,
        )
```

This approach allows you to customize each property\_layer’s appearance independently while keeping your visualization code clean and modular.

We’ll reuse the previously defined `agent_portrayal` function and introduce a new `property_layer_portrayal` function specifically for visualizing the property\_layer.

```
def agent_portrayal(agent):
    portrayal = AgentPortrayalStyle(size=50, color="orange")
    if agent.wealth > 0:
        portrayal.update(("color", "blue"), ("size", 100))
    return portrayal

def property_layer_portrayal(layer):
    if layer == "test":
        return PropertyLayerStyle(color="blue", alpha=0.8, colorbar=True)

# Create initial model instance
money_model = MoneyModel(n=50, width=10, height=10)
```

### Drawing the property\_layer

We’ll now create a renderer and draw the grid structure, the agents and the *test* using the `matplotlib` backend.

```
%%capture

renderer = SpaceRenderer(model=money_model, backend="matplotlib")
renderer.draw_structure(lw=2, ls="solid", color="black", alpha=0.1)
renderer.draw_agents(agent_portrayal)
renderer.draw_property_layer(property_layer_portrayal)
```

You can also use `render()` function to draw property\_layer in one go.

```
%%capture

renderer = SpaceRenderer(model=money_model, backend="matplotlib")
renderer.render(
    space_kwargs={  # an alternative way to customize the grid structure
        "lw": 2,
        "ls": "solid",
        "color": "black",
        "alpha": 0.1,
    },
    agent_portrayal=agent_portrayal,
    property_layer_portrayal=property_layer_portrayal,
)
```

We’ll keep the `post_process` to make the grid look good.

```
def post_process(ax):
    """Customize the matplotlib axes after rendering."""
    ax.set_title("Boltzmann Wealth Model")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.5)
    ax.set_aspect("equal", adjustable="box")

renderer.post_process = post_process

def post_process_lines(ax):
    """Customize the matplotlib axes for the Gini line plot."""
    ax.set_title("Gini Coefficient Over Time")
    ax.set_xlabel("Time Step")
    ax.set_ylabel("Gini Coefficient")
    ax.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.5)
    ax.set_aspect("auto")

GiniPlot = make_plot_component("Gini", post_process=post_process_lines)
```

### Launching the Visualization

Now that we have the model, visual renderer, and plot components defined, we can bring everything together using `SolaraViz`:

```
page = SolaraViz(
    money_model,
    renderer,
    components=[GiniPlot],
    model_params=model_params,
    name="Boltzmann Wealth Model",
)

# This is required to render the visualization in a Jupyter notebook
page
```

```
<Figure size 640x480 with 0 Axes>
```

## Exercise

- Try removing the `post_process` and changing the backend.
- Try visualizing multiple property\_layers.

## Next Steps

Checkout this [mesa example](https://github.com/mesa/mesa/tree/main/mesa/examples/advanced/sugarscape_g1mt) to further explore the capabilities of the property\_layer.
Check out the next [visualization tutorial custom components](10_visualization_custom.html) on how to further enhance your interactive dashboard.

[Comer2014] Comer, Kenneth W. “Who Goes First? An Examination of the Impact of Activation on Outcome Behavior in AgentBased Models.” George Mason University, 2014. http://mars.gmu.edu/bitstream/handle/1920/9070/Comer\_gmu\_0883E\_10539.pdf

[Dragulescu2002] Drăgulescu, Adrian A., and Victor M. Yakovenko. “Statistical Mechanics of Money, Income, and Wealth: A Short Survey.” arXiv Preprint Cond-mat/0211175, 2002. http://arxiv.org/abs/cond-mat/0211175.

On this page

[Show Source](../_sources/tutorials/9_visualization_property_layer_visualization.ipynb.txt)

---

Original source: https://mesa.readthedocs.io/latest/tutorials/9_visualization_property_layer_visualization.html
