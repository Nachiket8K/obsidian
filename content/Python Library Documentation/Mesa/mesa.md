---
title: "mesa package"
source: "https://mesa.readthedocs.io/latest/mesa.html"
imported_from: "Python library documentation"
library: "Mesa"
---

# mesa package

## Submodules

## mesa.agent module

Agent related classes.

Core Objects: Agent.

class Agent(*model: M*, *\*args*, *\*\*kwargs*)[[source]](_modules/mesa/agent.html#Agent)
:   Bases: [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "(in Python v3.14)")

    Base class for a model agent in Mesa.

    model
    :   A reference to the model instance.

        Type:
        :   [Model](#mesa.model.Model "mesa.model.Model")

    unique\_id
    :   A unique identifier for this agent.

        Type:
        :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    Notes

    Agents must be hashable to be used in an AgentSet.
    In Python 3, defining \_\_eq\_\_ without \_\_hash\_\_ makes an object unhashable,
    which will break AgentSet usage.
    unique\_id is unique relative to a model instance and starts from 1

    Create a new agent.

    Parameters:
    :   - **model** ([*Model*](#mesa.model.Model "mesa.model.Model")) – The model instance in which the agent exists.
        - **args** – Passed on to super.
        - **kwargs** – Passed on to super.

    Notes

    to make proper use of python’s super, in each class remove the arguments and
    keyword arguments you need and pass on the rest to super

    remove() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/agent.html#Agent.remove)
    :   Remove and delete the agent from the model.

        If the agent is currently performing an action, the action’s
        scheduled completion event is cancelled silently. The action’s
        on\_interrupt() callback is NOT fired, because the agent is being
        destroyed — not making a behavioral decision. The action moves
        to no defined end state; it is simply abandoned.

        If your action holds external resources (e.g., a Resource slot,
        a reservation, a lock), override Agent.remove() and call
        self.cancel\_action() before super().remove() to ensure
        on\_interrupt() fires and cleanup logic runs:

        > def remove(self):
        > :   self.cancel\_action() # Fires on\_interrupt for cleanup
        >     super().remove()

        Notes

        This is a deliberate design choice. The default silent
        cleanup is safe and avoids callbacks touching agent state
        during teardown. Models that need cleanup should opt in
        explicitly.

    step() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/agent.html#Agent.step)
    :   A single step of the agent.

    advance() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/agent.html#Agent.advance)

    classmethod create\_agents(*model: [Model](#mesa.model.Model "mesa.model.Model")*, *n: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *\*args*, *\*\*kwargs*) → [AgentSet](apis/agentset.html#mesa.agentset.AgentSet "mesa.agentset.AgentSet")[T][[source]](_modules/mesa/agent.html#Agent.create_agents)
    :   Create N agents.

        Parameters:
        :   - **model** – the model to which the agents belong
            - **args** – arguments to pass onto agent instances
              each arg is either a single object or a sequence of length n
            - **n** – the number of agents to create
            - **kwargs** – keyword arguments to pass onto agent instances
              each keyword arg is either a single object or a sequence of length n

        Returns:
        :   AgentSet containing the agents created.

    classmethod from\_dataframe(*model: [Model](#mesa.model.Model "mesa.model.Model")*, *df: pd.DataFrame*, *\*\*kwargs*) → [AgentSet](apis/agentset.html#mesa.agentset.AgentSet "mesa.agentset.AgentSet")[T][[source]](_modules/mesa/agent.html#Agent.from_dataframe)
    :   Create agents from a pandas DataFrame.

        Each row of the DataFrame represents one agent. The DataFrame columns are
        mapped to the agent’s constructor as keyword arguments. Additional keyword
        arguments (\*\*kwargs) can be used to set constant attributes for all agents.

        Parameters:
        :   - **model** – The model instance.
            - **df** – The pandas DataFrame. Each row represents an agent.
            - **\*\*kwargs** – Constant values to pass to every agent’s constructor.
              Only non-sequence data is allowed in kwargs to avoid ambiguity
              with DataFrame columns.

        Returns:
        :   AgentSet containing the agents created.

        If you need to pass variable data or sequences, add them as columns
        to the DataFrame before calling this method.

    property random: [Random](https://docs.python.org/3/library/random.html#random.Random "(in Python v3.14)")
    :   Return a seeded stdlib rng.

    property rng: Generator
    :   Return a seeded np.random rng.

    property scenario
    :   Return the scenario associated with the model.

    start\_action(*action: Action*) → Action[[source]](_modules/mesa/agent.html#Agent.start_action)
    :   Start performing an action.

        The action must be in PENDING or INTERRUPTED state and the agent
        must not be currently performing another action.

        Parameters:
        :   **action** – The Action to perform. Must have been created with
            this agent as its agent.

        Returns:
        :   The started Action.

        Raises:
        :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If the agent is already performing an action,
            or if the action doesn’t belong to this agent.

    interrupt\_for(*new\_action: Action*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](_modules/mesa/agent.html#Agent.interrupt_for)
    :   Interrupt the current action and start a new one.

        If there is no current action, simply starts the new one. If the
        current action is non-interruptible, returns False and does nothing.

        Parameters:
        :   **new\_action** – The Action to perform instead.

        Returns:
        :   True if the new action was started (either no current action,
            or the current one was successfully interrupted). False if the
            current action is non-interruptible.

    cancel\_action() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](_modules/mesa/agent.html#Agent.cancel_action)
    :   Cancel the current action, ignoring interruptible flag.

        Calls on\_interrupt with partial progress. Returns False only if
        there is no current action.

        Returns:
        :   True if an action was cancelled, False if idle.

    property is\_busy: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
    :   Whether the agent is currently performing an action.

## mesa.datacollection module

Mesa Data Collection Module.

DataCollector is meant to provide a simple, standard way to collect data
generated by a Mesa model. It collects four types of data: model-level data,
agent-level data, agent-type-level data, and tables.

A DataCollector is instantiated with three dictionaries of reporter names and
associated variable names or functions for each, one for model-level data,
one for agent-level data, and one for agent-type-level data; a fourth dictionary
provides table names and columns. Variable names are converted into functions
which retrieve attributes of that name.

When the collect() method is called, each model-level function is called, with
the model as the argument, and the results associated with the relevant
variable. Then the agent-level functions are called on each agent, and the
agent-type-level functions are called on each agent of the specified type.

Additionally, other objects can write directly to tables by passing in an
appropriate dictionary object for a table row.

The DataCollector then stores the data it collects in dictionaries:
:   - model\_vars maps each reporter to a list of its values
    - tables maps each table to a dictionary, with each column as a key with a
      list as its value.
    - \_agent\_records maps each model step to a list of each agent’s id
      and its values.
    - \_agenttype\_records maps each model step to a dictionary of agent types,
      each containing a list of each agent’s id and its values.

Finally, DataCollector can create a pandas DataFrame from each collection.

class DataCollector(*model\_reporters=None*, *agent\_reporters=None*, *agenttype\_reporters=None*, *tables=None*)[[source]](_modules/mesa/datacollection.html#DataCollector)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

    Class for collecting data generated by a Mesa model.

    A DataCollector is instantiated with dictionaries of names of model-,
    agent-, and agent-type-level variables to collect, associated with
    attribute names or functions which actually collect them. When the
    collect(…) method is called, it collects these attributes and executes
    these functions one by one and stores the results.

    Instantiate a DataCollector with lists of model, agent, and agent-type reporters.

    Both model\_reporters, agent\_reporters, and agenttype\_reporters accept a
    dictionary mapping a variable name to either an attribute name, a function,
    a method of a class/instance, a partial function, or a function with
    parameters placed in a list.

    Model reporters can take five types of arguments:
    1. Lambda function:

    > {“agent\_count”: lambda m: len(m.agents)}

    2. Method of a class/instance:
       {“agent\_count”: self.get\_agent\_count} # self here is a class instance
       {“agent\_count”: Model.get\_agent\_count} # Model here is a class
    3. Class attributes of a model:
       {“model\_attribute”: “model\_attribute”}
    4. Partial function:
       {“agent\_count”: functools.partial(count\_agents, multiplier=2)}
    5. Functions with parameters that have been placed in a list:
       {“Model\_Function”: [function, [param\_1, param\_2]]}

    Agent reporters can similarly take:
    1. Attribute name (string) referring to agent’s attribute:

    > {“energy”: “energy”}

    2. Lambda function:
       {“energy”: lambda a: a.energy}
    3. Method of an agent class/instance:
       {“agent\_action”: self.do\_action} # self here is an agent class instance
       {“agent\_action”: Agent.do\_action} # Agent here is a class
    4. Partial function:
       {“energy”: functools.partial(get\_energy, scale=2)}
    5. Functions with parameters placed in a list:
       {“Agent\_Function”: [function, [param\_1, param\_2]]}

    Agenttype reporters take a dictionary mapping agent types to dictionaries
    of reporter names and attributes/funcs/methods, similar to agent\_reporters:

    > {Wolf: {“energy”: lambda a: a.energy}}

    The tables arg accepts a dictionary mapping names of tables to lists of
    columns. For example, if we want to allow agents to write their age
    when they are destroyed (to keep track of lifespans), it might look
    like:

    > {“Lifespan”: [“unique\_id”, “age”]}

    Parameters:
    :   - **model\_reporters** – Dictionary of reporter names and attributes/funcs/methods.
        - **agent\_reporters** – Dictionary of reporter names and attributes/funcs/methods.
        - **agenttype\_reporters** – Dictionary of agent types to dictionaries of
          reporter names and attributes/funcs/methods.
        - **tables** – Dictionary of table names to lists of column names.

    Notes

    - If you want to pickle your model you must not use lambda functions.
    - If your model includes a large number of agents, it is recommended to
      use attribute names for the agent reporter, as it will be faster.

    collect(*model*)[[source]](_modules/mesa/datacollection.html#DataCollector.collect)
    :   Collect all the data for the given model object.

    add\_table\_row(*table\_name*, *row*, *ignore\_missing=False*)[[source]](_modules/mesa/datacollection.html#DataCollector.add_table_row)
    :   Add a row dictionary to a specific table.

        Parameters:
        :   - **table\_name** – Name of the table to append a row to.
            - **row** – A dictionary of the form {column\_name: value…}
            - **ignore\_missing** – If True, fill any missing columns with Nones;
              if False, throw an error if any columns are missing

    get\_model\_vars\_dataframe()[[source]](_modules/mesa/datacollection.html#DataCollector.get_model_vars_dataframe)
    :   Create a pandas DataFrame from the model variables.

        The DataFrame has one column for each model variable, and the index is
        (implicitly) the model tick.

    get\_agent\_vars\_dataframe()[[source]](_modules/mesa/datacollection.html#DataCollector.get_agent_vars_dataframe)
    :   Create a pandas DataFrame from the agent variables.

        The DataFrame has one column for each variable, with two additional
        columns for tick and agent\_id.

    get\_agenttype\_vars\_dataframe(*agent\_type*)[[source]](_modules/mesa/datacollection.html#DataCollector.get_agenttype_vars_dataframe)
    :   Create a pandas DataFrame from the agent-type variables for a specific agent type.

        The DataFrame has one column for each variable, with two additional
        columns for tick and agent\_id.

        Parameters:
        :   **agent\_type** – The type of agent to get the data for.

    get\_table\_dataframe(*table\_name*)[[source]](_modules/mesa/datacollection.html#DataCollector.get_table_dataframe)
    :   Create a pandas DataFrame from a particular table.

        Parameters:
        :   **table\_name** – The name of the table to convert.

## mesa.main module

## mesa.model module

The model class for Mesa framework.

Core Objects: Model

class Model(*\*args: Any*, *rng: RNGLike | SeedLike | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *scenario: S | [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[S] = <class 'mesa.experimental.scenarios.scenario.Scenario'>*, *\*\*kwargs: Any*)[[source]](_modules/mesa/model.html#Model)
:   Bases: `HasEmitters`, [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "(in Python v3.14)")

    Base class for models in the Mesa ABM library.

    This class serves as a foundational structure for creating agent-based models.
    It includes the basic attributes and methods necessary for initializing and
    running a simulation model.

    Type Parameters:
    :   A: The agent type used in this model
        S: The scenario type used in this model

    running
    :   A boolean indicating if the model should continue running.

    steps
    :   the number of times model.step() has been called.

    time
    :   the current simulation time.

    random
    :   a seeded python.random number generator.

    rng
    :   a seeded numpy.random.Generator

    scenario
    :   the scenario instance containing model parameters

    Notes

    Model.agents returns the AgentSet containing all agents registered with the model. Changing
    the content of the AgentSet directly can result in strange behavior. If you want change the
    composition of this AgentSet, ensure you operate on a copy.

    Create a new model.

    Overload this method with the actual code to initialize the model. Always start with super().\_\_init\_\_()
    to initialize the model object properly.

    Parameters:
    :   - **args** – arguments to pass onto super
        - **rng** – Seed for the random number generator. Accepts any value accepted by
          numpy.random.default\_rng(). Ignored if a Scenario instance is passed;
          used to instantiate the scenario when a Scenario class is passed.
        - **scenario** – A Scenario instance or subclass to use for this model. If a class
          is passed it is instantiated with rng. If an instance is passed, rng
          must not be set.
        - **kwargs** – keyword arguments to pass onto super

    Notes

    Pass either rng or a Scenario instance, not both. Passing rng alongside
    a Scenario class is valid — rng is forwarded to the class constructor.

    time: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")
    :   Observable descriptor.

        An observable is an attribute that emits ObservableSignals.CHANGED whenever it is changed to a different value.

    property scenario: S
    :   Return scenario instance.

    property agents: \_HardKeyAgentSet[A]
    :   Provides a \_HardKeyAgentSet of all agents in the model, combining agents from all types.

        Returns:
        :   The agent set containing all agents with strong references.

        Return type:
        :   \_HardKeyAgentSet

        This returns the actual internal \_HardKeyAgentSet used by Mesa for agent registration
        and tracking. It uses strong references to prevent premature garbage collection and reduce performance overhead
        caused by weak reference management.

        **Do not modify this AgentSet directly** (e.g., by adding or removing agents manually).
        Direct modifications can break the model’s agent tracking system and cause unexpected
        behavior. Instead:

        - Use `Agent()` to create new agents (automatically registers them)
        - Use `agent.remove()` to remove agents (automatically deregisters them)
        - For read-only operations or transformations, work on a copy: `model.agents.copy()`

        Notes

        This is Mesa’s core agent registration system. All agents created via `Agent.__init__`
        are automatically registered here.

    property agent\_types: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")]
    :   Return a list of all unique agent types registered with the model.

    property agents\_by\_type: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[A], \_HardKeyAgentSet[A]]
    :   A dictionary where keys are agent types and values are the corresponding \_HardKeyAgentSets.

        Returns:
        :   Dictionary mapping agent types to their AgentSets.

        Return type:
        :   [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[A], \_HardKeyAgentSet[A]]

        Each AgentSet in this dictionary is a \_HardKeyAgentSet with strong references,
        forming part of Mesa’s core agent registration system.

        **Do not modify these AgentSets directly**. Direct modifications can break agent
        tracking and cause unexpected behavior. Instead:

        - Use `Agent()` to create new agents (automatically registers them)
        - Use `agent.remove()` to remove agents (automatically deregisters them)
        - For read-only operations, work on copies: `model.agents_by_type[AgentType].copy()`

        Notes

        This is part of Mesa’s core agent registration system. All agents are automatically
        registered in the appropriate type-specific AgentSet when created via `Agent.__init__`.

    register\_agent(*agent: A*)[[source]](_modules/mesa/model.html#Model.register_agent)
    :   Register the agent with the model.

        Parameters:
        :   **agent** – The agent to register.

        Notes

        This method is called automatically by `Agent.__init__`, so there
        is no need to use this if you are subclassing Agent and calling its
        super in the `__init__` method.

    deregister\_agent(*agent: A*)[[source]](_modules/mesa/model.html#Model.deregister_agent)
    :   Deregister the agent with the model.

        Parameters:
        :   **agent** – The agent to deregister.

        Notes

        This method is called automatically by `Agent.remove`

    run\_model() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/model.html#Model.run_model)
    :   Run the model until the end condition is reached.

        Overload as needed.

    step() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/model.html#Model.step)
    :   A single step. Fill in here.

    observables: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[SignalType] | [frozenset](https://docs.python.org/3/library/stdtypes.html#frozenset "(in Python v3.14)")[SignalType]] = {'agents': frozenset({ModelSignals.AGENT\_ADDED, ModelSignals.AGENT\_REMOVED}), 'model': frozenset({ModelSignals.RUN\_ENDED}), 'time': <enum 'ObservableSignals'>}

    remove\_all\_agents()[[source]](_modules/mesa/model.html#Model.remove_all_agents)
    :   Remove all agents from the model.

        Notes

        This method calls agent.remove for all agents in the model. If you need to remove agents from
        e.g., a SingleGrid, you can either explicitly implement your own agent.remove method or clean this up
        near where you are calling this method.

    schedule\_event(*function: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *\**, *at: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *after: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *priority: [Priority](apis/time.html#mesa.time.Priority "mesa.time.events.Priority") = Priority.DEFAULT*) → [Event](apis/time.html#mesa.time.Event "mesa.time.events.Event")[[source]](_modules/mesa/model.html#Model.schedule_event)
    :   Schedule a one-off event.

        Parameters:
        :   - **function** – The callable to execute
            - **at** – Absolute time to execute (mutually exclusive with after)
            - **after** – Relative time from now to execute (mutually exclusive with at)
            - **priority** – Priority level for the event

        Returns:
        :   The scheduled Event (can be used to cancel)

        Raises:
        :   - [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If both or neither of at/after are specified
            - [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If both or neither of at/after are specified, or if the scheduled time is in the past.

    schedule\_recurring(*function: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *schedule: [Schedule](apis/time.html#mesa.time.Schedule "mesa.time.events.Schedule")*, *priority: [Priority](apis/time.html#mesa.time.Priority "mesa.time.events.Priority") = Priority.DEFAULT*) → [EventGenerator](apis/time.html#mesa.time.EventGenerator "mesa.time.events.EventGenerator")[[source]](_modules/mesa/model.html#Model.schedule_recurring)
    :   Schedule a recurring event based on a Schedule.

        Parameters:
        :   - **function** – The callable to execute repeatedly
            - **schedule** – The Schedule defining when events occur
            - **priority** – Priority level for generated events

        Returns:
        :   The EventGenerator (can be used to stop)

        Raises:
        :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If the schedule start time is in the past.

    run\_for(*duration: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/model.html#Model.run_for)
    :   Run the model for the specified duration.

        Parameters:
        :   **duration** – Time units to advance

    run\_until(*end\_time: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/model.html#Model.run_until)
    :   Run the model until the specified time.

        Parameters:
        :   **end\_time** – Absolute time to run until

        If model.time is larger than end\_time, the method returns directly.

## Module contents

Mesa Agent-Based Modeling Framework.

Core Objects: Model, and Agent.

class Agent(*model: M*, *\*args*, *\*\*kwargs*)[[source]](_modules/mesa/agent.html#Agent)
:   Bases: [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "(in Python v3.14)")

    Base class for a model agent in Mesa.

    model
    :   A reference to the model instance.

        Type:
        :   [Model](#mesa.Model "mesa.Model")

    unique\_id
    :   A unique identifier for this agent.

        Type:
        :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    Notes

    Agents must be hashable to be used in an AgentSet.
    In Python 3, defining \_\_eq\_\_ without \_\_hash\_\_ makes an object unhashable,
    which will break AgentSet usage.
    unique\_id is unique relative to a model instance and starts from 1

    Create a new agent.

    Parameters:
    :   - **model** ([*Model*](#mesa.Model "mesa.Model")) – The model instance in which the agent exists.
        - **args** – Passed on to super.
        - **kwargs** – Passed on to super.

    Notes

    to make proper use of python’s super, in each class remove the arguments and
    keyword arguments you need and pass on the rest to super

    remove() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/agent.html#Agent.remove)
    :   Remove and delete the agent from the model.

        If the agent is currently performing an action, the action’s
        scheduled completion event is cancelled silently. The action’s
        on\_interrupt() callback is NOT fired, because the agent is being
        destroyed — not making a behavioral decision. The action moves
        to no defined end state; it is simply abandoned.

        If your action holds external resources (e.g., a Resource slot,
        a reservation, a lock), override Agent.remove() and call
        self.cancel\_action() before super().remove() to ensure
        on\_interrupt() fires and cleanup logic runs:

        > def remove(self):
        > :   self.cancel\_action() # Fires on\_interrupt for cleanup
        >     super().remove()

        Notes

        This is a deliberate design choice. The default silent
        cleanup is safe and avoids callbacks touching agent state
        during teardown. Models that need cleanup should opt in
        explicitly.

    step() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/agent.html#Agent.step)
    :   A single step of the agent.

    advance() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/agent.html#Agent.advance)

    classmethod create\_agents(*model: [Model](#mesa.Model "mesa.Model")*, *n: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *\*args*, *\*\*kwargs*) → [AgentSet](apis/agentset.html#mesa.agentset.AgentSet "mesa.agentset.AgentSet")[T][[source]](_modules/mesa/agent.html#Agent.create_agents)
    :   Create N agents.

        Parameters:
        :   - **model** – the model to which the agents belong
            - **args** – arguments to pass onto agent instances
              each arg is either a single object or a sequence of length n
            - **n** – the number of agents to create
            - **kwargs** – keyword arguments to pass onto agent instances
              each keyword arg is either a single object or a sequence of length n

        Returns:
        :   AgentSet containing the agents created.

    classmethod from\_dataframe(*model: [Model](#mesa.Model "mesa.Model")*, *df: pd.DataFrame*, *\*\*kwargs*) → [AgentSet](apis/agentset.html#mesa.agentset.AgentSet "mesa.agentset.AgentSet")[T][[source]](_modules/mesa/agent.html#Agent.from_dataframe)
    :   Create agents from a pandas DataFrame.

        Each row of the DataFrame represents one agent. The DataFrame columns are
        mapped to the agent’s constructor as keyword arguments. Additional keyword
        arguments (\*\*kwargs) can be used to set constant attributes for all agents.

        Parameters:
        :   - **model** – The model instance.
            - **df** – The pandas DataFrame. Each row represents an agent.
            - **\*\*kwargs** – Constant values to pass to every agent’s constructor.
              Only non-sequence data is allowed in kwargs to avoid ambiguity
              with DataFrame columns.

        Returns:
        :   AgentSet containing the agents created.

        If you need to pass variable data or sequences, add them as columns
        to the DataFrame before calling this method.

    property random: [Random](https://docs.python.org/3/library/random.html#random.Random "(in Python v3.14)")
    :   Return a seeded stdlib rng.

    property rng: Generator
    :   Return a seeded np.random rng.

    property scenario
    :   Return the scenario associated with the model.

    start\_action(*action: Action*) → Action[[source]](_modules/mesa/agent.html#Agent.start_action)
    :   Start performing an action.

        The action must be in PENDING or INTERRUPTED state and the agent
        must not be currently performing another action.

        Parameters:
        :   **action** – The Action to perform. Must have been created with
            this agent as its agent.

        Returns:
        :   The started Action.

        Raises:
        :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If the agent is already performing an action,
            or if the action doesn’t belong to this agent.

    interrupt\_for(*new\_action: Action*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](_modules/mesa/agent.html#Agent.interrupt_for)
    :   Interrupt the current action and start a new one.

        If there is no current action, simply starts the new one. If the
        current action is non-interruptible, returns False and does nothing.

        Parameters:
        :   **new\_action** – The Action to perform instead.

        Returns:
        :   True if the new action was started (either no current action,
            or the current one was successfully interrupted). False if the
            current action is non-interruptible.

    cancel\_action() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](_modules/mesa/agent.html#Agent.cancel_action)
    :   Cancel the current action, ignoring interruptible flag.

        Calls on\_interrupt with partial progress. Returns False only if
        there is no current action.

        Returns:
        :   True if an action was cancelled, False if idle.

    property is\_busy: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
    :   Whether the agent is currently performing an action.

class DataCollector(*model\_reporters=None*, *agent\_reporters=None*, *agenttype\_reporters=None*, *tables=None*)[[source]](_modules/mesa/datacollection.html#DataCollector)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

    Class for collecting data generated by a Mesa model.

    A DataCollector is instantiated with dictionaries of names of model-,
    agent-, and agent-type-level variables to collect, associated with
    attribute names or functions which actually collect them. When the
    collect(…) method is called, it collects these attributes and executes
    these functions one by one and stores the results.

    Instantiate a DataCollector with lists of model, agent, and agent-type reporters.

    Both model\_reporters, agent\_reporters, and agenttype\_reporters accept a
    dictionary mapping a variable name to either an attribute name, a function,
    a method of a class/instance, a partial function, or a function with
    parameters placed in a list.

    Model reporters can take five types of arguments:
    1. Lambda function:

    > {“agent\_count”: lambda m: len(m.agents)}

    2. Method of a class/instance:
       {“agent\_count”: self.get\_agent\_count} # self here is a class instance
       {“agent\_count”: Model.get\_agent\_count} # Model here is a class
    3. Class attributes of a model:
       {“model\_attribute”: “model\_attribute”}
    4. Partial function:
       {“agent\_count”: functools.partial(count\_agents, multiplier=2)}
    5. Functions with parameters that have been placed in a list:
       {“Model\_Function”: [function, [param\_1, param\_2]]}

    Agent reporters can similarly take:
    1. Attribute name (string) referring to agent’s attribute:

    > {“energy”: “energy”}

    2. Lambda function:
       {“energy”: lambda a: a.energy}
    3. Method of an agent class/instance:
       {“agent\_action”: self.do\_action} # self here is an agent class instance
       {“agent\_action”: Agent.do\_action} # Agent here is a class
    4. Partial function:
       {“energy”: functools.partial(get\_energy, scale=2)}
    5. Functions with parameters placed in a list:
       {“Agent\_Function”: [function, [param\_1, param\_2]]}

    Agenttype reporters take a dictionary mapping agent types to dictionaries
    of reporter names and attributes/funcs/methods, similar to agent\_reporters:

    > {Wolf: {“energy”: lambda a: a.energy}}

    The tables arg accepts a dictionary mapping names of tables to lists of
    columns. For example, if we want to allow agents to write their age
    when they are destroyed (to keep track of lifespans), it might look
    like:

    > {“Lifespan”: [“unique\_id”, “age”]}

    Parameters:
    :   - **model\_reporters** – Dictionary of reporter names and attributes/funcs/methods.
        - **agent\_reporters** – Dictionary of reporter names and attributes/funcs/methods.
        - **agenttype\_reporters** – Dictionary of agent types to dictionaries of
          reporter names and attributes/funcs/methods.
        - **tables** – Dictionary of table names to lists of column names.

    Notes

    - If you want to pickle your model you must not use lambda functions.
    - If your model includes a large number of agents, it is recommended to
      use attribute names for the agent reporter, as it will be faster.

    collect(*model*)[[source]](_modules/mesa/datacollection.html#DataCollector.collect)
    :   Collect all the data for the given model object.

    add\_table\_row(*table\_name*, *row*, *ignore\_missing=False*)[[source]](_modules/mesa/datacollection.html#DataCollector.add_table_row)
    :   Add a row dictionary to a specific table.

        Parameters:
        :   - **table\_name** – Name of the table to append a row to.
            - **row** – A dictionary of the form {column\_name: value…}
            - **ignore\_missing** – If True, fill any missing columns with Nones;
              if False, throw an error if any columns are missing

    get\_model\_vars\_dataframe()[[source]](_modules/mesa/datacollection.html#DataCollector.get_model_vars_dataframe)
    :   Create a pandas DataFrame from the model variables.

        The DataFrame has one column for each model variable, and the index is
        (implicitly) the model tick.

    get\_agent\_vars\_dataframe()[[source]](_modules/mesa/datacollection.html#DataCollector.get_agent_vars_dataframe)
    :   Create a pandas DataFrame from the agent variables.

        The DataFrame has one column for each variable, with two additional
        columns for tick and agent\_id.

    get\_agenttype\_vars\_dataframe(*agent\_type*)[[source]](_modules/mesa/datacollection.html#DataCollector.get_agenttype_vars_dataframe)
    :   Create a pandas DataFrame from the agent-type variables for a specific agent type.

        The DataFrame has one column for each variable, with two additional
        columns for tick and agent\_id.

        Parameters:
        :   **agent\_type** – The type of agent to get the data for.

    get\_table\_dataframe(*table\_name*)[[source]](_modules/mesa/datacollection.html#DataCollector.get_table_dataframe)
    :   Create a pandas DataFrame from a particular table.

        Parameters:
        :   **table\_name** – The name of the table to convert.

class Model(*\*args: Any*, *rng: RNGLike | SeedLike | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *scenario: S | [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[S] = <class 'mesa.experimental.scenarios.scenario.Scenario'>*, *\*\*kwargs: Any*)[[source]](_modules/mesa/model.html#Model)
:   Bases: `HasEmitters`, [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "(in Python v3.14)")

    Base class for models in the Mesa ABM library.

    This class serves as a foundational structure for creating agent-based models.
    It includes the basic attributes and methods necessary for initializing and
    running a simulation model.

    Type Parameters:
    :   A: The agent type used in this model
        S: The scenario type used in this model

    running
    :   A boolean indicating if the model should continue running.

        Type:
        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    steps
    :   the number of times model.step() has been called.

    time
    :   the current simulation time.

        Type:
        :   [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")

    random
    :   a seeded python.random number generator.

    rng
    :   a seeded numpy.random.Generator

        Type:
        :   numpy.random.\_generator.Generator

    scenario
    :   the scenario instance containing model parameters

    Notes

    Model.agents returns the AgentSet containing all agents registered with the model. Changing
    the content of the AgentSet directly can result in strange behavior. If you want change the
    composition of this AgentSet, ensure you operate on a copy.

    Create a new model.

    Overload this method with the actual code to initialize the model. Always start with super().\_\_init\_\_()
    to initialize the model object properly.

    Parameters:
    :   - **args** – arguments to pass onto super
        - **rng** – Seed for the random number generator. Accepts any value accepted by
          numpy.random.default\_rng(). Ignored if a Scenario instance is passed;
          used to instantiate the scenario when a Scenario class is passed.
        - **scenario** – A Scenario instance or subclass to use for this model. If a class
          is passed it is instantiated with rng. If an instance is passed, rng
          must not be set.
        - **kwargs** – keyword arguments to pass onto super

    Notes

    Pass either rng or a Scenario instance, not both. Passing rng alongside
    a Scenario class is valid — rng is forwarded to the class constructor.

    running: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    time: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")
    :   Observable descriptor.

        An observable is an attribute that emits ObservableSignals.CHANGED whenever it is changed to a different value.

    agent\_id\_counter: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    property scenario: S
    :   Return scenario instance.

    rng: Generator

    property agents: \_HardKeyAgentSet[A]
    :   Provides a \_HardKeyAgentSet of all agents in the model, combining agents from all types.

        Returns:
        :   The agent set containing all agents with strong references.

        Return type:
        :   \_HardKeyAgentSet

        This returns the actual internal \_HardKeyAgentSet used by Mesa for agent registration
        and tracking. It uses strong references to prevent premature garbage collection and reduce performance overhead
        caused by weak reference management.

        **Do not modify this AgentSet directly** (e.g., by adding or removing agents manually).
        Direct modifications can break the model’s agent tracking system and cause unexpected
        behavior. Instead:

        - Use `Agent()` to create new agents (automatically registers them)
        - Use `agent.remove()` to remove agents (automatically deregisters them)
        - For read-only operations or transformations, work on a copy: `model.agents.copy()`

        Notes

        This is Mesa’s core agent registration system. All agents created via `Agent.__init__`
        are automatically registered here.

    property agent\_types: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")]
    :   Return a list of all unique agent types registered with the model.

    property agents\_by\_type: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[A], \_HardKeyAgentSet[A]]
    :   A dictionary where keys are agent types and values are the corresponding \_HardKeyAgentSets.

        Returns:
        :   Dictionary mapping agent types to their AgentSets.

        Return type:
        :   [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[A], \_HardKeyAgentSet[A]]

        Each AgentSet in this dictionary is a \_HardKeyAgentSet with strong references,
        forming part of Mesa’s core agent registration system.

        **Do not modify these AgentSets directly**. Direct modifications can break agent
        tracking and cause unexpected behavior. Instead:

        - Use `Agent()` to create new agents (automatically registers them)
        - Use `agent.remove()` to remove agents (automatically deregisters them)
        - For read-only operations, work on copies: `model.agents_by_type[AgentType].copy()`

        Notes

        This is part of Mesa’s core agent registration system. All agents are automatically
        registered in the appropriate type-specific AgentSet when created via `Agent.__init__`.

    register\_agent(*agent: A*)[[source]](_modules/mesa/model.html#Model.register_agent)
    :   Register the agent with the model.

        Parameters:
        :   **agent** – The agent to register.

        Notes

        This method is called automatically by `Agent.__init__`, so there
        is no need to use this if you are subclassing Agent and calling its
        super in the `__init__` method.

    deregister\_agent(*agent: A*)[[source]](_modules/mesa/model.html#Model.deregister_agent)
    :   Deregister the agent with the model.

        Parameters:
        :   **agent** – The agent to deregister.

        Notes

        This method is called automatically by `Agent.remove`

    run\_model() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/model.html#Model.run_model)
    :   Run the model until the end condition is reached.

        Overload as needed.

    step() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/model.html#Model.step)
    :   A single step. Fill in here.

    observables: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[SignalType] | [frozenset](https://docs.python.org/3/library/stdtypes.html#frozenset "(in Python v3.14)")[SignalType]] = {'agents': frozenset({ModelSignals.AGENT\_ADDED, ModelSignals.AGENT\_REMOVED}), 'model': frozenset({ModelSignals.RUN\_ENDED}), 'time': <enum 'ObservableSignals'>}

    remove\_all\_agents()[[source]](_modules/mesa/model.html#Model.remove_all_agents)
    :   Remove all agents from the model.

        Notes

        This method calls agent.remove for all agents in the model. If you need to remove agents from
        e.g., a SingleGrid, you can either explicitly implement your own agent.remove method or clean this up
        near where you are calling this method.

    schedule\_event(*function: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *\**, *at: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *after: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *priority: [Priority](apis/time.html#mesa.time.Priority "mesa.time.events.Priority") = Priority.DEFAULT*) → [Event](apis/time.html#mesa.time.Event "mesa.time.events.Event")[[source]](_modules/mesa/model.html#Model.schedule_event)
    :   Schedule a one-off event.

        Parameters:
        :   - **function** – The callable to execute
            - **at** – Absolute time to execute (mutually exclusive with after)
            - **after** – Relative time from now to execute (mutually exclusive with at)
            - **priority** – Priority level for the event

        Returns:
        :   The scheduled Event (can be used to cancel)

        Raises:
        :   - [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If both or neither of at/after are specified
            - [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If both or neither of at/after are specified, or if the scheduled time is in the past.

    schedule\_recurring(*function: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *schedule: [Schedule](apis/time.html#mesa.time.Schedule "mesa.time.events.Schedule")*, *priority: [Priority](apis/time.html#mesa.time.Priority "mesa.time.events.Priority") = Priority.DEFAULT*) → [EventGenerator](apis/time.html#mesa.time.EventGenerator "mesa.time.events.EventGenerator")[[source]](_modules/mesa/model.html#Model.schedule_recurring)
    :   Schedule a recurring event based on a Schedule.

        Parameters:
        :   - **function** – The callable to execute repeatedly
            - **schedule** – The Schedule defining when events occur
            - **priority** – Priority level for generated events

        Returns:
        :   The EventGenerator (can be used to stop)

        Raises:
        :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If the schedule start time is in the past.

    run\_for(*duration: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/model.html#Model.run_for)
    :   Run the model for the specified duration.

        Parameters:
        :   **duration** – Time units to advance

    run\_until(*end\_time: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/model.html#Model.run_until)
    :   Run the model until the specified time.

        Parameters:
        :   **end\_time** – Absolute time to run until

        If model.time is larger than end\_time, the method returns directly.

On this page

[Show Source](_sources/mesa.md.txt)

---

Original source: https://mesa.readthedocs.io/latest/mesa.html
