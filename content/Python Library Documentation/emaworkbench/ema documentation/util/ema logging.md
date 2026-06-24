---
title: "ema_logging"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/util/ema_logging.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `ema_logging`

Helper functions and classes for logging in the workbench.

It is modeled on the default [logging approach that comes with
Python](https://docs.python.org/library/logging.html).
This logging system will also work in case of multiprocessing.

ema\_workbench.util.ema\_logging.get\_module\_logger(*name: str*) → Logger
:   Return a module logger with the given name.

ema\_workbench.util.ema\_logging.get\_rootlogger() → Logger
:   Returns root logger used by the EMA workbench.

    Return type:
    :   the logger of the EMA workbench

ema\_workbench.util.ema\_logging.log\_to\_stderr(*level: int | None = None*, *pass\_root\_logger\_level: bool = False*) → Logger
:   Turn on logging and add a handler which prints to stderr.

    Parameters:
    :   - **level** (*int*) – minimum level of the messages that will be logged
        - **pas\_root\_logger\_level** (*bool**,* *optional. Default False*) – if true, all module loggers will be set to the
          same logging level as the root logger.
          Recommended True when using the MPIEvaluator.

ema\_workbench.util.ema\_logging.method\_logger(*name: str*) → callable
:   Wrap method so that every call to it is logged.

ema\_workbench.util.ema\_logging.temporary\_filter(*name: str | list[str] = 'EMA'*, *level: int | list[int] = 0*, *func\_name: str | list[str] | None = None*)
:   Temporary filter log message.

    Parameters:
    :   - **name** (*str* *or* *list* *of* *str**,* *optional*) – logger on which to apply the filter.
        - **level** (*int**, or* *list* *of* *int**,* *optional*) – don’t log message of this level or lower
        - **func\_name** (*str* *or* *list* *of* *str**,* *optional*) – don’t log message of this function
        - **logger** (*all modules have their own unique*)
        - **ema\_workbench.analysis.prim****)** (*(**e.g.*)

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/util/ema_logging.html
