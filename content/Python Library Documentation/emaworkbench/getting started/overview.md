---
title: "A High Level Overview"
source: "https://emaworkbench.readthedocs.io/en/latest/getting_started/overview.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# A High Level Overview

> - [Exploratory modeling framework](#emframework)
> - [Connectors](#connectors)
> - [Analysis](#analysis)

## Exploratory modeling framework

The core package contains the core functionality for setting up, designing,
and performing series of computational experiments on one or more models
simultaneously.

- Model ([`ema_workbench.em_framework.model`](../ema_documentation/em_framework/model.html#module-ema_workbench.em_framework.model "ema_workbench.em_framework.model")): an abstract base class for
  specifying the interface to the model on which you want to perform
  exploratory modeling.
- Samplers ([`ema_workbench.em_framework.samplers`](../ema_documentation/em_framework/samplers.html#module-ema_workbench.em_framework.samplers "ema_workbench.em_framework.samplers")): the various sampling
  techniques that are readily available in the workbench.
- Uncertainties ([`ema_workbench.em_framework.parameters`](../ema_documentation/em_framework/parameters.html#module-ema_workbench.em_framework.parameters "ema_workbench.em_framework.parameters")): various
  types of parameter classes that can be used to specify the uncertainties
  and/or levers on the model
- Outcomes ([`ema_workbench.em_framework.outcomes`](../ema_documentation/em_framework/outcomes.html#module-ema_workbench.em_framework.outcomes "ema_workbench.em_framework.outcomes")): various types
  of outcome classes
- Evaluators ([`ema_workbench.em_framework.evaluators`](../ema_documentation/em_framework/evaluators.html#module-ema_workbench.em_framework.evaluators "ema_workbench.em_framework.evaluators")): various evaluators
  for running experiments in sequence or in parallel.

## Connectors

The connectors package contains connectors to some existing simulation modeling
environments. For each of these, a standard ModelStructureInterface class is
provided that users can use as a starting point for specifying the interface
to their own model.

- Vensim connector (`ema_workbench.connectors.vensim`): This enables
  controlling (e.g. setting parameters, simulation setup, run, get output, etc
  .) a simulation model that is built in Vensim software, and conducting an
  EMA study based on this model.
- Excel connector ([`ema_workbench.connectors.excel`](../ema_documentation/connectors/excel.html#module-ema_workbench.connectors.excel "ema_workbench.connectors.excel")): This enables
  controlling models build in Excel.
- NetLogo connector (`ema_workbench.connectors.netlogo`): This enables
  controlling (e.g. setting parameters, simulation setup, run, get output, etc
  .) a simulation model that is built in NetLogo software, and conducting an
  EMA study based on this model.
- Simio connector (`ema_workbench.connectors.simio_connector`): This
  enables controlling models built in Simio
- Pysd connector (`ema_workbench.connectors.pysd_connector`)

## Analysis

The analysis package contains a variety of analysis and visualization
techniques for analyzing the results from the exploratory modeling. The
analysis scripts are tailored for use in combination with the workbench, but
they can also be used on their own with data generated in some other manner.

- Patient Rule Induction Method ([`ema_workbench.analysis.prim`](../ema_documentation/analysis/prim.html#module-ema_workbench.analysis.prim "ema_workbench.analysis.prim"))
- Classification Trees ([`ema_workbench.analysis.cart`](../ema_documentation/analysis/cart.html#module-ema_workbench.analysis.cart "ema_workbench.analysis.cart"))
- Logistic Regression ([`ema_workbench.analysis.logistic_regression`](../ema_documentation/analysis/logistic_regression.html#module-ema_workbench.analysis.logistic_regression "ema_workbench.analysis.logistic_regression"))
- Dimensional Stacking ([`ema_workbench.analysis.dimensional_stacking`](../ema_documentation/analysis/dimensional_stacking.html#module-ema_workbench.analysis.dimensional_stacking "ema_workbench.analysis.dimensional_stacking"))
- Feature Scoring ([`ema_workbench.analysis.feature_scoring`](../ema_documentation/analysis/feature_scoring.html#module-ema_workbench.analysis.feature_scoring "ema_workbench.analysis.feature_scoring"))
- Regional Sensitivity Analysis ([`ema_workbench.analysis.regional_sa`](../ema_documentation/analysis/regional_sa.html#module-ema_workbench.analysis.regional_sa "ema_workbench.analysis.regional_sa"))
- various plotting functions for time series data ([`ema_workbench.analysis.plotting`](../ema_documentation/analysis/plotting.html#module-ema_workbench.analysis.plotting "ema_workbench.analysis.plotting"))
- pair wise plots ([`ema_workbench.analysis.pairs_plotting`](../ema_documentation/analysis/pairs_plotting.html#module-ema_workbench.analysis.pairs_plotting "ema_workbench.analysis.pairs_plotting"))
- parallel coordinate plots ([`ema_workbench.analysis.parcoords`](../ema_documentation/analysis/parcoords.html#module-ema_workbench.analysis.parcoords "ema_workbench.analysis.parcoords"))
- support for converting figures to black and white (`ema_workbench.analysis.b_an_w_plotting`)

---

Original source: https://emaworkbench.readthedocs.io/en/latest/getting_started/overview.html
