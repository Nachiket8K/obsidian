---
title: "util"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/util.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `util`

utilities used throughout em\_framework.

class ema\_workbench.em\_framework.util.Counter(*startfrom=0*)
:   helper function for generating counter based names for NamedDicts.

class ema\_workbench.em\_framework.util.NamedDict(*name=<function representation>*, *\*\*kwargs*)
:   Named dictionary class.

    copy()
    :   Return a shallow copy of this object.

class ema\_workbench.em\_framework.util.NamedObject(*name: str*, *\*\*kwargs*)
:   Base object with a name attribute.

class ema\_workbench.em\_framework.util.NamedObjectMap(*kind: type[T]*)
:   A named object mapping class.

    clear() → None.  Remove all items from D.

    keys() → a set-like object providing a view on D's keys

class ema\_workbench.em\_framework.util.NamedObjectMapDescriptor(*kind*)
:   Descriptor class for named objects.

class ema\_workbench.em\_framework.util.ProgressTrackingMixIn(*N*, *reporting\_interval*, *logger*, *log\_progress=False*, *log\_func=<function ProgressTrackingMixIn.<lambda>>*)
:   Mixin for monitoring progress.

    Parameters:
    :   - **N** (*int*) – total number of experiments
        - **reporting\_interval** (*int*) – nfe between logging progress
        - **logger** (*logger instance*)
        - **log\_progress** (*bool**,* *optional*)
        - **log\_func** (*callable**,* *optional*) – function called with self as only argument, should invoke
          self.\_logger with custom log message

    i
    :   Type:
        :   int

    reporting\_interval
    :   Type:
        :   int

    log\_progress
    :   Type:
        :   bool

    log\_func
    :   Type:
        :   callable

    pbar
    :   if log\_progress is true, None, if false tqdm.tqdm instance

        Type:
        :   {None, tqdm.tqdm instance}

class ema\_workbench.em\_framework.util.Variable(*name: str*, *variable\_name: str | list[str] | None = None*)
:   Root class for input parameters and outcomes.

ema\_workbench.em\_framework.util.combine(*\*args*) → dict
:   Combine scenario and policy into a single experiment dict.

    Parameters:
    :   **args** (*two* *or* *more dicts that need to be combined*)

    Return type:
    :   a single unified dict containing the entries from all dicts

    Raises:
    :   [**EMAError**](../util/ema_exceptions.html#ema_workbench.util.ema_exceptions.EMAError "ema_workbench.util.ema_exceptions.EMAError") – if a keyword argument exists in more than one dict

ema\_workbench.em\_framework.util.determine\_objects(*models*, *attribute: Literal['uncertainties', 'levers', 'outcomes']*, *union=True*)
:   Determine the parameters over which to sample.

    Parameters:
    :   - **models** (*a collection* *of* *AbstractModel instances*)
        - **attribute** (*{'uncertainties'**,* *'levers'**,* *'outcomes'}*)
        - **union** (*bool**,* *optional*) – in case of multiple models, sample over the union of
          levers, or over the intersection of the levers

    Return type:
    :   collection of Parameter instances

ema\_workbench.em\_framework.util.representation(*named\_dict*)
:   Helper function for generating repr based names for NamedDicts.

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/util.html
