---
title: "Front Matter"
book: "Policy_Analysis_of_Multi-Actor_Systems"
source_pdf: "Policy_Analysis_of_Multi-Actor_Systems.pdf"
tags:
  - pdf-import
  - split-book
---

Policy Analysis
Second Edition
of Multi-Actor
Bert Enserink
Pieter Bots
Els van Daalen
Leon Hermans
Systems
Rens Kortmann
Joop Koppenjan
Jan Kwakkel
Tineke Ruijgh
Jill Slinger
Wil Thissen

Policy Analysis of Multi-Actor Systems

Policy Analysis of
Multi-Actor Systems
Bert Enserink
Pieter Bots
Els van Daalen
Leon Hermans
Rens Kortmann
Joop Koppenjan
Jan Kwakkel
Tineke Ruijgh-van der Ploeg
Jill Slinger
Wil Thissen

Published, sold and distributed by Eleven
P.O. Box 85576
2508 CG The Hague
The Netherlands
Tel.: +31 70 33 070 33
Fax: +31 70 33 070 30
e-mail: sales@elevenpub.nl
www.elevenpub.com
Sold and distributed in USA and Canada
Independent Publishers Group
814 N. Franklin Street
Chicago, IL 60610, USA
Order Placement: +1 800 888 4741
Fax: +1 312 337 5985
orders@ipgbook.com
www.ipgbook.com
Eleven is an imprint of Boom uitgevers Den Haag.
ISBN 978-94-6236-299-4
Online edition 2022 published by TU Delft Open
ISBN: 978-94-6366-575-9 (online)
DOI: https://doi.org/10.5074/T.2022.004
This book is published in open access under licence CC=BY-NC-SA. Without prejudice to the agree-
ments on reproduction rights and the reader regulation, this license allows reusers to distribute,
remix, adapt, and build upon the material in any medium or format for noncommercial purposes
only, and only so long as attribution is given to the creator. If you remix, adapt, or build upon the
material, you must license the modified material under identical terms.
This publication is protected by international copyright law.
All rights reserved. No part of this publication may be reproduced, stored in a retrieval system,
or transmitted in any form or by any means, electronic, mechanical, photocopying, recording or
otherwise, without the prior permission of the publisher.

Preface
Preface to the Second Edition (2022)
In 2020, after ten years of user experience by our teaching staff and thousands of students
practising multi-actor problem structuring, we decided the PA of MAS book needed an
update. In its basis and structure, the book did what it was supposed to do: teach students
how to create order in chaos and to think systems: multi-actor systems. Consequently, this
new edition is not a complete overhaul.
As our own experience as policy analysts and teachers grew, we noticed the synthesis
chapter needed an upgrade; here writing skills and analytical craftsmanship should be
combined to forge a rich problem description allowing for characterization and framing of
the problem. This chapter is the essential link between the analytical part (Chapters 3, 4
and 5) and the actionable part in Chapters 7 and 8 where the plan of action and research
plan are presented, which might culminate in an issue paper in which the framed problem
and envisioned follow-up activities are presented to a potential commissioner.
Moreover, over the last decade, new insights, new analytic methods and new data and
modelling techniques have been gaining ground and some of the examples and issues
presented in the first edition became outdated. The latter were replaced by more recent
examples; but knowing that good examples make happy learners, others were kept as they
convey such clear messages.
One prominent development in the past ten years was the rise of e-publishing, blended
and online teaching and ‘Open Science’. TU Delft has the ambition to make open research
and open education the standard of its scientific practice, and turning this book into an
Open Textbook is part of this ambition. We owe it to the financial and practical support of
TU Delft Open, the Faculty of Technology Policy and Management, and the cooperation
of BOOM Publishers that we can offer this book as Open Textbook, which will make this
book affordable and accessible for many more students. For those preferring a paper copy,
BOOM can provide a printed version.
This second edition, like the first edition, is based on the input of a large group of
engaged colleague policy analysts; four more colleagues joined the team, which now
consists of: Dr P.W.G. (Pieter) Bots, Dr Ir. C. (Els) van Daalen, Dr Ir. B. (Bert) Enserink,
Dr Ir. L.M. (Leon) Hermans, Dr L.J. (Rens) Kortmann, Prof. Dr J.F.M. (Joop) Koppenjan
(EUR), Prof. Dr Ir. J.H. (Jan) Kwakkel, Dr Ir. M.P.M. (Tineke) Ruijgh-van der Ploeg,
Dr J.H. (Jill) Slinger, Prof. Dr Ir. W.A.H. (Wil) Thissen.
Just like the first edition, this second edition will not be the final one; open textbooks
allow for continuous feedback and updating. We hope our readers will continue to send
us critical constructive comments to further improve the book; therefore, we expect that
this book will be alive and kicking for many more years to come.
Bert Enserink
5

