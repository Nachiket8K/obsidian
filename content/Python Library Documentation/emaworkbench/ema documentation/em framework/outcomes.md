---
title: "outcomes"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/outcomes.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `outcomes`

Module for outcome classes.

class ema\_workbench.em\_framework.outcomes.ArrayOutcome(*name*, *variable\_name=None*, *function=None*, *shape=None*, *dtype=None*)
:   Array Outcome class for n-dimensional arrays.

    Parameters:
    :   - **name** (*str*) – Name of the outcome.
        - **variable\_name** (*str**,* *optional*) – if the name of the outcome in the underlying model
          is different from the name of the outcome, you can
          supply the variable name as an optional argument,
          if not provided, defaults to name
        - **function** (*callable**,* *optional*) – a callable to perform postprocessing on data retrieved
          from model
        - **shape** (*{tuple**,* *None} optional*) – must be used in conjunction with dtype. Enables pre-allocation
          of data structure for storing results.
        - **dtype** (*datatype**,* *optional*) – must be used in conjunction with shape. Enables pre-allocation
          of data structure for storing results.

    name
    :   Type:
        :   str

    kind
    :   Type:
        :   int

    variable\_name
    :   Type:
        :   str

    function
    :   Type:
        :   callable

    shape
    :   Type:
        :   tuple

    dtype
    :   Type:
        :   datatype

    classmethod from\_disk(*filename*, *archive*)
    :   Helper function for loading from disk.

        Parameters:
        :   - **filename** (*str*)
            - **archive** (*Tarfile*)

    process(*values*)
    :   Process the values.

    classmethod to\_disk(*values*)
    :   Helper function for writing outcome to disk.

        Parameters:
        :   **values** (*ND array*)

        Returns:
        :   - *BytesIO*
            - *filename*

class ema\_workbench.em\_framework.outcomes.Constraint(*name*, *function: Callable*, *parameter\_names: list[str] | str | None = None*, *outcome\_names: list[str] | str | None = None*)
:   Constraints class that can be used when defining constrained optimization problems.

    Parameters:
    :   - **name** (*str*)
        - **parameter\_names** (*str* *or* *collection* *of* *str*)
        - **outcome\_names** (*str* *or* *collection* *of* *str*)
        - **function** (*callable*)

    name
    :   Type:
        :   str

    function
    :   The function should return the distance from the feasibility
        threshold, given the model outputs with a variable name. The
        distance should be 0 if the constraint is met.

        Type:
        :   callable

    parameter\_names
    :   name(s) of the uncertain parameter(s) and/or
        lever parameter(s) to which the constraint applies

        Type:
        :   str, list of str

    outcome\_names
    :   name(s) of the outcome(s) to which the constraint applies

        Type:
        :   str, list of str

    process(*values*)
    :   Process the values.

class ema\_workbench.em\_framework.outcomes.Outcome(*name: str*, *kind: int = 0*, *variable\_name: str | Sequence[str] | None = None*, *function: Callable[[...], Any] | None = None*, *shape: tuple[int, ...] | None = None*, *dtype: dtype | type | None = None*)
:   Base Outcome class.

    Parameters:
    :   - **name** (*str*) – Name of the outcome.
        - **kind** (*{INFO**,* *MINIMIZE**,* *MAXIMIZE}**,* *optional*)
        - **variable\_name** (*str**,* *optional*) – if the name of the outcome in the underlying model
          is different from the name of the outcome, you can
          supply the variable name as an optional argument,
          if not provided, defaults to name
        - **function** (*callable**,* *optional*) – a callable to perform postprocessing on data retrieved
          from model
        - **shape** (*{tuple**,* *None} optional*) – must be used in conjunction with dtype. Enables pre-allocation
          of data structure for storing results.
        - **dtype** (*datatype**,* *optional*) – must be used in conjunction with shape. Enables pre-allocation
          of data structure for storing results.

    name
    :   Type:
        :   str

    kind
    :   Type:
        :   int

    variable\_name
    :   Type:
        :   str

    function
    :   Type:
        :   callable

    shape
    :   Type:
        :   tuple

    dtype
    :   Type:
        :   dataype

    abstractmethod classmethod from\_disk(*filename: str*, *archive: TarFile*) → ndarray
    :   Helper function for loading from disk.

        Parameters:
        :   - **filename** (*str*)
            - **archive** (*Tarfile*)

    process(*values: list[Any]*) → Any
    :   Process the values.

    abstractmethod classmethod to\_disk(*values: ndarray | DataFrame*) → tuple[BytesIO, str]
    :   Helper function for writing outcome to disk.

        Parameters:
        :   **values** (*obj*) – data to store

        Return type:
        :   BytesIO

