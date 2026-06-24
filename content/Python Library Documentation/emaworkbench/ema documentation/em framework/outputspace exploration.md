---
title: "outputspace_exploration"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/outputspace_exploration.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `outputspace_exploration`

Provides a genetic algorithm based on novelty search for output space exploration.

The algorithm is inspired by [Chérel et al (2015)](https://doi.org/10.1371/journal.pone.0138212). In short,
from Chérel et al, we have taken the idea of the HitBox. Basically, this is an epsilon archive where one
keeps track of how many solutions have fallen into each grid cell. Next, tournament selection based on novelty is
used as the selective pressure. Novelty is defined as 1/nr. of solutions in same grid cell. This is then
combined with auto-adaptive population sizing as used in e-NSGAII. This replaces the use of adaptive Cauchy mutation
as used by Chérel et al. There is also an more sophisticated algorithm that adds auto-adaptive operator selection as
used in BORG.

The algorithm can be used in combination with the optimization functionality of the workbench.
Just pass an OutputSpaceExploration instance as algorithm to optimize.

class ema\_workbench.em\_framework.outputspace\_exploration.AutoAdaptiveOutputSpaceExplorationAlgorithm(*problem*, *grid\_spec=None*, *population\_size=100*, *generator=<platypus.operators.RandomGenerator object>*, *variator=None*, *\*\*kwargs*)
:   A combination of auto-adaptive operator selection with OutputSpaceExploration.

    The parametrization of all operators is based on the default values as used
    in Borg 1.9.

    Parameters:
    :   - **problem** (*a platypus Problem instance*)
        - **grid\_spec** (*list* *of* *tuples*) – with min, max, and epsilon for
          each outcome of interest
        - **population\_size** (*int**,* *optional*)

    Notes

    Limited to RealParameters only.

class ema\_workbench.em\_framework.outputspace\_exploration.OutputSpaceExplorationAlgorithm(*problem*, *grid\_spec=None*, *population\_size=100*, *generator=<platypus.operators.RandomGenerator object>*, *variator=None*, *\*\*kwargs*)
:   Basic genetic algorithm for output space exploration using novelty search.

    Parameters:
    :   - **problem** (*the optimization problem*)
        - **grid\_spec** (*specification* *of* *the grid used for novelty search*)
        - **population\_size** (*population size for the algorithm*)
        - **generator** (*generator* *of* *candidate solutions*)
        - **variator** (*the evolutionary variator to create new solutions.*)
        - **space.** (*The algorithm defines novelty using an epsilon-like grid in the output*)
        - **cell.** (*Novelty is one divided by the number* *of* *seen solutions in a given grid*)
        - **Crossover** (*Tournament selection using novelty is used to create offspring.*)
        - **polynomial** (*is done using simulated binary crossover and mutation is done using*)
        - **mutation.**
        - **implemented** (*The epsilon like grid structure for tracking novelty is*)
        - **archive** (*using an*)
        - **cell** (*the Hit Box. Per epsilon grid*)
        - **closes** (*a single solution*)
        - **algorithm** (*to the centre* *of* *the cell is maintained. This makes the*)
        - **ε-NSGAII.** (*behave virtually identical to*)
        - **defined.** (*The archive is returned as results and epsilon progress is*)
        - **search** (*To deal with a stalled*)
        - **continuation** (*adaptive time*)
        - **to** (*identical*)
        - **used.** (*ε-NSGAII is*)

    Notes

    Output space exploration relies on the optimization functionality of the
    workbench. Therefore, outcomes of kind INFO are ignored. For output
    space exploration the direction (i.e. minimize or maximize) does not matter.

    initialize() → None
    :   Initialize the algorithm.

    iterate() → None
    :   A signle iteration of the algorithm.

    step() → None
    :   A single step of the algorithm.

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/outputspace_exploration.html
