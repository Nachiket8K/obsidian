---
title: "Discrete Space"
source: "https://mesa.readthedocs.io/latest/apis/discrete_space.html"
imported_from: "Python library documentation"
library: "Mesa"
---

# Discrete Space

Cell spaces for active, property-rich spatial modeling in Mesa.

Cell spaces extend Mesa’s spatial modeling capabilities by making the space itself active -
each position (cell) can have properties and behaviors rather than just containing agents.
This enables more sophisticated environmental modeling and agent-environment interactions.

Key components:
- Cells: Active positions that can have properties and contain agents
- CellAgents: Agents that understand how to interact with cells
- Spaces: Different cell organization patterns (grids, networks, etc.)

This is particularly useful for models where the environment plays an active role,
like resource growth, pollution diffusion, or infrastructure networks. The cell
space system is experimental and under active development.

class Cell(*coordinate: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), ...]*, *position: ndarray | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *capacity: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *random: [Random](https://docs.python.org/3/library/random.html#random.Random "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/mesa/discrete_space/cell.html#Cell)
:   The cell represents a position in a discrete space.

    coordinate
    :   the logical position(or index) of the cell in the discrete space

        Type:
        :   Coordinate

    position
    :   the physical position of the cell in the discrete space

        Type:
        :   np.ndarray | None

    agents
    :   the agents occupying the cell

        Type:
        :   List[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")]

    capacity
    :   the maximum number of agents that can simultaneously occupy the cell

        Type:
        :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    random
    :   the random number generator

        Type:
        :   Random

    Initialise the cell.

    Parameters:
    :   - **coordinate** – coordinates of the cell
        - **position** – physical coordinates of the cell
        - **capacity** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – the capacity of the cell. If None, the capacity is infinite
        - **random** (*Random*) – the random number generator to use

    property position: ndarray
    :   Get the physical position of the cell.

        Returns:
        :   Physical position of the cell

        Return type:
        :   np.ndarray

    connect(*other: [Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")*, *key: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), ...] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/discrete_space/cell.html#Cell.connect)
    :   Connects this cell to another cell.

        Parameters:
        :   - **other** ([*Cell*](#mesa.discrete_space.__init__.Cell "mesa.discrete_space.__init__.Cell")) – other cell to connect to
            - **key** (*Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *...**]*) – key for the connection. Should resemble a relative coordinate

    disconnect(*other: [Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/discrete_space/cell.html#Cell.disconnect)
    :   Disconnects this cell from another cell.

        Parameters:
        :   **other** ([*Cell*](#mesa.discrete_space.__init__.Cell "mesa.discrete_space.__init__.Cell")) – other cell to remove from connections

    add\_agent(*agent: [CellAgent](#mesa.discrete_space.cell_agent.CellAgent "mesa.discrete_space.cell_agent.CellAgent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/discrete_space/cell.html#Cell.add_agent)
    :   Adds an agent to the cell.

        Parameters:
        :   **agent** ([*CellAgent*](#mesa.discrete_space.__init__.CellAgent "mesa.discrete_space.__init__.CellAgent")) – agent to add to this Cell

    remove\_agent(*agent: [CellAgent](#mesa.discrete_space.cell_agent.CellAgent "mesa.discrete_space.cell_agent.CellAgent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/discrete_space/cell.html#Cell.remove_agent)
    :   Removes an agent from the cell.

        Parameters:
        :   **agent** ([*CellAgent*](#mesa.discrete_space.__init__.CellAgent "mesa.discrete_space.__init__.CellAgent")) – agent to remove from this cell

    property is\_empty: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
    :   Returns a bool of the contents of a cell.

    property is\_full: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
    :   Returns a bool of the contents of a cell.

    property agents: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[CellAgent](#mesa.discrete_space.cell_agent.CellAgent "mesa.discrete_space.cell_agent.CellAgent")]
    :   Returns a list of the agents occupying the cell.

    property neighborhood: [CellCollection](#mesa.discrete_space.cell_collection.CellCollection "mesa.discrete_space.cell_collection.CellCollection")[[Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")]
    :   Returns the direct neighborhood of the cell.

        This is equivalent to cell.get\_neighborhood(radius=1)

    get\_neighborhood(*radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [CellCollection](#mesa.discrete_space.cell_collection.CellCollection "mesa.discrete_space.cell_collection.CellCollection")[[Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")][[source]](../_modules/mesa/discrete_space/cell.html#Cell.get_neighborhood)
    :   Returns a list of all neighboring cells for the given radius.

        For getting the direct neighborhood (i.e., radius=1) you can also use
        the neighborhood property.

        Parameters:
        :   - **radius** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – the radius of the neighborhood
            - **include\_center** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – include the center of the neighborhood

        Returns:
        :   a list of all neighboring cells

class CellAgent(*model: M*, *\*args*, *\*\*kwargs*)[[source]](../_modules/mesa/discrete_space/cell_agent.html#CellAgent)
:   Cell Agent is an extension of the Agent class and adds behavior for moving in discrete spaces.

    cell
    :   The cell the agent is currently in.

        Type:
        :   [Cell](#mesa.discrete_space.__init__.Cell "mesa.discrete_space.__init__.Cell")

    Create a new agent.

    Parameters:
    :   - **model** ([*Model*](../mesa.html#mesa.model.Model "mesa.model.Model")) – The model instance in which the agent exists.
        - **args** – Passed on to super.
        - **kwargs** – Passed on to super.

    Notes

    to make proper use of python’s super, in each class remove the arguments and
    keyword arguments you need and pass on the rest to super

    remove()[[source]](../_modules/mesa/discrete_space/cell_agent.html#CellAgent.remove)
    :   Remove the agent from the model.

class CellCollection(*cells: Mapping[T, [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[CellAgent](#mesa.discrete_space.__init__.CellAgent "mesa.discrete_space.__init__.CellAgent")]] | Iterable[T]*, *random: Random | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/mesa/discrete_space/cell_collection.html#CellCollection)
:   An immutable collection of cells.

    cells[[source]](../_modules/mesa/discrete_space/cell_collection.html#CellCollection.cells)
    :   The list of cells this collection represents

        Type:
        :   List[[Cell](#mesa.discrete_space.__init__.Cell "mesa.discrete_space.__init__.Cell")]

    agents
    :   List of agents occupying the cells in this collection

        Type:
        :   List[[CellAgent](#mesa.discrete_space.__init__.CellAgent "mesa.discrete_space.__init__.CellAgent")]

    random
    :   The random number generator

        Type:
        :   Random

    Notes

    A UserWarning is issued if random=None. You can resolve this warning by explicitly
    passing a random number generator. In most cases, this will be the seeded random number
    generator in the model. So, you would do random=self.random in a Model or Agent instance.

    Initialize a CellCollection.

    Parameters:
    :   - **cells** – cells to add to the collection
        - **random** – a seeded random number generator.

    select\_random\_cell(*default=<object object>*) → T | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/discrete_space/cell_collection.html#CellCollection.select_random_cell)
    :   Select a random cell from the collection.

        Parameters:
        :   **default** – Value to return if the collection is empty.
            If not provided, raises LookupError.

        Returns:
        :   A random cell, or the default value if provided and collection is empty.

        Return type:
        :   T

        Raises:
        :   [**LookupError**](https://docs.python.org/3/library/exceptions.html#LookupError "(in Python v3.14)") – If collection is empty and no default is provided.

    select\_random\_agent(*default=<object object>*) → [CellAgent](#mesa.discrete_space.__init__.CellAgent "mesa.discrete_space.__init__.CellAgent") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/discrete_space/cell_collection.html#CellCollection.select_random_agent)
    :   Select a random agent from the collection.

        Parameters:
        :   **default** – Value to return if the collection is empty.
            If not provided, raises LookupError.

        Returns:
        :   A random agent, or the default value if provided and collection is empty.

        Return type:
        :   [CellAgent](#mesa.discrete_space.__init__.CellAgent "mesa.discrete_space.__init__.CellAgent")

        Raises:
        :   [**LookupError**](https://docs.python.org/3/library/exceptions.html#LookupError "(in Python v3.14)") – If collection is empty and no default is provided.

    select(*filter\_func: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")[[T], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *at\_most: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = inf*)[[source]](../_modules/mesa/discrete_space/cell_collection.html#CellCollection.select)
    :   Select cells based on filter function.

        Parameters:
        :   - **filter\_func** – filter function
            - **at\_most** – The maximum amount of cells to select. Defaults to infinity.
              - If an integer, at most the first number of matching cells is selected.
              - If a float between 0 and 1, at most that fraction of original number of cells

        Returns:
        :   CellCollection

class DiscreteSpace(*capacity: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *cell\_klass: [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[T] = <class 'mesa.discrete\_space.cell.Cell'>*, *random: [Random](https://docs.python.org/3/library/random.html#random.Random "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/mesa/discrete_space/discrete_space.html#DiscreteSpace)
:   Base class for all discrete spaces.

    capacity
    :   The capacity of the cells in the discrete space

        Type:
        :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    all\_cells[[source]](../_modules/mesa/discrete_space/discrete_space.html#DiscreteSpace.all_cells)
    :   The cells composing the discrete space

        Type:
        :   [CellCollection](#mesa.discrete_space.__init__.CellCollection "mesa.discrete_space.__init__.CellCollection")

    random
    :   The random number generator

        Type:
        :   Random

    cell\_klass
    :   the type of cell class

        Type:
        :   Type

    empties
    :   collection of all cells that are empty

        Type:
        :   [CellCollection](#mesa.discrete_space.__init__.CellCollection "mesa.discrete_space.__init__.CellCollection")

    property\_layers
    :   property\_layer of the discrete space

        Type:
        :   [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), np.ndarray]

    Notes

    A UserWarning is issued if random=None. You can resolve this warning by explicitly
    passing a random number generator. In most cases, this will be the seeded random number
    generator in the model. So, you would do random=self.random in a Model or Agent instance.

    Instantiate a DiscreteSpace.

    Parameters:
    :   - **capacity** – capacity of cells
        - **cell\_klass** – base class for all cells
        - **random** – random number generator

    property agents: [AgentSet](agentset.html#mesa.agentset.AgentSet "mesa.agentset.AgentSet")
    :   Return an AgentSet with the agents in the space.

    abstractmethod find\_nearest\_cell(*position: ndarray*) → T[[source]](../_modules/mesa/discrete_space/discrete_space.html#DiscreteSpace.find_nearest_cell)
    :   Find the cell at or nearest to the given position.

    add\_cell(*cell: T*)[[source]](../_modules/mesa/discrete_space/discrete_space.html#DiscreteSpace.add_cell)
    :   Add a cell to the space.

        Parameters:
        :   **cell** – cell to add

        Discrete spaces rely on caching neighborhood relations for speedups. Adding or removing cells and
        connections at runtime is possible. However, only the caches of cells directly affected will be cleared. So
        if you rely on getting neighborhoods of cells with a radius higher than 1, these might not be cleared
        correctly if you are adding or removing cells and connections at runtime.

        Coordinate Collision: If a cell already exists at the specified
        coordinates (e.g., cell1), it will be overwritten silently by the
        new cell (cell2).

        Ensure the target coordinates are vacant before calling this method.

    remove\_cell(*cell: T*)[[source]](../_modules/mesa/discrete_space/discrete_space.html#DiscreteSpace.remove_cell)
    :   Remove a cell from the space.

        Discrete spaces rely on caching neighborhood relations for speedups. Adding or removing cells and
        connections at runtime is possible. However, only the caches of cells directly affected will be cleared. So
        if you rely on getting neighborhoods of cells with a radius higher than 1, these might not be cleared
        correctly if you are adding or removing cells and connections at runtime.

    add\_connection(*cell1: T*, *cell2: T*)[[source]](../_modules/mesa/discrete_space/discrete_space.html#DiscreteSpace.add_connection)
    :   Add a connection between the two cells.

        Discrete spaces rely on caching neighborhood relations for speedups. Adding or removing cells and
        connections at runtime is possible. However, only the caches of cells directly affected will be cleared. So
        if you rely on getting neighborhoods of cells with a radius higher than 1, these might not be cleared
        correctly if you are adding or removing cells and connections at runtime.

    remove\_connection(*cell1: T*, *cell2: T*)[[source]](../_modules/mesa/discrete_space/discrete_space.html#DiscreteSpace.remove_connection)
    :   Remove a connection between the two cells.

        Discrete spaces rely on caching neighborhood relations for speedups. Adding or removing cells and
        connections at runtime is possible. However, only the caches of cells directly affected will be cleared. So
        if you rely on getting neighborhoods of cells with a radius higher than 1, these might not be cleared
        correctly if you are adding or removing cells and connections at runtime.

    property all\_cells[[source]](../_modules/mesa/discrete_space/discrete_space.html#DiscreteSpace.all_cells)
    :   Return all cells in space.

    property empties: [CellCollection](#mesa.discrete_space.cell_collection.CellCollection "mesa.discrete_space.cell_collection.CellCollection")[T]
    :   Return all empty in spaces.

    select\_random\_empty\_cell() → T[[source]](../_modules/mesa/discrete_space/discrete_space.html#DiscreteSpace.select_random_empty_cell)
    :   Select random empty cell.

class FixedAgent(*model: M*, *\*args*, *\*\*kwargs*)[[source]](../_modules/mesa/discrete_space/cell_agent.html#FixedAgent)
:   A patch in a 2D grid.

    Create a new agent.

    Parameters:
    :   - **model** ([*Model*](../mesa.html#mesa.model.Model "mesa.model.Model")) – The model instance in which the agent exists.
        - **args** – Passed on to super.
        - **kwargs** – Passed on to super.

    Notes

    to make proper use of python’s super, in each class remove the arguments and
    keyword arguments you need and pass on the rest to super

    remove()[[source]](../_modules/mesa/discrete_space/cell_agent.html#FixedAgent.remove)
    :   Remove the agent from the model.

class Grid(*dimensions: ~collections.abc.Sequence[int], torus: bool = False, capacity: float | None = None, random: ~random.Random | None = None, cell\_klass: type[~mesa.discrete\_space.grid.T] = <class 'mesa.discrete\_space.cell.Cell'>*)[[source]](../_modules/mesa/discrete_space/grid.html#Grid)
:   Base class for all grid classes.

    dimensions
    :   the dimensions of the grid

        Type:
        :   Sequence[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]

    torus
    :   whether the grid is a torus

        Type:
        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    capacity
    :   the capacity of a grid cell

        Type:
        :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    random
    :   the random number generator

        Type:
        :   Random

    \_try\_random
    :   whether to get empty cell be repeatedly trying random cell

        Type:
        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    Notes

    width and height are accessible via property\_layers, higher dimensions can be retrieved via dimensions

    Initialise the grid class.

    Parameters:
    :   - **dimensions** – the dimensions of the space
        - **torus** – whether the space wraps
        - **capacity** – capacity of the grid cell
        - **random** – a random number generator
        - **cell\_klass** – the base class to use for the cells

    property width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
    :   Convenience access to the width of the grid.

    property height: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
    :   Convenience access to the height of the grid.

    create\_property\_layer(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *default\_value=0.0*, *dtype=<class 'float'>*, *read\_only: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → ndarray[[source]](../_modules/mesa/discrete_space/grid.html#Grid.create_property_layer)
    :   Create a property layer array and attach it to cells.

        Warning:
        Do not reassign grid.name directly — this will detach it from
        property\_layers and break cell-level access. Use in-place operations.

        > grid.sugar[:] = 0 # correct
        > grid.sugar = array # wrong — breaks cell access

    add\_property\_layer(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *array: ndarray*, *read\_only: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/discrete_space/grid.html#Grid.add_property_layer)
    :   Attach an existing array as a property layer. Shape must match self.dimensions.

        Warning:
        Do not reassign grid.name directly — this will detach it from
        property\_layers and break cell-level access. Use in-place operations.

        > grid.sugar[:] = 0 # correct
        > grid.sugar = array # wrong — breaks cell access

    remove\_property\_layer(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/discrete_space/grid.html#Grid.remove_property_layer)
    :   Remove a property\_layer.

        Parameters:
        :   **name** – property\_layer name.

    get\_neighborhood\_mask(*coordinate*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → ndarray[[source]](../_modules/mesa/discrete_space/grid.html#Grid.get_neighborhood_mask)
    :   Return a boolean mask shaped like `self.dimensions` for a neighborhood.

    find\_nearest\_cell(*position: ndarray*) → T[[source]](../_modules/mesa/discrete_space/grid.html#Grid.find_nearest_cell)
    :   Find the cell containing the given position.

        Parameters:
        :   **position** – Physical position [x, y]

        Returns:
        :   The cell containing the position

        Return type:
        :   [Cell](#mesa.discrete_space.__init__.Cell "mesa.discrete_space.__init__.Cell")

        Raises:
        :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If position is outside grid bounds and not a torus

    select\_random\_empty\_cell() → T[[source]](../_modules/mesa/discrete_space/grid.html#Grid.select_random_empty_cell)
    :   Select random empty cell.

    property cells\_with\_capacity: [CellCollection](#mesa.discrete_space.cell_collection.CellCollection "mesa.discrete_space.cell_collection.CellCollection")[T]
    :   Return all cells that have available capacity (i.e. are not full).

        A cell is considered *available* if `not cell.is_full`.

        This is meaningfully different from [`empties`](#id3 "mesa.discrete_space.__init__.DiscreteSpace.empties"):
        `empties` only includes cells with **zero** agents. If a cell has
        `capacity=5` and currently holds 3 agents it is **not** empty, but it
        **is** still available. `available_cells` is therefore the correct
        API for models where agents share cells up to a finite limit.

        For cells with `capacity=None` (unlimited), every cell is always
        available regardless of how many agents it holds.

        Returns:
        :   All cells where `len(agents) < capacity`
            (or all cells when capacity is None).

        Return type:
        :   [CellCollection](#mesa.discrete_space.__init__.CellCollection "mesa.discrete_space.__init__.CellCollection")[T]

        Example:

        ```
        # Place an agent in any non-full cell
        agent.move_to(grid.select_random_cell_with_capacity())

        # Count how many cells still have room
        len(list(grid.cells_with_capacity))
        ```

    select\_random\_cell\_with\_capacity() → [Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")[[source]](../_modules/mesa/discrete_space/grid.html#Grid.select_random_cell_with_capacity)
    :   Select a random cell that has remaining capacity.

        Raises:
        :   [**IndexError**](https://docs.python.org/3/library/exceptions.html#IndexError "(in Python v3.14)") – If every cell in the grid is at full capacity.

        Example:

        ```
        # Safe placement that respects capacity limits
        free_cell = grid.select_random_cell_with_capacity()
        agent.move_to(free_cell)
        ```

class Grid2DMovingAgent(*model: M*, *\*args*, *\*\*kwargs*)[[source]](../_modules/mesa/discrete_space/cell_agent.html#Grid2DMovingAgent)
:   Mixin for moving agents in 2D grids.

    Create a new agent.

    Parameters:
    :   - **model** ([*Model*](../mesa.html#mesa.model.Model "mesa.model.Model")) – The model instance in which the agent exists.
        - **args** – Passed on to super.
        - **kwargs** – Passed on to super.

    Notes

    to make proper use of python’s super, in each class remove the arguments and
    keyword arguments you need and pass on the rest to super

    move(*direction: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *distance: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*)[[source]](../_modules/mesa/discrete_space/cell_agent.html#Grid2DMovingAgent.move)
    :   Move the agent in a cardinal direction.

        Parameters:
        :   - **direction** – The cardinal direction to move in.
            - **distance** – The distance to move.

class HexGrid(*dimensions: ~collections.abc.Sequence[int], torus: bool = False, capacity: float | None = None, random: ~random.Random | None = None, cell\_klass: type[~mesa.discrete\_space.grid.T] = <class 'mesa.discrete\_space.cell.Cell'>*)[[source]](../_modules/mesa/discrete_space/grid.html#HexGrid)
:   A Grid with hexagonal tilling of the space.

    When torus=True, both width and height must be even.

    Raises:
    :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If torus=True and either width or height is odd.

    Initialize the hex grid.

    Parameters:
    :   - **dimensions** – the dimensions of the space
        - **torus** – whether the space wraps
        - **capacity** – capacity of the grid cell
        - **random** – a random number generator
        - **cell\_klass** – the base class to use for the cells

    find\_nearest\_cell(*position: ndarray*) → T[[source]](../_modules/mesa/discrete_space/grid.html#HexGrid.find_nearest_cell)
    :   Find the hex cell at the given position.

class Network(*G: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *capacity: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *random: [Random](https://docs.python.org/3/library/random.html#random.Random "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *cell\_klass: [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[[Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")] = <class 'mesa.discrete\_space.cell.Cell'>*, *layout: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.14)") | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/mesa/discrete_space/network.html#Network)
:   A networked discrete space.

    A Networked grid.

    Parameters:
    :   - **G** – a NetworkX Graph instance.
        - **capacity** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – the capacity of the cell
        - **random** (*Random*) – a random number generator
        - **cell\_klass** ([*type*](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")*[*[*Cell*](#mesa.discrete_space.__init__.Cell "mesa.discrete_space.__init__.Cell")*]*) – The base Cell class to use in the Network
        - **layout** – A dictionary mapping node IDs to physical positions (x, y),
          or a callable that generates them (e.g. nx.spring\_layout).
          It defaults to nx.circular\_layout
          This ensures all nodes possess physical (x, y) positions for visualization and
          spatial queries without introducing performance bottlenecks on large graphs

    find\_nearest\_cell(*position: ndarray*) → [Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")[[source]](../_modules/mesa/discrete_space/network.html#Network.find_nearest_cell)
    :   Find the network node nearest to the given position.

        Only works for spatial networks (networks with node positions).

        The KD-Tree index is rebuilt lazily. If cells were added or removed
        since the previous spatial query, this method rebuilds the KD-Tree
        before performing the nearest-neighbor lookup.

        Parameters:
        :   **position** – Physical position [x, y]

        Returns:
        :   The node closest to the position

        Return type:
        :   [Cell](#mesa.discrete_space.__init__.Cell "mesa.discrete_space.__init__.Cell")

        Raises:
        :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If network is not spatial

    add\_cell(*cell: [Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")*)[[source]](../_modules/mesa/discrete_space/network.html#Network.add_cell)
    :   Add a cell to the space.

    remove\_cell(*cell: [Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")*)[[source]](../_modules/mesa/discrete_space/network.html#Network.remove_cell)
    :   Remove a cell from the space.

    add\_connection(*cell1: [Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")*, *cell2: [Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")*)[[source]](../_modules/mesa/discrete_space/network.html#Network.add_connection)
    :   Add a connection between the two cells.

    remove\_connection(*cell1: [Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")*, *cell2: [Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")*)[[source]](../_modules/mesa/discrete_space/network.html#Network.remove_connection)
    :   Remove a connection between the two cells.

class OrthogonalMooreGrid(*dimensions: ~collections.abc.Sequence[int], torus: bool = False, capacity: float | None = None, random: ~random.Random | None = None, cell\_klass: type[~mesa.discrete\_space.grid.T] = <class 'mesa.discrete\_space.cell.Cell'>*)[[source]](../_modules/mesa/discrete_space/grid.html#OrthogonalMooreGrid)
:   Grid where cells are connected to their 8 neighbors.

    Example for two dimensions:
    directions = [

    > (-1, -1), (-1, 0), (-1, 1),
    > ( 0, -1), ( 0, 1),
    > ( 1, -1), ( 1, 0), ( 1, 1),

    ]

    Initialise the grid class.

    Parameters:
    :   - **dimensions** – the dimensions of the space
        - **torus** – whether the space wraps
        - **capacity** – capacity of the grid cell
        - **random** – a random number generator
        - **cell\_klass** – the base class to use for the cells

class OrthogonalVonNeumannGrid(*dimensions: ~collections.abc.Sequence[int], torus: bool = False, capacity: float | None = None, random: ~random.Random | None = None, cell\_klass: type[~mesa.discrete\_space.grid.T] = <class 'mesa.discrete\_space.cell.Cell'>*)[[source]](../_modules/mesa/discrete_space/grid.html#OrthogonalVonNeumannGrid)
:   Grid where cells are connected to their 4 neighbors.

    Example for two dimensions:
    directions = [

    > > (0, -1),
    >
    > (-1, 0), ( 1, 0),
    > :   (0, 1),

    ]

    Initialise the grid class.

    Parameters:
    :   - **dimensions** – the dimensions of the space
        - **torus** – whether the space wraps
        - **capacity** – capacity of the grid cell
        - **random** – a random number generator
        - **cell\_klass** – the base class to use for the cells

class VoronoiGrid(*centroids\_coordinates: ~collections.abc.Sequence[~collections.abc.Sequence[float]], capacity: int | ~collections.abc.Callable | None = None, random: ~random.Random | None = None, cell\_klass: type[~mesa.discrete\_space.cell.Cell] = <class 'mesa.discrete\_space.cell.Cell'>*)[[source]](../_modules/mesa/discrete_space/voronoi.html#VoronoiGrid)
:   Voronoi meshed GridSpace.

    A Voronoi Tessellation Grid.

    Given a set of points, this class creates a grid where a cell is centered in each point,
    its neighbors are given by Voronoi Tessellation cells neighbors
    and the capacity by the polygon area.

    Parameters:
    :   - **centroids\_coordinates** – coordinates of centroids to build the tessellation space
        - **capacity** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – capacity of the cells in the discrete space
        - **random** (*Random*) – random number generator
        - **cell\_klass** ([*type*](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")*[*[*Cell*](#mesa.discrete_space.__init__.Cell "mesa.discrete_space.__init__.Cell")*]*) – type of cell class
        - **capacity\_function** (*Callable*) – function to compute (int) capacity according to (float) area

    find\_nearest\_cell(*position: ndarray*) → [Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")[[source]](../_modules/mesa/discrete_space/voronoi.html#VoronoiGrid.find_nearest_cell)
    :   Find the Voronoi cell nearest to the given position.

        Parameters:
        :   **position** – Physical position [x, y]

        Returns:
        :   The Voronoi cell whose centroid is nearest to position

        Return type:
        :   [Cell](#mesa.discrete_space.__init__.Cell "mesa.discrete_space.__init__.Cell")

Cells are positions in space that can have properties and contain agents.

A cell represents a location that can:
- Have properties (like temperature or resources)
- Track and limit the agents it contains
- Connect to neighboring cells
- Provide neighborhood information

Cells form the foundation of the cell space system, enabling rich spatial
environments where both location properties and agent behaviors matter. They’re
useful for modeling things like varying terrain, infrastructure capacity, or
environmental conditions.

class Cell(*coordinate: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), ...]*, *position: ndarray | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *capacity: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *random: [Random](https://docs.python.org/3/library/random.html#random.Random "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/mesa/discrete_space/cell.html#Cell)
:   The cell represents a position in a discrete space.

    coordinate
    :   the logical position(or index) of the cell in the discrete space

        Type:
        :   Coordinate

    position
    :   the physical position of the cell in the discrete space

        Type:
        :   np.ndarray | None

    agents
    :   the agents occupying the cell

        Type:
        :   List[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")]

    capacity
    :   the maximum number of agents that can simultaneously occupy the cell

        Type:
        :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    random
    :   the random number generator

        Type:
        :   Random

    Initialise the cell.

    Parameters:
    :   - **coordinate** – coordinates of the cell
        - **position** – physical coordinates of the cell
        - **capacity** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – the capacity of the cell. If None, the capacity is infinite
        - **random** (*Random*) – the random number generator to use

    property position: ndarray
    :   Get the physical position of the cell.

        Returns:
        :   Physical position of the cell

        Return type:
        :   np.ndarray

    connect(*other: [Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")*, *key: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), ...] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/discrete_space/cell.html#Cell.connect)
    :   Connects this cell to another cell.

        Parameters:
        :   - **other** ([*Cell*](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")) – other cell to connect to
            - **key** (*Tuple**[*[*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *...**]*) – key for the connection. Should resemble a relative coordinate

    disconnect(*other: [Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/discrete_space/cell.html#Cell.disconnect)
    :   Disconnects this cell from another cell.

        Parameters:
        :   **other** ([*Cell*](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")) – other cell to remove from connections

    add\_agent(*agent: [CellAgent](#mesa.discrete_space.cell_agent.CellAgent "mesa.discrete_space.cell_agent.CellAgent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/discrete_space/cell.html#Cell.add_agent)
    :   Adds an agent to the cell.

        Parameters:
        :   **agent** ([*CellAgent*](#mesa.discrete_space.__init__.CellAgent "mesa.discrete_space.__init__.CellAgent")) – agent to add to this Cell

    remove\_agent(*agent: [CellAgent](#mesa.discrete_space.cell_agent.CellAgent "mesa.discrete_space.cell_agent.CellAgent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/discrete_space/cell.html#Cell.remove_agent)
    :   Removes an agent from the cell.

        Parameters:
        :   **agent** ([*CellAgent*](#mesa.discrete_space.__init__.CellAgent "mesa.discrete_space.__init__.CellAgent")) – agent to remove from this cell

    property is\_empty: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
    :   Returns a bool of the contents of a cell.

    property is\_full: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
    :   Returns a bool of the contents of a cell.

    property agents: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[CellAgent](#mesa.discrete_space.cell_agent.CellAgent "mesa.discrete_space.cell_agent.CellAgent")]
    :   Returns a list of the agents occupying the cell.

    property neighborhood: [CellCollection](#mesa.discrete_space.cell_collection.CellCollection "mesa.discrete_space.cell_collection.CellCollection")[[Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")]
    :   Returns the direct neighborhood of the cell.

        This is equivalent to cell.get\_neighborhood(radius=1)

    get\_neighborhood(*radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [CellCollection](#mesa.discrete_space.cell_collection.CellCollection "mesa.discrete_space.cell_collection.CellCollection")[[Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")][[source]](../_modules/mesa/discrete_space/cell.html#Cell.get_neighborhood)
    :   Returns a list of all neighboring cells for the given radius.

        For getting the direct neighborhood (i.e., radius=1) you can also use
        the neighborhood property.

        Parameters:
        :   - **radius** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – the radius of the neighborhood
            - **include\_center** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – include the center of the neighborhood

        Returns:
        :   a list of all neighboring cells

Agents that understand how to exist in and move through cell spaces.

Provides specialized agent classes that handle cell occupation, movement, and
proper registration:
- CellAgent: Mobile agents that can move between cells
- FixedAgent: Immobile agents permanently fixed to cells
- Grid2DMovingAgent: Agents with grid-specific movement capabilities

These classes ensure consistent agent-cell relationships and proper state management
as agents move through the space. They can be used directly or as examples for
creating custom cell-aware agents.

class HasCellProtocol(*\*args*, *\*\*kwargs*)[[source]](../_modules/mesa/discrete_space/cell_agent.html#HasCellProtocol)
:   Protocol for discrete space cell holders.

class HasCell[[source]](../_modules/mesa/discrete_space/cell_agent.html#HasCell)
:   Descriptor for cell movement behavior.

class BasicMovement[[source]](../_modules/mesa/discrete_space/cell_agent.html#BasicMovement)
:   Mixin for moving agents in discrete space.

    move\_to(*cell: [Cell](#mesa.discrete_space.__init__.Cell "mesa.discrete_space.__init__.Cell")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/discrete_space/cell_agent.html#BasicMovement.move_to)
    :   Move to a new cell.

    move\_relative(*direction: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), ...]*)[[source]](../_modules/mesa/discrete_space/cell_agent.html#BasicMovement.move_relative)
    :   Move to a cell relative to the current cell.

        Parameters:
        :   **direction** – The direction to move in.

class FixedCell[[source]](../_modules/mesa/discrete_space/cell_agent.html#FixedCell)
:   Mixin for agents that are fixed to a cell.

    Once assigned to a cell, the agent cannot be moved to a different cell.
    The assignment is atomic: if cell.add\_agent() raises (e.g. capacity
    reached), the agent’s \_mesa\_cell reference is left unchanged.

    property cell: [Cell](#mesa.discrete_space.__init__.Cell "mesa.discrete_space.__init__.Cell") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   The cell the agent is fixed to.

class CellAgent(*model: M*, *\*args*, *\*\*kwargs*)[[source]](../_modules/mesa/discrete_space/cell_agent.html#CellAgent)
:   Cell Agent is an extension of the Agent class and adds behavior for moving in discrete spaces.

    cell
    :   The cell the agent is currently in.

        Type:
        :   [Cell](#mesa.discrete_space.__init__.Cell "mesa.discrete_space.__init__.Cell")

    Create a new agent.

    Parameters:
    :   - **model** ([*Model*](../mesa.html#mesa.model.Model "mesa.model.Model")) – The model instance in which the agent exists.
        - **args** – Passed on to super.
        - **kwargs** – Passed on to super.

    Notes

    to make proper use of python’s super, in each class remove the arguments and
    keyword arguments you need and pass on the rest to super

    remove()[[source]](../_modules/mesa/discrete_space/cell_agent.html#CellAgent.remove)
    :   Remove the agent from the model.

class FixedAgent(*model: M*, *\*args*, *\*\*kwargs*)[[source]](../_modules/mesa/discrete_space/cell_agent.html#FixedAgent)
:   A patch in a 2D grid.

    Create a new agent.

    Parameters:
    :   - **model** ([*Model*](../mesa.html#mesa.model.Model "mesa.model.Model")) – The model instance in which the agent exists.
        - **args** – Passed on to super.
        - **kwargs** – Passed on to super.

    Notes

    to make proper use of python’s super, in each class remove the arguments and
    keyword arguments you need and pass on the rest to super

    remove()[[source]](../_modules/mesa/discrete_space/cell_agent.html#FixedAgent.remove)
    :   Remove the agent from the model.

class Grid2DMovingAgent(*model: M*, *\*args*, *\*\*kwargs*)[[source]](../_modules/mesa/discrete_space/cell_agent.html#Grid2DMovingAgent)
:   Mixin for moving agents in 2D grids.

    Create a new agent.

    Parameters:
    :   - **model** ([*Model*](../mesa.html#mesa.model.Model "mesa.model.Model")) – The model instance in which the agent exists.
        - **args** – Passed on to super.
        - **kwargs** – Passed on to super.

    Notes

    to make proper use of python’s super, in each class remove the arguments and
    keyword arguments you need and pass on the rest to super

    move(*direction: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *distance: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*)[[source]](../_modules/mesa/discrete_space/cell_agent.html#Grid2DMovingAgent.move)
    :   Move the agent in a cardinal direction.

        Parameters:
        :   - **direction** – The cardinal direction to move in.
            - **distance** – The distance to move.

Collection class for managing and querying groups of cells.

The CellCollection class provides a consistent interface for operating on multiple
cells, supporting:
- Filtering and selecting cells based on conditions
- Random cell and agent selection
- Access to contained agents
- Group operations

This is useful for implementing area effects, zones, or any operation that needs
to work with multiple cells as a unit. The collection handles efficient iteration
and agent access across cells. The class is used throughout the cell space
implementation to represent neighborhoods, selections, and other cell groupings.

class CellCollection(*cells: Mapping[T, [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[CellAgent](#mesa.discrete_space.__init__.CellAgent "mesa.discrete_space.__init__.CellAgent")]] | Iterable[T]*, *random: Random | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/mesa/discrete_space/cell_collection.html#CellCollection)
:   An immutable collection of cells.

    cells[[source]](../_modules/mesa/discrete_space/cell_collection.html#CellCollection.cells)
    :   The list of cells this collection represents

        Type:
        :   List[[Cell](#mesa.discrete_space.__init__.Cell "mesa.discrete_space.__init__.Cell")]

    agents
    :   List of agents occupying the cells in this collection

        Type:
        :   List[[CellAgent](#mesa.discrete_space.__init__.CellAgent "mesa.discrete_space.__init__.CellAgent")]

    random
    :   The random number generator

        Type:
        :   Random

    Notes

    A UserWarning is issued if random=None. You can resolve this warning by explicitly
    passing a random number generator. In most cases, this will be the seeded random number
    generator in the model. So, you would do random=self.random in a Model or Agent instance.

    Initialize a CellCollection.

    Parameters:
    :   - **cells** – cells to add to the collection
        - **random** – a seeded random number generator.

    select\_random\_cell(*default=<object object>*) → T | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/discrete_space/cell_collection.html#CellCollection.select_random_cell)
    :   Select a random cell from the collection.

        Parameters:
        :   **default** – Value to return if the collection is empty.
            If not provided, raises LookupError.

        Returns:
        :   A random cell, or the default value if provided and collection is empty.

        Return type:
        :   T

        Raises:
        :   [**LookupError**](https://docs.python.org/3/library/exceptions.html#LookupError "(in Python v3.14)") – If collection is empty and no default is provided.

    select\_random\_agent(*default=<object object>*) → [CellAgent](#mesa.discrete_space.__init__.CellAgent "mesa.discrete_space.__init__.CellAgent") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/discrete_space/cell_collection.html#CellCollection.select_random_agent)
    :   Select a random agent from the collection.

        Parameters:
        :   **default** – Value to return if the collection is empty.
            If not provided, raises LookupError.

        Returns:
        :   A random agent, or the default value if provided and collection is empty.

        Return type:
        :   [CellAgent](#mesa.discrete_space.__init__.CellAgent "mesa.discrete_space.__init__.CellAgent")

        Raises:
        :   [**LookupError**](https://docs.python.org/3/library/exceptions.html#LookupError "(in Python v3.14)") – If collection is empty and no default is provided.

    select(*filter\_func: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")[[T], [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *at\_most: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = inf*)[[source]](../_modules/mesa/discrete_space/cell_collection.html#CellCollection.select)
    :   Select cells based on filter function.

        Parameters:
        :   - **filter\_func** – filter function
            - **at\_most** – The maximum amount of cells to select. Defaults to infinity.
              - If an integer, at most the first number of matching cells is selected.
              - If a float between 0 and 1, at most that fraction of original number of cells

        Returns:
        :   CellCollection

Abstract Base class for building cell-based spatial environments.

DiscreteSpace provides the core functionality needed by all cell-based spaces:
- Cell creation and tracking
- Agent-cell relationship management
- Property Layer support
- Random selection capabilities
- Capacity management

This serves as the foundation for specific space implementations like grids
and networks, ensuring consistent behavior and shared functionality across
different space types. All concrete cell space implementations (grids, networks, etc.)
inherit from this class.

class DiscreteSpace(*capacity: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *cell\_klass: [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[T] = <class 'mesa.discrete\_space.cell.Cell'>*, *random: [Random](https://docs.python.org/3/library/random.html#random.Random "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/mesa/discrete_space/discrete_space.html#DiscreteSpace)
:   Base class for all discrete spaces.

    capacity
    :   The capacity of the cells in the discrete space

        Type:
        :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    all\_cells[[source]](../_modules/mesa/discrete_space/discrete_space.html#DiscreteSpace.all_cells)
    :   The cells composing the discrete space

        Type:
        :   [CellCollection](#mesa.discrete_space.__init__.CellCollection "mesa.discrete_space.__init__.CellCollection")

    random
    :   The random number generator

        Type:
        :   Random

    cell\_klass
    :   the type of cell class

        Type:
        :   Type

    empties
    :   collection of all cells that are empty

        Type:
        :   [CellCollection](#mesa.discrete_space.__init__.CellCollection "mesa.discrete_space.__init__.CellCollection")

    property\_layers
    :   property\_layer of the discrete space

        Type:
        :   [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), np.ndarray]

    Notes

    A UserWarning is issued if random=None. You can resolve this warning by explicitly
    passing a random number generator. In most cases, this will be the seeded random number
    generator in the model. So, you would do random=self.random in a Model or Agent instance.

    Instantiate a DiscreteSpace.

    Parameters:
    :   - **capacity** – capacity of cells
        - **cell\_klass** – base class for all cells
        - **random** – random number generator

    property agents: [AgentSet](agentset.html#mesa.agentset.AgentSet "mesa.agentset.AgentSet")
    :   Return an AgentSet with the agents in the space.

    abstractmethod find\_nearest\_cell(*position: ndarray*) → T[[source]](../_modules/mesa/discrete_space/discrete_space.html#DiscreteSpace.find_nearest_cell)
    :   Find the cell at or nearest to the given position.

    add\_cell(*cell: T*)[[source]](../_modules/mesa/discrete_space/discrete_space.html#DiscreteSpace.add_cell)
    :   Add a cell to the space.

        Parameters:
        :   **cell** – cell to add

        Discrete spaces rely on caching neighborhood relations for speedups. Adding or removing cells and
        connections at runtime is possible. However, only the caches of cells directly affected will be cleared. So
        if you rely on getting neighborhoods of cells with a radius higher than 1, these might not be cleared
        correctly if you are adding or removing cells and connections at runtime.

        Coordinate Collision: If a cell already exists at the specified
        coordinates (e.g., cell1), it will be overwritten silently by the
        new cell (cell2).

        Ensure the target coordinates are vacant before calling this method.

    remove\_cell(*cell: T*)[[source]](../_modules/mesa/discrete_space/discrete_space.html#DiscreteSpace.remove_cell)
    :   Remove a cell from the space.

        Discrete spaces rely on caching neighborhood relations for speedups. Adding or removing cells and
        connections at runtime is possible. However, only the caches of cells directly affected will be cleared. So
        if you rely on getting neighborhoods of cells with a radius higher than 1, these might not be cleared
        correctly if you are adding or removing cells and connections at runtime.

    add\_connection(*cell1: T*, *cell2: T*)[[source]](../_modules/mesa/discrete_space/discrete_space.html#DiscreteSpace.add_connection)
    :   Add a connection between the two cells.

        Discrete spaces rely on caching neighborhood relations for speedups. Adding or removing cells and
        connections at runtime is possible. However, only the caches of cells directly affected will be cleared. So
        if you rely on getting neighborhoods of cells with a radius higher than 1, these might not be cleared
        correctly if you are adding or removing cells and connections at runtime.

    remove\_connection(*cell1: T*, *cell2: T*)[[source]](../_modules/mesa/discrete_space/discrete_space.html#DiscreteSpace.remove_connection)
    :   Remove a connection between the two cells.

        Discrete spaces rely on caching neighborhood relations for speedups. Adding or removing cells and
        connections at runtime is possible. However, only the caches of cells directly affected will be cleared. So
        if you rely on getting neighborhoods of cells with a radius higher than 1, these might not be cleared
        correctly if you are adding or removing cells and connections at runtime.

    property all\_cells[[source]](../_modules/mesa/discrete_space/discrete_space.html#DiscreteSpace.all_cells)
    :   Return all cells in space.

    property empties: [CellCollection](#mesa.discrete_space.cell_collection.CellCollection "mesa.discrete_space.cell_collection.CellCollection")[T]
    :   Return all empty in spaces.

    select\_random\_empty\_cell() → T[[source]](../_modules/mesa/discrete_space/discrete_space.html#DiscreteSpace.select_random_empty_cell)
    :   Select random empty cell.

Grid-based cell space implementations with different connection patterns.

Provides several grid types for organizing cells:
- OrthogonalMooreGrid: 8 neighbors in 2D, (3^n)-1 in nD
- OrthogonalVonNeumannGrid: 4 neighbors in 2D, 2n in nD
- HexGrid: 6 neighbors in hexagonal pattern (2D only)

Each grid type supports optional wrapping (torus) and cell capacity limits.
Choose based on how movement and connectivity should work in your model -
Moore for unrestricted movement, Von Neumann for orthogonal-only movement,
or Hex for more uniform distances.

pickle\_gridcell(*obj*)[[source]](../_modules/mesa/discrete_space/grid.html#pickle_gridcell)
:   Helper function for pickling GridCell instances.

unpickle\_gridcell(*parent*, *fields*)[[source]](../_modules/mesa/discrete_space/grid.html#unpickle_gridcell)
:   Helper function for unpickling GridCell instances.

class Grid(*dimensions: ~collections.abc.Sequence[int], torus: bool = False, capacity: float | None = None, random: ~random.Random | None = None, cell\_klass: type[~mesa.discrete\_space.grid.T] = <class 'mesa.discrete\_space.cell.Cell'>*)[[source]](../_modules/mesa/discrete_space/grid.html#Grid)
:   Base class for all grid classes.

    dimensions
    :   the dimensions of the grid

        Type:
        :   Sequence[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]

    torus
    :   whether the grid is a torus

        Type:
        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    capacity
    :   the capacity of a grid cell

        Type:
        :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    random
    :   the random number generator

        Type:
        :   Random

    \_try\_random
    :   whether to get empty cell be repeatedly trying random cell

        Type:
        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    Notes

    width and height are accessible via property\_layers, higher dimensions can be retrieved via dimensions

    Initialise the grid class.

    Parameters:
    :   - **dimensions** – the dimensions of the space
        - **torus** – whether the space wraps
        - **capacity** – capacity of the grid cell
        - **random** – a random number generator
        - **cell\_klass** – the base class to use for the cells

    property width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
    :   Convenience access to the width of the grid.

    property height: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
    :   Convenience access to the height of the grid.

    create\_property\_layer(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *default\_value=0.0*, *dtype=<class 'float'>*, *read\_only: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → ndarray[[source]](../_modules/mesa/discrete_space/grid.html#Grid.create_property_layer)
    :   Create a property layer array and attach it to cells.

        Warning:
        Do not reassign grid.name directly — this will detach it from
        property\_layers and break cell-level access. Use in-place operations.

        > grid.sugar[:] = 0 # correct
        > grid.sugar = array # wrong — breaks cell access

    add\_property\_layer(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *array: ndarray*, *read\_only: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/discrete_space/grid.html#Grid.add_property_layer)
    :   Attach an existing array as a property layer. Shape must match self.dimensions.

        Warning:
        Do not reassign grid.name directly — this will detach it from
        property\_layers and break cell-level access. Use in-place operations.

        > grid.sugar[:] = 0 # correct
        > grid.sugar = array # wrong — breaks cell access

    remove\_property\_layer(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/discrete_space/grid.html#Grid.remove_property_layer)
    :   Remove a property\_layer.

        Parameters:
        :   **name** – property\_layer name.

    get\_neighborhood\_mask(*coordinate*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → ndarray[[source]](../_modules/mesa/discrete_space/grid.html#Grid.get_neighborhood_mask)
    :   Return a boolean mask shaped like `self.dimensions` for a neighborhood.

    find\_nearest\_cell(*position: ndarray*) → T[[source]](../_modules/mesa/discrete_space/grid.html#Grid.find_nearest_cell)
    :   Find the cell containing the given position.

        Parameters:
        :   **position** – Physical position [x, y]

        Returns:
        :   The cell containing the position

        Return type:
        :   [Cell](#mesa.discrete_space.__init__.Cell "mesa.discrete_space.__init__.Cell")

        Raises:
        :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If position is outside grid bounds and not a torus

    select\_random\_empty\_cell() → T[[source]](../_modules/mesa/discrete_space/grid.html#Grid.select_random_empty_cell)
    :   Select random empty cell.

    property cells\_with\_capacity: [CellCollection](#mesa.discrete_space.cell_collection.CellCollection "mesa.discrete_space.cell_collection.CellCollection")[T]
    :   Return all cells that have available capacity (i.e. are not full).

        A cell is considered *available* if `not cell.is_full`.

        This is meaningfully different from `empties`:
        `empties` only includes cells with **zero** agents. If a cell has
        `capacity=5` and currently holds 3 agents it is **not** empty, but it
        **is** still available. `available_cells` is therefore the correct
        API for models where agents share cells up to a finite limit.

        For cells with `capacity=None` (unlimited), every cell is always
        available regardless of how many agents it holds.

        Returns:
        :   All cells where `len(agents) < capacity`
            (or all cells when capacity is None).

        Return type:
        :   [CellCollection](#mesa.discrete_space.__init__.CellCollection "mesa.discrete_space.__init__.CellCollection")[T]

        Example:

        ```
        # Place an agent in any non-full cell
        agent.move_to(grid.select_random_cell_with_capacity())

        # Count how many cells still have room
        len(list(grid.cells_with_capacity))
        ```

    select\_random\_cell\_with\_capacity() → [Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")[[source]](../_modules/mesa/discrete_space/grid.html#Grid.select_random_cell_with_capacity)
    :   Select a random cell that has remaining capacity.

        Raises:
        :   [**IndexError**](https://docs.python.org/3/library/exceptions.html#IndexError "(in Python v3.14)") – If every cell in the grid is at full capacity.

        Example:

        ```
        # Safe placement that respects capacity limits
        free_cell = grid.select_random_cell_with_capacity()
        agent.move_to(free_cell)
        ```

class OrthogonalMooreGrid(*dimensions: ~collections.abc.Sequence[int], torus: bool = False, capacity: float | None = None, random: ~random.Random | None = None, cell\_klass: type[~mesa.discrete\_space.grid.T] = <class 'mesa.discrete\_space.cell.Cell'>*)[[source]](../_modules/mesa/discrete_space/grid.html#OrthogonalMooreGrid)
:   Grid where cells are connected to their 8 neighbors.

    Example for two dimensions:
    directions = [

    > (-1, -1), (-1, 0), (-1, 1),
    > ( 0, -1), ( 0, 1),
    > ( 1, -1), ( 1, 0), ( 1, 1),

    ]

    Initialise the grid class.

    Parameters:
    :   - **dimensions** – the dimensions of the space
        - **torus** – whether the space wraps
        - **capacity** – capacity of the grid cell
        - **random** – a random number generator
        - **cell\_klass** – the base class to use for the cells

class OrthogonalVonNeumannGrid(*dimensions: ~collections.abc.Sequence[int], torus: bool = False, capacity: float | None = None, random: ~random.Random | None = None, cell\_klass: type[~mesa.discrete\_space.grid.T] = <class 'mesa.discrete\_space.cell.Cell'>*)[[source]](../_modules/mesa/discrete_space/grid.html#OrthogonalVonNeumannGrid)
:   Grid where cells are connected to their 4 neighbors.

    Example for two dimensions:
    directions = [

    > > (0, -1),
    >
    > (-1, 0), ( 1, 0),
    > :   (0, 1),

    ]

    Initialise the grid class.

    Parameters:
    :   - **dimensions** – the dimensions of the space
        - **torus** – whether the space wraps
        - **capacity** – capacity of the grid cell
        - **random** – a random number generator
        - **cell\_klass** – the base class to use for the cells

class HexGrid(*dimensions: ~collections.abc.Sequence[int], torus: bool = False, capacity: float | None = None, random: ~random.Random | None = None, cell\_klass: type[~mesa.discrete\_space.grid.T] = <class 'mesa.discrete\_space.cell.Cell'>*)[[source]](../_modules/mesa/discrete_space/grid.html#HexGrid)
:   A Grid with hexagonal tilling of the space.

    When torus=True, both width and height must be even.

    Raises:
    :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If torus=True and either width or height is odd.

    Initialize the hex grid.

    Parameters:
    :   - **dimensions** – the dimensions of the space
        - **torus** – whether the space wraps
        - **capacity** – capacity of the grid cell
        - **random** – a random number generator
        - **cell\_klass** – the base class to use for the cells

    find\_nearest\_cell(*position: ndarray*) → T[[source]](../_modules/mesa/discrete_space/grid.html#HexGrid.find_nearest_cell)
    :   Find the hex cell at the given position.

Network-based cell space using arbitrary connection patterns.

Creates spaces where cells connect based on network relationships rather than
spatial proximity. Built on NetworkX graphs, this enables:
- Arbitrary connectivity patterns between cells
- Graph-based neighborhood definitions
- Logical rather than physical distances
- Dynamic connectivity changes
- Integration with NetworkX’s graph algorithms

Useful for modeling systems like social networks, transportation systems,
or any environment where connectivity matters more than physical location.

class Network(*G: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*, *capacity: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *random: [Random](https://docs.python.org/3/library/random.html#random.Random "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *cell\_klass: [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[[Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")] = <class 'mesa.discrete\_space.cell.Cell'>*, *layout: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.14)") | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/mesa/discrete_space/network.html#Network)
:   A networked discrete space.

    A Networked grid.

    Parameters:
    :   - **G** – a NetworkX Graph instance.
        - **capacity** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – the capacity of the cell
        - **random** (*Random*) – a random number generator
        - **cell\_klass** ([*type*](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")*[*[*Cell*](#mesa.discrete_space.__init__.Cell "mesa.discrete_space.__init__.Cell")*]*) – The base Cell class to use in the Network
        - **layout** – A dictionary mapping node IDs to physical positions (x, y),
          or a callable that generates them (e.g. nx.spring\_layout).
          It defaults to nx.circular\_layout
          This ensures all nodes possess physical (x, y) positions for visualization and
          spatial queries without introducing performance bottlenecks on large graphs

    find\_nearest\_cell(*position: ndarray*) → [Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")[[source]](../_modules/mesa/discrete_space/network.html#Network.find_nearest_cell)
    :   Find the network node nearest to the given position.

        Only works for spatial networks (networks with node positions).

        The KD-Tree index is rebuilt lazily. If cells were added or removed
        since the previous spatial query, this method rebuilds the KD-Tree
        before performing the nearest-neighbor lookup.

        Parameters:
        :   **position** – Physical position [x, y]

        Returns:
        :   The node closest to the position

        Return type:
        :   [Cell](#mesa.discrete_space.__init__.Cell "mesa.discrete_space.__init__.Cell")

        Raises:
        :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If network is not spatial

    add\_cell(*cell: [Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")*)[[source]](../_modules/mesa/discrete_space/network.html#Network.add_cell)
    :   Add a cell to the space.

    remove\_cell(*cell: [Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")*)[[source]](../_modules/mesa/discrete_space/network.html#Network.remove_cell)
    :   Remove a cell from the space.

    add\_connection(*cell1: [Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")*, *cell2: [Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")*)[[source]](../_modules/mesa/discrete_space/network.html#Network.add_connection)
    :   Add a connection between the two cells.

    remove\_connection(*cell1: [Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")*, *cell2: [Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")*)[[source]](../_modules/mesa/discrete_space/network.html#Network.remove_connection)
    :   Remove a connection between the two cells.

Cell spaces based on Voronoi tessellation around seed points.

Creates irregular spatial divisions by building cells around seed points,
where each cell contains the area closer to its seed than any other.
Features:
- Organic-looking spaces from point sets
- Automatic neighbor determination
- Area-based cell capacities
- Natural regional divisions

Useful for models requiring irregular but mathematically meaningful spatial
divisions, like territories, service areas, or natural regions.

class Delaunay(*center: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)") = (0, 0)*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 9999*)[[source]](../_modules/mesa/discrete_space/voronoi.html#Delaunay)
:   Class to compute a Delaunay triangulation in 2D.

    ref: [jmespadero/pyDelaunay2D](http://github.com/jmespadero/pyDelaunay2D)

    Init and create a new frame to contain the triangulation.

    Parameters:
    :   - **center** – Optional position for the center of the frame. Default (0,0)
        - **radius** – Optional distance from corners to the center.

    add\_point(*point: [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/discrete_space/voronoi.html#Delaunay.add_point)
    :   Add a point to the current DT, and refine it using Bowyer-Watson.

    export\_triangles() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[source]](../_modules/mesa/discrete_space/voronoi.html#Delaunay.export_triangles)
    :   Export the current list of Delaunay triangles.

    export\_voronoi\_regions()[[source]](../_modules/mesa/discrete_space/voronoi.html#Delaunay.export_voronoi_regions)
    :   Export coordinates and regions of Voronoi diagram as indexed data.

class VoronoiGrid(*centroids\_coordinates: ~collections.abc.Sequence[~collections.abc.Sequence[float]], capacity: int | ~collections.abc.Callable | None = None, random: ~random.Random | None = None, cell\_klass: type[~mesa.discrete\_space.cell.Cell] = <class 'mesa.discrete\_space.cell.Cell'>*)[[source]](../_modules/mesa/discrete_space/voronoi.html#VoronoiGrid)
:   Voronoi meshed GridSpace.

    A Voronoi Tessellation Grid.

    Given a set of points, this class creates a grid where a cell is centered in each point,
    its neighbors are given by Voronoi Tessellation cells neighbors
    and the capacity by the polygon area.

    Parameters:
    :   - **centroids\_coordinates** – coordinates of centroids to build the tessellation space
        - **capacity** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – capacity of the cells in the discrete space
        - **random** (*Random*) – random number generator
        - **cell\_klass** ([*type*](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")*[*[*Cell*](#mesa.discrete_space.__init__.Cell "mesa.discrete_space.__init__.Cell")*]*) – type of cell class
        - **capacity\_function** (*Callable*) – function to compute (int) capacity according to (float) area

    find\_nearest\_cell(*position: ndarray*) → [Cell](#mesa.discrete_space.cell.Cell "mesa.discrete_space.cell.Cell")[[source]](../_modules/mesa/discrete_space/voronoi.html#VoronoiGrid.find_nearest_cell)
    :   Find the Voronoi cell nearest to the given position.

        Parameters:
        :   **position** – Physical position [x, y]

        Returns:
        :   The Voronoi cell whose centroid is nearest to position

        Return type:
        :   [Cell](#mesa.discrete_space.__init__.Cell "mesa.discrete_space.__init__.Cell")

On this page

[Show Source](../_sources/apis/discrete_space.md.txt)

---

Original source: https://mesa.readthedocs.io/latest/apis/discrete_space.html
