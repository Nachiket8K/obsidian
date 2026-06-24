---
title: "Sim Practice Ch 05 S5.6 - Random Sampling from Distribution Functions"
aliases:
  - "Random Sampling from Distribution Functions"
category: "source"
book: "Sim Practice"
chapter: "5"
part: "Introduction and Methods"
parent_chapter: "Sim Practice Ch 05 - The Simulation Engine"
parent_section: "Sim Practice Ch 05 - The Simulation Engine"
tags:
  - source
  - section
  - simulation
  - active
  - review
  - decision-support
  - method
  - simulation-engine
  - events
  - randomness
  - application
  - manufacturing
---

# Random Sampling from Distribution Functions

## Upward links
- [[Simulation in Practice - Source]]
- [[Sim Practice Ch 05 - The Simulation Engine]]

## Summary
Shows how individual stochastic values are generated from probability distributions so entity attributes, arrivals, and processing times can vary from case to case.

## Downward links
- [[Inverse-transformation method]]
- [[Workstation analysis]]

## Lateral links
- [[Sim Practice Ch 05 S5.1 - Introduction|Introduction]]
- [[Sim Practice Ch 05 S5.2 - Events and Event Graphs|Events and Event Graphs]]
- [[Sim Practice Ch 05 S5.3 - Time Advance and Event Lists|Time Advance and Event Lists]]
- [[Sim Practice Ch 05 S5.4 - Simulating the Two Workstation Model|Simulating the Two Workstation Model]]
- [[Sim Practice Ch 05 S5.5 - Organizing Entities Waiting for a Resource|Organizing Entities Waiting for a Resource]]
- [[Sim Practice Ch 05 S5.7 - Pseudo-random Number Generation|Pseudo-random Number Generation]]
- [[Sim Practice Ch 05 S5.8 - Summary|Summary]]

## Source highlights
- In chapter 2, entity attribute values and the time between entity arrivals as well as operation and transportation times were modeled using probability distributions. Furthermore, values for these variables need to be as
- Consider the time between entity arrivals in the two workstations in a series model: exponential (10) seconds, where 10 is the average time between arrivals, TBA. This quantity follows the cumulative distribution functio
- y = F(x) = 1 - e[- x / TBA] = 1 - e[- x / 10]
- x = -TBA ln (1 - y) = -10 ln (1-y)

## Reuse note
This section note preserves one stable entry point into the book so later synthesis can link a specific simulation idea, workflow step, or application detail without collapsing everything back into a single chapter summary.
