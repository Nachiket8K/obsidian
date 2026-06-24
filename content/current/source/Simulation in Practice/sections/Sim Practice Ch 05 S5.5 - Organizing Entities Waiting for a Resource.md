---
title: "Sim Practice Ch 05 S5.5 - Organizing Entities Waiting for a Resource"
aliases:
  - "Organizing Entities Waiting for a Resource"
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
  - application
  - manufacturing
---

# Organizing Entities Waiting for a Resource

## Upward links
- [[Simulation in Practice - Source]]
- [[Sim Practice Ch 05 - The Simulation Engine]]

## Summary
Explains how waiting entities are organized when a required resource is unavailable, making queue discipline part of the model’s operational logic.

## Downward links
- [[Workstation analysis]]

## Lateral links
- [[Sim Practice Ch 05 S5.1 - Introduction|Introduction]]
- [[Sim Practice Ch 05 S5.2 - Events and Event Graphs|Events and Event Graphs]]
- [[Sim Practice Ch 05 S5.3 - Time Advance and Event Lists|Time Advance and Event Lists]]
- [[Sim Practice Ch 05 S5.4 - Simulating the Two Workstation Model|Simulating the Two Workstation Model]]
- [[Sim Practice Ch 05 S5.6 - Random Sampling from Distribution Functions|Random Sampling from Distribution Functions]]
- [[Sim Practice Ch 05 S5.7 - Pseudo-random Number Generation|Pseudo-random Number Generation]]
- [[Sim Practice Ch 05 S5.8 - Summary|Summary]]

## Source highlights
- Notice from the discussion in section 5.2 that there is either zero or one event occurrence on the event list corresponding to each entity. If there is no event occurrence, the entity is waiting usually for a resource to
- Entities wait for a resource that is currently not in the idle state in an ordered list similar to the event list. When a unit of the resource completes its current task or otherwise becomes idle, it will process the fir
- Suppose entities in the two workstation model have the following attributes:
- 1. Time of arrival to the system

## Reuse note
This section note preserves one stable entry point into the book so later synthesis can link a specific simulation idea, workflow step, or application detail without collapsing everything back into a single chapter summary.
