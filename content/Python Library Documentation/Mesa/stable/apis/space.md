---
title: "Spaces"
source: "https://mesa.readthedocs.io/stable/apis/space.html"
imported_from: "Python library documentation"
library: "Mesa"
---

# Spaces

Mesa Space Module.

Objects used to add a spatial component to a model.

mesa.space now in maintenance-only mode. While these classes remain
fully supported, new development occurs in the discrete space module
(`mesa.discrete_space`) and the experimental ContinuousSpace module

## Classes

- PropertyLayer: A data layer that can be added to Grids to store cell properties
- SingleGrid: a Grid which strictly enforces one agent per cell.
- MultiGrid: a Grid where each cell can contain a set of agents.
- HexGrid: a Grid to handle hexagonal neighbors.
- ContinuousSpace: a two-dimensional space where each agent has an arbitrary position of float’s.
- NetworkGrid: a network where each node contains zero or more agents.

accept\_tuple\_argument(*wrapped\_function: F*) → F[[source]](../_modules/mesa/space.html#accept_tuple_argument)
:   Decorator to allow grid methods that take a list of (x, y) coord tuples to also handle a single position.

    Tuples are wrapped in a single-item list rather than forcing user to do it.

is\_integer(*x: [Real](https://docs.python.org/3/library/numbers.html#numbers.Real "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/mesa/space.html#is_integer)
:   Check if x is either a CPython integer or Numpy integer.

warn\_if\_agent\_has\_position\_already(*placement\_func*)[[source]](../_modules/mesa/space.html#warn_if_agent_has_position_already)
:   Decorator to give warning if agent has position already set.

is\_single\_argument\_function(*function*)[[source]](../_modules/mesa/space.html#is_single_argument_function)
:   Check if a function is a single argument function.

class PropertyLayer(*name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *height: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *default\_value*, *dtype=<class 'numpy.float64'>*)[[source]](../_modules/mesa/space.html#PropertyLayer)
:   A class representing a layer of properties in a two-dimensional grid.

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

    set\_cell(*position: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *value*)[[source]](../_modules/mesa/space.html#PropertyLayer.set_cell)
    :   Update a single cell’s value in-place.

    set\_cells(*value*, *condition=None*)[[source]](../_modules/mesa/space.html#PropertyLayer.set_cells)
    :   Perform a batch update either on the entire grid or conditionally, in-place.

        Parameters:
        :   - **value** – The value to be used for the update.
            - **condition** – (Optional) A callable (like a lambda function or a NumPy ufunc)
              that returns a boolean array when applied to the data.

    modify\_cell(*position: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *operation*, *value=None*)[[source]](../_modules/mesa/space.html#PropertyLayer.modify_cell)
    :   Modify a single cell using an operation, which can be a lambda function or a NumPy ufunc.

        If a NumPy ufunc is used, an additional value should be provided.

        Parameters:
        :   - **position** – The grid coordinates of the cell to modify.
            - **operation** – A function to apply. Can be a lambda function or a NumPy ufunc.
            - **value** – The value to be used if the operation is a NumPy ufunc. Ignored for lambda functions.

    modify\_cells(*operation*, *value=None*, *condition\_function=None*)[[source]](../_modules/mesa/space.html#PropertyLayer.modify_cells)
    :   Modify cells using an operation, which can be a lambda function or a NumPy ufunc.

        If a NumPy ufunc is used, an additional value should be provided.

        Parameters:
        :   - **operation** – A function to apply. Can be a lambda function or a NumPy ufunc.
            - **value** – The value to be used if the operation is a NumPy ufunc. Ignored for lambda functions.
            - **condition\_function** – (Optional) A callable that returns a boolean array when applied to the data.

    select\_cells(*condition*, *return\_list=True*)[[source]](../_modules/mesa/space.html#PropertyLayer.select_cells)
    :   Find cells that meet a specified condition using NumPy’s boolean indexing, in-place.

        Parameters:
        :   - **condition** – A callable that returns a boolean array when applied to the data.
            - **return\_list** – (Optional) If True, return a list of (x, y) tuples. Otherwise, return a boolean array.

        Returns:
        :   A list of (x, y) tuples or a boolean array.

    aggregate\_property(*operation*)[[source]](../_modules/mesa/space.html#PropertyLayer.aggregate_property)
    :   Perform an aggregate operation (e.g., sum, mean) on a property across all cells.

        Parameters:
        :   **operation** – A function to apply. Can be a lambda function or a NumPy ufunc.

class SingleGrid(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *height: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *torus: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *property\_layers: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [PropertyLayer](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[PropertyLayer](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer")] = None*)[[source]](../_modules/mesa/space.html#SingleGrid)
:   Rectangular grid where each cell contains exactly at most one agent.

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
        - **property\_layers** (*None* *|* [*PropertyLayer*](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer") *|* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*[*[*PropertyLayer*](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer")*]**,* *optional*) – A single PropertyLayer instance,
          a list of PropertyLayer instances, or None to initialize without any property layers.

    Raises:
    :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If a property layer’s dimensions do not match the grid dimensions.

    remove\_agent(*agent: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/space.html#SingleGrid.remove_agent)
    :   Remove the agent from the grid and set its pos attribute to None.

    add\_property\_layer(*property\_layer: [PropertyLayer](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer")*)
    :   Adds a new property layer to the grid.

        Parameters:
        :   **property\_layer** ([*PropertyLayer*](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer")) – The PropertyLayer instance to be added to the grid.

        Raises:
        :   - [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If a property layer with the same name already exists in the grid.
            - [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If the dimensions of the property layer do not match the grid’s dimensions.

    property agents: [AgentSet](agentset.html#mesa.agentset.AgentSet "mesa.agentset.AgentSet")
    :   Return an AgentSet with the agents in the space.

    coord\_iter() → [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]]
    :   An iterator that returns positions as well as cell contents.

    static default\_val() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Default value for new cell elements.

    property empty\_mask: ndarray
    :   Returns a boolean mask indicating empty cells on the grid.

    exists\_empty\_cells() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
    :   Return True if any cells empty else False.

    get\_neighborhood(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *moore: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]
    :   Return a list of cells that are in the neighborhood of a certain point.

        Parameters:
        :   - **pos** – Coordinate tuple for the neighborhood to get.
            - **moore** – If True, return Moore neighborhood
              (including diagonals)
              If False, return Von Neumann neighborhood
              (exclude diagonals)
            - **include\_center** – If True, return the (x, y) cell as well.
              Otherwise, return surrounding cells only.
            - **radius** – radius, in cells, of neighborhood to get.

        Returns:
        :   A list of coordinate tuples representing the neighborhood;
            With radius 1, at most 9 if Moore, 5 if Von Neumann (8 and 4
            if not including the center).

    get\_neighborhood\_mask(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *moore: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → ndarray
    :   Generate a boolean mask representing the neighborhood.

        Helper method for select\_cells\_multi\_properties() and move\_agent\_to\_random\_cell()

        Parameters:
        :   - **pos** (*Coordinate*) – Center of the neighborhood.
            - **moore** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – True for Moore neighborhood, False for Von Neumann.
            - **include\_center** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Include the central cell in the neighborhood.
            - **radius** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The radius of the neighborhood.

        Returns:
        :   A boolean mask representing the neighborhood.

        Return type:
        :   np.ndarray

    get\_neighbors(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *moore: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")]
    :   Return a list of neighbors to a certain point.

        Parameters:
        :   - **pos** – Coordinate tuple for the neighborhood to get.
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
        :   A list of non-None objects in the given neighborhood;
            at most 9 if Moore, 5 if Von-Neumann
            (8 and 4 if not including the center).

    is\_cell\_empty(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
    :   Returns a bool of the contents of a cell.

    iter\_neighborhood(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *moore: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]
    :   Return an iterator over cell coordinates that are in the neighborhood of a certain point.

        Parameters:
        :   - **pos** – Coordinate tuple for the neighborhood to get.
            - **moore** –

              If True, return Moore neighborhood
              :   (including diagonals)

              If False, return Von Neumann neighborhood
              :   (exclude diagonals)
            - **include\_center** – If True, return the (x, y) cell as well.
              Otherwise, return surrounding cells only.
            - **radius** – radius, in cells, of neighborhood to get.

        Returns:
        :   An iterator of coordinate tuples representing the neighborhood. For
            example with radius 1, it will return list with number of elements
            equals at most 9 (8) if Moore, 5 (4) if Von Neumann (if not
            including the center).

    iter\_neighbors(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *moore: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")]
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

    move\_agent(*agent: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*, *pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Move an agent from its current position to a new position.

        Parameters:
        :   - **agent** – Agent object to move. Assumed to have its current location
              stored in a ‘pos’ tuple.
            - **pos** – Tuple of new position to move the agent to.

    move\_agent\_to\_one\_of(*agent: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*, *pos: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]*, *selection: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'random'*, *handle\_empty: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Move an agent to one of the given positions.

        Parameters:
        :   - **agent** – Agent object to move. Assumed to have its current location stored in a ‘pos’ tuple.
            - **pos** – List of possible positions.
            - **selection** – String, either “random” (default) or “closest”. If “closest” is selected and multiple
              cells are the same distance, one is chosen randomly.
            - **handle\_empty** – String, either “warning”, “error” or None (default). If “warning” or “error” is selected
              and no positions are given (an empty list), a warning or error is raised respectively.

    move\_to\_empty(*agent: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Moves agent to a random empty cell, vacating agent’s old cell.

    out\_of\_bounds(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
    :   Determines whether position is off the grid, returns the out of bounds coordinate.

    remove\_property\_layer(*property\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)
    :   Removes a property layer from the grid by its name.

        Parameters:
        :   **property\_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The name of the property layer to be removed.

        Raises:
        :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If a property layer with the given name does not exist in the grid.

    select\_cells(*conditions: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *extreme\_values: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *masks: ndarray | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[ndarray] = None*, *only\_empty: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *return\_list: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]] | ndarray
    :   Select cells based on property conditions, extreme values, and/or masks, with an option to only select empty cells.

        Parameters:
        :   - **conditions** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – A dictionary where keys are property names and values are callables that return a boolean when applied.
            - **extreme\_values** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – A dictionary where keys are property names and values are either ‘highest’ or ‘lowest’.
            - **masks** (*np.ndarray* *|* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*[**np.ndarray**]**,* *optional*) – A mask or list of masks to restrict the selection.
            - **only\_empty** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) – If True, only select cells that are empty. Default is False.
            - **return\_list** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) – If True, return a list of coordinates, otherwise return a mask.

        Returns:
        :   Coordinates where conditions are satisfied or the combined mask.

        Return type:
        :   Union[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[Coordinate], np.ndarray]

    swap\_pos(*agent\_a: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*, *agent\_b: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Swap agents positions.

    torus\_adj(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]
    :   Convert coordinate, handling torus looping.

class MultiGrid(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *height: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *torus: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *property\_layers: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [PropertyLayer](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[PropertyLayer](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer")] = None*)[[source]](../_modules/mesa/space.html#MultiGrid)
:   Rectangular grid where each cell can contain more than one agent.

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
        - **property\_layers** (*None* *|* [*PropertyLayer*](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer") *|* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*[*[*PropertyLayer*](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer")*]**,* *optional*) – A single PropertyLayer instance,
          a list of PropertyLayer instances, or None to initialize without any property layers.

    Raises:
    :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If a property layer’s dimensions do not match the grid dimensions.

    static default\_val() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")][[source]](../_modules/mesa/space.html#MultiGrid.default_val)
    :   Default value for new cell elements.

    remove\_agent(*agent: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/space.html#MultiGrid.remove_agent)
    :   Remove the agent from the given location and set its pos attribute to None.

    iter\_neighbors(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *moore: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")][[source]](../_modules/mesa/space.html#MultiGrid.iter_neighbors)
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

    add\_property\_layer(*property\_layer: [PropertyLayer](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer")*)
    :   Adds a new property layer to the grid.

        Parameters:
        :   **property\_layer** ([*PropertyLayer*](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer")) – The PropertyLayer instance to be added to the grid.

        Raises:
        :   - [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If a property layer with the same name already exists in the grid.
            - [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If the dimensions of the property layer do not match the grid’s dimensions.

    property agents: [AgentSet](agentset.html#mesa.agentset.AgentSet "mesa.agentset.AgentSet")
    :   Return an AgentSet with the agents in the space.

    coord\_iter() → [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]]
    :   An iterator that returns positions as well as cell contents.

    property empty\_mask: ndarray
    :   Returns a boolean mask indicating empty cells on the grid.

    exists\_empty\_cells() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
    :   Return True if any cells empty else False.

    get\_neighborhood(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *moore: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]
    :   Return a list of cells that are in the neighborhood of a certain point.

        Parameters:
        :   - **pos** – Coordinate tuple for the neighborhood to get.
            - **moore** – If True, return Moore neighborhood
              (including diagonals)
              If False, return Von Neumann neighborhood
              (exclude diagonals)
            - **include\_center** – If True, return the (x, y) cell as well.
              Otherwise, return surrounding cells only.
            - **radius** – radius, in cells, of neighborhood to get.

        Returns:
        :   A list of coordinate tuples representing the neighborhood;
            With radius 1, at most 9 if Moore, 5 if Von Neumann (8 and 4
            if not including the center).

    get\_neighborhood\_mask(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *moore: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → ndarray
    :   Generate a boolean mask representing the neighborhood.

        Helper method for select\_cells\_multi\_properties() and move\_agent\_to\_random\_cell()

        Parameters:
        :   - **pos** (*Coordinate*) – Center of the neighborhood.
            - **moore** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – True for Moore neighborhood, False for Von Neumann.
            - **include\_center** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Include the central cell in the neighborhood.
            - **radius** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The radius of the neighborhood.

        Returns:
        :   A boolean mask representing the neighborhood.

        Return type:
        :   np.ndarray

    get\_neighbors(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *moore: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")]
    :   Return a list of neighbors to a certain point.

        Parameters:
        :   - **pos** – Coordinate tuple for the neighborhood to get.
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
        :   A list of non-None objects in the given neighborhood;
            at most 9 if Moore, 5 if Von-Neumann
            (8 and 4 if not including the center).

    is\_cell\_empty(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
    :   Returns a bool of the contents of a cell.

    iter\_neighborhood(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *moore: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]
    :   Return an iterator over cell coordinates that are in the neighborhood of a certain point.

        Parameters:
        :   - **pos** – Coordinate tuple for the neighborhood to get.
            - **moore** –

              If True, return Moore neighborhood
              :   (including diagonals)

              If False, return Von Neumann neighborhood
              :   (exclude diagonals)
            - **include\_center** – If True, return the (x, y) cell as well.
              Otherwise, return surrounding cells only.
            - **radius** – radius, in cells, of neighborhood to get.

        Returns:
        :   An iterator of coordinate tuples representing the neighborhood. For
            example with radius 1, it will return list with number of elements
            equals at most 9 (8) if Moore, 5 (4) if Von Neumann (if not
            including the center).

    move\_agent(*agent: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*, *pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Move an agent from its current position to a new position.

        Parameters:
        :   - **agent** – Agent object to move. Assumed to have its current location
              stored in a ‘pos’ tuple.
            - **pos** – Tuple of new position to move the agent to.

    move\_agent\_to\_one\_of(*agent: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*, *pos: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]*, *selection: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'random'*, *handle\_empty: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Move an agent to one of the given positions.

        Parameters:
        :   - **agent** – Agent object to move. Assumed to have its current location stored in a ‘pos’ tuple.
            - **pos** – List of possible positions.
            - **selection** – String, either “random” (default) or “closest”. If “closest” is selected and multiple
              cells are the same distance, one is chosen randomly.
            - **handle\_empty** – String, either “warning”, “error” or None (default). If “warning” or “error” is selected
              and no positions are given (an empty list), a warning or error is raised respectively.

    move\_to\_empty(*agent: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Moves agent to a random empty cell, vacating agent’s old cell.

    out\_of\_bounds(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
    :   Determines whether position is off the grid, returns the out of bounds coordinate.

    remove\_property\_layer(*property\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)
    :   Removes a property layer from the grid by its name.

        Parameters:
        :   **property\_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The name of the property layer to be removed.

        Raises:
        :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If a property layer with the given name does not exist in the grid.

    select\_cells(*conditions: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *extreme\_values: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *masks: ndarray | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[ndarray] = None*, *only\_empty: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *return\_list: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]] | ndarray
    :   Select cells based on property conditions, extreme values, and/or masks, with an option to only select empty cells.

        Parameters:
        :   - **conditions** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – A dictionary where keys are property names and values are callables that return a boolean when applied.
            - **extreme\_values** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – A dictionary where keys are property names and values are either ‘highest’ or ‘lowest’.
            - **masks** (*np.ndarray* *|* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*[**np.ndarray**]**,* *optional*) – A mask or list of masks to restrict the selection.
            - **only\_empty** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) – If True, only select cells that are empty. Default is False.
            - **return\_list** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) – If True, return a list of coordinates, otherwise return a mask.

        Returns:
        :   Coordinates where conditions are satisfied or the combined mask.

        Return type:
        :   Union[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[Coordinate], np.ndarray]

    swap\_pos(*agent\_a: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*, *agent\_b: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Swap agents positions.

    torus\_adj(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]
    :   Convert coordinate, handling torus looping.

class HexSingleGrid(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *height: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *torus: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *property\_layers: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [PropertyLayer](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[PropertyLayer](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer")] = None*)[[source]](../_modules/mesa/space.html#HexSingleGrid)
:   Hexagonal SingleGrid: a SingleGrid where neighbors are computed according to a hexagonal tiling of the grid.

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
        - **property\_layers** (*None* *|* [*PropertyLayer*](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer") *|* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*[*[*PropertyLayer*](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer")*]**,* *optional*) – A single PropertyLayer instance,
          a list of PropertyLayer instances, or None to initialize without any property layers.

    Raises:
    :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If a property layer’s dimensions do not match the grid dimensions.

    add\_property\_layer(*property\_layer: [PropertyLayer](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer")*)
    :   Adds a new property layer to the grid.

        Parameters:
        :   **property\_layer** ([*PropertyLayer*](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer")) – The PropertyLayer instance to be added to the grid.

        Raises:
        :   - [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If a property layer with the same name already exists in the grid.
            - [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If the dimensions of the property layer do not match the grid’s dimensions.

    property agents: [AgentSet](agentset.html#mesa.agentset.AgentSet "mesa.agentset.AgentSet")
    :   Return an AgentSet with the agents in the space.

    coord\_iter() → [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]]
    :   An iterator that returns positions as well as cell contents.

    static default\_val() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Default value for new cell elements.

    property empty\_mask: ndarray
    :   Returns a boolean mask indicating empty cells on the grid.

    exists\_empty\_cells() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
    :   Return True if any cells empty else False.

    get\_neighborhood(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]
    :   Return a list of coordinates that are in the neighborhood of a certain point.

        To calculate the neighborhood for a HexGrid the parity of the x coordinate of the point is
        important, the neighborhood can be sketched as:

        > Always: (0,-), (0,+)
        > When x is even: (-,+), (-,0), (+,+), (+,0)
        > When x is odd: (-,0), (-,-), (+,0), (+,-)

        Parameters:
        :   - **pos** – Coordinate tuple for the neighborhood to get.
            - **include\_center** – If True, return the (x, y) cell as well.
              Otherwise, return surrounding cells only.
            - **radius** – radius, in cells, of neighborhood to get.

        Returns:
        :   A list of coordinate tuples representing the neighborhood. For
            example with radius 1, it will return list with number of elements
            equals at most 9 (8) if Moore, 5 (4) if Von Neumann (if not
            including the center).

    get\_neighborhood\_mask(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *moore: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → ndarray
    :   Generate a boolean mask representing the neighborhood.

        Helper method for select\_cells\_multi\_properties() and move\_agent\_to\_random\_cell()

        Parameters:
        :   - **pos** (*Coordinate*) – Center of the neighborhood.
            - **moore** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – True for Moore neighborhood, False for Von Neumann.
            - **include\_center** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Include the central cell in the neighborhood.
            - **radius** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The radius of the neighborhood.

        Returns:
        :   A boolean mask representing the neighborhood.

        Return type:
        :   np.ndarray

    get\_neighbors(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")]
    :   Return a list of neighbors to a certain point.

        Parameters:
        :   - **pos** – Coordinate tuple for the neighborhood to get.
            - **include\_center** – If True, return the (x, y) cell as well.
              Otherwise,
              return surrounding cells only.
            - **radius** – radius, in cells, of neighborhood to get.

        Returns:
        :   A list of non-None objects in the given neighborhood

    is\_cell\_empty(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
    :   Returns a bool of the contents of a cell.

    iter\_neighborhood(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]
    :   Return an iterator over cell coordinates that are in the neighborhood of a certain point.

        Parameters:
        :   - **pos** – Coordinate tuple for the neighborhood to get.
            - **include\_center** – If True, return the (x, y) cell as well.
              Otherwise, return surrounding cells only.
            - **radius** – radius, in cells, of neighborhood to get.

        Returns:
        :   An iterator of coordinate tuples representing the neighborhood.

    iter\_neighbors(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")]
    :   Return an iterator over neighbors to a certain point.

        Parameters:
        :   - **pos** – Coordinates for the neighborhood to get.
            - **include\_center** – If True, return the (x, y) cell as well.
              Otherwise,
              return surrounding cells only.
            - **radius** – radius, in cells, of neighborhood to get.

        Returns:
        :   An iterator of non-None objects in the given neighborhood

    move\_agent(*agent: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*, *pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Move an agent from its current position to a new position.

        Parameters:
        :   - **agent** – Agent object to move. Assumed to have its current location
              stored in a ‘pos’ tuple.
            - **pos** – Tuple of new position to move the agent to.

    move\_agent\_to\_one\_of(*agent: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*, *pos: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]*, *selection: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'random'*, *handle\_empty: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Move an agent to one of the given positions.

        Parameters:
        :   - **agent** – Agent object to move. Assumed to have its current location stored in a ‘pos’ tuple.
            - **pos** – List of possible positions.
            - **selection** – String, either “random” (default) or “closest”. If “closest” is selected and multiple
              cells are the same distance, one is chosen randomly.
            - **handle\_empty** – String, either “warning”, “error” or None (default). If “warning” or “error” is selected
              and no positions are given (an empty list), a warning or error is raised respectively.

    move\_to\_empty(*agent: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Moves agent to a random empty cell, vacating agent’s old cell.

    out\_of\_bounds(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
    :   Determines whether position is off the grid, returns the out of bounds coordinate.

    remove\_agent(*agent: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Remove the agent from the grid and set its pos attribute to None.

    remove\_property\_layer(*property\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)
    :   Removes a property layer from the grid by its name.

        Parameters:
        :   **property\_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The name of the property layer to be removed.

        Raises:
        :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If a property layer with the given name does not exist in the grid.

    select\_cells(*conditions: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *extreme\_values: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *masks: ndarray | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[ndarray] = None*, *only\_empty: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *return\_list: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]] | ndarray
    :   Select cells based on property conditions, extreme values, and/or masks, with an option to only select empty cells.

        Parameters:
        :   - **conditions** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – A dictionary where keys are property names and values are callables that return a boolean when applied.
            - **extreme\_values** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – A dictionary where keys are property names and values are either ‘highest’ or ‘lowest’.
            - **masks** (*np.ndarray* *|* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*[**np.ndarray**]**,* *optional*) – A mask or list of masks to restrict the selection.
            - **only\_empty** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) – If True, only select cells that are empty. Default is False.
            - **return\_list** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) – If True, return a list of coordinates, otherwise return a mask.

        Returns:
        :   Coordinates where conditions are satisfied or the combined mask.

        Return type:
        :   Union[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[Coordinate], np.ndarray]

    swap\_pos(*agent\_a: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*, *agent\_b: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Swap agents positions.

    torus\_adj(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]
    :   Convert coordinate, handling torus looping.

class HexMultiGrid(*width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *height: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *torus: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *property\_layers: [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") | [PropertyLayer](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer") | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[PropertyLayer](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer")] = None*)[[source]](../_modules/mesa/space.html#HexMultiGrid)
:   Hexagonal MultiGrid: a MultiGrid where neighbors are computed according to a hexagonal tiling of the grid.

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
        - **property\_layers** (*None* *|* [*PropertyLayer*](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer") *|* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*[*[*PropertyLayer*](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer")*]**,* *optional*) – A single PropertyLayer instance,
          a list of PropertyLayer instances, or None to initialize without any property layers.

    Raises:
    :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If a property layer’s dimensions do not match the grid dimensions.

    add\_property\_layer(*property\_layer: [PropertyLayer](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer")*)
    :   Adds a new property layer to the grid.

        Parameters:
        :   **property\_layer** ([*PropertyLayer*](../mesa.html#mesa.space.PropertyLayer "mesa.space.PropertyLayer")) – The PropertyLayer instance to be added to the grid.

        Raises:
        :   - [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If a property layer with the same name already exists in the grid.
            - [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If the dimensions of the property layer do not match the grid’s dimensions.

    property agents: [AgentSet](agentset.html#mesa.agentset.AgentSet "mesa.agentset.AgentSet")
    :   Return an AgentSet with the agents in the space.

    coord\_iter() → [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)"), [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]]
    :   An iterator that returns positions as well as cell contents.

    static default\_val() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")]
    :   Default value for new cell elements.

    property empty\_mask: ndarray
    :   Returns a boolean mask indicating empty cells on the grid.

    exists\_empty\_cells() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
    :   Return True if any cells empty else False.

    get\_neighborhood(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]
    :   Return a list of coordinates that are in the neighborhood of a certain point.

        To calculate the neighborhood for a HexGrid the parity of the x coordinate of the point is
        important, the neighborhood can be sketched as:

        > Always: (0,-), (0,+)
        > When x is even: (-,+), (-,0), (+,+), (+,0)
        > When x is odd: (-,0), (-,-), (+,0), (+,-)

        Parameters:
        :   - **pos** – Coordinate tuple for the neighborhood to get.
            - **include\_center** – If True, return the (x, y) cell as well.
              Otherwise, return surrounding cells only.
            - **radius** – radius, in cells, of neighborhood to get.

        Returns:
        :   A list of coordinate tuples representing the neighborhood. For
            example with radius 1, it will return list with number of elements
            equals at most 9 (8) if Moore, 5 (4) if Von Neumann (if not
            including the center).

    get\_neighborhood\_mask(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *moore: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → ndarray
    :   Generate a boolean mask representing the neighborhood.

        Helper method for select\_cells\_multi\_properties() and move\_agent\_to\_random\_cell()

        Parameters:
        :   - **pos** (*Coordinate*) – Center of the neighborhood.
            - **moore** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – True for Moore neighborhood, False for Von Neumann.
            - **include\_center** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")) – Include the central cell in the neighborhood.
            - **radius** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The radius of the neighborhood.

        Returns:
        :   A boolean mask representing the neighborhood.

        Return type:
        :   np.ndarray

    get\_neighbors(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")]
    :   Return a list of neighbors to a certain point.

        Parameters:
        :   - **pos** – Coordinate tuple for the neighborhood to get.
            - **include\_center** – If True, return the (x, y) cell as well.
              Otherwise,
              return surrounding cells only.
            - **radius** – radius, in cells, of neighborhood to get.

        Returns:
        :   A list of non-None objects in the given neighborhood

    is\_cell\_empty(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
    :   Returns a bool of the contents of a cell.

    iter\_neighborhood(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]
    :   Return an iterator over cell coordinates that are in the neighborhood of a certain point.

        Parameters:
        :   - **pos** – Coordinate tuple for the neighborhood to get.
            - **include\_center** – If True, return the (x, y) cell as well.
              Otherwise, return surrounding cells only.
            - **radius** – radius, in cells, of neighborhood to get.

        Returns:
        :   An iterator of coordinate tuples representing the neighborhood.

    iter\_neighbors(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")]
    :   Return an iterator over neighbors to a certain point.

        Parameters:
        :   - **pos** – Coordinates for the neighborhood to get.
            - **include\_center** – If True, return the (x, y) cell as well.
              Otherwise,
              return surrounding cells only.
            - **radius** – radius, in cells, of neighborhood to get.

        Returns:
        :   An iterator of non-None objects in the given neighborhood

    move\_agent(*agent: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*, *pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Move an agent from its current position to a new position.

        Parameters:
        :   - **agent** – Agent object to move. Assumed to have its current location
              stored in a ‘pos’ tuple.
            - **pos** – Tuple of new position to move the agent to.

    move\_agent\_to\_one\_of(*agent: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*, *pos: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]]*, *selection: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'random'*, *handle\_empty: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Move an agent to one of the given positions.

        Parameters:
        :   - **agent** – Agent object to move. Assumed to have its current location stored in a ‘pos’ tuple.
            - **pos** – List of possible positions.
            - **selection** – String, either “random” (default) or “closest”. If “closest” is selected and multiple
              cells are the same distance, one is chosen randomly.
            - **handle\_empty** – String, either “warning”, “error” or None (default). If “warning” or “error” is selected
              and no positions are given (an empty list), a warning or error is raised respectively.

    move\_to\_empty(*agent: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Moves agent to a random empty cell, vacating agent’s old cell.

    out\_of\_bounds(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
    :   Determines whether position is off the grid, returns the out of bounds coordinate.

    remove\_agent(*agent: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Remove the agent from the given location and set its pos attribute to None.

    remove\_property\_layer(*property\_name: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*)
    :   Removes a property layer from the grid by its name.

        Parameters:
        :   **property\_name** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The name of the property layer to be removed.

        Raises:
        :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If a property layer with the given name does not exist in the grid.

    select\_cells(*conditions: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *extreme\_values: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *masks: ndarray | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[ndarray] = None*, *only\_empty: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *return\_list: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]] | ndarray
    :   Select cells based on property conditions, extreme values, and/or masks, with an option to only select empty cells.

        Parameters:
        :   - **conditions** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – A dictionary where keys are property names and values are callables that return a boolean when applied.
            - **extreme\_values** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – A dictionary where keys are property names and values are either ‘highest’ or ‘lowest’.
            - **masks** (*np.ndarray* *|* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*[**np.ndarray**]**,* *optional*) – A mask or list of masks to restrict the selection.
            - **only\_empty** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) – If True, only select cells that are empty. Default is False.
            - **return\_list** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) – If True, return a list of coordinates, otherwise return a mask.

        Returns:
        :   Coordinates where conditions are satisfied or the combined mask.

        Return type:
        :   Union[[list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[Coordinate], np.ndarray]

    swap\_pos(*agent\_a: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*, *agent\_b: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Swap agents positions.

    torus\_adj(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]
    :   Convert coordinate, handling torus looping.

class ContinuousSpace(*x\_max: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *y\_max: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *torus: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*, *x\_min: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 0*, *y\_min: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 0*)[[source]](../_modules/mesa/space.html#ContinuousSpace)
:   Continuous space where each agent can have an arbitrary position.

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

    property agents: [AgentSet](agentset.html#mesa.agentset.AgentSet "mesa.agentset.AgentSet")
    :   Return an AgentSet with the agents in the space.

    move\_agent(*agent: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*, *pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")] | ndarray[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), ...], dtype[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/space.html#ContinuousSpace.move_agent)
    :   Move an agent from its current position to a new position.

        Parameters:
        :   - **agent** – The agent object to move.
            - **pos** – Coordinate tuple to move the agent to.

    remove\_agent(*agent: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/space.html#ContinuousSpace.remove_agent)
    :   Remove an agent from the space.

        Parameters:
        :   **agent** – The agent object to remove

    get\_neighbors(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")] | ndarray[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), ...], dtype[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]]*, *radius: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")][[source]](../_modules/mesa/space.html#ContinuousSpace.get_neighbors)
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

    get\_heading(*pos\_1: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")] | ndarray[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), ...], dtype[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]]*, *pos\_2: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")] | ndarray[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), ...], dtype[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]]*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")] | ndarray[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), ...], dtype[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]][[source]](../_modules/mesa/space.html#ContinuousSpace.get_heading)
    :   Get the heading vector between two points, accounting for toroidal space.

        It is possible to calculate the heading angle by applying the atan2 function to the
        result.

        Parameters:
        :   - **pos\_1** – Coordinate tuples for both points.
            - **pos\_2** – Coordinate tuples for both points.

    get\_distance(*pos\_1: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")] | ndarray[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), ...], dtype[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]]*, *pos\_2: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")] | ndarray[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), ...], dtype[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]]*) → [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")[[source]](../_modules/mesa/space.html#ContinuousSpace.get_distance)
    :   Get the distance between two point, accounting for toroidal space.

        Parameters:
        :   - **pos\_1** – Coordinate tuples for point1.
            - **pos\_2** – Coordinate tuples for point2.

    torus\_adj(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")] | ndarray[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), ...], dtype[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]]*) → [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")] | ndarray[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), ...], dtype[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]][[source]](../_modules/mesa/space.html#ContinuousSpace.torus_adj)
    :   Adjust coordinates to handle torus looping.

        If the coordinate is out-of-bounds and the space is toroidal, return
        the corresponding point within the space. If the space is not toroidal,
        raise an exception.

        Parameters:
        :   **pos** – Coordinate tuple to convert.

    out\_of\_bounds(*pos: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)"), [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")] | ndarray[[tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), ...], dtype[[float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")]]*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/mesa/space.html#ContinuousSpace.out_of_bounds)
    :   Check if a point is out of bounds.

class NetworkGrid(*g: [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")*)[[source]](../_modules/mesa/space.html#NetworkGrid)
:   Network Grid where each node contains zero or more agents.

    Create a new network.

    Parameters:
    :   **g** – a NetworkX graph instance.

    property agents: [AgentSet](agentset.html#mesa.agentset.AgentSet "mesa.agentset.AgentSet")
    :   Return an AgentSet with the agents in the space.

    static default\_val() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[source]](../_modules/mesa/space.html#NetworkGrid.default_val)
    :   Default value for a new node.

    get\_neighborhood(*node\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")][[source]](../_modules/mesa/space.html#NetworkGrid.get_neighborhood)
    :   Get all adjacent nodes within a certain radius.

        Parameters:
        :   - **node\_id** – node id for which to get neighborhood
            - **include\_center** – boolean to include node itself or not
            - **radius** – size of neighborhood

        Returns:
        :   a list

    get\_neighbors(*node\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*, *include\_center: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *radius: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")][[source]](../_modules/mesa/space.html#NetworkGrid.get_neighbors)
    :   Get all agents in adjacent nodes (within a certain radius).

        Parameters:
        :   - **node\_id** – node id for which to get neighbors
            - **include\_center** – whether to include node itself or not
            - **radius** – size of neighborhood in which to find neighbors

        Returns:
        :   list of agents in neighborhood.

    move\_agent(*agent: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*, *node\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/space.html#NetworkGrid.move_agent)
    :   Move an agent from its current node to a new node.

        Parameters:
        :   - **agent** – agent instance
            - **node\_id** – id of node

    remove\_agent(*agent: [Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/space.html#NetworkGrid.remove_agent)
    :   Remove the agent from the network and set its pos attribute to None.

        Parameters:
        :   **agent** – agent instance

    is\_cell\_empty(*node\_id: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*) → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/mesa/space.html#NetworkGrid.is_cell_empty)
    :   Returns a bool of the contents of a cell.

        Parameters:
        :   **node\_id** – id of node

    get\_cell\_list\_contents(*cell\_list: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")][[source]](../_modules/mesa/space.html#NetworkGrid.get_cell_list_contents)
    :   Returns a list of the agents contained in the nodes identified in cell\_list.

        Nodes with empty content are excluded.

        Parameters:
        :   **cell\_list** – list of cell ids.

        Returns:
        :   list of the agents contained in the nodes identified in cell\_list.

    get\_all\_cell\_contents() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")][[source]](../_modules/mesa/space.html#NetworkGrid.get_all_cell_contents)
    :   Returns a list of all the agents in the network.

    iter\_cell\_list\_contents(*cell\_list: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [Iterator](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator "(in Python v3.14)")[[Agent](../mesa.html#mesa.agent.Agent "mesa.agent.Agent")][[source]](../_modules/mesa/space.html#NetworkGrid.iter_cell_list_contents)
    :   Returns an iterator of the agents contained in the nodes identified in cell\_list.

        Nodes with empty content are excluded.

        Parameters:
        :   **cell\_list** – list of cell ids.

        Returns:
        :   iterator of the agents contained in the nodes identified in cell\_list.

On this page

### This Page

- [Show Source](../_sources/apis/space.md.txt)

---

Original source: https://mesa.readthedocs.io/stable/apis/space.html
