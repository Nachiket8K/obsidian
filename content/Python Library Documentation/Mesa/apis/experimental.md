---
title: "Experimental"
source: "https://mesa.readthedocs.io/latest/apis/experimental.html"
imported_from: "Python library documentation"
library: "Mesa"
---

# Experimental

This namespace contains experimental features. These are under development, and their API is not necessarily stable.

## Continuous Space

A Continuous Space class.

class ContinuousSpace(*dimensions: ArrayLike*, *torus: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *random: [Random](https://docs.python.org/3/library/random.html#random.Random "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *n\_agents: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 100*)[[source]](../_modules/experimental/continuous_space/continuous_space.html#ContinuousSpace)
:   Continuous space where each agent can have an arbitrary position.

    Create a new continuous space.

    Parameters:
    :   - **dimensions** – a numpy array like object where each row specifies the minimum and maximum value of that dimension.
        - **torus** – boolean for whether the space wraps around or not
        - **random** – a seeded stdlib random.Random instance
        - **n\_agents** – the expected number of agents in the space

    Internally, a numpy array is used to store the positions of all agents. This is resized if needed,
    but you can control the initial size explicitly by passing n\_agents.

    property agents: [AgentSet](agentset.html#mesa.agentset.AgentSet "mesa.agentset.AgentSet")
    :   Return an AgentSet with the agents in the space.

    calculate\_difference\_vector(*point: ndarray*, *agents=None*) → ndarray[[source]](../_modules/experimental/continuous_space/continuous_space.html#ContinuousSpace.calculate_difference_vector)
    :   Calculate the difference vector between the point and all agenents.

        Parameters:
        :   - **point** – the point to calculate the difference vector for
            - **agents** – the agents to calculate the difference vector of point with. By default,
              all agents are considered.

    calculate\_distances(*point: ArrayLike*, *agents: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*kwargs*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[ndarray, [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")][[source]](../_modules/experimental/continuous_space/continuous_space.html#ContinuousSpace.calculate_distances)
    :   Calculate the distance between the point and all agents.

        Parameters:
        :   - **point** – the point to calculate the difference vector for
            - **agents** – the agents to calculate the difference vector of point with. By default,
              all agents are considered.
            - **kwargs** – any additional keyword arguments are passed to scipy’s cdist, which is used
              only if torus is False. This allows for non-Euclidian distance measures.

    get\_agents\_in\_radius(*point: ArrayLike*, *radius: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"), ndarray][[source]](../_modules/experimental/continuous_space/continuous_space.html#ContinuousSpace.get_agents_in_radius)
    :   Return the agents and their distances within a radius for the point.

    get\_k\_nearest\_agents(*point: ArrayLike*, *k: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"), ndarray][[source]](../_modules/experimental/continuous_space/continuous_space.html#ContinuousSpace.get_k_nearest_agents)
    :   Return the k nearest agents and their distances to the point.

        Notes

        This method returns exactly k agents, ignoring ties. In case of ties, the
        earlier an agent is inserted the higher it will rank.

        If fewer than k agents are present in the space, all agents are returned
        and a UserWarning is emitted to indicate that the requested k could not be
        satisfied. If the space is empty or k <= 0, an empty result is returned
        without a warning.

    in\_bounds(*point: ArrayLike*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/experimental/continuous_space/continuous_space.html#ContinuousSpace.in_bounds)
    :   Check if point is inside the bounds of the space.

    torus\_correct(*point: ArrayLike*) → ndarray[[source]](../_modules/experimental/continuous_space/continuous_space.html#ContinuousSpace.torus_correct)
    :   Apply a torus correction to the point.

Continuous space agents.

class HasPositionProtocol(*\*args*, *\*\*kwargs*)[[source]](../_modules/experimental/continuous_space/continuous_space_agents.html#HasPositionProtocol)
:   Protocol for continuous space position holders.

class ContinuousSpaceAgent(*space: ContinuousSpace*, *model*)[[source]](../_modules/experimental/continuous_space/continuous_space_agents.html#ContinuousSpaceAgent)
:   A continuous space agent.

    space
    :   the continuous space in which the agent is located

        Type:
        :   [ContinuousSpace](#experimental.continuous_space.continuous_space.ContinuousSpace "experimental.continuous_space.continuous_space.ContinuousSpace")

    position
    :   the position of the agent

        Type:
        :   np.ndarray

    Initialize a continuous space agent.

    Parameters:
    :   - **space** – the continuous space in which the agent is located
        - **model** – the model to which the agent belongs

    property position: ndarray
    :   Position of the agent.

    remove() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/experimental/continuous_space/continuous_space_agents.html#ContinuousSpaceAgent.remove)
    :   Remove and delete the agent from the model and continuous space.

    get\_neighbors\_in\_radius(*radius: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"), ndarray][[source]](../_modules/experimental/continuous_space/continuous_space_agents.html#ContinuousSpaceAgent.get_neighbors_in_radius)
    :   Get neighbors within radius.

        Parameters:
        :   **radius** – radius within which to look for neighbors

    get\_nearest\_neighbors(*k: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"), ndarray][[source]](../_modules/experimental/continuous_space/continuous_space_agents.html#ContinuousSpaceAgent.get_nearest_neighbors)
    :   Get neighbors within radius.

        Parameters:
        :   **k** – the number of nearest neighbors to return

## Continuous Space

A Continuous Space class.

class ContinuousSpace(*dimensions: ArrayLike*, *torus: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *random: [Random](https://docs.python.org/3/library/random.html#random.Random "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *n\_agents: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 100*)[[source]](../_modules/experimental/continuous_space/continuous_space.html#ContinuousSpace)
:   Continuous space where each agent can have an arbitrary position.

    Create a new continuous space.

    Parameters:
    :   - **dimensions** – a numpy array like object where each row specifies the minimum and maximum value of that dimension.
        - **torus** – boolean for whether the space wraps around or not
        - **random** – a seeded stdlib random.Random instance
        - **n\_agents** – the expected number of agents in the space

    Internally, a numpy array is used to store the positions of all agents. This is resized if needed,
    but you can control the initial size explicitly by passing n\_agents.

    property agents: [AgentSet](agentset.html#mesa.agentset.AgentSet "mesa.agentset.AgentSet")
    :   Return an AgentSet with the agents in the space.

    calculate\_difference\_vector(*point: ndarray*, *agents=None*) → ndarray[[source]](../_modules/experimental/continuous_space/continuous_space.html#ContinuousSpace.calculate_difference_vector)
    :   Calculate the difference vector between the point and all agenents.

        Parameters:
        :   - **point** – the point to calculate the difference vector for
            - **agents** – the agents to calculate the difference vector of point with. By default,
              all agents are considered.

    calculate\_distances(*point: ArrayLike*, *agents: [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*kwargs*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[ndarray, [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")][[source]](../_modules/experimental/continuous_space/continuous_space.html#ContinuousSpace.calculate_distances)
    :   Calculate the distance between the point and all agents.

        Parameters:
        :   - **point** – the point to calculate the difference vector for
            - **agents** – the agents to calculate the difference vector of point with. By default,
              all agents are considered.
            - **kwargs** – any additional keyword arguments are passed to scipy’s cdist, which is used
              only if torus is False. This allows for non-Euclidian distance measures.

    get\_agents\_in\_radius(*point: ArrayLike*, *radius: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"), ndarray][[source]](../_modules/experimental/continuous_space/continuous_space.html#ContinuousSpace.get_agents_in_radius)
    :   Return the agents and their distances within a radius for the point.

    get\_k\_nearest\_agents(*point: ArrayLike*, *k: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"), ndarray][[source]](../_modules/experimental/continuous_space/continuous_space.html#ContinuousSpace.get_k_nearest_agents)
    :   Return the k nearest agents and their distances to the point.

        Notes

        This method returns exactly k agents, ignoring ties. In case of ties, the
        earlier an agent is inserted the higher it will rank.

        If fewer than k agents are present in the space, all agents are returned
        and a UserWarning is emitted to indicate that the requested k could not be
        satisfied. If the space is empty or k <= 0, an empty result is returned
        without a warning.

    in\_bounds(*point: ArrayLike*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/experimental/continuous_space/continuous_space.html#ContinuousSpace.in_bounds)
    :   Check if point is inside the bounds of the space.

    torus\_correct(*point: ArrayLike*) → ndarray[[source]](../_modules/experimental/continuous_space/continuous_space.html#ContinuousSpace.torus_correct)
    :   Apply a torus correction to the point.

Continuous space agents.

class HasPositionProtocol(*\*args*, *\*\*kwargs*)[[source]](../_modules/experimental/continuous_space/continuous_space_agents.html#HasPositionProtocol)
:   Protocol for continuous space position holders.

class ContinuousSpaceAgent(*space: ContinuousSpace*, *model*)[[source]](../_modules/experimental/continuous_space/continuous_space_agents.html#ContinuousSpaceAgent)
:   A continuous space agent.

    space
    :   the continuous space in which the agent is located

        Type:
        :   [ContinuousSpace](#experimental.continuous_space.continuous_space.ContinuousSpace "experimental.continuous_space.continuous_space.ContinuousSpace")

    position
    :   the position of the agent

        Type:
        :   np.ndarray

    Initialize a continuous space agent.

    Parameters:
    :   - **space** – the continuous space in which the agent is located
        - **model** – the model to which the agent belongs

    property position: ndarray
    :   Position of the agent.

    remove() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/experimental/continuous_space/continuous_space_agents.html#ContinuousSpaceAgent.remove)
    :   Remove and delete the agent from the model and continuous space.

    get\_neighbors\_in\_radius(*radius: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"), ndarray][[source]](../_modules/experimental/continuous_space/continuous_space_agents.html#ContinuousSpaceAgent.get_neighbors_in_radius)
    :   Get neighbors within radius.

        Parameters:
        :   **radius** – radius within which to look for neighbors

    get\_nearest\_neighbors(*k: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)"), ndarray][[source]](../_modules/experimental/continuous_space/continuous_space_agents.html#ContinuousSpaceAgent.get_nearest_neighbors)
    :   Get neighbors within radius.

        Parameters:
        :   **k** – the number of nearest neighbors to return

## Scenarios

Base Scenario class.

rescale\_samples(*samples: ndarray*, *ranges: ndarray*, *\**, *inplace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → ndarray[[source]](../_modules/experimental/scenarios/scenario.html#rescale_samples)
:   Rescale samples from the unit interval [0, 1] to parameter ranges.

    Parameters:
    :   - **samples** (*ndarray* *(**n**,* *d**)*) – Samples drawn from the unit interval.
        - **ranges** (*ndarray* *(**d**,* *2**)*) – Parameter ranges given as [[min, max], …].
        - **inplace** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) – If True, the input `samples` array is modified in place.
          If False (default), a new array containing the rescaled samples
          is returned.
        - **Returns**
        - **-------**
        - **(****n** (*ndarray*) – Rescaled samples.
        - **d****)** – Rescaled samples.
        - **Notes**
        - **-----**
        - **inplace=True** (*The rescaling is performed using NumPy broadcasting. If*)

    :param :
    :param the original `samples` array is overwritten.:

class Scenario(*\**, *rng: Generator | BitGenerator | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | integer | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | SeedSequence | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *scenario\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *replication\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*kwargs*)[[source]](../_modules/experimental/scenarios/scenario.html#Scenario)
:   A Scenario class for defining model parameters and experiments.

    Supports both simple instantiation and type-hinted subclassing:

    > # Simple usage
    > scenario = Scenario(rng=42, density=0.8, minority\_pc=0.5)
    >
    > # Type-hinted subclass (recommended for complex models)
    > class MyScenario(Scenario):
    >
    > > citizen\_density: float = 0.7
    > > cop\_vision: int = 7
    > > movement: bool = True
    >
    > scenario = MyScenario(rng=42, cop\_vision=10) # Override defaults

    scenario\_id
    :   A unique identifier for this scenario, auto-generated starting from 0

    experiment\_id
    :   Identifies the design point (e.g., row in a QMC sample matrix)

    replication\_id
    :   Identifies the stochastic replication within a design point

    rng
    :   Random number generator seed value

    Notes

    All parameters are accessible via attribute access (scenario.param).
    Class-level attributes in subclasses serve as default values.
    Scenario instances are frozen after initialisation; parameters cannot be modified.
    To create replications with derived seeds, use replicate().

    Initialize a Scenario.

    Parameters:
    :   - **rng** – Seed for the random number generator. Accepts any value accepted by
          numpy.random.default\_rng(). scenario.rng is always a Generator after
          initialisation. The initial rng state is stored in scenario.initial\_rng\_state
          and used by spawn\_replications() to derive child seeds.
        - **scenario\_id** – Index of the design point in the experiment matrix.
        - **replication\_id** – Index of the stochastic replication for this design point.
        - **\*\*kwargs** – All other scenario parameters (override class-level defaults).

    to\_dict() → [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")][[source]](../_modules/experimental/scenarios/scenario.html#Scenario.to_dict)
    :   Return dict representation of the scenario.

    spawn\_replications(*n: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Scenario](#experimental.scenarios.scenario.Scenario "experimental.scenarios.scenario.Scenario")][[source]](../_modules/experimental/scenarios/scenario.html#Scenario.spawn_replications)
    :   Spawn n replications of this scenario with deterministically derived seeds.

        Each replication has identical user provided parameters but a unique random number generator and replication\_id.
        The rng is spawned from the original rng of the base scenario instance.

        Parameters:
        :   **n** – Number of replications to create.

        Returns:
        :   A list of n Scenario instances with replication\_id 0..n-1.

    classmethod from\_dataframe(*experiments: DataFrame*, *\**, *rng: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | integer | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | SeedSequence | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *replications: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Scenario](#experimental.scenarios.scenario.Scenario "experimental.scenarios.scenario.Scenario")][[source]](../_modules/experimental/scenarios/scenario.html#Scenario.from_dataframe)
    :   Turn a dataframe into a list of scenarios.

        Parameters:
        :   - **experiments** – Dataframe containing the parameters for the scenarios.
            - **rng** – the number of random seeds to use or a list of seeds.
            - **replications** – the number of replications to create for each scenario

        Returns:
        :   a list of scenario instances

        If rng is an integer, numpy will be used to generate that many seed values.

    classmethod from\_ndarray(*experiments: ndarray*, *parameter\_names: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *\**, *rng: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | integer | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | SeedSequence | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *replications: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Scenario](#experimental.scenarios.scenario.Scenario "experimental.scenarios.scenario.Scenario")][[source]](../_modules/experimental/scenarios/scenario.html#Scenario.from_ndarray)
    :   Turn a numpy array into a list of scenarios.

        Parameters:
        :   - **experiments** – Dataframe containing the parameters for the scenarios.
            - **parameter\_names** – the names of the parameters
            - **rng** – the number of random seeds to use or a list of seeds.
            - **replications** – the number of replications to create for each scenario

        Returns:
        :   a list of scenario instances

        If rng is an integer, numpy will be used to generate that many seed values.

On this page

[Show Source](../_sources/apis/experimental.md.txt)

---

Original source: https://mesa.readthedocs.io/latest/apis/experimental.html
