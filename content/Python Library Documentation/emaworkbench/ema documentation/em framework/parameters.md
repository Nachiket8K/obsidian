---
title: "parameters"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/parameters.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `parameters`

parameters and related helper classes and functions.

class ema\_workbench.em\_framework.parameters.BooleanParameter(*name*, *shape: tuple[int] | None = None*, *default: bool | None = None*, *variable\_name: str | list[str] | None = None*)
:   boolean model input parameter.

    A BooleanParameter is similar to a CategoricalParameter, except
    the category values can only be True or False.

    Parameters:
    :   - **name** (*str*)
        - **shape** (*tuple*)
        - **variable\_name** (*str**, or* *list* *of* *str*)

class ema\_workbench.em\_framework.parameters.CategoricalParameter(*name*, *categories*, *shape: tuple[int] | None = None*, *default=None*, *variable\_name: str | list[str] | None = None*, *multivalue: bool = False*)
:   categorical model input parameter.

    Parameters:
    :   - **name** (*str*)
        - **categories** (*collection* *of* *obj*)
        - **shape** (*tuple*)
        - **variable\_name** (*str**, or* *list* *of* *str*)
        - **multivalue** (*boolean*) – if categories have a set of values, for each variable\_name
          a different one.
        - **TODO** (*#*)
        - **TODO**

    cat\_for\_index(*index: int*) → [Category](#ema_workbench.em_framework.parameters.Category "ema_workbench.em_framework.parameters.Category")
    :   Return category given index.

        Parameters:
        :   **index** (*int*)

        Return type:
        :   object

    from\_dist(*name: str*, *dist*, *\*\*kwargs*)
    :   Factory method for creating a Parameter from a scipy distribution.

        Alternative constructor for creating a parameter from a frozen
        scipy.stats distribution directly

        Parameters:
        :   - **name** (*the name for the parameter*)
            - **dist** (*scipy stats frozen dist*)
            - **\*\*kwargs** (*valid keyword arguments for Parameter instance*)

    index\_for\_cat(*category: str*) → int
    :   Return index of category.

        Parameters:
        :   **category** (*object*)

        Return type:
        :   int

class ema\_workbench.em\_framework.parameters.Category(*name: str*, *value: Any*)
:   Category class.

class ema\_workbench.em\_framework.parameters.Constant(*name: str*, *value: Any*, *variable\_name: str | list[str] | None = None*)
:   Constant class.

    Can be used for any parameter that has to be set to a fixed value

class ema\_workbench.em\_framework.parameters.IntegerParameter(*name*, *lower\_bound: int*, *upper\_bound: int*, *shape: tuple[int] | None = None*, *resolution=None*, *default: int | None = None*, *variable\_name: str | list[str] | None = None*)
:   integer valued model input parameter.

    Parameters:
    :   - **name** (*str*)
        - **lower\_bound** (*int*)
        - **upper\_bound** (*int*)
        - **resolution** (*iterable*)
        - **variable\_name** (*str**, or* *list* *of* *str*)

    Raises:
    :   - **ValueError** – if lower bound is larger than upper bound
        - **ValueError** – if entries in resolution are outside range of lower\_bound and
          upper\_bound, or not an integer instance
        - **ValueError** – if lower\_bound or upper\_bound is not an integer instance

    classmethod from\_dist(*name: str*, *dist*, *\*\*kwargs*)
    :   Factory method for creating a Parameter from a scipy distribution.

        Alternative constructor for creating a parameter from a frozen
        scipy.stats distribution directly

        Parameters:
        :   - **name** (*the name for the parameter*)
            - **dist** (*scipy stats frozen dist*)
            - **\*\*kwargs** (*valid keyword arguments for Parameter instance*)

class ema\_workbench.em\_framework.parameters.Parameter(*name: str*, *lower\_bound*, *upper\_bound*, *shape: tuple[int] | None = None*, *resolution=None*, *default=None*, *variable\_name: str | list[str] | None = None*)
:   Base class for any model input parameter.

    Parameters:
    :   - **name** (*str*)
        - **lower\_bound** (*int* *or* *float*)
        - **upper\_bound** (*int* *or* *float*)
        - **shape** (*int* *or* *tuple*)
        - **resolution** (*collection*)

    Raises:
    :   - **ValueError** – if lower bound is larger than upper bound
        - **ValueError** – if entries in resolution are outside range of lower\_bound and
          upper\_bound

    classmethod from\_dist(*name: str*, *dist: rv\_continuous | rv\_discrete*, *\*\*kwargs: Any*) → [Parameter](#ema_workbench.em_framework.parameters.Parameter "ema_workbench.em_framework.parameters.Parameter")
    :   Factory method for creating a Parameter from a scipy distribution.

        Alternative constructor for creating a parameter from a frozen
        scipy.stats distribution directly

        Parameters:
        :   - **name** (*the name for the parameter*)
            - **dist** (*scipy stats frozen dist*)
            - **\*\*kwargs** (*valid keyword arguments for Parameter instance*)

    property resolution: list | None
    :   Getter for resolution.

class ema\_workbench.em\_framework.parameters.RealParameter(*name: str*, *lower\_bound: float*, *upper\_bound: float*, *shape: tuple[int] | None = None*, *resolution=None*, *default: float | None = None*, *variable\_name: str | list[str] | None = None*)
:   real valued model input parameter.

    Parameters:
    :   - **name** (*str*)
        - **lower\_bound** (*int* *or* *float*)
        - **upper\_bound** (*int* *or* *float*)
        - **shape** (*tuple*)
        - **resolution** (*iterable*)
        - **variable\_name** (*str**, or* *list* *of* *str*)

    Raises:
    :   - **ValueError** – if lower bound is larger than upper bound
        - **ValueError** – if entries in resolution are outside range of lower\_bound and
          upper\_bound

    classmethod from\_dist(*name: str*, *dist*, *\*\*kwargs*)
    :   Factory method for creating a Parameter from a scipy distribution.

        Alternative constructor for creating a parameter from a frozen
        scipy.stats distribution directly

        Parameters:
        :   - **name** (*the name for the parameter*)
            - **dist** (*scipy stats frozen dist*)
            - **\*\*kwargs** (*valid keyword arguments for Parameter instance*)

ema\_workbench.em\_framework.parameters.parameters\_from\_csv(*uncertainties*, *\*\*kwargs*)
:   Helper function for creating many Parameters based on a DataFrame or csv file.

    Parameters:
    :   - **uncertainties** (*str**,* *DataFrame*)
        - **\*\*kwargs** (*dict**,* *arguments to pass to pandas.read\_csv*)

    Return type:
    :   list of Parameter instances

    This helper function creates uncertainties. It assumes that the
    DataFrame or csv file has a column titled ‘name’, optionally a type column
    {int, real, cat}, can be included as well. the remainder of the columns
    are handled as values for the parameters. If type is not specified,
    the function will try to infer type from the values.

    Note that this function does not support the resolution and default kwargs
    on parameters.

    An example of a csv:

    NAME,TYPE,,,
    a\_real,real,0,1.1,
    an\_int,int,1,9,
    a\_categorical,cat,a,b,c

    this CSV file would result in

    [RealParameter(‘a\_real’, 0, 1.1, resolution=[], default=None),
    :   IntegerParameter(‘an\_int’, 1, 9, resolution=[], default=None),
        CategoricalParameter(‘a\_categorical’, [‘a’, ‘b’, ‘c’], default=None)]

ema\_workbench.em\_framework.parameters.parameters\_to\_csv(*parameters*, *file\_name*)
:   Helper function for writing a collection of parameters to a csv file.

    Parameters:
    :   - **parameters** (*collection* *of* *Parameter instances*)
        - **file\_name** (*str*)

    The function iterates over the collection and turns these into a data
    frame prior to storing them. The resulting csv can be loaded using the
    parameters\_from\_csv function. Note that currently we don’t store resolution
    and default attributes.

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/parameters.html
