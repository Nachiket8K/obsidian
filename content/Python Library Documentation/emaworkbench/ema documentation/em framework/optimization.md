---
title: "optimization"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/optimization.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `optimization`

Wrapper around platypus-opt.

class ema\_workbench.em\_framework.optimization.GenerationalBorg(*problem: ~ema\_workbench.em\_framework.optimization.Problem, epsilons: list[float], population\_size: int = 100, generator: ~platypus.core.Generator = <platypus.operators.RandomGenerator object>, selector: ~platypus.core.Selector = <platypus.operators.TournamentSelector object>, \*\*kwargs*)
:   A generational implementation of the BORG Framework.

    This algorithm adopts Epsilon Progress Continuation, and Auto Adaptive
    Operator Selection, but embeds them within the NSGAII generational
    algorithm, rather than the steady state implementation used by the BORG
    algorithm.

    The parametrization of all operators is based on the default values as used
    in Borg 1.9.

    Note:: limited to RealParameters only.

class ema\_workbench.em\_framework.optimization.Problem(*searchover: Literal['levers', 'uncertainties', 'robust']*, *decision\_variables: ParameterMap | list[[Parameter](parameters.html#ema_workbench.em_framework.parameters.Parameter "ema_workbench.em_framework.parameters.Parameter")]*, *objectives: list[[ScalarOutcome](outcomes.html#ema_workbench.em_framework.outcomes.ScalarOutcome "ema_workbench.em_framework.outcomes.ScalarOutcome")]*, *constraints: list[[Constraint](outcomes.html#ema_workbench.em_framework.outcomes.Constraint "ema_workbench.em_framework.outcomes.Constraint")] | None = None*, *reference: [Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample") | Iterable[[Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")] | int | None = None*)
:   Small extension to Platypus problem object.

    Includes the decision variables, outcomes, and constraints,
    any reference Sample(s), and the type of search.

    property constraint\_names: list[str]
    :   Getter for constraint names.

    property outcome\_names: list[str]
    :   Getter for outcome names.

    property parameter\_names: list[str]
    :   Getter for parameter names.

ema\_workbench.em\_framework.optimization.epsilon\_nondominated(*results: list[DataFrame]*, *epsilons: list[float]*, *problem: [Problem](#ema_workbench.em_framework.optimization.Problem "ema_workbench.em_framework.optimization.Problem")*) → DataFrame
:   Merge the list of results into a single set of non dominated results using the provided epsilon values.

    Parameters:
    :   - **results** (*list* *of* *DataFrames*)
        - **epsilons** (*epsilon values for each objective*)
        - **problem** (*PlatypusProblem instance*)

    Return type:
    :   DataFrame

    Notes

    this is a platypus based alternative to pareto.py (<https://github.com/matthewjwoodruff/pareto.py>)

ema\_workbench.em\_framework.optimization.load\_archives(*path\_to\_file: str*) → list[tuple[int, DataFrame]]
:   Returns a list of stored archives.

    Each entry in the list is a tuple. The first element is the number of
    nfe, the second is the archive at that number of nfe.

    Parameters:
    :   **path\_to\_file** (*the path to the archive*)

ema\_workbench.em\_framework.optimization.rebuild\_platypus\_population(*archive: DataFrame*, *problem: [Problem](#ema_workbench.em_framework.optimization.Problem "ema_workbench.em_framework.optimization.Problem")*) → list[Solution]
:   Rebuild a population of platypus Solution instances.

    Parameters:
    :   - **archive** (*DataFrame*)
        - **problem** (*PlatypusProblem instance*)

    Return type:
    :   list of platypus Solutions

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/optimization.html
