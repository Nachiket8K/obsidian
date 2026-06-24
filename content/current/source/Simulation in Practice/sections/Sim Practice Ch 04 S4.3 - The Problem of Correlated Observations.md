---
title: "Sim Practice Ch 04 S4.3 - The Problem of Correlated Observations"
aliases:
  - "The Problem of Correlated Observations"
category: "source"
book: "Sim Practice"
chapter: "4"
part: "Introduction and Methods"
parent_chapter: "Sim Practice Ch 04 - Conducting Simulation Experiments"
parent_section: "Sim Practice Ch 04 - Conducting Simulation Experiments"
tags:
  - source
  - section
  - simulation
  - active
  - review
  - decision-support
  - method
  - experimentation
  - validation
  - dmdu
  - application
  - manufacturing
---

# The Problem of Correlated Observations

## Upward links
- [[Simulation in Practice - Source]]
- [[Sim Practice Ch 04 - Conducting Simulation Experiments]]

## Summary
Most statistical analysis procedures require independent (and identically distributed) observations of performance measure values. However, the observations in a simulation experiment are typically dependent (correlated).

## Downward links
- [[Simulation experiments]]
- [[Workstation analysis]]

## Lateral links
- [[Sim Practice Ch 04 S4.1 - Introduction|Introduction]]
- [[Sim Practice Ch 04 S4.2 - Verification and Validation|Verification and Validation]]
- [[Sim Practice Ch 04 S4.4 - Common Design Elements|Common Design Elements]]
- [[Sim Practice Ch 04 S4.5 - Design Elements Specific to Terminating Simulation Experiments|Design Elements Specific to Terminating Simulation Experiments]]
- [[Sim Practice Ch 04 S4.6 - Examining the Results for a Single Scenario|Examining the Results for a Single Scenario]]
- [[Sim Practice Ch 04 S4.7 - Comparing Scenarios|Comparing Scenarios]]
- [[Sim Practice Ch 04 S4.8 - Summary|Summary]]

## Source highlights
- Most statistical analysis procedures require independent (and identically distributed) observations of performance measure values. However, the observations in a simulation experiment are typically dependent (correlated)
- Consider the time the nth part arriving to workstation A in the two stations in a series model would spend at the workstation:
- Time at workstation An = Time in buffern + Operation timen
- The time in the buffer for the nth part is composed of the operation times for the parts that preceded it in processing while the nth part was in the buffer. For example, suppose the fourth part to arrive does so while t

## Reuse note
This section note preserves one stable entry point into the book so later synthesis can link a specific simulation idea, workflow step, or application detail without collapsing everything back into a single chapter summary.
