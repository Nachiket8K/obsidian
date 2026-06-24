---
title: The Classic Transportation Problem
aliases:
  - "[AM-05-042] The Classic Transportation Problem"
  - AM-05-042
category: source
source_type: living-textbook-topic
book: "GIS&T Body of Knowledge"
topic_code: AM-05-042
domain_code: AM
domain_name: Analytics and Modeling
raw_source_path: "GIS&T Body of Knowledge/AM Analytics and Modeling/AM-05-042 The Classic Transportation Problem.md"
tags:
  - source
  - giscience
  - geospatial
  - active
  - review
  - simulation
  - decision-support
  - python-gis
---

# The Classic Transportation Problem

## Upward links
- [[GIS&T Body of Knowledge - Source]]
- [[current/source/GIS&T Body of Knowledge/UCGIS GIS&T Body of Knowledge|Mirrored GIS&T overview]]
- [[current/source/GIS&T Body of Knowledge/AM Analytics and Modeling/AM Analytics and Modeling|AM Analytics and Modeling]]

## Summary
The classic transportation problem concerns minimizing the cost of transporting a product from sources/supplies to destinations/demands. It is a network-flow problem that arises in industrial logistics and is often solved by linear programming (LP). The three inputs of the model are total units produced at each source, total units needed at each destination, and the cost to transport one unit from each source to each destination. And the objective is to minimize the total cost of transporting all units produced at sources to meet the demands at destinations. The problem solution includes three basic steps: 1) finding an initial basic feasible solution, 2) checking if the current solution is optimal (with the lowest costs), and improving the current solution through iteration. Solving such a problem relies strongly on the network data models, least-cost path algorithms, other functionalities in GIS. And an integrated framework is often adopted to utilize both GIS and non-GIS linear programming solvers to search for the optimal solution.

## Downward links
- Learning outcome: 291 - Define the classic transportation problem analytically using graphs,equations, and matrices.
- Learning outcome: 310 - Delineate three major steps toward solving the classic transportation problem as a linear program and use simplex methods to get the optimal solution.
- Learning outcome: 337 - Demonstrate how to model real-world transportation problems as linear programs.
- Learning outcome: 479 - Describe some main contributions of GIS to the classic transportation problem.
- Learning outcome: 910 - Distinguish between balanced and unbalanced problems, and explain why, if supply equals demand, there will always be a feasible solution.

## Related GIS&T topics
- [AM-05-043] Location and Service Area Problems
- [AM-05-044] Modelling Accessibility
- [AM-05-046] Location-allocation modeling
- [FC-04-019] Networks

## Lateral links
- None added yet.

## Traceability
- Raw note: [[GIS&T Body of Knowledge/AM Analytics and Modeling/AM-05-042 The Classic Transportation Problem|Raw GIS&T topic]]
- Mirrored from: `GIS&T Body of Knowledge/AM Analytics and Modeling/AM-05-042 The Classic Transportation Problem.md`
- Topic code: `AM-05-042`
