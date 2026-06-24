---
title: "callbacks"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/callbacks.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `callbacks`

Abstract base class for a callback and a default implementation.

If you want to store the data in a way that is different from the
functionality provided by the default callback, you can write your own
extension of callback. For example, you can easily implement a callback
that stores the data in e.g. a NoSQL file.

The only method to implement is the \_\_call\_\_ magic method. To use logging of
progress, always call super.

class ema\_workbench.em\_framework.callbacks.AbstractCallback(*uncertainties: list[[Parameter](parameters.html#ema_workbench.em_framework.parameters.Parameter "ema_workbench.em_framework.parameters.Parameter")]*, *levers: list[[Parameter](parameters.html#ema_workbench.em_framework.parameters.Parameter "ema_workbench.em_framework.parameters.Parameter")]*, *outcomes: list[[Outcome](outcomes.html#ema_workbench.em_framework.outcomes.Outcome "ema_workbench.em_framework.outcomes.Outcome")]*, *nr\_experiments: int*, *reporting\_interval: int | None = None*, *reporting\_frequency: int = 10*, *log\_progress: bool = False*)
:   Abstract base class from which different call back classes can be derived.

    Callback is responsible for storing the results of the runs.

    Parameters:
    :   - **uncertainties** (*list*) – list of uncertain parameters
        - **levers** (*list*) – list of lever parameters
        - **outcomes** (*list*) – a list of outcomes
        - **nr\_experiments** (*int*) – the total number of experiments to be executed
        - **reporting\_interval** (*int**,* *optional*) – the interval between progress logs
        - **reporting\_frequency** (*int**,* *optional*) – the total number of progress logs
        - **log\_progress** (*bool**,* *optional*) – if true, progress is logged, if false, use
          tqdm progress bar.

    i
    :   a counter that keeps track of how many experiments have been
        saved

        Type:
        :   int

    nr\_experiments
    :   Type:
        :   int

    outcomes
    :   Type:
        :   list

    parameters
    :   combined list of uncertain parameters and lever parameters

        Type:
        :   list

    reporting\_interval
    :   the interval between progress logs

        Type:
        :   int,

    abstractmethod get\_results() → Any
    :   Method for retrieving the results.

        Called after all experiments have been completed. Any extension of AbstractCallback needs to
        implement this method.

class ema\_workbench.em\_framework.callbacks.DefaultCallback(*uncertainties: list[[Parameter](parameters.html#ema_workbench.em_framework.parameters.Parameter "ema_workbench.em_framework.parameters.Parameter")]*, *levers: list[[Parameter](parameters.html#ema_workbench.em_framework.parameters.Parameter "ema_workbench.em_framework.parameters.Parameter")]*, *outcomes: list[[Outcome](outcomes.html#ema_workbench.em_framework.outcomes.Outcome "ema_workbench.em_framework.outcomes.Outcome")]*, *nr\_experiments: int*, *reporting\_interval: int = 100*, *reporting\_frequency: int = 10*, *log\_progress: bool = False*)
:   Default callback class.

    Parameters:
    :   - **uncertainties** (*list*) – list of uncertain parameters
        - **levers** (*list*) – list of lever parameters
        - **outcomes** (*list*) – a list of outcomes
        - **nr\_experiments** (*int*) – the total number of experiments to be executed
        - **reporting\_interval** (*int**,* *optional*) – the interval between progress logs
        - **reporting\_frequency** (*int**,* *optional*) – the total number of progress logs
        - **log\_progress** (*bool**,* *optional*) – if true, progress is logged, if false, use
          tqdm progress bar.

    Callback can be used in perform\_experiments as a means for
    specifying the way in which the results should be handled. If no
    callback is specified, this default implementation is used. This
    one can be overwritten or replaced with a callback of your own
    design. For example if you prefer to store the result in a database
    or write them to a text file.

    get\_results() → tuple[DataFrame, dict[str, ndarray]]
    :   Return the experiments and their results.

class ema\_workbench.em\_framework.callbacks.FileBasedCallback(*uncertainties: list[[Parameter](parameters.html#ema_workbench.em_framework.parameters.Parameter "ema_workbench.em_framework.parameters.Parameter")]*, *levers: list[[Parameter](parameters.html#ema_workbench.em_framework.parameters.Parameter "ema_workbench.em_framework.parameters.Parameter")]*, *outcomes: list[[Outcome](outcomes.html#ema_workbench.em_framework.outcomes.Outcome "ema_workbench.em_framework.outcomes.Outcome")]*, *nr\_experiments: int*, *reporting\_interval: int = 100*, *reporting\_frequency: int = 10*)
:   Callback that stores data in csv files while running th model.

    Parameters:
    :   - **uncertainties** (*list*) – list of uncertain parameters
        - **levers** (*list*) – list of lever parameters
        - **outcomes** (*list*) – a list of outcomes
        - **nr\_experiments** (*int*) – the total number of experiments to be executed
        - **reporting\_interval** (*int**,* *optional*) – the interval between progress logs
        - **reporting\_frequency** (*int**,* *optional*) – the total number of progress logs
        - **log\_progress** (*bool**,* *optional*) – if true, progress is logged, if false, use
          tqdm progress bar.

    This class is still in beta.
    the data is stored in ./temp, relative to the current
    working directory. If this directory already exists, it will be
    overwritten.

    get\_results()
    :   Return the experiments and their results.

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/callbacks.html
