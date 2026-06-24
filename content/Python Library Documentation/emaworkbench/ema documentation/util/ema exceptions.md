---
title: "ema_exceptions"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/util/ema_exceptions.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `ema_exceptions`

Exceptions and warning used internally by the EMA workbench.

In line with advice given in [PEP 8](https://www.python.org/dev/peps/pep-0008/).

exception ema\_workbench.util.ema\_exceptions.EMAError(*\*args*)
:   Base EMA error.

exception ema\_workbench.util.ema\_exceptions.EMAParallelError(*\*args*)
:   Parallel EMA error.

exception ema\_workbench.util.ema\_exceptions.EMAWarning(*\*args*)
:   base EMA warning class.

exception ema\_workbench.util.ema\_exceptions.ExperimentError(*message: str*, *experiment*, *policy=None*)
:   Error to be used when a particular experiment does not complete correctly.

    The character of the error can be specified as the message, and the actual experiment that
    gave rise to the error.

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/util/ema_exceptions.html
