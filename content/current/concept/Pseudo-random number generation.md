---
title: "Pseudo-random number generation"
aliases:
  - "pseudo-random number generation"
  - "pseudorandom number generation"
  - "random number streams"
category: "concept"
tags:
  - concept
  - simulation
  - randomness
  - active
  - review
---

# Pseudo-random number generation

## Upward links
- [[Simulation in Practice - Source]]

## Summary
The computational basis for producing repeatable streams of random-looking values in simulation models. It matters because experimental reproducibility depends on well-managed streams.

## Downward links
- [[Sim Practice Ch 04 S4.4 - Common Design Elements]]
- [[Sim Practice Ch 04 - Conducting Simulation Experiments]]
- [[Sim Practice Ch 04 S4.5.4 - Design Summary]]
- [[Sim Practice Ch 04 S4.7.2 - Comparison by Statistical Analysis]]
- [[Sim Practice Ch 05 S5.7 - Pseudo-random Number Generation]]
- [[Sim Practice Ch 05 - The Simulation Engine]]
- [[Sim Practice Ch 05 S5.8 - Summary]]
- [[Sim Practice Ch 06 S6.3.3.2 - Simulation Analysis of the Single Workstation]]
- [[Sim Practice Ch 06 - The Workstation]]
- [[Sim Practice Ch 07 S7.3.3 - Identify Root Causes and Assess Initial Alternatives]]
- [[Sim Practice Ch 07 - Serial Lines]]
- [[Sim Practice Ch 08 S8.3.3 - Identify Root Causes and Assess Initial Alternatives]]
- [[Sim Practice Ch 08 - Job Shops]]
- [[Sim Practice Ch 10 S10.3.3 - Identify Root Causes and Assess Initial Alternatives]]
- [[Sim Practice Ch 10 - Inventory Control using Kanbans]]
- [[Sim Practice Ch 11 S11.3.2 - Build Models]]
- [[Sim Practice Ch 11 - Cellular Manufacturing]]
- [[Sim Practice Ch 12 S12.3.3 - Identify Root Causes and Assess Initial Alternatives]]
- [[Sim Practice Ch 12 - Flexible Manufacturing Systems]]
- [[Sim Practice Ch 13 S13.3.3 - Identify Root Causes and Assess Initial Alternatives]]
- [[Sim Practice Ch 13 - Automated Inventory Management]]
- [[Sim Practice Ch 14 S14.3.3 - Identify Root Causes and Assess Initial Alternatives]]
- [[Sim Practice Ch 14 - Logistics]]
- [[Sim Practice Ch 15 S15.3.3 - Identify Root Causes and Assess Initial Alternatives]]
- [[Sim Practice Ch 15 - Integrated Supply Chains]]
- [[Sim Practice Ch 16 S16.3.3 - Identify Root Causes and Assess Initial Alternatives]]
- [[Sim Practice Ch 16 - Transfer Hubs]]
- [[Sim Practice Ch 18 S18.3.3 - Identify Root Causes and Assess Initial Alternatives]]
- [[Sim Practice Ch 18 - Automated Storage and Retrieval]]

## Key points
- Conducting Simulation Experiments / Common Design Elements: The elements common to all simulation experiments are discussed in the following sections. These include model parameters and their values, performance measures, and random number streams.
- Conducting Simulation Experiments / Design Summary: The specification of design elements for a terminating simulation experiment can be accomplished by completing the template shown in Table 4-1. **Table 4-1: Terminating Simulation Experiment Design**
- Conducting Simulation Experiments / Comparison by Statistical Analysis: This section discusses the use of confidence intervals to confirm that perceived differences in the simulation results for two scenarios are not just due to random variation in the experim
- The Simulation Engine / Pseudo-random Number Generation: All of the random sampling strategies discussed in the previous section require a random sample uniformly distributed in the range (0,1). Fortunately, there are several well known algorithms for generati
- The Simulation Engine / Summary: This chapter discusses the basic operations of a simulation engine. While these operations are performed transparently to the modeler, an understanding of them helps clarify how simulation experiments work.
- The Workstation / Simulation Analysis of the Single Workstation: Summarizes how the simulation experiment is configured and interpreted so the analytic reasoning can be checked against replicated model output.

## Lateral links
- [[Inverse-transformation method]]
- [[Simulation experiments]]
- [[Workstation analysis]]
- [[Verification and validation]]
- [[Event graphs]]
- [[Serial lines]]
- [[Job shops]]
- [[Little's Law]]
- [[VUT equation]]
- [[Kanban systems]]
- [[Inventory control]]
- [[Cellular manufacturing]]
- [[Flexible manufacturing systems]]
- [[Automated inventory management]]
- [[Supply chain logistics]]
- [[Transfer hubs]]
- [[Automated storage and retrieval]]

## Reuse note
This canonical note is meant to absorb cross-links from multiple books so reusable simulation knowledge is enriched rather than duplicated.
