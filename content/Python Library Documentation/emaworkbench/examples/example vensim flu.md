---
title: "example_vensim_flu.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/example_vensim_flu.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# example\_vensim\_flu.py

```
  1"""A showcase of a mexican flu model with Vensim.
  2
  3This module shows how you can use vensim models directly
  4instead of coding the model in Python. The underlying case
  5is the same as used in example_flu.py
  6
  7
  8"""
  9
 10# Created on 20 May, 2011
 11# .. codeauthor:: jhkwakkel <j.h.kwakkel (at) tudelft (dot) nl>
 12#                 epruyt <e.pruyt (at) tudelft (dot) nl>
 13
 14import numpy as np
 15
 16from ema_workbench import (
 17    RealParameter,
 18    Sample,
 19    ScalarOutcome,
 20    TimeSeriesOutcome,
 21    ema_logging,
 22    perform_experiments,
 23    save_results,
 24)
 25from ema_workbench.connectors.vensim import VensimModel
 26
 27if __name__ == "__main__":
 28    ema_logging.log_to_stderr(ema_logging.INFO)
 29
 30    model = VensimModel(
 31        "fluCase", wd=r"./models/flu", model_file=r"FLUvensimV1basecase.vpm"
 32    )
 33
 34    # outcomes
 35    model.outcomes = [
 36        TimeSeriesOutcome("deceased_population_region_1"),
 37        TimeSeriesOutcome("infected_fraction_R1"),
 38        ScalarOutcome(
 39            "max_infection_fraction",
 40            function=np.max,
 41            variable_name="infected_fraction_R1",
 42        ),
 43    ]
 44
 45    # Plain Parametric Uncertainties
 46    model.uncertainties = [
 47        RealParameter("additional_seasonal_immune_population_fraction_R1", 0, 0.5),
 48        RealParameter(
 49            "additional_seasonal_immune_population_fraction_R2",
 50            0,
 51            0.5,
 52        ),
 53        RealParameter(
 54            "fatality_ratio_region_1",
 55            0.0001,
 56            0.1,
 57        ),
 58        RealParameter(
 59            "fatality_rate_region_2",
 60            0.0001,
 61            0.1,
 62        ),
 63        RealParameter(
 64            "initial_immune_fraction_of_the_population_of_region_1",
 65            0,
 66            0.5,
 67        ),
 68        RealParameter(
 69            "initial_immune_fraction_of_the_population_of_region_2",
 70            0,
 71            0.5,
 72        ),
 73        RealParameter(
 74            "normal_interregional_contact_rate",
 75            0,
 76            0.9,
 77        ),
 78        RealParameter(
 79            "permanent_immune_population_fraction_R1",
 80            0,
 81            0.5,
 82        ),
 83        RealParameter(
 84            "permanent_immune_population_fraction_R2",
 85            0,
 86            0.5,
 87        ),
 88        RealParameter("recovery_time_region_1", 0.1, 0.75),
 89        RealParameter("recovery_time_region_2", 0.1, 0.75),
 90        RealParameter("susceptible_to_immune_population_delay_time_region_1", 0.5, 2),
 91        RealParameter("susceptible_to_immune_population_delay_time_region_2", 0.5, 2),
 92        RealParameter("root_contact_rate_region_1", 0.01, 5),
 93        RealParameter("root_contact_ratio_region_2", 0.01, 5),
 94        RealParameter(
 95            "infection_ratio_region_1",
 96            0,
 97            0.15,
 98        ),
 99        RealParameter("infection_rate_region_2", 0, 0.15),
100        RealParameter(
101            "normal_contact_rate_region_1",
102            10,
103            100,
104        ),
105        RealParameter(
106            "normal_contact_rate_region_2",
107            10,
108            200,
109        ),
110    ]
111
112    # add policies
113    policies = [
114        Sample("no policy", model_file=r"FLUvensimV1basecase.vpm"),
115        Sample("static policy", model_file=r"FLUvensimV1static.vpm"),
116        Sample("adaptive policy", model_file=r"FLUvensimV1dynamic.vpm"),
117    ]
118
119    results = perform_experiments(model, 1000, policies=policies)
120    save_results(results, "./data/1000 flu cases with policies.tar.gz")
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/example_vensim_flu.html
