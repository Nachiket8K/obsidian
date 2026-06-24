---
title: "Agent activation"
category: "concept"
tags:
  - concept
  - mesa
  - agent-based-modeling
  - simulation
  - adaptive-policy
  - active
  - review
---

# Agent activation

## Upward links
- [[Mesa Documentation - Source]]

## Summary
Agent activation describes the order and pattern by which agents act during a simulation. In Mesa, activation design is an important modelling choice because sequential, random, staged, and conditional activation can lead to different emergent outcomes.

## Downward links
- [[Python Library Documentation/Mesa/getting started|Mesa getting started]]
- [[Python Library Documentation/Mesa/tutorials/2 agent activation|Mesa tutorial: agent activation]]

## Key points
- Activation order is not a technical detail; it can change model behaviour.
- Mesa supports sequential, random, staged, type-based, and callable-driven activation.
- Activation design is part of the model structure and should be justified like any other modelling assumption.

## Lateral links
- [[AgentSet]]
- [[Event scheduling (Mesa)]]
- [[System dynamics]]
- [[Exploratory modeling]]

## Reuse note
This note is useful whenever activation order, scheduling logic, or micro-level behavioural assumptions affect interpretation of a model.
