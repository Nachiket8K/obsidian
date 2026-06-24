---
title: "model"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/model.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `model`

A collection of classes for interfacing with simulation models.

Any model that is to be controlled from the workbench is controlled via
an instance of an extension of this abstract base class.

class ema\_workbench.em\_framework.model.AbstractModel(*name: str*)
:   Abstract base class for models.

    This is an abstract base class
    and cannot be used directly.

    uncertainties
    :   list of parameter instances

        Type:
        :   list

    levers
    :   list of parameter instances

        Type:
        :   list

    outcomes
    :   list of outcome instances

        Type:
        :   list

    name
    :   alphanumerical name of model structure interface

        Type:
        :   str

    output
    :   this should be a dict with the names of the outcomes as
        key

        Type:
        :   dict

    When extending this class :meth:`model\_init` and

    :meth:`run\_model` have to be implemented.

    as\_dict()
    :   Return a dict representation of the model.

    cleanup()
    :   Perform any cleanup after all experiments have completed.

        This model is called after finishing all the experiments, but
        just prior to returning the results. This method gives a hook for
        doing any cleanup, such as closing applications.

        In case of running in parallel, this method is called during
        the cleanup of the pool, just prior to removing the temporary
        directories.

    initialized(*policy: [Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")*) → bool
    :   Check if model has been initialized.

        Parameters:
        :   **policy** (*a Sample instance*)

    model\_init(*policy: [Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")*)
    :   Initialize the model.

        Parameters:
        :   **policy** (*dict*) – policy to be run.

    property outcomes\_output: dict
    :   Getter for outcomes output.

    property output\_variables: list[str]
    :   Getter for output variables.

    reset\_model()
    :   Reset the model.

        The default implementation only sets the outputs to an empty dict.

    run\_model(*scenario: [Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")*, *policy: [Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")*, *constants: [Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")*) → None
    :   Run the model for the specified scenario, policy, and constants.

        Parameters:
        :   - **scenario** (*Sample instance*)
            - **policy** (*Sample instance*)
            - **constants** (*Sample instance*)

class ema\_workbench.em\_framework.model.FileModel(*name*, *wd: str | None = None*, *model\_file: str | None = None*)
:   Base class for a model that uses underlying files.

    as\_dict() → dict
    :   Return a dict representation of the model.

    property working\_directory: str
    :   Getter for working directory.

class ema\_workbench.em\_framework.model.Model(*name: str*, *function: Callable | None = None*)
:   Default model class for python callables that are run once per experiment.

class ema\_workbench.em\_framework.model.Replicator(*name: str*)
:   Base class for a model where experiments are run for multiple replications.

    property replications
    :   Getter for replications.

    run\_model(*scenario: [Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")*, *policy: [Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")*, *constants: [Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")*) → None
    :   Run the model for the specified scenario, policy, and constants.

        Parameters:
        :   - **scenario** (*Sample instance*)
            - **policy** (*Sample instance*)
            - **constants** (*Sample instance*)

class ema\_workbench.em\_framework.model.ReplicatorModel(*name: str*, *function: Callable | None = None*)
:   Default model class for python callables that are run for multiple replications per experiment.

class ema\_workbench.em\_framework.model.SingleReplication(*name: str*)
:   Base class for models that require only a single replication.

    run\_model(*scenario: [Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")*, *policy: [Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")*, *constants: [Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")*) → None
    :   Run the model for the specified scenario, policy, and constants.

        Parameters:
        :   - **scenario** (*Sample instance*)
            - **policy** (*Sample instance*)
            - **constants** (*Sample instance*)

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/model.html
