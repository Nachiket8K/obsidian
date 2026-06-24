---
title: "experiment_runner"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/experiment_runner.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `experiment_runner`

helper module for running individual experiments.

class ema\_workbench.em\_framework.experiment\_runner.ExperimentRunner(*msis*)
:   Helper class for running the experiments.

    This class contains the logic for initializing models properly,
    running the experiment, getting the results, and cleaning up afterwards.

    Parameters:
    :   - **msis** (*dict*)
        - **model\_kwargs** (*dict*)

    msi\_initializiation
    :   keeps track of which model is initialized with
        which policy.

        Type:
        :   dict

    msis
    :   models indexed by name

        Type:
        :   dict

    model\_kwargs
    :   keyword arguments for model\_init

        Type:
        :   dict

    cleanup()
    :   Cleanup after running.

    run\_experiment(*experiment*)
    :   The logic for running a single experiment.

        This code makes sure that model(s) are initialized correctly.

        Parameters:
        :   **experiment** (*Case instance*)

        Returns:
        :   - **experiment\_id** (*int*)
            - **case** (*dict*)
            - **policy** (*str*)
            - **model\_name** (*str*)
            - **result** (*dict*)

        Raises:
        :   - [**EMAError**](../util/ema_exceptions.html#ema_workbench.util.ema_exceptions.EMAError "ema_workbench.util.ema_exceptions.EMAError") – if the model instance raises an EMA error, these are reraised.
            - **Exception** – Catch all for all other exceptions being raised by the model.
              These are reraised.

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/em_framework/experiment_runner.html
