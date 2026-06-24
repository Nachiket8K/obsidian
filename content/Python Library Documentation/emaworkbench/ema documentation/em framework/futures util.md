---
title: "futures_util"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/futures_util.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `futures_util`

Utilities for futures modules.

ema\_workbench.em\_framework.futures\_util.determine\_rootdir(*msis: Collection[[AbstractModel](model.html#ema_workbench.em_framework.model.AbstractModel "ema_workbench.em_framework.model.AbstractModel")]*) → str | None
:   Determine common root directory for all models.

ema\_workbench.em\_framework.futures\_util.finalizer(*experiment\_runner: [AbstractModel](model.html#ema_workbench.em_framework.model.AbstractModel "ema_workbench.em_framework.model.AbstractModel")*) → callable
:   Cleanup.

ema\_workbench.em\_framework.futures\_util.setup\_working\_directories(*models: Collection[[AbstractModel](model.html#ema_workbench.em_framework.model.AbstractModel "ema_workbench.em_framework.model.AbstractModel")]*, *root\_dir: str*) → str | None
:   Setup working directories when running in parallel.

    Copies the working directory of each model to a process specific
    temporary directory and update the working directory of the model.

    Parameters:
    :   - **models** (*list*)
        - **root\_dir** (*str*)

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/futures_util.html
