---
title: "AgentSet"
source: "https://mesa.readthedocs.io/latest/apis/agentset.html"
imported_from: "Python library documentation"
library: "Mesa"
---

# AgentSet

AgentSet related classes.

Core Objects: AgentSet, AbstractAgentSet, \_HardKeyAgentSet, GroupBy.

class AbstractAgentSet[[source]](../_modules/mesa/agentset.html#AbstractAgentSet)
:   An abstract base collection class that represents an ordered set of agents within an agent-based model (ABM).

    This class defines the minimal interface that all AgentSet implementations must follow.
    Subclasses are free to override methods with optimized implementations based on their
    storage mechanism (weak references vs strong references).

    model
    :   The ABM model instance to which this AbstractAgentSet belongs.

        Type:
        :   [Model](../mesa.html#mesa.model.Model "mesa.model.Model")

    select(*filter\_func: Callable[[A], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *at\_most: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = inf*, *inplace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *agent\_type: [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[A] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [AbstractAgentSet](#mesa.agentset.AbstractAgentSet "mesa.agentset.AbstractAgentSet")[A][[source]](../_modules/mesa/agentset.html#AbstractAgentSet.select)
    :   Select a subset of agents from the AbstractAgentSet based on a filter function and/or quantity limit.

        Parameters:
        :   - **filter\_func** (*Callable**[**[*[*Agent*](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*]**,* *optional*) – A function that takes an Agent and returns True if the
              agent should be included in the result. Defaults to None, meaning no filtering is applied.
            - **at\_most** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *|* [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) – The maximum amount of agents to select. Defaults to infinity.
              - If an integer, at most the first number of matching agents are selected.
              - If a float between 0 and 1, at most that fraction of original the agents are selected.
            - **inplace** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) – If True, modifies the current AbstractAgentSet; otherwise, returns a new AbstractAgentSet. Defaults to False.
            - **agent\_type** ([*type*](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")*[*[*Agent*](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*]**,* *optional*) – The class type of the agents to select. Defaults to None, meaning no type filtering is applied.

        Returns:
        :   A new AbstractAgentSet containing the selected agents, unless inplace is True, in which case the current AbstractAgentSet is updated.

        Return type:
        :   [AbstractAgentSet](#mesa.agentset.AbstractAgentSet "mesa.agentset.AbstractAgentSet")

        Notes

        - at\_most just return the first n or fraction of agents. To take a random sample, shuffle() beforehand.
        - at\_most is an upper limit. When specifying other criteria, the number of agents returned can be smaller.

    agg(*attribute: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *func: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)") | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")]*) → [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")][[source]](../_modules/mesa/agentset.html#AbstractAgentSet.agg)
    :   Aggregate an attribute of all agents in the AgentSet using one or more functions.

        Parameters:
        :   - **attribute** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The name of the attribute to aggregate.
            - **func** (*Callable* *|* *Iterable**[**Callable**]*) –
              - If Callable: A single function to apply to the attribute values (e.g., min, max, sum, np.mean)
              - If Iterable: Multiple functions to apply to the attribute values

        Returns:
        :   Result of applying the function(s) to the attribute values.

        Return type:
        :   Any | [Any, …]

        Examples

        # Single function
        avg\_energy = model.agents.agg(“energy”, np.mean)

        # Multiple functions
        min\_wealth, max\_wealth, total\_wealth = model.agents.agg(“wealth”, [min, max, sum])

    get(*attr\_names: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *handle\_missing: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['error', 'default'] = 'error'*, *default\_value: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)") = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")][[source]](../_modules/mesa/agentset.html#AbstractAgentSet.get)

    get(*attr\_names: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *handle\_missing: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['error', 'default'] = 'error'*, *default\_value: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)") = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]]
    :   Retrieve the specified attribute(s) from each agent in the AgentSet.

        Parameters:
        :   - **attr\_names** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *|* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]*) – The name(s) of the attribute(s) to retrieve from each agent.
            - **handle\_missing** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) – How to handle missing attributes. Can be:
              - ‘error’ (default): raises an AttributeError if attribute is missing.
              - ‘default’: returns the specified default\_value.
            - **default\_value** (*Any**,* *optional*) – The default value to return if ‘handle\_missing’ is set to ‘default’
              and the agent does not have the attribute.

        Returns:
        :   A list with the attribute value for each agent if attr\_names is a str.
            list[list[Any]]: A list with a lists of attribute values for each agent if attr\_names is a list of str.

        Return type:
        :   [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[Any]

        Raises:
        :   - [**AttributeError**](https://docs.python.org/3/library/exceptions.html#AttributeError "(in Python v3.14)") – If ‘handle\_missing’ is ‘error’ and the agent does not have the specified attribute(s).
            - [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If an unknown ‘handle\_missing’ option is provided.

    set(*attr\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value: Any*) → [AgentSet](#mesa.agentset.AgentSet "mesa.agentset.AgentSet")[A][[source]](../_modules/mesa/agentset.html#AbstractAgentSet.set)
    :   Set a specified attribute to a given value for all agents in the AgentSet.

        Parameters:
        :   - **attr\_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The name of the attribute to set.
            - **value** (*Any*) – The value to set the attribute to.

        Returns:
        :   The AgentSet instance itself, after setting the attribute.

        Return type:
        :   [AgentSet](#mesa.agentset.AgentSet "mesa.agentset.AgentSet")

    to\_list() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[A][[source]](../_modules/mesa/agentset.html#AbstractAgentSet.to_list)
    :   Convert the AbstractAgentSet to a list.

        Returns:
        :   A list containing all agents in the AbstractAgentSet.

        Return type:
        :   [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")]

        Notes

        This method provides an explicit way to convert the AgentSet to a list.
        It is the recommended approach when list operations (indexing, slicing)
        are needed, as direct sequence operations on AgentSet are deprecated
        and will be removed in Mesa 4.0.

    abstractmethod add(*agent: A*)[[source]](../_modules/mesa/agentset.html#AbstractAgentSet.add)
    :   Add an agent to the AbstractAgentSet.

        Parameters:
        :   **agent** ([*Agent*](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")) – The agent to add to the set.

        This method is an implementation of the abstract method from MutableSet.

    abstractmethod discard(*agent: A*)[[source]](../_modules/mesa/agentset.html#AbstractAgentSet.discard)
    :   Remove an agent from the AbstractAgentSet if it exists.

        This method does not raise an error if the agent is not present.

        Parameters:
        :   **agent** ([*Agent*](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")) – The agent to remove from the set.

        This method is an implementation of the abstract method from MutableSet.

    abstractmethod remove(*agent: A*)[[source]](../_modules/mesa/agentset.html#AbstractAgentSet.remove)
    :   Remove an agent from the AbstractAgentSet.

        Raises:
        :   **An Exception if the agent is not present.** –

        Parameters:
        :   **agent** ([*Agent*](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")) – The agent to remove from the set.

        This method is an implementation of the abstract method from MutableSet.

    groupby(*by: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *result\_type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['agentset', 'list'] = 'agentset'*) → [GroupBy](#mesa.agentset.GroupBy "mesa.agentset.GroupBy")[[source]](../_modules/mesa/agentset.html#AbstractAgentSet.groupby)
    :   Group agents by the specified attribute or return from the callable.

        Parameters:
        :   - **by** (*Callable**,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) –

              used to determine what to group agents by

              - if `by` is a callable, it will be called for each agent and the return is used
                for grouping
              - if `by` is a str, it should refer to an attribute on the agent and the value
                of this attribute will be used for grouping
            - **result\_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) – The datatype for the resulting groups {“agentset”, “list”}

        Returns:
        :   GroupBy

        Notes

        There might be performance benefits to using result\_type=’list’ if you don’t need the advanced functionality
        of an AbstractAgentSet.

    abstractmethod shuffle(*inplace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [AbstractAgentSet](#mesa.agentset.AbstractAgentSet "mesa.agentset.AbstractAgentSet")[A][[source]](../_modules/mesa/agentset.html#AbstractAgentSet.shuffle)
    :   Randomly shuffle the order of agents in the AbstractAgentSet.

    abstractmethod sort(*key: Callable[[A], Any] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *ascending: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *inplace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [AbstractAgentSet](#mesa.agentset.AbstractAgentSet "mesa.agentset.AbstractAgentSet")[A][[source]](../_modules/mesa/agentset.html#AbstractAgentSet.sort)
    :   Sort the agents in the AbstractAgentSet based on a specified attribute or custom function.

    abstractmethod do(*method: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | Callable*, *\*args*, *\*\*kwargs*) → [AbstractAgentSet](#mesa.agentset.AbstractAgentSet "mesa.agentset.AbstractAgentSet")[A][[source]](../_modules/mesa/agentset.html#AbstractAgentSet.do)
    :   Invoke a method or function on each agent in the AbstractAgentSet.

    abstractmethod shuffle\_do(*method: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | Callable*, *\*args*, *\*\*kwargs*) → [AbstractAgentSet](#mesa.agentset.AbstractAgentSet "mesa.agentset.AbstractAgentSet")[A][[source]](../_modules/mesa/agentset.html#AbstractAgentSet.shuffle_do)
    :   Shuffle the agents in the AbstractAgentSet and then invoke a method or function on each agent.

    abstractmethod map(*method: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *\*args*, *\*\*kwargs*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")][[source]](../_modules/mesa/agentset.html#AbstractAgentSet.map)
    :   Invoke a method or function on each agent in the AbstractAgentSet and return the results.

    clear()
    :   This is slow (creates N new iterators!) but effective.

    isdisjoint(*other*)
    :   Return True if two sets have a null intersection.

    pop()
    :   Return the popped value. Raise KeyError if empty.

class AgentSet(*agents: Iterable[A]*, *random: Random | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/mesa/agentset.html#AgentSet)
:   A collection class that represents an ordered set of agents using weak references.

    This implementation uses weak references to agents, allowing for efficient management
    of agent lifecycles without preventing garbage collection.

    random
    :   The random number generator for this agent set.

        Type:
        :   Random

    Notes

    The AgentSet maintains weak references to agents, which means that agents not
    referenced elsewhere in the program may be automatically removed from the AgentSet.
    This is the default implementation for most use cases where automatic cleanup is desired.

    Performance-critical methods are optimized to work directly with weak references,
    avoiding the overhead of creating strong references during iteration.

    Initialize the AgentSet with weak references to agents.

    Parameters:
    :   - **agents** (*Iterable**[*[*Agent*](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*]*) – An iterable of Agent objects to be included in the set.
        - **random** (*Random* *|* *None*) – The random number generator for this agent set.

    shuffle(*inplace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [AgentSet](#mesa.agentset.AgentSet "mesa.agentset.AgentSet")[A][[source]](../_modules/mesa/agentset.html#AgentSet.shuffle)
    :   Randomly shuffle the order of agents in the AgentSet.

        Parameters:
        :   **inplace** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) – If True, shuffles the agents in the current AgentSet; otherwise, returns a new shuffled AgentSet. Defaults to False.

        Returns:
        :   A shuffled AgentSet. Returns the current AgentSet if inplace is True.

        Return type:
        :   [AgentSet](#mesa.agentset.AgentSet "mesa.agentset.AgentSet")

        Using inplace = True is more performant

    sort(*key: Callable[[A], Any] | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *ascending: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *inplace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [AgentSet](#mesa.agentset.AgentSet "mesa.agentset.AgentSet")[A][[source]](../_modules/mesa/agentset.html#AgentSet.sort)
    :   Sort the agents in the AgentSet based on a specified attribute or custom function.

        Parameters:
        :   - **key** (*Callable**[**[*[*Agent*](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*]**,* *Any**]* *|* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – A function or attribute name based on which the agents are sorted.
            - **ascending** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) – If True, the agents are sorted in ascending order. Defaults to False.
            - **inplace** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) – If True, sorts the agents in the current AgentSet; otherwise, returns a new sorted AgentSet. Defaults to False.

        Returns:
        :   A sorted AgentSet. Returns the current AgentSet if inplace is True.

        Return type:
        :   [AgentSet](#mesa.agentset.AgentSet "mesa.agentset.AgentSet")

    do(*method: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | Callable*, *\*args*, *\*\*kwargs*) → [AgentSet](#mesa.agentset.AgentSet "mesa.agentset.AgentSet")[A][[source]](../_modules/mesa/agentset.html#AgentSet.do)
    :   Invoke a method or function on each agent in the AgentSet.

        Parameters:
        :   - **method** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *callable*) –

              the callable to do on each agent

              - in case of str, the name of the method to call on each agent.
              - in case of callable, the function to be called with each agent as first argument
            - **\*args** – Variable length argument list passed to the callable being called.
            - **\*\*kwargs** – Arbitrary keyword arguments passed to the callable being called.

        Returns:
        :   The AgentSet instance itself.

        Return type:
        :   [AgentSet](#mesa.agentset.AgentSet "mesa.agentset.AgentSet")

    shuffle\_do(*method: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | Callable*, *\*args*, *\*\*kwargs*) → [AgentSet](#mesa.agentset.AgentSet "mesa.agentset.AgentSet")[A][[source]](../_modules/mesa/agentset.html#AgentSet.shuffle_do)
    :   Shuffle the agents in the AgentSet and then invoke a method or function on each agent.

        It’s a fast, optimized version of calling shuffle() followed by do().

    map(*method: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *\*args*, *\*\*kwargs*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")][[source]](../_modules/mesa/agentset.html#AgentSet.map)
    :   Invoke a method or function on each agent in the AgentSet and return the results.

        Parameters:
        :   - **method** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *callable*) –

              the callable to apply on each agent

              - in case of str, the name of the method to call on each agent.
              - in case of callable, the function to be called with each agent as first argument
            - **\*args** – Variable length argument list passed to the callable being called.
            - **\*\*kwargs** – Arbitrary keyword arguments passed to the callable being called.

        Returns:
        :   The results of the callable calls

        Return type:
        :   [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[Any]

    add(*agent: A*)[[source]](../_modules/mesa/agentset.html#AgentSet.add)
    :   Add an agent to the AgentSet.

        Parameters:
        :   **agent** ([*Agent*](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")) – The agent to add to the set.

        This method is an implementation of the abstract method from MutableSet.

    discard(*agent: A*)[[source]](../_modules/mesa/agentset.html#AgentSet.discard)
    :   Remove an agent from the AgentSet if it exists.

        This method does not raise an error if the agent is not present.

        Parameters:
        :   **agent** ([*Agent*](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")) – The agent to remove from the set.

        This method is an implementation of the abstract method from MutableSet.

    remove(*agent: A*)[[source]](../_modules/mesa/agentset.html#AgentSet.remove)
    :   Remove an agent from the AgentSet.

        This method raises an error if the agent is not present.

        Parameters:
        :   **agent** ([*Agent*](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")) – The agent to remove from the set.

        This method is an implementation of the abstract method from MutableSet.

    agg(*attribute: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *func: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)") | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")]*) → [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]
    :   Aggregate an attribute of all agents in the AgentSet using one or more functions.

        Parameters:
        :   - **attribute** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The name of the attribute to aggregate.
            - **func** (*Callable* *|* *Iterable**[**Callable**]*) –
              - If Callable: A single function to apply to the attribute values (e.g., min, max, sum, np.mean)
              - If Iterable: Multiple functions to apply to the attribute values

        Returns:
        :   Result of applying the function(s) to the attribute values.

        Return type:
        :   Any | [Any, …]

        Examples

        # Single function
        avg\_energy = model.agents.agg(“energy”, np.mean)

        # Multiple functions
        min\_wealth, max\_wealth, total\_wealth = model.agents.agg(“wealth”, [min, max, sum])

    clear()
    :   This is slow (creates N new iterators!) but effective.

    count(*value*) → integer -- return number of occurrences of value

    get(*attr\_names*, *handle\_missing='error'*, *default\_value=None*)
    :   Retrieve the specified attribute(s) from each agent in the AgentSet.

        Parameters:
        :   - **attr\_names** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *|* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]*) – The name(s) of the attribute(s) to retrieve from each agent.
            - **handle\_missing** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) – How to handle missing attributes. Can be:
              - ‘error’ (default): raises an AttributeError if attribute is missing.
              - ‘default’: returns the specified default\_value.
            - **default\_value** (*Any**,* *optional*) – The default value to return if ‘handle\_missing’ is set to ‘default’
              and the agent does not have the attribute.

        Returns:
        :   A list with the attribute value for each agent if attr\_names is a str.
            list[list[Any]]: A list with a lists of attribute values for each agent if attr\_names is a list of str.

        Return type:
        :   [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[Any]

        Raises:
        :   - [**AttributeError**](https://docs.python.org/3/library/exceptions.html#AttributeError "(in Python v3.14)") – If ‘handle\_missing’ is ‘error’ and the agent does not have the specified attribute(s).
            - [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If an unknown ‘handle\_missing’ option is provided.

    groupby(*by: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *result\_type: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['agentset', 'list'] = 'agentset'*) → [GroupBy](#mesa.agentset.GroupBy "mesa.agentset.GroupBy")
    :   Group agents by the specified attribute or return from the callable.

        Parameters:
        :   - **by** (*Callable**,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) –

              used to determine what to group agents by

              - if `by` is a callable, it will be called for each agent and the return is used
                for grouping
              - if `by` is a str, it should refer to an attribute on the agent and the value
                of this attribute will be used for grouping
            - **result\_type** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *optional*) – The datatype for the resulting groups {“agentset”, “list”}

        Returns:
        :   GroupBy

        Notes

        There might be performance benefits to using result\_type=’list’ if you don’t need the advanced functionality
        of an AbstractAgentSet.

    index(*value*[, *start*[, *stop*]]) → integer -- return first index of value.
    :   Raises ValueError if the value is not present.

        Supporting start and stop arguments is optional, but
        recommended.

    isdisjoint(*other*)
    :   Return True if two sets have a null intersection.

    pop()
    :   Return the popped value. Raise KeyError if empty.

    select(*filter\_func: Callable[[A], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *at\_most: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = inf*, *inplace: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *agent\_type: [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[A] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [AbstractAgentSet](#mesa.agentset.AbstractAgentSet "mesa.agentset.AbstractAgentSet")[A]
    :   Select a subset of agents from the AbstractAgentSet based on a filter function and/or quantity limit.

        Parameters:
        :   - **filter\_func** (*Callable**[**[*[*Agent*](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*]**,* [*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*]**,* *optional*) – A function that takes an Agent and returns True if the
              agent should be included in the result. Defaults to None, meaning no filtering is applied.
            - **at\_most** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") *|* [*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) – The maximum amount of agents to select. Defaults to infinity.
              - If an integer, at most the first number of matching agents are selected.
              - If a float between 0 and 1, at most that fraction of original the agents are selected.
            - **inplace** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) – If True, modifies the current AbstractAgentSet; otherwise, returns a new AbstractAgentSet. Defaults to False.
            - **agent\_type** ([*type*](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")*[*[*Agent*](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*]**,* *optional*) – The class type of the agents to select. Defaults to None, meaning no type filtering is applied.

        Returns:
        :   A new AbstractAgentSet containing the selected agents, unless inplace is True, in which case the current AbstractAgentSet is updated.

        Return type:
        :   [AbstractAgentSet](#mesa.agentset.AbstractAgentSet "mesa.agentset.AbstractAgentSet")

        Notes

        - at\_most just return the first n or fraction of agents. To take a random sample, shuffle() beforehand.
        - at\_most is an upper limit. When specifying other criteria, the number of agents returned can be smaller.

    set(*attr\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *value: Any*) → [AgentSet](#mesa.agentset.AgentSet "mesa.agentset.AgentSet")[A]
    :   Set a specified attribute to a given value for all agents in the AgentSet.

        Parameters:
        :   - **attr\_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The name of the attribute to set.
            - **value** (*Any*) – The value to set the attribute to.

        Returns:
        :   The AgentSet instance itself, after setting the attribute.

        Return type:
        :   [AgentSet](#mesa.agentset.AgentSet "mesa.agentset.AgentSet")

    to\_list() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[A]
    :   Convert the AbstractAgentSet to a list.

        Returns:
        :   A list containing all agents in the AbstractAgentSet.

        Return type:
        :   [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")]

        Notes

        This method provides an explicit way to convert the AgentSet to a list.
        It is the recommended approach when list operations (indexing, slicing)
        are needed, as direct sequence operations on AgentSet are deprecated
        and will be removed in Mesa 4.0.

class GroupBy(*groups: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") | [AbstractAgentSet](#mesa.agentset.AbstractAgentSet "mesa.agentset.AbstractAgentSet")]*)[[source]](../_modules/mesa/agentset.html#GroupBy)
:   Helper class for AgentSet.groupby.

    groups
    :   A dictionary with the group\_name as key and group as values

        Type:
        :   [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")

    Initialize a GroupBy instance.

    Parameters:
    :   **groups** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – A dictionary with the group\_name as key and group as values

    get\_group(*name: [Hashable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "(in Python v3.14)")*, *default: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)") = <object object>*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)") | [AbstractAgentSet](#mesa.agentset.AbstractAgentSet "mesa.agentset.AbstractAgentSet") | [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")[[source]](../_modules/mesa/agentset.html#GroupBy.get_group)
    :   Return the group for the given name.

        Parameters:
        :   - **name** (*Hashable*) – The group name to retrieve.
            - **default** (*Any**,* *optional*) – Value to return when the group is missing.

        Raises:
        :   [**KeyError**](https://docs.python.org/3/library/exceptions.html#KeyError "(in Python v3.14)") – If the group does not exist and no default is provided.

    map(*method: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *\*args*, *\*\*kwargs*) → [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")][[source]](../_modules/mesa/agentset.html#GroupBy.map)
    :   Apply the specified callable to each group and return the results.

        Parameters:
        :   - **method** (*Callable**,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) –

              The callable to apply to each group,

              - if `method` is a callable, it will be called it will be called with the group as first argument
              - if `method` is a str, it should refer to a method on the group

              Additional arguments and keyword arguments will be passed on to the callable.
            - **args** – arguments to pass to the callable
            - **kwargs** – keyword arguments to pass to the callable

        Returns:
        :   dict with group\_name as key and the return of the method as value

        Notes

        this method is useful for methods or functions that do return something. It
        will break method chaining. For that, use `do` instead.

    do(*method: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)") | [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *\*args*, *\*\*kwargs*) → [GroupBy](#mesa.agentset.GroupBy "mesa.agentset.GroupBy")[[source]](../_modules/mesa/agentset.html#GroupBy.do)
    :   Apply the specified callable to each group.

        Parameters:
        :   - **method** (*Callable**,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) –

              The callable to apply to each group,

              - if `method` is a callable, it will be called it will be called with the group as first argument
              - if `method` is a str, it should refer to a method on the group

              Additional arguments and keyword arguments will be passed on to the callable.
            - **args** – arguments to pass to the callable
            - **kwargs** – keyword arguments to pass to the callable

        Returns:
        :   the original GroupBy instance

        Notes

        this method is useful for methods or functions that don’t return anything and/or
        if you want to chain multiple do calls

    count() → [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](../_modules/mesa/agentset.html#GroupBy.count)
    :   Return the count of agents in each group.

        Returns:
        :   A dictionary mapping group names to the number of agents in each group.

        Return type:
        :   [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")

    agg(*attr\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *func: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*) → [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[Hashable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Hashable "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")][[source]](../_modules/mesa/agentset.html#GroupBy.agg)
    :   Aggregate the values of a specific attribute across each group using the provided function.

        Parameters:
        :   - **attr\_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The name of the attribute to aggregate.
            - **func** (*Callable*) – The function to apply (e.g., sum, min, max, mean).

        Returns:
        :   A dictionary mapping group names to the result of applying the aggregation function.

        Return type:
        :   [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[Hashable, Any]

On this page

[Show Source](../_sources/apis/agentset.md.txt)

---

Original source: https://mesa.readthedocs.io/latest/apis/agentset.html