class ema\_workbench.em\_framework.outcomes.ScalarOutcome(*name: str*, *kind: int = 0*, *variable\_name: str | Sequence[str] | None = None*, *function: Callable[[...], Any] | None = None*, *dtype: dtype | type | None = None*)
:   Scalar Outcome class.

    Parameters:
    :   - **name** (*str*) – Name of the outcome.
        - **kind** (*{INFO**,* *MINIMIZE**,* *MAXIMIZE}**,* *optional*)
        - **variable\_name** (*str**,* *optional*) – if the name of the outcome in the underlying model
          is different from the name of the outcome, you can
          supply the variable name as an optional argument,
          if not provided, defaults to name
        - **function** (*callable**,* *optional*) – a callable to perform post processing on data retrieved
          from model
        - **dtype** (*datatype**,* *optional*) – Enables pre-allocation of data structure for storing results.

    name
    :   Type:
        :   str

    kind
    :   Type:
        :   int

    variable\_name
    :   Type:
        :   str

    function
    :   Type:
        :   callable

    shape
    :   Type:
        :   tuple

    dtype
    :   Type:
        :   datatype

    classmethod from\_disk(*filename*, *archive*)
    :   Helper function for loading from disk.

        Parameters:
        :   - **filename** (*str*)
            - **archive** (*Tarfile*)

    process(*values*)
    :   Process the values.

    classmethod to\_disk(*values*)
    :   Helper function for writing outcome to disk.

        Parameters:
        :   **values** (*1D array*)

        Returns:
        :   - *BytesIO*
            - *filename*

class ema\_workbench.em\_framework.outcomes.TimeSeriesOutcome(*name*, *variable\_name=None*, *function=None*, *shape=None*, *dtype=None*)
:   TimeSeries Outcome class for 1D arrays.

    Parameters:
    :   - **name** (*str*) – Name of the outcome.
        - **variable\_name** (*str**,* *optional*) – if the name of the outcome in the underlying model
          is different from the name of the outcome, you can
          supply the variable name as an optional argument,
          if not provided, defaults to name
        - **function** (*callable**,* *optional*) – a callable to perform postprocessing on data retrieved
          from model
        - **shape** (*{tuple**,* *None} optional*) – must be used in conjunction with dtype. Enables pre-allocation
          of data structure for storing results.
        - **dtype** (*datatype**,* *optional*) – must be used in conjunction with shape. Enables pre-allocation
          of data structure for storing results.

    name
    :   Type:
        :   str

    kind
    :   Type:
        :   int

    variable\_name
    :   Type:
        :   str

    function
    :   Type:
        :   callable

    shape
    :   Type:
        :   tuple

    dtype
    :   Type:
        :   datatype

    Notes

    Time series outcomes are currently assumed to be 1D arrays. If you
    are dealing with higher dimensional outputs (e.g., multiple replications
    resulting in 2D arrays), use ArrayOutcome instead.

    classmethod from\_disk(*filename*, *archive*)
    :   Helper function for loading from disk.

        Parameters:
        :   - **filename** (*str*)
            - **archive** (*Tarfile*)

    classmethod to\_disk(*values*)
    :   Helper function for writing outcome to disk.

        Parameters:
        :   **values** (*DataFrame*)

        Returns:
        :   - *StringIO*
            - *filename*

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/outcomes.html
