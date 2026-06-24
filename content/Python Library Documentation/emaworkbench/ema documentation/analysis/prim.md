---
title: "prim"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/prim.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `prim`

A scenario discovery oriented implementation of PRIM.

The implementation of prim provided here is data type aware, so
categorical variables will be handled appropriately. It also uses a
non-standard objective function in the peeling and pasting phase of the
algorithm. This algorithm looks at the increase in the mean divided
by the amount of data removed. So essentially, it uses something akin
to the first order derivative of the original objective function.

The implementation is designed for interactive use in combination with
the jupyter notebook.

class ema\_workbench.analysis.prim.PRIMObjectiveFunctions(*\*values*)
:   Enum for the prim objectives functions.

class ema\_workbench.analysis.prim.Prim(*x: DataFrame*, *y: ndarray*, *obj\_function: Literal[PRIMObjectiveFunctions.LENIENT1, PRIMObjectiveFunctions.LENIENT2, PRIMObjectiveFunctions.ORIGINAL] = PRIMObjectiveFunctions.LENIENT1*, *peel\_alpha: float = 0.05*, *paste\_alpha: float = 0.05*, *mass\_min: float = 0.05*, *update\_function: Literal['default', 'guivarch'] = 'default'*)
:   Patient rule induction algorithm.

    The implementation of Prim is tailored to interactive use in the
    context of scenario discovery.

    Parameters:
    :   - **x** (*DataFrame*) – the independent variables
        - **y** (*1d ndarray*) – the dependent variable
        - **obj\_function** (*{LENIENT1**,* *LENIENT2**,* *ORIGINAL}*) – the objective function used by PRIM. Defaults to a
          lenient objective function based on the gain of mean
          divided by the loss of mass.
        - **peel\_alpha** (*float**,* *optional*) – parameter controlling the peeling stage (default = 0.05).
        - **paste\_alpha** (*float**,* *optional*) – parameter controlling the pasting stage (default = 0.05).
        - **mass\_min** (*float**,* *optional*) – minimum mass of a box (default = 0.05).
        - **{'default'** (*update\_function =*) – controls behavior of PRIM after having found a
          first box. use either the default behavior were
          all points are removed, or the procedure
          suggested by Guivarch et al (2016)
          doi:10.1016/j.envsoft.2016.03.006 to simply set
          all points to be no longer of interest (only
          valid in binary mode).
        - **'guivarch'}** – controls behavior of PRIM after having found a
          first box. use either the default behavior were
          all points are removed, or the procedure
          suggested by Guivarch et al (2016)
          doi:10.1016/j.envsoft.2016.03.006 to simply set
          all points to be no longer of interest (only
          valid in binary mode).
        - **optional** – controls behavior of PRIM after having found a
          first box. use either the default behavior were
          all points are removed, or the procedure
          suggested by Guivarch et al (2016)
          doi:10.1016/j.envsoft.2016.03.006 to simply set
          all points to be no longer of interest (only
          valid in binary mode).

    `cart`

class ema\_workbench.analysis.prim.PrimBox(*prim: BasePrim*, *box\_lims: DataFrame*, *indices: ndarray*)
:   A class that holds information for a specific box.

    coverage
    :   coverage of currently selected box

        Type:
        :   float

    density
    :   density of currently selected box

        Type:
        :   float

    mean
    :   mean of currently selected box

        Type:
        :   float

    res\_dim
    :   number of restricted dimensions of currently selected box

        Type:
        :   int

    mass
    :   mass of currently selected box

        Type:
        :   float

    peeling\_trajectory
    :   stats for each box in peeling trajectory

        Type:
        :   DataFrame

    box\_lims
    :   list of box lims for each box in peeling trajectory

        Type:
        :   list

    by default, the currently selected box is the last box on the
    peeling trajectory, unless this is changed via
    `PrimBox.select()`.

    inspect\_tradeoff()
    :   Inspecting tradeoff using altair.

    resample(*i: int | None = None*, *iterations: int = 10*, *p: float = 0.5*, *rng: RNGLike | NumpySeedLike | None = None*) → DataFrame
    :   Calculate resample statistics for candidate box i.

        Parameters:
        :   - **i** (*int**,* *optional*)
            - **iterations** (*int**,* *optional*)
            - **p** (*float**,* *optional*)
            - **rng** (*seed* *or* *random number generator**,* *optional*)

        Return type:
        :   DataFrame

    show\_tradeoff(*cmap=<matplotlib.colors.ListedColormap object>*, *annotated: bool = False*) → Figure
    :   Visualize the trade-off between coverage and density.

        Color is used to denote the number of restricted dimensions.

        Parameters:
        :   - **cmap** (*valid matplotlib colormap*)
            - **annotated** (*bool**,* *optional. Shows point labels if True.*)

        Return type:
        :   a Figure instance

    property stats
    :   Return stats of this box.

    update(*box\_lims: DataFrame*, *indices: ndarray*)
    :   Update the box to the provided box limits.

        Parameters:
        :   - **box\_lims** (*DataFrame*) – the new box\_lims
            - **indices** (*ndarray*) – the indices of y that are inside the box

ema\_workbench.analysis.prim.pca\_preprocess(*experiments: DataFrame*, *y: ndarray*, *subsets: dict | None = None*, *exclude: list[str] | None = None*) → tuple[DataFrame, DataFrame]
:   Perform PCA to preprocess experiments before running PRIM.

    Pre-process the data by performing a pca based rotation on it.
    This effectively turns the algorithm into PCA-PRIM as described
    in [Dalal et al. (2013)](https://www.sciencedirect.com/science/article/pii/S1364815213001345)

    Parameters:
    :   - **experiments** (*DataFrame*)
        - **y** (*ndarray*) – one dimensional binary array
        - **subsets** (*dict**,* *optional*) – expects a dictionary with group name as key and a list of
          uncertainty names as values. If this is used, a constrained
          PCA-PRIM is executed
        - **exclude** (*list* *of* *str**,* *optional*) – the uncertainties that should be excluded from the rotation

    Returns:
    :   - *rotated\_experiments* – DataFrame
        - *rotation\_matrix* – DataFrame

    Raises:
    :   **RuntimeError** – if mode is not binary (i.e. y is not a binary classification).
        if X contains non numeric columns

ema\_workbench.analysis.prim.run\_constrained\_prim(*experiments: DataFrame*, *y: ndarray*, *issignificant: bool = True*, *\*\*kwargs*) → [PrimBox](#ema_workbench.analysis.prim.PrimBox "ema_workbench.analysis.prim.PrimBox")
:   Run PRIM repeatedly while constraining the maximum number of dimensions available in x.

    Improved usage of PRIM as described in [Kwakkel (2019)](https://onlinelibrary.wiley.com/doi/full/10.1002/ffo2.8).

    Parameters:
    :   - **experiments** (*DataFrame*)
        - **y** (*numpy array*)
        - **issignificant** (*bool**,* *optional*) – if True, run prim only on subsets of dimensions
          that are significant for the initial PRIM on the
          entire dataset.
        - **\*\*kwargs** (*any additional keyword arguments are passed on to PRIM*)

    Return type:
    :   PrimBox instance

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/prim.html
