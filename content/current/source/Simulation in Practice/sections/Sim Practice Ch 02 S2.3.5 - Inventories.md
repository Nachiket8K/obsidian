---
title: "Sim Practice Ch 02 S2.3.5 - Inventories"
aliases:
  - "Inventories"
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
---

# Inventories

## Upward links
- [[Simulation in Practice - Source]]
- [[Sim Practice Ch 02 - Simulation Model Building]]
- [[Sim Practice Ch 02 S2.3 - Models of System Components]]

## Summary
In many systems, items are produced and stored for subsequent use. A collection of such stored items is called an inventory, for example televisions waiting in a store for purchase or hamburgers under the hot lamp at a fast food restaurant.

## Downward links
- None yet

## Lateral links
- [[Sim Practice Ch 02 S2.3.1 - Arrivals|Arrivals]]
- [[Sim Practice Ch 02 S2.3.3 - Routing Entities|Routing Entities]]
- [[Sim Practice Ch 02 S2.3.4 - Batching|Batching]]

## Source highlights
- In many systems, items are produced and stored for subsequent use. A collection of such stored items is called an inventory, for example televisions waiting in a store for purchase or hamburgers under the hot lamp at a f
- Inventory processes have to do with adding items to an inventory and removing items from an inventory. The number of items in an inventory can be modeled using a state variable, for example INV_LEVEL. Placing an item in
- 1. Wait for an item to be in the inventory: WAIT UNTIL INV_LEVEL > 0
- 2. Subtract one from the number of items in the inventory: INV_LEVEL -= 1

## Reuse note
This section note preserves one stable entry point into the book so later synthesis can link a specific simulation idea, workflow step, or application detail without collapsing everything back into a single chapter summary.
