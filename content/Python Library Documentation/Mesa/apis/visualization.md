---
title: "Visualization"
source: "https://mesa.readthedocs.io/latest/apis/visualization.html"
imported_from: "Python library documentation"
library: "Mesa"
---

# Visualization

⚠️ **Important note for SolaraViz users**

When using **SolaraViz**, Mesa models must be instantiated **using keyword arguments only**.
SolaraViz creates model instances internally via keyword-based parameters, and positional arguments are **not supported**.

**Not supported:**

```
MyModel(10, 10)
```

**Supported:**

```
MyModel(width=10, height=10)
```

To avoid errors, it is recommended to define your model constructor with keyword-only arguments, for example:

```
class MyModel(Model):
    def __init__(self, *, width, height, seed=None):
        ...
```

For detailed tutorials, please refer to:

- [Basic Visualization](#../tutorials/4_visualization_basic)
- [Dynamic Agent Visualization](#../tutorials/5_visualization_dynamic_agents)
- [Custom Agent Visualization](#../tutorials/6_visualization_custom)

## Jupyter Visualization

Mesa visualization module for creating interactive model visualizations.

This module provides components to create browser- and Jupyter notebook-based visualizations of
Mesa models, allowing users to watch models run step-by-step and interact with model parameters.

Key features:
:   - SolaraViz: Main component for creating visualizations, supporting grid displays and plots
    - ModelController: Handles model execution controls (step, play, pause, reset)
    - UserInputs: Generates UI elements for adjusting model parameters

The module uses Solara for rendering in Jupyter notebooks or as standalone web applications.
It supports various types of visualizations including matplotlib plots, agent grids, and
custom visualization components.

Usage:
:   1. Define an agent\_portrayal function to specify how agents should be displayed
    2. Set up model\_params to define adjustable parameters
    3. Create a SolaraViz instance with your model, parameters, and desired measures
    4. Display the visualization in a Jupyter notebook or run as a Solara app

See the Visualization Tutorial and example models for more details.

create\_space\_component(*renderer: [SpaceRenderer](#mesa.visualization.space_renderer.SpaceRenderer "mesa.visualization.space_renderer.SpaceRenderer")*)[[source]](../_modules/mesa/visualization/solara_viz.html#create_space_component)
:   Create a space visualization component for the given renderer.

split\_model\_params(*model\_params*)[[source]](../_modules/mesa/visualization/solara_viz.html#split_model_params)
:   Split model parameters into user-adjustable and fixed parameters.

    Parameters:
    :   **model\_params** – Dictionary of all model parameters

    Returns:
    :   (user\_adjustable\_params, fixed\_params)

    Return type:
    :   [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")

check\_param\_is\_fixed(*param*)[[source]](../_modules/mesa/visualization/solara_viz.html#check_param_is_fixed)
:   Check if a parameter is fixed (not user-adjustable).

    Parameters:
    :   **param** – Parameter to check

    Returns:
    :   True if parameter is fixed, False otherwise

    Return type:
    :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

make\_initial\_grid\_layout(*num\_components*)[[source]](../_modules/mesa/visualization/solara_viz.html#make_initial_grid_layout)
:   Create an initial grid layout for visualization components.

    Parameters:
    :   **num\_components** – Number of components to display

    Returns:
    :   Initial grid layout configuration

    Return type:
    :   [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")

copy\_renderer(*renderer: [SpaceRenderer](#mesa.visualization.space_renderer.SpaceRenderer "mesa.visualization.space_renderer.SpaceRenderer")*, *model: [Model](../mesa.html#mesa.model.Model "mesa.model.Model")*)[[source]](../_modules/mesa/visualization/solara_viz.html#copy_renderer)
:   Create a new renderer instance with the same configuration as the original.

Custom visualization components.

class AgentPortrayalStyle(*x: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *y: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *color: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 'tab:blue'*, *marker: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 'o'*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 50*, *zorder: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 1*, *alpha: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 1.0*, *edgecolors: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *linewidths: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 1.0*, *tooltip: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/mesa/visualization/components/portrayal_components.html#AgentPortrayalStyle)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

    Represents the visual styling options for an agent in a visualization.

    User facing component to control how agents are drawn.
    Allows specifying properties like color, size,
    marker shape, position, and other plot attributes.

    x, y are determined automatically according to the agent’s type
    (normal/CellAgent) and position in the space if not manually declared.

    Example

    ```
    >>> def agent_portrayal(agent):
    >>>     return AgentPortrayalStyle(
    >>>         x=agent.cell.coordinate[0],
    >>>         y=agent.cell.coordinate[1],
    >>>         color="red",
    >>>         marker="o",
    >>>         size=20,
    >>>         zorder=2,
    >>>         alpha=0.8,
    >>>         edgecolors="black",
    >>>         linewidths=1.5
    >>>     )
    >>>
    >>> # or for a default agent portrayal
    >>> def agent_portrayal(agent):
    >>>     return AgentPortrayalStyle()
    ```

    x: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None

    y: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None

    color: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 'tab:blue'

    marker: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 'o'

    size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 50

    zorder: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 1

    alpha: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 1.0

    edgecolors: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None

    linewidths: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 1.0

    tooltip: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None

    update(*\*updates\_fields: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*)[[source]](../_modules/mesa/visualization/components/portrayal_components.html#AgentPortrayalStyle.update)
    :   Updates attributes from variable (field\_name, new\_value) tuple arguments.

        Example

        ```
        >>> def agent_portrayal(agent):
        >>>     primary_style = AgentPortrayalStyle(color="blue", marker="^", size=10, x=agent.pos[0], y=agent.pos[1])
        >>>     if agent.type == 1:
        >>>         primary_style.update(("color", "red"), ("size", 30))
        >>>     return primary_style
        ```

class PropertyLayerStyle(*colormap: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *color: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *alpha: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 0.8*, *colorbar: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *vmin: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *vmax: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/mesa/visualization/components/portrayal_components.html#PropertyLayerStyle)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

    Represents the visual styling options for a property layer in a visualization.

    User facing component to control how property layers are drawn.
    Allows specifying properties like colormap, single color, value limits
    (vmin, vmax), transparency (alpha) and colorbar visibility.

    Note: vmin and vmax are the lower and upper bounds for the colorbar and the data is
    normalized between these values for color/colormap rendering. If they are not
    declared the values are automatically determined from the data range.

    Note: You can specify either a ‘colormap’ (for varying data) or a single
    ‘color’ (for a uniform layer appearance), but not both simultaneously.

    Example

    ```
    >>> def property_layer_portrayal(layer):
    >>>     return PropertyLayerStyle(colormap="viridis", vmin=0, vmax=100, alpha=0.5, colorbar=True)
    >>> # or for a uniform color layer
    >>> def property_layer_portrayal(layer):
    >>>     return PropertyLayerStyle(color="lightblue", alpha=0.8, colorbar=False)
    ```

    colormap: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None

    color: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None

    alpha: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 0.8

    colorbar: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True

    vmin: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None

    vmax: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None

make\_altair\_space(*agent\_portrayal*, *property\_layer\_portrayal=None*, *post\_process=None*, *\*\*space\_drawing\_kwargs*)[[source]](../_modules/mesa/visualization/components/altair_components.html#make_altair_space)
:   Create an Altair-based space visualization component.

    Parameters:
    :   - **agent\_portrayal** – Function to portray agents.
        - **property\_layer\_portrayal** – Dictionary of property\_layer portrayal specifications
        - **post\_process** – A user specified callable that will be called with the Chart instance from Altair. Allows for fine tuning plots (e.g., control ticks)
        - **space\_drawing\_kwargs** – not yet implemented

    `agent_portrayal` is called with an agent and should return a dict. Valid fields in this dict are “color”,
    “size”, “marker”, and “zorder”. Other field are ignored and will result in a user warning.

    Returns:
    :   A function that creates a SpaceMatplotlib component

    Return type:
    :   [function](time.html#mesa.time.EventGenerator.function "mesa.time.EventGenerator.function")

make\_mpl\_plot\_component(*measure: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *post\_process: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *page: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *save\_format='png'*)[[source]](../_modules/mesa/visualization/components/matplotlib_components.html#make_mpl_plot_component)
:   Create a plotting function for a specified measure.

    Parameters:
    :   - **measure** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *|* [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]* *|* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]* *|* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]*) – Measure(s) to plot.
        - **post\_process** – a user-specified callable to do post-processing called with the Axes instance.
        - **page** – Page number where the plot should be displayed.
        - **save\_format** – save format of figure in solara backend

    Returns:
    :   A tuple of a function that creates a PlotMatplotlib component and a page number.

    Return type:
    :   ([function](time.html#mesa.time.EventGenerator.function "mesa.time.EventGenerator.function"), page)

make\_mpl\_space\_component(*agent\_portrayal: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *property\_layer\_portrayal: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *post\_process: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*space\_drawing\_kwargs*) → SpaceMatplotlib[[source]](../_modules/mesa/visualization/components/matplotlib_components.html#make_mpl_space_component)
:   Create a Matplotlib-based space visualization component.

    Parameters:
    :   - **agent\_portrayal** – Function to portray agents.
        - **property\_layer\_portrayal** – Dictionary of property\_layer portrayal specifications
        - **post\_process** – a callable that will be called with the Axes instance. Allows for fine tuning plots (e.g., control ticks)
        - **space\_drawing\_kwargs** – additional keyword arguments to be passed on to the underlying space drawer function. See
          the functions for drawing the various spaces for further details.

    `agent_portrayal` is called with an agent and should return a dict. Valid fields in this dict are “color”,
    “size”, “marker”, “zorder”, alpha, linewidths, and edgecolors. Other field are ignored and will result in a user warning.

    Returns:
    :   A function that creates a SpaceMatplotlib component

    Return type:
    :   [function](time.html#mesa.time.EventGenerator.function "mesa.time.EventGenerator.function")

make\_plot\_component(*measure: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *post\_process: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *backend: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'matplotlib'*, *page: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *\*\*plot\_drawing\_kwargs*)[[source]](../_modules/mesa/visualization/components/__init__.html#make_plot_component)
:   Create a plotting function for a specified measure using the specified backend.

    Parameters:
    :   - **measure** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *|* [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]* *|* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]* *|* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]*) – Measure(s) to plot.
        - **post\_process** – a user-specified callable to do post-processing called with the Axes instance.
        - **backend** – the backend to use {“matplotlib”, “altair”}
        - **page** – Page number where the plot should be displayed (default 0).
        - **plot\_drawing\_kwargs** – additional keyword arguments to pass onto the backend specific function for making a plotting component

    Returns:
    :   A tuple of a function and page number that creates a plot component on that specific page.

    Return type:
    :   ([function](time.html#mesa.time.EventGenerator.function "mesa.time.EventGenerator.function"), page)

make\_space\_component(*agent\_portrayal: Callable | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *property\_layer\_portrayal: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *post\_process: Callable | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *backend: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = 'matplotlib'*, *\*\*space\_drawing\_kwargs*) → SpaceMatplotlib | SpaceAltair[[source]](../_modules/mesa/visualization/components/__init__.html#make_space_component)
:   Create a Matplotlib-based space visualization component.

    Parameters:
    :   - **agent\_portrayal** – Function to portray agents.
        - **property\_layer\_portrayal** – Dictionary of property\_layer portrayal specifications
        - **post\_process** – a callable that will be called with the Axes instance. Allows for fine-tuning plots (e.g., control ticks)
        - **backend** – the backend to use {“matplotlib”, “altair”}
        - **space\_drawing\_kwargs** – additional keyword arguments to be passed on to the underlying backend specific space drawer function. See
          the functions for drawing the various spaces for the appropriate backend further details.

    Returns:
    :   A function that creates a space component

    Return type:
    :   [function](time.html#mesa.time.EventGenerator.function "mesa.time.EventGenerator.function")

## User Parameters

Solara visualization related helper classes.

class UserParam[[source]](../_modules/mesa/visualization/user_param.html#UserParam)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

    UserParam.

    maybe\_raise\_error(*param\_type*, *valid*)[[source]](../_modules/mesa/visualization/user_param.html#UserParam.maybe_raise_error)

class Slider(*label=''*, *value=None*, *min=None*, *max=None*, *step=1*, *dtype=None*)[[source]](../_modules/mesa/visualization/user_param.html#Slider)
:   Bases: [`UserParam`](#mesa.visualization.user_param.UserParam "mesa.visualization.user_param.UserParam")

    A number-based slider input with settable increment.

    Example:
    slider\_option = Slider(“My Slider”, value=123, min=10, max=200, step=0.1)

    Parameters:
    :   - **label** – The displayed label in the UI
        - **value** – The initial value of the slider
        - **min** – The minimum possible value of the slider
        - **max** – The maximum possible value of the slider
        - **step** – The step between min and max for a range of possible values
        - **dtype** – either int or float

    Initializes a slider.

    Parameters:
    :   - **label** – The displayed label in the UI
        - **value** – The initial value of the slider
        - **min** – The minimum possible value of the slider
        - **max** – The maximum possible value of the slider
        - **step** – The step between min and max for a range of possible values
        - **dtype** – either int or float

    get(*attr*)[[source]](../_modules/mesa/visualization/user_param.html#Slider.get)

## Matplotlib-based visualizations

Matplotlib based solara components for visualization MESA spaces and plots.

make\_space\_matplotlib(*\*args*, *\*\*kwargs*)[[source]](../_modules/mesa/visualization/components/matplotlib_components.html#make_space_matplotlib)

make\_mpl\_space\_component(*agent\_portrayal: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *property\_layer\_portrayal: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *post\_process: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*space\_drawing\_kwargs*) → SpaceMatplotlib[[source]](../_modules/mesa/visualization/components/matplotlib_components.html#make_mpl_space_component)
:   Create a Matplotlib-based space visualization component.

    Parameters:
    :   - **agent\_portrayal** – Function to portray agents.
        - **property\_layer\_portrayal** – Dictionary of property\_layer portrayal specifications
        - **post\_process** – a callable that will be called with the Axes instance. Allows for fine tuning plots (e.g., control ticks)
        - **space\_drawing\_kwargs** – additional keyword arguments to be passed on to the underlying space drawer function. See
          the functions for drawing the various spaces for further details.

    `agent_portrayal` is called with an agent and should return a dict. Valid fields in this dict are “color”,
    “size”, “marker”, “zorder”, alpha, linewidths, and edgecolors. Other field are ignored and will result in a user warning.

    Returns:
    :   A function that creates a SpaceMatplotlib component

    Return type:
    :   [function](time.html#mesa.time.EventGenerator.function "mesa.time.EventGenerator.function")

make\_plot\_measure(*\*args*, *\*\*kwargs*)[[source]](../_modules/mesa/visualization/components/matplotlib_components.html#make_plot_measure)

make\_mpl\_plot\_component(*measure: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *post\_process: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *page: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *save\_format='png'*)[[source]](../_modules/mesa/visualization/components/matplotlib_components.html#make_mpl_plot_component)
:   Create a plotting function for a specified measure.

    Parameters:
    :   - **measure** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *|* [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]* *|* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]* *|* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]*) – Measure(s) to plot.
        - **post\_process** – a user-specified callable to do post-processing called with the Axes instance.
        - **page** – Page number where the plot should be displayed.
        - **save\_format** – save format of figure in solara backend

    Returns:
    :   A tuple of a function that creates a PlotMatplotlib component and a page number.

    Return type:
    :   ([function](time.html#mesa.time.EventGenerator.function "mesa.time.EventGenerator.function"), page)

Helper functions for drawing mesa spaces with matplotlib.

These functions are used by the provided matplotlib components, but can also be used to quickly visualize
a space with matplotlib for example when creating a mp4 of a movie run or when needing a figure
for a paper.

collect\_agent\_data(*space: [OrthogonalMooreGrid](discrete_space.html#mesa.discrete_space.grid.OrthogonalMooreGrid "mesa.discrete_space.grid.OrthogonalMooreGrid") | [OrthogonalVonNeumannGrid](discrete_space.html#mesa.discrete_space.grid.OrthogonalVonNeumannGrid "mesa.discrete_space.grid.OrthogonalVonNeumannGrid") | [HexGrid](discrete_space.html#mesa.discrete_space.grid.HexGrid "mesa.discrete_space.grid.HexGrid") | [Network](discrete_space.html#mesa.discrete_space.network.Network "mesa.discrete_space.network.Network") | ContinuousSpace | [VoronoiGrid](discrete_space.html#mesa.discrete_space.voronoi.VoronoiGrid "mesa.discrete_space.voronoi.VoronoiGrid")*, *agent\_portrayal: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *default\_size: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[source]](../_modules/mesa/visualization/mpl_space_drawing.html#collect_agent_data)
:   Collect the plotting data for all agents in the space.

    Parameters:
    :   - **space** – The space containing the Agents.
        - **agent\_portrayal** – A callable that is called with the agent and returns a AgentPortrayalStyle
        - **default\_size** – default size

    agent\_portrayal should return a AgentPortrayalStyle, limited to size (size of marker), color (color of marker), zorder (z-order),
    marker (marker style), alpha, linewidths, and edgecolors.

draw\_space(*space*, *agent\_portrayal: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *property\_layer\_portrayal: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *ax: Axes | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*space\_drawing\_kwargs*)[[source]](../_modules/mesa/visualization/mpl_space_drawing.html#draw_space)
:   Draw a Matplotlib-based visualization of the space.

    Parameters:
    :   - **space** – the space of the mesa model
        - **agent\_portrayal** – A callable that returns a AgnetPortrayalStyle specifying how to show the agent
        - **property\_layer\_portrayal** – A callable that returns a PropertyLayerStyle specifying how to show the property layer
        - **ax** – the axes upon which to draw the plot
        - **space\_drawing\_kwargs** – any additional keyword arguments to be passed on to the underlying function for drawing the space.

    Returns:
    :   Returns the Axes object with the plot drawn onto it.

    `agent_portrayal` is called with an agent and should return a AgentPortrayalStyle. Valid fields in this object are “color”,
    “size”, “marker”, “zorder”, alpha, linewidths, and edgecolors. Other field are ignored and will result in a user warning.

draw\_property\_layers(*space*, *property\_layer\_portrayal: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]] | [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *ax: Axes*)[[source]](../_modules/mesa/visualization/mpl_space_drawing.html#draw_property_layers)
:   Draw Property Layers on the given axes.

    Parameters:
    :   - **space** – The space having the property\_layer.
        - **property\_layer\_portrayal** (*Callable*) – A function that accepts a property layer object
          and returns either a PropertyLayerStyle object defining its visualization,
          or None to skip drawing this particular layer.
        - **ax** (*matplotlib.axes.Axes*) – The axes to draw on.

draw\_orthogonal\_grid(*space: [OrthogonalMooreGrid](discrete_space.html#mesa.discrete_space.grid.OrthogonalMooreGrid "mesa.discrete_space.grid.OrthogonalMooreGrid") | [OrthogonalVonNeumannGrid](discrete_space.html#mesa.discrete_space.grid.OrthogonalVonNeumannGrid "mesa.discrete_space.grid.OrthogonalVonNeumannGrid")*, *agent\_portrayal: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *ax: Axes | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *draw\_grid: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *\*\*kwargs*)[[source]](../_modules/mesa/visualization/mpl_space_drawing.html#draw_orthogonal_grid)
:   Visualize a orthogonal grid.

    Parameters:
    :   - **space** – the space to visualize
        - **agent\_portrayal** – a callable that is called with the agent and returns a AgentPortrayalStyle
        - **ax** – a Matplotlib Axes instance. If none is provided a new figure and ax will be created using plt.subplots
        - **draw\_grid** – whether to draw the grid
        - **kwargs** – additional keyword arguments passed to ax.scatter

    Returns:
    :   Returns the Axes object with the plot drawn onto it.

    `agent_portrayal` is called with an agent and should return a AgentPortrayalStyle. Valid fields in this object are “color”,
    “size”, “marker”, “zorder”, alpha, linewidths, and edgecolors. Other field are ignored and will result in a user warning.

draw\_hex\_grid(*space: [HexGrid](discrete_space.html#mesa.discrete_space.grid.HexGrid "mesa.discrete_space.grid.HexGrid")*, *agent\_portrayal: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *ax: Axes | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *draw\_grid: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *\*\*kwargs*)[[source]](../_modules/mesa/visualization/mpl_space_drawing.html#draw_hex_grid)
:   Visualize a hex grid.

    Parameters:
    :   - **space** – the space to visualize
        - **agent\_portrayal** – a callable that is called with the agent and returns a AgentPortrayalStyle
        - **ax** – a Matplotlib Axes instance. If none is provided a new figure and ax will be created using plt.subplots
        - **draw\_grid** – whether to draw the grid
        - **kwargs** – additional keyword arguments passed to ax.scatter

    Returns:
    :   Returns the Axes object with the plot drawn onto it.

    `agent_portrayal` is called with an agent and should return a AgentPortrayalStyle. Valid fields in this object are “color”,
    “size”, “marker”, “zorder”, alpha, linewidths, and edgecolors. Other field are ignored and will result in a user warning.

draw\_network(*space: [Network](discrete_space.html#mesa.discrete_space.network.Network "mesa.discrete_space.network.Network")*, *agent\_portrayal: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *ax: Axes | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *draw\_grid: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *\*\*kwargs*)[[source]](../_modules/mesa/visualization/mpl_space_drawing.html#draw_network)
:   Visualize a network space.

    Parameters:
    :   - **space** – the space to visualize
        - **agent\_portrayal** – a callable that is called with the agent and returns a AgentPortrayalStyle
        - **ax** – a Matplotlib Axes instance. If none is provided a new figure and ax will be created using plt.subplots
        - **draw\_grid** – whether to draw the grid
        - **kwargs** – additional keyword arguments passed to ax.scatter

    Returns:
    :   Returns the Axes object with the plot drawn onto it.

    `agent_portrayal` is called with an agent and should return a AgentPortrayalStyle. Valid fields in this object are “color”,
    “size”, “marker”, “zorder”, alpha, linewidths, and edgecolors. Other field are ignored and will result in a user warning.

draw\_continuous\_space(*space: ContinuousSpace*, *agent\_portrayal: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *ax: Axes | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *\*\*kwargs*)[[source]](../_modules/mesa/visualization/mpl_space_drawing.html#draw_continuous_space)
:   Visualize a continuous space.

    Parameters:
    :   - **space** – the space to visualize
        - **agent\_portrayal** – a callable that is called with the agent and returns a AgentPortrayalStyle
        - **ax** – a Matplotlib Axes instance. If none is provided a new figure and ax will be created using plt.subplots
        - **kwargs** – additional keyword arguments passed to ax.scatter

    Returns:
    :   Returns the Axes object with the plot drawn onto it.

    `agent_portrayal` is called with an agent and should return a AgentPortrayalStyle. Valid fields in this object are “color”,
    “size”, “marker”, “zorder”, alpha, linewidths, and edgecolors. Other field are ignored and will result in a user warning.

draw\_voronoi\_grid(*space: [VoronoiGrid](discrete_space.html#mesa.discrete_space.voronoi.VoronoiGrid "mesa.discrete_space.voronoi.VoronoiGrid")*, *agent\_portrayal: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *ax: Axes | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *draw\_grid: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *\*\*kwargs*)[[source]](../_modules/mesa/visualization/mpl_space_drawing.html#draw_voronoi_grid)
:   Visualize a voronoi grid.

    Parameters:
    :   - **space** – the space to visualize
        - **agent\_portrayal** – a callable that is called with the agent and returns a AgentPortrayalStyle
        - **ax** – a Matplotlib Axes instance. If none is provided a new figure and ax will be created using plt.subplots
        - **draw\_grid** – whether to draw the grid or not
        - **kwargs** – additional keyword arguments passed to ax.scatter

    Returns:
    :   Returns the Axes object with the plot drawn onto it.

    `agent_portrayal` is called with an agent and should return a AgentPortrayalStyle. Valid fields in this object are “color”,
    “size”, “marker”, “zorder”, alpha, linewidths, and edgecolors. Other field are ignored and will result in a user warning.

## Altair-based visualizations

Altair based solara components for visualization mesa spaces.

make\_space\_altair(*\*args*, *\*\*kwargs*)[[source]](../_modules/mesa/visualization/components/altair_components.html#make_space_altair)

make\_altair\_space(*agent\_portrayal*, *property\_layer\_portrayal=None*, *post\_process=None*, *\*\*space\_drawing\_kwargs*)[[source]](../_modules/mesa/visualization/components/altair_components.html#make_altair_space)
:   Create an Altair-based space visualization component.

    Parameters:
    :   - **agent\_portrayal** – Function to portray agents.
        - **property\_layer\_portrayal** – Dictionary of property\_layer portrayal specifications
        - **post\_process** – A user specified callable that will be called with the Chart instance from Altair. Allows for fine tuning plots (e.g., control ticks)
        - **space\_drawing\_kwargs** – not yet implemented

    `agent_portrayal` is called with an agent and should return a dict. Valid fields in this dict are “color”,
    “size”, “marker”, and “zorder”. Other field are ignored and will result in a user warning.

    Returns:
    :   A function that creates a SpaceMatplotlib component

    Return type:
    :   [function](time.html#mesa.time.EventGenerator.function "mesa.time.EventGenerator.function")

chart\_property\_layers(*space*, *property\_layer\_portrayal*, *chart\_width*, *chart\_height*)[[source]](../_modules/mesa/visualization/components/altair_components.html#chart_property_layers)
:   Creates Property Layers in the Altair Components.

    Parameters:
    :   - **space** – the ContinuousSpace instance
        - **property\_layer\_portrayal** – Dictionary of property\_layer portrayal specifications
        - **chart\_width** – width of the agent chart to maintain consistency with the property\_layer charts
        - **chart\_height** – height of the agent chart to maintain consistency with the property\_layer charts

    Returns:
    :   Altair Chart

make\_altair\_plot\_component(*measure: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")] | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")]*, *post\_process: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *page: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 0*, *grid=False*)[[source]](../_modules/mesa/visualization/components/altair_components.html#make_altair_plot_component)
:   Create a plotting function for a specified measure.

    Parameters:
    :   - **measure** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") *|* [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* [*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]* *|* [*list*](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]* *|* [*tuple*](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")*[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*]*) – Measure(s) to plot.
        - **post\_process** – a user-specified callable to do post-processing called with the Axes instance.
        - **page** – Page number where the plot should be displayed.
        - **grid** – Bool to draw grid or not.

    Returns:
    :   A tuple of a function that creates a PlotAltair component and a page number.

    Return type:
    :   ([function](time.html#mesa.time.EventGenerator.function "mesa.time.EventGenerator.function"), page)

## Command Console

A command console interface for interactive Python code execution in the browser.

This module provides a set of classes and functions to create an interactive Python console
that can be embedded in a web browser. It supports command history, multi-line code blocks,
and special commands for console management.

Notes

- The console supports multi-line code blocks with proper indentation
- Output is captured and displayed with appropriate formatting
- Error messages are displayed in red with distinct styling
- The console maintains a history of commands and their outputs

class ConsoleEntry(*command: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *output: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''*, *is\_error: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*, *is\_continuation: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False*)[[source]](../_modules/mesa/visualization/command_console.html#ConsoleEntry)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

    A class to store command console entries.

    command
    :   The command entered

        Type:
        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    output
    :   The output of the command

        Type:
        :   [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    is\_error
    :   Whether the entry represents an error

        Type:
        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    is\_continuation
    :   Whether the entry is a continuation of previous command

        Type:
        :   [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")

    command: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")

    output: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") = ''

    is\_error: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False

    is\_continuation: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = False

class CaptureOutput[[source]](../_modules/mesa/visualization/command_console.html#CaptureOutput)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

    A context manager for capturing stdout and stderr output.

    This class provides a way to capture output that would normally be printed
    to stdout and stderr during the execution of code within its context.

    Initialize the CaptureOutput context manager with empty string buffers.

    get\_output()[[source]](../_modules/mesa/visualization/command_console.html#CaptureOutput.get_output)
    :   Retrieve and clear the captured output.

        Returns:
        :   A pair of strings (stdout\_output, stderr\_output)

        Return type:
        :   [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")

class InteractiveConsole(*locals\_dict=None*)[[source]](../_modules/mesa/visualization/command_console.html#InteractiveConsole)
:   Bases: [`InteractiveConsole`](https://docs.python.org/3/library/code.html#code.InteractiveConsole "(in Python v3.14)")

    A custom interactive Python console with output capturing capabilities.

    This class extends code.InteractiveConsole to provide output capturing functionality
    when executing Python code interactively.

    Parameters:
    :   **locals\_dict** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")*,* *optional*) – Dictionary of local variables. Defaults to None.

    Initialize the InteractiveConsole with the provided locals dictionary.

    push(*line*)[[source]](../_modules/mesa/visualization/command_console.html#InteractiveConsole.push)
    :   Push a line to the command interpreter and execute it.

        This method captures the output of the executed command and returns both
        the ‘more’ flag and the captured output.

        Parameters:
        :   **line** ([*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")) – The line of code to be executed.

        Returns:
        :   A tuple containing:
            :   - more (bool): Flag indicating if more input is needed
                - str: The captured output from executing the command

        Return type:
        :   [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")

class ConsoleManager(*model=None*, *additional\_imports=None*)[[source]](../_modules/mesa/visualization/command_console.html#ConsoleManager)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

    A console manager for executing Python code interactively.

    This class provides functionality to execute Python code in an interactive console environment,
    maintain command history, and handle multi-line code blocks.

    locals\_dict
    :   Dictionary containing local variables available to the console

        Type:
        :   [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")

    console
    :   Python’s interactive console instance

        Type:
        :   [InteractiveConsole](#mesa.visualization.command_console.InteractiveConsole "mesa.visualization.command_console.InteractiveConsole")

    buffer
    :   Buffer for storing multi-line code blocks

        Type:
        :   [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")

    history
    :   List of console entries containing commands and their outputs

        Type:
        :   [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[ConsoleEntry](#mesa.visualization.command_console.ConsoleEntry "mesa.visualization.command_console.ConsoleEntry")]

    Special Commands:
    :   1. history : Shows the command history
        2. cls : Clears the console screen
        3. tips : Shows available console commands and usage tips

    Example

    ```
    >>> console = ConsoleManager(model=my_model)
    >>> console.execute_code("print('hello world')", set_input_callback)
    ```

    Initialize the console manager with the provided model and imports.

    history: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[ConsoleEntry](#mesa.visualization.command_console.ConsoleEntry "mesa.visualization.command_console.ConsoleEntry")]

    execute\_code(*code\_line: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *set\_input\_text: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/visualization/command_console.html#ConsoleManager.execute_code)
    :   Execute the provided code line and update the console history.

    clear\_console() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/visualization/command_console.html#ConsoleManager.clear_console)
    :   Clear the console history and reset the console state.

    get\_entries() → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[ConsoleEntry](#mesa.visualization.command_console.ConsoleEntry "mesa.visualization.command_console.ConsoleEntry")][[source]](../_modules/mesa/visualization/command_console.html#ConsoleManager.get_entries)
    :   Get the list of console entries.

    prev\_command(*current\_text: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*, *set\_input\_text: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/visualization/command_console.html#ConsoleManager.prev_command)
    :   Navigate to previous command in history.

    next\_command(*set\_input\_text: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")[[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/visualization/command_console.html#ConsoleManager.next_command)
    :   Navigate to next command in history.

format\_command\_html(*entry*)[[source]](../_modules/mesa/visualization/command_console.html#format_command_html)
:   Format the command part of a console entry as HTML.

format\_output\_html(*entry*)[[source]](../_modules/mesa/visualization/command_console.html#format_output_html)
:   Format the output part of a console entry as HTML.

## Portrayal Components

Portrayal Components Module.

This module defines data structures for styling visual elements in Mesa agent-based model visualizations.
It provides user-facing classes to specify how agents and property layers should appear in the rendered space.

Classes:
1. AgentPortrayalStyle: Controls the appearance of individual agents (e.g., color, shape, size, etc.).
2. PropertyLayerStyle: Controls the appearance of background property layers (e.g., color gradients or uniform fills).

These components are designed to be passed into Mesa visualizations to customize and standardize how data is presented.

class AgentPortrayalStyle(*x: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *y: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *color: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 'tab:blue'*, *marker: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 'o'*, *size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 50*, *zorder: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 1*, *alpha: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 1.0*, *edgecolors: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *linewidths: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 1.0*, *tooltip: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/mesa/visualization/components/portrayal_components.html#AgentPortrayalStyle)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

    Represents the visual styling options for an agent in a visualization.

    User facing component to control how agents are drawn.
    Allows specifying properties like color, size,
    marker shape, position, and other plot attributes.

    x, y are determined automatically according to the agent’s type
    (normal/CellAgent) and position in the space if not manually declared.

    Example

    ```
    >>> def agent_portrayal(agent):
    >>>     return AgentPortrayalStyle(
    >>>         x=agent.cell.coordinate[0],
    >>>         y=agent.cell.coordinate[1],
    >>>         color="red",
    >>>         marker="o",
    >>>         size=20,
    >>>         zorder=2,
    >>>         alpha=0.8,
    >>>         edgecolors="black",
    >>>         linewidths=1.5
    >>>     )
    >>>
    >>> # or for a default agent portrayal
    >>> def agent_portrayal(agent):
    >>>     return AgentPortrayalStyle()
    ```

    x: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None

    y: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None

    color: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 'tab:blue'

    marker: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 'o'

    size: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 50

    zorder: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 1

    alpha: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 1.0

    edgecolors: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None

    linewidths: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 1.0

    tooltip: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None

    update(*\*updates\_fields: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*)[[source]](../_modules/mesa/visualization/components/portrayal_components.html#AgentPortrayalStyle.update)
    :   Updates attributes from variable (field\_name, new\_value) tuple arguments.

        Example

        ```
        >>> def agent_portrayal(agent):
        >>>     primary_style = AgentPortrayalStyle(color="blue", marker="^", size=10, x=agent.pos[0], y=agent.pos[1])
        >>>     if agent.type == 1:
        >>>         primary_style.update(("color", "red"), ("size", 30))
        >>>     return primary_style
        ```

class PropertyLayerStyle(*colormap: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *color: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *alpha: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 0.8*, *colorbar: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *vmin: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *vmax: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/mesa/visualization/components/portrayal_components.html#PropertyLayerStyle)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

    Represents the visual styling options for a property layer in a visualization.

    User facing component to control how property layers are drawn.
    Allows specifying properties like colormap, single color, value limits
    (vmin, vmax), transparency (alpha) and colorbar visibility.

    Note: vmin and vmax are the lower and upper bounds for the colorbar and the data is
    normalized between these values for color/colormap rendering. If they are not
    declared the values are automatically determined from the data range.

    Note: You can specify either a ‘colormap’ (for varying data) or a single
    ‘color’ (for a uniform layer appearance), but not both simultaneously.

    Example

    ```
    >>> def property_layer_portrayal(layer):
    >>>     return PropertyLayerStyle(colormap="viridis", vmin=0, vmax=100, alpha=0.5, colorbar=True)
    >>> # or for a uniform color layer
    >>> def property_layer_portrayal(layer):
    >>>     return PropertyLayerStyle(color="lightblue", alpha=0.8, colorbar=False)
    ```

    colormap: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None

    color: [str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None

    alpha: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") = 0.8

    colorbar: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True

    vmin: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None

    vmax: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None

## Backends

Visualization backends for Mesa space rendering.

This module provides different backend implementations for visualizing
Mesa agent-based model spaces and components.

These backends are used internally by the space renderer and are not intended for
direct use by end users. See SpaceRenderer for actual usage and setting up
visualizations.

Available Backends:
:   1. AltairBackend
    2. MatplotlibBackend

class AltairBackend(*space\_drawer*)[[source]](../_modules/mesa/visualization/backends/altair_backend.html#AltairBackend)
:   Bases: [`AbstractRenderer`](#mesa.visualization.backends.abstract_renderer.AbstractRenderer "mesa.visualization.backends.abstract_renderer.AbstractRenderer")

    Altair-based renderer for Mesa spaces.

    This module provides an Altair-based renderer for visualizing Mesa model spaces,
    agents, and property layers with interactive charting capabilities.

    Initialize the renderer.

    Parameters:
    :   - **space\_drawer** – Object responsible for drawing space elements. Checkout SpaceDrawer
        - **functions.** (*for more details on the detailed implementations* *of* *the drawing*)

    initialize\_canvas() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/visualization/backends/altair_backend.html#AltairBackend.initialize_canvas)
    :   Initialize the Altair canvas.

    draw\_structure(*\*\*kwargs*) → Chart[[source]](../_modules/mesa/visualization/backends/altair_backend.html#AltairBackend.draw_structure)
    :   Draw the space structure using Altair.

        Parameters:
        :   - **\*\*kwargs** – Additional arguments passed to the space drawer.
            - **\*\*kwargs.** (*Checkout respective SpaceDrawer class on details how to pass*) –

        Returns:
        :   The Altair chart representing the space structure.

        Return type:
        :   alt.Chart

    collect\_agent\_data(*space*, *agent\_portrayal: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *default\_size: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/mesa/visualization/backends/altair_backend.html#AltairBackend.collect_agent_data)
    :   Collect plotting data for all agents in the space for Altair.

        Parameters:
        :   - **space** – The Mesa space containing agents.
            - **agent\_portrayal** – Callable that returns AgentPortrayalStyle for each agent.
            - **default\_size** – Default marker size if not specified in portrayal.

        Returns:
        :   Dictionary containing agent plotting data arrays.

        Return type:
        :   [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")

    draw\_agents(*arguments*, *chart\_width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 450*, *chart\_height: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 350*, *\*\*kwargs*)[[source]](../_modules/mesa/visualization/backends/altair_backend.html#AltairBackend.draw_agents)
    :   Draw agents using Altair backend.

        Parameters:
        :   - **arguments** – Dictionary containing agent data arrays.
            - **chart\_width** – Width of the chart.
            - **chart\_height** – Height of the chart.
            - **\*\*kwargs** – Additional keyword arguments for customization.
            - **\*\*kwargs.** (*Checkout respective SpaceDrawer class on details how to pass*) –

        Returns:
        :   The Altair chart representing the agents, or None if no agents.

        Return type:
        :   alt.Chart

    draw\_property\_layer(*space*, *property\_layers: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), ndarray]*, *property\_layer\_portrayal: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *chart\_width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 450*, *chart\_height: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 350*)[[source]](../_modules/mesa/visualization/backends/altair_backend.html#AltairBackend.draw_property_layer)
    :   Draw property layers using Altair backend.

        Parameters:
        :   - **space** – The Mesa space object containing the property layers.
            - **property\_layers** – A dictionary mapping property\_layer names to numpy arrays.
            - **property\_layer\_portrayal** – A function that returns PropertyLayerStyle
              that contains the visualization parameters.
            - **chart\_width** – The width of the chart.
            - **chart\_height** – The height of the chart.

        Returns:
        :   A tuple containing the base chart and the color bar chart.

        Return type:
        :   alt.Chart

class MatplotlibBackend(*space\_drawer*)[[source]](../_modules/mesa/visualization/backends/matplotlib_backend.html#MatplotlibBackend)
:   Bases: [`AbstractRenderer`](#mesa.visualization.backends.abstract_renderer.AbstractRenderer "mesa.visualization.backends.abstract_renderer.AbstractRenderer")

    Matplotlib-based renderer for Mesa spaces.

    Provides visualization capabilities using Matplotlib for rendering
    space structures, agents, and property layers.

    Initialize the Matplotlib backend.

    Parameters:
    :   **space\_drawer** – An instance of a SpaceDrawer class that handles
        the drawing of the space structure.

    initialize\_canvas(*ax=None*)[[source]](../_modules/mesa/visualization/backends/matplotlib_backend.html#MatplotlibBackend.initialize_canvas)
    :   Initialize the matplotlib canvas.

        Parameters:
        :   **ax** (*matplotlib.axes.Axes**,* *optional*) – Existing axes to use.
            If None, creates new figure and axes.

    draw\_structure(*\*\*kwargs*)[[source]](../_modules/mesa/visualization/backends/matplotlib_backend.html#MatplotlibBackend.draw_structure)
    :   Draw the space structure using matplotlib.

        Parameters:
        :   - **\*\*kwargs** – Additional arguments passed to the space drawer.
            - **\*\*kwargs.** (*Checkout respective SpaceDrawer class on details how to pass*) –

        Returns:
        :   The matplotlib axes with the drawn structure.

    collect\_agent\_data(*space*, *agent\_portrayal*, *default\_size=None*)[[source]](../_modules/mesa/visualization/backends/matplotlib_backend.html#MatplotlibBackend.collect_agent_data)
    :   Collect plotting data for all agents in the space.

        Parameters:
        :   - **space** – The Mesa space containing agents.
            - **agent\_portrayal** (*Callable*) – Function that returns AgentPortrayalStyle for each agent.
            - **default\_size** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) – Default marker size if not specified in portrayal.

        Returns:
        :   Dictionary containing agent plotting data arrays.

        Return type:
        :   [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")

    draw\_agents(*arguments*, *\*\*kwargs*)[[source]](../_modules/mesa/visualization/backends/matplotlib_backend.html#MatplotlibBackend.draw_agents)
    :   Draw agents on the backend’s axes - optimized version.

        Parameters:
        :   - **arguments** – Dictionary containing agent data arrays.
            - **\*\*kwargs** – Additional keyword arguments for customization.
            - **\*\*kwargs.** (*Checkout respective SpaceDrawer class on details how to pass*) –

        Returns:
        :   The Matplotlib Axes with the agents drawn upon it.

        Return type:
        :   matplotlib.axes.Axes

    draw\_property\_layer(*space*, *property\_layers*, *property\_layer\_portrayal*)[[source]](../_modules/mesa/visualization/backends/matplotlib_backend.html#MatplotlibBackend.draw_property_layer)
    :   Draw property layers using matplotlib backend.

        Parameters:
        :   - **space** – The Mesa space object.
            - **property\_layers** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – Dictionary of property layers to visualize.
            - **property\_layer\_portrayal** (*Callable*) – Function that returns PropertyLayerStyle.

        Returns:
        :   (matplotlib.axes.Axes, colorbar) - The matplotlib axes and colorbar objects.

        Return type:
        :   [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")

Abstract base class for visualization backends in Mesa.

This module provides the foundational interface for implementing various
visualization backends for Mesa agent-based models.

class AbstractRenderer(*space\_drawer*)[[source]](../_modules/mesa/visualization/backends/abstract_renderer.html#AbstractRenderer)
:   Bases: [`ABC`](https://docs.python.org/3/library/abc.html#abc.ABC "(in Python v3.14)")

    Abstract base class for visualization backends.

    This class defines the interface for rendering Mesa spaces and agents.
    For details on the methods checkout specific backend implementations.

    Initialize the renderer.

    Parameters:
    :   - **space\_drawer** – Object responsible for drawing space elements. Checkout SpaceDrawer
        - **functions.** (*for more details on the detailed implementations* *of* *the drawing*)

    abstractmethod initialize\_canvas()[[source]](../_modules/mesa/visualization/backends/abstract_renderer.html#AbstractRenderer.initialize_canvas)
    :   Set up the drawing canvas.

    abstractmethod draw\_structure(*\*\*kwargs*)[[source]](../_modules/mesa/visualization/backends/abstract_renderer.html#AbstractRenderer.draw_structure)
    :   Draw the space structure.

        Parameters:
        :   **\*\*kwargs** – Structure drawing configuration options.

    abstractmethod collect\_agent\_data(*space*, *agent\_portrayal*, *default\_size=None*)[[source]](../_modules/mesa/visualization/backends/abstract_renderer.html#AbstractRenderer.collect_agent_data)
    :   Collect plotting data for all agents in the space.

        Parameters:
        :   - **space** – The Mesa space containing agents.
            - **agent\_portrayal** (*Callable*) – Function that returns AgentPortrayalStyle for each agent.
            - **default\_size** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) – Default marker size if not specified in portrayal.

        Returns:
        :   Dictionary containing agent plotting data arrays with keys:

        Return type:
        :   [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")

    abstractmethod draw\_agents(*arguments*, *\*\*kwargs*)[[source]](../_modules/mesa/visualization/backends/abstract_renderer.html#AbstractRenderer.draw_agents)
    :   Drawing agents on space.

        Parameters:
        :   - **arguments** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – Dictionary containing agent data.
            - **\*\*kwargs** – Additional drawing configuration options.

    abstractmethod draw\_property\_layer(*space*, *property\_layers*, *property\_layer\_portrayal*)[[source]](../_modules/mesa/visualization/backends/abstract_renderer.html#AbstractRenderer.draw_property_layer)
    :   Draw property layers on the visualization.

        Parameters:
        :   - **space** – The model’s space object.
            - **property\_layers** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – Dictionary of property layers to visualize.
            - **property\_layer\_portrayal** (*Callable*) – Function that returns PropertyLayerStyle.

class AltairBackend(*space\_drawer*)[[source]](../_modules/mesa/visualization/backends/altair_backend.html#AltairBackend)
:   Bases: [`AbstractRenderer`](#mesa.visualization.backends.abstract_renderer.AbstractRenderer "mesa.visualization.backends.abstract_renderer.AbstractRenderer")

    Altair-based renderer for Mesa spaces.

    This module provides an Altair-based renderer for visualizing Mesa model spaces,
    agents, and property layers with interactive charting capabilities.

    Initialize the renderer.

    Parameters:
    :   - **space\_drawer** – Object responsible for drawing space elements. Checkout SpaceDrawer
        - **functions.** (*for more details on the detailed implementations* *of* *the drawing*)

    initialize\_canvas() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/visualization/backends/altair_backend.html#AltairBackend.initialize_canvas)
    :   Initialize the Altair canvas.

    draw\_structure(*\*\*kwargs*) → Chart[[source]](../_modules/mesa/visualization/backends/altair_backend.html#AltairBackend.draw_structure)
    :   Draw the space structure using Altair.

        Parameters:
        :   - **\*\*kwargs** – Additional arguments passed to the space drawer.
            - **\*\*kwargs.** (*Checkout respective SpaceDrawer class on details how to pass*) –

        Returns:
        :   The Altair chart representing the space structure.

        Return type:
        :   alt.Chart

    collect\_agent\_data(*space*, *agent\_portrayal: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *default\_size: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/mesa/visualization/backends/altair_backend.html#AltairBackend.collect_agent_data)
    :   Collect plotting data for all agents in the space for Altair.

        Parameters:
        :   - **space** – The Mesa space containing agents.
            - **agent\_portrayal** – Callable that returns AgentPortrayalStyle for each agent.
            - **default\_size** – Default marker size if not specified in portrayal.

        Returns:
        :   Dictionary containing agent plotting data arrays.

        Return type:
        :   [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")

    draw\_agents(*arguments*, *chart\_width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 450*, *chart\_height: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 350*, *\*\*kwargs*)[[source]](../_modules/mesa/visualization/backends/altair_backend.html#AltairBackend.draw_agents)
    :   Draw agents using Altair backend.

        Parameters:
        :   - **arguments** – Dictionary containing agent data arrays.
            - **chart\_width** – Width of the chart.
            - **chart\_height** – Height of the chart.
            - **\*\*kwargs** – Additional keyword arguments for customization.
            - **\*\*kwargs.** (*Checkout respective SpaceDrawer class on details how to pass*) –

        Returns:
        :   The Altair chart representing the agents, or None if no agents.

        Return type:
        :   alt.Chart

    draw\_property\_layer(*space*, *property\_layers: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), ndarray]*, *property\_layer\_portrayal: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *chart\_width: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 450*, *chart\_height: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 350*)[[source]](../_modules/mesa/visualization/backends/altair_backend.html#AltairBackend.draw_property_layer)
    :   Draw property layers using Altair backend.

        Parameters:
        :   - **space** – The Mesa space object containing the property layers.
            - **property\_layers** – A dictionary mapping property\_layer names to numpy arrays.
            - **property\_layer\_portrayal** – A function that returns PropertyLayerStyle
              that contains the visualization parameters.
            - **chart\_width** – The width of the chart.
            - **chart\_height** – The height of the chart.

        Returns:
        :   A tuple containing the base chart and the color bar chart.

        Return type:
        :   alt.Chart

class MatplotlibBackend(*space\_drawer*)[[source]](../_modules/mesa/visualization/backends/matplotlib_backend.html#MatplotlibBackend)
:   Bases: [`AbstractRenderer`](#mesa.visualization.backends.abstract_renderer.AbstractRenderer "mesa.visualization.backends.abstract_renderer.AbstractRenderer")

    Matplotlib-based renderer for Mesa spaces.

    Provides visualization capabilities using Matplotlib for rendering
    space structures, agents, and property layers.

    Initialize the Matplotlib backend.

    Parameters:
    :   **space\_drawer** – An instance of a SpaceDrawer class that handles
        the drawing of the space structure.

    initialize\_canvas(*ax=None*)[[source]](../_modules/mesa/visualization/backends/matplotlib_backend.html#MatplotlibBackend.initialize_canvas)
    :   Initialize the matplotlib canvas.

        Parameters:
        :   **ax** (*matplotlib.axes.Axes**,* *optional*) – Existing axes to use.
            If None, creates new figure and axes.

    draw\_structure(*\*\*kwargs*)[[source]](../_modules/mesa/visualization/backends/matplotlib_backend.html#MatplotlibBackend.draw_structure)
    :   Draw the space structure using matplotlib.

        Parameters:
        :   - **\*\*kwargs** – Additional arguments passed to the space drawer.
            - **\*\*kwargs.** (*Checkout respective SpaceDrawer class on details how to pass*) –

        Returns:
        :   The matplotlib axes with the drawn structure.

    collect\_agent\_data(*space*, *agent\_portrayal*, *default\_size=None*)[[source]](../_modules/mesa/visualization/backends/matplotlib_backend.html#MatplotlibBackend.collect_agent_data)
    :   Collect plotting data for all agents in the space.

        Parameters:
        :   - **space** – The Mesa space containing agents.
            - **agent\_portrayal** (*Callable*) – Function that returns AgentPortrayalStyle for each agent.
            - **default\_size** ([*float*](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*,* *optional*) – Default marker size if not specified in portrayal.

        Returns:
        :   Dictionary containing agent plotting data arrays.

        Return type:
        :   [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")

    draw\_agents(*arguments*, *\*\*kwargs*)[[source]](../_modules/mesa/visualization/backends/matplotlib_backend.html#MatplotlibBackend.draw_agents)
    :   Draw agents on the backend’s axes - optimized version.

        Parameters:
        :   - **arguments** – Dictionary containing agent data arrays.
            - **\*\*kwargs** – Additional keyword arguments for customization.
            - **\*\*kwargs.** (*Checkout respective SpaceDrawer class on details how to pass*) –

        Returns:
        :   The Matplotlib Axes with the agents drawn upon it.

        Return type:
        :   matplotlib.axes.Axes

    draw\_property\_layer(*space*, *property\_layers*, *property\_layer\_portrayal*)[[source]](../_modules/mesa/visualization/backends/matplotlib_backend.html#MatplotlibBackend.draw_property_layer)
    :   Draw property layers using matplotlib backend.

        Parameters:
        :   - **space** – The Mesa space object.
            - **property\_layers** ([*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")) – Dictionary of property layers to visualize.
            - **property\_layer\_portrayal** (*Callable*) – Function that returns PropertyLayerStyle.

        Returns:
        :   (matplotlib.axes.Axes, colorbar) - The matplotlib axes and colorbar objects.

        Return type:
        :   [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")

## Space Renderer

Space rendering module for Mesa visualizations.

This module provides functionality to render Mesa model spaces with different
backends, supporting various space types and visualization components.

class SpaceRenderer(*model: [Model](../mesa.html#mesa.model.Model "mesa.model.Model")*, *backend: [Literal](https://docs.python.org/3/library/typing.html#typing.Literal "(in Python v3.14)")['matplotlib', 'altair'] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 'matplotlib'*)[[source]](../_modules/mesa/visualization/space_renderer.html#SpaceRenderer)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

    Renders Mesa spaces using different visualization backends.

    Supports multiple space types and backends for flexible visualization
    of agent-based models.

    Initialize the space renderer.

    Parameters:
    :   - **model** ([*mesa.Model*](../mesa.html#mesa.Model "mesa.Model")) – The Mesa model to render.
        - **backend** (*Literal**[**"matplotlib"**,* *"altair"**]* *|* *None*) – The visualization backend to use.

    setup\_structure(*\*\*kwargs*) → [SpaceRenderer](#mesa.visualization.space_renderer.SpaceRenderer "mesa.visualization.space_renderer.SpaceRenderer")[[source]](../_modules/mesa/visualization/space_renderer.html#SpaceRenderer.setup_structure)
    :   Setup the space structure without drawing.

        Parameters:
        :   - **\*\*kwargs** – Additional keyword arguments for the setup function. For ContinuousSpace,
              you may pass `viz_dims=(i, j)` to select which two dimensions are projected
              to x/y.
            - **\*\*kwargs.** (*Checkout respective SpaceDrawer class on details how to pass*) –

        Returns:
        :   The current instance for method chaining.

        Return type:
        :   [SpaceRenderer](#mesa.visualization.space_renderer.SpaceRenderer "mesa.visualization.space_renderer.SpaceRenderer")

    setup\_agents(*agent\_portrayal: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")*, *\*\*kwargs*) → [SpaceRenderer](#mesa.visualization.space_renderer.SpaceRenderer "mesa.visualization.space_renderer.SpaceRenderer")[[source]](../_modules/mesa/visualization/space_renderer.html#SpaceRenderer.setup_agents)
    :   Setup agents on the space without drawing.

        Parameters:
        :   - **agent\_portrayal** (*Callable*) – Function that takes an agent and returns AgentPortrayalStyle.
            - **\*\*kwargs** – Additional keyword arguments for the setup function.
            - **\*\*kwargs.** (*Checkout respective SpaceDrawer class on details how to pass*) –

        Returns:
        :   The current instance for method chaining.

        Return type:
        :   [SpaceRenderer](#mesa.visualization.space_renderer.SpaceRenderer "mesa.visualization.space_renderer.SpaceRenderer")

    setup\_property\_layer(*property\_layer\_portrayal: Callable | [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") | [PropertyLayerStyle](#mesa.visualization.components.__init__.PropertyLayerStyle "mesa.visualization.components.__init__.PropertyLayerStyle")*) → [SpaceRenderer](#mesa.visualization.space_renderer.SpaceRenderer "mesa.visualization.space_renderer.SpaceRenderer")[[source]](../_modules/mesa/visualization/space_renderer.html#SpaceRenderer.setup_property_layer)
    :   Setup property layers on the space without drawing.

        Parameters:
        :   **property\_layer\_portrayal** (*Callable* *|* [*dict*](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)") *|* [*PropertyLayerStyle*](#mesa.visualization.components.__init__.PropertyLayerStyle "mesa.visualization.components.__init__.PropertyLayerStyle")) – A PropertyLayerStyle,
            a function that produces a PropertyLayerStyle instance, or a dictionary specifying portrayal parameters.

        Returns:
        :   The current instance for method chaining.

        Return type:
        :   [SpaceRenderer](#mesa.visualization.space_renderer.SpaceRenderer "mesa.visualization.space_renderer.SpaceRenderer")

    draw\_structure(*\*\*kwargs*)[[source]](../_modules/mesa/visualization/space_renderer.html#SpaceRenderer.draw_structure)
    :   Draw the space structure.

        Parameters:
        :   **\*\*kwargs** – (Deprecated) Additional keyword arguments for drawing.
            Use setup\_structure() instead.

        Returns:
        :   The visual representation of the space structure.

    draw\_agents(*agent\_portrayal=None*, *\*\*kwargs*)[[source]](../_modules/mesa/visualization/space_renderer.html#SpaceRenderer.draw_agents)
    :   Draw agents on the space.

        Parameters:
        :   - **agent\_portrayal** – (Deprecated) Function that takes an agent and returns AgentPortrayalStyle.
              Use setup\_agents() instead.
            - **\*\*kwargs** – (Deprecated) Additional keyword arguments for drawing.

        Returns:
        :   The visual representation of the agents.

    draw\_property\_layer(*property\_layer\_portrayal=None*)[[source]](../_modules/mesa/visualization/space_renderer.html#SpaceRenderer.draw_property_layer)
    :   Draw property layers on the space.

        Parameters:
        :   - **property\_layer\_portrayal** – (Deprecated) A PropertyLayerStyle, a function that produces
            - **instance** (*a PropertyLayerStyle*)
            - **parameters.** (*or a dictionary specifying portrayal*)
            - **instead.** (*Use setup\_property\_layer**(**)*)

        Returns:
        :   The visual representation of the property layers.

        Raises:
        :   [**Exception**](https://docs.python.org/3/library/exceptions.html#Exception "(in Python v3.14)") – If no property layers are found on the space.

    render(*agent\_portrayal=None*, *property\_layer\_portrayal=None*, *\*\*kwargs*)[[source]](../_modules/mesa/visualization/space_renderer.html#SpaceRenderer.render)
    :   Render the complete space with structure, agents, and property layers.

        Parameters:
        :   - **agent\_portrayal** – (Deprecated) Function for agent portrayal. Use setup\_agents() instead.
            - **property\_layer\_portrayal** – (Deprecated) Function for property layer portrayal. Use setup\_property\_layer() instead.
            - **\*\*kwargs** – (Deprecated) Additional keyword arguments.

    property canvas
    :   Get the current canvas object.

        Returns:
        :   The backend-specific canvas object.

    property post\_process
    :   Get the current post-processing function.

        Returns:
        :   The post-processing function, or None if not set.

        Return type:
        :   Callable | None

## Space Drawers

Mesa visualization space drawers.

This module provides the core logic for drawing spaces in Mesa, supporting
orthogonal grids, hexagonal grids, networks, continuous spaces, and Voronoi grids.
It includes implementations for both Matplotlib and Altair backends.

class BaseSpaceDrawer(*space*)[[source]](../_modules/mesa/visualization/space_drawers.html#BaseSpaceDrawer)
:   Bases: [`object`](https://docs.python.org/3/library/functions.html#object "(in Python v3.14)")

    Base class for all space drawers.

    Initialize the base space drawer.

    Parameters:
    :   **space** – Grid/Space type to draw.

    get\_viz\_limits()[[source]](../_modules/mesa/visualization/space_drawers.html#BaseSpaceDrawer.get_viz_limits)
    :   Get visualization limits for the space.

        Returns:
        :   A tuple of (xmin, xmax, ymin, ymax) for visualization limits.

class OrthogonalSpaceDrawer(*space: [OrthogonalMooreGrid](discrete_space.html#mesa.discrete_space.grid.OrthogonalMooreGrid "mesa.discrete_space.grid.OrthogonalMooreGrid") | [OrthogonalVonNeumannGrid](discrete_space.html#mesa.discrete_space.grid.OrthogonalVonNeumannGrid "mesa.discrete_space.grid.OrthogonalVonNeumannGrid")*)[[source]](../_modules/mesa/visualization/space_drawers.html#OrthogonalSpaceDrawer)
:   Bases: [`BaseSpaceDrawer`](#mesa.visualization.space_drawers.BaseSpaceDrawer "mesa.visualization.space_drawers.BaseSpaceDrawer")

    Drawer for orthogonal grid spaces (SingleGrid, MultiGrid, Moore, VonNeumann).

    Initialize the orthogonal space drawer.

    Parameters:
    :   **space** – The orthogonal grid space to draw

    draw\_matplotlib(*ax=None*, *\*\*draw\_space\_kwargs*)[[source]](../_modules/mesa/visualization/space_drawers.html#OrthogonalSpaceDrawer.draw_matplotlib)
    :   Draw the orthogonal grid using matplotlib.

        Parameters:
        :   - **ax** – Matplotlib axes object to draw on
            - **\*\*draw\_space\_kwargs** – Additional keyword arguments for styling.

        Examples

        figsize=(10, 10), color=”blue”, linewidth=2.

        Returns:
        :   The modified axes object

    draw\_altair(*chart\_width=450*, *chart\_height=350*, *\*\*draw\_chart\_kwargs*)[[source]](../_modules/mesa/visualization/space_drawers.html#OrthogonalSpaceDrawer.draw_altair)
    :   Draw the orthogonal grid using Altair.

        Parameters:
        :   - **chart\_width** – Width for the shown chart
            - **chart\_height** – Height for the shown chart
            - **\*\*draw\_chart\_kwargs** – Additional keyword arguments for styling the chart.

        Examples

        width=500, height=500, title=”Grid”.

        Returns:
        :   Altair chart object

class HexSpaceDrawer(*space: [HexGrid](discrete_space.html#mesa.discrete_space.grid.HexGrid "mesa.discrete_space.grid.HexGrid")*)[[source]](../_modules/mesa/visualization/space_drawers.html#HexSpaceDrawer)
:   Bases: [`BaseSpaceDrawer`](#mesa.visualization.space_drawers.BaseSpaceDrawer "mesa.visualization.space_drawers.BaseSpaceDrawer")

    Drawer for hexagonal grid spaces.

    Initialize the hexagonal space drawer.

    Parameters:
    :   **space** – The hexagonal grid space to draw

    draw\_matplotlib(*ax=None*, *\*\*draw\_space\_kwargs*)[[source]](../_modules/mesa/visualization/space_drawers.html#HexSpaceDrawer.draw_matplotlib)
    :   Draw the hexagonal grid using matplotlib.

        Parameters:
        :   - **ax** – Matplotlib axes object to draw on
            - **\*\*draw\_space\_kwargs** – Additional keyword arguments for styling.

        Examples

        figsize=(8, 8), color=”red”, alpha=0.5.

        Returns:
        :   The modified axes object

    draw\_altair(*chart\_width=450*, *chart\_height=350*, *\*\*draw\_chart\_kwargs*)[[source]](../_modules/mesa/visualization/space_drawers.html#HexSpaceDrawer.draw_altair)
    :   Draw the hexagonal grid using Altair.

        Parameters:
        :   - **chart\_width** – Width for the shown chart
            - **chart\_height** – Height for the shown chart
            - **\*\*draw\_chart\_kwargs** – Additional keyword arguments for styling the chart.

        Examples

        - Line properties like color, strokeDash, strokeWidth, opacity.
        - Other kwargs (e.g., width, title) apply to the chart.

        Returns:
        :   Altair chart object representing the hexagonal grid.

class NetworkSpaceDrawer(*space: [Network](discrete_space.html#mesa.discrete_space.network.Network "mesa.discrete_space.network.Network")*, *layout\_alg=<function spring\_layout>*, *layout\_kwargs=None*)[[source]](../_modules/mesa/visualization/space_drawers.html#NetworkSpaceDrawer)
:   Bases: [`BaseSpaceDrawer`](#mesa.visualization.space_drawers.BaseSpaceDrawer "mesa.visualization.space_drawers.BaseSpaceDrawer")

    Drawer for network-based spaces.

    Initialize the network space drawer.

    Parameters:
    :   - **space** – The network space to draw
        - **layout\_alg** – NetworkX layout algorithm to use
        - **layout\_kwargs** – Keyword arguments for the layout algorithm

    draw\_matplotlib(*ax=None*, *\*\*draw\_space\_kwargs*)[[source]](../_modules/mesa/visualization/space_drawers.html#NetworkSpaceDrawer.draw_matplotlib)
    :   Draw the network using matplotlib.

        Parameters:
        :   - **ax** – Matplotlib axes object to draw on.
            - **\*\*draw\_space\_kwargs** – Dictionaries of keyword arguments for styling.
              Can also handle zorder for both nodes and edges if passed.
              \* `node_kwargs`: A dict passed to nx.draw\_networkx\_nodes.
              \* `edge_kwargs`: A dict passed to nx.draw\_networkx\_edges.

        Returns:
        :   The modified axes object.

    draw\_altair(*chart\_width=450*, *chart\_height=350*, *\*\*draw\_chart\_kwargs*)[[source]](../_modules/mesa/visualization/space_drawers.html#NetworkSpaceDrawer.draw_altair)
    :   Draw the network using Altair.

        Parameters:
        :   - **chart\_width** – Width for the shown chart
            - **chart\_height** – Height for the shown chart
            - **\*\*draw\_chart\_kwargs** – Dictionaries for styling the chart.
              \* `node_kwargs`: A dict of properties for the node’s mark\_point.
              \* `edge_kwargs`: A dict of properties for the edge’s mark\_rule.
              \* Other kwargs (e.g., title, width) are passed to chart.properties().

        Returns:
        :   Altair chart object representing the network.

class ContinuousSpaceDrawer(*space: ContinuousSpace*, *viz\_dims: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] = (0, 1)*)[[source]](../_modules/mesa/visualization/space_drawers.html#ContinuousSpaceDrawer)
:   Bases: [`BaseSpaceDrawer`](#mesa.visualization.space_drawers.BaseSpaceDrawer "mesa.visualization.space_drawers.BaseSpaceDrawer")

    Drawer for continuous spaces.

    Initialize the continuous space drawer.

    Parameters:
    :   - **space** – The continuous space to draw.
        - **viz\_dims** – The pair of dimension indices to project onto the x and y axes.

    Raises:
    :   - [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If the space has fewer than two dimensions.
        - [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If viz\_dims does not contain exactly two distinct valid indices.

    set\_viz\_dims(*viz\_dims: [tuple](https://docs.python.org/3/library/stdtypes.html#tuple "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)"), [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/visualization/space_drawers.html#ContinuousSpaceDrawer.set_viz_dims)
    :   Set which dimensions are visualized on the x and y axes.

        Parameters:
        :   **viz\_dims** – Tuple of two distinct dimension indices.

        Raises:
        :   [**ValueError**](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") – If viz\_dims is invalid for the underlying space.

    project(*position*)[[source]](../_modules/mesa/visualization/space_drawers.html#ContinuousSpaceDrawer.project)
    :   Project an n-dimensional position onto the configured 2D plane.

    draw\_matplotlib(*ax=None*, *\*\*draw\_space\_kwargs*)[[source]](../_modules/mesa/visualization/space_drawers.html#ContinuousSpaceDrawer.draw_matplotlib)
    :   Draw the continuous space using matplotlib.

        Parameters:
        :   - **ax** – Matplotlib axes object to draw on.
            - **\*\*draw\_space\_kwargs** – Keyword arguments for styling the axis frame. You may
              optionally pass `viz_dims=(i, j)` to select which two dimensions of an
              n-dimensional space are projected to x/y.

        Examples

        linewidth=3, color=”green”

        Returns:
        :   The modified axes object.

    draw\_altair(*chart\_width=450*, *chart\_height=350*, *\*\*draw\_chart\_kwargs*)[[source]](../_modules/mesa/visualization/space_drawers.html#ContinuousSpaceDrawer.draw_altair)
    :   Draw the continuous space using Altair.

        Parameters:
        :   - **chart\_width** – Width for the shown chart.
            - **chart\_height** – Height for the shown chart.
            - **\*\*draw\_chart\_kwargs** – Keyword arguments for styling the chart’s view properties.
              You may optionally pass `viz_dims=(i, j)` to select which two dimensions of an
              n-dimensional space are projected to x/y.

        Returns:
        :   An Altair Chart object representing the space.

class VoronoiSpaceDrawer(*space: [VoronoiGrid](discrete_space.html#mesa.discrete_space.voronoi.VoronoiGrid "mesa.discrete_space.voronoi.VoronoiGrid")*)[[source]](../_modules/mesa/visualization/space_drawers.html#VoronoiSpaceDrawer)
:   Bases: [`BaseSpaceDrawer`](#mesa.visualization.space_drawers.BaseSpaceDrawer "mesa.visualization.space_drawers.BaseSpaceDrawer")

    Drawer for Voronoi diagram spaces.

    Initialize the Voronoi space drawer.

    Parameters:
    :   **space** – The Voronoi grid space to draw

    draw\_matplotlib(*ax=None*, *\*\*draw\_space\_kwargs*)[[source]](../_modules/mesa/visualization/space_drawers.html#VoronoiSpaceDrawer.draw_matplotlib)
    :   Draw the Voronoi diagram using matplotlib.

        Parameters:
        :   - **ax** – Matplotlib axes object to draw on
            - **\*\*draw\_space\_kwargs** – Keyword arguments passed to matplotlib’s LineCollection.

        Examples

        lw=2, alpha=0.5, colors=’red’

        Returns:
        :   The modified axes object

    draw\_altair(*chart\_width=450*, *chart\_height=350*, *\*\*draw\_chart\_kwargs*)[[source]](../_modules/mesa/visualization/space_drawers.html#VoronoiSpaceDrawer.draw_altair)
    :   Draw the Voronoi diagram using Altair.

        Parameters:
        :   - **chart\_width** – Width for the shown chart
            - **chart\_height** – Height for the shown chart
            - **\*\*draw\_chart\_kwargs** – Additional keyword arguments for styling the chart.

        Examples

        - Line properties like color, strokeDash, strokeWidth, opacity.
        - Other kwargs (e.g., width, title) apply to the chart.

        Returns:
        :   An Altair Chart object representing the Voronoi diagram.

On this page

[Show Source](../_sources/apis/visualization.md.txt)

---

Original source: https://mesa.readthedocs.io/latest/apis/visualization.html
