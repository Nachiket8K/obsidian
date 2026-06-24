---
title: "Directed search"
category: "method"
tags:
  - method
  - emaworkbench
  - optimization
  - simulation
  - dmdu
  - active
  - review
---

# Directed search

## Upward links
- [[EMA Workbench Documentation - Source]]

## Summary
An optimization-oriented exploratory modeling method that searches decision or uncertainty spaces in a guided way in order to find promising strategies, worst cases, or trade-off surfaces.

## Downward links
- [[Python Library Documentation/emaworkbench/getting started/overview|EMA Workbench overview]]
- [[Python Library Documentation/emaworkbench/indepth tutorial/directed-search|Directed search tutorial]]
- [[Python Library Documentation/emaworkbench/examples/optimization lake model dps|Optimization lake model DPS]]
- [[Python Library Documentation/emaworkbench/examples/optimization lake model intertemporal|Optimization lake model intertemporal]]
- [[Python Library Documentation/emaworkbench/examples/optimization convergence analysis|Optimization convergence analysis]]

## Core ideas
- Replace purely passive sampling with guided search over levers, uncertainties, or both.
- Make objective direction explicit so the search reflects the decision problem rather than raw model output.
- Track convergence and repeat search across seeds because evolutionary optimization is stochastic.
- Use search outputs as candidate strategies for later robustness testing and interpretation.

## Lateral links
- [[Open exploration]]
- [[Robust search]]
- [[Policy robustness]]
- [[Robust Decision Making (RDM)]]
- [[Feature scoring]]
- [[System dynamics modelling]]

## Reuse note
Use this as the canonical note for optimization-based exploratory studies, including many-objective search over policies and uncertainty spaces.