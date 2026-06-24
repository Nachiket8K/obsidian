---
title: "points"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/points.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `points`

Classes for representing points in parameter space.

As well as associated helper functions

class ema\_workbench.em\_framework.points.Experiment(*name: str*, *model\_name: str*, *policy: [Sample](#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")*, *scenario: [Sample](#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")*, *experiment\_id: int*)
:   A convenience object that contains a specification of the model, policy, and scenario to run.

    name
    :   Type:
        :   str

    model\_name
    :   Type:
        :   str

    policy
    :   Type:
        :   Sample instance

    scenario
    :   Type:
        :   Sample instance

    experiment\_id
    :   Type:
        :   int

class ema\_workbench.em\_framework.points.ExperimentReplication(*scenario*, *policy*, *constants*, *replication=None*)
:   Helper class that combines scenario, policy, any constants, and replication information.

    This class represent the complete specification of parameters to run for
    a given experiment.

class ema\_workbench.em\_framework.points.Sample(*name=None*, *unique\_id=None*, *\*\*kwargs*)
:   A point in parameter space.

class ema\_workbench.em\_framework.points.SampleCollection(*samples: ndarray*, *parameters: ParameterMap | Iterable[[Parameter](parameters.html#ema_workbench.em_framework.parameters.Parameter "ema_workbench.em_framework.parameters.Parameter")]*)
:   Collection of sample instances.

    A Sample is a point in a parameter space.

    combine(*other: [SampleCollection](#ema_workbench.em_framework.points.SampleCollection "ema_workbench.em_framework.points.SampleCollection")*, *how: Literal['full\_factorial', 'sample', 'cycle']*, *rng: NumpySeedLike | RNGLike | None = None*) → [SampleCollection](#ema_workbench.em_framework.points.SampleCollection "ema_workbench.em_framework.points.SampleCollection")
    :   Combine two SampleCollections into a new SampleCollection.

        Use this if you have two sets of samples for different parameters that
        you want to combine into a bigger set of samples across the combined set
        of parameters.

        If you want to simple combine two sets of samples for the same parameters,
        use concat instead.

        Parameters:
        :   - **other** (*the SampleCollection to combine with this one*)
            - **how** (*how to combine the designs.*)
            - **rng** (*RNG* *or* *None**,* *only relevant in case combine is "sample"*)

        Return type:
        :   a new SampleCollection instance

        Raises:
        :   **ValueError if one** **or** **more parameters with the same name are present in both collections** –

    concat(*other: [SampleCollection](#ema_workbench.em_framework.points.SampleCollection "ema_workbench.em_framework.points.SampleCollection")*) → [SampleCollection](#ema_workbench.em_framework.points.SampleCollection "ema_workbench.em_framework.points.SampleCollection")
    :   Concatenate two SampleCollections.

        Parameters:
        :   **other** (*the SampleCollection to combine with this one*)

        Return type:
        :   a new SampleCollection instance

        Raises:
        :   **ValueError if one** **or** **more parameters are present in only one** **of** **the two SampleCollections.** –

    property shape: tuple[int, int]
    :   Shape of the samples.

ema\_workbench.em\_framework.points.experiment\_generator(*models: Iterable[[AbstractModel](model.html#ema_workbench.em_framework.model.AbstractModel "ema_workbench.em_framework.model.AbstractModel")]*, *scenarios: Iterable[[Sample](#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")]*, *policies: Iterable[[Sample](#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")]*, *combine: Literal['full\_factorial', 'sample', 'cycle'] = 'full\_factorial'*, *rng: NumpySeedLike | RNGLike | None = None*) → Generator[[Experiment](#ema_workbench.em_framework.points.Experiment "ema_workbench.em_framework.points.Experiment")]
:   Generator function which yields experiments.

    Parameters:
    :   - **models** (*list*)
        - **scenarios** (*iterable* *of* *scenarios*)
        - **policies** (*iterable* *of* *policies*)
        - **{'full\_factorial** (*combine =*) – controls how to combine scenarios, policies, and models
          into experiments.
        - **sample'** – controls how to combine scenarios, policies, and models
          into experiments.
        - **"cycle"}** – controls how to combine scenarios, policies, and models
          into experiments.
        - **rng** (*a numpy random number generator**, or* *a value to seed a generator.*)

    Notes

    if combine is full\_factorial’ then this generator is essentially three nested
    loops: for each model, for each policy, for each scenario,
    return the experiment. This means that scenarios should not be a generator
    because this will be exhausted after the running the first policy on the
    first model.
    if combine is ‘cycle’ then this generator cycles over scenarios, policies
    and models until the longest of the three collections is
    exhausted.

ema\_workbench.em\_framework.points.from\_experiments(*experiments: DataFrame*, *drop\_defaults: bool = True*) → list[[Sample](#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")]
:   Generate scenarios from an existing experiments DataFrame.

    This function takes a pandas DataFrame and turns it into a list of Sample instances.
    There is no further processing done, so it is up to the user to ensure that the columsn in the
    dataframe map to parameters in the model.

    Parameters:
    :   - **experiments** (*DataFrame*)
        - **drop\_defaults** (*bool*) – By default, an experiments dataframe as returned by the workbench after performing experiments contains
          a ‘model’, ‘scenario’ and ‘policy’ column. If drop\_defaults is True, these columns are automatically ignored.

    Return type:
    :   list of Sample instances

ema\_workbench.em\_framework.points.sample\_generator(*samples: ndarray*, *params: Iterable[[Parameter](parameters.html#ema_workbench.em_framework.parameters.Parameter "ema_workbench.em_framework.parameters.Parameter")]*) → Generator[[Sample](#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")]
:   Return a generator yielding points instances.

    This generator iterates over the samples, and turns each row into a Sample and ensures datatypes are correctly handled.

    Parameters:
    :   - **samples** (*The samples taken for the parameters*)
        - **params** (*the Parameter instances that have been sampled*)

    Yields:
    :   *Sample*

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/points.html
