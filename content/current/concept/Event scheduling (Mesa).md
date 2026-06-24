---
title: "Event scheduling (Mesa)"
category: "concept"
tags:
  - concept
  - mesa
  - event-scheduling
  - simulation
  - dmdu
  - system-dynamics
  - active
  - review
---

# Event scheduling (Mesa)

## Upward links
- [[Mesa Documentation - Source]]

## Summary
Event scheduling in Mesa supports one-off and recurring events that can occur at specific simulation times, including between standard agent steps. This makes Mesa useful for hybrid models that combine agent activation with policy changes, shocks, interventions, or other timed processes.

## Downward links
- [[Python Library Documentation/Mesa/apis/time|Mesa time API]]
- [[Python Library Documentation/Mesa/apis/model|Mesa model API]]
- [[Python Library Documentation/Mesa/tutorials/3 event scheduling|Mesa tutorial: event scheduling]]

## Key points
- Events can be scheduled at absolute or relative times.
- Mesa supports recurring events and event priority.
- Event scheduling is a strong bridge to adaptive interventions, scenario timing, and policy experiments.

## Lateral links
- [[Agent activation]]
- [[Adaptive policies]]
- [[Monitor-and-adapt]]
- [[Policy testing (system dynamics)]]
- [[Exploratory modeling]]

## Reuse note
Use this note whenever timing, interventions, or hybrid event-driven simulation are important to the argument or implementation.
