---
title: "Sim Practice Ch 05 S5.2 - Events and Event Graphs"
aliases:
  - "Events and Event Graphs"
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
  - concept
  - application
  - manufacturing
---

# Events and Event Graphs

## Upward links
- [[Simulation in Practice - Source]]
- [[Sim Practice Ch 05 - The Simulation Engine]]

## Summary
Explains how a discrete-event model can be represented as events connected by timing and logic relationships, making the simulation engine easier to reason about.

## Downward links
- [[Event graphs]]
- [[Workstation analysis]]

## Lateral links
- [[Sim Practice Ch 05 S5.1 - Introduction|Introduction]]
- [[Sim Practice Ch 05 S5.3 - Time Advance and Event Lists|Time Advance and Event Lists]]
- [[Sim Practice Ch 05 S5.4 - Simulating the Two Workstation Model|Simulating the Two Workstation Model]]
- [[Sim Practice Ch 05 S5.5 - Organizing Entities Waiting for a Resource|Organizing Entities Waiting for a Resource]]
- [[Sim Practice Ch 05 S5.6 - Random Sampling from Distribution Functions|Random Sampling from Distribution Functions]]
- [[Sim Practice Ch 05 S5.7 - Pseudo-random Number Generation|Pseudo-random Number Generation]]
- [[Sim Practice Ch 05 S5.8 - Summary|Summary]]

## Source highlights
- Event graphs (Schruben, 1983; 1995) are a diagramming technique for showing the events comprising a model. An event graph consists of nodes and arcs. Nodes correspond to events. Arcs tell the relationships between events
- The event graph for the two station serial system is shown in Figure 5-1. There are four state variables: the number in the buffer of each station and the state (busy, idle) of each station. Three events are associated w
- The entity arrives event associated with station A causes itself to occur again, that is the next entity to arrive, after a time interval specified by the time between arrivals. The number in the buffer of workstation A
- The entity arrives event causes the start service event to begin processing the arriving entity immediately if the machine is IDLE. The start service event decreases the number in the buffer of workstation A by 1 and mak

## Reuse note
This section note preserves one stable entry point into the book so later synthesis can link a specific simulation idea, workflow step, or application detail without collapsing everything back into a single chapter summary.
