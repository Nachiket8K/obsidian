---
title: "example_mesa.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/example_mesa.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# example\_mesa.py

```
  1"""Example of using the workbench together with mesa."""
  2
  3# Import EMA Workbench modules
  4# Necessary packages for the model
  5import math
  6import sys
  7from enum import Enum
  8
  9import mesa
 10import networkx as nx
 11import numpy as np
 12
 13from ema_workbench import (
 14    ArrayOutcome,
 15    Constant,
 16    IntegerParameter,
 17    RealParameter,
 18    ReplicatorModel,
 19    ema_logging,
 20    perform_experiments,
 21)
 22
 23# MESA demo model "Virus on a Network", from https://github.com/projectmesa/mesa-examples/blob/d16736778fdb500a3e5e05e082b27db78673b562/examples/virus_on_network/virus_on_network/model.py
 24
 25
 26class State(Enum):
 27    """Possible states of an agent."""
 28
 29    SUSCEPTIBLE = 0
 30    INFECTED = 1
 31    RESISTANT = 2
 32
 33
 34def number_state(model, state):
 35    """Helper function."""
 36    return sum(1 for a in model.grid.agents if a.state is state)
 37
 38
 39def number_infected(model):
 40    """Helper function."""
 41    return number_state(model, State.INFECTED)
 42
 43
 44def number_susceptible(model):
 45    """Helper function."""
 46    return number_state(model, State.SUSCEPTIBLE)
 47
 48
 49def number_resistant(model):
 50    """Helper function."""
 51    return number_state(model, State.RESISTANT)
 52
 53
 54class VirusOnNetwork(mesa.Model):
 55    """A virus model with some number of agents."""
 56
 57    def __init__(
 58        self,
 59        num_nodes: int = 10,
 60        avg_node_degree: int = 3,
 61        initial_outbreak_size: int = 1,
 62        virus_spread_chance: float = 0.4,
 63        virus_check_frequency: float = 0.4,
 64        recovery_chance: float = 0.3,
 65        gain_resistance_chance: float = 0.5,
 66        rng: int | None = None,
 67    ):
 68        """Init."""
 69        super().__init__(rng=rng)
 70        self.num_nodes = num_nodes
 71        prob = avg_node_degree / self.num_nodes
 72        graph = nx.erdos_renyi_graph(n=self.num_nodes, p=prob)
 73
 74        self.grid = mesa.discrete_space.Network(graph, capacity=1, random=self.random)
 75
 76        self.initial_outbreak_size = (
 77            initial_outbreak_size if initial_outbreak_size <= num_nodes else num_nodes
 78        )
 79
 80        self.datacollector = mesa.DataCollector(
 81            {
 82                "Infected": number_infected,
 83                "Susceptible": number_susceptible,
 84                "Resistant": number_resistant,
 85            }
 86        )
 87
 88        # Create agents
 89        VirusAgent.create_agents(
 90            self,
 91            num_nodes,
 92            State.SUSCEPTIBLE,
 93            virus_spread_chance,
 94            virus_check_frequency,
 95            recovery_chance,
 96            gain_resistance_chance,
 97            list(self.grid.all_cells),
 98        )
 99
100        # Infect some nodes
101        infected_nodes = mesa.discrete_space.CellCollection(
102            self.random.sample(list(self.grid.all_cells), self.initial_outbreak_size),
103            random=self.random,
104        )
105        for a in infected_nodes.agents:
106            a.state = State.INFECTED
107
108        self.running = True
109        self.datacollector.collect(self)
110
111    def resistant_susceptible_ratio(self):
112        """Calculate ratio of resistant to susceptible."""
113        try:
114            return number_state(self, State.RESISTANT) / number_state(
115                self, State.SUSCEPTIBLE
116            )
117        except ZeroDivisionError:
118            return math.inf
119
120    def step(self):
121        """A single step of the model."""
122        # collect data
123        self.agents.shuffle_do("step")
124        self.datacollector.collect(self)
125
126    def run_model(self, n):
127        """Run the model for n steps."""
128        for _ in range(n):
129            self.step()
130
131
132class VirusAgent(mesa.discrete_space.FixedAgent):
133    """A VirusAgent."""
134
135    def __init__(
136        self,
137        model,
138        initial_state,
139        virus_spread_chance,
140        virus_check_frequency,
141        recovery_chance,
142        gain_resistance_chance,
143        cell,
144    ):
145        """Init."""
146        super().__init__(model)
147
148        self.state = initial_state
149
150        self.virus_spread_chance = virus_spread_chance
151        self.virus_check_frequency = virus_check_frequency
152        self.recovery_chance = recovery_chance
153        self.gain_resistance_chance = gain_resistance_chance
154        self.cell = cell
155
156    def try_infect_neighbors(self):
157        """Try to infect neighbors."""
158        for agent in self.cell.neighborhood.agents:
159            if (agent.state is State.SUSCEPTIBLE) and (
160                self.random.random() < self.virus_spread_chance
161            ):
162                agent.state = State.INFECTED
163
164    def try_gain_resistance(self):
165        """Try to gain resistance."""
166        if self.random.random() < self.gain_resistance_chance:
167            self.state = State.RESISTANT
168
169    def try_remove_infection(self):
170        """Try to remove infection."""
171        # Try to remove
172        if self.random.random() < self.recovery_chance:
173            # Success
174            self.state = State.SUSCEPTIBLE
175            self.try_gain_resistance()
176        else:
177            # Failed
178            self.state = State.INFECTED
179
180    def check_situation(self):
181        """Check if the agent is infected and if so, see if she is cured."""
182        if (self.random.random() < self.virus_check_frequency) and (
183            self.state is State.INFECTED
184        ):
185            self.try_remove_infection()
186
187    def step(self):
188        """A single step of the model."""
189        if self.state is State.INFECTED:
190            self.try_infect_neighbors()
191        self.check_situation()
192
193
194# Setting up the model as a function
195def model_virus_on_network(
196    num_nodes=1,
197    avg_node_degree=1,
198    initial_outbreak_size=1,
199    virus_spread_chance=1,
200    virus_check_frequency=1,
201    recovery_chance=1,
202    gain_resistance_chance=1,
203    steps=10,
204    rng=None,
205):
206    """Run the model once."""
207    # Initialising the model
208    virus_on_network = VirusOnNetwork(
209        num_nodes=num_nodes,
210        avg_node_degree=avg_node_degree,
211        initial_outbreak_size=initial_outbreak_size,
212        virus_spread_chance=virus_spread_chance,
213        virus_check_frequency=virus_check_frequency,
214        recovery_chance=recovery_chance,
215        gain_resistance_chance=gain_resistance_chance,
216        rng=rng,
217    )
218
219    # Run the model steps times
220    virus_on_network.run_model(steps)
221
222    # Get model outcomes
223    outcomes = virus_on_network.datacollector.get_model_vars_dataframe()
224
225    # Return model outcomes
226    return {
227        "Infected": outcomes["Infected"].tolist(),
228        "Susceptible": outcomes["Susceptible"].tolist(),
229        "Resistant": outcomes["Resistant"].tolist(),
230    }
231
232
233if __name__ == "__main__":
234    # Initialize logger to keep track of experiments run
235    ema_logging.log_to_stderr(ema_logging.INFO)
236
237    # Instantiate and pass the model
238    model = ReplicatorModel("VirusOnNetwork", function=model_virus_on_network)
239
240    # Define model parameters and their ranges to be sampled
241    model.uncertainties = [
242        IntegerParameter("num_nodes", 10, 100),
243        IntegerParameter("avg_node_degree", 2, 8),
244        RealParameter("virus_spread_chance", 0.1, 1),
245        RealParameter("virus_check_frequency", 0.1, 1),
246        RealParameter("recovery_chance", 0.1, 1),
247        RealParameter("gain_resistance_chance", 0.1, 1),
248    ]
249
250    # Define model parameters that will remain constant
251    model.constants = [Constant("initial_outbreak_size", 1), Constant("steps", 30)]
252
253    # Define model outcomes
254    model.outcomes = [
255        ArrayOutcome("Infected"),
256        ArrayOutcome("Susceptible"),
257        ArrayOutcome("Resistant"),
258    ]
259
260    # Define the number of replications and the seed for each of then
261    n_replications = 10
262    model.replications = [
263        {"rng": i}
264        for i in np.random.default_rng().integers(sys.maxsize, size=n_replications)
265    ]
266
267    # Run experiments with the aforementioned parameters and outputs
268    experiments, outcomes = perform_experiments(models=model, scenarios=20)
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/example_mesa.html
