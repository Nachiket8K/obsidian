---
title: "Vadere EMA connector demo"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/vadere_demo.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# Vadere EMA connector demo

This notebook demonstrates the setup of a Vadere model connection. It uses an example Vadere model, made with Vadere 2.1. Before running the code yourself, please acquire a copy of Vadere from [the official Vadere website](https://www.vadere.org/download/). For more information on the use of the EMA Workbench, please refer to the [official EMA Workbench documentation](https://emaworkbench.readthedocs.io/en/latest/). This demo is based on the code provided on the documentation pages.

## Step 1: imports

The first step is to import the needed modules. This depends on the use and the type of analysis that is intended. The most important one here is the VadereModel from the model connectors. As said, please refer for more information on this to the [official EMA Workbench documentation](https://emaworkbench.readthedocs.io/en/latest/).

```
[ ]:
```

```
import numpy as np
import pandas as pd

from ema_workbench import (
    IntegerParameter,
    MultiprocessingEvaluator,
    RealParameter,
    Samplers,
    ScalarOutcome,
    ema_logging,
    perform_experiments,
)
from ema_workbench.connectors.vadere import VadereModel
```

## Step 2: Setting up the model

In this demonstration, we use a simple Vadere model example. The model includes two sources and one target, and spawns a number of pedestrians every second. The model uses the OSM locomotion implementation, and collects the following:

- The average evacuation time -> stored in evacuationTime.txt
- The average speed of all pedestrians each time step -> stored in speed.csv

Note that the EMA connector assumes .txt files for scalar outcomes and .csv files for time series outcomes. Pleasure use these file types, and declare them explicitly in processor\_files as shown below.

```
[2]:
```

```
# This model saves scalar results to a density.txt and speed.txt file.
# Please acquire your own copy of Vadere, and place the vadere-console.jar in your model/scenarios directory
# Note that the vadere model files and the console.jar should always be placed in a separate wd as the python runfile
model = VadereModel(
    "demoModel",
    vadere_jar="vadere-console.jar",
    processor_files=["evacuationTime.txt", "speed.csv"],
    model_file="demo.scenario",
    wd="models/vadereModel/scenarios/",
)
```

```
[3]:
```

```
# set the number of replications to handle model stochasticity
model.replications = 5
```

Note that for specifying model uncertainties (and potential levers), the Vadere model class can change any variable present in the model file (Vadere scenario). To realize this, an exact location to the variable of interest in the Vadere scenario file has to be specified. Vadere scenario files follow a nested dictionary structure. Therefore, the exact location of the variable should be passed in a list of argumentes, passed as one string.

See the example below, that variates the following:

- The number of spawned pedestrians from both sources
- The mean of the free flow speed distribution

```
[4]:
```

```
model.uncertainties = [
    IntegerParameter(
        name="spawnNumberA",
        lower_bound=1,
        upper_bound=50,
        variable_name=['("scenario", "topography", "sources", 0, "spawnNumber")'],
    ),
    IntegerParameter(
        name="spawnNumberB",
        lower_bound=1,
        upper_bound=50,
        variable_name=['("scenario", "topography", "sources", 1, "spawnNumber")'],
    ),
    RealParameter(
        name="μFreeFlowSpeed",
        lower_bound=0.7,
        upper_bound=1.5,
        variable_name=[
            '("scenario", "topography", "attributesPedestrian", "speedDistributionMean")'
        ],
    ),
]
```

The model outcomes can be specified by passing the exact name as present in the output file (speed.txt here). The naming convention depends on the used Vadere data processors, but usually follows the name + id of the processor. When in doubt, it is advised to do a demo Vadere run using the Vadere software and to inspect the generated output files. Note that we take the mean of the outcomes here, since we specified multiple replications. Note that we now only focus on scalar outcomes. See the end
of this demo for timeseries.

```
[5]:
```

```
model.outcomes = [
    ScalarOutcome(
        name="evacuationTime", variable_name="meanEvacuationTime-PID8", function=np.mean
    )
]
```

## Step 3: Performing experiments

The last step is to perform experiment with the Vadere model. Both sequential runs as runs in parallel are supported. Note however that a Vadere run can use a lot of RAM, and using all available CPU cores can lead to performance issues in some cases. Additionally, one Vadere run is by default already multithreaded. It is therefore recommended to not use the full set of available processes.

```
[6]:
```

```
# enable EMA logging
ema_logging.log_to_stderr(ema_logging.INFO)
```

```
[6]:
```

```
<Logger EMA (DEBUG)>
```

```
[7]:
```

```
# run in sequential 2 experiments
results_sequential = perform_experiments(
    model, scenarios=2, uncertainty_sampling=Samplers.LHS
)
```

```
[MainProcess/INFO] performing 2 scenarios * 1 policies * 1 model(s) = 2 experiments
  0%|                                                    | 0/2 [00:00<?, ?it/s][MainProcess/INFO] performing experiments sequentially
100%|████████████████████████████████████████████| 2/2 [01:03<00:00, 31.75s/it]
[MainProcess/INFO] experiments finished
```

```
[8]:
```

```
# run 6 experiments in parallel
with MultiprocessingEvaluator(model, n_processes=-1) as evaluator:
    experiments, outcomes = evaluator.perform_experiments(
        scenarios=4, uncertainty_sampling=Samplers.LHS
    )
```

```
[MainProcess/INFO] pool started with 4 workers
[MainProcess/INFO] performing 4 scenarios * 1 policies * 1 model(s) = 4 experiments
100%|████████████████████████████████████████████| 4/4 [00:37<00:00,  9.39s/it]
[MainProcess/INFO] experiments finished
[MainProcess/INFO] terminating pool
[ForkPoolWorker-1/INFO] finalizing
[ForkPoolWorker-4/INFO] finalizing
[ForkPoolWorker-3/INFO] finalizing
[ForkPoolWorker-2/INFO] finalizing
```

## Inspect the results

we can now look at the results directly. For more extensive exploratory analysis methods, please refer to the [official EMA Workbench documentation](https://emaworkbench.readthedocs.io/en/latest/).

```
[9]:
```

```
experiments.head()
```

```
[9]:
```

|  | spawnNumberA | spawnNumberB | μFreeFlowSpeed | scenario | policy | model |
| --- | --- | --- | --- | --- | --- | --- |
| 0 | 25.0 | 33.0 | 0.838960 | 2 | None | demoModel |
| 1 | 46.0 | 19.0 | 1.413804 | 3 | None | demoModel |
| 2 | 28.0 | 11.0 | 0.942684 | 4 | None | demoModel |
| 3 | 2.0 | 50.0 | 1.111305 | 5 | None | demoModel |

```
[10]:
```

```
pd.DataFrame(outcomes).head()
```

```
[10]:
```

|  | evacuationTime |
| --- | --- |
| 0 | 14.268966 |
| 1 | 9.990154 |
| 2 | 11.673846 |
| 3 | 11.155385 |

## Using time series data

It is additionally possible to specify time series output data. See below for an example on how to do this.

Note that this example now uses a different model class, since we do not want to average multiple scalar outcomes but are rather interested in a time series outcome. Hence, the SingleReplicationVadereModel is used. Now, the timeStep and average speeds are collected every step.

```
[11]:
```

```
from ema_workbench import TimeSeriesOutcome
from ema_workbench.connectors.vadere import SingleReplicationVadereModel
```

```
[12]:
```

```
# This model saves scalar results to a density.txt and speed.txt file.
# Please acquire your own copy of Vadere, and place the vadere-console.jar in your model/scenarios directory
# Note that the vadere model files should always be placed in a separate wd as the python runfile
model = SingleReplicationVadereModel(
    "demoModel",
    vadere_jar="vadere-console.jar",
    processor_files=["evacuationTime.txt", "speed.csv"],
    model_file="demo.scenario",
    wd="models/vadereModel/scenarios/",
)
```

```
[13]:
```

```
model.uncertainties = [
    IntegerParameter(
        name="spawnNumberA",
        lower_bound=1,
        upper_bound=50,
        variable_name=['("scenario", "topography", "sources", 0, "spawnNumber")'],
    ),
    IntegerParameter(
        name="spawnNumberB",
        lower_bound=1,
        upper_bound=50,
        variable_name=['("scenario", "topography", "sources", 1, "spawnNumber")'],
    ),
    RealParameter(
        name="μFreeFlowSpeed",
        lower_bound=0.7,
        upper_bound=1.5,
        variable_name=[
            '("scenario", "topography", "attributesPedestrian", "speedDistributionMean")'
        ],
    ),
]
```

```
[14]:
```

```
model.outcomes = [TimeSeriesOutcome(name="speedTime", variable_name="areaSpeed-PID5")]
```

```
[15]:
```

```
# Run experiments in parallel with all logical CPU cores except one
with MultiprocessingEvaluator(model, n_processes=-1) as evaluator:
    experiments, outcomes = evaluator.perform_experiments(
        scenarios=4, uncertainty_sampling=Samplers.LHS
    )
```

```
[MainProcess/INFO] pool started with 4 workers
[MainProcess/INFO] performing 4 scenarios * 1 policies * 1 model(s) = 4 experiments
100%|████████████████████████████████████████████| 4/4 [00:07<00:00,  1.90s/it]
[MainProcess/INFO] experiments finished
[MainProcess/INFO] terminating pool
[ForkPoolWorker-8/INFO] finalizing
[ForkPoolWorker-5/INFO] finalizing
[ForkPoolWorker-6/INFO] finalizing
[ForkPoolWorker-7/INFO] finalizing
```

```
[16]:
```

```
from ema_workbench.analysis.plotting import lines

lines(experiments, outcomes, outcomes_to_show="speedTime")
```

```
[16]:
```

```
(<Figure size 432x288 with 1 Axes>,
 {'speedTime': <AxesSubplot:title={'center':'speedTime'}, xlabel='Time', ylabel='speedTime'>})
```

![../_images/examples_vadere_demo_23_1.png](../_images/examples_vadere_demo_23_1.png)

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/vadere_demo.html
