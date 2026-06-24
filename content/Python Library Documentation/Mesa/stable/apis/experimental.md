---
title: "Experimental"
source: "https://mesa.readthedocs.io/stable/apis/experimental.html"
imported_from: "Python library documentation"
library: "Mesa"
---

# Experimental

This namespace contains experimental features. These are under development, and their API is not necessarily stable.

## Devs

Simulator implementations for different time advancement approaches in Mesa.

Deprecated since version 3.5.0: The Simulator, ABMSimulator, and DEVSimulator classes are deprecated
and will be removed in Mesa 4.0. Use the new public methods on Model instead:
run\_for(), run\_until(), schedule\_event(), and schedule\_recurring().
See <https://mesa.readthedocs.io/latest/migration_guide.html#replacing-simulator-classes>

This module provides simulator classes that control how simulation time advances and how
events are executed. It supports both discrete-time and continuous-time simulations through
three main classes:

- Simulator: Base class defining the core simulation control interface
- ABMSimulator: A simulator for agent-based models that combines fixed time steps with
  event scheduling. Uses integer time units and automatically schedules model.step()
- DEVSimulator: A pure discrete event simulator using floating-point time units for
  continuous time simulation

Key features:
- Flexible time units (integer or float)
- Event scheduling using absolute or relative times
- Priority-based event execution
- Support for running simulations for specific durations or until specific end times

The simulators enable Mesa models to use traditional time-step based approaches, pure
event-driven approaches, or hybrid combinations of both.

