---
title: "Robust search"
category: "method"
tags:
  - method
  - emaworkbench
  - robust-optimization
  - simulation
  - dmdu
  - active
  - review
---

# Robust search

## Upward links
- [[EMA Workbench Documentation - Source]]

## Summary
A robustness-oriented search method that evaluates candidate strategies across sets of scenarios and optimizes robustness metrics instead of single-scenario performance.

## Downward links
- [[Python Library Documentation/emaworkbench/indepth tutorial/directed-search|Directed search tutorial]]
- [[Python Library Documentation/emaworkbench/examples/robust optimization lake model dps|Robust optimization lake model DPS]]
- [[Python Library Documentation/emaworkbench/examples/optimization convergence analysis|Optimization convergence analysis]]

## Core ideas
- Define robustness metrics that aggregate model outcomes across many scenarios.
- Keep a scenario ensemble fixed during optimization so strategies can be compared consistently.
- Use many-objective optimization to expose trade-offs between alternative notions of robustness.
- Interpret robust solutions as candidates for DMDU-style deliberation rather than as final prescriptions.

## Lateral links
- [[Policy robustness]]
- [[Directed search]]
- [[Robust Decision Making (RDM)]]
- [[Adaptive planning]]
- [[Open exploration]]

## Reuse note
Use this note as the canonical bridge between computational optimization workflows and DMDU notions of robustness, adaptivity, and strategy comparison.