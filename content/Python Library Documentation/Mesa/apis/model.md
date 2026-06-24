---
title: "Model"
source: "https://mesa.readthedocs.io/latest/apis/model.html"
imported_from: "Python library documentation"
library: "Mesa"
---

# Model

The model class for Mesa framework.

Core Objects: Model

class Model(*\*args: Any*, *rng: RNGLike | SeedLike | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *scenario: S | [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[S] = <class 'mesa.experimental.scenarios.scenario.Scenario'>*, *\*\*kwargs: Any*)[[source]](../_modules/mesa/model.html#Model)
:   Base class for models in the Mesa ABM library.

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

    register\_agent(*agent: A*)[[source]](../_modules/mesa/model.html#Model.register_agent)
    :   Register the agent with the model.

        Parameters:
        :   **agent** – The agent to register.

        Notes

        This method is called automatically by `Agent.__init__`, so there
        is no need to use this if you are subclassing Agent and calling its
        super in the `__init__` method.

    deregister\_agent(*agent: A*)[[source]](../_modules/mesa/model.html#Model.deregister_agent)
    :   Deregister the agent with the model.

        Parameters:
        :   **agent** – The agent to deregister.

        Notes

        This method is called automatically by `Agent.remove`

    run\_model() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/model.html#Model.run_model)
    :   Run the model until the end condition is reached.

        Overload as needed.

    step() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/model.html#Model.step)
    :   A single step. Fill in here.

    batch()
    :   Return a context manager that batches signals.

        Signals emitted during the batch are buffered and aggregated on exit.
        Nested batches merge into the outer batch; only the outermost dispatches.

        Computed properties may return stale cached values during the batch.
        They will be updated when aggregated signals are dispatched on exit.

    classmethod clear\_all\_class\_subscriptions(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | \_AllSentinel | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*)
    :   Clears all class-level subscriptions for the observable <name>.

        if name is ALL, all subscriptions are removed

        Parameters:
        :   **name** – name of the Observable to unsubscribe for all signal types

    clear\_all\_subscriptions(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | \_AllSentinel | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*)
    :   Clears all instance-level subscriptions for the observable <name>.

        if name is ALL, all subscriptions are removed

        Parameters:
        :   **name** – name of the Observable to unsubscribe for all signal types

    notify(*observable: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *signal\_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | SignalType*, *\*\*kwargs*)
    :   Emit a signal.

        Parameters:
        :   - **observable** – the public name of the observable emitting the signal
            - **signal\_type** – the type of signal to emit
            - **kwargs** – additional keyword arguments to include in the signal

    observe(*observable\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | \_AllSentinel | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *signal\_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | SignalType | \_AllSentinel | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | SignalType]*, *handler: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*)
    :   Subscribe to the Observable <name> for signal\_type.

        Parameters:
        :   - **observable\_name** – name of the Observable to subscribe to
            - **signal\_type** – the type of signal on the Observable to subscribe to
            - **handler** – the handler to call

        Raises:
        :   - [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – if the Observable <name> is not registered or if the Observable
            - **does not emit the given signal\_type** –

    classmethod observe\_class(*observable\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | \_AllSentinel | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *signal\_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | SignalType | \_AllSentinel | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | SignalType]*, *handler: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*)
    :   Subscribe at the class level to the Observable <name> for signal\_type.

        All instances of this class will trigger the handler when they emit this signal.
        Handlers are stored as weak references to prevent memory leaks during experiments.

        Parameters:
        :   - **observable\_name** – name of the Observable to subscribe to
            - **signal\_type** – the type of signal on the Observable to subscribe to
            - **handler** – the handler to call

    remove\_all\_agents()[[source]](../_modules/mesa/model.html#Model.remove_all_agents)
    :   Remove all agents from the model.

        Notes

        This method calls agent.remove for all agents in the model. If you need to remove agents from
        e.g., a SingleGrid, you can either explicitly implement your own agent.remove method or clean this up
        near where you are calling this method.

    suppress()
    :   Return a context manager that suppresses all signals.

        No signals are emitted, buffered, or dispatched during suppression.

        Computed properties may become permanently stale because their
        triggering signals are dropped entirely.

    unobserve(*observable\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | \_AllSentinel | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *signal\_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | SignalType | \_AllSentinel | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | SignalType]*, *handler: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*)
    :   Unsubscribe to the Observable <name> for signal\_type.

        Parameters:
        :   - **observable\_name** – name of the Observable to unsubscribe from
            - **signal\_type** – the type of signal on the Observable to unsubscribe to
            - **handler** – the handler that is unsubscribing

    classmethod unobserve\_class(*observable\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | \_AllSentinel | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *signal\_type: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | SignalType | \_AllSentinel | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | SignalType]*, *handler: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*)
    :   Unsubscribe at the class level to the Observable <name> for signal\_type.

        Parameters:
        :   - **observable\_name** – name of the Observable to unsubscribe from
            - **signal\_type** – the type of signal on the Observable to unsubscribe to
            - **handler** – the handler that is unsubscribing

    schedule\_event(*function: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *\**, *at: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *after: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *priority: [Priority](time.html#mesa.time.Priority "mesa.time.events.Priority") = Priority.DEFAULT*) → [Event](time.html#mesa.time.Event "mesa.time.events.Event")[[source]](../_modules/mesa/model.html#Model.schedule_event)
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

    schedule\_recurring(*function: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *schedule: [Schedule](time.html#mesa.time.Schedule "mesa.time.events.Schedule")*, *priority: [Priority](time.html#mesa.time.Priority "mesa.time.events.Priority") = Priority.DEFAULT*) → [EventGenerator](time.html#mesa.time.EventGenerator "mesa.time.events.EventGenerator")[[source]](../_modules/mesa/model.html#Model.schedule_recurring)
    :   Schedule a recurring event based on a Schedule.

        Parameters:
        :   - **function** – The callable to execute repeatedly
            - **schedule** – The Schedule defining when events occur
            - **priority** – Priority level for generated events

        Returns:
        :   The EventGenerator (can be used to stop)

        Raises:
        :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If the schedule start time is in the past.

    run\_for(*duration: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/model.html#Model.run_for)
    :   Run the model for the specified duration.

        Parameters:
        :   **duration** – Time units to advance

    run\_until(*end\_time: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/model.html#Model.run_until)
    :   Run the model until the specified time.

        Parameters:
        :   **end\_time** – Absolute time to run until

        If model.time is larger than end\_time, the method returns directly.

On this page

[Show Source](../_sources/apis/model.md.txt)

---

Original source: https://mesa.readthedocs.io/latest/apis/model.html