Policy AnAlysis of Multi-Actor systeMs
Preface to the First Edition (2010)
This book Policy Analysis of Multi-Actor Systems is the result of interdisciplinary coop-
eration in teaching and learning in courses on problem analysis and problem structuring
methods at bachelor and master level at the Faculty of Technology, Policy and Manage-
ment (TPM) of Delft University of Technology. A first draft was published in 1999 carrying
the Dutch title ‘Analyse van Complexe Omgevingen’.
A first English version dates back to April 2006. A major revision by Bert Enserink,
Leon Hermans and Jan Kwakkel took place in 2008 and the first book version is a new
step in this highly iterative process. Consequently, this book is the product of intensive
interaction and discussions on teaching problem structuring methods amongst TPM
staff members over a period of many years. The main contributors are Dr Ir. B. Enserink,
Dr Ir. L. Hermans, Ir. J. Kwakkel, Prof. Dr Ir. W.A.H. Thissen, Dr J.F.M. Koppenjan and
Dr P.W.G. Bots.
Numerous other colleagues were involved in discussing and defining concepts, revising
texts and teaching classes, including Ir. D.P. Kamps, and Ir. G. Bekebrede, Dr P. Ker Rault,
Dr E.M. van Bueren, Dr Ir. A.R.C. de Haan and Prof Dr W.E. Walker with other colleagues
and students who participated in the course over the years. The current version will not
be the final one as we know that science evolves through constant debate and change. We
therefore welcome any comments.
Bert Enserink
Leon Hermans
Jan Kwakkel
Wil Thissen
Joop Koppenjan
Pieter Bots
6

Table of Contents
1 Introduction 11
1.1 The Challenge of Policy Analysis in Multi-Actor Systems 11
1.2 The Problem Structuring Focus 12
1.2.1 The Policy Process as a Problem-Solving Process 13
1.2.2 Policy Analysis to Support Problem-Solving 14
1.2.3 Policy Problems: Gaps and Dilemmas 16
1.3 Approach Taken and Outline of This Course Book 17
References 19
2 Problem Formulation in Complex Environments 21
2.1 Coping with Complexity 21
2.1.1 Technical Dimension of Problems 23
2.1.2 Social Dimension of Problems 25
2.1.3 Institutional Dimension of Problems 26
2.1.4 Normative Dimension of Problems 28
2.2 Framing Complexity 29
2.2.1 Structured and Unstructured Problems 30
2.2.2 Objective versus Subjective Problems: The Role of Perceptions
and Interests 32
2.2.3 The Problem Formulation Battle 35
2.2.4 The Social Construction of Problems 36
2.3 Problem Formulation as Part of Problem-Solving 36
2.3.1 Garbage Cans and Streams 37
2.3.2 Problem-Solving Following the Streams Model 39
2.3.3 Problem-Solving in Arenas and Rounds 41
2.3.4 Problem-Solving and Advocacy Coalitions 41
2.4 Points of Intervention 43
2.5 Problem Formulation as First Step in Problem Analysis 44
2.6 Takeaways 48
References 48
3 Systems Analysis 53
3.1 Introduction to Systems Analysis 53
3.2 Conceptual Framework for Systems Analysis 54
3.2.1 The System Diagram and Its Components 54
3.2.2 Interests, Objectives, Criteria and Means 56
3.3 A Method to Develop a System Diagram 58
3.3.1 Problem Demarcation: Means-Ends Analysis 59
7

