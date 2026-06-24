---
title: "Sim Practice Ch 07 S7.3.2 - Build Models"
aliases:
  - "Build Models"
category: "source"
book: "Sim Practice"
chapter: "7"
part: "Basic Organizations for Systems"
parent_chapter: "Sim Practice Ch 07 - Serial Lines"
parent_section: "Sim Practice Ch 07 S7.3 - The Case Study"
tags:
  - source
  - subsection
  - simulation
  - active
  - review
  - decision-support
  - application
  - manufacturing
  - tooling
---

# Build Models

## Upward links
- [[Simulation in Practice - Source]]
- [[Sim Practice Ch 07 - Serial Lines]]
- [[Sim Practice Ch 07 S7.3 - The Case Study]]

## Summary
Translates the problem into explicit model structure by defining entities, resources, flows, random inputs, and the measurements needed for analysis.

## Downward links
- [[Serial lines]]
- [[Workstation analysis]]
- [[AutoMod]]

## Lateral links
- [[Sim Practice Ch 07 S7.3.1 - Define the Issues and Solution Objective|Define the Issues and Solution Objective]]
- [[Sim Practice Ch 07 S7.3.3 - Identify Root Causes and Assess Initial Alternatives|Identify Root Causes and Assess Initial Alternatives]]
- [[Sim Practice Ch 07 S7.3.4 - Review and Extend Previous Work|Review and Extend Previous Work]]
- [[Sim Practice Ch 07 S7.3.5 - Implement the Selected Solution and Evaluate|Implement the Selected Solution and Evaluate]]
- [[Sim Practice Ch 06 S6.3.2 - Build Models]]
- [[Sim Practice Ch 06 S6.4.2 - Build Models]]
- [[Sim Practice Ch 08 S8.3.2 - Build Models]]
- [[Sim Practice Ch 10 S10.3.2 - Build Models]]
- [[Sim Practice Ch 11 S11.3.2 - Build Models]]
- [[Sim Practice Ch 12 S12.3.2 - Build Models]]
- [[Sim Practice Ch 13 S13.3.2 - Build Models]]
- [[Sim Practice Ch 14 S14.3.2 - Build Models]]
- [[Sim Practice Ch 15 S15.3.2 - Build Models]]
- [[Sim Practice Ch 16 S16.3.2 - Build Models]]
- [[Sim Practice Ch 16 S16.4.1 - Build Models]]
- [[Sim Practice Ch 17 S17.3.2 - Build Models]]
- [[Sim Practice Ch 18 S18.3.2 - Build Models]]

## Source highlights
- The model of the serial system includes the arrival process for circuit cards, operations at the three stations, and tray movement into and out of the two inter-station buffers.
- There are four entity attributes. One entity attribute is arrival time to the system, ArrivalTime. The other three entity attributes store the operation times for that particular entity at each station.
- Assigning all operating times when the entity arrives assures that the first entity has the first operating time sample at each station, the second the second and so forth. This assignment is the best way to ensure that
- The processing of a circuit card tray at the deposition station is done in the following way. A circuit card tray uses the station when the latter becomes idle. The operation is performed. The circuit card tray then must

## Reuse note
This section note preserves one stable entry point into the book so later synthesis can link a specific simulation idea, workflow step, or application detail without collapsing everything back into a single chapter summary.
