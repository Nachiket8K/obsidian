---
title: "mesa package"
source: "https://mesa.readthedocs.io/stable/mesa.html"
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

    pos
    :   A reference to the position where this agent is located.

        Type:
        :   Position

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

        Notes

        If you need to do additional cleanup when removing an agent by for example removing
        it from a space, consider extending this method in your own agent class.

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

## mesa.batchrunner module

batchrunner for running a factorial experiment design over a model.

To take advantage of parallel execution of experiments, batch\_run uses
multiprocessing if `number_processes` is larger than 1. It is strongly advised
to only run in parallel using a normal python file (so don’t try to do it in a
jupyter notebook). This is because Jupyter notebooks have a different execution
model that can cause issues with Python’s multiprocessing module, especially on
Windows. The main problems include the lack of a traditional \_\_main\_\_ entry
point, serialization issues, and potential deadlocks.

Moreover, best practice when using multiprocessing is to
put the code inside an `if __name__ == '__main__':` code black as shown below:

```
from mesa.batchrunner import batch_run

params = {"width": 10, "height": 10, "N": range(10, 500, 10)}

if __name__ == '__main__':
    results = batch_run(
        MoneyModel,
        parameters=params,
        iterations=5,
        max_steps=100,
        number_processes=None,
        data_collection_period=1,
        display_progress=True,
    )
```

