---
title: "Sim Practice App A SA-9 - Choose between Two Resources"
aliases:
  - "Choose between Two Resources"
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
---

# Choose between Two Resources

## Upward links
- [[Simulation in Practice - Source]]
- [[Sim Practice App - AutoMod Summary and Tutorial for the Chapter 6 Case Study]]

## Summary
Explains a resource-selection pattern that can be reused when an entity must choose among alternative resource options in an implementation model.

## Downward links
- [[AutoMod]]

## Lateral links
- [[Sim Practice App A SA.1 - Introduction|Introduction]]
- [[Sim Practice App A SA.2 - AutoMod Modeling Elements|AutoMod Modeling Elements]]
- [[Sim Practice App A SA-3 - Tutorial - Model Building|Tutorial - Model Building]]
- [[Sim Practice App A SA-4 - Tutorial - Model Execution|Tutorial - Model Execution]]
- [[Sim Practice App A SA-5 - Tutorial - Modeling Extension|Tutorial - Modeling Extension]]
- [[Sim Practice App A SA-6 - Tutorial - Conducting Experiments with AutoStat|Tutorial - Conducting Experiments with AutoStat]]
- [[Sim Practice App A SA-7 - Initialization of State Variables|Initialization of State Variables]]
- [[Sim Practice App A SA-8 - Creating a Trace File in Comma Separated Value (.csv) Format|Creating a Trace File in Comma Separated Value (.csv) Format]]
- [[Sim Practice App B SB.1 - Introduction|Introduction]]
- [[Sim Practice App B SB.2 - Procedures for Fitting Data to Distributions|Procedures for Fitting Data to Distributions]]

## Source highlights
- Suppose an operation can be performed by either of two resources, R_MachineA or R_MachineB. The first resource with one unit in the idle state will be used. If both are available R_MachineA will be use. The following pro
- wait until R_MachineA remaining > 0 or R_MachineB remaining > 0 // wait for a machine if R_MachineA remaining > 0 then
- set A_Machine = R_MachineA // Machine A is available end else begin set A_Machine = R_MachineB // Only Machine B is available end
- get A_Machine // get selected machine wait for 15 min // perform operation free A_Machine // free selected machine

## Reuse note
This section note preserves one stable entry point into the book so later synthesis can link a specific simulation idea, workflow step, or application detail without collapsing everything back into a single chapter summary.
