---
title: "Sim Practice Ch 05 S5.4 - Simulating the Two Workstation Model"
aliases:
  - "Simulating the Two Workstation Model"
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
  - validation
  - verification
  - dmdu
  - application
  - manufacturing
---

# Simulating the Two Workstation Model

## Upward links
- [[Simulation in Practice - Source]]
- [[Sim Practice Ch 05 - The Simulation Engine]]

## Summary
Uses a trace-style walkthrough to show how the simulation engine processes a concrete model step by step over time.

## Downward links
- [[Verification and validation]]
- [[Workstation analysis]]

## Lateral links
- [[Sim Practice Ch 05 S5.1 - Introduction|Introduction]]
- [[Sim Practice Ch 05 S5.2 - Events and Event Graphs|Events and Event Graphs]]
- [[Sim Practice Ch 05 S5.3 - Time Advance and Event Lists|Time Advance and Event Lists]]
- [[Sim Practice Ch 05 S5.5 - Organizing Entities Waiting for a Resource|Organizing Entities Waiting for a Resource]]
- [[Sim Practice Ch 05 S5.6 - Random Sampling from Distribution Functions|Random Sampling from Distribution Functions]]
- [[Sim Practice Ch 05 S5.7 - Pseudo-random Number Generation|Pseudo-random Number Generation]]
- [[Sim Practice Ch 05 S5.8 - Summary|Summary]]

## Source highlights
- This section discusses and illustrates the record of the time ordered sequence of events that are processed by a simulation engine for a particular model. This record is called a **trace** and includes the changes in sta
- Consider one possible simulation of the two workstations in sequence model. Let’s follow the sequence of events processed in time order when only one entity moves through the two workstations, assuming that no other enti
- The trace for the simulation with one entity is shown Table 5-1. Only the new values of state variables whose values are changed by an event are shown. At the start of the simulation there are no entities in the model, t
- ## **Table 5-1: Simulation Trace for One Entity**

## Reuse note
This section note preserves one stable entry point into the book so later synthesis can link a specific simulation idea, workflow step, or application detail without collapsing everything back into a single chapter summary.
