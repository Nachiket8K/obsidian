---
title: "Sim Practice Ch 18 S18.3.2 - Build Models"
aliases:
  - "Build Models"
category: "source"
book: "Sim Practice"
chapter: "18"
part: "Material Handling"
parent_chapter: "Sim Practice Ch 18 - Automated Storage and Retrieval"
parent_section: "Sim Practice Ch 18 S18.3 - The Case Study"
tags:
  - source
  - subsection
  - simulation
  - active
  - review
  - decision-support
  - application
  - material-handling
---

# Build Models

## Upward links
- [[Simulation in Practice - Source]]
- [[Sim Practice Ch 18 - Automated Storage and Retrieval]]
- [[Sim Practice Ch 18 S18.3 - The Case Study]]

## Summary
Translates the problem into explicit model structure by defining entities, resources, flows, random inputs, and the measurements needed for analysis.

## Downward links
- [[Automated storage and retrieval]]

## Lateral links
- [[Sim Practice Ch 18 S18.3.1 - Define the Issues and Solution Objective|Define the Issues and Solution Objective]]
- [[Sim Practice Ch 18 S18.3.3 - Identify Root Causes and Assess Initial Alternatives|Identify Root Causes and Assess Initial Alternatives]]
- [[Sim Practice Ch 18 S18.3.4 - Review and Extend Previous Work|Review and Extend Previous Work]]
- [[Sim Practice Ch 18 S18.3.5 - Implement the Selected Solution and Evaluate|Implement the Selected Solution and Evaluate]]
- [[Sim Practice Ch 06 S6.3.2 - Build Models]]
- [[Sim Practice Ch 06 S6.4.2 - Build Models]]
- [[Sim Practice Ch 07 S7.3.2 - Build Models]]
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

## Source highlights
- The two operations performed by the AS/RS system are modeled as two separate processes. The first operation stores a subassembly in a bin. The second retrieves a subassembly from a bin.
- Entities represent subassemblies to be stored or retreived and have five attributes:
- Type = Type of subassembly: 1, 2, 3, 4. ArriveTime = Time of arrival to the AS/RS system. Rack = Rack in which to store the subassembly: 1 or 2. Row = Horizontal position of the bin in which to store the subassembly. Col
- A state variable is used to track the state of each bin:: idle, filled with a subassembly of a particular type, or filled with a subassembly of a particular type that is committed to the second manufacturing process. In

## Reuse note
This section note preserves one stable entry point into the book so later synthesis can link a specific simulation idea, workflow step, or application detail without collapsing everything back into a single chapter summary.
