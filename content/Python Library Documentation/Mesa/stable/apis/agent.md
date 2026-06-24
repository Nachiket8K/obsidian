---
title: "Agent"
source: "https://mesa.readthedocs.io/stable/apis/agent.html"
imported_from: "Python library documentation"
library: "Mesa"
---

# Agent

Agent related classes.

Core Objects: Agent.

class Agent(*model: M*, *\*args*, *\*\*kwargs*)[[source]](../_modules/mesa/agent.html#Agent)
:   Base class for a model agent in Mesa.

    model
    :   A reference to the model instance.

        Type:
        :   [Model](../mesa.html#mesa.model.Model "mesa.model.Model")

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
    :   - **model** ([*Model*](../mesa.html#mesa.model.Model "mesa.model.Model")) – The model instance in which the agent exists.
        - **args** – Passed on to super.
        - **kwargs** – Passed on to super.

    Notes

    to make proper use of python’s super, in each class remove the arguments and
    keyword arguments you need and pass on the rest to super

    remove() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/agent.html#Agent.remove)
    :   Remove and delete the agent from the model.

        Notes

        If you need to do additional cleanup when removing an agent by for example removing
        it from a space, consider extending this method in your own agent class.

    step() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/agent.html#Agent.step)
    :   A single step of the agent.

    classmethod create\_agents(*model: [Model](../mesa.html#mesa.model.Model "mesa.model.Model")*, *n: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *\*args*, *\*\*kwargs*) → [AgentSet](agentset.html#mesa.agentset.AgentSet "mesa.agentset.AgentSet")[T][[source]](../_modules/mesa/agent.html#Agent.create_agents)
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

    classmethod from\_dataframe(*model: [Model](../mesa.html#mesa.model.Model "mesa.model.Model")*, *df: pd.DataFrame*, *\*\*kwargs*) → [AgentSet](agentset.html#mesa.agentset.AgentSet "mesa.agentset.AgentSet")[T][[source]](../_modules/mesa/agent.html#Agent.from_dataframe)
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

On this page

### This Page

- [Show Source](../_sources/apis/agent.md.txt)

---

Original source: https://mesa.readthedocs.io/stable/apis/agent.html
