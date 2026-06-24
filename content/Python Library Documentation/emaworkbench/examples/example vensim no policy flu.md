---
title: "example_vensim_no_policy_flu.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/example_vensim_no_policy_flu.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# example\_vensim\_no\_policy\_flu.py

```
  1"""No policy example of flu model.
  2
  3This module shows how you can use vensim models directly
  4instead of coding the model in Python. The underlying case
  5is the same as used in fluExample
  6
  7"""
  8
  9from ema_workbench import (
 10    MultiprocessingEvaluator,
 11    RealParameter,
 12    TimeSeriesOutcome,
 13    ema_logging,
 14    perform_experiments,
 15    save_results,
 16)
 17from ema_workbench.connectors.vensim import VensimModel
 18
 19# Created on 20 May, 2011
 20#
 21# .. codeauthor:: jhkwakkel <j.h.kwakkel (at) tudelft (dot) nl>
 22#                 epruyt <e.pruyt (at) tudelft (dot) nl>
 23
 24
 25if __name__ == "__main__":
 26    ema_logging.log_to_stderr(ema_logging.INFO)
 27
 28    model = VensimModel(
 29        "flu", wd=r"./models/flu", model_file=r"FLUvensimV1basecase.vpm"
 30    )
 31
 32    # outcomes
 33    model.outcomes = [
 34        TimeSeriesOutcome("deceased_population_region_1"),
 35        TimeSeriesOutcome("infected_fraction_R1"),
 36    ]
 37
 38    # Plain Parametric Uncertainties
 39    model.uncertainties = [
 40        RealParameter(
 41            "additional_seasonal_immune_population_fraction_R1",
 42            0,
 43            0.5,
 44        ),
 45        RealParameter(
 46            "additional_seasonal_immune_population_fraction_R2",
 47            0,
 48            0.5,
 49        ),
 50        RealParameter(
 51            "fatality_ratio_region_1",
 52            0.0001,
 53            0.1,
 54        ),
 55        RealParameter(
 56            "fatality_rate_region_2",
 57            0.0001,
 58            0.1,
 59        ),
 60        RealParameter(
 61            "initial_immune_fraction_of_the_population_of_region_1",
 62            0,
 63            0.5,
 64        ),
 65        RealParameter(
 66            "initial_immune_fraction_of_the_population_of_region_2",
 67            0,
 68            0.5,
 69        ),
 70        RealParameter(
 71            "normal_interregional_contact_rate",
 72            0,
 73            0.9,
 74        ),
 75        RealParameter(
 76            "permanent_immune_population_fraction_R1",
 77            0,
 78            0.5,
 79        ),
 80        RealParameter(
 81            "permanent_immune_population_fraction_R2",
 82            0,
 83            0.5,
 84        ),
 85        RealParameter("recovery_time_region_1", 0.1, 0.75),
 86        RealParameter("recovery_time_region_2", 0.1, 0.75),
 87        RealParameter(
 88            "susceptible_to_immune_population_delay_time_region_1",
 89            0.5,
 90            2,
 91        ),
 92        RealParameter(
 93            "susceptible_to_immune_population_delay_time_region_2",
 94            0.5,
 95            2,
 96        ),
 97        RealParameter(
 98            "root_contact_rate_region_1",
 99            0.01,
100            5,
101        ),
102        RealParameter(
103            "root_contact_ratio_region_2",
104            0.01,
105            5,
106        ),
107        RealParameter(
108            "infection_ratio_region_1",
109            0,
110            0.15,
111        ),
112        RealParameter("infection_rate_region_2", 0, 0.15),
113        RealParameter(
114            "normal_contact_rate_region_1",
115            10,
116            100,
117        ),
118        RealParameter(
119            "normal_contact_rate_region_2",
120            10,
121            200,
122        ),
123    ]
124
125    nr_experiments = 1000
126    with MultiprocessingEvaluator(model) as evaluator:
127        results = perform_experiments(model, nr_experiments, evaluator=evaluator)
128
129    save_results(results, "./data/1000 flu cases no policy.tar.gz")
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/example_vensim_no_policy_flu.html
