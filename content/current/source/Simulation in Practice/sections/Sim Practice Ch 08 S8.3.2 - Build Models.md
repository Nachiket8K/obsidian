---
title: "Sim Practice Ch 08 S8.3.2 - Build Models"
aliases:
  - "Build Models"
category: "source"
book: "Sim Practice"
chapter: "8"
part: "Basic Organizations for Systems"
parent_chapter: "Sim Practice Ch 08 - Job Shops"
parent_section: "Sim Practice Ch 08 S8.3 - The Case Study"
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
- [[Sim Practice Ch 08 - Job Shops]]
- [[Sim Practice Ch 08 S8.3 - The Case Study]]

## Summary
Translates the problem into explicit model structure by defining entities, resources, flows, random inputs, and the measurements needed for analysis.

## Downward links
- [[Job shops]]
- [[Workstation analysis]]

## Lateral links
- [[Sim Practice Ch 08 S8.3.1 - Define the Issues and Solution Objective|Define the Issues and Solution Objective]]
- [[Sim Practice Ch 08 S8.3.3 - Identify Root Causes and Assess Initial Alternatives|Identify Root Causes and Assess Initial Alternatives]]
- [[Sim Practice Ch 08 S8.3.4 - Review and Extend Previous Work|Review and Extend Previous Work]]
- [[Sim Practice Ch 06 S6.3.2 - Build Models]]
- [[Sim Practice Ch 06 S6.4.2 - Build Models]]
- [[Sim Practice Ch 07 S7.3.2 - Build Models]]
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
- The model of the job shop uses the following logic:
- 1. A job arrives as modeled in the arrival process.
- 2. The job is routed according to the routing process. A. If the job needs more operations, it is sent to the station corresponding to its next operation.
- B. If the job has completed all operations, its lead time is computed and the service level for this job recorded. Then the job leaves the shop. Note that the service level is either 100 for acceptable (less than 8 hours

## Reuse note
This section note preserves one stable entry point into the book so later synthesis can link a specific simulation idea, workflow step, or application detail without collapsing everything back into a single chapter summary.
