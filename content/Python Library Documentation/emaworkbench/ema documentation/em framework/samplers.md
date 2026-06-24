---
title: "samplers"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/samplers.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `samplers`

A variety of samplers.

These different samplers implement basic sampling
techniques including Full Factorial sampling, Latin Hypercube sampling, and
Monte Carlo sampling.

class ema\_workbench.em\_framework.samplers.AbstractSampler
:   Abstract base class from which different samplers can be derived.

    In the simplest cases, only the sample method needs to be overwritten.
    generate\_designs` is the only method called from outside. The
    other methods are used internally to generate the designs.

    abstractmethod generate\_samples(*parameters: ParameterMap | Iterable[[Parameter](parameters.html#ema_workbench.em_framework.parameters.Parameter "ema_workbench.em_framework.parameters.Parameter")]*, *size: int*, *rng: NumpySeedLike | RNGLike | None = None*, *\*\*kwargs*) → [SampleCollection](points.html#ema_workbench.em_framework.points.SampleCollection "ema_workbench.em_framework.points.SampleCollection")
    :   Generate n samples from the parameters.

        Parameters:
        :   - **parameters** (*collection*) – a collection of `RealParameter`,
              `IntegerParameter`,
              and `CategoricalParameter`
              instances.
            - **size** (*int*) – the number of samples to generate.
            - **rng** (*numpy random number generator*)
            - **kwargs** (*any additional keyword arguments*)

        Return type:
        :   numpy array with samples

class ema\_workbench.em\_framework.samplers.FullFactorialSampler
:   Generates a full factorial sample.

    If the parameter is non-categorical, the resolution is set the
    number of samples. If the parameter is categorical, the specified value
    for samples will be ignored and each category will be used instead.

    generate\_samples(*parameters: ParameterMap | Iterable[[Parameter](parameters.html#ema_workbench.em_framework.parameters.Parameter "ema_workbench.em_framework.parameters.Parameter")]*, *size: int*, *rng: NumpySeedLike | RNGLike | None = None*, *\*\*kwargs*) → [SampleCollection](points.html#ema_workbench.em_framework.points.SampleCollection "ema_workbench.em_framework.points.SampleCollection")
    :   Generate samples using full factorial sampling.

        Parameters:
        :   - **parameters** (*collection*) – a collection of `RealParameter`,
              `IntegerParameter`,
              and `CategoricalParameter`
              instances.
            - **size** (*int*) – the number of samples to generate.
            - **rng** (*numpy random number generator*)
            - **kwargs** (*any additional keyword arguments*)
            - **sampler.** (*There are no additional valid keyword arguments for the Monte Carlo*)

class ema\_workbench.em\_framework.samplers.LHSSampler
:   generates a Latin Hypercube sample over the parameters.

    generate\_samples(*parameters: ParameterMap*, *size: int*, *rng: NumpySeedLike | RNGLike | None = None*, *\*\*kwargs*) → [SampleCollection](points.html#ema_workbench.em_framework.points.SampleCollection "ema_workbench.em_framework.points.SampleCollection")
    :   Generate samples using latin hypercube sampling.

        Parameters:
        :   - **parameters** (*collection*) – a collection of `RealParameter`,
              `IntegerParameter`,
              and `CategoricalParameter`
              instances.
            - **size** (*int*) – the number of samples to generate.
            - **rng** (*numpy random number generator*)
            - **kwargs** (*any additional keyword arguments*)
            - **are** (*Additional valid keyword arguments*)
            - **scramble** (*bool**,* *optional*)
            - **optimization** (*{None**,* *"random-cd"**,* *"lloyd"}**,* *optional*)
            - **strength** (*{1**,* *2}**,* *optional*)

        Return type:
        :   numpy array with samples

class ema\_workbench.em\_framework.samplers.MonteCarloSampler
:   Monte Carlo sampler for each of the parameters.

    generate\_samples(*parameters: ParameterMap | Iterable[[Parameter](parameters.html#ema_workbench.em_framework.parameters.Parameter "ema_workbench.em_framework.parameters.Parameter")]*, *size: int*, *rng: NumpySeedLike | RNGLike | None = None*, *\*\*kwargs*) → [SampleCollection](points.html#ema_workbench.em_framework.points.SampleCollection "ema_workbench.em_framework.points.SampleCollection")
    :   Generate samples using Monte Carlo sampling.

        Parameters:
        :   - **parameters** (*collection*) – a collection of `RealParameter`,
              `IntegerParameter`,
              and `CategoricalParameter`
              instances.
            - **size** (*int*) – the number of samples to generate.
            - **rng** (*numpy random number generator*)
            - **kwargs** (*any additional keyword arguments*)
            - **sampler.** (*There are no additional valid keyword arguments for the Monte Carlo*)

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/samplers.html