class Simulator(*time\_unit: [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")*, *start\_time: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*)[[source]](../_modules/experimental/devs/simulator.html#Simulator)
:   The Simulator controls the time advancement of the model.

    The simulator uses next event time progression to advance the simulation time, and execute the next event

    event\_list
    :   The list of events to execute

        Type:
        :   [EventList](time.html#mesa.time.EventList "mesa.time.EventList")

    time
    :   The current simulation time

        Type:
        :   [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    time\_unit
    :   The unit of the simulation time

        Type:
        :   [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")

    model
    :   The model to simulate

        Type:
        :   [Model](../mesa.html#mesa.model.Model "mesa.model.Model")

    Initialize a Simulator instance.

    Parameters:
    :   - **time\_unit** – type of the smulaiton time
        - **start\_time** – the starttime of the simulator

    property event\_list: [EventList](time.html#mesa.time.EventList "mesa.time.events.EventList")
    :   Return the event list from the model.

    property time: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")
    :   Simulator time (deprecated).

    setup(*model: [Model](../mesa.html#mesa.model.Model "mesa.model.Model")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/experimental/devs/simulator.html#Simulator.setup)
    :   Set up the simulator with the model to simulate.

        Parameters:
        :   **model** ([*Model*](../mesa.html#mesa.model.Model "mesa.model.Model")) – The model to simulate

        Raises:
        :   - **Exception if simulator.time is not equal to simulator.starttime** –
            - **Exception if event list is not empty** –

    reset()[[source]](../_modules/experimental/devs/simulator.html#Simulator.reset)
    :   Reset the simulator.

    run\_until(*end\_time: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/experimental/devs/simulator.html#Simulator.run_until)
    :   Run the simulator until the end time.

        Parameters:
        :   **end\_time** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *|* [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – The end time for stopping the simulator

        Raises:
        :   **Exception if simulator.setup****(****)** **has not yet been called** –

    run\_next\_event()[[source]](../_modules/experimental/devs/simulator.html#Simulator.run_next_event)
    :   Execute the next event.

        Raises:
        :   **Exception if simulator.setup****(****)** **has not yet been called** –

    run\_for(*time\_delta: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*)[[source]](../_modules/experimental/devs/simulator.html#Simulator.run_for)
    :   Run the simulator for the specified time delta.

        Parameters:
        :   **time\_delta** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*|* [*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The time delta. The simulator is run from the current time to the current time
            plus the time delta

        Raises:
        :   **Exception if simulator.setup****(****)** **has not yet been called** –

    schedule\_event\_now(*function: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *priority: [Priority](time.html#mesa.time.Priority "mesa.time.events.Priority") = Priority.DEFAULT*, *function\_args: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *function\_kwargs: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Event](time.html#mesa.time.Event "mesa.time.events.Event")[[source]](../_modules/experimental/devs/simulator.html#Simulator.schedule_event_now)
    :   Schedule event for the current time instant.

        Parameters:
        :   - **function** (*Callable*) – The callable to execute for this event
            - **priority** ([*Priority*](time.html#mesa.time.Priority "mesa.time.Priority")) – the priority of the event, optional
            - **function\_args** (*List**[**Any**]*) – list of arguments for function
            - **function\_kwargs** (*Dict**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *Any**]*) – dict of keyword arguments for function

        Returns:
        :   the simulation event that is scheduled

        Return type:
        :   [Event](time.html#mesa.time.Event "mesa.time.Event")

    schedule\_event\_absolute(*function: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *time: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *priority: [Priority](time.html#mesa.time.Priority "mesa.time.events.Priority") = Priority.DEFAULT*, *function\_args: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *function\_kwargs: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Event](time.html#mesa.time.Event "mesa.time.events.Event")[[source]](../_modules/experimental/devs/simulator.html#Simulator.schedule_event_absolute)
    :   Schedule event for the specified time instant.

        Parameters:
        :   - **function** (*Callable*) – The callable to execute for this event
            - **time** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *|* [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – the time for which to schedule the event
            - **priority** ([*Priority*](time.html#mesa.time.Priority "mesa.time.Priority")) – the priority of the event, optional
            - **function\_args** (*List**[**Any**]*) – list of arguments for function
            - **function\_kwargs** (*Dict**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *Any**]*) – dict of keyword arguments for function

        Returns:
        :   the simulation event that is scheduled

        Return type:
        :   [Event](time.html#mesa.time.Event "mesa.time.Event")

    schedule\_event\_relative(*function: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *time\_delta: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *priority: [Priority](time.html#mesa.time.Priority "mesa.time.events.Priority") = Priority.DEFAULT*, *function\_args: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *function\_kwargs: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Event](time.html#mesa.time.Event "mesa.time.events.Event")[[source]](../_modules/experimental/devs/simulator.html#Simulator.schedule_event_relative)
    :   Schedule event for the current time plus the time delta.

        Parameters:
        :   - **function** (*Callable*) – The callable to execute for this event
            - **time\_delta** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *|* [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – the time delta
            - **priority** ([*Priority*](time.html#mesa.time.Priority "mesa.time.Priority")) – the priority of the event, optional
            - **function\_args** (*List**[**Any**]*) – list of arguments for function
            - **function\_kwargs** (*Dict**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *Any**]*) – dict of keyword arguments for function

        Returns:
        :   the simulation event that is scheduled

        Return type:
        :   [Event](time.html#mesa.time.Event "mesa.time.Event")

    cancel\_event(*event: [Event](time.html#mesa.time.Event "mesa.time.events.Event")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/experimental/devs/simulator.html#Simulator.cancel_event)
    :   Remove the event from the event list.

        Parameters:
        :   **event** ([*Event*](time.html#mesa.time.Event "mesa.time.Event")) – The simulation event to remove

class ABMSimulator[[source]](../_modules/experimental/devs/simulator.html#ABMSimulator)
:   This simulator uses incremental time progression, while allowing for additional event scheduling.

    Deprecated since version 3.5.0: ABMSimulator is deprecated and will be removed in Mesa 4.0.
    Use model.run\_for(), model.run\_until(), and model.schedule\_event() instead.
    See <https://mesa.readthedocs.io/latest/migration_guide.html#replacing-simulator-classes>

    The basic time unit of this simulator is an integer. It schedules model.step for each tick with the
    highest priority. This implies that by default, model.step is the first event executed at a specific tick.
    In addition, discrete event scheduling, using integer as the time unit is fully supported, paving the way
    for hybrid ABM-DEVS simulations.

    Initialize a ABM simulator.

    setup(*model*)[[source]](../_modules/experimental/devs/simulator.html#ABMSimulator.setup)
    :   Set up the simulator with the model to simulate.

        Parameters:
        :   **model** ([*Model*](../mesa.html#mesa.model.Model "mesa.model.Model")) – The model to simulate

    check\_time\_unit(*time*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/experimental/devs/simulator.html#ABMSimulator.check_time_unit)
    :   Check whether the time is of the correct unit.

        Parameters:
        :   **time** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *|* [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – the time

        Returns:
        :   whether the time is of the correct unit

        Return type:
        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    schedule\_event\_next\_tick(*function: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *priority: [Priority](time.html#mesa.time.Priority "mesa.time.events.Priority") = Priority.DEFAULT*, *function\_args: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *function\_kwargs: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [Event](time.html#mesa.time.Event "mesa.time.events.Event")[[source]](../_modules/experimental/devs/simulator.html#ABMSimulator.schedule_event_next_tick)
    :   Schedule a Event for the next tick.

        Parameters:
        :   - **function** (*Callable*) – the callable to execute
            - **priority** ([*Priority*](time.html#mesa.time.Priority "mesa.time.Priority")) – the priority of the event
            - **function\_args** (*List**[**Any**]*) – List of arguments to pass to the callable
            - **function\_kwargs** (*Dict**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *Any**]*) – List of keyword arguments to pass to the callable

class DEVSimulator[[source]](../_modules/experimental/devs/simulator.html#DEVSimulator)
:   A simulator where the unit of time is a float.

    Deprecated since version 3.5.0: DEVSimulator is deprecated and will be removed in Mesa 4.0.
    Use model.run\_for(), model.run\_until(), model.schedule\_event(), and model.schedule\_recurring() instead.
    See <https://mesa.readthedocs.io/latest/migration_guide.html#replacing-simulator-classes>

    Can be used for full-blown discrete event simulating using event scheduling.

    Initialize a DEVS simulator.

    setup(*model: [Model](../mesa.html#mesa.model.Model "mesa.model.Model")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/experimental/devs/simulator.html#DEVSimulator.setup)
    :   Set up the simulator with the model to simulate.

        Parameters:
        :   **model** ([*Model*](../mesa.html#mesa.model.Model "mesa.model.Model")) – The model to simulate

    check\_time\_unit(*time*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/experimental/devs/simulator.html#DEVSimulator.check_time_unit)
    :   Check whether the time is of the correct unit.

        Parameters:
        :   **time** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")) – the time

        Returns:
        bool: whether the time is of the correct unit

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

class Scenario(*\**, *rng: Generator | BitGenerator | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | integer | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | SeedSequence | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*kwargs*)[[source]](../_modules/experimental/scenarios/scenario.html#Scenario)
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

    model
    :   The model instance to which this scenario belongs

    scenario\_id
    :   A unique identifier for this scenario, auto-generated starting from 0

    rng
    :   Random number generator or seed value

    Notes

    All parameters are accessible via attribute access (scenario.param).
    Class-level attributes in subclasses serve as default values.
    Scenario parameters cannot be modified during model execution.

    Initialize a Scenario.

    Parameters:
    :   - **rng** – Random number generator or valid seed value
        - **\*\*kwargs** – All other scenario parameters (override class-level defaults)

    to\_dict() → [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")][[source]](../_modules/experimental/scenarios/scenario.html#Scenario.to_dict)
    :   Return dict representation of the scenario.

On this page

### This Page

- [Show Source](../_sources/apis/experimental.md.txt)

---

Original source: https://mesa.readthedocs.io/stable/apis/experimental.html
