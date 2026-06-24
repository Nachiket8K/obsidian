---
title: "evaluators"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/evaluators.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `evaluators`

collection of evaluators for performing experiments, optimization, and robust optimization.

class ema\_workbench.em\_framework.evaluators.BaseEvaluator(*msis: [AbstractModel](model.html#ema_workbench.em_framework.model.AbstractModel "ema_workbench.em_framework.model.AbstractModel") | list[[AbstractModel](model.html#ema_workbench.em_framework.model.AbstractModel "ema_workbench.em_framework.model.AbstractModel")]*)
:   evaluator for experiments using a multiprocessing pool.

    Parameters:
    :   **msis** (*collection* *of* [*models*](../analysis/logistic_regression.html#ema_workbench.analysis.logistic_regression.Logit.models "ema_workbench.analysis.logistic_regression.Logit.models"))

    Raises:
    :   **ValueError** –

    evaluate\_all(*jobs: list[EvaluateSolution]*, *\*\*kwargs*)
    :   Makes ema\_workbench evaluators compatible with platypus evaluators.

    abstractmethod evaluate\_experiments(*experiments: Iterable[[Experiment](points.html#ema_workbench.em_framework.points.Experiment "ema_workbench.em_framework.points.Experiment")]*, *callback: Callable*, *\*\*kwargs*)
    :   Used by ema\_workbench.

    abstractmethod finalize()
    :   Finalize the evaluator.

    abstractmethod initialize()
    :   Initialize the evaluator.

    optimize(*algorithm: type[AbstractGeneticAlgorithm] = EpsNSGAII*, *nfe: int = 10000*, *searchover: str = 'levers'*, *reference: [Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample") | None = None*, *constraints: Iterable[[Constraint](outcomes.html#ema_workbench.em_framework.outcomes.Constraint "ema_workbench.em_framework.outcomes.Constraint")] | None = None*, *convergence\_freq: int = 1000*, *logging\_freq: int = 5*, *variator: type[Variator] | None = None*, *rng: Iterable[StdlibSeedLike] | None = None*, *initial\_population: Iterable[[Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")] | None = None*, *filename: str | None = None*, *directory: str | None = None*, *\*\*kwargs*) → list[tuple[DataFrame, DataFrame]]

    optimize(*algorithm: type[AbstractGeneticAlgorithm] = EpsNSGAII*, *nfe: int = 10000*, *searchover: str = 'levers'*, *reference: [Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample") | None = None*, *constraints: Iterable[[Constraint](outcomes.html#ema_workbench.em_framework.outcomes.Constraint "ema_workbench.em_framework.outcomes.Constraint")] | None = None*, *convergence\_freq: int = 1000*, *logging\_freq: int = 5*, *variator: type[Variator] | None = None*, *rng: StdlibSeedLike | None = None*, *initial\_population: Iterable[[Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")] | None = None*, *filename: str | None = None*, *directory: str | None = None*, *\*\*kwargs*) → tuple[DataFrame, DataFrame]
    :   Convenience method for outcome optimization.

        A call to this method is forwarded to :func:optimize, with evaluator and models
        arguments added in.

    perform\_experiments(*scenarios: int | Iterable[[Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")] | [Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample") = 0*, *policies: int | Iterable[[Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")] | [Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample") = 0*, *reporting\_interval: int | None = None*, *reporting\_frequency: int | None = 10*, *uncertainty\_union: bool = False*, *lever\_union: bool = False*, *outcome\_union: bool = False*, *uncertainty\_sampling: [AbstractSampler](samplers.html#ema_workbench.em_framework.samplers.AbstractSampler "ema_workbench.em_framework.samplers.AbstractSampler") | SamplerTypes = Samplers.LHS*, *uncertainty\_sampling\_kwargs: dict | None = None*, *lever\_sampling: [AbstractSampler](samplers.html#ema_workbench.em_framework.samplers.AbstractSampler "ema_workbench.em_framework.samplers.AbstractSampler") | SamplerTypes = Samplers.LHS*, *lever\_sampling\_kwargs: dict | None = None*, *callback: type[[AbstractCallback](callbacks.html#ema_workbench.em_framework.callbacks.AbstractCallback "ema_workbench.em_framework.callbacks.AbstractCallback")] | None = None*, *combine: Literal['full\_factorial', 'sample', 'cycle'] = 'full\_factorial'*, *\*\*kwargs*)
    :   Convenience method for performing experiments.

        A call to this method is forwarded to :func:perform\_experiments, with evaluator and
        models arguments added in.

    robust\_optimize(*robustness\_functions: list[~ema\_workbench.em\_framework.outcomes.ScalarOutcome], scenarios: int | ~collections.abc.Iterable[~ema\_workbench.em\_framework.points.Sample], algorithm: type[~platypus.algorithms.AbstractGeneticAlgorithm] = <class 'platypus.algorithms.EpsNSGAII'>, nfe: int = 10000, convergence\_freq: int = 1000, logging\_freq: int = 5, rng: ~ema\_workbench.em\_framework.util.StdlibSeedLike | ~collections.abc.Iterable[~ema\_workbench.em\_framework.util.StdlibSeedLike] | None = None, \*\*kwargs*) → tuple[DataFrame, DataFrame]
    :   Convenience method for robust optimization.

        A call to this method is forwarded to :func:robust\_optimize, with evaluator and models
        arguments added in.

class ema\_workbench.em\_framework.evaluators.Samplers(*\*values*)
:   Enum for different kinds of samplers.

class ema\_workbench.em\_framework.evaluators.SequentialEvaluator(*msis: [AbstractModel](model.html#ema_workbench.em_framework.model.AbstractModel "ema_workbench.em_framework.model.AbstractModel") | list[[AbstractModel](model.html#ema_workbench.em_framework.model.AbstractModel "ema_workbench.em_framework.model.AbstractModel")]*)
:   Sequential evaluator.

    evaluate\_experiments(*experiments: Iterable[[Experiment](points.html#ema_workbench.em_framework.points.Experiment "ema_workbench.em_framework.points.Experiment")]*, *callback: Callable*, *\*\*kwargs*)
    :   Evaluate experiments.

    finalize()
    :   Finalizer.

    initialize()
    :   Initializer.

ema\_workbench.em\_framework.evaluators.optimize(*model: [AbstractModel](model.html#ema_workbench.em_framework.model.AbstractModel "ema_workbench.em_framework.model.AbstractModel")*, *algorithm: type[AbstractGeneticAlgorithm] = EpsNSGAII*, *nfe: int = 10000*, *searchover: str = 'levers'*, *evaluator: [BaseEvaluator](#ema_workbench.em_framework.evaluators.BaseEvaluator "ema_workbench.em_framework.evaluators.BaseEvaluator") | None = None*, *reference: [Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample") | None = None*, *constraints: Iterable[[Constraint](outcomes.html#ema_workbench.em_framework.outcomes.Constraint "ema_workbench.em_framework.outcomes.Constraint")] | None = None*, *convergence\_freq: int = 1000*, *logging\_freq: int = 5*, *variator: Variator = None*, *rng: Iterable[StdlibSeedLike] | None = None*, *initial\_population: Iterable[[Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")] | None = None*, *filename: str | None = None*, *directory: str | None = None*, *\*\*kwargs*) → list[tuple[DataFrame, DataFrame]]

ema\_workbench.em\_framework.evaluators.optimize(*model: [AbstractModel](model.html#ema_workbench.em_framework.model.AbstractModel "ema_workbench.em_framework.model.AbstractModel")*, *algorithm: type[AbstractGeneticAlgorithm] = EpsNSGAII*, *nfe: int = 10000*, *searchover: str = 'levers'*, *evaluator: [BaseEvaluator](#ema_workbench.em_framework.evaluators.BaseEvaluator "ema_workbench.em_framework.evaluators.BaseEvaluator") | None = None*, *reference: [Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample") | None = None*, *constraints: Iterable[[Constraint](outcomes.html#ema_workbench.em_framework.outcomes.Constraint "ema_workbench.em_framework.outcomes.Constraint")] | None = None*, *convergence\_freq: int = 1000*, *logging\_freq: int = 5*, *variator: Variator = None*, *rng: StdlibSeedLike | None = None*, *initial\_population: Iterable[[Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")] | None = None*, *filename: str | None = None*, *directory: str | None = None*, *\*\*kwargs*) → tuple[DataFrame, DataFrame]
:   Optimize the model.

    Parameters:
    :   - **model** (*1* *or* *more Model instances*)
        - **algorithm** (*a valid Platypus optimization algorithm*)
        - **nfe** (*int*)
        - **searchover** (*{'uncertainties'**,* *'levers'}*)
        - **evaluator** (*evaluator instance*)
        - **reference** (*Sample instance**,* *optional*) – overwrite the default scenario in case of searching over
          levers, or default policy in case of searching over
          uncertainties
        - **constraints** (*list**,* *optional*)
        - **convergence\_freq** (*int*) – nfe between convergence check
        - **logging\_freq** (*int*) – number of generations between logging of progress
        - **variator** (*platypus GAOperator instance**,* *optional*) – if None, it falls back on the defaults in platypus-opts
          which is SBX with PM
        - **rng** (*seed for initializing the global python random number generator as used by platypus-opt*) – because platypus-opt uses the global random number generator, full reproducibility cannot
          be guaranteed in case of threading.
          If seed is an iterable, the optimization is run for each seed. The seed is added to the filename
          to ensure separate tarballs for each run of the optimization.
        - **initial\_population** (*A collection* *of* *samples with which to initialize the optimization algorithm*)
        - **filename** (*filename for storing intermediate archives/results*) – Every convergence\_freq, the archive or results at that moment are added to this file.
          The file itself will be a tarball.
        - **directory** (*directory in which to store tarball* *of* *intermediate archives/results.*)
        - **kwargs** (*any additional arguments will be passed on to algorithm*)

    Returns:
    :   - *pandas DataFrame with pareto front*
        - *pandas DataFrame with runtime convergence information*

    Raises:
    :   **ValueError if searchover is not one** **of** **'uncertainties'** **or** **'levers'** –

ema\_workbench.em\_framework.evaluators.perform\_experiments(*models: [AbstractModel](model.html#ema_workbench.em_framework.model.AbstractModel "ema_workbench.em_framework.model.AbstractModel") | list[[AbstractModel](model.html#ema_workbench.em_framework.model.AbstractModel "ema_workbench.em_framework.model.AbstractModel")]*, *scenarios: int | Iterable[[Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")] | [Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample") = 0*, *policies: int | Iterable[[Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample")] | [Sample](points.html#ema_workbench.em_framework.points.Sample "ema_workbench.em_framework.points.Sample") = 0*, *evaluator: [BaseEvaluator](#ema_workbench.em_framework.evaluators.BaseEvaluator "ema_workbench.em_framework.evaluators.BaseEvaluator") | None = None*, *reporting\_interval: int | None = None*, *reporting\_frequency: int | None = 10*, *uncertainty\_union: bool = False*, *lever\_union: bool = False*, *outcome\_union: bool = False*, *uncertainty\_sampling: [AbstractSampler](samplers.html#ema_workbench.em_framework.samplers.AbstractSampler "ema_workbench.em_framework.samplers.AbstractSampler") | SamplerTypes = Samplers.LHS*, *uncertainty\_sampling\_kwargs: dict | None = None*, *lever\_sampling: [AbstractSampler](samplers.html#ema_workbench.em_framework.samplers.AbstractSampler "ema_workbench.em_framework.samplers.AbstractSampler") | SamplerTypes = Samplers.LHS*, *lever\_sampling\_kwargs: dict | None = None*, *callback: type[[AbstractCallback](callbacks.html#ema_workbench.em_framework.callbacks.AbstractCallback "ema_workbench.em_framework.callbacks.AbstractCallback")] | None = None*, *return\_callback: bool = False*, *combine: Literal['full\_factorial', 'sample', 'cycle'] = 'full\_factorial'*, *log\_progress: bool = False*, *\*\*kwargs*) → [DefaultCallback](callbacks.html#ema_workbench.em_framework.callbacks.DefaultCallback "ema_workbench.em_framework.callbacks.DefaultCallback") | tuple[DataFrame, dict[str, ndarray]]
:   Sample uncertainties and levers, and perform the resulting experiments on each of the models.

    Parameters:
    :   - **models** (*one* *or* *more AbstractModel instances*)
        - **scenarios** (*int* *or* *iterable* *of* *Sample instances**,* *optional*)
        - **policies** (*int* *or* *iterable* *of* *Sample instances**,* *optional*)
        - **evaluator** (*Additional keyword arguments are passed on to evaluate\_experiments* *of* *the*)
        - **reporting\_interval** (*int**,* *optional*)
        - **reporting\_frequency** (*int**,* *optional*)
        - **uncertainty\_union** (*boolean**,* *optional*)
        - **lever\_union** (*boolean**,* *optional*)
        - **outcome\_union** (*boolean**,* *optional*)
        - **uncertainty\_sampling** (*{LHS**,* *MC**,* *FF**,* *SOBOL**,* *MORRIS**,* *FAST}**,* *optional*)
        - **uncertainty\_sampling\_kwargs** (*dict**,* *optional*)
        - **lever\_sampling** (*{LHS**,* *MC**,* *FF**,* *SOBOL**,* *MORRIS**,* *FAST}**,* *optional TODO:: update doc*)
        - **lever\_sampling\_kwargs** (*dict**,* *optional*)
        - **callback** (*Callback instance**,* *optional*)
        - **return\_callback** (*boolean**,* *optional*)
        - **log\_progress** (*bool**,* *optional*)
        - **combine** (*{'factorial'**,* *'sample'}**,* *optional*) – how to combine uncertainties and levers?
          In case of ‘factorial’, both are sampled separately using their
          respective samplers. Next the resulting designs are combined in a
          full factorial manner.
          In case of ‘sample’, both are sampled separately and
          then combined by cycling over the shortest of the the two sets
          of designs until the longest set of designs is exhausted.
        - **evaluator**

    Returns:
    :   the experiments as a dataframe, and a dict
        with the name of an outcome as key, and the associated values
        as numpy array. Experiments and outcomes are aligned on index.

    Return type:
    :   tuple

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/evaluators.html
