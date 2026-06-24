---
title: "Sim Practice Ch 12 S12.3.2 - Build Models"
aliases:
  - "Build Models"
category: "source"
book: "Sim Practice"
chapter: "12"
part: "Lean and Beyond Manufacturing"
parent_chapter: "Sim Practice Ch 12 - Flexible Manufacturing Systems"
parent_section: "Sim Practice Ch 12 S12.3 - The Case Study"
tags:
  - source
  - subsection
  - simulation
  - active
  - review
  - decision-support
  - application
  - manufacturing
---

# Build Models

## Upward links
- [[Simulation in Practice - Source]]
- [[Sim Practice Ch 12 - Flexible Manufacturing Systems]]
- [[Sim Practice Ch 12 S12.3 - The Case Study]]

## Summary
Translates the problem into explicit model structure by defining entities, resources, flows, random inputs, and the measurements needed for analysis.

## Downward links
- [[Flexible manufacturing systems]]

## Lateral links
- [[Sim Practice Ch 12 S12.3.1 - Define the Issues and Solution Objective|Define the Issues and Solution Objective]]
- [[Sim Practice Ch 12 S12.3.3 - Identify Root Causes and Assess Initial Alternatives|Identify Root Causes and Assess Initial Alternatives]]
- [[Sim Practice Ch 12 S12.3.4 - Review and Extend Previous Work|Review and Extend Previous Work]]
- [[Sim Practice Ch 12 S12.3.5 - Implement the Selected Solution and Evaluate|Implement the Selected Solution and Evaluate]]
- [[Sim Practice Ch 06 S6.3.2 - Build Models]]
- [[Sim Practice Ch 06 S6.4.2 - Build Models]]
- [[Sim Practice Ch 07 S7.3.2 - Build Models]]
- [[Sim Practice Ch 08 S8.3.2 - Build Models]]
- [[Sim Practice Ch 10 S10.3.2 - Build Models]]
- [[Sim Practice Ch 11 S11.3.2 - Build Models]]
- [[Sim Practice Ch 13 S13.3.2 - Build Models]]
- [[Sim Practice Ch 14 S14.3.2 - Build Models]]
- [[Sim Practice Ch 15 S15.3.2 - Build Models]]
- [[Sim Practice Ch 16 S16.3.2 - Build Models]]
- [[Sim Practice Ch 16 S16.4.1 - Build Models]]
- [[Sim Practice Ch 17 S17.3.2 - Build Models]]
- [[Sim Practice Ch 18 S18.3.2 - Build Models]]

## Source highlights
- The model includes arrivals of batches of parts as well as decomposing the batches into individual parts. Thus, arriving entities represent batches of parts and subsequent entities represent parts. The part entities have
- ArrivalTime = Time of arrival to the FMS PartType = Part type Machine = Machine used in current operation Tool = Tool used in current operation OpTime = Operation time for current operation = f(machine used) CurrentOp =
- The model of an operation on a part requires two resources, one representing a machine and the other a tool. Movement between machines must be included in the model both for parts and tools. An procedure to select the ma
- Each tool resource has an attribute: ToolLocation = The machine on which it currently resides.

## Reuse note
This section note preserves one stable entry point into the book so later synthesis can link a specific simulation idea, workflow step, or application detail without collapsing everything back into a single chapter summary.
