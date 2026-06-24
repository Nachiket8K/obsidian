---
title: "Sim Practice Ch 02 S2.3.3 - Routing Entities"
aliases:
  - "Routing Entities"
category: "source"
book: "Sim Practice"
chapter: "2"
part: "Introduction and Methods"
parent_chapter: "Sim Practice Ch 02 - Simulation Model Building"
parent_section: "Sim Practice Ch 02 S2.3 - Models of System Components"
tags:
  - source
  - subsection
  - simulation
  - active
  - review
  - decision-support
  - method
  - model-building
  - application
  - manufacturing
---

# Routing Entities

## Upward links
- [[Simulation in Practice - Source]]
- [[Sim Practice Ch 02 - Simulation Model Building]]
- [[Sim Practice Ch 02 S2.3 - Models of System Components]]

## Summary
In many systems, decisions must be made about the routing of entities from operation to operation. This section discusses typical ways systems make such routing decisions as well as techniques for modeling them.

## Downward links
- [[Job shops]]
- [[Workstation analysis]]

## Lateral links
- [[Sim Practice Ch 02 S2.3.1 - Arrivals|Arrivals]]
- [[Sim Practice Ch 02 S2.3.4 - Batching|Batching]]
- [[Sim Practice Ch 02 S2.3.5 - Inventories|Inventories]]

## Source highlights
- In many systems, decisions must be made about the routing of entities from operation to operation. This section discusses typical ways systems make such routing decisions as well as techniques for modeling them. A distin
- Consider a system that processes multiple item types using several workstations. Each workstation performs a unique function. Each job type is operated on by a unique sequence of workstations called a route. In a manufac
- Each entity in the model of a job shop organization could have the following attributes:
- ArrivalTime: Time of arrival Type: The type of job, which implies the route. Location: The current location on the route relative to the beginning of the route.

## Reuse note
This section note preserves one stable entry point into the book so later synthesis can link a specific simulation idea, workflow step, or application detail without collapsing everything back into a single chapter summary.
