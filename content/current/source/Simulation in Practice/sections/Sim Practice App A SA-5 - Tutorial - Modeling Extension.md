---
title: "Sim Practice App A SA-5 - Tutorial - Modeling Extension"
aliases:
  - "Tutorial - Modeling Extension"
category: "source"
book: "Sim Practice"
chapter: "appendix"
part: "Appendices"
parent_chapter: "Sim Practice App - AutoMod Summary and Tutorial for the Chapter 6 Case Study"
parent_section: "Sim Practice App - AutoMod Summary and Tutorial for the Chapter 6 Case Study"
tags:
  - source
  - tutorial
  - simulation
  - active
  - review
  - decision-support
  - tooling
  - application
  - concept
  - validation
  - verification
  - dmdu
  - manufacturing
---

# Tutorial - Modeling Extension

## Upward links
- [[Simulation in Practice - Source]]
- [[Sim Practice App - AutoMod Summary and Tutorial for the Chapter 6 Case Study]]

## Summary
Next close the execution window and return to the model. Save the model under a new name so that the modifications to follow are kept distinct from the original model.

## Downward links
- [[Verification and validation]]
- [[Workstation analysis]]
- [[AutoMod]]

## Lateral links
- [[Sim Practice App A SA.1 - Introduction|Introduction]]
- [[Sim Practice App A SA.2 - AutoMod Modeling Elements|AutoMod Modeling Elements]]
- [[Sim Practice App A SA-3 - Tutorial - Model Building|Tutorial - Model Building]]
- [[Sim Practice App A SA-4 - Tutorial - Model Execution|Tutorial - Model Execution]]
- [[Sim Practice App A SA-6 - Tutorial - Conducting Experiments with AutoStat|Tutorial - Conducting Experiments with AutoStat]]
- [[Sim Practice App A SA-7 - Initialization of State Variables|Initialization of State Variables]]
- [[Sim Practice App A SA-8 - Creating a Trace File in Comma Separated Value (.csv) Format|Creating a Trace File in Comma Separated Value (.csv) Format]]
- [[Sim Practice App A SA-9 - Choose between Two Resources|Choose between Two Resources]]
- [[Sim Practice App B SB.1 - Introduction|Introduction]]
- [[Sim Practice App B SB.2 - Procedures for Fitting Data to Distributions|Procedures for Fitting Data to Distributions]]

## Source highlights
- Next close the execution window and return to the model. Save the model under a new name so that the modifications to follow are kept distinct from the original model.
- The first modification is to model setup and batching at the workstation using the logic described in chapter 6. First determine the batch size using the computations in chapter 6. The enter setup and batching into the m
- 1. Modify P_Arrive to create a batch. Whenever the total number of arrivals to P_Arrive ( **P_Arrive total** ) is a multiple of the batch size, a batch is created. Thus, when a load arrives, test whether or not this cond
- a. If it is NOT met: **wait to be ordered on OL_BatchList // hold load on batch list** b. If it is met: **send to P_WSA**

## Reuse note
This section note preserves one stable entry point into the book so later synthesis can link a specific simulation idea, workflow step, or application detail without collapsing everything back into a single chapter summary.
