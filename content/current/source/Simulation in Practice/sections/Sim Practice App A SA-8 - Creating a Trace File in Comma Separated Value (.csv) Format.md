---
title: "Sim Practice App A SA-8 - Creating a Trace File in Comma Separated Value (.csv) Format"
aliases:
  - "Creating a Trace File in Comma Separated Value (.csv) Format"
category: "source"
book: "Sim Practice"
chapter: "appendix"
part: "Appendices"
parent_chapter: "Sim Practice App - AutoMod Summary and Tutorial for the Chapter 6 Case Study"
parent_section: "Sim Practice App - AutoMod Summary and Tutorial for the Chapter 6 Case Study"
tags:
  - source
  - appendix
  - simulation
  - active
  - review
  - decision-support
  - tooling
  - application
  - manufacturing
---

# Creating a Trace File in Comma Separated Value (.csv) Format

## Upward links
- [[Simulation in Practice - Source]]
- [[Sim Practice App - AutoMod Summary and Tutorial for the Chapter 6 Case Study]]

## Summary
Consider the model of a single workstation with no detractors as described in section III above. Suppose a trace of all state changes: from idle to busy as well as from busy to idle is desired.

## Downward links
- [[Workstation analysis]]
- [[AutoMod]]

## Lateral links
- [[Sim Practice App A SA.1 - Introduction|Introduction]]
- [[Sim Practice App A SA.2 - AutoMod Modeling Elements|AutoMod Modeling Elements]]
- [[Sim Practice App A SA-3 - Tutorial - Model Building|Tutorial - Model Building]]
- [[Sim Practice App A SA-4 - Tutorial - Model Execution|Tutorial - Model Execution]]
- [[Sim Practice App A SA-5 - Tutorial - Modeling Extension|Tutorial - Modeling Extension]]
- [[Sim Practice App A SA-6 - Tutorial - Conducting Experiments with AutoStat|Tutorial - Conducting Experiments with AutoStat]]
- [[Sim Practice App A SA-7 - Initialization of State Variables|Initialization of State Variables]]
- [[Sim Practice App A SA-9 - Choose between Two Resources|Choose between Two Resources]]
- [[Sim Practice App B SB.1 - Introduction|Introduction]]
- [[Sim Practice App B SB.2 - Procedures for Fitting Data to Distributions|Procedures for Fitting Data to Distributions]]

## Source highlights
- Consider the model of a single workstation with no detractors as described in section III above. Suppose a trace of all state changes: from idle to busy as well as from busy to idle is desired. This trace is to be writte
- The following example shows how to open .csv file in the model initialization function and write the column headers to the file.
- begin model initialization function
- // open the trace file; note that the variable V_TraceFile is of type file ptr (pointer)

## Reuse note
This section note preserves one stable entry point into the book so later synthesis can link a specific simulation idea, workflow step, or application detail without collapsing everything back into a single chapter summary.