Policy AnAlysis of Multi-Actor systeMs
3.3.2 Specify Objectives and Criteria: Objectives Tree 64
3.4 Mapping Causal Relations 70
3.5 Overview of the System and Its Boundaries: The System Diagram 73
3.5.3 The Multi-Actor Situation 76
3.6 Takeaways 77
References 78
4 Actor Analysis 79
4.1 Introduction: Why Actor Analysis? 79
4.2 Conceptual Framework for Actor Analysis 80
4.3 Methods for Actor Analysis 81
4.4 Steps in Actor Analyses 83
4.4.1 Step 1: Use Problem Formulation and Associated Decision Arena as
Point of Departure 83
4.4.2 Step 2: Make an Inventory of the Actors Involved 85
4.4.3 Step 3: Mapping Formal Institutions and Relations 89
4.4.4 Step 4: Identifying Key Actor Characteristics 92
4.4.5 Step 5: Summarizing Interdependencies 97
4.4.6 Step 6: Confront the Initial Problem Formulation with the Findings 101
4.5 Points of Attention in Actor Analysis 102
4.5.1 Trustworthy Sources of Information 102
4.5.2 Actor Analysis Tries to Hit a Moving Target 103
4.5.3 Some Important Limitations of Actor Analysis 103
4.6 Takeaways 104
References 104
5 Exploring the Future 109
5.1 Introduction 109
5.2 Analysing and Classifying Uncertainties 110
5.3 Overview of Methods for Exploring the Future 112
5.3.1 Formal Methods 112
5.3.2 Consulting Experts 119
5.3.3 Scenarios 123
5.4 Developing Scenarios 126
5.5 Example: Scenario Analysis for Examining Civil Aviation Infrastructure
Options in the Netherlands 130
5.5.1 Step 1: Determine Key Question 130
5.5.2 Step 2: Determine the Contextual Factors 130
5.5.3 Step 3: Cluster the Contextual Factors into Driving Forces 131
5.5.4 Step 4: Classify the Driving Forces According to Their Impact and
Uncertainty 133
5.5.5 Step 5: Design a Scenario Logic 133
5.5.6 Step 6: Detail the Scenario 134
5.5.7 Step 7: Evaluate the Key Question 135
5.6 Beyond Exploring the Future 136
5.7 Takeaways 137
References 137
8

Table of ConTenTs
6 From Synthesis to Plan of Action 141
6.1 System Diagram Revision 143
6.1.1 Consistency Check 145
6.2 Rich Problem Description 145
6.3 Characterizing and Framing the Problem 146
6.4 Knowledge Gaps 147
6.5 The Role of the Analyst 148
6.5.1 Six Types of Policy Analytical Activities 149
6.5.2 Blends of Activities and Roles 150
6.6 Proposing Follow-On Activities 151
6.7 Takeaways 152
References 152
7 The Research Plan 153
7.1 Introduction 153
7.2 Why? – Knowledge Gaps 154
7.3 What? – Research Questions 155
7.4 How? – Research Methods 158
7.4.1 Methods for Definitional Enquiry 159
7.4.2 Methods for Descriptive Enquiry 159
7.4.3 Methods for Relational Enquiry 161
7.4.4 Methods for Explanatory Enquiry 161
7.4.5 Using Models in Research 162
7.4.6 Data Management in Research 164
7.4.7 Involving People in Research 164
7.5 When? Who? – Research Planning 165
7.6 Conclusion 166
7.7 Takeaways 168
References 168
8 Preparing an Issue Paper 171
8.1 Role of an Issue Paper in Policy Analysis 172
8.2 The Key Elements of an Issue Paper 173
8.2.1 Effective Outline for the Issue Paper 173
8.2.2 Demarcation of Initial Problem Situation 174
8.2.3 Mutually Consistent, Partial Analyses of Multi-Actor System 174
8.2.4 Storyline for the ‘Framed Problem’ 175
8.2.5 Recommendations and Related Proposal for a Follow-On Activity 175
8.2.6 Accountability Statement 175
8.2.7 A List of Resources or Bibliography 175
8.2.8 A Convincing Style of Communication 176
8.3 Different Problem Diagnoses, Different Storylines 176
8.4 A Systematic Approach to Preparing Issue Papers 177
8.4.1 Introduction: The Initial Description Problem 178
8.4.2 Description of the ‘Framed Problem’ 179
9

Policy AnAlysis of Multi-Actor systeMs
