---
title: "salib_samplers"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/salib_samplers.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `salib_samplers`

Samplers for working with SALib.

class ema\_workbench.em\_framework.salib\_samplers.FASTSampler
:   Sampler generating a Fourier Amplitude Sensitivity Test (FAST).

    sample(*problem: dict*, *size: int*, *rng: Generator | None*, *\*\*kwargs*) → ndarray
    :   Call the underlying salib sampling method and return the samples.

        Any additional keyword arguments will be passed to the underlying salib sampling method

        Parameters:
        :   - **problem** (*a dictionary with the problem specification*)
            - **size** (*the number* *of* *samples to generate*)
            - **rng** (*a np.random.Generator**, or* *something that can seed a rgn.*)
            - **kwargs** (*any additional keyword arguments*)
            - **are** (*Additional valid keyword arguments*)
            - **M** (*int* *(**default: 4**)*) – The interference parameter, i.e., the number of harmonics to sum in the
              Fourier series decomposition (default 4)
            - **decomposition** (*Fourier series*)

class ema\_workbench.em\_framework.salib\_samplers.MorrisSampler
:   Sampler generating a morris design using SALib.

    sample(*problem: dict*, *size: int*, *rng: Generator | None*, *\*\*kwargs*) → ndarray
    :   Call the underlying salib sampling method and return the samples.

        Any additional keyword arguments will be passed to the underlying salib sampling method

        Parameters:
        :   - **problem** (*a dictionary with the problem specification*)
            - **size** (*the number* *of* *samples to generate*)
            - **rng** (*a np.random.Generator**, or* *something that can seed a rgn.*)
            - **kwargs** (*any additional keyword arguments*)
            - **are** (*Additional valid keyword arguments*)
            - **num\_levels** (*int*) – The number of grid levels
            - **grid\_jump** (*int*) – The grid jump size
            - **optimal\_trajectories** (*int**,* *optional*) – The number of optimal trajectories to sample (between 2 and N)
            - **local\_optimization** (*bool**,* *optional*) – Flag whether to use local optimization according to Ruano et al. (2012)
              Speeds up the process tremendously for bigger N and num\_levels.
              Stating this variable to be true causes the function to ignore gurobi.

class ema\_workbench.em\_framework.salib\_samplers.SobolSampler
:   Sampler generating a Sobol design using SALib.

    sample(*problem: dict*, *size: int*, *rng: Generator | None*, *\*\*kwargs*) → ndarray
    :   Call the underlying salib sampling method and return the samples.

        Any additional keyword arguments will be passed to the underlying salib sampling method

        Parameters:
        :   - **problem** (*a dictionary with the problem specification*)
            - **size** (*the number* *of* *samples to generate*)
            - **rng** (*a np.random.Generator**, or* *something that can seed a rgn.*)
            - **kwargs** (*any additional keyword arguments*)
            - **are** (*Additional valid keyword arguments*)
            - **calc\_second\_order** (*bool**,* *optional*) – Calculate second-order sensitivities. Default is True.
            - **scramble** (*bool**,* *optional*) – If True, use LMS+shift scrambling. Otherwise, no scrambling is done.
              Default is True.
            - **skip\_values** (*int**,* *optional*) – Number of points in Sobol’ sequence to skip, ideally a value of base 2.
              It’s recommended not to change this value and use scramble instead.
              scramble and skip\_values can be used together.
              Default is 0.

ema\_workbench.em\_framework.salib\_samplers.get\_SALib\_problem(*parameters: Collection[[Parameter](parameters.html#ema_workbench.em_framework.parameters.Parameter "ema_workbench.em_framework.parameters.Parameter")]*)
:   Returns a dict with a problem specification as required by SALib.

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/salib_samplers.html