batch\_run(*model\_cls: [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[[Model](#mesa.model.Model "mesa.model.Model")]*, *parameters: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)") | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]]*, *number\_processes: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 1*, *iterations: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *data\_collection\_period: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = -1*, *max\_steps: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1000*, *display\_progress: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *rng: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | integer | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | SeedSequence | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | integer | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | SeedSequence] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]][[source]](_modules/mesa/batchrunner.html#batch_run)
:   Batch run a mesa model with a set of parameter values.

    Parameters:
    :   - **model\_cls** (*Type**[*[*Model*](#mesa.model.Model "mesa.model.Model")*]*) – The model class to batch-run
        - **parameters** (*Mapping**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *Union**[**Any**,* *Iterable**[**Any**]**]**]*) – Dictionary with model parameters over which to run the model. You can either pass single values or iterables.
        - **number\_processes** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) – Number of processes used, by default 1. Set this to None if you want to use all CPUs.
        - **iterations** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) – Number of iterations for each parameter combination, by default 1
        - **data\_collection\_period** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) – Number of steps after which data gets collected, by default -1 (end of episode)
        - **max\_steps** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) – Maximum number of model steps after which the model halts, by default 1000
        - **display\_progress** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) – Display batch run process, by default True
        - **rng** – a valid value or iterable of values for seeding the random number generator in the model

    Returns:
    :   List[Dict[str, Any]]

    Notes

    batch\_run assumes the model has a datacollector attribute that has a DataCollector object initialized.

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

class Model(*\*args: Any*, *seed: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *rng: RNGLike | SeedLike | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *scenario: S | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*kwargs: Any*)[[source]](_modules/mesa/model.html#Model)
:   Bases: `HasObservables`, [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "(in Python v3.14)")

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
    :   the current simulation time. Automatically increments by 1.0
        with each step unless controlled by a discrete event simulator.

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
        - **seed** – the seed for the random number generator
        - **rng** – Pseudorandom number generator state. When rng is None, a new numpy.random.Generator is created
          using entropy from the operating system. Types other than numpy.random.Generator are passed to
          numpy.random.default\_rng to instantiate a Generator.
        - **scenario** – the scenario specifying the computational experiment to run
        - **kwargs** – keyword arguments to pass onto super

    Notes

    you have to pass either seed or rng, but not both.

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

    observables = {'agents': frozenset({ModelSignals.AGENT\_ADDED, ModelSignals.AGENT\_REMOVED}), 'time': <enum 'ObservableSignals'>}

    run\_model() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/model.html#Model.run_model)
    :   Run the model until the end condition is reached.

        Overload as needed.

    step() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/model.html#Model.step)
    :   A single step. Fill in here.

    reset\_randomizer(*seed: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/model.html#Model.reset_randomizer)
    :   Reset the model random number generator.

        Parameters:
        :   **seed** – A new seed for the RNG; if None, reset using the current seed

    reset\_rng(*rng: Generator | BitGenerator | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | integer | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | SeedSequence | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/model.html#Model.reset_rng)
    :   Reset the model random number generator.

        Parameters:
        :   **rng** – A new seed for the RNG; if None, reset using the current seed

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

## mesa.space module

Mesa Space Module.

Objects used to add a spatial component to a model.

mesa.space now in maintenance-only mode. While these classes remain
fully supported, new development occurs in the discrete space module
(`mesa.discrete_space`) and the experimental ContinuousSpace module

### Classes

- PropertyLayer: A data layer that can be added to Grids to store cell properties
- SingleGrid: a Grid which strictly enforces one agent per cell.
- MultiGrid: a Grid where each cell can contain a set of agents.
- HexGrid: a Grid to handle hexagonal neighbors.
- ContinuousSpace: a two-dimensional space where each agent has an arbitrary position of float’s.
- NetworkGrid: a network where each node contains zero or more agents.

accept\_tuple\_argument(*wrapped\_function: F*) → F[[source]](_modules/mesa/space.html#accept_tuple_argument)
:   Decorator to allow grid methods that take a list of (x, y) coord tuples to also handle a single position.

    Tuples are wrapped in a single-item list rather than forcing user to do it.

is\_integer(*x: [Real](https://docs.python.org/3/library/numbers.html#numbers.Real "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](_modules/mesa/space.html#is_integer)
:   Check if x is either a CPython integer or Numpy integer.

warn\_if\_agent\_has\_position\_already(*placement\_func*)[[source]](_modules/mesa/space.html#warn_if_agent_has_position_already)
:   Decorator to give warning if agent has position already set.

is\_single\_argument\_function(*function*)[[source]](_modules/mesa/space.html#is_single_argument_function)
:   Check if a function is a single argument function.

ufunc\_requires\_additional\_input(*ufunc*)[[source]](_modules/mesa/space.html#ufunc_requires_additional_input)

class PropertyLayer(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *height: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *default\_value*, *dtype=<class 'numpy.float64'>*)[[source]](_modules/mesa/space.html#PropertyLayer)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

    A class representing a layer of properties in a two-dimensional grid.

    Each cell in the grid can store a value of a specified data type.

    name
    :   The name of the property layer.

        Type:
        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    width
    :   The width of the grid (number of columns).

        Type:
        :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    height
    :   The height of the grid (number of rows).

        Type:
        :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    data
    :   A NumPy array representing the grid data.

        Type:
        :   numpy.ndarray

    Initializes a new PropertyLayer instance.

    Parameters:
    :   - **name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The name of the property layer.
        - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The width of the grid (number of columns). Must be a positive integer.
        - **height** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The height of the grid (number of rows). Must be a positive integer.
        - **default\_value** – The default value to initialize each cell in the grid. Should ideally
          be of the same type as specified by the dtype parameter.
        - **dtype** (*data-type**,* *optional*) – The desired data-type for the grid’s elements. Default is np.float64.

    Raises:
    :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If width or height is not a positive integer.

    Notes

    A UserWarning is raised if the default\_value is not of a type compatible with dtype.
    The dtype parameter can accept both Python data types (like bool, int or float) and NumPy data types
    (like np.int64 or np.float64). Using NumPy data types is recommended (except for bool) for better control
    over the precision and efficiency of data storage and computations, especially in cases of large data
    volumes or specialized numerical operations.

    set\_cell(*position: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *value*)[[source]](_modules/mesa/space.html#PropertyLayer.set_cell)
    :   Update a single cell’s value in-place.

    set\_cells(*value*, *condition=None*)[[source]](_modules/mesa/space.html#PropertyLayer.set_cells)
    :   Perform a batch update either on the entire grid or conditionally, in-place.

        Parameters:
        :   - **value** – The value to be used for the update.
            - **condition** – (Optional) A callable (like a lambda function or a NumPy ufunc)
              that returns a boolean array when applied to the data.

    modify\_cell(*position: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *operation*, *value=None*)[[source]](_modules/mesa/space.html#PropertyLayer.modify_cell)
    :   Modify a single cell using an operation, which can be a lambda function or a NumPy ufunc.

        If a NumPy ufunc is used, an additional value should be provided.

        Parameters:
        :   - **position** – The grid coordinates of the cell to modify.
            - **operation** – A function to apply. Can be a lambda function or a NumPy ufunc.
            - **value** – The value to be used if the operation is a NumPy ufunc. Ignored for lambda functions.

    modify\_cells(*operation*, *value=None*, *condition\_function=None*)[[source]](_modules/mesa/space.html#PropertyLayer.modify_cells)
    :   Modify cells using an operation, which can be a lambda function or a NumPy ufunc.

        If a NumPy ufunc is used, an additional value should be provided.

        Parameters:
        :   - **operation** – A function to apply. Can be a lambda function or a NumPy ufunc.
            - **value** – The value to be used if the operation is a NumPy ufunc. Ignored for lambda functions.
            - **condition\_function** – (Optional) A callable that returns a boolean array when applied to the data.

    select\_cells(*condition*, *return\_list=True*)[[source]](_modules/mesa/space.html#PropertyLayer.select_cells)
    :   Find cells that meet a specified condition using NumPy’s boolean indexing, in-place.

        Parameters:
        :   - **condition** – A callable that returns a boolean array when applied to the data.
            - **return\_list** – (Optional) If True, return a list of (x, y) tuples. Otherwise, return a boolean array.

        Returns:
        :   A list of (x, y) tuples or a boolean array.

    aggregate\_property(*operation*)[[source]](_modules/mesa/space.html#PropertyLayer.aggregate_property)
    :   Perform an aggregate operation (e.g., sum, mean) on a property across all cells.

        Parameters:
        :   **operation** – A function to apply. Can be a lambda function or a NumPy ufunc.

class SingleGrid(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *height: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *torus: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *property\_layers: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [PropertyLayer](#mesa.space.PropertyLayer "mesa.space.PropertyLayer") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[PropertyLayer](#mesa.space.PropertyLayer "mesa.space.PropertyLayer")] = None*)[[source]](_modules/mesa/space.html#SingleGrid)
:   Bases: `_PropertyGrid`

    Rectangular grid where each cell contains exactly at most one agent.

    Grid cells are indexed by [x, y], where [0, 0] is assumed to be the
    bottom-left and [width-1, height-1] is the top-right. If a grid is
    toroidal, the top and bottom, and left and right, edges wrap to each other.

    This class provides a property empties that returns a set of coordinates
    for all empty cells in the grid. It is automatically updated whenever
    agents are added or removed from the grid. The empties property should be
    used for efficient access to current empty cells rather than manually
    iterating over the grid to check for emptiness.

    Properties:
    :   width, height: The grid’s width and height.
        torus: Boolean which determines whether to treat the grid as a torus.
        empties: Returns a set of (x, y) tuples for all empty cells. This set is

        > maintained internally and provides a performant way to query
        > the grid for empty spaces.

    Initializes a new \_PropertyGrid instance with specified dimensions and optional property layers.

    Parameters:
    :   - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The width of the grid (number of columns).
        - **height** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The height of the grid (number of rows).
        - **torus** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – A boolean indicating if the grid should behave like a torus.
        - **property\_layers** (*None* *|* [*PropertyLayer*](#mesa.space.PropertyLayer "mesa.space.PropertyLayer") *|* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*[*[*PropertyLayer*](#mesa.space.PropertyLayer "mesa.space.PropertyLayer")*]**,* *optional*) – A single PropertyLayer instance,
          a list of PropertyLayer instances, or None to initialize without any property layers.

    Raises:
    :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If a property layer’s dimensions do not match the grid dimensions.

    place\_agent(*agent*, *\*args*, *\*\*kwargs*)[[source]](_modules/mesa/space.html#SingleGrid.place_agent)

    remove\_agent(*agent: [Agent](#mesa.agent.Agent "mesa.agent.Agent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/space.html#SingleGrid.remove_agent)
    :   Remove the agent from the grid and set its pos attribute to None.

class MultiGrid(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *height: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *torus: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *property\_layers: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [PropertyLayer](#mesa.space.PropertyLayer "mesa.space.PropertyLayer") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[PropertyLayer](#mesa.space.PropertyLayer "mesa.space.PropertyLayer")] = None*)[[source]](_modules/mesa/space.html#MultiGrid)
:   Bases: `_PropertyGrid`

    Rectangular grid where each cell can contain more than one agent.

    Grid cells are indexed by [x, y], where [0, 0] is assumed to be at
    bottom-left and [width-1, height-1] is the top-right. If a grid is
    toroidal, the top and bottom, and left and right, edges wrap to each other.

    This class maintains an empties property, which is a set of coordinates
    for all cells that currently contain no agents. This property is updated
    automatically as agents are added to or removed from the grid.

    Properties:
    :   width, height: The grid’s width and height.
        torus: Boolean which determines whether to treat the grid as a torus.
        empties: Returns a set of (x, y) tuples for all empty cells.

    Initializes a new \_PropertyGrid instance with specified dimensions and optional property layers.

    Parameters:
    :   - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The width of the grid (number of columns).
        - **height** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The height of the grid (number of rows).
        - **torus** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – A boolean indicating if the grid should behave like a torus.
        - **property\_layers** (*None* *|* [*PropertyLayer*](#mesa.space.PropertyLayer "mesa.space.PropertyLayer") *|* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*[*[*PropertyLayer*](#mesa.space.PropertyLayer "mesa.space.PropertyLayer")*]**,* *optional*) – A single PropertyLayer instance,
          a list of PropertyLayer instances, or None to initialize without any property layers.

    Raises:
    :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If a property layer’s dimensions do not match the grid dimensions.

    grid: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Agent](#mesa.agent.Agent "mesa.agent.Agent")]]]

    static default\_val() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Agent](#mesa.agent.Agent "mesa.agent.Agent")][[source]](_modules/mesa/space.html#MultiGrid.default_val)
    :   Default value for new cell elements.

    place\_agent(*agent*, *\*args*, *\*\*kwargs*)[[source]](_modules/mesa/space.html#MultiGrid.place_agent)

    remove\_agent(*agent: [Agent](#mesa.agent.Agent "mesa.agent.Agent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/space.html#MultiGrid.remove_agent)
    :   Remove the agent from the given location and set its pos attribute to None.

    iter\_neighbors(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *moore: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.14)")[[Agent](#mesa.agent.Agent "mesa.agent.Agent")][[source]](_modules/mesa/space.html#MultiGrid.iter_neighbors)
    :   Return an iterator over neighbors to a certain point.

        Parameters:
        :   - **pos** – Coordinates for the neighborhood to get.
            - **moore** –

              If True, return Moore neighborhood
              :   (including diagonals)

              If False, return Von Neumann neighborhood
              :   (exclude diagonals)
            - **include\_center** – If True, return the (x, y) cell as well.
              Otherwise,
              return surrounding cells only.
            - **radius** – radius, in cells, of neighborhood to get.

        Returns:
        :   An iterator of non-None objects in the given neighborhood;
            at most 9 if Moore, 5 if Von-Neumann
            (8 and 4 if not including the center).

    iter\_cell\_list\_contents(*positions*) → [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[source]](_modules/mesa/space.html#MultiGrid.iter_cell_list_contents)

class HexSingleGrid(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *height: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *torus: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *property\_layers: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [PropertyLayer](#mesa.space.PropertyLayer "mesa.space.PropertyLayer") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[PropertyLayer](#mesa.space.PropertyLayer "mesa.space.PropertyLayer")] = None*)[[source]](_modules/mesa/space.html#HexSingleGrid)
:   Bases: `_HexGrid`, [`SingleGrid`](#mesa.space.SingleGrid "mesa.space.SingleGrid")

    Hexagonal SingleGrid: a SingleGrid where neighbors are computed according to a hexagonal tiling of the grid.

    Functions according to odd-q rules.
    See <http://www.redblobgames.com/grids/hexagons/#coordinates> for more.

    This class also maintains an empties property, similar to SingleGrid,
    which provides a set of coordinates for all empty hexagonal cells.

    Properties:
    :   width, height: The grid’s width and height.
        torus: Boolean which determines whether to treat the grid as a torus.
        empties: Returns a set of hexagonal coordinates for all empty cells.

    Initializes a new \_PropertyGrid instance with specified dimensions and optional property layers.

    Parameters:
    :   - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The width of the grid (number of columns).
        - **height** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The height of the grid (number of rows).
        - **torus** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – A boolean indicating if the grid should behave like a torus.
        - **property\_layers** (*None* *|* [*PropertyLayer*](#mesa.space.PropertyLayer "mesa.space.PropertyLayer") *|* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*[*[*PropertyLayer*](#mesa.space.PropertyLayer "mesa.space.PropertyLayer")*]**,* *optional*) – A single PropertyLayer instance,
          a list of PropertyLayer instances, or None to initialize without any property layers.

    Raises:
    :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If a property layer’s dimensions do not match the grid dimensions.

class HexMultiGrid(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *height: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *torus: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *property\_layers: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [PropertyLayer](#mesa.space.PropertyLayer "mesa.space.PropertyLayer") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[PropertyLayer](#mesa.space.PropertyLayer "mesa.space.PropertyLayer")] = None*)[[source]](_modules/mesa/space.html#HexMultiGrid)
:   Bases: `_HexGrid`, [`MultiGrid`](#mesa.space.MultiGrid "mesa.space.MultiGrid")

    Hexagonal MultiGrid: a MultiGrid where neighbors are computed according to a hexagonal tiling of the grid.

    Functions according to odd-q rules.
    See <http://www.redblobgames.com/grids/hexagons/#coordinates> for more.

    Similar to the standard MultiGrid, this class maintains an empties property,
    which is a set of coordinates for all hexagonal cells that currently contain
    no agents. This property is updated automatically as agents are added to or
    removed from the grid.

    Properties:
    :   width, height: The grid’s width and height.
        torus: Boolean which determines whether to treat the grid as a torus.
        empties: Returns a set of hexagonal coordinates for all empty cells.

    Initializes a new \_PropertyGrid instance with specified dimensions and optional property layers.

    Parameters:
    :   - **width** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The width of the grid (number of columns).
        - **height** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The height of the grid (number of rows).
        - **torus** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – A boolean indicating if the grid should behave like a torus.
        - **property\_layers** (*None* *|* [*PropertyLayer*](#mesa.space.PropertyLayer "mesa.space.PropertyLayer") *|* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*[*[*PropertyLayer*](#mesa.space.PropertyLayer "mesa.space.PropertyLayer")*]**,* *optional*) – A single PropertyLayer instance,
          a list of PropertyLayer instances, or None to initialize without any property layers.

    Raises:
    :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If a property layer’s dimensions do not match the grid dimensions.

class ContinuousSpace(*x\_max: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *y\_max: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *torus: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *x\_min: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 0*, *y\_min: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 0*)[[source]](_modules/mesa/space.html#ContinuousSpace)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

    Continuous space where each agent can have an arbitrary position.

    Assumes that all agents have a pos property storing their position as
    an (x, y) tuple.

    This class uses a numpy array internally to store agents in order to speed
    up neighborhood lookups. This array is calculated on the first neighborhood
    lookup, and is updated if agents are added or removed.

    The concept of ‘empty cells’ is not directly applicable in continuous space,
    as positions are not discretized.

    Create a new continuous space.

    Parameters:
    :   - **x\_max** – the maximum x-coordinate
        - **y\_max** – the maximum y-coordinate.
        - **torus** – Boolean for whether the edges loop around.
        - **x\_min** – (default 0) If provided, set the minimum x -coordinate for the space. Below them, values loop to
          the other edge (if torus=True) or raise an exception.
        - **y\_min** – (default 0) If provided, set the minimum y -coordinate for the space. Below them, values loop to
          the other edge (if torus=True) or raise an exception.

    property agents: [AgentSet](apis/agentset.html#mesa.agentset.AgentSet "mesa.agentset.AgentSet")
    :   Return an AgentSet with the agents in the space.

    place\_agent(*agent*, *\*args*, *\*\*kwargs*)[[source]](_modules/mesa/space.html#ContinuousSpace.place_agent)

    move\_agent(*agent: [Agent](#mesa.agent.Agent "mesa.agent.Agent")*, *pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")] | ndarray[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), ...], dtype[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/space.html#ContinuousSpace.move_agent)
    :   Move an agent from its current position to a new position.

        Parameters:
        :   - **agent** – The agent object to move.
            - **pos** – Coordinate tuple to move the agent to.

    remove\_agent(*agent: [Agent](#mesa.agent.Agent "mesa.agent.Agent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/space.html#ContinuousSpace.remove_agent)
    :   Remove an agent from the space.

        Parameters:
        :   **agent** – The agent object to remove

    get\_neighbors(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")] | ndarray[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), ...], dtype[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]]*, *radius: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Agent](#mesa.agent.Agent "mesa.agent.Agent")][[source]](_modules/mesa/space.html#ContinuousSpace.get_neighbors)
    :   Get all agents within a certain radius.

        Parameters:
        :   - **pos** – (x,y) coordinate tuple to center the search at.
            - **radius** – Get all the objects within this distance of the center.
            - **include\_center** – If True, include an object at the *exact* provided
              coordinates. i.e. if you are searching for the
              neighbors of a given agent, True will include that
              agent in the results.

        Notes

        If 1 or more agents are located on pos, include\_center=False will remove all these agents
        from the results. So, if you really want to get the neighbors of a given agent,
        you should set include\_center=True, and then filter the list of agents to remove
        the given agent (i.e., self when calling it from an agent).

    get\_heading(*pos\_1: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")] | ndarray[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), ...], dtype[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]]*, *pos\_2: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")] | ndarray[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), ...], dtype[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]]*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")] | ndarray[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), ...], dtype[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]][[source]](_modules/mesa/space.html#ContinuousSpace.get_heading)
    :   Get the heading vector between two points, accounting for toroidal space.

        It is possible to calculate the heading angle by applying the atan2 function to the
        result.

        Parameters:
        :   - **pos\_1** – Coordinate tuples for both points.
            - **pos\_2** – Coordinate tuples for both points.

    get\_distance(*pos\_1: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")] | ndarray[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), ...], dtype[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]]*, *pos\_2: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")] | ndarray[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), ...], dtype[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]]*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[source]](_modules/mesa/space.html#ContinuousSpace.get_distance)
    :   Get the distance between two point, accounting for toroidal space.

        Parameters:
        :   - **pos\_1** – Coordinate tuples for point1.
            - **pos\_2** – Coordinate tuples for point2.

    torus\_adj(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")] | ndarray[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), ...], dtype[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]]*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")] | ndarray[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), ...], dtype[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]][[source]](_modules/mesa/space.html#ContinuousSpace.torus_adj)
    :   Adjust coordinates to handle torus looping.

        If the coordinate is out-of-bounds and the space is toroidal, return
        the corresponding point within the space. If the space is not toroidal,
        raise an exception.

        Parameters:
        :   **pos** – Coordinate tuple to convert.

    out\_of\_bounds(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")] | ndarray[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), ...], dtype[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]]*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](_modules/mesa/space.html#ContinuousSpace.out_of_bounds)
    :   Check if a point is out of bounds.

class NetworkGrid(*g: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*)[[source]](_modules/mesa/space.html#NetworkGrid)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

    Network Grid where each node contains zero or more agents.

    Create a new network.

    Parameters:
    :   **g** – a NetworkX graph instance.

    property agents: [AgentSet](apis/agentset.html#mesa.agentset.AgentSet "mesa.agentset.AgentSet")
    :   Return an AgentSet with the agents in the space.

    static default\_val() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[source]](_modules/mesa/space.html#NetworkGrid.default_val)
    :   Default value for a new node.

    place\_agent(*agent*, *\*args*, *\*\*kwargs*)[[source]](_modules/mesa/space.html#NetworkGrid.place_agent)

    get\_neighborhood(*node\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](_modules/mesa/space.html#NetworkGrid.get_neighborhood)
    :   Get all adjacent nodes within a certain radius.

        Parameters:
        :   - **node\_id** – node id for which to get neighborhood
            - **include\_center** – boolean to include node itself or not
            - **radius** – size of neighborhood

        Returns:
        :   a list

    get\_neighbors(*node\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Agent](#mesa.agent.Agent "mesa.agent.Agent")][[source]](_modules/mesa/space.html#NetworkGrid.get_neighbors)
    :   Get all agents in adjacent nodes (within a certain radius).

        Parameters:
        :   - **node\_id** – node id for which to get neighbors
            - **include\_center** – whether to include node itself or not
            - **radius** – size of neighborhood in which to find neighbors

        Returns:
        :   list of agents in neighborhood.

    move\_agent(*agent: [Agent](#mesa.agent.Agent "mesa.agent.Agent")*, *node\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/space.html#NetworkGrid.move_agent)
    :   Move an agent from its current node to a new node.

        Parameters:
        :   - **agent** – agent instance
            - **node\_id** – id of node

    remove\_agent(*agent: [Agent](#mesa.agent.Agent "mesa.agent.Agent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/space.html#NetworkGrid.remove_agent)
    :   Remove the agent from the network and set its pos attribute to None.

        Parameters:
        :   **agent** – agent instance

    is\_cell\_empty(*node\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](_modules/mesa/space.html#NetworkGrid.is_cell_empty)
    :   Returns a bool of the contents of a cell.

        Parameters:
        :   **node\_id** – id of node

    get\_cell\_list\_contents(*cell\_list: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Agent](#mesa.agent.Agent "mesa.agent.Agent")][[source]](_modules/mesa/space.html#NetworkGrid.get_cell_list_contents)
    :   Returns a list of the agents contained in the nodes identified in cell\_list.

        Nodes with empty content are excluded.

        Parameters:
        :   **cell\_list** – list of cell ids.

        Returns:
        :   list of the agents contained in the nodes identified in cell\_list.

    get\_all\_cell\_contents() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Agent](#mesa.agent.Agent "mesa.agent.Agent")][[source]](_modules/mesa/space.html#NetworkGrid.get_all_cell_contents)
    :   Returns a list of all the agents in the network.

    iter\_cell\_list\_contents(*cell\_list: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.14)")[[Agent](#mesa.agent.Agent "mesa.agent.Agent")][[source]](_modules/mesa/space.html#NetworkGrid.iter_cell_list_contents)
    :   Returns an iterator of the agents contained in the nodes identified in cell\_list.

        Nodes with empty content are excluded.

        Parameters:
        :   **cell\_list** – list of cell ids.

        Returns:
        :   iterator of the agents contained in the nodes identified in cell\_list.

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

    pos
    :   A reference to the position where this agent is located.

        Type:
        :   Position

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

        Notes

        If you need to do additional cleanup when removing an agent by for example removing
        it from a space, consider extending this method in your own agent class.

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

class Model(*\*args: Any*, *seed: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *rng: RNGLike | SeedLike | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *scenario: S | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*kwargs: Any*)[[source]](_modules/mesa/model.html#Model)
:   Bases: `HasObservables`, [`Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "(in Python v3.14)")

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

        Type:
        :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    time
    :   the current simulation time. Automatically increments by 1.0
        with each step unless controlled by a discrete event simulator.

        Type:
        :   [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")

    random
    :   a seeded python.random number generator.

    rng
    :   a seeded numpy.random.Generator

        Type:
        :   np.random.Generator

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
        - **seed** – the seed for the random number generator
        - **rng** – Pseudorandom number generator state. When rng is None, a new numpy.random.Generator is created
          using entropy from the operating system. Types other than numpy.random.Generator are passed to
          numpy.random.default\_rng to instantiate a Generator.
        - **scenario** – the scenario specifying the computational experiment to run
        - **kwargs** – keyword arguments to pass onto super

    Notes

    you have to pass either seed or rng, but not both.

    running: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    steps: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    time: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")
    :   Observable descriptor.

        An observable is an attribute that emits ObservableSignals.CHANGED whenever it is changed to a different value.

    agent\_id\_counter: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    rng: np.random.Generator

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

    observables = {'agents': frozenset({ModelSignals.AGENT\_ADDED, ModelSignals.AGENT\_REMOVED}), 'time': <enum 'ObservableSignals'>}

    run\_model() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/model.html#Model.run_model)
    :   Run the model until the end condition is reached.

        Overload as needed.

    step() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/model.html#Model.step)
    :   A single step. Fill in here.

    reset\_randomizer(*seed: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/model.html#Model.reset_randomizer)
    :   Reset the model random number generator.

        Parameters:
        :   **seed** – A new seed for the RNG; if None, reset using the current seed

    reset\_rng(*rng: Generator | BitGenerator | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | integer | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | SeedSequence | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](_modules/mesa/model.html#Model.reset_rng)
    :   Reset the model random number generator.

        Parameters:
        :   **rng** – A new seed for the RNG; if None, reset using the current seed

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

batch\_run(*model\_cls: [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[[Model](#mesa.model.Model "mesa.model.Model")]*, *parameters: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)") | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]]*, *number\_processes: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 1*, *iterations: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *data\_collection\_period: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = -1*, *max\_steps: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1000*, *display\_progress: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *rng: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | integer | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | SeedSequence | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | integer | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | SeedSequence] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]][[source]](_modules/mesa/batchrunner.html#batch_run)
:   Batch run a mesa model with a set of parameter values.

    Parameters:
    :   - **model\_cls** (*Type**[*[*Model*](#mesa.Model "mesa.Model")*]*) – The model class to batch-run
        - **parameters** (*Mapping**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *Union**[**Any**,* *Iterable**[**Any**]**]**]*) – Dictionary with model parameters over which to run the model. You can either pass single values or iterables.
        - **number\_processes** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) – Number of processes used, by default 1. Set this to None if you want to use all CPUs.
        - **iterations** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) – Number of iterations for each parameter combination, by default 1
        - **data\_collection\_period** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) – Number of steps after which data gets collected, by default -1 (end of episode)
        - **max\_steps** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) – Maximum number of model steps after which the model halts, by default 1000
        - **display\_progress** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) – Display batch run process, by default True
        - **rng** – a valid value or iterable of values for seeding the random number generator in the model

    Returns:
    :   List[Dict[str, Any]]

    Notes

    batch\_run assumes the model has a datacollector attribute that has a DataCollector object initialized.

On this page

### This Page

- [Show Source](_sources/mesa.md.txt)

---

Original source: https://mesa.readthedocs.io/stable/mesa.html
