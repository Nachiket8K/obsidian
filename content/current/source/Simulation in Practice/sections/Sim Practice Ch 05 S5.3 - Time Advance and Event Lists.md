---
title: "Sim Practice Ch 05 S5.3 - Time Advance and Event Lists"
aliases:
  - "Time Advance and Event Lists"
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

# Time Advance and Event Lists

## Upward links
- [[Simulation in Practice - Source]]
- [[Sim Practice Ch 05 - The Simulation Engine]]

## Summary
Describes how a discrete-event simulation advances through simulated time by processing the next scheduled event on the event list.

## Downward links
- [[Workstation analysis]]

## Lateral links
- [[Sim Practice Ch 05 S5.1 - Introduction|Introduction]]
- [[Sim Practice Ch 05 S5.2 - Events and Event Graphs|Events and Event Graphs]]
- [[Sim Practice Ch 05 S5.4 - Simulating the Two Workstation Model|Simulating the Two Workstation Model]]
- [[Sim Practice Ch 05 S5.5 - Organizing Entities Waiting for a Resource|Organizing Entities Waiting for a Resource]]
- [[Sim Practice Ch 05 S5.6 - Random Sampling from Distribution Functions|Random Sampling from Distribution Functions]]
- [[Sim Practice Ch 05 S5.7 - Pseudo-random Number Generation|Pseudo-random Number Generation]]
- [[Sim Practice Ch 05 S5.8 - Summary|Summary]]

## Source highlights
- This section discusses how the simulation proceeds through time by scheduling event occurrences and processing each of them in turn. In general, a model is simulated as a time ordered sequence of the occurrences of the e
- The **event list** is the time ordered list of all event occurrences scheduled at the current time and in the future. The simulation proceeds by removing the first event occurrence on the list and processing it. This pro
- For the two workstation model, the simulation engine must deal with six events that change the values of the state variables. Each of these events must be scheduled in time and processed. These events are the arrival of
- At any point in time, the event list could contain the following event occurrences at future points in time:

## Reuse note
This section note preserves one stable entry point into the book so later synthesis can link a specific simulation idea, workflow step, or application detail without collapsing everything back into a single chapter summary.
