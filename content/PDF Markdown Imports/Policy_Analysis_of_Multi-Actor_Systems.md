---
title: "Policy_Analysis_of_Multi-Actor_Systems"
source_pdf: "Policy_Analysis_of_Multi-Actor_Systems.pdf"
converted_with: "markitdown"
tags:
  - pdf-import
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
8.4.3 Conclusions and Recommendations 179
8.4.4 Proposal for Follow-On Action or Research Plan 180
References 180
Annex 181
About the Authors 187
10

noitcudortnI
1 Introduction
Policy analysis in multi-actor systems. Now what
‘If you have only four fingers on does that mean?
one hand, that’s not a problem,
that is a situation.’ To start with policy analysis: although it can mean
Kingdon, 1984 various things to various people in various situ-
ations, we can say that ‘policy analysis’ is about
‘Successful problem solving using analytical tools and a systematic way of
requires finding the right solution working to support policy-making processes. For
to the right problem. We fail more instance, we can use analysis to inform policy-
often because we solve the wrong makers and decision-makers about the pros and
problem than because we get cons of different policy alternatives or we can use
the wrong solution to the right a systematic approach to support various parties
problem.’ in reaching an agreement on a suitable policy as
Russell L. Ackoff, 1974 (on cit) a future course of action to address a problem.
In this chapter, we will explain how policy analysis
contributes to problem-solving, and we position
this book in the scientific debate on problem structuring during the initial stages of the
policy analysis process.
1.1 The Challenge of Policy Analysis in Multi-Actor Systems
This book places policy analysis in a multi-actor environment. This means that it addresses
policy problems and policy processes that involve multiple actors (‘parties’), who are typi-
cally organized in a network rather than in a classic hierarchy. This means that no single
actor will be able to unilaterally impose their desired solution on others, but rather that
some form of cooperation between parties is required. Therefore we talk about multi-
actor systems. In such a setting, complications quickly arise. Typically, different actors will
have different views of a situation. They may not agree on what the main problem is, they
may not accept the same forms of evidence as ‘facts’, they are almost certain to subscribe
to different priorities and preferences for particular solutions and they may have different
opinions about what is fair and just in policy-making. Any one of these multiple actors is
likely to change views over time. Moreover, if these actors are addressing a problem that is
characterized by complexity and uncertainty, then how do we go about supporting policy-
makers and decision-makers, as policy analysts?
11

Introduction
Policy AnAlysis of Multi-Actor systeMs
Text box 1.1 Example of the involvement of many actors
In the area of water management and water policies, we can see that at the international
level there is not one single UN agency responsible for water, but rather that it is handled
by UN-Water, an umbrella agency that includes a multitude of UN organizations (see:
www.unwater.org/). On a national level, in the Netherlands for example, the national water
plan is the joint responsibility of different ministries (see: www.platformparticipatie.nl/
nationaalwaterprogramma/nationaalwaterprogramma_/default.aspx). Each of these ministries
has its own priorities in terms of water using sectors to be served, and water problems to be
solved. Increased flood risks due to climate change; insufficient water for agriculture, industry
and nature; pollution, by industry, agriculture or households; water needs for recreation and
tourism; siltation of fresh water resources, where nature and human uses are at odds. What
problems take priority, in what locations and how to solve these problems? If these national
ministries want to implement their plans, they need the cooperation of a whole range of
other organizations, not least the regional authorities such as water boards, provinces and
municipalities.
In the end, even with many actors and different interests, policy decisions and plans have
to be made. Not doing anything is also a decision, which may not be in everyone’s best
interest either. The question is: how to support decision-makers and other stakeholders
with meaningful analysis? In this book we provide readers with an answer to this question.
1.2 The Problem Structuring Focus
Our point of departure is a systematic way (i.e. done according to a plan; methodical) of
analysing a problem situation which we call problem structuring. The principal objective
of this book is to offer tools and approaches for problem structuring that help to create
a clear picture of complex situations and to mark out a path for supporting the process
towards a policy decision. We call the product that results from the activity of problem
structuring a (rich) problem description. It is important to distinguish the process/activity
from the product/outcome. Problem formulation, i.e. the structuring of a problem, is an
activity fundamental to the problem-solving process.
A poorly structured problem creates the risk of a failure to recognize an urgent or
impending problem in time, thus making it more difficult and more expensive to find a
solution. Incorrect structuring may result in selection of the wrong solution, which will not
alleviate the problem. It is even conceivable that an admirable solution will be designed
and implemented to solve a problem that did not exist.
12

noitcudortnI
1 InTroduCTIon
Text box 1.2 Examples of the consequences of inadequate problem structuring
Some solutions do not solve a problem at all, like the many schools constructed in rural
areas in Latin American and African countries in places where there are no teachers. In such
situations problem structuring has not been performed or it has been done in too limited
a way, which has led to solutions that focus on school buildings rather than also taking into
account teaching capacity.
A common example of a solution for a problem that does not exist or creates a new problem is
the construction of infrastructure where there is no real need or use. The so-called ‘Betuwelijn’,
a rail line dedicated to transport heavy goods and containers by train from Rotterdam Harbour
in the Netherlands to Germany to warrant Rotterdam’s position as an international hub for
container transport, is an example of failing infrastructure. In their enthusiasm the Dutch
built 160 km of rail line, which were ready in 2007, but forgot about the 70 km of new rail line
needed in Germany to connect their line to the German rail system. Construction of the latter
part is currently expected to be finished in 2026. Consequently the Betuwelijn does not reach
its full capacity and its exploitation is leading to big financial losses. Although traffic has been
gaining traction, many heavy trains are following the old routes, causing nuisance in the urban
areas they are passing through.
In this chapter, we will examine the question of what a problem actually is. Although fail-
ures may seem obvious in hindsight, it is not easy to conduct problem structuring well.
We will show the difficulties that arise during attempts to define the nature and content of
problems and we will position ourselves in the field of policy analysis (Thissen & Walker,
2013).
It is important to recognize that a policy analysis process and a policy process are not the
same. The policy process is the context in which a policy analyst operates. The policy
analyst needs to be aware of this context when advising policy or decision-makers who are
faced with a policy problem. The policy analyst conducts an analysis process in support
of a policy process.
1.2.1 The Policy Process as a Problem-Solving Process
According to Nobel Prize winner Herbert Simon (1977, 1991), people solve problems in
four steps: intelligence, design, choice and implementation. ‘Intelligence’ involves gath-
ering information, identifying a problem and examining the problem situation. ‘Design’
entails developing alternative solutions that are possible. ‘Choice’ means selecting an
alternative from the available solutions. ‘Implementation’ puts the selected alternative
into effect. These four steps form the basis for numerous attempts to conceptualize deci-
sion-making, problem-solving and design processes in wide-ranging disciplines.
A policy process can be seen as a problem-solving cycle consisting of stages during
which a policy problem is addressed. Many different representations of such a policy cycle
can be found in the literature, but the general idea is similar. Figure 1.1 shows a representa-
tion of the public policy cycle consisting of four subprocesses that take place continuously
(arrows). Every subprocess involves two types of actors (shown in rectangles).
• Agenda setting: citizens raise issues so that they will be brought to the attention by
politicians in the political arena as policy problems.
13

Introduction
PolICy analysIs of mulTI-aCTor sysTems
• Decision-making: politicians decide, after deliberation, negotiation and formal deci-
sion procedures, on policies that are to be implemented by government.
• Policy implementation: administrators translate policies to more specifi c formal rules
and guidelines that are implemented by executive agencies.
• Policy impact: the execution of new rules by public servants will lead to societal eff ects
which may be perceived as problematic by some societal stakeholders. This will lead
to the next policy cycle requiring a new policy decision.
Although the policy cycle is illustrated here for public policy-making, it can be translated
to policy processes in other contexts.
ci�zens
public servants poli�cians
administrators
Figure 1.1 Cyclical representation of a policy process
The activities of a policy analyst can be aligned with a perspective of the policy process
as a problem-solving cycle consisting of stages (Jann & Wegrich, 2017). Supporting the
policy process thus implies conducting activities that support this problem-solving cycle.
In Chapter 2 we will see that actual policy processes are more complex than presented
here by means of the policy cycle framework. The main message, however, is that the
policy analyst supports a policy process and that the policy analysis process, i.e. the activi-
ties of the policy analyst, takes place in the context of the policy process.
1.2.2 Policy Analysis to Support Problem-Solving
A policy analyst can support any subprocess of the policy cycle. Policy analysis conducted
prior to decision-making is termed ex ante policy analysis, and policy analysis conducted
following a policy decision is termed ex post policy analysis. The ex ante activities will
usually be conducted to support the decision-making subprocess and ex post activities
are usually conducted as evaluation activities of the eff ects of implementing a specifi c
policy. However, agenda setting and implementation may also be supported by policy
analysis.
Articles and textbooks on policy analysis often distinguish a number of phases accord-
ing to which a systematic policy analysis process is conducted. Table 1.1 shows the steps
identifi ed by a number of authors in this fi eld.
14

noitcudortnI
1 InTroduCTIon
Table 1.1 Policy analysis as a sequence of steps
Bardach (2000) Walker (2000) Patton et al. (2012)
Define the problem Identify the problem Verify, define and detail the problem
Assemble some evidence Identify the objectives of the new Establish evaluation criteria
policy
Construct the alternatives Decide on the criteria with which to Identify alternative policies
evaluate alternative policies
Select the criteria Select the alternative policies to be Evaluate alternative policies
evaluated
Project the outcomes Analyse each alternative Display and distinguish among alterna-
tive policies
Confront the trade-offs Compare the alternatives in terms of Monitor and evaluate the implemented
projected costs and effects policy
Decide Implement the chosen alternatives
Tell your story
Although there are differences in the activities that are defined by different authors, the
general sequence is similar. It can be seen that Walker (2000) and Patton et al. (2012)
include both ex ante as well as ex post policy analysis in their steps. In general, during the
policy analysis process the policy problem is explored in some detail in order to clarify
the problem situation. It is also necessary to determine what would be considered to be a
successful solution to the policy problem. This is done by identifying criteria for success.
In addition, various candidate solutions (i.e. alternative policies) are selected and evalu-
ated. This enables the choice of a policy, which has to be monitored and evaluated after
implementation.
The summaries of activities in Table 1.1 suggest a chronology, but the authors consider
them to be important activities, which are not necessarily taken in exactly that order. In
practice, the policy analysis process is regarded as a cycle in which numerous iterations
are possible.
This book focuses on ex ante policy analysis to support the early phases of decision-
making. In the terminology by Simon (1977), the policy analyst supports decision-makers
with intelligence and initial design. In the sequence of the stepwise policy analysis activi-
ties shown earlier, we roughly consider the first iterations of the steps up until a qualitative
evaluation of alternative policies in order to provide an overview of the trade-offs involved.
What sets this book apart from other texts on ex ante policy analysis is an emphasis on
the multi-actor perspective, hence the title Policy Analysis of Multi-Actor Systems. What also
distinguishes this book is that specific attention is given to supporting decision- making
under uncertainty. In many policy problems there are significant uncertainties about the
current situation and about how the situation may develop over time, and decisions have
to be made despite of and in light of these uncertainties. This multi-actor perspective and
attention for decision-making under uncertainty are reflected in the tools and techniques
that are presented and/or the way in which these can be utilized. Over the course of the
book we will see that the activities that can be conducted by the policy analyst are more
varied than the style of policy support described here in this introductory chapter.
15

Introduction
Policy AnAlysis of Multi-Actor systeMs
1.2.3 Policy Problems: Gaps and Dilemmas
Before addressing the complexities and the specifics involved in supporting the early
phases of decision-making in order to address policy problems, we first need to specify
what we mean when we speak of a policy problem. The definition that we will use is
adapted from earlier definitions by Hoogerwerf (1987) and others. We speak of a policy
problem if two conditions are met:
1. There is a gap between an existing or expected situation and a desired situation.
2. There is a dilemma: there is a difficult choice between possibilities that can (partly)
close the gap but that also have undesirable outcomes.
In other words, there needs to be a gap, as well as some perspective of a possible, if par-
tial, solution. If there is a gap, but no solution, there is no policy problem, only a situation
(refer to the citation from Kingdon, 1984, at the beginning of this chapter).
Most decisions concerning implementing measures, or creating or modifying facilities
or projects, are driven by a desire to solve problems, or at the very least to make them
controllable. Before making such decisions, it is important to know precisely what the
problem is that you are planning to address.
Contrary to what one might expect, it is often far from clear what problem a certain
decision or plan should solve and how. Even if a problem may seem clear, it is important
to beware that certain solutions may lead to new problems.
Text box 1.3 Examples of solutions possibly leading to new problems
China is finishing the construction of a canal system to channel more than 40 billion cubic
metres of fresh water annually from the Yangtze River in southern China to the more arid and
industrialized north, where there is a huge shortage of fresh water sources. Will this South-
North water transfer solve the water problem in the North-Eastern provinces? What about
the increased evaporation and the 330,000 people that had to be relocated? How will this
diversion impact on the water balance and the water quality in the southern part of China?
Biofuels and biomass energy are used as alternative sources of energy. Are biofuels and
biomass energy sustainable and reducing our CO emissions, or are they drivers for new
2
problems such as higher emissions, deforestation and rising food prices?
To determine the desirability of a solution, it is important to understand different aspects
of a problem. To that end it is necessary to appropriately structure the problem.
An additional complication is that in reality, actors often do not agree upon what the
actual problem is. They each have their own objectives and their own ideas about what the
desired situation should be.
Text box 1.4 Example of different perceptions on a problem
A crowded airport may be perceived as a capacity problem of the airport, as a noise nuisance
problem, as a problem related to CO emissions, as a safety threat or more than one of these.
2
The range of potential solutions that will be considered strongly depends on the way in which
the problem is structured. The issue of scale also plays an important role. Are the problems at
the airport seen as a local problem, a national problem or an international problem? This will
16

noitcudortnI
1 InTroduCTIon
also influence the solution space. This does not only hold for geographical scale. The problems
at the airport can be seen as related to air transport only or to transport and mobility issues in
general, which will also have consequences for the types of solutions that are considered.
This raises the question of how the analyst, in the midst of all these problem percep-
tions, can come up with a useful problem description (see, for instance, Thissen, 2000;
Wildavsky, 1979). Therefore we need to have insight into what the concept ‘problem’ actu-
ally means, what analysing or structuring a problem really is and which mechanisms have
to be dealt with in developing a problem description.
As analysts we need to be aware of the fact that an ‘objective’ problem does not exist
and that there can be several problem descriptions, each of which can be correct and
relevant. This also implies that an analyst can never just copy the problem description of
the problem owner who has commissioned the analysis. The analyst has to compare that
problem description to his own analysis of the situation and the problem perceptions of
other actors. The next section describes the challenges to be faced and difficulties that
can be encountered when structuring a problem.
1.3 Approach Taken and Outline of This Course Book
An appropriate problem description, based on a systematic and sound analysis of the
complex environment of policy problems, is crucial for successful policy analysis and
supporting problem-solving. In this book we provide a way to develop such a problem
description.
It all starts with a good understanding of the role of problem structuring in support-
ing policy processes and in dealing with complex policy problems, for which the next
chapter offers theoretical perspectives. A useful problem description provides a sound
basis for determining whether the situation merits further action, and, if so, what actions
are indicated. As will be further explained in Chapter 2, insights are therefore needed in
(1) substantive, i.e. content related, aspects and (2) actor, network and institutional char-
acteristics.
Substantive aspects include, but are not limited to
– the perception of the gap: what are the key attributes of the desired situation? What are
the differences with (expected) reality? How serious is this? What are the causes of this
situation? What possibilities exist to improve or solve the problem situation?
– availability of knowledge required to select a good solution
Actor, network and institutional characteristics, among other things, focus on:
– identification of the relevant actors, their beliefs and perceptions regarding the prob-
lem situation and their means to influence the situation
– actor interdependencies and interactions
– the formal and informal rules governing decision-making
Problem structuring efforts need to address the broad spectrum of issues covering sub-
stantive, actor and network, and institutional aspects in a coherent manner. In the pro-
cess, choices also need to be made regarding what is most important, and what less so.
How these choices are made may significantly affect the results.
17

Introduction
Policy AnAlysis of Multi-Actor systeMs
Similarly, where the analysis starts may significantly affect the outcome. The starting
point may be a focus on substance, or a focus on the actors, processes and institutions in
the policy arena. If the initial analysis concentrates on substance, political and institutional
issues will come to light only later, if at all. If, on the other hand, the initial attention goes
to the political arena, political or institutional problems (such as the lack of trust between
key actors involved) will come to the front, and the substantive aspects of the issue may be
driven to the background or suppressed altogether, since solutions for the trust problem
may be found in entirely different fields.
While ideally, in a balanced approach, all the different aspects are considered and syn-
thesized, experience and personal judgment are important in attempts to achieve this
ideal – if possible at all.
The approach taken in this book assumes that a policy analyst mostly becomes involved
at the initiative of a client/problem owner, i.e. an actor who feels a need for support. In the
description of our approach, we first take the problem owner’s initial problem perception
as a starting point. Next, we show how an approach starting with a focus on the substan-
tive aspects of an issue can be extended and integrated with an analysis of actors and
institutions. As problem situations evolve over time, and efforts to solve or ameliorate
them will inevitably occur in the future, we add an exploration of possible future situations
that could affect the situation.
Figure 1.2 illustrates the key elements of this approach. The initial problem perception
of the client or ‘problem owner’ is taken as starting point. Chapter 2 provides, among
other things, some practical suggestions for the development of the very first problem
description.
Next, three types of problem structuring methods and techniques are proposed that
help in the critical analysis of this initial problem description, in order to develop an
improved version of the problem description, which we call a rich problem description,
that is more likely to lead to the realization of a suitable solution. The approach starts
with systems analysis methods (Chapter 3). This comprises a number of basic techniques
and methods for analysing and structuring problems, or parts of problems. The various
techniques cumulate in a so-called system diagram, in which the problem is delineated,
defined and positioned in its dynamic context. This system diagram can then be updated
and adjusted based on the outcomes of additional analyses. Analysis of the actor environ-
ment, the networks and stakeholders engaged in the problem is another important topic,
elaborated in Chapter 4. Next, exploring the future as a strategy for dealing with contex-
tual uncertainty is discussed in Chapter 5.
These three analytic activities are not independent. System analysis provides indica-
tions about actors that do or may affect the situation, while the inclusion of new actors
can lead to the need for addition of new relevant factors in the system analysis. Simi-
larly, insights from both system and actor analysis guide the selection of possibly relevant
future developments, and vice versa. Given the importance of overall consistency of the
different analyses, special attention is given to the synthesis of the results of different
analyses in Chapter 6.
Problem structuring results in a rich problem description. After problem structuring,
the question is if the policymaker has sufficient information to make a policy decision. If
this is not yet the case, then the policy analyst develops a suggested path forward. This
may, for example, consist of the analyst conducting an impact assessment of the identi-
fied alternatives, conducting more detailed research into a specific alternative, investigat-
18

noitcudortnI
1 InTroduCTIon
ing the underlying values of actors involved in the problem situation, etc. The suggested
path forward may also include participative activities, such as focus groups, that involve
actor interaction, in which the role of a policy analyst may be more facilitating. Alterna-
tively, it may be concluded that the rich picture is not yet fully developed and requires a
further iteration of problem structuring.
Chapter 6 provides a framework to characterize a problem situation that can help in
developing a plan of action following problem structuring. Depending on the problem
situation, different types of activities, such as research, design or mediation, may be pro-
posed and specified in such a plan of action. Within the context of this course, particular
attention is given to conducting research as a follow-up activity (Chapter 7). Finally, the
problem structuring results and the suggested plan of action can be communicated to
the client in the form of a so-called issue paper, and guidance for this can be found in
Chapter 8.
Synthesize
Plan
Actor/ Charac-
network terizethe Propose
Ini�al C sy a s u t s e a m l/ analysis Rich problem f a o c l � lo v w i� -o es n pr F o r b am lem ed &
problem analysis problem Plan of
percep�on descrip�on
ac�on
Iden�fy
Future knowledge
scenario gaps
analysis
Result or situa�on Time sequence
Process or ac�vity Mutual influence
Figure 1.2 Steps in problem analysis and outline of the approach followed in this book
References
Ackoff, R. L. (1974). The Art of Problem Solving. New York: Wiley.
Bardach, E. (2000). A Practical Guide for Policy Analysis: The Eightfold Path to More
Effective Problem Solving. New York: Chatham House Publishers.
Hoogerwerf, A. (1987). De levensloop van problemen: definiëring, precisering en
oplossing. Beleidswetenschap, 1, 159-181.
Jann, W. & Wegrich, K. (2017). Theories of the Policy Cycle. In: F. Fischer, G. J. Miller &
M. S. Sidney (Eds.), Handbook of Public Policy Analysis. Theory, Politics, and Methods.
Boca Raton, FL. Taylor & Francis Group (pp. 43-62).
Kingdon, J. W. (1984/1995). Agendas, Alternative and Public Policy. Boston: Little, Brown
and Company.
Patton, C. V., Sawicki, D. S. & Clark, J. J. (2012). Basic Methods of Policy Analysis and
Planning. New York: Routledge.
19

Introduction
Policy AnAlysis of Multi-Actor systeMs
Simon, H. A. (1977). The New Science of Management Decision. Upper Saddle River:
Prentice Hall PTR.
Simon, H. A. (1991). Organization Science, 2(1) (Special Issue: Organizational Learning:
Papers in Honor of (and by) James G. March), 125-134.
Thissen, W. A. H. (2000). Issue-Formulation in a Multi-actor Context: A Five Step
Approach. Proceedings of the IEEE Conference on Systems, Man and Cybernetics, 301-306.
Thissen, W. A. H. & Walker, W. E. (Eds.) (2013). Public Policy Analysis: New Developments.
Springer.
Walker, W. E. (2000). Policy Analysis: A Systematic Approach to Supporting
Policymaking in the Public Sector. Journal of Multi-Criteria Decision Analysis, 9, 11-27.
https://doi.org/10.1002/1099-1360(200001/05)9:1/33.3.CO;2-V.
Wildavsky, A. (1979). The Art and Craft of Policy Analysis. Hampshire and London:
MacMillan Press.
20

smelborP
2 Problem Formulation in Complex
Environments
Problem formulation is an important analytical
‘A problem well stated is a problem activity. A badly or wrongly formulated problem
half solved.’ will lead to a problem continuing or getting
Charles Kettering (1876-1958) worse, or to the wrong problem being solved,
or to implementing a solution that serves a dif-
ferent goal. It may even create a new problem.
Therefore in this chapter we look at the process of problem formulation, the dimensions
of problems that need to be considered and complexity encountered. In the second part of
this chapter we position problem formulation as part of a policy process, wherein the lat-
ter is not a rational stepwise procedure but rather an iterative and opportunistic decision-
making process. In the final part of the chapter we will position problem formulation as a
first step in problem analysis.
2.1 Coping with Complexity
Complexity is the everyday reality of the problems faced by analysts and problem solvers
concerned with complex socio-technological systems. For technicians and engineers, the
complexity of problems tends to be one-dimensional and is often technical in nature. In
reality, however, there are few clearly structured problems with a single problem owner,
a single problem definition, a small number of players and few alternative solutions, of
which one is objectively the best. There are numerous examples of technically and organi-
zationally complex or unstructured problems in which different rationalities play a role,
knowledge is disputed, often with conflicting problem definitions and conflicting inter-
ests.
Dunn (1981) notes that one of the lessons we have learned from policy sciences and the
science of public administration is that problems with a good or medium level of struc-
turing seldom occur in the complex reality of the world we live in. Whereas conventional
methods will solve well-structured problems, analysts confronted with complex situations
must first actively explore the problem and its context to formulate an approach. This is
usually done in an issue paper (see also Chapter 8). Exploration of the problem situation
and the definition of what exactly the problem is are therefore the first steps that must be
taken towards solving a complex problem. Dunn (1981: 106) explains this in the following
way:
Whereas well-structured problems permit analysts to use conventional methods to resolve
clearly formulated or self-evident problems, ill-structured problems demand that the ana-
lyst first take[s] an active part in defining the nature of the problem itself.
21

Problems
Policy AnAlysis of Multi-Actor systeMs
Dunn (1981) refers to complex issues of this nature as ‘ill-structured’ problems, as opposed
to ‘well-structured’ problems. Rittel and Webber (1973) used the distinction between
‘tame’ and ‘wicked’ problems, and other labels referring for instance to messy problems,
ill-defined problems, untamed problems or ambiguous problems. Characteristic features
of these ill-structured problems are the large number of players who are involved, the con-
flicts of values and the unlimited number of potential policy alternatives. Global current
examples of these kind of ‘wicked’ problems are the development of policies to recover
from the COVID-19 crisis lockdown, to develop policies to comply with the climate change
agreements, the uncontrolled and unaccounted emissions of air transport, the energy
transition in Europe and the tension between (cyber-)security and privacy. At a national
scale, examples in the Netherlands include the expansion of Schiphol Airport, the gas
transition, the taxation rules for multinationals and the location of wind farms on land.
Next to value conflicts and abundance of alternatives, several identifiable factors influence
the complexity of a problem. Some of these characteristics of problems or dimensions are
listed in Table 2.1.
Table 2.1 Dimensions of complexity
Low Complexity High Complexity
Well defined Poorly defined
Well structured Poorly structured
Closed Open
Static Dynamic
versus
Static context Dynamic context
Scientific Practical/Applied
Individual Collective
Single level Multi-level
Local International
Complexity springs from numerous sources, as shown in Text box 2.1. Whereas a complex
technical problem can usually be solved by a technical or engineering solution, the com-
plexity of players caused by different perspectives and conflicting interests implies that
solutions either need to be negotiated or are imposed by a party with the power to do so.
Next we will examine these technical and social dimensions of problems in more depth.
Text box 2.1 Example: Airbnb as a complex problem
Airbnb and Uber probably are the most well-known and fast-growing peer-to-peer platforms in
the early 21st century. The unprecedented success of these internationally operating platforms
not only is a threat to traditional local service providers such as hotels and taxi services; it also
leads to issues such as doubts on the fairness of competition; discussions on the terms of
employment and liability; deterioration/improvement of the quality of services; and unforeseen
impacts including congestion, safety violations, and complaints and policies to prevent
tourists driving out inhabitants from popular tourist destinations in Europe.
Way ahead of all other conceivable factors, the number of parties or actors involved in policy-
making is the primary complicating factor, because the number of potential interrelationships,
coalitions, issues and conflicts increases exponentially as the number of involved parties
22

smelborP
2 Problem formulaTIon In ComPlex envIronmenTs
increases. The social complexity is boosted by interdependencies, and differences in power,
knowledge and information levels. Take the City of Amsterdam as an example where the local
authorities want to restrict the maximum number of nights property owners are allowed to
rent out their premises to tourists. They have to deal with Airbnb HQ and its lawyers (who
try to deny responsibility), with local property owners (who do not like the restrictions and
sometimes rent out illegally), with housing associations and neighbours/inhabitants (who
oppose and complain about Airbnb guests being noisy, and littering and occupying their
cafes), with hotel and catering industry (who want fair competition) and with many tourists
and tourist attractions flourishing on traction, with the police, fire department and taxing
agency, with their own municipal organization for control on compliance and many more.
It is clear that the second most important complicating factor is the difference in problem
perceptions held by these actors, stemming from their differing ambitions, interests and
cultural-historical backgrounds. As indicated, they each experience different complicating
factors of a technical/material nature, such as the nuisance caused by drunken partyers, the
ignorance of and unfamiliarity with (fire) safety regulations, the absence of a level-playing field
and the lack of means to check compliance.
2.1.1 Technical Dimension of Problems
In this section, we will use some examples to examine the role of technology, or the techni-
cal aspects, in complex problems and their resolution. When talking about the technical
dimension of a problem, we refer to the substantive aspects of a problem such as trans-
port, construction, civil engineering, environment, safety or economic aspects. Any refer-
ence to techniques or technical aspects should therefore be interpreted broadly.
Technology can play different roles in a complex problem. There are countless examples
of technology solving problems (e.g. the Internet and Skype as a solution to long-distance
communication and more recently Zoom and Teams as tools for teaching online), but
also as the direct cause of problems (e.g. air pollution and environmental degradation as
a result of industrialization or mining activities) or indirect cause of new problems (e.g.
safer cars provoking risky driving behaviour or data centres consuming huge amounts
of (scarce, green) energy). Moreover, something that is technically feasible is not always
socially or ethically desirable (e.g. nuclear weapons or genetic modification). The norms
that scientists, engineers and technicians apply sometimes diverge greatly from those of
other groups in society. Controversies surrounding technologies such as nuclear energy,
biotechnology, cryptocurrency, artificial intelligence and prenatal diagnosis/genetic
screening spring from differences in the norms applied by different sections of society.
Intentionally or otherwise, technology may have a major impact on the organization of
a society. The invention of the motor vehicle in conjunction with mass production using
conveyor belts and growth of the oil industry opened the door to mass mobility. Automo-
biles (and now mobile phones) impacted everyday life enormously – they changed the
way people lived, worked, commuted, communicated and spent their free time. It sud-
denly became possible to transport individual goods and people over long distances. Its
influence is visible everywhere, and nowhere more so than in the United States, the prime
example of a motorized nation, where it has impacted urban development (sprawl), the
distribution of communities and facilities (e.g. shopping malls at the outskirts of town),
the layout of the road infrastructure and public spaces, the near absence of public trans-
port, the settling of the Great Plains and so on.
23

Problems
Policy AnAlysis of Multi-Actor systeMs
Technical solutions sometimes trigger new problems. The automobile may have driven
the American dream and solved the transport problem; it also brought air pollution,
CO emissions, traffic congestion, accidents and social segregation. Fresh problems such
2
as these are countered in turn by new technical solutions, such as cleaner and more eco-
nomical engines, deformation zones and automatic lane-warning and vehicle control sys-
tems. New policy measures may also be introduced such as energy taxes, the compulsory
wearing of seatbelts and rush-hour tolls. Until today, emotions run high in the discussion
on congestion and road-pricing in the Netherlands; some people even claim their free-
dom is at risk. A similar story can be constructed considering the advancement of social
media and fake news; about Facebook and privacy or about Huawei and alleged Chinese
espionage. In fact, almost any new technology or technical solution to a problem creates
both positive/intended and negative/unintended effects.
Often difficult choices must be made between the pros and cons of a technical solution.
It is a question of deciding whether the new problems spawned by a solution are better
or worse than the original problems. Is carbon sequestration and storage a solution or a
problem? Is Alibaba’s Sesame credit system combined with facial recognition techniques
by Intellifusion and the Chinese government’s use of algorithms and AI techniques for
social control good or bad? Is in post-Corona times an app registering everyone’s where-
abouts a necessary life-saving precautionary health measure or an impingement on citi-
zens’ privacy and a tool for political regimes to exercise control? In this modern age, we
are inclined to see technology as the universal remedy to all our problems, but evidently,
this is not always true. In the presence of many of these examples, we must be mindful of
Ackoff’s statement (see the start of the first chapter) and ask ourselves which problem we
are actually solving.
We must also be wary of overestimating the power of technology. Despite the highly
advanced state of medical science, many diseases remain incurable or unavoidable. At
the same time, technology provides only limited possibilities for remedying the environ-
mental impact of our high-quality transport systems, and experts disagree fiercely about
how to calculate that impact. A good early 21st century example of these phenomena is
the improvement of fuel efficiency of traditional car engines being completely cancelled
out by the gain in weight and size of the average car. As electric driving is rapidly expand-
ing the promise of a clean commute, in practice the CO gain is limited as most of the
2
electricity needed for charging the batteries is still being generated by traditional coal-fired
power plants. In short, a problem may be complex because of the absence of a technical
solution or the unintended impacts of the solution. But even when a technical solution is
present, it does not necessarily mean that we can solve the problem. Diverging interests
may constrain the implementation of such a solution. For instance, capacity problems
and noise hindrance issues at Amsterdam Schiphol Airport may be abated by building a
new airfield at sea, but disputes on the costs, risks and environmental impact of such an
island prevent serious studies of the effects of this solution.
In summary, the technical dimension of problems can be problematic in itself; technol-
ogy can be part of a solution to a problem but also be the cause of new problems arising.
Taking a systems perspective (which is the focus of Chapter 3) can help to define and
delineate a problem and study the impacts of technology,
24

smelborP
2 Problem formulaTIon In ComPlex envIronmenTs
2.1.2 Social Dimension of Problems
The number of actors involved and the divergence of their interests and goals are impor-
tant determinants of the complexity and solvability of problems. As illustrated by the
Airbnb case in Text box 2.1 the growing number of actors not only exponentially increases
the number of potential relationships, it also increases the number of potential conflicts
of interest. Social factors such as mutual dependence and differences in levels of power,
knowledge and information – and the possibility of utilizing those differences – determine
in part the opportunities for social groups or actors to exert influence on the problem and
possible solutions. Moreover, the parties involved usually have different perceptions of,
and opinions on, the problem. This disparity stems, among other things, from the differ-
ences that exist in their ambitions, interests and cultural-historical backgrounds.
Neglecting the social complexity and ignoring the legitimate concerns of other stake-
holders may disrupt policy processes and decision-making. In 1994, the Netherlands Gov-
ernmental Scientific Council, a government think tank, published a report that stated as
one of its conclusions that the tendency of engineers to concentrate on technical details
and produce elaborate proposals provoked unnecessary resistance (WRR, 1994: 7). The
Council also stated that major projects needed to be viewed as social transformation
(because of the social effects of, for example, the building of a motorway: such as accessi-
bility to areas, changes in business capacity, noise nuisance, effects on health and quality
of living) and recommended integrating the social and political processes in all phases
of formulating and solving problems and decision-making (WRR, 1994: 105). A current
example is the settlement of damage to private property in North-East Groningen in the
Netherlands, which was caused by earthquakes that were triggered by decades of extrac-
tion of natural gas from the deep underground. Cracks, subsidence and ultimately collaps-
ing houses are threatening the life, health and well-being of the people living in the area. It
also threatens their socio-economic well-being as their houses lose value, cannot be sold
anymore and the village society is falling apart as the government, dedicated agencies and
especially the semi-private sector company NAM have failed to respond to complaints
and to compensate for the losses.1
In the private sector, too, there has been a change in attitude as companies face social
resistance when over-exploiting resources and contaminating the environment. Especially
in Western countries, public pressure obliges big multinationals to adapt their policies; all
over the world national governments are instating environmental regulatory regimes and
sustainable policies.
This pursuit of integration of political/social and technical elements is entirely in line with
the ‘Polder Model’ in the Netherlands that puts consultation in the place of hierarchical
administration. Essentially, the Polder Model dictates that all interests must receive atten-
tion when solving problems. In the Netherlands the decision-making culture is based
on the principle of consensus (Hendriks & Toonen, 2001). In practice, this consensus
model does not work perfectly though, for example, because groups of stakeholders
have insurmountable or fundamental objections or because there is much disagreement
about the nature and formulation of the problem. Examples of the latter are the discus-
sion on energy transition and the Netherlands off-natural gas, or whether rare expensive
1 See for instance: www.rijksoverheid.nl/onderwerpen/gaswinning-in-groningen/schade-door-gaswinning
(accessed November 2021).
25

Problems
Policy AnAlysis of Multi-Actor systeMs
medicines should be reimbursed by medical insurance or whether obliged COVID vac-
cination would have prevented a lockdown. Rather than focusing debate on the technical
opportunity or solution these discussions centre on usefulness and necessity and moral
justification of the proposed solutions.
It is the absence of consensus about a problem in particular that makes problem-solving
complex and difficult. Problem definition and system demarcation become essential as
different questions get mixed up, address different aspects, affect different stakeholder
groups and occur on different scales. It brings to the foreground questions such as:
What is the problem? Where are the boundaries of the system under examination? What
assumptions exist regarding the context of the problem? How much policy space is there
to solve the problem? In this book we will present the basic methods that allow a policy
analyst to just do that: define and demarcate the problem considering the different stake-
holder perceptions.
Outside the Netherlands, typically more hierarchically organized societies are to be
found, and here too huge conflicts of interest and contestation are common. These con-
flicts are dealt with in a different, often more hierarchical, style of policy-making, but
worldwide agreements on issues such as ‘good governance’ and ‘public participation’, e.g.
the Arhus convention (see: http://ec.europa.eu/environment/aarhus and www.unescap.
org/huset/gg/governance.htm), require the initiators of large engineering projects and
new policies to instigate strategic and environmental impact assessment (EIA) studies
to allow for the public to have a say (see for instance: www.iaia.org.) Even China, which
is considered to have a hierarchical, state- and party-dominated governmental system,
formally adopted the concept of ‘harmonious society’ and institutionalized an extensive
system of environmental regulations (Enserink & Koppenjan, 2007). Moreover, China’s
State Environmental Protection Administration (SEPA) intends to strengthen public par-
ticipation in the EIA process. The new regulation includes stipulations on openness of
information; safeguarding participants’ rights; and procedures and methods for public
involvement, including opinion surveys, consultations, seminars, debates and hearings.2
In summary, the actors at play, the stakeholders affected, their perceptions, means and
objectives are largely influencing the complexity of a situation. Therefore Chapter 4 is
dedicated to analysing and mapping the world of actors and stakeholders.
2.1.3 Institutional Dimension of Problems
In an ideal world, a single powerful ‘comprehensively rational’ policy-maker would be at
the heart of your client organization or government, making policies in an orderly and
organized fashion, going through the sequence of steps sketched in the policy cycle (see
Chapter 1). For the analyst operating in this hypothetical world, it would suffice to execute
scientific research and advise the rational decision-maker based on the outcomes of the
study. Our world, though, is far messier and less predictable; policy issues are highly con-
tested; even the problem formulation may be highly contested; there is no single centre of
power and consequently, it is not always clear who is responsible for policy-making. So,
who holds the power to turn your recommendation into an outcome?
In practice, policy-makers, influencers, lobbyists and analysts are spread across many
levels in public and private organizations and types of government. Therefore, it may not
2 Worldwatch Institute, 5 June 2019, www.worldwatch.org/china-strengthen-public-participation-
environmental-impact-assessments.
26

smelborP
2 Problem formulaTIon In ComPlex envIronmenTs
be easy to identify and know your audience, to find out who controls the instruments you
need to solve the problem, especially when several actors control part of these instru-
ments and they need to cooperate to solve the problem. What makes your task even
more daunting is the fact that each organization has its own way of working, formal and
informal ways of organizing itself and the policy process it is organizing or in which it is
participating. As Paul Cairney (2019) summarizes,3
Each venue resembles an institution driven by formal and informal rules. Formal rules are
written-down or widely-known. Informal rules are unwritten, difficult to understand, and
may not even be understood in the same way by participants. Consequently, it is difficult to
know if your solution will be a good fit with the standard operating procedures of organisa-
tions (and therefore if it is politically feasible or too challenging).
Institutional complexity, therefore, is also about legislation and procedures and the fact
that problems often cut across sectors. An integral approach required for problem-solving
often implies that regulations, norms and values from different sectors come together
and this can cause conflict and confusion (Klijn & Koppenjan, 2014). Institutional com-
plexity occurs whenever an organization is confronted with incompatible prescriptions
from multiple institutional logics (Greenwood et al., 2011). For instance, Qiu et al. (2019)
who studied the case of the Hong Kong-Zhuhai-Macao Bridge project describe how the
governance of these kind of megaprojects is facing the challenge of institutional differ-
ences among actors, groups and political regimes, and the macro-environments, which
bring about conflicts and uncertainty. Institutional arrangements therefore can add to the
complexity of such (mega-)projects and not seldom are a cause of problems. For instance,
the disconnect between (national) policymakers and the practice of (local) field workers is
a well-known phenomenon in water and sanitation projects in many developing countries.
This disconnect though is not unique for developing nations; the Dutch childcare benefits
scandal (Dutch: toeslagenaffaire) is a recent example from the Netherlands concerning
false allegations of fraud made by the Tax and Customs Administration while attempting
to implement and regulate the distribution of childcare benefits as designed by the Dutch
parliament.4
When focusing on problem analysis institutional arrangements, the division of tasks,
jurisdictions and responsibilities is highly relevant as this is often a source of tensions and
important for co-defining the decision arenas (who are the relevant stakeholders and deci-
sion-makers at what moment?) and for defining the solution space. The alignment of insti-
tutions is a requirement for successful problem-solving and implementation. M ethods for
analysing this institutional context included in this course book are the formal chart and
interdependencies table presented in Chapter 4.
3 https://paulcairney.wordpress.com/2019/12/19/policy-analysis-in-750-words-what-can-you-realistically-
expect-policymakers-to-do/.
4 www.cnbc.com/2021/01/15/dutch-government-resigns-after-childcare-benefits-scandal-.html.
27

Problems
Policy AnAlysis of Multi-Actor systeMs
2.1.4 Normative Dimension of Problems
Traditional policy analysis was positivistic5 in character in ‘speaking truth to power’ and
stressed value neutrality and rationality (Wildavsky, 1979). A large variety of authors
objected against this positivistic paradigm and attempted to establish a more post-mod-
ern paradigm which allows for social constructivism and appreciation of different per-
spectives (Durning, 1993; Mayer, 1997; Thissen & Walker, 2013). Schön and Rein (1994) for
instance claim that participants in policy processes might have different frames through
which they see and value things. For them the logical next step was to conclude that
the objectivity of the policy analyst is an illusion and the analytical process is loaded
with implicit and explicit value choices, as is the policy process it is meant to support
( Monnikhof, 2006).
In the previous sections, we already mentioned that moral and ethical dilemmas might
add to complexity. We like to frame these as ‘value conflicts’. Values are lasting convic-
tions or matters that people feel should be strived for in general, and not just for them-
selves, to be able to lead a good life or to realize a just society (van de Poel & Royakkers,
2011). Good examples of such values are equity, equality and sustainability, both widely
accepted and heavily disputed at the same time. Although most of us will support the
idea that all people are equal and the colour of our skin or sexual preferences should not
matter, in practice in many countries and societies they do. A black lesbian in Uganda
will be in a less privileged position than a white straight male in Kansas, USA, but even
in a relatively liberal country like the Netherlands the LGBTI+ community is fighting for
acceptance and discussions are ongoing on implicit or even institutionalized discrimina-
tion. The Dutch ‘Zwarte Piet’ (blackface) debate and the lively demonstrations of the Black
Lives Matter movement at the start of the second decade of the 21st century – also in the
Netherlands – show these values are contested. The interpretation of sustainability also
widely differs for instance when comparing statements made by representatives of oil
and gas companies such as Shell and Exxon and representatives of Saudi Arabia, after the
Glasgow 2021 Agreements on the one hand, and the ones expressed by environmentalists
on the other.
Well-known and much debated is of course the utilitarian idea that an action or institu-
tion must be judged by the extent to which it contributes to the achievement of a collec-
tive utility. Public policy in this perspective should lead to higher public welfare, which
is defined as the sum of the welfare of all individuals; and the distribution of the welfare
among the individuals is not relevant as long as the average utility goes up. Consequently,
as Monnikhof (2006) discusses, policies are legitimate if some people gain (a lot) while
others may lose (a lot). The solution to this problem or maybe the circumvention was
given by Pareto who spoke about optimality when a situation has been achieved in which
no one can be made better off without making at least one other person involved worse
off. For practical reasons welfare theory was then expanded with the Kaldor-Hicks crite-
rion which implies that those having advantage from the new situation, the winners, could
fully compensate the losers and still have some gain left. Unfortunately, most of these
losers are never (fully) compensated for their losses and when the losers do not have a
5 Positivism is the philosophical idea that only what can be scientifically verified or proven by logical
reasoning or mathematical proof is true. Pure positivists trust in science only. In contrast relativists argue
that knowledge is not absolute; truth and morality exist in relation to culture, society and the historical
context.
28

smelborP
2 Problem formulaTIon In ComPlex envIronmenTs
legal entity (like the air, the landscape, etc.) compensation and mitigation often are not
included in the economic calculation of costs and benefits (Monnikhof, 2006). Utilitarian-
ism still is prevalent in government policy; for instance large infrastructure projects such
as dams and highways are often constructed referring to national importance and their
contribution to national welfare, while having a big negative impact on local scale both
on nature and on society. Resistance against large infrastructure projects, therefore, often
finds it roots in the uneven distribution of costs and benefits of these projects and the
absent or insufficient compensation of those who incur the negative effects or costs.
It gets more problematic when human life is involved. Cost-benefit analysis when con-
sidering the safety of coastal defences, mining operations or large clusters of the chemical
industry tries to take along safety issues and potential victims of failing operations and the
risk of disasters. But how do you value human life? Measures used include the ‘lifelong
earning capacity’ (also used by insurance companies), but as earning capacity is much
lower than in more economically developed countries this approach entails that human
life in developing countries like Kenya or India is considered less valuable than in more
developed countries in the West. People in Bangladesh, for example, thus may run higher
consequences from drowning because of sea-level rise than people in the Netherlands.
In summary, the normative dimension of problems largely determines the complexity
of a situation and underlying values determine actor objectives and problem perceptions.
Methods for analysing values and objectives are discussed in Chapter 4.
2.2 Framing Complexity
Van de Graaf and Hoppe (1989) report a useful typology of problems, similar to a typology
of problems of risk by Douglas and Wildavsky (1982). Both are based on the distinction
between technological complexity and social complexity (Table 2.2). The axes of the typo-
logy consist of (1) the degree of certainty of knowledge (i.e. high/low) and (2) the degree
of consent about the nature of the problem (the gap between an existing or expected situ-
ation and the desired situation).
Table 2.2 Typology of tamed and untamed problems
Degree of Technological Uncertainty
Small Large
Degree of social consensus Large 1. Tamed problems 2. Untamed technical problems
on a problem Small 3. Untamed political problems 4. Untamed problems
Source: Own work after van de Graaf and Hoppe (1989)
This results in four types of problems:
Type 1. Tamed problems: problems without social conflicts and for which technical solu-
tions are available. The problem-solving process is characterized by analysing the problem
and applying the most suitable solution.
Type 2. Untamed technical problems: problems that everybody feels should be solved,
but technological solutions are not yet available. Investment in research is necessary to
find a solution.
Type 3. Untamed political problems: problems for which technical solutions are avail-
able, but about which a social conflict exists regarding their application.
29

Problems
Policy AnAlysis of Multi-Actor systeMs
Type 4. Untamed problems: problems with the duality of uncertain technical solutions
and lack of social consensus. From a social point of view there is a clash between values
and interests of stakeholder groups and no certainty about the technical knowledge.
According to van de Graaf and Hoppe (1989), problem-solving strategies seek to mould
problems of types 2, 3 and 4 in a way that makes them fit into type 1, i.e. untamed prob-
lems need to be tamed. This is achievable by reducing technological uncertainty and
creating social consensus. This approach will often require a redefinition of the problem.
For instance, defining HIV/AIDS, obesity or internet privacy as an issue of social respon-
sibility and behaviour and not as a purely technical or medical issue opens the door to
different types of solutions, such as awareness campaigns aimed at prevention and at
modification of lifestyles and (sexual) behaviour. Redefinition frequently makes it possible
to find solutions that reconcile the interests of parties who originally oppose each other.
Another example is the construction of surface tunnels in new highway and railroad infra-
structure as a way of limiting the impact (noise, view, air quality) on the surroundings, like
the A4 Delft-Vlaardingen highway in the Netherlands. This latter example illustrates that
new technology is not always necessary in order to tame these types of problems, rather
political will to generate the finances needed to use (existing) technology for compensa-
tion and mitigation measures. Although all the earlier may be true, one should keep in
mind that, when dealing with real untamed problems, taming them is essential but highly
difficult: it is easier said than done, as we will see for instance in Sections 2.2.3 and further.
2.2.1 Structured and Unstructured Problems
Table 2.3 shows yet another typology of policy problems derived from van de Graaf and
Hoppe (1989) and using the dimensions on consensus on values and consensus on knowl-
edge. When there is consensus on values as well as knowledge, providing information will
suffice and no extensive active participation is required. Such problems can be solved in
a technocratic way but when facing the more contentious ones, special attention should
be paid to the design of the decision-making process and the way information is handled
or negotiated within such a process (e.g. de Bruijn et al., 2002; Klijn & Koppenjan, 2016;
Koppenjan & Klijn, 2004). When both knowledge and values are contested, interactive
analysis is the only way forward. As de Bruijn and Porter (2004: 268) argue,
especially when the subject is pressing to the stakeholders, knowledge needs to be negoti-
ated and when both values and knowledge are contested the process of involving actors is
an important aspect of the analysis itself.
When facing an ill-structured problem, discussion on values is required and policy- makers
need to engage in a process with stakeholders to jointly find the necessary decision- making
space. When confronted with a moderately structured problem extensive consultation of
stakeholders and good communication is the way forward.
30

smelborP
2 Problem formulaTIon In ComPlex envIronmenTs
Table 2.3 Typology of problems
Consensus on Values
NO YES
NO Unstructured Problem Moderately Structured Problem
Consensus on Knowledge
YES Ill-structured Problem Structured Problem
Source: Enserink (2005) after Simon (1973) and Keeney and Raiffa (1977)
De Bruijn and Porter (2004) in this respect talk about ‘contested problems’ when referring
to the degree of consensus. They provide us with a kind of decision tree on what to do
when confronted with a complex issue (see Figure 2.1). Answering the five questions listed
next will lead the analyst to a suitable strategy for problem-solving (de Bruijn & Porter,
2004: 265). We rephrase their questions to make their conceptual scheme fit the purposes
of this course. Answering these five questions will lead you through the decision tree and
provide you with advice on how to continue (see Figure 2.1).
1. Can the problem be solved and the solution decided upon essentially by one actor
(i.e. authoritarian) or by a consensual process of multiple actors (i.e. network)?
2. Are the interests and objectives of the actors involved closely aligned?
3. Is there consensus on the knowledge/technological information?
4. Is the issue considered vitally important to the stakeholders?
5. Is there agreement that the decision is urgent?
Figure 2.1 Decision tree to diagnose whether a situation requires stakeholder
engagement (Source: After de Bruijn and Porter 2004; Enserink et al. 2010
cc Jill Slinger)
31

Problems
Policy AnAlysis of Multi-Actor systeMs
Choosing a path through the decision tree will lead to one of five actions which can easily
be linked to the policy analysis styles included in the hexagon model described by Mayer
et al. (2004) which will be introduced in Chapter 6:
1. Traditional disciplinary science and engineering: professional analysts using scientific
methods and tools conduct the analysis, ratio leads to a best outcome.
2. Mediated interactive analysis and democratizing science: important stakeholders are
actively involved and make the crucial decisions regarding these analyses. For instance,
they should decide on the scope of the analysis and what method to use.
3. Good communication, clarifying values and arguments: the main stakeholders should
be consulted to obtain information about their ‘frames’ and perceptions of the prob-
lems at issue. The main interest of the analyst is to present his or her findings as trans-
parently as possible.
4. Identify solution space: focus is on the process and legitimacy of decision-making as
the issue is urgent and important. Diverse knowledge sources and interests, although
not closely aligned, must be taken into account. It is important for stakeholders to
make a ‘no-regret’ decision that offers sufficient space for future decision-making.
5. No action: sometimes any resulting knowledge or information is so unlikely to be used
that analysis would be a waste of time and resources.
2.2.2 Objective versus Subjective Problems: The Role of Perceptions and Interests
Conceptually we defined a problem to be the gap between the desired and the existing or
expected situation, but given that different stakeholders hold different ideas about what
is desired and different perceptions of the existing (or future) situation, the analyst’s task
is complicated (see Figure 2.2).
Desired
Situa�on
Gap
Exis�ng or
Actor Expected
percep�on Situa�on
Causes
Solu�ons
Figure 2.2 Problems as a perceived gap
Complicated may evolve into complex as different actors may have very different ideas
about the desired and/or existing situation and about how the problem should be for-
mulated and solved. ‘Problem perception’ is the term used to describe these subjective
views of actors on problems which may in the end lead to different problem definitions.
Logically, this can result in a concrete problem situation in which different definitions of
‘gaps’ exist alongside one another, gaps of which other participants involved may not even
be aware. An example of such a situation is depicted in Text box 2.2 where we introduce
32

smelborP
2 Problem formulaTIon In ComPlex envIronmenTs
the example of the former railway overpass in Delft in the Netherlands and the lengthy
decision-making process that led to the new solution: a tunnel and an underground rail-
way station allowing for the former rail track area to be developed into a new living/work-
ing/recreational area.
Text box 2.2 Example of objective and subjective problems: the Delft railway passage
By the turn of the century trains passed through the city area of Delft in the Netherlands on an
elevated rail track, cutting the town into two parts and causing noise pollution, nuisance and
safety threats for the citizens (see Figure 2.3). The Netherlands Railways wanted to intensify
rail traffic on this so-called ‘old line’ between Amsterdam and Rotterdam. Growing passenger
numbers in the future would require doubling its capacity. Clearly realization of the initial plans
for doubling the elevated track would increase the level of hindrance (esp. noise pollution). The
definition of the problem, or gap between the existing or expected situation and the desired
situation, is not clear and surrounded by uncertainties.
Figure 2.3 Old and current situation in Delft (pictures by author)
The objective problem
In the Noise Abatement Act, noise pollution is expressed in terms of the noise volume, in
decibels, at the outer wall of a dwelling. The maximum permissible volume due to railway
traffic is 57 dB. A dispensation may be granted up to 70 dB, and higher volume levels can be
permitted under certain circumstances. Inside the dwelling, the maximum permissible volume
is 37 dB. To achieve such a low value, extreme noise insulation measures, such as installation
of triple-glazing, must be taken. In the vicinity of a railway station (1500 metres on both sides),
the permissible volume is 5 dB higher. The trains on the former railway viaduct at Delft for
instance gave rise to peak loudness levels at outer walls of dwellings of between 93 and 98
dB. However, in the Noise Abatement Act, the peak volume is not the determining factor: it is
the mean volume per hour that is considered. This means that a situation can arise in which
residents are being woken up every night by the rumble of goods trains and the hiss of railway
lines even though formally the volume does not exceed the stipulated levels.
The subjectivity of the problem
Residents: The current use of the railway viaduct in Delft causes serious noise and health
nuisance. The peak noise largely exceeds what is permitted! We wake up several times every
night! Measures should be taken immediately. Expansion of the railway service will worsen
these problems.
33

Problems
Policy AnAlysis of Multi-Actor systeMs
Municipality: The existing viaduct causes nuisance and is undesirable within the urban setting;
the railway infrastructure and any expansions must be placed below ground. The latter will
create opportunities for city redevelopment.
Netherlands Railways: The current use is within the limits set by the Noise Abatement Act.
To maintain the quality of passenger services in the ‘Randstad’ area it will be necessary to
intensify the use of this section of the track in the near future; while in the longer term the
capacity will have to be doubled. Noise abatement and mitigation measures will reduce the
hindrance for residents along the track.
Passengers: Comfort, speed and reliability of the rail service must be guaranteed; the present
capacity causes too many delays.
Ministry of Transport: The current use is within the limits set by the Noise Abatement Act.
Priority in the new railway infrastructure is being given to the high-speed rail link (HSL) and the
preferred HSL route does not pass through Delft.
The Delft textbox example makes clear that problem perceptions are linked to actors,
their positions and roles. It may even be the case that one actor is still thinking in terms
of problems while another is already talking about solutions; actually it is quite common
that the preferred solution of one actor is seen as a problem by another actor. A number
of explanatory variables exist for differences in perception. These differences are related
to such circumstances as:
– the background and history of the actor concerned;
– the position and interests of the actor (‘where you sit is where you stand’);
– communication patterns (who talks to whom);
– individual reference frameworks (selective perception);
– the available vocabulary (what can be discussed);
– the modelling method (graphical, mathematical, procedural).
Text box 2.3 The Delft railway passage – continued
Returning to our example of the train track in Delft: the complexity grew when during the debate
on the need for a tunnel, the discussion on costs and especially on (financial) risks was gaining
prevalence. The Mayor and Aldermen of Delft were willing to invest in the tunnel project and
to bear a large part of the financial risks in order to persuade the Ministry of Transport and
Waterways to also invest in the way more expensive tunnel solution. Opponents accused them
of bringing the city to bankruptcy and clashed with proponents in the Delft City Council over
almost anything regarding the tunnel project and the area redevelopment process. Interestingly,
with hindsight, we can conclude that both sides were both right and wrong. The city of Delft
took big financial risks and when economic crisis hit the Netherlands Delft no longer could
fulfil its financial obligations and received a so-called Article 12 Status, implying it was under
curatorship by the national government because of its structural financial problems. As an
ultimate consequence, the new city hall building that would have been constructed on top of the
underground railway station lost its top floor. When the economy started to blossom again and
investors returned the financial problems diminished. Around 2020 the new railway station has
become a modern city icon and construction works in the ‘New Delft’ city development area are
well underway. The criticism on the boastful plans has dwindled.
34

smelborP
2 Problem formulaTIon In ComPlex envIronmenTs
2.2.3 The Problem Formulation Battle
The way a problem is defined is not neutral. Problem formulations indicate the elements
of a situation that matter and those that matter less. This not only marks out the problem
field, it also identifies the relevant and less relevant variables and standards. In the Delft
example, these are: the nuisance for the city dwellers, the capacity for the railroad services
for the Dutch Railways and financial risks for the municipality of Delft and the Ministry of
Transport. Consequently, problem formulation sets the direction of possible solutions
and excludes others. Problem formulation thus influences the division of potential costs
and benefits for the parties involved in the problem. Indeed, the supposedly unfair distri-
bution of costs and benefits, the absence of (sufficient financial) compensation and insuf-
ficient mitigation are quite often a reason for resistance against major infrastructure works
(Monnikhof, 2006).
This explains why the formulation of a problem
‘The thought process and the is a contentious activity; it is a political and
exercise of power are closely related strategic choice that centres on what the nature
to each other. They may coincide or of the problem is and, by extension, what the
follow on from each other, but they most promising solutions are, and sometimes
continuously influence each other.’ on the question of whether or not a problem
(Hoogerwerf, 1992: 13) exists. Problem owners who are confronted
with the costs of an existing situation usually
find themselves lined up against parties with a
vested interest in the continuation of the existing situation because they stand to benefit
from it (and can saddle others with the costs). At times stakeholders who are confronted
with the cost of a solution usually oppose the initiator or problem owner because it is
in their interest to maintain the status quo. In brief, the formulation of a problem is of a
political nature and often the cause of conflict (Schattschneider, 1960). Nonetheless, the
first and most important challenge of the analyst is to come up with a proper substantive
(scientific) problem definition that is considered legitimate to other actors. This probably
implies active involvement of stakeholders in the problem formulation process (de Bruijn
et al., 2002).
Communicating the problem, therefore, is the next challenge for the policy advisor; how
to bring about the message? How to create a strong message and how to choose the right
words? In his book Narrative Is Everything Olson (2019) argues that the ‘And, But, There-
fore (ABT)’ narrative template is the simplest and most powerful tool to communicate a
message and to attract and keep the attention of your public. ‘And, But, Therefore’, he
argues, is for all kinds of psychological reasons thought to be the most effective way to
present a message. Referring to the Delft railway problem the message could have read:
the capacity of the rail track falls short and the noise hindrance is excessive, but enlarging the
existing viaduct is not acceptable, therefore a radically different – underground – solution is
needed. This is a strong message stating the problem and showing the way out. But the
earlier problem formulation might not be the right one. In his book The Art of Political
Framing de Bruijn (2019) gives nice examples of framing and reframing and the impact
of using the right words. For instance, in the sentence on the Delft railway expansion, the
focus is on the capacity needed, but when the discussion focuses on the financial risks
involved, a different frame might work: A railway tunnel is more expensive, the construction
works will have a big impact on the city centre and may take much more time to implement,
35

Problems
Policy AnAlysis of Multi-Actor systeMs
but the hindrance caused by the viaduct is excessive and new chances for the development of
Delft are created; therefore, it is legitimate to invest more public money in this infrastructure
project. This, too, is a strong message in ABT style, but which frame to choose is a matter
of politics and may indeed be the essence of the problem formulation battle. It illustrates
that the policy analyst almost inevitably will operate in a politicized environment in which
choosing the right words contributes to the impact of your findings.
2.2.4 The Social Construction of Problems
It is usually assumed that there is a specific problem owner who puts forward a problem.
A policy analyst who accepts an assignment to solve this problem should ask – if for no
other reason than their professionalism – whether the client’s problem formulation is
acceptable and eventually redefine this formulation in researchable, workable and accept-
able terms. The policy analyst has to operate in the field of tension that exists between the
problem formulation made known by the client and the knowledge that other actors may
view the problem very differently. One can question whether manuals that speak of ‘prob-
lem exploration in the context of the assignment’ do sufficient justice to the existence of
different and sometimes contradicting problem formulations.
Some approaches define the phase of getting matters onto the agenda as a policy-
analysing activity. Hogwood and Gunn (1984), for example, describe and examine ‘issue-
search’ activities. Theories that describe the agenda-setting part of the policy cycle (such
as agenda forming) highlight the fact that problems do not appear automatically on the
agenda of problem solvers. Problems are not objective facts that are waiting ‘somewhere
out there’ for somebody to discover them. The actors involved must experience them, put
them into words and articulate them, i.e. submit them as claims to decisions-makers; a
newer take on this topic is that of ‘framing’ (de Bruijn, 2019). Cobb and Elder (1983) refer
to the process of ‘issue creation’ whereby initiators actively endeavour to place a problem
they are experiencing on the agenda of the media, policy-makers and politicians. Accord-
ing to Cobb and Elder, the probability of gaining support and consequently agenda status
will increase if a problem formulation:
– has major societal relevance (i.e. affects a large number of people);
– will bring about long-term effects as well as short-term ones;
– is specified to a lesser degree in technical terms;
– is not so specific;
– is presented as new.
2.3 Problem Formulation as Part of Problem-Solving
It will be clear that problem formulation is a critical but contested and difficult activity in
policy analysis in complex environments. When dealing with wicked problems according
to Rittel and Webber (1973) the formulation of the problem is the problem, and the main
challenge for a policy analyst facing complex problems is ‘finding problems worth solving’
(Wildavsky, 1979). However, such problem formulation is not neatly separated from other
activities in the problem-solving process. Problem-solving processes at the level of com-
plex systems, networks and chains do not take place in a number of chronological phases
but are rather extremely unstructured. ‘Formulating problems’, ‘designing’ and ‘deciding’
are activities that are linked in a complex way and have the nature of a strategic interaction
process in which analysis and the exercise of power are important. As regards the content
36

smelborP
2 Problem formulaTIon In ComPlex envIronmenTs
of the process of problem formulation, this means that the objective must not be to pur-
sue a detailed problem analysis based on a substantive analysis and (scientific) research
alone, rather a rich problem analysis also includes the perceptions of other parties and
should be scientifically defensible. Combining these insights is important as a point of
departure for interaction and mutual adjustment between parties.
As mentioned before, Herbert Simon (1977, 1991) claimed that people solve problems
in four steps: intelligence, design, choice and implementation. These four steps form
the basis for numerous attempts to conceptualize decision-making, problem-solving
and design processes in a wide range of disciplines. As mentioned, Hogwood and Gunn
(1984) identified nine core activities for policy analysis and Hoogerwerf (1987, 1992 or
1998) needed the same number to describe policy design processes. They all suggest a
rational chronology of activities, but in the next sections we will look at policy theories
that seem to contradict any rationality or chronology in policy-making; rather they suggest
there are plural forms of rationality, e.g. political rationality. They sketch the dynamic and
unpredictable nature of policy-making that analysts have to deal with; therefore it may be
a rational choice to take note of these contextual characteristics!
2.3.1 Garbage Cans and Streams
Even though the inventors of the earlier models immediately point out that the phases are
meant to be logical rather than chronological and recognize that feedback and iterations
take place, this thinking in phases often results in attempts to tackle problems following
a number of fixed, sequential steps. In practice though, problem-solving processes may
prove to be extremely unstructured, often resulting in unexpected outcomes. Cohen et al.
(1972) produced arguably the most radical conceptualization of this unpredictable charac-
ter in their ‘Garbage can model of decision-making’ (see Figure 2.4). This garbage can model
applies to complex situations without a clear fixed hierarchy of objectives and values and
where routine procedures seem absent. Moreover, in these situations it is not even clear
who is participating in the decision-making processes as the latter is not regulated. These
situations are called ‘organized anarchies’. With their model, Cohen, March and Olsen
originally had in mind professional organizations such as hospitals and universities, but
they soon discovered this model could also be applied for network-like situations, such as
decision-making on public infrastructures where numerous actors are involved.
37

Problems
Policy AnAlysis of Multi-Actor systeMs
problem
solution
participant
solution
participant
decision
problem
choice opportunity
problem
participant
solution
problem
decision
T
participant 0 decision
T
1 choice opportunity
choice opportunity
Figure 2.4 The garbage can model by Cohen, March and Olsen (Source: Koppenjan
& Klijn, 2004)
Text box 2.4 Example of a garbage can solution
An example that seems to fit nicely the garbage can theory is the highly expensive seven-
kilometres-long tunnel in the high-speed rail line between Amsterdam and Rotterdam in
the Netherlands. This expensive bored tunnel was an unanticipated outcome of the highly
politicized debate on the preferred trajectory: speed versus nuisance. The seven kilometres of
bored tunnel would allow for an eight minute faster route with no stop-over in the city of the
Hague. Even better: such a tunnel would save the vulnerable, valuable open landscape with
ditches, meadows, cows and traditional windmills of the so-called Dutch Green Heart area.
Tunnel boring technique in soft soils was new and ‘hot’ at that time; construction companies
and consultants were promoting this newly discovered engineering opportunity; it was a
solution looking for a problem. A solution which became available when the political parties
needed a breakthrough in the stalled debate on the trajectory of the rail line.
In this radical perspective a decision moment is presented as a garbage can into which
participants deposit their problems and solutions. The contents of such a garbage can
depend on the moment in time in combination with the production of waste (the prob-
lems, solutions and participants), the availability of other garbage cans in the area and the
speed at which the garbage cans are emptied. The result of decision-making therefore is
almost impossible to predict and largely depends on what happens to be in the garbage
38

smelborP
2 Problem formulaTIon In ComPlex envIronmenTs
can in the way of problems, solutions and participants at the decision-making moment.
This garbage can theory can explain unexpected or unanticipated outcomes of decision-
making processes. The radical idea of the garbage can is the absence of control and unpre-
dictability of the outcome (Text box 2.4).
2.3.2 Problem-Solving Following the Streams Model
Cohen, March and Olsen (1972) refer to streams of problems, solutions, participants and
decision moments/choice opportunities as shown in Figure 2.4. Kingdon (1984/1995)
took this idea further, modified it in a number of places and applied the streams idea to
public decision-making processes. Kingdon identified three streams: problems, solutions
and political events (see Figure 2.5). This implied that political events such as changes of
governments and/or changes in the political and social climate are seen as opportuni-
ties for solving problems or realizing opportunities. Shifts in political preferences may
result in certain problems and/or solutions gaining (and others losing) political support.
The change of administration in the USA from Obama to Trump to Biden for instance
largely determined the fate of Obamacare, US foreign policy and the US stance on climate
change. In contrast to the garbage can model, in the streams model actors or participants
are located and active within and between the streams because, according to Kingdon,
problems cannot be isolated from people (or groups or organizations). People need to
articulate problems. The same applies to solutions: you need people to think them up and
to bring them to the attention of other people in order to get them accepted and imple-
mented. Kingdon introduces a new metaphor – the policy window – which refers to the
coupling of participants, problems and political events. Without such a coupling of these
streams, the decision-makers will not take a decision, no matter how urgent the problem
may be or how promising a design is.
Figure 2.5 Kingdon’s streams model (Source: Own work after Pauly 2001)
Policy windows do not come about automatically; they are created by ‘policy entrepre-
neurs’: actors hunting for solutions to their problems, or problems for their solutions, or
for support for their problem-solution combinations and choice opportunities looking
for participants. In effect, the streams model turns the traditional phases model upside
down: in the rational model, agenda setting and analysis of the problem are followed by
39

Problems
Policy AnAlysis of Multi-Actor systeMs
the development and selection of the solution, based on unambiguous and explicit crite-
ria; the streams model affords scope to solutions looking for problems and for decision-
makers looking for solutions and problems.
Text box 2.5 Example of streams model decision-making
In the Dutch river dike debate in the 1970s/1980s it was thought that traditional dike
reinforcement would damage important landscape features and natural landscapes in the
area and the opposition to traditional enforcement was fierce. Numerous alternative dike
construction methods, so-called ‘smart dikes’, were developed that would spare monuments
and nature, but these solutions were considered (too) expensive. The extreme high river
waters in 1993 and 1995 that led to complete evacuation of the area created the policy window
where the three streams met: the problem was urgent; the solution was around and politicians
needed to act. An emergency law was drafted leading to extensive dike improvement works
that used ‘smart’ solutions at vulnerable places.
Kingdon’s streams model may appear to be extreme at first sight, but closer examination
will reveal several recognizable points. In the Netherlands for instance, during the 1970s
and 1980s the decision-making on the improvement of the river dikes had been in a dead-
lock situation (see Text box 2.5).
A current example is the very fast development of COVID-19 vaccines; they could be
developed starting from the vaccines that just had become available to counter the related
SARS viruses, the problem was urgent and the political will to implement vaccination
schemes was present.
Text box 2.6 Example of a solution looking for a problem
Yet another example of a solution looking for a problem is the so-called Betuwe Route – i.e.
a ready-to-go design of a goods rail line between the harbour of Rotterdam and the German
border. At the start of this century, it was presented and defended by the Netherlands
national government without an initial clear discussion on the usefulness and necessity of
the line. This explains why over time diverging problem formulations have been linked to the
Betuwe Route – including the safety on the existing infrastructure, the supposed threat to
the competitive position of the port of Rotterdam, the sluggish development of the Dutch
economy, employment opportunities and solving environmental problems – all of them
presented without any change to the pre-defined solution: a new rail line. A proper problem
formulation would have centred not on the question ‘How do we realize the Betuwe Route?’
but on the question of ‘How to improve the link between the port of Rotterdam and inland
areas?’ This kind of problem formulation would have left room for entirely different solutions,
including transport by barges. Moreover, the challenge to legitimate the high expenses made
proponents focus on solving problems in the Netherlands and may partly explain why in 2021
the connecting rail link in Germany is still under construction.
40

smelborP
2 Problem formulaTIon In ComPlex envIronmenTs
2.3.3 Problem-Solving in Arenas and Rounds
Building on the garbage can and streams model, it can safely be stated that decision-making
regarding problems takes place in rounds and arenas and not according to chronological
phases (Figure 2.6). Activities within these rounds may differ widely though; they can be
undertaken to explore a problem, to design or select a solution or a combination thereof.
A round ends with a ‘crucial decision’, i.e. a decision or outcome that is taken for granted
and settles the debate on issues central in this round and acts as a point for departure
for new rounds of negotiations and that influences the rest of the process. This does not
necessarily imply that this decision will be elaborated further in a subsequent round. For
example, the decision may have been to refrain from adopting a certain solution and to re-
examine the question of what the problem actually is. The problem-solving process in the
rounds model strongly resembles a boxing contest, i.e. the result of each round can differ
and the winner only becomes apparent at the end (Teisman, 2000). To further complicate
the decision-making process, sometimes several arenas exist simultaneously, where par-
ties push and shove about problems and solutions in different places at the same time.
These arenas are places where choices are made or the garbage cans where participants
create, negotiate and decide about problem formulations and solutions. In these different
rounds and arenas, decision-making processes are characterized by their zigzag course,
ups and downs and iterations (van Bueren et al., 2003).
Figure 2.6 The rounds model: problem-solving in rounds and arenas (own work)
2.3.4 Problem-Solving and Advocacy Coalitions
Describing problem-solving as a sequence of rounds, where streams of problems, solu-
tions and events are connected in and across different arenas, offers a rich picture but
does not look specifically into the role that formal analysis and technical information
can play in these processes. For this, yet another theoretical perspective from the policy
sciences is useful: the Advocacy Coalition Framework (ACF). The concept of an ACF was
developed by Sabatier and Jenkins-Smith (1988) to deal with ‘wicked’ problems and to bet-
ter understand the roles that formal analysis and technical information play in the policy
process (Sabatier & Weible, 2007).
41

Problems
Policy AnAlysis of Multi-Actor systeMs
The framework assumes that policy-making occurs within policy subsystems consisting
of several theoretical components (see Figure 2.7). Within those subsystems, advocacy
coalitions are formed by clusters of stakeholders who share a belief system. For instance,
in many environmental policy problems, one could find typically an environmental or con-
servation coalition as well as a business development coalition. These coalitions have
different beliefs, not only about ‘how the world works’ but also about ‘what is good for
the world’, thus they hold different problem formulations. The coalitions aim to translate
components of their belief systems into public policy, using for instance a lobbying strat-
egy – aimed at the formal decision-makers, so-called sovereigns – to introduce their argu-
ments into the decision-making process. For this, they have the resources to pursue their
interests (Sabatier, 1988; Sabatier & Weible, 2007). According to the ACF, the sovereigns
have legal power and adopt legislation and public policies while the coalitions attempt to
influence this legislation via lobbying activities targeted at the different sovereigns during
the decision-making process. The actors in a policy subsystem are affected not only by
the processes within the policy subsystem but also by external factors and events in the
broader political, physical and socio-economic system (Sabatier, 1988; Sabatier & Weible,
2007). Compared to the previous descriptive theories of problem-solving, the ACF assigns
a bigger role to the argumentative dimension of policy processes, although it also includes
specific factors that address the more political games of using resources strategically to
pursue specific interests.
a B a th � r a e e s r a i i p c b ( r u g o t o b e o l s e d o m ) f r B d o e i f a s s s n t o i r a c u i t b r u u c r e � a s o l n v F s s o o a u c c l n u i i d o a e a l - s c m a u n e lt d n u t r a a l l s ( B c r t o a u r n s u le i s c c � s t ) u tu re � onal c C s e o o c h o c n a i n d n o o i g - � m e o s i n c i s n C pu h b an lic g e o s p i i n n ion C s g c y o o h s a v a t l e e n i� r m g n o e i i n s n c g in o P d im o t e h c p li e i c a s r y c i o ts n s fr a o n m d
structure subsystems
Coali�on A Policy Coali�on B
Policy beliefs brokers Policy beliefs
resources resources
Strategy A StategyB
lobby lobby
Decision by
sovereigns
Ins�tu�onal rules, resource
alloca�on and appointments
Policy outputs
Policy impacts
Figure 2.7 Advocacy coalition framework (own work after Sabatier, 1988)
42

smelborP
2 Problem formulaTIon In ComPlex envIronmenTs
2.4 Points of Intervention
In the previous sections we discussed that policy-making is neither straightforward nor a
scientific process, rather it is haphazard and strategic and political in character. Solutions
depend on the willingness of coalitions, political opportunism or the activity of policy
entrepreneurs. The question arises: what kinds of solutions do fit what kinds of prob-
lems? Our task as the analyst is even more complicated; we noted in earlier sections that
causes are hard to identify since various actors have different problem formulations, and
normative positions determine what is considered problematic in situations. And what is
more, complex problems – even if consensus exists – may have various causes and it is
hard to distinguish between root causes and symptoms. Nonetheless, we will distinguish
between different categories of solutions. Fundamental solutions address the cause of
a problem situation and are more effective than solutions that focus more on the con-
sequences of a problem (i.e. the characteristics of the problem situation). This explains
why these latter measures are often referred to as the treatment of symptoms. There is
a third category of solutions, i.e. solutions that seek to modify standards, or the level of
ambition that is coupled to the desired situation. Lowering the standard is another way of
closing the gap without much fuss. Finally, a fourth solution is to alter the perception of
the problem by providing information, by reframing or by ridiculing and trimming down
the problem (Text box 2.7).
Text box 2.7 Example of fundamental, consequential or norm relaxation approaches
As an illustration we take a look at the nitrate debate in the Netherlands. In early 2019 the
Netherlands Supreme Court decided that no building permits would be granted as long
as there would not be a guarantee for zero nitrate emissions because of these activities.
Construction permits were halted, the problem was getting out of hand and somewhere,
somehow somebody should provide a quick solution to reduce nitrate emission in the
Netherlands. One member of Parliament suggested that – as cattle farmers alone are
responsible for 43% of the nitrate emissions in the Netherlands (and nitrate is poisoning our
groundwater) – the number of cattle farms should be reduced by 50%. This remark sparked
intensive farmer’s protests culminating in two days of protests by farmers driving their tractors
to the seat of the Netherlands Parliament: The Hague. A fundamental solution indeed would
be to reduce the number of farms emitting nitrates, especially NH. Treating the consequences
3
would focus on installing air washers, removing topsoil of contaminated nature reserves,
anticipating new cleaning technologies and the like. Reducing the level of ambition was also
suggested, especially by the farmers as other economic sectors (like air transport) should also
contribute. Finally, many farmers suggested the problem was overestimated as on their way
to the protest manifestations in The Hague they had been passing flowering heather, so the
problem could not be as bad as suggested by these politicians.
The aim of the problem specification process therefore also is to obtain clarity and con-
sensus about the intervention aspects of an issue. It is then possible to develop measures
that address one or more of these four aspects, depending on the availability and accept-
ability of means. Figure 2.8 shows the aspects of a problem formulation as a stepping
stone for solutions. A final remark on interventions may be useful though. It was sug-
gested that problems can be solved by reducing ambitions, but a strategy may also be
43

Problems
Policy AnAlysis of Multi-Actor systeMs
to raise the ambition levels. For instance, in its 2020 State of the Union address, the EU
Commission raised its climate ambition and proposed a 55% cut in emissions by 2030.6
So lowering the ambition level may not always be the right way of dealing with a problem!
Perceptions may be addressed, but not always to lower expectation but for instance to
make people aware of problems. Raising the EU ambitions in this respect is a clear sign
and warning to European countries to start implementing measures and to other world
players like the USA, China and India to raise their ambitions too.
Influencing ambition
Desired situation
level
Influencing perceptions
Perceptions
through information
Characteristics and
Influencing effects and
consequences of existing
impacts
or expected situation
Cause of the situation Influencing causes
Figure 2.8 Problem formulation and points of intervention (inspired by Koppenjan,
1990)
Summarizing what we said about the activity of problem formulation and intervention
a number of functional requirements can be derived from the earlier sections. They are
(a) the need for joint problem formulation, (b) the need for accepted knowledge often
derived through stakeholder involvement, joint fact-finding and negotiated knowledge,
(c) the need for understanding the importance of the political process for creating a coali-
tion of the willing, (d) agreement on the point of intervention.
2.5 Problem Formulation as First Step in Problem Analysis
Problem analysis and problem formulation is an activity that is fundamental to the prob-
lem-solving process. Formulating the problem in an adequate manner is a necessary con-
dition for finding good solutions. However, it is easier said than done. As indicated in
Chapter 1, the progress of the analysis and problem-solving process is determined to a
large extent by choices that are made during the problem formulation process. Therefore,
6 https://ec.europa.eu/commission/presscorner/detail/en/ip_20_1599.
44

smelborP
2 Problem formulaTIon In ComPlex envIronmenTs
it is of the utmost importance to spend enough time and attention to problem f ormulation
and demarcation. Handbooks suggest that problem exploration may take up 20 to 25% of
the total time needed for problem-solving!
In this book we presume multi-actor complexity as previously mentioned. We intro-
duced a situation where the policy analyst is asked by a client (problem owner)7 to give
support and make suggestions for other approaches. The problem will be positioned in
a complex multi-actor environment. The role of the analyst is that of policy advisor (see
Chapter 1): from the viewpoint of a client or problem owner an analysis is conducted and
a strategy is developed aimed at improving the situation that is perceived as a problem
by that actor.
In many cases, the analyst’s first impressions of the problem come from the problem
owner’s formulation: ‘Traffic safety is affected negatively because a lot of car drivers make
telephone calls while driving. We have developed a portable phone which can be used
hands-free in a car, eliminating the problem mentioned above’ or ‘Trucks cause pollution,
so we have to try to move haulage transport from the road to the railway network.’ It is not
advisable though for analysts to uncritically accept the problem formulation of potential
clients. This even constitutes a disservice to the client. Experience teaches us that most of
these first impressions of the problem do not stand up to criticism. The problem formula-
tion often points too strongly in the direction of a specific solution, and many times other
important actors involved in the tackling of the problem turn out to have a different view
on it. Sometimes closer analysis shows that the first impressions of a problem are wrong,
in part or wholly, or an assessment of the future points to the likelihood of the problem
disappearing in time without intervention by the problem owner. Also, we see situations
with many different problem perceptions present, where framing and disinformation and
even disruptive communication by social media may play a role. Examples are climate
change denial, Trump’s campaign on the ‘stolen elections’ or the conspiracy theories on
vaccination with microchips during the COVID-19 pandemic.
What then distinguishes good problem formulations from bad ones? Unfortunately,
there is no final answer (‘good’ also depends on the perceptions of actors), but there are
a number of characteristics that can be used to distinguish the better (or improved) prob-
lem formulation from the not so good ones. A good problem formulation must be con-
vincing because of (a) the scope of the approach that was followed (that made sure that
nothing important was overlooked), and (b) the consistency and clarity in the argumen-
tation of the choices that were made. Good problem formulations are characterized by:
– a clear and well-thought-out introduction to the problem (context, history);
– a precise identification of the client and other relevant stakeholders, those that can
affect or are affected by the problem or its solution (see: Bryson, 2004);
– a concise description of the problem from a multi-actor perspective (what is the
desired situation and how is that measured,8 what is the present or expected situation
and what is the gap between these two situations?);
7 Problem owner is a term that is not used in a tender procedure, instead client or commissioner is used.
8 Also shown in an objectives tree.
45

Problems
Policy AnAlysis of Multi-Actor systeMs
– a demarcation of the aspects9 and factors that are important10 (what does the problem
relate to?);
– an overview of potential solutions;11
– a concise description of the main uncertainties in the context of the problem that may
influence the problem, its demarcation and/or the effectiveness of proposed solutions;
– an overview of existing knowledge gaps;
– an indication of strategic threats and opportunities (the context of the analysis, how to
fit into the whole process of problem-solving);
– a description of the basis of support, sketching what other actors are needed in the
process of problem-solving.
From these we determine that a thorough and in-depth problem formulation pays atten-
tion to the causes of the problem (factors) as well as to the context of the problem (the
views on the problem and the solutions of other actors involved and aspects that the
client did not think were relevant). To achieve all of this, a large variety of analytical tech-
niques are available to the analyst. In the next chapters we will present a number of basic
techniques which can serve as a starting point for analysing complex problem situations.
In Table 2.4 a sequence of analytical steps is presented that supports problem for-
mulation. This general sequence, although with the premise that it is an iterative and
interactive activity, is reported in many scholarly articles and books such as (Checkland,
1985; Thissen, 2000; Thissen & Walker, 2013; van der Lei et al., 2011). These activities may
be considered standard procedure for any problem analysis, no matter whether it is a
tamed or untamed problem. Beware that during the very first stage of problem analysis
in Table 2.4 indicated as ‘put into words the problem formulation of the problem owner’,
our inquiry or research aims at verifying whether the suspicion of a problem is grounded
or not (is there a problem that one or more actors experience?); finding out what the most
important characteristics of the problem are, both technically or in terms of content, and
whether they are socially or actor related; and working out what the best direction is for
finding solutions. The final step of this preliminary exploratory research is to reformulate
the problem and draft an accompanying plan for further research, including one or more
research questions posed by the analyst.
This very first step is aimed at preventing miscommunications between the analyst and
the client, by presenting a clear and structured picture of the initial problem formulation.
This step is not so much about the verification of a problem (is this problem formulation
correct?), but about the exact formulation of words, which reflects the problem perception
of the problem owner/commissioner. Even though it may not be possible to pay attention
to all these points, the requirements for good problem formulation from the previous
section can serve as some form of guideline. This initial problem (re-)formulation by the
analyst gives the client something to think about because the initial problem formulation
by the client is often one-sided, unclear, incomplete, consisting of contradictory elements
and/or conflicting goals and is often aimed at implementing a preferred solution.
9 Aspects = a cluster of coherent factors.
10 Also depicted in a causal map and a system diagram. Note that when a factor does not appear in these
diagrams, this indicates that this factor is considered to be not important. The term ‘demarcation’
denotes this ‘drawing the line’ between what is important and what is not (see Chapter 3).
11 Also depicted in a means-ends diagram (see Chapter 3).
46

smelborP
2 Problem formulaTIon In ComPlex envIronmenTs
The second step consists of an initial, critical analysis and subsequent reformulation
and delineation of the problem, using techniques such as objectives trees, causal map-
ping and means-ends analysis. This critical analysis and problem reformulation stays
within the boundaries of the interests and perspective of the client. It is discussed in the
next chapter on systems analysis.
However, problems and their owners do not operate in a vacuum. For example, the
traffic problem of the container shipper is inextricably connected to the plans of a railway
company regarding a new railway to inland areas, the different public authorities whose
area the proposed railway will cross, the residential areas that are going to be traversed, the
landscape and its inhabitants and so on. All these contextual factors and actors influence
in turn the problem situation. The third step therefore is an actor and network analysis,
which is aimed at systematically mapping out these relevant contextual factors (particu-
larly the varied perceptions and intentions that exist) and analysing the institutional con-
text and the interdependencies between the problem owner and the other actors. More
detailed information about the actor and network analysis can be found in Chapter 4.
Problems, problem situations and actor configurations are not stable but may change
over time and most often contextual factors change too. Therefore, the fourth step takes
a systematic look at important plausible future developments in the problem context. For
more information about dealing with uncertainties in the future, we refer you to Chapter 5.
In the next step, a balance is drawn: to what extent must and can the problem be refor-
mulated, by choosing different objectives, a different demarcation or by considering a
larger number of interested actors/stakeholders as joint problem owners? The conse-
quences for the continuation must be formulated: Is the problem worth tackling? Does
action need to be taken towards other actors? Is a more detailed analysis necessary, and
if so, a more detailed analysis of what, and in which way? Chapter 6 deals with the charac-
terization of the problem and thinking up of follow-on activities.
An overview of the different steps and the most important techniques that can be used
in performing a problem analysis are shown in Table 2.4. Note, however, that the head-
ing ‘sequence of steps’ falsely suggests a logical sequence of these activities. In practice,
these activities form part of an iterative process and the steps mentioned do not always
have to be followed in the order suggested. Situations may arise in which one or more
steps are disregarded. It is important to realize that the sequence is a guideline and noth-
ing more. Specific problems ask for a specific approach.
47

Problems
Policy AnAlysis of Multi-Actor systeMs
Table 2.4 Sequence of steps
Step Techniques, Chapters
Initial problem formulation: put into words the Interviews, literature
problem formulation of the problem owner See: Chapters 1 and 2
System exploration and delineation:
Choice of problem definition level and objectives Means-ends diagram
Specify criteria Objectives tree
Identify and structure relevant factors
Identify possibilities of influence and constraints Causal map
Synthesis and consistency check System diagram
See: Chapter 3
Actors and network analysis Stakeholder grid, formal chart, etc.
Institutional and stakeholder analysis See: Chapter 4
Study of the future Trend-extrapolations and contextual scenarios
See: Chapter 5
Synthesis, consistency check and reformulation of the Among others system diagram
problem See: Chapter 6
Draw up a plan of action and a research plan Various
See: Chapters 7 and 8
2.6 Takeaways
– Problem-solving is not a rational activity.
– Problem-solving and (political) decision-making processes at the level of complex sys-
tems, networks and chains are not chronological, but rather extremely unstructured.
– Complexity is anchored more often in the multi-actor situation with competing values,
political ideas and interests than in the technology.
– Policy analysis may add sense and content to the problem-solving process.
– The political process may not be in need for scientific analysis, rather looking for infor-
mation or supportive evidence.
– A well-formulated problem is the right starting point for problem analysis.
References
Checkland, P. B. (1985). Formulating Problems for Systems Analysis. In H. J. Miser
& E. S. Quade (Eds.), Handbook of Systems Analysis. Overview of Uses, Procedures,
Applications, and Practice. Elsevier Science Ltd., ISBN: 9780444009180. pp.9-48
Cobb, R. W. & Elder, C. D. (1983). Participation in American Politics. The Dynamics of
Agenda-Building. Baltimore: John Hopkins University Press.
Cohen, M. D., March, J. G. & Olsen, J. P. (1972). A Garbage Can Model of Organizational
Choice. Administrative Science Quarterly, 17(1), 1-25. https://doi.org/10.2307/2392088.
de Bruijn, H. (2019) The Art of Political Framing How Politicians Convince Us That They
Are Right. Amsterdam University Press, Amsterdam.
de Bruijn, H., Heuvelhof, E. ten & Veld, R. in ’t (2002). Process Management. Why Project
Management Fails in Complex Decision Making Processes. Boston: Kluwer Academic
Publishers.
48

smelborP
2 Problem formulaTIon In ComPlex envIronmenTs
de Bruijn, H. & Porter, A. L. (2004). The Education of a Technology Policy Analyst – to
Process Management. Technology Analysis & Strategic Management, 16(2), 261-274.
https://doi.org/10.1080/09537320410001682919.
Douglas, M. & Wildavsky, A. (1982). Risk and Culture: An Essay on the Selection of
Technical and Environmental Dangers. Berkeley: University of California Press.
Dunn, W. N. (1981). Public Policy Analysis: An Introduction. New York: Prentice-Hall.
Durning, D. (1993). Participatory Policy Analysis in a Social Service Agency: A Case Study.
In: Journal of Policy Analysis and Management v12 n2 (19930401): 297-322
Enserink, B. (2005). Public Participation in Dutch Watermanagement: Pragmatism
in Meeting EU Requirements. In P. H. Feindt & J. Newig (Eds.), Partizipation,
Öffentlichkeitsbeteiligung, Nachhaltigkeit. Perspektiven der politischen Ökonomie
(pp. 203-227) (Ökologie und Wirtschaftsforschung, Band 62). Marburg: Metropolis
Verlag.
Enserink, B. & Koppenjan, J. (2007). Public Participation in China: Sustainable
Urbanization and Governance. Management of Environmental Quality: An International
Journal, 18(4), 459-474. https://doi.org/10.1108/14777830710753848.
Enserink, B., Hermans, L., Kwakkel, J., Thissen, W., Koppenjan, J. & Bots, P. (2010). Policy
Analysis of Multi-Actor Systems. Den Haag: Boom/Lemma.
Greenwood, R., Raynard, M., Kodeih, F., Micelotta E. R. & Lounsbury, R. (2011).
Institutional Complexity and Organizational Responses. The Academy of Management
Annals, 5(1), 317-371. http://doi.org/10.1080/19416520.2011.590299.
Hendriks, F. & Toonen, T. A. J. (Eds.) (2001). Polder Politics: The Re-Invention of Consensus
Democracy in the Netherlands (reissued 2018 by Routledge, London).
Hogwood, B. W. & Gunn, L. A. (1984). Policy Analysis for the Real World. Oxford: Oxford
University Press.
Hoogerwerf, A. (1987). De levensloop van problemen: definiëring, precisering en oplossing.
Beleidswetenschap, 1, 159-181.
Hoogerwerf, A. (1992). Het ontwerpen van beleid. Een handleiding voor de praktijk en
resultaten van onderzoek. Alphen a/d Rijn: Samsom HD Tjeenk Willink.
Hoogerwerf, A. (red.) (1998). Het ontwerpen van beleid. Een handleiding voor de praktijk
en resultaten van onderzoek. Alphen a/d Rijn: Samsom H.D. Tjeenk Willink.
Keeney, R. L. & Raiffa, H. (1977). Conflicting Objectives in Decisions. Chichester: John
Wiley & Sons.
Kingdon, J. W. (1984/1995). Agendas, Alternative and Public Policy. Boston: Little, Brown
and Company.
Klijn, E. & Koppenjan, J. (2014) Complexity in Governance Network Theory. Complexity,
Governance & Networks, 1(1). https://doi.org/10.7564/14-CGN8.
Klijn, E. H. & Koppenjan, J. (2016). The Shift toward Network Governance: Drivers,
Characteristics and Manifestations. In Klijn, E.H., & Koppenjan, J. (2016) Theory and
Practice of Public Sector Reform (pp. 158-177). Routledge, London.
Koppenjan, J. F. M. (1990). Definiëring van complexe problemen door de overheid:
balanceren tussen ruim en precies. Beleidswetenschap, 4(1), 21-45.
Koppenjan, J. & Klijn, E. (2004). Managing Uncertainties in Networks. New York and
London: Routledge.
Mayer, I., 1997. Debating Technologies: A Methodological Contribution to the Design
and Evaluation of Participatory Policy Analysis (PhD thesis)Mayer, I. S., van Daalen,
C. E. & Bots, P. W. G. (2004). Perspectives on Policy Analysis: A Framework
49

Problems
Policy AnAlysis of Multi-Actor systeMs
for Understanding and Design. International Journal of Technology, Policy and
Management, 4(2), 169-191. https://doi.org/10.1504/IJTPM.2004.004819.
Monnikhof, R. (2006) Policy Analysis for Participatory Policy Making (PhD thesis TU
Delft).
Olson, R. (2019). Narrative Is Everything. The ABT Framework and Narrative Evolution.
Independently Published ISBN: 9781072232575.
Pauly, S. (2001). Ambiguïteit in het spel. De casus PolyVinylChloride (PhD thesis). Delft:
Eburon.
Qiu, Y., Chen, H., Sheng, Z. & Cheng, S. (2019) Governance of Institutional Complexity
in Megaproject Organizations. International Journal of Project Management, 37, 425-
433. https://doi.org/10.1016/j.ijproman.2019.02.001.
Rein, M., Schön, D. (1996) Frame-critical policy analysis and frame-reflective policy
practice. Knowledge and Policy 9, 85–104. https://doi-org.tudelft.idm.oclc.org/10.1007/
BF02832235
Rittel, H. W. J. & Webber, M. M. (1973). Dilemmas in a General Theory of Planning. Policy
Sciences, 4, 155-169. https://doi.org/10.1007/BF01405730.
Sabatier, P. A. (1988). An Advocacy Coalition Framework of Policy Change and the Role
of Policy-oriented Learning Therein. Policy Sciences, 21(2-3), 129-168. https://doi.
org/10.1007/BF00136406.
Sabatier, P. A. & Jenkins-Smith, H. (1988). Policy Change and Policy-Oriented Learning:
Exploring an Advocacy Coalition Framework. Dordrecht: Kluwer.
Sabatier, P. A. & Weible, C. M. (2007). The Advocacy Coalition Framework: Innovations
and Clarifications. Theories of the Policy Process (pp. 189-220). Boulder: Westview Press.
Schattschneider, E. E. (1960). The Semisovereign People: A Realist’s View of Democracy in
America. New York: Holt, Reinhart and Winston.
Simon, H. A. (1973). The Structure of Ill-structured Problems. Artificial Intelligence, 4,
181-201.
Simon, H. A. (1977). The New Science of Management Decision. Upper Saddle River:
Prentice Hall PTR.
Simon, H. A. (1991). Bounded Rationality and Organizational Learning. Organization
Science, 2(1) (Special Issue: Organizational Learning: Papers in Honor of (and by)
James G. March), 125-134. https://doi.org/10.1287/orsc.2.1.125.
Teisman, G. R. (1992/1995). Complexe besluitvorming. Een pluricentrisch perspectief op
besluitvorming over ruimtelijke beslissingen. Den Haag: VUGA.
Teisman, G. (2000) Models For Research into Decision-MakingProcesses: On Phases,
Streams and Decision-Making Rounds. Public Administration 78(4), 937 – 956.
https://doi.org/10.1111/1467-9299.00238
Thissen, W. A. H. (2000). Issue-Formulation in a Multi-Actor Context: A Five Step
Approach. Proceedings of the IEEE Conference on Systems, Man and Cybernetics
(pp. 301-306).
Thissen, W. (Ed.) & Walker, W. (2013). Public Policy Analysis: New Developments.
(International Series in Operations Research & Management Science). Springer New
York Heidelberg Dordrecht London.
van Bueren, E. M., Klijn, E. & Koppenjan, J. F. M. (2003). Dealing with Wicked Problems
in Networks: Analyzing an Environmental Debate from a Network Perspective. Journal
of Public Administration Research and Theory, 13(2), 193-212. https://doi.org/10.1093/
jpart/mug017.
50

smelborP
2 Problem formulaTIon In ComPlex envIronmenTs
van de Graaf, H. & Hoppe, R. (1989). Beleid en politiek. Een inleiding tot de
beleidswetenschap en de beleidskunde. Muiderberg: Coutinho.
van de Poel, I. & Royakkers, L. (2011). Ethics, Technology, and Engineering. Chichester:
Wiley-Blackwell.
van der Lei, T. E., Enserink, B., Thissen, W. A. H. & Bekebrede, G. (2011). How to Use a
Systems Diagram to Analyse and Structure Complex Problems for Policy Issue Papers.
Journal of the Operational Research Society, 62(7), 1391-1402. https://doi.org/10.1057/
jors.2010.28.
Wildavsky, A. (1979). The Art and Craft of Policy Analysis. Hampshire and London:
MacMillan Press.
WRR (Netherlands Policy Research Council) (1994). Besluiten over grote projecten (Report
No. 46). The Hague: SDUB.
51

smetsyS
3 Systems Analysis
In this book, we provide analytical tools and
“Systems analysis is to a large methods to structure multi-actor problem
extent a craft activity in which situations that are ill-structured, messy and
skilled persons draw upon the wicked. Various perspectives and disciplines
knowledge and tools of many dif- have put forward analytical tools and meth-
ferent sciences and technologies to ods, but a logical place to start is systems
create a product responsive to the analysis. Systems analysis is the approach
needs of the eventual users” that evolved in the 1950s and 1960s from the
(Miser and Quade, 1985: 29) field of operations research. Systems analysis
applied scientific, and often mathematical,
approaches to investigate and solve problems
in large systems. For many policy analysts the analysis methods and approaches that were
developed for systems analysis form an important part of their toolbox. This chapter pro-
vides an introduction to analytic thinking and to some of the methods that are most use-
ful to support problem formulation and problem exploration in the early stages of policy
analysis: means-ends analysis, objectives trees, causal diagrams and system diagrams.
However, we will start with a brief introduction to the field of systems analysis and its use
by policy analysts.
3.1 Introduction to Systems Analysis
Systems analysis applies scientific methods to analyse large and complex systems. When
applied as part of policy analysis processes, the system under study is typically a cer-
tain policy domain, seen from the perspective of a policy-maker, client or, more basically,
someone who thinks there is a problem (Findeisen & Quade, 1985). Systems analysis
seeks to map and analyse this system, and structure the problem, through a way of work-
ing that is open and explicit, empirically based, consistent with existing knowledge and
for which the results are verifiable and reproducible (Walker, 2000: 12). In addition to
applying scientific methods, systems analysis is scientific in that it seeks to develop and
test ‘theories’: causal assumptions of how the world works. Systems and policy analysts
“speak of their theories as models, but the terms are really synonymous” (Miser & Quade,
1985: 19). Another key feature of systems analysis is the recognition that the complexity
of the systems that are studied is such that complete certainty is impossible, and that
systems analysis is essentially an art and a craft, drawing on tacit and informal methods,
in addition to formal and explicit approaches (Miser & Quade, 1985).
The systems analysis approach that we describe in this chapter grew out of the opera-
tions research field and historically is connected to the work of institutes such as the
RAND Corporation, a US-based think tank, and the International Institute for Applied
Systems Analysis (IIASA). This means that we will not be discussing the full range of sys-
tems theories such as cybernetics, general systems theory, system dynamics and complex
53

Systems
Policy AnAlysis of Multi-Actor systeMs
adaptive systems, but will focus on applied systems analysis. An overview of system theo-
ries and approaches, including systems analysis, can be found in Jackson (1992), Daalen
& Bots (2010) and Slinger et al. (2020).
The primary advantage of using a systems analysis approach is that it helps to put
some structure to complex and ill-defined policy fields. It helps analysts to make their
own assumptions and expectations explicit, providing a basis for communication with
clients, as well as with fellow analysts. Furthermore, the field of systems analysis is rich in
useful guidelines, tools and techniques, enabling an analyst to develop detailed and com-
prehensive models of a policy domain. This in turn can help them in advising their clients
about possible courses of action in a particular problem situation. Even if systems analysis
cannot provide complete and detailed prescriptions in a particular situation, it can almost
always eliminate the really bad alternatives (Miser & Quade, 1985). In this chapter, we
focus on the early stages of systems analysis in which a system diagram of the problem
situation is developed as part of problem structuring.
A known limitation of systems analysis is that it is necessarily incomplete, not only
because of practical limitations in terms of time, money or human resources but also
because it simply cannot synthesize all potentially relevant considerations (Miser &
Quade, 1985). This means that during problem structuring an analyst must make choices
about what to consider, what to include as part of the analysis and what aspects are left
outside the scope of analysis. As a result, uncertainties remain. The uncertainties increase
even more when we take into account that many policy decisions apply for long periods of
time. No-one can know how the system will evolve, what it will look like in two, five or ten
years from now. To address this limitation, Chapter 5 discusses some methods for explor-
ing the future. Also, systems analysis generally starts from the perspective of a specific
problem owner. Multi-actor considerations are usually accommodated by applying stan-
dard methods and then iterating, but standard systems analysis was not specifically devel-
oped to function in multi-actor policy systems. If the multi-actor complexities are many
and pervasive, additional approaches and reflexive iteration will be needed to incorporate
them in a policy analysis. Some of the additional approaches are discussed in Chapter 4,
while the reflexive iteration is discussed in Chapter 6.
3.2 Conceptual Framework for Systems Analysis
Meaningful discussion of systems analysis tools and methods requires a basic description
of what we mean when we speak of a system. If our aim is to analyse a certain ‘system’,
then what is this object of analysis, what are the main concepts involved and how are
these structured and related?
3.2.1 The System Diagram and Its Components
A system is defined as a part of the reality that is being studied as a result of the existence,
or suspicion, of a problem. An analyst makes a system model that clarifies the system
by (1) defining its boundaries and (2) defining its structure – the main elements and the
relationships among them (Walker, 2000: 13). The question of which part of reality, which
system, is relevant for further analysis is directly related to the problem perspective that
is adopted.
We have seen that a problem implies a perceived gap between an existing or expected
situation and a desired situation, and the person who perceives the gap wants to know
54

smetsyS
3 sysTems analysIs
what can be done about it (see Chapter 1; Checkland, 1985). This means that a system
model is actor-specific: it describes the system from the viewpoint of a specific actor. It
also implies that a system is relevant only because it influences the realization of a certain
desired situation. The desired situation is generally described in terms of objectives. The
realization of objectives is measured through the use of criteria that are linked to the main
outcomes of interest of a system (Walker, 2000: 13).
Another part of our definition of a policy problem concerns the possible means to ‘do
something about it’. A problem owner should have some means (e.g. policy instruments)
through which she/he can influence the system, improving the degree to which objectives
are being realized. Since we are dealing with complex problems, the means generally do
not influence the outcomes of interest directly. Instead, the outcomes are influenced indi-
rectly through elements inside the system, which are called internal factors. By a factor
we mean a system property that is taken into account. The influences of the means on the
internal factors and ultimately on the criteria are causal influences. In systems analysis,
the focus of attention often lies on the internal factors and their interrelationships as these
determine how influences propagate through the system.
Finally, there are likely to be some important influences on the system from the external
environment, factors from outside the system over which the decision-maker or problem
owner has no control (Checkland, 1985; Walker, 2000). These external factors are ele-
ments that cannot be influenced by the problem owner or by the factors inside the system,
but that can have an important influence on the behaviour of the system.
Depicting these elements leads to a system diagram, as shown in Figure 3.1. It consists
of the system demarcation, the boundary, with three groups of factors at the boundary:
the means of the problem owner, the external factors and the criteria. The direction of the
arrows shows that the means and the external factors influence the system, and that these
influences propagate through the internal factors of the system, eventually influencing the
criteria.
external factors
means system criteria
(internal factors)
Figure 3.1 General elements of a system diagram
When the system diagram is filled in for a particular problem situation it provides a struc-
tured overview of the problem situation. It supports the problem owner in gaining insight
into the problem situation and analysing whether his/her objectives can be attained. For
instance, the system diagram can be used to explore whether a particular means that leads
to desired changes in one criterion also has positive effects on other criteria or not. The
55

Systems
Policy AnAlysis of Multi-Actor systeMs
sensitivity of the criteria to changes in external factors can also be analysed. Key internal
factors can be determined and (additional) means to influence these can be identified.
Such a filled-in system diagram is a conceptual model of a problem situation. A concep-
tual model is a representation of a system that shows relevant concepts and relationships
between the concepts. The uses of a system diagram are discussed further in Section 3.5.
3.2.2 Interests, Objectives, Criteria and Means
The terms ‘interest’, ‘objective’, ‘means’ and ‘criterion’ all have to do with the point of
view of one or several actors. Because a lot of confusion exists about the exact meaning of
these different terms, we provide working definitions here.
By interests we mean the values and desires that an actor finds important, regardless
of the specific situation. Interests are usually formulated in an abstract way and they are
relatively stable over time. They are often referred to as categories: social interests include
issues such as equity and social justice, environmental interests include biodiversity and
ecosystem health, economic interests include economic growth and competitiveness and
so on. There are different organizations and groups in most countries that protect these
kinds of interests. Think of human rights organizations, environmental protection organi-
zations, branch organizations of employers and employees, women’s organizations, car
owner groups and so on. On an individual level interests such as good health, a good
income and so on can be categorized as interests. These interests are sometimes called
‘fundamental objectives’ (Keeney, 1992).
Objectives differ from interests in that they are specific to a situation. Objectives belong
to a particular problem or project. Objectives are interests made concrete, which translate
to current policy issues. An actor will strive to achieve a situation-specific objective in
order to ultimately realize his/her interests. The general interest ‘a healthy environment’
of an environmental protection organization could translate into the objective ‘low nitrate
concentration in groundwater’ when the organization discusses the problem of polluted
groundwater due to over-fertilization. When discussing the planned extension of a high-
way in a green belt area, the same interest ‘a healthy environment’ can translate into the
objectives ‘large area of open meadow landscape’ and ‘low noise nuisance’. In both cases,
the preservation of the environment is the underlying interest, but the objectives differ.
In common language use, objectives can be formulated freely, for example, in terms of
verbs, nouns or constraints. In systems analysis we formulate objectives using nouns pre-
ceded by relative adjectives, such as high or low, large or small, to indicate the direction of
the desired situation. Formulating objectives as nouns with relative adjective allows us to
use the objectives to determine the relevant criteria.
Criteria are objectives operationalized in terms of factors for which a value can be estab-
lished on a scale, via direct or indirect measurement. Objectives can be fairly abstract, for
instance high traffic safety. Operationalization of traffic safety produces criteria such as
‘number of casualties per year’ and ‘number of accidents per year’ (measured by count-
ing), ‘probability of being involved in an accident’ (measured as the ratio of accidents in a
year over the total distance travelled by all travellers in that year), ‘material damages as a
consequence of accidents per year’ (measured in Euros per year) and so on. As they can
be measured, criteria can be used to determine whether the desired situation has been
attained.
56

smetsyS
3 sysTems analysIs
By means1 we mean any actions that can be used in order to achieve an objective. This
implies that means and objectives are related to each other. Like objectives, in common
language use means can be described in global terms, such as ‘money’ or ‘legislation’, but
they can also be specified more precisely, e.g. ‘subsidize biological products’ or ‘forbid the
use of pesticide X’.
Figure 3.2 Meaning depends on perspective
The distinction between objectives and means is not absolute. This ambiguity is similar to
that of Figure 3.2: whether the image depicts a bird or a rabbit depends on the perspective
one takes. Likewise, what may be a means to one actor can be an objective to another.
From a government perspective, subsidizing biological products and forbidding the use
of pesticides are possible means to achieve the objective of an ecologically friendly agri-
cultural sector, while from the perspective of an environmental protection organization,
low use of pesticide X and high subsidy on bio-products are objectives, since an environ-
mental protection organization cannot itself reduce the use of pesticides. A single actor
may also experience this ambiguity: an automobile manufacturer may see the high safety
of a car as an objective (and see installing airbags as a means to achieve this), but also as
a means for high car sales (combined with other means, such as a publicity campaign that
highlights the safety features of the car).
Interests, objectives, means and criteria play an essential part in problem structuring.
Knowledge of the interests, objectives and means of actors is necessary in order to reach
a meaningful problem description. The example in Text box 3.1 illustrates this.
Text box 3.1 Interests, objectives and means: Bicycle helmets example
The requirement for cyclists to wear helmets: an exploration of a policy problem
In various countries the use of helmets has become mandatory for cyclists. In the Netherlands
this is currently not the case. Cyclists are a relatively vulnerable group of road users and it
may be possible to improve safety by requiring them to wear helmets. Suppose that, with
forthcoming elections in mind, a popular politician has called for it to become compulsory for
cyclists to wear crash helmets, and for this measure to take immediate effect.
1 The singular of ‘means’ is also ‘means’; one may look for a means as well as for different means to attain
a goal.
57

Systems
Policy AnAlysis of Multi-Actor systeMs
What is the problem here? The answer will depend on who is giving it. What possible different
perspectives on this problem exist, and which will be useful to elaborate further?
Is the problem an excessively high accident rate among cyclists? Or is it more specifically the
number of fatal and serious accidents? A number of factors may contribute to the problem:
increased traffic, insufficient attention to road safety in primary education, unsafe road
infrastructure, slow and fast (electric) bicycles in the same lanes, youthful overconfidence, use
of mobile phones while cycling, an over-representation of vulnerable older cyclists who are
somewhat slower to react or other road users who are not careful or not paying attention.
What then is the problem that the analyst is expected to address? He/she must first find out
whether the problem actually exists, define it in detail and then investigate whether any policy
measures can be found to contribute to a solution of the problem, over which the client has
some form of authority. Assuming that the problem does indeed exist, the analyst will wish
to establish its true extent and scope. For example, how many accident victims are there per
travelled kilometre, and in which age categories are they to be found? How severe are the
injuries? How do these statistics relate to those of other groups of road users, using other
modes of transport? Such figures will indicate the extent and the boundaries of the problem.
For example, is it only the groups of cyclists over the age of 60 who have a higher-than-average
accident rate, or only the group aged under 18? Further information on this point and about,
say, the development of the issue over time can perhaps be gained by consulting the results of
similar or comparable studies.
Another part of the problem structuring will consist of establishing the position and influence
of the various individuals and groups concerned. Who is addressing this problem? Why?
What are their interests? What influence do they have on policy? In this example, interested
parties may include: the politician who raised the issue to win votes, the National Road Safety
Organization, police officers with a strong involvement in road safety, medical specialists
who wish to prevent serious injuries, insurance companies who wish to reduce treatment
expenditure, insured people who wish to pay lower insurance premiums, cyclists who wish
to maintain the freedom to ride without a helmet, the manufacturers and retailers of bicycles
(who may see their market share decline were helmets to be made compulsory), road
infrastructure companies who see a potential demand for reconstruction and perhaps many
others, such as school principals, the cyclists’ federation, helmet manufacturers, mobile
phone companies etc.
The example in Text box 3.1 shows that it is difficult to get a grip on a complex problem
situation. Investigating interests, objectives and means in a structured way can contribute
to understanding the complex problem. Next, we describe such a structured systems
analysis method to investigate a problem situation that results in a system diagram.
3.3 A Method to Develop a System Diagram
There are various ways to develop an adequate system diagram, which includes identify-
ing suitable system boundaries as well as the main factors and the important relations
among them. Here, we will use the following steps, each of which is supported by a spe-
cific technique:
1. set the initial problem demarcation and level of analysis;
2. specify objectives and criteria;
58

smetsyS
3 sysTems analysIs
3. identify potential means, and map the main causal relations with and between internal
factors, and their influence on the criteria;
4. provide an overview of the problem situation using a system diagram.
Taken together, these steps help to develop a first system diagram and to perform a first,
qualitative systems analysis, supporting a sound problem description. A system diagram
is a conceptual model of a problem situation. A model is a simplification of reality, and
problem structuring necessarily implies making choices. As an analyst it is important to
substantiate these choices and to iterate through these steps, to arrive at a sound problem
description.
3.3.1 Problem Demarcation: Means-Ends Analysis
In many cases, problems can be analysed at different levels. Choosing a useful level from
which to start the analysis is not always easy. However, the level at which a problem is ana-
lysed largely determines the problem demarcation, the spectrum of aspects/factors and
possible solutions that are taken into account. Hence it is worthwhile to spend time at the
beginning of an analysis looking at the different levels at which problems can be identified.
The first thing to find out is why a problem is important for a client. Means-ends analysis
therefore starts out by formulating the client’s dissatisfaction with the actual situation as
a verb sentence that expresses the desired situation. This verb sentence will typically be at
the core of the client’s problem, for example, ‘to have enough water even in dry summers’
for a farmer who sees his crops wither after weeks without rain. We call this verb sentence
an ‘end’. In common language ‘objectives’ and ‘ends’ may be used interchangeably to
describe a desired situation. However, we distinguish a desired situation formulated as a
verb sentence (end) from a desired situation formulated as a noun qualified by a relative
adjective (objective). We make this distinction because they are used differently in two
different analytic techniques. An ‘end’ (to have enough water even in dry summers) can
be reformulated into an ‘objective’ (large amount of water in summer) and vice versa. A
means-ends analysis uses the verb formulation because it makes use of the change of per-
spective illustrated in Figure 3.2. A means for one actor may be an objective for another,
therefore in a means-ends analysis all elements are formulated in an active sense as verbs.
The question to pose next is why this end is worth striving for? Does the end contribute
to the realization of a higher end? Asking this question several times, until a meaningful
answer cannot be given anymore, will result in a means-ends network2 (Gregory & Kee-
ney, 1994; Keeney, 1992). This ‘why’ exercise will reveal that there are fundamental ends,
and means-ends. The latter can be seen as ends, but they are also means to realize other,
more fundamental, ends. In the drought example, the farmer also wants to ‘have a good
crop’. If, when asked why this is worth striving for, he answers ‘Because I am a farmer!’
this would indicate that ‘have a good crop’ is a fundamental end. If he answers ‘To make
a living!’ this would suggest that switching from farming to another livelihood is conceiv-
able.
Having identified the client’s fundamental end, a means-ends analysis continues in the
opposite direction. For each end identified so far, the analyst now asks how (using which
means) this end can be achieved. This may identify additional conditions for the client to
2 Keeney calls this a means-end objective network. In order to avoid confusion with the objectives tree
technique which is explained in Section 3.3.2, we do not include the term ‘objective’ here.
59

Systems
Policy AnAlysis of Multi-Actor systeMs
be satisfied (e.g. have sufficient arable land, and fertile soil), and at the same time addi-
tional means for attaining an end (e.g. switch to drought-resistant crops and store water
during the wet season). Posing the how question is important because if nothing can be
done to realize a certain end, that end does not provide a very promising starting point
for a problem analysis as the problem owner apparently has no means to improve the
situation.
By first asking ‘why’ and then asking ‘how’, a means-ends analysis can, in principle,
cover the whole spectrum from concrete to abstract, from very specific actions up to the
fundamental end. The result permits a deliberate choice for a particular problem level. In
the drought example, the problem demarcation might range from very broad (‘ensure that
the client has sufficient income’) to very narrow (‘create an efficient water storage facil-
ity’). The example in Text box 3.2 provides a complete illustration of this process and of
how the resulting diagram helps in choosing the level of problem structuring.
Text box 3.2 City metro – Example of means-ends analysis
Suppose that the mayor of a city asks you to help her make more people use the metro. As an
analyst, you will first ask the why questions, and then the how questions.
Q: Why do you want to stimulate the use of the metro?
A: To reduce congestion in the city centre!
Q: Why do you want to reduce congestion in the city centre?
A: To make the city more attractive!
Q: Why do you want to make the city more attractive?
A: Are you daft? Because I am the mayor of the city!
Here you have reached a fundamental end, as it is essential for your client. So now you start
asking how questions:
Q: How can you make the city more attractive? Only by reducing congestion?
A: No, there are other ways. We are also considering renovating some of the older city districts,
and upgrading parks and other public spaces, but congestion hinders both business and
tourism, and therefore should have priority.
Q: Supposing that this is true (but you might want to have this checked!), is the metro line the
only means for reducing congestion? Some cities have effectively implemented congestion
levies, or have reduced congestion by regulating freight delivery, barring trucks during rush
hours.
A: No, but it might be worth investigating. We are considering creating additional park and ride
facilities in the city’s peripheral zone.
You can summarize this dialogue in the means-ends diagram of Figure 3.3. It shows that
the problem of getting more people to use the metro is embedded in another problem (the
congested city centre), which in turn is part of a larger problem (the city being unattractive
for business and tourists). It might be that some of the other means are more effective than
stimulating the use of the metro system. In general, it is sensible to choose an objective
on a more fundamental level because then the analysis will include a broader spectrum of
important objectives, and hence a broader spectrum of means will be taken into account.
60

3  sysTems analysIs
Please note that the means-ends diagram is split into an upper and lower part here only
for ease of reading. This is not standard practice; a means-ends diagram should consist of
one diagram. The rectangles represent means-ends, and arrows denote causal relations in
Figures 3.3 and 3.4.
make city
more attractive
| renovate      | reduce congestion | upgrade parks     |     |
| ------------- | ----------------- | ----------------- | --- |
| old districts | in city center    | and public spaces |     |
smetsyS
| regulate urban | stimulate | implement | raise parking |
| -------------- | --------- | --------- | ------------- |
freight distribution use of metro congestion pricing fees in center
Figure 3.3  Upper part of the means-ends diagram
For a complete means-ends analysis, you would now ask the how question for the other two
second-level means-ends, and for each of the four third-level means-ends. But assuming that
your client (the mayor of the city) prefers to focus on the objective ‘stimulate use of metro’,
repeatedly asking the question ‘How can you realize that goal?’ could lead to the part of the
means-ends diagram in Figure 3.4.
stimulate
use of metro
| reduce | improve |     |     |
| ------ | ------- | --- | --- |
ticket price  quality of service
| provide      |          | provide          |              |
| ------------ | -------- | ---------------- | ------------ |
| more comfort |          | faster transport |              |
| increase     | increase | stop at          | operate with |
train frequency  seating capacity  fewer stations faster trains
Figure 3.4  Lower part of the means-ends diagram
61

Systems
Policy AnAlysis of Multi-Actor systeMs
Rules for Constructing a Means-Ends Diagram
All diagramming techniques require that the analyst obeys certain notational rules. Only
when this convention is followed will the diagram be meaningful to other analysts and
permit logical interpretation. For means-ends diagrams, the following rules apply:
1. Rectangles denote means-ends. The text in a rectangle should be a verb phrase (‘stim-
ulate ...’, ‘improve ...’, ‘reduce ...’) because this preserves the ambiguity of a means-
ends: a verb phrase can be read as a means (‘we can improve the quality of service’)
and also as an end (‘we want to improve the quality of service’).
2. Arrows denote causal relations: it should be possible to read each arrow X → Y as in
‘if we do X, this will help to Y’, or (if the causal relation is less certain) ‘if we do X, this
will probably Y’ or ‘if we do X, this may Y’.
3. Arrows should point upwards. This rule guarantees that the most fundamental ends
are at the top of the diagram.
4. More than one arrow may proceed from the same rectangle. This rule is useful because
it may be that one means can contribute to the realization of several ends.
5. Each rectangle should have either none or more than one ingoing arrow. This rule
prohibits that the diagram suggests that an end Y can be realized by only one means
X. If that were the case, Y could be replaced by X, as the client has no choice. This rule
forces the analyst to keep the diagram as simple as possible.
6. The diagram should not contain redundant arrows. An arrow X → Z is redundant if the
diagram also contains some indirect path X → Y → ... → Z. Combined with rule 3, this
rule forces the analyst to place elements at the correct level, and to keep the diagram
as simple as possible.
Interpreting Means-Ends Diagrams
A means-ends diagram can help to choose the appropriate level for analysis by selecting
one particular end in the means-ends hierarchy and reformulating this as the focal objec-
tive. For example, the means-end verb phrase ‘reduce congestion in the city centre’ can
be reformulated as the focal objective ‘low congestion in the city centre’ since objectives
are expressed as nouns with a relative adjective. In general, a focal objective should be
fundamental enough to enable the problem owner to undertake different actions to solve
a problem without introducing considerations that are clearly irrelevant and that will add
unnecessary complexity to the analysis. Note that this implies that you cannot choose
one of the lowest means-ends for the focal objective. If you do want to focus on one of
these, then you should identify additional means. This is usually possible. For instance,
looking more closely at even the most straightforward means (e.g. ‘reduce ticket price’
in Figure 3.4) for an objective will still reveal a diversity of means for achieving it (lower
fares only outside rush hour, provide city passes for tourists, provide free transport for
students, etc.).
One way to test whether a particular end Z is suitable for a focal objective is to ask the
problem owner the following questions:
– ‘Do you agree that it is desirable to Z? And that when you succeed in achieving Z, your
main problem is solved?’
– ‘Do you agree that Z can be achieved by doing M, M, ... (the means immediately
1 2
below Z)? And that you indeed have the means to do this?’
– Do you agree that at this moment you lack the knowledge to decide whether you
should either M or M or ... , or a combination of these means?
1 2
62

smetsyS
3 sysTems analysIs
These questions test whether the conditions for a policy problem mentioned in Sec-
tion 1.2.3 are met: (1) is there a gap between an existing or expected situation and the
desired situation (the objective Z)? and (2) is there a dilemma, that is, a difficult choice
between possibilities that can (partly) close the gap, but also have undesirable outcomes?
If the problem owner disagrees on some of the questions, you shift the focus to finding
another objective in the means-ends diagram.
It is important to realize that even an elaborate means-ends diagram is only a ‘quick
scan’ of the client’s problem. Even when you agree on what should be the focal objective,
it is wise to also make problem statements based on the goals on the immediately adja-
cent levels because this will bring out the dilemmas involved. The arrows in a means-ends
diagram represent only the desirable causal relations; potential side effects of means are
ignored. A problem statement of the form ‘How can the client achieve [end Z related to
focal objective] without [undesirable side effects of the means immediately below Z]?’
makes the dilemma explicit. Taking the end ‘stimulate use of metro’ in Text box 3.2 for the
focal objective, a problem statement results in something like:
‘How can metro use be stimulated without incurring operating losses?’
or, if the mayor is concerned with the safety of passengers:
‘How can metro use be stimulated without people getting crushed during rush hour?’
Choosing the end on the next higher level in the means-ends diagram for the focal objec-
tive would produce different dilemmas. Considering the side effects of regulating freight
traffic, a possible problem statement could be:
‘How can the traffic congestion in the city centre be reduced without hampering commer-
cial transport?’
The idea of congestion levies may raise concerns regarding the high investments needed
to implement large-scale congestion-mitigating measures:
‘How can the traffic congestion in the city centre be reduced without incurring large finan-
cial costs?’
As raising the parking fees in the city centre may lead drivers to look for parking space in
the peripheral districts, this means introduces yet another dilemma:
‘How can the traffic congestion in the city centre be reduced without causing nuisance in
other parts of the city?’
Discussing the different problem statements with the client will be helpful in deciding
which problem to focus upon.
63

Systems
Policy AnAlysis of Multi-Actor systeMs
Other Aspects of Problem Demarcation
The problem demarcation is more than choosing the relevant level of analysis on the basis
of the objectives to be considered. Demarcations in space and time are also necessary in
determining the system boundary of the problem to be analysed.
Spatial demarcations focus on the physical scope of the problem situation. The geo-
graphical area affected by the problem is relevant when it comes to deeper analysis. For
example, is it wise to consider only the traffic congestion in the city centre? Here, again,
a critical attitude is desirable: has the question of whether the problem is local, regional
or national been considered; which spatial scale is most appropriate for the best solu-
tions? Could it be that the causes of the problem lie outside the area where the problem is
felt? Then that is where the most interesting solutions can be found, so the geographical
area should be widened. And even if only local measures are taken, do these have conse-
quences for a larger area? If so, this would also call for a wider spatial demarcation.
Temporal demarcations focus on the time frame within which one analyses the problem.
This demarcation is not always as clear because there is strong interdependence between
the different choices in problem structuring. The time frame is not only determined by the
question of when the problem arises but also by the characteristics of the solutions that
are being investigated. For example, changing the metro fares can be done within months
whereas constructing a new metro line is a matter of five years or more.
The problem demarcation results in an initial choice for the level of analysis on the basis
of the means-ends analysis and a specification of the spatial and temporal scales relevant
to the problem. In effect, the problem demarcation defines the boundary between what
is internal to the system and what is external to the system. We specify here that this rep-
resents an initial choice that can be iteratively refined as each of the steps in the problem
structuring process is executed.
3.3.2 Specify Objectives and Criteria: Objectives Tree
The means-ends analysis will have helped to determine the focal objective for the problem
analysis. When this objective is abstract or encompasses multiple aspects, it needs to be
defined in more specific terms. For this, a method for analysing objectives is used: the
objectives tree.
Objectives trees help analysts to find, in a relatively simple way, an answer to the ques-
tion: what exactly does the problem owner want? It helps the analyst to define a high-level,
abstract objective in terms of more specific lower level objectives. The lowest-level objec-
tives in the tree provide the criteria to be used for measuring the degree to which the
problem owner’s objectives are being met. These criteria can then be used to compare
and evaluate different means and combinations of means.
Constructing an objectives tree begins by considering the focal objective selected using
the means-ends diagram and then making one or more problem statements that make the
client’s dilemmas apparent. The next step is to define both the desired change (the focal
objective) and the undesirable side effects (the ‘without’ part of the problem statements)
as objectives. Since the aim is to obtain criteria, these objectives should be defined in
such a way that they show what factors are concerned (see Section 3.2.1). Taking again the
example of the problem of the mayor who would like to see more people use the metro
(see Text box 3.2), we could decide to define only one objective: ‘many passengers’, which
would then give us a single criterion: the number of passengers, measured in number of
passengers per year. However, the problem statements we made revealed that the mayor
64

smetsyS
3 sysTems analysIs
not only wants to see many passengers on the metro but also wants to keep the operating
loss within limits and avoid the metro becoming so crowded that people get crushed dur-
ing rush hour. The objectives tree in Figure 3.5 reflects that these three objectives together
define the mayor’s main objective: good use of the metro line in her city.
good use of metro line
many low low
passengers operating loss crowding
Figure 3.5 An objectives tree with two levels
This rather simple objectives tree illustrates how the abstract qualification ‘good’ is
defined in terms of targets for concrete, measurable factors: the number of passengers
(should be high), the operating loss (i.e. the cost of operating the metro minus the rev-
enue from tickets, measured in Euro per year; this amount should be relatively small) and
the occurrence of crowding (e.g. the number of times per year that there are more than 3
people per m2 on a train; this number should be low).
If we apply the same method to the mayor’s higher level objective to reduce traffic
congestion in the city centre, we might again settle for a single objective: low traffic con-
gestion. This would produce the simplest objectives tree possible: a single rectangle.
We would then still need to operationalize the factor ‘traffic congestion’, for example,
by meas uring it as the total time (in hours per year) for all main streets that the traffic
in these streets moves at less than 15 km/h. By doing so we would have properly defined
the single criterion for measuring the extent to which the congestion problem has been
solved. But here, too, the different problem statements we made revealed several dilem-
mas, and these should be articulated in the objectives tree. The upper part of the tree in
Figure 3.6 summarizes that the mayor wants to reduce congestion, but without restricting
commercial traffic and causing nuisance in other city districts, and with low financial risk.
Note that the main objective now does not mention the factor ‘congestion’; this is because
the four second-level objectives span a much broader range of factors. As the objective
‘low nuisance for other city districts’ is still rather abstract, it has been elaborated further.
65

Systems
Policy AnAlysis of Multi-Actor systeMs
efficient accessibility
of city center
short access time short access time for low nuisance in low
for individuals commercial vehicles other city districts investment costs
low amount of high availability
traffic in districts of parking place
Figure 3.6 An objectives tree with three levels
Constructing an objectives tree is a process of ‘finding the right words’. Having expressed
the client’s dilemmas in one or more problem statements, the analyst defines an initial
level of objectives that represents what the client wants to achieve and what the client
wants to avoid. The next step is to define a more abstract objective that encompasses all
of this, and yet is as specific as possible. This then becomes the ‘root objective’ for the
objectives tree. The analyst then checks whether each objective at the lower level is opera-
tional, i.e. that the factor it entails can be measured and expressed on some unit scale.
If so, then this factor is a usable criterion, and no further elaboration of the objective is
needed. Otherwise the analyst tries to formulate two or more objectives that clarify its
meaning. If new objectives have been added in this way, the procedure is repeated.
Rules for Constructing an Objectives Tree
For objectives trees, the following rules apply:
1. Rectangles denote objectives. The text in a rectangle should be a noun phrase that
indicates a desired state (e.g. ‘high ...’ or ‘good ...’). To avoid confusion with means (i.e.
actions the client can take), verbs should not be used.
2. Connecting lines denote definition relations: lower level objectives specify the mean-
ing of the higher level objective to which they are directly connected.
3. Each objective should have either zero or more than one sub-objective. If an objective
Y can be defined in terms of a single sub-objective X, then Y should be replaced by X.
This rule forces the analyst to keep the diagram as simple as possible.
4. The lowest-level objectives should be operational: the noun phrase in these rectangles
should make clear which factor is to change (or not change) as well as the direction of
the desirable and undesirable changes, and the factor concerned should be measur-
able on some scale (preferably ISO standard units).
66

smetsyS
3 sysTems analysIs
Objectives Tree ≠ Means-Ends Diagram!
As both diagrams relate to goals, and both consist of rectangles that are arranged in levels
and linked by lines or arrows, the objectives tree is easily confused with a means-ends
diagram. However, the two serve very different purposes: a means-ends diagram is used
to decide which problem to focus on; an objectives tree is then used to define the criteria
for evaluating alternative solutions for this problem. Given these different functions, the
diagrams must be constructed and interpreted following different principles.
Because means-ends can also be seen as ways to realize some higher level means-end,
a means-ends diagram can be read in two directions. When read from top to bottom, a
means-ends diagram clarifies for each means-end how that means-end can be achieved.
Reading a means-ends diagram from bottom to top clarifies why it is desirable to realize
a means-end. The relation denoted by the arrow X→Y is a causal relation: it is a directed
relation (up!) to reflect that X leads to Y, and not the other way around.
In contrast, an objectives tree should only be read from top to bottom, and then it clari-
fies the meaning of a still abstract objective by specifying two or more concrete objectives
that can be considered as ‘component elements’. The relation denoted by the lines is a
definition relation: a cluster of lines departing from a higher level objective X to two or
more lower level objectives Y, Y, ... reflects that the extent to which objective X is realized
1 2
can be measured by measuring the extent to which Y, Y, ... are realized.
1 2
Interpreting an Objectives Tree
The main function of an objectives tree is to define the objectives of an actor (the client
or some other stakeholder in the policy problem) in such detail that the analyst can infer
the set of criteria that need to be considered when evaluating alternative solutions. In
essence, the interpretation of an objectives tree consists of compiling this set of criteria.
Assuming that the objectives tree has been properly constructed (i.e. following the rules
mentioned earlier), all of the ‘leaves’ of the tree (i.e. the objectives that are not defined
in terms of more concrete sub-objectives) each produce one criterion, while the ‘internal
nodes’ of the tree (i.e. all objectives that are not ‘leaves’) can be ignored. Interpreting an
objectives tree thus consists of listing the criteria that should be used in the problem anal-
ysis. For each criterion, a suitable unit scale should be specified. These units are usually
denoted between brackets. Text box 3.3 shows the criteria lists derived from the objectives
trees in Figures 3.5 and 3.6.
67

Systems
Policy AnAlysis of Multi-Actor systeMs
Text box 3.3 Different problem demarcation ⇒ different criteria
Criteria derived for the problem of inadequate use of the metro:
– number of metro passengers [passenger/day];
– operating loss [€/year];
– number of crowding incidents [crowding incidenta/day].
a A crowding incident is defined as a situation in which the density of passengers in a metro
train exceeds 3 persons per m2.
Criteria derived for the problem of traffic congestion in the city centre:
– access time for individuals [minuteb];
– access time for commercial vehicles [minuteb];
– number of vehicles entering/leaving a district [vehicle/day];
– availability of parking space [% vacant placesc];
– estimated investment costs [€].
b Average time needed to cover the last 2 km to destination in city centre.
c Average of vacant places/total parking places, measured at 11 a.m.
Being a factor, a criterion should be denoted by a noun phrase that refers to a specific
system property. For typical objectives like ‘low nitrate emissions to groundwater’, ‘high
crop yield’ and ‘high profit’, the criteria are easily obtained by omitting the words like ‘low’
or ‘high’. For objectives such as ‘many passengers’ and ‘few drop-outs’, the factors are
tallies (i.e. they count discrete entities), in which case the word ‘many’ or ‘few’ should be
replaced by ‘number of’ to obtain a well-defined criterion. An objective that needs a little
more translation effort is ‘few power failures’. The criterion would then be ‘frequency of
power failures’ (measured in failures per year), but one could also opt for ‘mean time
between power failures’ (measured in days). Note that for the first criterion, low values
are better than high values, whereas for the second criterion, high values are better than
low values. The commonly made mistake of operationalizing ‘traffic safety’ by measuring
it in terms of casualties per year highlights that the analyst should take care in choosing
an appropriate unit of measurement for a criterion.
While interpreting the objectives tree, the analyst should also pay specific attention to
the independence of the criteria. When criteria are not independent of each other (e.g.
‘NO emission’ and ‘NO concentration in the air’, or ‘average duration of traffic jams’ and
x x
‘length of traffic jams’), or when a criterion is included in another, broader criterion (e.g.
‘concentration of aerosols’ and ‘concentration of small particulate matter’), this system
characteristic will ‘count double’ when alternative solutions are evaluated using the list
of criteria. In that case, a choice will have to be made between accepting the aggregated
criterion ‘quality of air’, or elaborating the quality of air into a number of suitable parallel
criteria. Such problems of overlapping criteria, or criteria that are causally related, are less
likely to occur when the objectives tree has been properly constructed.
Using Proxies as Criteria
Some criteria are intrinsically difficult to measure. In such cases, it can be useful or even
necessary to work with proxies. A proxy is a measurable factor that is believed to give a
good indication of the realization of the actual objective.
68

smetsyS
3 sysTems analysIs
Text box 3.4 Using proxies as criteria
The use of fertilizers in agriculture constitutes a problem for the environment because the
residues of fertilizers seep into surface waters, degrading the environment. In this case, one
might suggest as a criterion the quantity of fertilizer that seeps into the surface water yearly.
However, this factor will be hard to measure or observe directly, as this would require the
installation of monitoring equipment next to every agricultural plot. Alternatively, the quantity
of fertilizer that is introduced onto the land could be used. This would be justified under the
assumption that the quantity that seeps into the system is proportional to the amount of
fertilizer applied.
A similar choice for a proxy as criterion can be made when analysing the problem of
environmental damage as a consequence of freight transport by road. In principle, indicators
for the eventual environmental consequences of freight transport – for example, respiratory
problems for humans – should be used as criteria. Knowing that respiratory problems correlate
with the concentration of certain substances in the air (aerosols, nitrogen oxides), the yearly
emission of these substances may be chosen as a proxy for environmental damage.
The examples in Text box 3.4 clarify that the use of a proxy as a criterion leads to a nar-
rower demarcation of the system that needs to be analysed, and therefore to a less com-
plicated analysis: the mechanisms in the natural environment do not have to be taken into
account. The danger of using proxies is that they may not be representative of the degree
to which the objectives are actually achieved. For example, death rate could well serve
as a proxy for the status of public health. The death rate gives a fair indication, but there
are many more factors at stake in public health. When the death rate is taken as proxy for
public health, the analysis will overlook increases in health risks that are not immediately
fatal (e.g. obesity). A similar problem occurs when the chosen proxy reflects the degree
to which certain means have been put to use, rather than the degree of achievement of
the objective. Consider, for example, using the number of doctors or hospitals per 1,000
persons as an indicator for public health. These kinds of faulty substitutions produce mis-
leading results and occur more often than you would think!
The Multi-Actor Situation
We often find ourselves in the situation where we have to take into account several actors
who may have different interests, and possibly conflicting objectives. This multi-actor
aspect is addressed in detail in the next chapter, but we should mention here that its
importance has also been recognized by systems analysts. For instance, Ralph Keeney
indicates in his book ‘Value-Focused Thinking’ (1992), which is almost entirely devoted to
the analysis of objectives and means, how a so-called ‘overall objectives hierarchy’ can be
deduced by combining and structuring the criteria from the objectives trees of different
actors in a problem context. This kind of joint hierarchy of objectives allows the analyst to
evaluate alternatives while considering the objectives of all stakeholders involved.
The following small example illustrates this approach. Three actors are stakeholders in
the issue of further developing a local airport A near city C. The management of airport A
wants to construct a second runway in order to improve its turnover and its competitive
position. The city council of C wants high employment, but also a good living environment
for its inhabitants, more specifically, low noise nuisance and good air quality. The envi-
69

Systems
Policy AnAlysis of Multi-Actor systeMs
ronmental organization E wants to protect the bird species that breed in the area, and
therefore wants low noise nuisance and low air pollution. An operationalization of these
objectives could result in the following list of criteria:
– turnover of airport A [€/year];
– number of new jobs near C [job];
– number of houses exposed to more than 70 dB(A) [house];
– emissions of small particulate matter [kg/year].
The environmental organization is hardly interested in the effects on the first two criteria.
As a firm, the airport is interested in the last two criteria only because neglecting these
aspects is bound to lead to lengthy legal procedures that would cause delays. The munici-
pality will be interested in the last three criteria. By working with the whole set of criteria,
the analyst can perform research and prepare evaluations that are interesting and accept-
able to all three actors.
3.4 Mapping Causal Relations
Now that it is clear what we want to achieve, through the identification of objectives and
the specification of associated criteria, we should investigate the elements that influence
the realization of these objectives. The means-ends diagram constructed at the beginning
to support the initial problem demarcation and identify an appropriate level of analysis
provides a starting point. However, in almost all cases, it is sensible to develop a ‘map’ of
the causal chains in the system that link means to criteria.
A causal map depicts the causal relations between the factors that are relevant to the
problem. It represents the internal structure of the problem, supporting a qualitative form
of ‘what if?’ analysis that helps in understanding the effects of means and/or external
factors on other factors, notably the criteria (Montibeller & Belton, 2006). Furthermore,
a causal map can provide a good starting point for quantitative models that might be
developed later in the process of policy analysis. Another term for a causal map is a causal
(relation) diagram. A reason for using the general term ‘map’ here is to distinguish it from
a system diagram, which will be discussed in the next section.
The basis for a causal map is a ‘theory’ about how a system works. Usually, this theory
is a mental model produced by the researcher/analyst, complemented with knowledge
from literature research, interviews and experts about the essential causal mechanisms
of the system that are relevant to the problem. The criteria resulting from the objectives
tree offer a good starting point for the construction of the causal map. Potential solutions
are aimed at changing the criteria in the desired direction, and by doing so closing the
gap that is at the heart of the problem. Reasoning backwards from the list of criteria is
therefore a sensible approach when elaborating a causal map. Next we reason backwards
from the criteria, asking the same question over and over again: which factors influence X?
During the problem structuring, a causal map should remain limited to those factors
that are most relevant to the problem and its solution. It is easy to get carried away while
drafting a causal map, trying to represent all aspects of the problem in detail. However,
excessive detail renders the map ineffective as a tool for clarification and communica-
tion. It is therefore advisable to choose a rather high level of aggregation. A general rule
of thumb is that a causal map becomes difficult to interpret when it contains more than
twenty elements. If the system is so complex that more factors are really needed to cap-
70

smetsyS
3 sysTems analysIs
ture its main elements and structure, it is advisable to develop different causal maps for
different ‘subsystems’ and for different levels of aggregation.
When thinking about which factors to include in a causal map, keep in mind that causal
analysis is about understanding how changes in one factor result in changes in other
factors. This implies that you should focus on factors that can change; constants can be
ignored. A second consideration is that only those factors that have a significant influence
on one or more criteria need to be included.
The causal map in Figure 3.7 shows the intermediate result of starting a causal map
from the criteria derived from the objectives tree in Figure 3.5, and then for each of these
factors X repeatedly asking the question ‘what factors can cause X to change?’ Each newly
identified factor Y is then added to the map, and the causal relation Y→X is depicted by an
arrow. This arrow is then labelled with a sign: a ‘+’ to denote that if the value of Y increases,
the value of X will also increase (positive relation), or a ‘–’ to denote that if the value of Y
increases, the value of X will decrease (negative relation). This process is repeated for all
factors that are not directly influenced by some means of the client.
+
electricity price
opera�ng cost
+
opera�ng loss
+ -
turnover
�cket price
-
number of number of
tourists + passengers
+
-
cost of driving a
car
number of stops +
+
trip �me
-
speed -
crowding
train capacity
-
train frequency
Figure 3.7 Intermediate result of causal mapping
71

Systems
Policy AnAlysis of Multi-Actor systeMs
The process of ‘backward reasoning’ is then followed by a process of ‘forward reasoning’
by asking for every factor X ‘what other factors change when X changes?’ As can be seen in
Figure 3.8, this leads to adding new causal relations. Thinking in this way may also reveal
additional side effects (new factors), and if these turn out to be of interest to the client,
they should be added to the list of criteria. When constructing a causal map, it is advisable
to document the underlying assumptions, because causal assumptions that may seem
self-evident to the analyst may not be obvious to others.
turnover +
road tax
oil price + - opera�ng loss
+
+ +
+
�cket price
+ electricity price
opera�ng cost cost of driving a
+ car -
+ speed + number of
passengers
+ trip �me
- -
- + + +
train frequency number of stops number of +
tourists
crowding
train capacity -
-
Figure 3.8 A completed causal map
Rules for Constructing a Causal Map
For a causal map, the following rules apply:
1. Each of the factors should be a noun phrase that denotes some variable system prop-
erty. Each noun phrase F should be such that the sentence ‘F increases’ is grammati-
cally correct and meaningful.
2. Arrows denote first-order causal relations. Each arrow X→Y should signify that a
change in X will result in a change in Y.
3. Each arrow X→Y should be labelled with either a plus (to denote that the values of X
and Y are positively related) or a minus (to denote a negative relation).
4. Each factor should be connected to at least one other factor.
5. To enhance legibility of the diagram, crossing arrows should be avoided as much as
possible.
6. If the diagram contains an arrow X→Z and also some indirect path X→Y→ ... →Z,
then the analyst should justify this multiple causality by explaining that the two paths
have different underlying causal mechanisms. This rule forces the analyst to keep the
diagram as simple as possible.
Interpreting a Causal Map
The main function of a causal map is to provide an overview of the factors and causal rela-
tions that are relevant to the client’s problem and therefore need to be considered in the
72

smetsyS
3 sysTems analysIs
problem analysis. The analyst uses the diagram first to find out to what extent the client
distinguishes the same factors and interrelationships, if not, what the differences are and
whether this has implications for the problem formulation and associated initial system
demarcation.
Having established that all elements of the causal map (factors and relations) make
sense, the analyst should verify whether the causal relations denoted by the arrows occur
within the time frame set by the problem demarcation. If an effect is expected to occur so
slowly that it is not significant on the time scale selected for the analysis, it is advisable to
remove the arrow involved.
The next step is to scan for loops: causal paths that start from some factor X and even-
tually join this same factor X again. Figure 3.8 contains one such loop, involving only
two factors: ‘number of passengers’ and ‘crowding’. Such loops denote a dynamic feed-
back mechanism. The type of feedback can be determined by multiplying the signs along
the cyclic path to determine the net effect. An even number of minuses (this includes 0
minuses) indicates positive feedback, and an odd number indicates negative feedback.
Positive feedback means that over time the effects of changes that affect any of the factors
involved in the loop may be amplified; negative feedback means that these effects may
be reduced. The loop in Figure 3.8 suggests the latter: when more people start using the
metro, this increases crowding, and this is expected to deter people from using the metro,
which in turn reduces crowding.
Having checked for loops, the analyst should also check whether the causal map con-
tains factors X and Y linked by more than one causal path X→ ... →Y. If these paths have
opposite signs (as is the case for the two paths between ‘number of stops’ and ‘number of
passengers’ in Figure 3.8), this raises the question of which influence is stronger.
Besides providing an overview of factors and relations, a causal map facilitates the
search for means to attain objectives. The set of means identified while constructing the
means-ends diagram is usually incomplete. The causal map permits a more systematic
search: for each factor X, the analyst poses the question ‘How can the client change X?’
For some factors, this may reveal several means, for others none. Some factors may be
affected by the same means. The resulting list of means needs to be integrated consist-
ently and iteratively with the results of the other analyses (criteria, causal map) in the
system diagram.
3.5 Overview of the System and Its Boundaries: The System Diagram
The primary function of a system diagram is to summarize the systems analysis by show-
ing the boundary and the elements relevant to the problem analysis. The boundary rep-
resents the system demarcation (the level and spatial and temporal scales of analysis).
The elements come in four categories: criteria (the factors whose values indicate to what
extent the problem has been solved), external factors (factors that cannot be influenced
by the client, but do affect one or more criteria), means (actions of the client that affect
one or more criteria) and internal factors (all other factors within the boundary that play a
role in the causal chains that affect the criteria). The first three categories (criteria, exter-
nal factors and means) are often said to be on the system boundary, as they are depicted
as such in the system diagram. As mentioned at the start of this chapter, the means are
placed on the left-hand side of the diagram, external factors at the top and criteria on the
right-hand side of the diagram. Whereas means and external factors cannot be influenced
73

Policy AnAlysis of Multi-Actor systeMs
by internal factors, the criteria are influenced by internal factors and can themselves also
influence internal factors. So although the criteria are located on the right system bound-
ary they may be connected to internal system factors.
As it synthesizes the results of the exploratory systems analysis, the system diagram is
a conceptual model of the system. It constitutes the basis for further analysis, but also
forms a useful tool for communicating about the system demarcation and the structure
of the problem with the client, fellow analysts or other actors.
external factors
number of
|     | oil price  road tax  |     |     |
| --- | -------------------- | --- | --- |
Systems tourists
+
+
electricity price turnover
opera�ng loss
|     |     | - + | -   |
| --- | --- | --- | --- |
+
| reducefares | +   | + �cket price+ |     |
| ----------- | --- | -------------- | --- |
cost of driving a
| means             | opera�ng cost | car      |                    |
| ----------------- | ------------- | -------- | ------------------ |
|                   | + + speed     |          | - criteria         |
| intensifyschedule |               | + +      |                    |
|                   | +             | trip �me | n u m b e r  o f   |
|                   | +             | -        | p a s se n g e r s |
-
+
| use new trains |                 | +               | -   |
| -------------- | --------------- | --------------- | --- |
|                | +               | +               |     |
|                | train frequency | number of stops |     |
+
+
|     | train capacity | -   | crowding |
| --- | -------------- | --- | -------- |
-
| Figure 3.9  | A system diagram |     |     |
| ----------- | ---------------- | --- | --- |
Figure 3.9 depicts a system diagram that summarizes the results of the city metro exam-
ple. It shows that three means have been identified, and that these allow the client to
directly affect the factors ‘ticket price’, ‘number of stops’, ‘train frequency’, ‘speed’ and
‘train capacity’, and so indirectly influence the criteria.
Rules for Constructing a System Diagram
For a system diagram, the following rules apply:
1.  The means are located at the left boundary. To be relevant to the problem, there must
be a causal route from a means through the internal factors to at least one criterion.
Means seldom connect directly to a criterion. If the system diagram has such direct
connections, check your logic carefully.
2.  Criteria, located at the right-hand boundary, must have incoming arrows, and can have
outgoing arrows (if they connect back to an internal factor).
3.  Every internal factor must have an incoming arrow. Every internal factor must have an
outgoing arrow, except if it forms a criterion.
4.  Means and external factors do not have incoming arrows.
5.  External factors are located at the upper boundary. For an external factor to be relevant
there must be a route through the internal factors to at least one criterion.
6.  Arrows must be accompanied by a ‘+’ or ‘−’ sign.
7.  Means are formulated as verb phrases.
74

smetsyS
3 sysTems analysIs
8. All factors are formulated as noun phrases and can be measured and expressed on
some unit scale.
9. The outer dashed boundary depicts the system demarcation, representing the spatial
and temporal scales chosen for the systems analysis and the level of aggregation.
Which factors are internal or external to the system needs to be consistent with the
choice of system boundary.
Because the system diagram also represents means, and because the placing of factors is
more constrained than for a causal map (means on the left, criteria on the right, external
factors at the top), it can become unclear due to crossing lines. For complex problems,
with many internal factors, it is advisable to hide clusters of internal factors by depicting
them as ‘subsystems’ as shown in Figure 3.10. With unsigned arrows, as the ‘+’ and ‘–’
only make sense between two factors. The factors and relations that remain hidden in this
‘upper level’ system diagram should be shown in separate diagrams, one for each of the
subsystems.
external factors
S S
1 2
means
criteria
S
3
Figure 3.10 A system diagram with subsystems
Interpretation of a System Diagram
A system diagram is used in the first place to summarize the findings from the means-
ends analysis, the client’s objectives tree and the causal analysis. It can also be used for
qualitative analysis of the effect of using particular means, or of changes in external fac-
tors, on the criteria. To do this, the analyst selects a means or external factor X, and inves-
tigates, by following the causal path(s) from X, which criteria are eventually affected, and
in what way. For each affected criterion Z, the effect (an increase or decrease of the value
of Z) is assessed by taking into account the multiplication of the signs along the arrows as
discussed in the previous section. Doing this allows for the identification of the desirable
effects as well as the undesirable side effects of the means employed. It facilitates identify-
ing intrinsic dilemmas, means that are good for some objectives but not for others, and
whether the problem owner can potentially attain all the objectives.
Alternatively, the question ‘how can we increase criterion Z?’ can be answered by fol-
lowing the causal chains back to specific means and/or external factors. This can indicate
75

Policy AnAlysis of Multi-Actor systeMs
whether criteria are sensitive to external influences, giving insight into how much control
the problem owner has over the criteria and whether the objectives might be attained
without action having to be taken.
In tracing causal pathways from the means and/or external factors through the internal
factors to the criteria, key internal factors can be identified. This may lead to a search for
(additional) means to influence the key factors, and even the identification of actors who
may be able to help in influencing these key factors and attaining the problem owner’s
objectives, or who share similar objectives.
For a particular problem situation, it can be useful to tabulate the findings in a conse-
quences table like the one in Table 3.1, to get an impression of which means affect which
criteria in which ways.
Systems
Table 3.1  Qualitative consequences table indicating the effects of different means on
criteria
Criteria
|       |     | C1  | C2  | C3  | C4  |
| ----- | --- | --- | --- | --- | --- |
|       | M1  | +   |     | –   |     |
|       | M2  | +   | +   |     |     |
|       | M3  | –   |     |     | +   |
| Means | M4  |     | +   | +   |     |
|       | M5  |     | +/– | –   |     |
|       | M6  |     |     | +   | +   |
|       | M7  |     |     |     | –   |
In a similar fashion, the effects of changes in the external factors on the criteria can be
explored (Table 3.2). The effects of combinations of changes in external factors and means
can also be analysed, as discussed further in Chapter 5.
Table 3.2  Qualitative consequences table indicating the effects of changes in external
factors on criteria
Criteria
|          |     | C1  | C2  | C3  | C4  |
| -------- | --- | --- | --- | --- | --- |
|          | E1  |     | +   |     |     |
| External | E2  | +   |     | –   |     |
|          | E3  | –   |     |     | +   |
3.5.3  The Multi-Actor Situation
In Section 3.3.2, we showed how a broader set of criteria can be defined by taking into
account the problem perceptions of several actors, typically the client and a selection of
stakeholders. This broader set may of course also be used as the starting point for making
a causal map, and eventually result in a system diagram that comprises the means and
criteria of all of these actors. This multi-actor system diagram can be constructed and
interpreted using the same principles. However, the following points are worth noting.
When a system is viewed from a single actor’s perspective, all actions of all other actors
are represented using factors and causal relations. For example, when the client is a local
water authority that considers enforcing anti-pollution laws more strictly, other actors,
76

smetsyS
3 sysTems analysIs
such as the industry that discharges its wastewater into the river, are assumed to comply,
for example, by installing filters. In a causal map, this would typically be represented as
a minus-labelled causal link ‘enforce more strictly’ → ’emissions’. When the analyst also
wants to include the perspective of the industry in the system diagram, the criteria and
possible actions of this new actor (e.g. installing filters) should be added. To properly
represent the interplay between the local water authority and the industry, the rational-
ity of the industry should be made explicit. The extended diagram should reflect that
installing filters costs money and hence negatively affects the industry’s main criterion:
profit. There is a direct negative causal link from ‘install filters’ → ‘profit’. So why would
the industry install filters? The answer could be that the local water authority can fine the
industry if it does not comply with the anti-pollution act. To articulate that the industry
is sensitive to this financial incentive, the diagram could be extended further by adding
the factor ‘compliance with norms’ and a positive-labelled causal link from the indus-
try’s means ‘install filters’ → ’compliance with norms’, followed by a positive-labelled
link from this factor to the industry’s profit criterion to reflect that compliance will avoid
fines. Phrased differently, non-compliance will cost money. Adding a link from the means
‘enforce more strictly’ → ‘compliance with norms’ then reflects that when the local water
authority uses this means, the industry’s profit will be affected indirectly and will only
increase if the industry installs filters.
In a single-actor system diagram, actions of other actors (or rather, the immediate
effects of these actions) will typically be represented as external factors if the client has no
means to control these other actors. When the system diagram is extended to include the
perception of such an actor, the actions of this actor become means (and hence should be
represented at the left side of the diagram), while the factors that represent the effects of
the actions move ‘inside’ the system: they change from external factors to internal factors.
Clearly, shifting from a single-actor system diagram to a multi-actor system diagram will
change the system demarcation – the system boundary – with the means of other actors
now being included as means, or factors that were considered external potentially becom-
ing internal factors, or the causal map becoming more complex, or the criteria becom-
ing more numerous. When interpreting a multi-actor system diagram, it is important to
keep track of which actor takes an interest in which criterion, as different combinations
of means may distribute the costs and benefits differently across actors. The methods for
identifying and dealing with this multi-actor aspect will be discussed in detail in the fol-
lowing chapter.
3.6 Takeaways
– Systems analysis is used to arrive at a conceptual model of the problem situation,
depicted in a system diagram.
– The system diagram provides a structured overview of the problem situation, from
the perspective of the problem owner, and can be extended into a multi-actor system
diagram.
– A system diagram is based on a causal map of the problem situation.
– A system diagram consists of a boundary, with three groups of factors at the boundary:
means, external factors and criteria.
– Means-ends analysis is a tool that can be used to support system demarcation.
77

Systems
Policy AnAlysis of Multi-Actor systeMs
– An objectives tree is a tool to support the identification of outcomes of interest for the
problem situation which are formulated in the form of measurable criteria.
– The means and the external factors influence the system, and these influences propa-
gate through the internal factors, eventually influencing the criteria.
References
Checkland, P. (1985). A Development of Systems Thinking for the 1990s. Journal of the
Operational Research Society, 36(9), 757-767. https://doi.org/10.2307/2582164.
Daalen, C.E. van & Bots, P.W.G. (2010). Using a Systems Perspective to Design
a Problem Solving Process. Journal of Design Research, 8, 301-316. https://doi.
org/10.1504/JDR.2010.035674.
Findeisen, W. & Quade, E. S. (1985). The Methodology of System Analysis: An
Introduction and Overview. In H. J. E. Miser & E. S. Quade (Eds.), Handbook of
Systems Analysis, part I. Overview of Uses, Procedures, Applications, and Practice
(pp. 117-150). Amsterdam: Elsevier Science Publishing.
Gregory, R. & Keeney, R. L. (1994). Creating Policy Alternatives using Stakeholder Values.
Management Science, 40(8), 1035-1048. https://doi.org/10.1287/mnsc.40.8.1035.
Jackson, M. C. (1992). Systems Methodology for the Management Sciences. Boston:
Kluwer Academic Publishers.
Keeney, R. (1992). Value-focused Thinking. A Path to Creative Decision Making. Cambridge,
MA: Harvard University Press.
Miser, H. J. & Quade, E. S. (Eds.) (1985). Handbook of Systems Analysis, Part I. Overview
of Uses, Procedures, Applications, and Practice. Amsterdam: Elsevier Science Publishing.
Montibeller, G. & Belton, V. (2006). Causal Maps and the Evaluation of Decision
Options – A Review. Journal of the Operational Research Society, 57(7), 779-791.
https://doi.org/10.1057/palgrave.jors.2602214.
Slinger, J. H., Taljaard, S. & d’Hont, F. (2020). Complex Coastal Systems. Transdisciplinary
Learning on International Case Studies. Delft: Delft Academic Publishers.
Walker, W. E. (2000). Policy Analysis: A Systematic Approach to Supporting
Policymaking in the Public Sector. Journal of Multi-Criteria Decision Analysis, 9, 11-27.
https://doi.org/10.1002/1099-1360(200001/05)9:1/3<11::AID-MCDA264>3.0.CO;2-3.
78

srotcA
4 Actor Analysis
An actor is a social entity, a person or an organization, able to act on or exert influence on
a decision. This book places policy analysis in a multi-actor environment. From this per-
spective policy problems and policy processes involve multiple actors (‘parties’) because
we presume that no single actor will be able to unilaterally impose its desired solution
onto the others. Some form of cooperation, coordination or congruence between actors
is required; the actors are interdependent. In such circumstances knowing who are the
‘others’ and understanding their objectives and motivation for participating is a crucial
part of problem structuring. This chapter presents a method for analysing actors to help
structure a complex policy issue.
4.1 Introduction: Why Actor Analysis?
The system diagram presented in Chapter 3 presumes that policy analysis revolves around
the perspective, interests and the policy instruments or means of one problem owner.
This approach suffices when the problem owner himself has sufficient means to solve
a policy problem. In practice, however, such situations are rare. Therefore, the problem
owner has to be aware of the interests and objectives of the other actors who are in some
way involved with the policy problem, will be affected by the solutions or have means that
are essential for solving the problem.
Sometimes these interests and/or the others’ objectives may be aligned with those of
the problem owner, but very often they are not fully aligned or even conflicting; knowing
friends and foes; anticipating their concerns and issues; maybe engaging them in prob-
lem analysis and problem-solving activities might enrich the process and lead to better
solutions, legitimate decisions and reduce resistance. Thus it is of great importance that
a problem analysis provides insight into the range of actors involved as well as their net-
works.
As indicated this insight can support policy analysis in various ways. Presupposing that
we are dealing with untamed or ill- or unstructured problems as discussed in Chapter 2
actor and network analysis will help to choose the fitting style of policy analysis for the
current problem (see Figure 2.1). Mayer et al. (2004) describe six so-called ‘styles of policy
analysis’ that describe a specific way of dealing with problems adapted to the character of
the problem. According to Mayer et al. (2004), whose work will be discussed extensively in
Chapter 6, actor analysis can help to support various policy analysis activities; it can mobi-
lize knowledge, clarify values, help generate new ideas, map areas of potential conflict or
mobilize support (see Table 4.1).
79

Actors
Policy AnAlysis of Multi-Actor systeMs
Table 4.1 Possible contributions of actor analysis to policy analysis activities
Policy Analysis Activity Actor Analysis Can Help to …
Research and analyse Mobilize (scientific) knowledge and information from a broad actor base, which is
likely to improve the quality of the problem analysis.
Design and Create ideas for alternative strategies and tactics by mapping options and interests
recommend of different actors. This helps to identify common ground and shared fundamental
values, to identify ways in which different actors can contribute to these shared values
and to identify needs and possibilities for compensation or mitigating measures to
satisfy particular actors.
Advise strategically Assess the feasibility and potential to implement policy options, by mapping the
positions, interests, resources and relations of actors, providing insight into the
opportunities and threats that actors pose for problem-solving.
Mediate Map conflicts, identify potential coalitions of actors and propose a road map for a
negotiation process, including agenda items and participants in various stages of
discussion.
Democratize Ensure that all the important actors are included in the policy process, and/or that
their views and concerns are incorporated in the problem analysis. From a normative
point of view, this supports a more legitimate and inclusive problem analysis.
Clarify values and Include the full range of values and arguments in a problem analysis, which aids
arguments a problem analysis that is recognized and accepted by different parties, offering a
better basis for agreement and cooperation concerning policy options.
4.2 Conceptual Framework for Actor Analysis
Before sketching the main steps involved in actor analysis, it is useful to reflect on the object
of analysis: what is an actor and what are the main concepts that are needed to describe
actor interactions in policy processes? This helps to identify the main concepts and dimen-
sions that one should cover in a first scan of the multi-actor context of a policy problem.
In this chapter, we define an actor as “individuals, organizations, or groups capable
of autonomous and intentional actions that have an impact on a problem or system of
interest” (Hermans & Cunningham, 2018: 13-14). Actors are those parties that have a cer-
tain interest in the system and/or that have some ability to influence that system, either
directly or indirectly. Note that we use the term ‘actor’, and not ‘stakeholder’. In practice,
the terms are often interchanged. However, sometimes the term ‘stakeholder’ is used to
refer to those groups that are mostly involved because they have an interest, or stake, in
decision-making processes, while the term ‘actor’ is used to refer to those with the capac-
ity to influence the decision-making or to act on decisions and their outcomes.
Beyond a direct description of the term ‘actor’, further insight into what an actor is can
be gained by discussing the key attributes of actors in relation to policy-making and policy
analysis. What characterizes an actor? For this, we turn to theories of the policy process,
many of which have been presented in Chapter 2.
Public policies are generated within decision arenas: “a dedicated social space for stra-
tegic decision-making” (Hermans & Cunningham, 2018: 14). These arenas may have clear
formal boundaries or they may be more virtual spaces in which actors interact (Ostrom,
2005). These arenas set the stage for actor interactions, whereby the network rela-
tions and the institutions provide key conditions for actor’s behaviour (see Hermans &
Cunningham, 2018: 19). Looking only at the networks and institutions, however, has a lim-
ited potential to explain policy changes if it is not complemented by an analysis at a lower
80

srotcA
4 aCTor analysIs
level in terms of actor properties (Rhodes & Marsh, 1992: 196). At this actor level, most
theories converge around three basic dimensions that help explain actor behaviour: per-
ceptions, values and resources (Jobert, 1989; Mitroff, 1983; Sabatier, 1988; Scharpf, 1997).
If one takes the arena level and the actor level into account, the behaviour of actors in
policy processes can be described using the following conceptual dimensions (Hermans,
2005):
Arena level:
1 Networks: ‘More or less stable patterns of social relations between interdependent
actors, which take shape around policy problems and/or policy programmes’ (Klijn,
1997: 30). Policy networks may coincide with arenas, or they may offer the larger social
context for a decision arena.
2 Institutions: In networks, the institutions provide an important influence for the rela-
tions in the network and for the behaviour of actors. Institutions are defined here as
the ‘rules of the game’ (North, 1994). These include formal and informal rules, explicit
and implicit (Ostrom, 2005).
Actor level:
3 Perceptions: The image that actors have of the world around them, both of the other
actors and networks, and of the substantive characteristics of a policy problem (Bots
et al., 2000; Scharpf, 1997). Perceptions may also be labelled causal beliefs, cognitions
or frames of reference. Perceptions here refer only to ‘neutral’ theories of how the
world operates, and not to normative beliefs about what is good and desirable. The
latter are discussed under the dimension of ‘values’.
4 Values: These provide the directions in which actors would like to move; they describe
the internal motivations of actors. Related concepts such as ‘norms’, ‘interests’ and
‘purposes’ function on a more abstract level, whereas ‘objectives’, ‘goals’ and ‘targets’
express values in more specific terms. ‘Preferences’ and ‘positions’ translate values
into a preference ordering over specific solutions or policy outcomes. Variables on this
dimension are closely linked to actors’ perceptions (see also Sabatier, 1988: 131-133).
5 Resources: The practical means that actors have to realize their objectives. Resources
are the ‘things over which they have control and in which they have some interest’
(Coleman, 1990: 28). Resources enable actors to influence the world around them,
including other actors, relations and rules in a network. As such, resources are closely
related to power and influence.
4.3 Methods for Actor Analysis
There are several methods available to support actor analysis. In practice, most use is made
of approaches for stakeholder analysis, which are rooted in strategic management literature
(see, e.g. Bryson, 2004; MacArthur, 1997; Freeman, 1984; Grimble & Chan, 1995; Mitroff,
1983). The popularity of stakeholder analysis methods is explained by the fact that they are
relatively easy to use and can be applied in a wide range of situations. Furthermore, these
methods are flexible enough to cover a wide range of conceptual dimensions. These quali-
ties also make stakeholder analysis methods very useful for an initial problem exploration.
Hence, they provide the basis for the actor analysis approach described in this chapter.
However, it should be kept in mind that in many cases it may be worthwhile to carry out
an actor analysis that goes beyond an initial scan or exploration. In such cases, a more
81

Policy AnAlysis of Multi-Actor systeMs
focused and detailed actor analysis method is required. In these cases, several meth-
ods are available depending on the concepts that are of most interest. These include for
instance methods that focus specifically on the structure of social networks (Scott, 1991),
methods that map actor perceptions (Bots et al., 2000) and methods that analyse con-
flicts between actors (Hipel et al., 2008). An overview of different actor analysis methods
for policy analysts is provided in Table 4.2. More background information on the methods
in this overview and their use can be found in Hermans and Thissen (2009) and in Her-
mans and Cunningham (2018).
Table 4.2  Overview of methods for actor analysis
| Method           | Focus    | References |
| ---------------- | -------- | ---------- |
| Network Analysis | Networks |            |
Social network analysis Structural characteristics of actor networks Kenis and Schneider
(1991); Scott (1991)
| Stakeholder Analysis | Resources and Interdependencies |     |
| -------------------- | ------------------------------- | --- |
Stakeholder analysis Stakeholder environment to maximize cooperative  Freeman (1984);
|     | potential and minimize threat of obstruction | Bryson (2004) |
| --- | -------------------------------------------- | ------------- |
Motivation and ability analysis Stakeholder setting and influence of (policy) triggers  Phi et al. (2015);
Actors
|     | to motivate or enable actors to support action | Nguyen et al. (2019);  |
| --- | ---------------------------------------------- | ---------------------- |
Korbee et al. (2019)
| Game Theory Models | Resources and Interdependencies |     |
| ------------------ | ------------------------------- | --- |
Metagame analysis Structure of policy ‘game’ to help identify stable  Howard (1971, 1989);
|     | outcomes and advise on strategies for negotiation  | Fraser and Hipel  |
| --- | -------------------------------------------------- | ----------------- |
|     | and coalition building                             | (1984)            |
Hypergame analysis Structure of policy ‘game’ and role of   Bennet et al. (1989)
(mis)information and strategic surprise
| Transactional Analysis | Resources and Interdependencies |     |
| ---------------------- | ------------------------------- | --- |
Transactional process models Potential for exchange of control between different  Coleman (1990); Tim-
|     | actors, to facilitate policy process | mermans (2004) |
| --- | ------------------------------------ | -------------- |
Vote-exchange models Predicted shifts in actors’ positions and outcomes  Stokman (1994);
|                    | of collective decision-making   | Thomson et al. (2003) |
| ------------------ | ------------------------------- | --------------------- |
| Discourse Analysis | Perceptions of Groups of Actors |                       |
Argumentative analysis Different chains of reasoning used in policy debate  Toulmin (1958);
|     | and underlying values and assumptions | Mitroff (1983) |
| --- | ------------------------------------- | -------------- |
Narrative policy analysis Opposing views of controversial problems and  Roe (1994); van Eeten
|     | possible meta-narratives to reformulate those  | (2006) |
| --- | ---------------------------------------------- | ------ |
problems
Q-methodology Groups of actors with shared perspectives and their  McKeown and
|     | underlying basis |  Thomas (1988) |
| --- | ---------------- | -------------- |
Cognitive Mapping Perceptions of Individual Actors Axelrod (1976)
Self-Q interviews Possibilities to address policy problems through  Bougon et al. (1990)
actors’ rationale
Dynamic actor network  Perceptions of actors to enable comparative analysis  Bots et al. (2000)
| analysis (DANA) | of agreement, conflict etc. |     |
| --------------- | --------------------------- | --- |
82

srotcA
4 aCTor analysIs
Preference Elicitation Values of Actors
Value-focused thinking, Structure and hierarchy in various attributes and Keeney (1992); Saaty
analytic hierarchy process alternatives (1990); McDaniels
(AHP), multi-attribute and Thomas (1999)
assessment etc.
Source: Hermans and Cunningham (2018); Hermans and Thissen (2009)
4.4 Steps in Actor Analyses
The following sections of this chapter discuss and clarify the steps that need to be fol-
lowed in general actor analyses. The core of the method described here is in line with
the guidelines for stakeholder analysis that are available in various documents. However,
whereas stakeholder analysis methods typically focus on the dimensions of power and
interests of actors, our initial scan of the actor network will also cover the network struc-
ture and perceptions of actors. This results in a basic procedure for actor analysis that
covers six steps:
1 Formulation of a problem and associated decision arena as a point of departure.
2 Identification of the actors involved.
3 Mapping the formal institutional playing field: Chart the formal institutions and rela-
tions of actors.
4 Identifying actor characteristics: Determining the interests, objectives, perceptions
and resources of actors.
5 Summarizing the interdependencies between actors using overview tables or dia-
grams.
6 Determining the consequences of these findings with regard to the problem formula-
tion.
These steps are further explained in the following sections. These explanations are sup-
ported by a case example of New York City drinking water supply, introduced in Text
box 4.1.
4.4.1 Step 1: Use Problem Formulation and Associated Decision Arena as Point of
Departure
There needs to be an initial problem formulation which can serve as a point of departure
for the actor analysis. There are two possible alternatives:
1 The problem formulation as viewed by the problem owner, which is mapped out by the
analyst as a first research activity.
2 The problem formulation as formulated by the analyst, based on a first substantial
problem exploration.
A good problem formulation includes a clear description of the gap and the dilemma of
the main problem owner. What is the gap between the desired situation and the current/
expected situation? And what is the action dilemma for the main actors involved when it
comes to closing this gap?
For further requirements and examples of good problem formulations, refer to Chapter
2. However, for an actor analysis, this problem formulation needs to be linked to a decision
arena. There might be multiple arenas you can consider, and it is important to be explicit
83

Actors
Policy AnAlysis of Multi-Actor systeMs
about those. Where are actors deciding about this problem? These decision-making pro-
cesses might be formal or informal and they might be simultaneous and coordinated, or
asynchronous and piecemeal. Bringing into vision the decision arenas is necessary for the
next steps in the actor analysis, but might also cause you to modify your initial problem
formulation. It is the expectation that an actor analysis yields new insights that help the
analyst to further complement or sharpen the initial problem formulation, and that might
already start with this very first step in an actor analysis.
Text box 4.1 Problem formulation for the case of New York City drinking water supply
Throughout this chapter, we will use one example as a means of illustration. The example
concerns the drinking water supply for New York City and the associated New York City
watershed agreement. The specifics discussed here are dated around the turn of the
millennium, but are described in present tense for illustrative purposes. As with many wicked
or untamed problems, also this case and the watershed agreement are still relevant (see for
instance New York Times, 2018). The specifics, however, may have changed. More details on
this example can be found for instance in Hermans et al. (2003) and NRC (2000). A short
introduction to the problem will help to understand the case.
The inhabitants of New York City depend on upstream rural watersheds for their drinking water
supply. Water is collected in several surface water reservoirs located in New York State. It is
not filtered before distribution to the users and New York City wants to maintain this situation
because filtration is very costly. Avoiding filtration is only possible if the water in the reservoirs
meets certain quality standards that ensure that public health is not endangered. The quality of
the water in one particular watershed, located in Delaware County, does not meet the required
standards. Based on the prevalent watershed rules, this watershed has a ‘restricted status’.
Location map of the New York City watersheds
(Source: https://www.dec.ny.gov/docs/water_
pdf/nycsystem.pdf accessed June 2022)
84

srotcA
4 aCTor analysIs
The problem owner in this case is the local government of Delaware County. The ‘restricted
status’ of the watershed prohibits the addition of polluting substances to water streams in the
area, which in turn severely restricts economic growth. The problem that Delaware County
faces is essentially the problem of how to reduce the pollution loads in the watershed in order
to create room for further economic growth. Pollution reduction could be achieved for instance
by reducing pollution from farms and other businesses, from the rural households that are not
yet connected to the sewerage grid or by upgrading the existing wastewater treatment plants.
Whatever the solution, it is likely to put local economic development at risk and it is likely to be
costly, stretching the resources of an already underdeveloped rural community.
4.4.2 Step 2: Make an Inventory of the Actors Involved
Identifying actors that are possibly involved in the problem and its solution is an iterative
process. By acknowledging the existence of other actors with different problem defini-
tions, shifts can occur in the problem definition and configuration of actors, specifically in
the exploration phase, which makes it possible that other actors become relevant for the
solution of the problem. Also later in the policy process, unforeseen shifts can take place
in the problem definition and configuration of actors, for example, when new solutions
are thought of, new parties appear on the scene or new technology becomes available.
Actor Identification Techniques
There are different methods that complement each other and that help analysts to make a
first selection of actors that may be involved. The different actor identification approaches
discussed by Mitroff (1983) and Bryson (2004) offer a useful starting point. The resulting
techniques are complementary, if partly overlapping, and their joint use is likely to result
in a list that has less risk of omitting important actors. They can be used by the analyst,
preferably in dialogue with the problem owner, and one or more key informants, persons
knowledgeable about the policy field.
– The interest-based or imperative approach identifies actors who feel strongly enough
about a certain policy problem or issue to act on their feelings. More generally, one
could ask ‘Who has an interest in or feels the consequences of the issues around which
the problem revolves, or the solutions that are being considered?’
– The institutional or positional approach reviews the existing policy-making structures
to identify actors with a formal position in policy-making. Studying the formal legisla-
tion, procedures, policy documents and so on provides a first indication of the parties
that are possibly involved.
– The reputational approach uses key informants related to the policy problem and asks
them to identify important actors. The resulting list of actors may be further expanded
by asking each of the actors on the list to nominate additional actors. The latter tech-
nique is known as ‘snowballing’ (Wasserman & Faust, 1994). A variation to this tech-
nique is for the analyst to ask for any of the seemingly important actors who have
important relationships with that actor.
– The social participation approach identifies actors to the extent that they participate
in activities related to a policy issue. For instance as part of committees, by attending
meetings or as part of platforms.
85

Actors
Policy AnAlysis of Multi-Actor systeMs
– The opinion leadership method identifies actors who tend to shape the opinions of
other actors. For instance, the opinions of certain universities or research groups, cer-
tain international organizations or certain individuals may be highly influential.
– The demographic approach identifies actors by such characteristics as age, sex, occu-
pation, religion, level of education, residence etc. This is relevant when policy prob-
lems and policy options have a different impact on different demographic groups.
Also, this can be particularly helpful to specify the types of ‘citizens’ or ‘voters’ that are
involved. Being more specific on this will be more useful than just including a generic
label for all citizens, voters or consumers.
– Finally, the system diagram and the causal map offer important leads. Relevant actors
can be identified by asking the questions: ‘Who influences, directly or indirectly, rel-
evant system factors?’ and ‘Who is impacted by changes in these factors?’ Attention
needs to be given here to the actors and factors inside the system, as well as in the
environment of the system.
Some Specific Points of Attention
Dealing with Composite Actors
A problem occurs when we have to deal with a composite actor. An organization can be
involved in the problem situation with more than one of its parts. For instance, a govern-
ment ministry typically consists of different directorates, departments and sections, each
with its own mandate and mission. The question is then which organization level we have
to appoint as an actor: the ministry as a whole, or one or more specific units within the
ministry.
When different units of an organization are involved with a problem based on their own
distinctive objectives and responsibilities, it is wise to include all these units as separate
actors.
When there is only one unit of an organization involved, then the question remains: is
that specific unit or the whole organization the actor? The rule here is: choose an organiza-
tion level as high as possible, without losing information in the process or involving objec-
tives that are irrelevant to the problem situation. However, avoid the inclusion of actors on
the level of ‘government’ or the ‘trade and industry’. Such a high level of aggregation limits
the usefulness of the analysis.
Text box 4.2 offers an example for the New York City drinking water case.
Text box 4.2 Composite actors in the New York City drinking water problem
In our example of Delaware County’s problem with New York City’s drinking water supply,
several composite actors play a role. For instance, the government of New York City is
organized in several bureaus and departments. However, only one department is responsible
for the City’s water supply: the Department of Environmental Protection. Therefore, this
department can be identified as the actor representing New York City’s interests. For Delaware
County, two distinct organizational units should be included as they have clearly different
interests and roles in the problem: the Department of Soil and Water Conservation, which is
concerned with environmental protection, and the Department of Planning and Economic
Development.
86

srotcA
4 aCTor analysIs
Setting Boundaries to Decision Arena or Actor Network
Depending on the problem, it may be difficult to identify the boundaries of the decision
arena or the actor network. Where to draw the line between actors that are important and
those that are not? The first general advice is not to be too restrictive in the identifica-
tion of actors to prevent premature focusing on a limited number of actors (Brugha &
Varvasovszky, 2000: 341). Although this is good advice for drawing up an initial long list of
actors, keeping the remainder of the analysis feasible means that one subsequently needs
to limit the number of actors to keep the time and resources required for the analysis
within reasonable limits (cf. Grimble & Chan, 1995: 119).
Suggestions for how to do this streamlining of the initial long list of actors are not easy
to find. However, three general guidelines may help:
– Ensure that the actor network is in line with the chosen level of problem analysis. For
instance, if the problem is on the regional or local level, there is often less need to
involve national level actors who often set relevant boundary conditions without active
involvement in local policy-making. Often, not always. If the problem analysis focuses
on the national level, there is less need for actors that are predominantly active on
the regional or local level. For instance, one could include the National Association of
Municipalities, but there will be little need to include individual municipalities.
– Ensure that the list of actors covers a balanced set of interests and roles. Ideally, all the
important interests and roles within a policy-making situation should be represented
in the initial actor selection. If possible, at least two or three actors with different roles
should be identified for each interest. For instance, if agriculture is an important inter-
est, one could identify the Ministry of Agriculture, the national association of farm-
ers’ cooperatives and an agri-business branch association as important actors. In this
regard, the categorization of actors using two or three different classification schemes,
as illustrated in Text box 4.3, offers a useful tool.
– Finally, a simple rule of thumb: experience indicates that a useful actor analysis often
includes anywhere between ten and twenty different actors. Taking less than ten actors
into account will increase the risk that important actors are being overlooked. Taking
more than twenty actors into account increases the risk that the analysis is insuffi-
ciently focused to be useful. This may be the case when the network boundaries are
too broad or when an unnecessary level of detail is employed.
Changing Roles of Actors
In determining arena boundaries and identifying actors, one has to keep in mind that the
inventory of actors who are actively involved at the moment of the analysis does not have
a predictable value for the future: new actors may participate and parties that play an
important role now may ‘exit the stage’ later on. For instance, climate change and energy
transition have the interest of many more actors now than it did some years ago. The same
applies to public health and pandemic disease control. This means that the list of actors
involved in policy problems that involve climate change will have changed dramatically in
the past years or so.
Furthermore, from the earlier descriptions it will be clear that, throughout the actor
analysis, one needs to check at regular intervals whether or not the initial list of actors is
still appropriate, or if new insights require new actors to be added or existing actors to be
removed from the list.
87

Actors
Policy AnAlysis of Multi-Actor systeMs
Problem Owner as an Actor in Actor Analysis
Make sure to include the problem owner in the list of actors and the subsequent steps in
actor analysis. In order to produce a complete overview of an actor network, it is impor-
tant to include the problem owner explicitly in the analysis – at least in those steps where
comparisons and overviews are made of the characteristics of various actors. This helps
to understand the position of the problem owner vis-à-vis the other actors. This is not
possible when the problem owner is excluded from the analysis.
Structuring the List of Actors
The clarity of the list of actors can benefit from dividing actors into categories. This can be
done in various ways, as illustrated in Text box 4.3. A first classification can be based on
the role and position in a governance system: government authorities on various levels;
companies (utilities and enterprises, both private and semi-public); non-governmental
organizations (NGOs); local interest groups (e.g. local community organizations); non-
organized interests or individuals.
Another complementary classification of actors can be made by looking at their inter-
ests in the problem or their position in a production chain. For instance, in relation to a
policy problem in the field of energy, such interest categories could include: energy provi-
sion, energy consumption, environmental conservation, economic development and so
forth. Use of this second classification logic will be helped by a specific assessment of
each actor’s individual interests. This is done in Step 4 of the actor analysis, so it will be
worthwhile to revisit and reconsider the initial categorization in a later stage of the analysis
– as part of an iterative process.
Text box 4.3 Actors involved in the New York City drinking water problem
The table below contains the actors identified for the New York City drinking water problem,
using two different classifications. The first column uses a classification based on their role in
governance, the second column contains the same actors, but grouped based on their main
interests.
Actors’ roles in governance Actors’ issues of interest
Federal government Environment
US Environmental Protection Agency US Environmental Protection Agency
US Department of Agriculture NYS Dep. Of Environmental Conservation
New York State (NYS) government Delaware County Soil & Water Conserv. District
NYS Dep. of Environmental Conservation Catskill Watershed Corporation
NYS Dep. of Health Health: Water supply and sanitation
NYS Dep. of Agriculture and Markets NYS Dep. of Health
Local government New York City Dep. of Environmental Protection
New York City Dep. of Environmental Protection Health interest groups in NY City
Delaware County Soil & Water Conserv. District Wastewater treatment plant operators
Delaware County Dep. of Planning & Econ. Dev. Agriculture
Towns and villages in Delaware County US Department of Agriculture
Non-governmental organizations NYS Dep. of Agriculture and Markets
Cornell Cooperative Extension Association Farmers
Catskill Watershed Corporation Watershed Agricultural Council
Watershed Agricultural Council Cornell Cooperative Extension Association
88

srotcA
4 aCTor analysIs
Organized local interests Local economic development
Delaware County Chamber of Commerce Delaware County Dep. of Planning & Econ. Dev.
Companies and non-organized interests Towns and villages in Delaware County
Farmers Small and Medium sized Enterprises
Small and Medium sized Enterprises Delaware County Chamber of Commerce
Wastewater treatment plant operators
Health interest groups in NY City
4.4.3 Step 3: Mapping Formal Institutions and Relations
Characteristics and positions of actors and their mutual relations have a formal and an
informal side. Knowledge about both sides is essential in order to understand actors and
their environments. The analysis should begin by mapping out the formal institutions and
relations because these are mostly easy to reconstruct using available documents. Map-
ping those formal institutions offers a good starting point to understand the background
against which other, informal, relations take shape, and to sketch the formal playing field
within which actors interact in a policy process. A ‘formal chart’ can be used as a means
of orientation in this.
The formal institutions offer a good basis to subsequently investigate the informal insti-
tutions and relations. Although formal authorities and formal hierarchical relations do not
fully determine the informal relations between actors, it would be wrong to assume that
hierarchical relations do not matter. On the contrary, they have a strong shaping influence
and they do limit the informal interaction processes. It is clear that legislation and formal
procedures strongly shape the interaction and influence the behaviour of parties. There-
fore it is good to know which laws and procedures actors have or will have to deal with.
Formal task settings determine to a large extent the identity of public organizations.
They derive formal rights and duties from these tasks, as well as associated authority and
resources to enforce those rights and act on their duties. Therefore, often their interests
and resources can be related back to these task settings. So it is a good thing to systemati-
cally map out those formal tasks. Formal authorities are also a type of resource, to which
we will turn later in the analysis when we map out the interdependencies between parties.
Drafting the ‘formal chart’ produces not only context information for the analysis of the
informal relations but also information about resource dependencies between actors in
a network.
Inventory of Relevant Formal Rights, Responsibilities and Relations
Formal relations can be described by:
– Describing the formal positions of actors and their rights and responsibilities. Actors’
rights and responsibilities are often formalized in laws and regulations. Especially for
government organizations, these positions and responsibilities are likely to be defined
in specific laws and regulations. Information about the position and tasks of non-gov-
ernment actors, although often more ‘fuzzy’ and somewhat less formal, can often be
found on websites, annual reports etc. Also, their room for manoeuvre will be limited
by the prevailing legislation, see third point of this list.
– Specifying formal relations between actors, when possible, by exhibiting an organization
chart with clarification. Do certain organizations or departments have a hierarchical
relationship? Is there a formal membership of representational arrangement? Who
89

Actors
Policy AnAlysis of Multi-Actor systeMs
bears final responsibility, or acts as coordinating agency? Who has a formal advisory
role in a decision-making process?
– Describing in short the most important laws, legislation, procedures and authorities that
play a role in the problem situation. This is likely to provide information in support of
the previous items, but also may yield additional information that is useful for getting
an idea of the position, interests, influence and ‘solution space’ of actors.
Drawing a Formal Chart
Parts of the information on formal positions and relations between actors can be pre-
sented using a so-called ‘formal chart’. Usually, such diagrams do not depict all the exist-
ing formal relations, but those deemed most important for the problem analysis. Note
that in fact each arrow in this formal chart represents a resource needed for analysing
dependencies. The construction of a formal chart is a matter of sound judgment. The
following guidelines apply:
1 Use the key legislation and formal agreements that apply to your specific problem and
decision arena as a first starting point.
2 Position the actors mentioned therein while preserving some intuitive vertical hierar-
chy (typically state-level actors such as ministries on top and local level actors such as
municipalities or executive branches more at the bottom).
3 Draw arrows only if they depict a specific formal relation between two actors. The
hierarchy flows from the actor with the outgoing arrow to the actor with the incoming
arrow. It therefore indicates some kind of formal hierarchy, control or influence.
4 Each arrow needs to be labelled. Use a short label to explain the formal relation.
5 You may use dotted rectangles to indicate clusters of actors that are all subject to a
similar type of law or formal rule.
6 Limit the formal chart to only show the most important formal relations – to avoid
cluttering of your diagram.
7 Provide a clear explanatory text with your formal chart, which includes reference to
the formal acts, laws and agreements that provide the basis for the formal relations
depicted in the diagram.
Text box 4.4 gives an example.
90

srotcA
4 aCTor analysIs
Text box 4.4 Formal chart for the New York City drinking water problem
The next figure shows the most important formal relations between the actors. It should be
noted that not all the informal influence relations have been included. As a result of this, the
non-governmental actors may seem less connected or less influential than they may actually
be.
Formal chart for the New York City drinking water problem
Single-sided arrows indicate a hierarchical relationship, two-sided arrows indicate formal representation
relationships/membership.
91

Actors
Policy AnAlysis of Multi-Actor systeMs
This figure shows that the US Environmental Protection Agency (USEPA) is ‘on top’ of the
hierarchy, according to the Safe Drinking Water Act (SDWA). Based on this Act, USEPA
determines whether or not New York City should filter its drinking water. The State agencies
have some influence over NY City Department of Environmental Protection (NYCDEP), as
their approval or permits are needed for some of the NYCDEP’s activities. NYCDEP and the
NY State Department for Environmental Conservation are jointly responsible for permits and
determining acceptable pollution loads. As a water supplier, NYCDEP is authorized to develop
and implement rules and regulations to protect the water quality in the City’s watershed,
including those in Delaware County, provided that NY State Department of Health approves of
these rules. This gives NYCDEP a strong position vis-à-vis the Delaware County agencies.
To protect New York City’s reservoirs from pollution while maintaining the economic viability
of the Catskill and Delaware watershed region, an agreement was signed between New York
City and the watershed communities. Part of this agreement was the establishment of several
programmes to support pollution reduction. The Catskill Watershed Corporation (CWC)
was established to administer and manage some of these programmes. The CWC is a non-
profit organization and its members consist of twelve representatives of West of Hudson
communities (of which six are from Delaware County), two members appointed by the State
Governor and one New York City employee. Since agriculture is the main economic activity
and the main source of pollution in the New York City watersheds, specific arrangements
were made concerning agriculture. This resulted in a Watershed Agricultural Programme,
which is implemented by the Watershed Agricultural Council (WAC), a farmer-led non-
profit organization. Its board consists of farmers, agri-business representatives and the
Commissioner of NYCDEP. The WAC has contracted the local Soil and Water Conservation
Districts (SWCD), the Cornell Cooperative Extension Association (CCE) and other parties to
assist in implementing its programme (note that these contractual relations are not depicted
to maintain a certain level of clarity in the diagram).
4.4.4 Step 4: Identifying Key Actor Characteristics
For a better understanding of actor networks, we also need to zoom into the level of the
individual actors. This means we want to analyse the values, perceptions and resources of
the different actors.
Problem situations are complex because different problem formulations co-exist and
because different actors are capable of influencing the resolution of these problems. The
initial problem formulation by the problem owner is just one of the possible formulations
of the problem that is faced in the initial situation. In the first parts of this analysis step,
the problem formulation of the different actors is systematically assessed by looking at
their interests, objectives and causal beliefs or perceptions. This is followed by a closer
look at the resources that different actors control.
Specify Interests of Actors
Interests are the issues that matter most to an actor, and usually interests have a clear
direction. Interests are not directly linked to a concrete problem situation, as opposed
to objectives, and are relatively stable. A company typically has an interest in making an
economic profit, whereas the direction will be to increase profits. Another typical company
interest will be continuity of business. For the Directorate General for the Environment
of the Netherlands Ministry of Infrastructure and Water Management, the main issue of
92

srotcA
4 aCTor analysIs
interest will be the environment, which needs to be conserved or protected (and remem-
ber that this can be seen from the formal chart in Step 3). For a politician the main interest
may be re-election. An assessment of the interests of an actor helps to estimate to what
extent certain objectives or solutions will be acceptable for the actor involved. Interests
can be found out by asking questions such as: Why is the problem situation of importance
to an actor? How are actors affected by the problem and why do they care?
Specify Objectives of Actors
Objectives indicate what actors wish to achieve in a certain situation, which changes they
would like to realize (or what they would like to maintain). All actors that are involved in a
problem have their own more or less clearly formulated objectives. They use these objec-
tives as a measure to judge the existing situation. The gap between the objectives or the
desired situation and the perceived existing or expected situation determines the nature
and seriousness of the problem. Objectives are the translation of an actor’s interests into
specific, measurable terms.
An actor usually has multiple objectives, some of which may have nothing to do with
the problem. Clearly, in our problem analysis we are first and foremost interested in the
objectives that are directly related to the problem situation. These objectives can be found
by asking the questions: What does the actor want to achieve when it comes to the problem
situation? When does the actor want to achieve this? And: Which specific costs and benefits
are associated with the problem situation or the proposed solutions for a certain actor?
Specify Perceptions
Most actors have their own, unique perceptions of a problem situation and these percep-
tions can differ significantly. When dealing with complex policy problems, it is neither easy
nor useful to determine ‘who is right’ (see Chapter 2). Thus, instead of looking for who
is right, we try to map out the similarities and differences between problem perceptions
in the actor analysis. After all, even if ‘wrong’ problem perceptions arise, they exist, they
are a part of the problem situation and they will influence the behaviour of the actors who
hold them! Therefore, all perceptions should be mapped in a problem analysis, staying as
close as possible to the way the actor sees the system – whether we as analysts believe
they are right or wrong.
The specific problem perceptions of actors can be specified in causal maps for individ-
ual actors, as is done for instance in Dynamic Actor Network Analysis (Bots et al., 2000).
Actors may distinguish different factors and may have different assumptions of the main
causal relations between those factors: Is there a causal relation? What is the direction
and intensity of the relation? Is there a direct relation between factors A and B, or is factor
A mainly influenced by factor B via factor C? However, for our purposes we need not map
these detailed diagrams, but we can get a useful impression by addressing the following
questions:
– What is the actor’s perception of the problem? What is the core of the problem: which
factors are central in the system and what are the causal relations between factors?
– What are the main causes of the problem according to an actor? (Rule in this course:
limit to a maximum of 3)
– What possible solutions do they distinguish with regard to the problem situation and
its causes? (Rule in this course: limit to a maximum of 3)
93

Actors
Policy AnAlysis of Multi-Actor systeMs
Make a Systematic Comparison
With the help of the previous steps, a table can be completed that summarizes the prob-
lem formulation for each actor. The result will be an overview table as depicted in Table 4.3.
Note that the complete overview table may be quite large.
Table 4.3 Overview table of actors’ problem formulations
Actors Interests Desired Situa- Existing or Causes Possible
tion/Objectives Expected Situa- Solutions
tion and Gap
Problem owner
Actor 1
Actor 2
…
Actor N
The summary table supports a systematic comparison of the problem formulation of the
problem owner and the other actors. This helps to identify the similarities and differences,
as well as common objectives and shared interests, or potential conflicts. These insights
can be used to complement the initial problem formulation and problem analysis. Also,
they can help to formulate recommendations for the problem owner related to the interac-
tion with other actors, and on how to influence other actors.
94

srotcA
4 aCTor analysIs
95
esac retaw
gniknird
ytiC
kroY weN
eht
ni
srotca
fo
snoitalumrof
melborP
5.4
xob
txeT
snoitulo
S elbissoP
sesuaC
noitautiS detcepxE ro gnitsixE
sevitcejbO/noitautiS
deriseD
stseretnI
srotcA
TI ,msiruot(
ymonoce
yfisreviD
-lucfifid
evah seimonoce
laruR
tsewol gnoma slevel emocnI
deniatsus
,sessenisub
yhtlaeH
-poleved
cimonoce
lanoigeR
tnemtrapeD
ytnuoC
erawaleD
latnemnorivne
netfos
,)secivres
latnemnorivne
,ediwnoitan
seit
lacol ni enilced ,yrtnuoc eht ni
-yolpme doog
,htworg
cimonoce
fo snezitic
fo
eraflew
,tnem
cimonocE
dna
gninnalP
fo
snoitaluger
snoitcirtser
rehtruf esopmi
selur
fo slevel hgih ,sessenisub
seitinutroppo
tnem
ytnuoC
erawaleD
tnempoleveD
tnemyolpmenu
mraf-no
evorpmi
:srehto gnomA
-mraf
yriad
yllaicepse ,sremraF
rof hgih eb yam slevel tnerruC
dna lios suoirav
no erocs
dooG
-sysoce
dna
namuh
fo
noitcetorP
retaW
& lioS
ytnuoC
erawaleD
-elpmi
hguorht
tnemeganam
,secnatsbus
gnitullop time
,sre
od tub ,sesoprup retaw gniknird
rof( sretemarap
ytilauq
retaw
htlaeh
met
tcirtsiD
noitavresnoC
dehsretaW
eht
fo noitatnem
tnemtaert
retawetsaw
od sa
melborp htlaeh tcerid a esop ton
aidraig ,surohpsohp
ecnatsni
emmargorP
larutlucirgA
dna
stneve
retaw mrots ,stnalp
stnatibahni ytnuoC erawaleD rof
)muidiropsotpyrc
dna
sdlohesuoh
fo sknat citpes
dlo
egarewes
eht ot detcennoc
ton
latnemnorivne
tcirts esopmI
maertspu
eht ni seitinummoC
gniregnadne ,hgih oot era sleveL
eht ni
ytilauq
retaw
dooG
-oce dna
namuh
fo
noitcetorP
fo tnemtrapeD
ytiC
YN
-moc
dehsretaw
no snoitaluger
slevel
hgih
oot time sdehsretaw
-egnarra ylppus retaw tnerruc
deef taht sdehsretaw
maertspu
efas
fo noisivorp
,htlaeh
metsys
noitcetorP
latnemnorivnE
sdnal
eht
esahcrup
,seitinum
-epse
,secnatsbus
gnitullop
fo
fo deen gninetaerht ,stnem
:esac siht ni(
sriovreser
CYN
eht
-tibahni
CYN
ot
retaw
gniknird
pots
ot sriovreser
eht dnuora
dna
aidraig
,surohpsohp
yllaic
noitartlfi ni stnemtsevni yltsoc
aidraig ,surohpsohp
fo slevel
wol
ecirp
elbadroffa
na
ta
stna
ereht
seitivitca
gnitullop
muidiropsotpyrc
seuqinhcet
)muidiropsotpyrc
dna
fo gnirewol
elbaniatsus
erusnE
sdehsretaw
ni slevel noissimE
gniknird CYN eht ,yltnerruC
efas dna
ytilauq
retaw
dooG
noitcetorp
latnemnorivnE
APE
SU
ro sdehsretaw
ni
slevel noissime
eht
ot
noitaler ni hgih oot
era
ton seod metsys ylppus retaw
secruos ylppus
retaw gniknird
noitartlfi
ni tsevni
seod
taht
metsys ylppus gnitsixe
sdradnats lanoitan eht teem
ytiC
kroY weN
rof
noitartlfi edulcni
ton
tnemeganam
mraf-no
evorpmI
-ram
larutlucirga
fo erutcurtS
wol si gnimraf morf emocnI
dna gnimraf
morf
emocni
dooG
erutlucirgA
ytnuoC
erawaleD
sremraF
-lucirgA
dehsretaW
fo pleh htiw
-nosaernu
htiw denibmoc
,stek
dna – kaelb era stcepsorp dna
-mraf rof stcepsorp
erutuf
doog
licnuoC larut
kroY
weN
morf sdnamed
elba
-norivne evitcirtser yb denesrow
ssenisub
gni
sdehsretaw
enitsirp rof
ytiC
snoitaluger latnem
latnemnorivne
tcirts esopmI
sdehsretaw
ni sdaol noitulloP
yltsoc era stnemegnarra tnerruC
na ta ylppus
retaw
gniknird
efaS
gnivil
fo
stsoc
dna
htlaeh
cilbuP
rof
spuorg
tseretni
htlaeH
dehsretaw
no snoitaluger
-saem
tnerruc
dna hgih oot
era
-recnu ynam oot evael llits dna
tsoc elbadroffa
snezitic
CYN
eht
esahcrup
,seitinummoc
era
meht
ecuder ot nekat
seru
htlaeh cilbup gnidrager seitniat
dna sriovreser
eht
dnuora sdnal
tneicfifus
ton
erutuf eht ni dna won sksir
sdnal
eseht
ot
ssecca tcirtser
.ctE

Actors
Policy AnAlysis of Multi-Actor systeMs
The above table shows that water quality in the reservoirs downstream of Delaware County
does not meet the drinking water standards. This is a problem for New York City and its
Department of Environmental Protection because it means they cannot use this water
for public drinking water supply without treating it. Restricting the pollution levels in the
watersheds is a solution to New York City DEP, but creates a problem for the actors in
Delaware County: it would damage the economy in a region that is already lagging behind in
terms of economic development. The health interest groups in New York City consider the
current efforts of the New York City government and the local watershed actors as a problem.
They are altogether sceptical about the effectiveness of pollution reduction by the watershed
communities and they claim that New York City should enforce a strict ban on all economic
activities in sensitive areas, by buying up lands and restricting access to it. Otherwise they will
be forced to build a filtration plant for its drinking water supply in the near future anyway.
Resources of Actors
In this sub-step, we investigate the dependency of the problem owner on the actors in his
environment. This relationship is determined by three things: the importance to the prob-
lem owner of resources of other actors, the extent to which those resources are replace-
able and the degree to which the interests and objectives of other actors are similar (Hanf
& Scharpf, 1978). Furthermore, it is important to know how important and urgent the
problem is to other actors: this will determine whether or not actors are likely to be willing
to play an active role in the debate and resolution.
The degree to which a problem owner depends on an actor is related to the resources
of that actor. Critical actors are those on whom a problem owner critically depends for
solving his problem. Identifying critical actors is an important part of actor analysis, and
logically starts with an inventory of the resources of the various actors.
The resources of actors are the formal and informal means that are available to the
actors to realize their objectives. Formal means are for instance authority (power of deci-
sion) and instruments (subsidies). An example of an informal resource is information. The
following resources can be distinguished (adapted from Kok, 1981):
– information;
– knowledge (and skills);
– manpower (including often skilled manpower);
– money (or access to money through loans or credit facilities);
– technology, equipment, infrastructure;
– authority/formal power (as per the laws and regulations in Step 3);
– position in the network: support from or access to other actors;
– legitimacy;
– organization (ability to mobilize and use resources effectively and efficiently);
– (social) media platform or access;
– others, such as ….
In this step we find out which resources are available to various actors. Since every actor
has a spectrum of resources, actor analyses often do not benefit from an exhausting
overview. Only the resources that are most relevant to the problem situation need to be
included. Make sure to be specific when listing resources. So do not simply ‘select’ from
the earlier list, but if you do so, specify what kind of knowledge an actor has that is of
96

srotcA
4 aCTor analysIs
relevance to the problem, or what kind of authority an actor has that is of importance in
the arena.
Resource Dependency and Critical Actors
The resource dependency of one actor in relation to a second actor depends on the impor-
tance of the resources held by the second actor and the degree to which these resources
can be replaced by other resources. For instance, most Western countries heavily depend
on oil imports to sustain their economies. Thus, they are highly dependent on OPEC
countries. However, as alternative fuel technologies are being developed, such as biofu-
els, hydrogen and solar energy, this resource dependency is decreasing. Schematically, the
issue of resource dependency can be illustrated as in Table 4.4:
Table 4.4 Resource dependency
Limited Importance Great Importance
Limited options to replace Medium dependency High dependency
Can easily be replaced Limited dependency Medium dependency
Using Table 4.4 helps to assess resource dependency but tends to overlook resource
dependency related to blocking power. As Hanf and Scharpf (1978) back in the days argued,
the problem owner not only depends on actors with the resources to support problem-
solving, or to sustain existing systems, but he also depends on actors with resources to
hinder the activities of the problem owner, or to prevent the successful implementation
of a solution. Actors that are either important for their ‘power of realization’ or for their
‘blocking power’ are the critical actors – the actors that a problem owner cannot ignore
(Table 4.5) (Enserink, 1993).
Table 4.5 Overview table for determining critical and non-critical actors
Actors Important Replaceable? Dependency Limited, Critical Actor?
Resources Average, High Yes/No
Actor 1:
Actor 2:
Actor N:
4.4.5 Step 5: Summarizing Interdependencies
Assess the Criticality, Dedication and Support of Actors
The previous step shows you the ‘critical actors’. Your problem owner is to an important
extent resource dependent on those actors. Resource dependency of your problem owner
on another actor is determined by the extent to which the realization of your problem
owner’s objectives depends on the resources controlled by that other actor.
Interdependency is slightly different. It reflects a two-way relationship, and is influenced
not only by the resources of actors but also by their interest in the problem and their
dedication to act on it. Two actors that both take a high interest in a problem, and that
both control critical but different resources to influence this problem, can be said to be
interdependent. The importance of a problem to an actor will appear from his problem
formulation and the extent to which his core interests are affected by the problem or by
possible solutions. In addition, it can help to assess whether an actor will be affected by
97

Actors
Policy AnAlysis of Multi-Actor systeMs
clear costs or benefits. If he is affected, he will probably be a ‘dedicated actor’, or he may
become one in time. If an actor does not experience any clear costs or benefits, or if costs
and benefits seem to negate each other, this actor will be less likely to try to influence the
problem analysis and the choice and implementation of a particular solution. This means
that such actors are less likely to pose a threat to the problem owner, but also that it will
be more difficult for a problem owner to mobilize their active support. In such cases, we
are dealing with a ‘non-dedicated’ actor.
Dedicated actors do not necessarily share the same interests and objectives. The previ-
ous step of the actor analysis, in which the interests and objectives of actors have been
assessed, enables the analyst to assess if actors have interests that are similar to the
interests of the problem owner, or if actors have interests that conflict with the interests of
the problem owner. Actors with interests and objectives that are well-aligned or similar to
those of the problem owner are more likely to offer support. Actors with conflicting inter-
ests are more likely to offer opposition. Adding this information to the results of the previ-
ous identification of critical and non-critical actors, and of dedicated and non-dedicated
actors, enables one to complete an overview of dependencies of the problem owner on
the different actors.
Overview Table for Classification of Actor Dependencies
Completing the cells of Table 4.6 provides an overview of the different types of actors
on whom the problem owner depends to a larger or lesser degree. Table 4.6 offers the
problem owner an impression of the possible reactions of actors in his environment to his
problem formulation and the intended solution.
Table 4.6 Overview table for classification of interdependencies
Dedicated Actors Non-dedicated Actors
Critical Actors Non-critical Actors Critical Actors Non-critical Actors
Actors that Actors that
Support: Similar/ will probably will probably Indispensable Actors that do not
supportive inter- participate and are participate and are potential allies that have to be involved
ests and objectives potentially strong potentially weak are hard to activate initially
allies allies
Potential blockers
Opposition: Con- Potential blockers Potential critics of Actors that need
that will not act
flicting interests of certain changes certain changes little attention
immediately
and objectives (biting dogs) (barking dogs) initially (stray dogs)
(sleeping dogs)
Visualizing Interdependencies
The information contained in the overview table for interdependencies (Table 4.6) can
also be visualized in ‘alignment-interest-influence’ diagrams (ODI, 2010) or ‘power-inter-
est grids’ (Figure 4.1) (Bryson, 2004; Eden & Ackermann, 1998). In some cases, such maps
may have certain advantages over tables, especially when they provide a quick illustration
of important patterns in the actor environment of the problem owner. In these maps,
the power and interests of actors are used to classify different actors, whereas pluses
and minuses are used to indicate if an actor supports or opposes the main interests and
objectives of the problem owner. Critical actors are those with a high level of power – i.e.
important resources – while dedicated actors are those with a high level of interest in the
98

srotcA
4 aCTor analysIs
problem. Such maps may be used to characterize actors (Bryson, 2004) and to formulate
a generic advice regarding the types of relationships a problem owner typically might
establish with actors in different quadrants (Johnson et al., 2005).
Context setters: Key players:
High
Meet their needs Engage
Keep satisfied Manage closely
Handle with care
Crowd: Subjects:
Monitor Some effort
Minimal effort Show consideration
Low Keep informed
Low High
99
rewoP
Level of Interest
Figure 4.1 Mapping actor dependencies: Power/interest matrix
Drawing Conclusions from Overview Tables and Maps
The insights contained in overview tables or dependency maps can be translated into
different types of conclusions. The diagrams depict the current position of actors. This
will hold important information. At the same time, because actors are interdependent, it
is also possible to think of ways to change the current picture, and to influence the posi-
tion of actors. That way, one can think of actors that could be ‘moved’ around in the grid.
Especially the power-interest grid or similar diagrams are useful to trigger thinking about
the latter (see ODI, 2010).
The overview of actor dependencies can be a reason to iterate in your problem structur-
ing steps and modify the problem formulation. For instance by identifying key interests in
addition to those of the problem owner, that need to be taken into account – i.e. it is wise
to at least ensure that the problem formulation recognizes the key interests of critical and
dedicated actors.
The overview can also be used to identify existing or potential coalitions and alliances that
might need to be established, encouraged or discouraged, mainly in relation to the dedi-
cated and non-dedicated critical actors (compare Koppenjan, 1993). Thought needs to be
given to the fact that seeking support and coalition building is not necessarily a remedy for

Actors
Policy AnAlysis of Multi-Actor systeMs
the presence of dedicated critical actors that may potentially block certain changes. Their
status of critical actor gives them the power of veto to oppose majorities. Therefore the
analyst also needs to indicate what opportunities there are to overcome differences and
to avoid or defuse conflicts.
Another approach to coalitions and alliances may be to think about the actor constel-
lation as a strategic game where the action (activation of the actor’s means) by actor A
may induce a re-action by actor B. The latter re-action might be either supportive or a
counter-action, which in turn may seduce other actors in the arena to choose position
and/or employ their means to support or counter the initiatives by A and B. Playing these
kinds of virtual games may lead to the insight that only if special conditions are met, for
instance only if critical actors A and B cooperate and both put in their means, a policy has
a fair chance to succeed.
Finally, the analyst can reflect on possibilities to change the position of actors in the
power/interest matrix. Are there ways to mobilize supporting ‘context setters’? What could
turn ‘biting dogs’ into ‘sleeping dogs’ or ‘barking dogs’ to prevent ‘sleeping dogs’ from
waking up, or to raise the dedication from critical non-dedicated actors with supportive
interests and objectives? The latter is typically done through education and awareness-
raising activities or maybe even active engagement, participation and co-design. This line
of thinking is similar to that discussed by Quan et al. (2019) to see where actors’ abilities
or power could be strengthened and where actors’ interests or motivations need atten-
tion.
Difficulties and Pitfalls in Mapping Actor Interdependencies
Whether one uses a table or a matrix, one has to be aware of a number of difficulties and
pitfalls when making and using a power-interest grid.
First, make sure that the overview table or power-interest grid is indeed consistent with
the earlier tables and diagrams. This may sound obvious, but too often, power-interest
grids show actors as ‘low’ on power that, according to the resources tables, are critical,
or the other way around. The same applies to the problem formulation table and the
depicted level of interest or support of actors. Action groups for instance may be very loud
but lacking a real constituency and may have little means or actual influence. Therefore,
make sure to use these tables to build your final overview table and power-interest grid.
Sometimes the actors have not determined their position yet, or they are internally
divided. If this is the case, they should not be included in the table. The solution can be
to distinguish between different units within composed actors, or to put question marks
behind the positions of the actors and to include them, if necessary, with question marks
in two cells. Assigning them a preconceived position might turn into a self-fulfilling proph-
ecy and may be counter-productive.
The tables and maps were initially developed to be used for stakeholder analysis in
relation to project design and implementation. In those cases, it is often easier to assess
who is likely to support a specific project, and who is likely to oppose it (or parts of it).
However, when the focus is on a policy problem, rather than a specific project, a range of
solutions is still possible, and assessing support and opposition is likely to be conditional
on the specific types of solutions one has in mind, and is linked to the level at which one
looks at interests and objectives. At a higher level, interests may be similar among actors
(e.g. in the case of New York, many actors may share an interest in good water quality in
the watershed), but at the level of specific objectives, conflicts may arise (e.g. the objective
100

srotcA
4 aCTor analysIs
of fewer agricultural activities in a specific part of a watershed). Therefore, when used to
analyse policy problems, these tables and maps require a clear explanation of why certain
actors are believed to be opposing or supportive.
Related to the previous point of attention, it is not uncommon that a first actor analysis
results in an overview table with no critical opposing actors. If this is the case, it needs
to trigger another, deeper, look at actors’ objectives and perceptions. Because if really all
critical actors would be in agreement, solving the problem at hand should be easy; all
agree on what needs to be done and how. If you are facing a truly complex problem, this
will not be the case.
4.4.6 Step 6: Confront the Initial Problem Formulation with the Findings
The last step of an actor and network analysis consists of the confrontation of the find-
ings with the problem owner’s problem formulation. The logical starting point here is the
conclusion you have drawn based on the overview tables and power/interest diagram in
the previous step. Use these as your basis. However, in addition to this summarizing step,
also each of the previous contributing steps offers potentially interesting new insights.
Therefore it is necessary to list the conclusions and insights from the different analysis
steps, translating them into a list of potential threats and opportunities stemming from
the characteristics of actors and networks. These conclusions, threats and opportunities
may have consequences for:
– the content of the problem analysis,
– the interaction with actors,
– the system diagram and
– research activities.
Consequences that Relate to the Content of the Problem Analysis of the Analyst
This actor and network analysis will often be a reason for reformulating the problem. Pos-
sibly the core of the problem is different from the original one, a different demarcation is
needed, other factors are noticed and causal relations are different.
Consequences that Relate to Dealing with Other Actors
The actor and network analysis can be used to inform the problem owner about the con-
sequences of his problem formulation. Will it provoke resistance or support? Regarding
which points? With which actors? It can indicate with which actors a fruitful cooperation
is possible and from which actors opposition can be expected. The advice can also include
involving actors with the further problem analysis or even to set up a future course inter-
actively.
Consequences that Relate to the System Diagram
When a different problem demarcation is needed the system diagram may need to be
adapted accordingly. The same is true when the analyst judges that major concerns of
other, critical actors need to be taken into account. The latter may imply that additional
outcomes of interest/criteria might need to be added. When means of those other criti-
cal actors are essential to reach the objectives these new means may need to be added
to the diagram too. In this iterative way the system diagram is adapted to match the new
insights. We will come back to this in Chapter 6.
101

Actors
Policy AnAlysis of Multi-Actor systeMs
Consequences Regarding Research Activities
Thirdly, knowledge gaps and new research questions may have been discovered that relate
to the causal, substantial aspects of the problem situation, as well as to the social dimen-
sions. These need to be specified at the end of the actor and network analysis. They are
possible ingredients for the research approach that is presented in the plan of approach
at the end of the issue paper.
Text box 4.6 has an example of consequences of the actor analysis for Delaware County,
as the problem owner in the New York City drinking water problem.
Text box 4.6 Consequences of the actor analysis for Delaware County
The actor analysis for the New York City drinking water supply problem suggests that the
problem owner, Delaware County, indeed faces a dilemma. However, the dilemma is not so
much what specific pollution-reducing alternatives to implement and how to bear the costs
of those. In fact, costs may be less of a problem than effectiveness. Money has been made
available by New York City and New York State to support the implementation of measures.
The sums available through various funds under the watershed agreement are considerable
and may even help to improve the local farming system. However, health interest groups in
New York City worry about the adequacy of pollution reduction measures to meet the water
quality standards – and they may have a point. Nevertheless, given the apparent power and
influence of the government coalition of New York State and City actors that favour pollution
reduction, it will be difficult for Delaware County to object to the need for pollution reduction
as something that is a questionable exercise. The current agricultural activities are not
very profitable economically, and are still at risk of being further impaired by the pollution
restrictions. This suggests an important knowledge gap. The problem owner should consider
widening its problem formulation to look not only for means to reduce pollution but also for
opportunities for economic development.
4.5 Points of Attention in Actor Analysis
Risks and pitfalls are manifold when executing stakeholder or actor analyses. Below we
highlight some of the main points of attention, limitations and ways to cope with those.
4.5.1 Trustworthy Sources of Information
Real-world actor networks can be characterized as messy, dynamic and ill-defined sys-
tems. The task of an analyst is to provide some structure in this mess that allows him to
extract some useful lessons for the problem formulation and interaction strategies of the
problem owner. In this task, the analyst requires sound and trustworthy information on
the characteristics and relations of the actors. Unfortunately, such information sources
are not always easy to come by.
Information for an actor analysis can be obtained through text analysis: finding out per-
ceptions, resources and objectives from written documents. On a generic level – and for
an analysis of formal positions of actors – websites, annual reports and official policy
statements may be available. However, when it comes to assessing actor perceptions and
their informal relations and means of power, useful written sources of information are
generally rare. This means that analysts will have to complement the information from
102

srotcA
4 aCTor analysIs
written sources with interviews with the most important actors and with some key infor-
mants. This means that data collection often has to be done ‘on-site’, and is likely to
require a substantial amount of time and resources.
Furthermore, getting access to actors and ensuring their collaboration, poses additional
challenges – not everyone is willing to share their ideas with an analyst, or respondents
may provide strategically distorted or desirable answers to questions, rather than speak-
ing their minds truthfully.
To counter the risks and limitations inherent in any single source of information about
actors’ characteristics, the reliability of the information should be improved by compar-
ing and cross-checking information from different sources, by expanding the number of
interviews and questioning actors about each other’s positions.
When there is a lack of data, problem perceptions, objectives, interests and/or depend-
encies can be estimated by the researcher, using logical reasoning based on the informa-
tion that is available. However, here the researcher needs to be very careful. Estimations
may be wrong, and there are many examples where problem owners or analysts hold the
wrong assumptions about other actors’ objectives or resources. In those cases, a problem
owner might be in for a very unpleasant surprise, for instance when an alleged supporter
turns out to be a fierce opponent, or when a ‘sleeping dog’ turns out to be wide awake.
Therefore, it is sometimes better to indicate that information is lacking. This means that
there is a knowledge gap, which leads to the formulation of a research question for future
research. But in any case, it is very important to indicate the sources of information used
for an actor analysis, to indicate which information is based on estimations and to identify
key assumptions that underlie the final conclusions and recommendations. When these
are not specified, it has a negative impact on the reliability of the whole analysis – and it
makes an analyst vulnerable to the justified criticism of a disappointed problem owner
once he finds out the recommendations from an actor analysis are counter-productive!
Also remember that parties do not always have crystallized opinions and that these
opinions can change. This information is especially interesting because it shows that there
are possibilities to influence the realization of problem formulations and courses of solu-
tions.
4.5.2 Actor Analysis Tries to Hit a Moving Target
The findings of the actor analysis result in a snapshot. Actors’ problem perceptions change
continually, as do their objectives, strategies and mutual relations. Actually the mere exer-
cise of executing an actor analysis may influence the position and attitude of actors, for
instance when they become aware of their (limited) power position in the game. This
continual dynamic causes strategic and institutional uncertainty. This uncertainty needs
to be taken into account. The possibility to discount this uncertainty in the analysis itself
is limited. That is why it is important to be aware of the fact that the validity of the findings
from an actor analysis is limited in time. The most important remedy is to re-execute the
analysis after a period of time.
4.5.3 Some Important Limitations of Actor Analysis
The actor analysis classification is static, but actors are changing constantly. Allies today
can be opponents tomorrow and vice versa. Furthermore, limits in access to information
about actors may result in incorrect assumptions or black spots in the analysis. Therefore
the problem owner can be thrown off guard by the results. As said before there is a risk
103

Actors
Policy AnAlysis of Multi-Actor systeMs
that the actor analysis will work as a ‘self-fulfilling prophecy’: because actors are carelessly
earmarked and therefore treated as an opponent by the problem owner, they may feel left
out and may start acting as an opponent.
The table and dependency maps can have a polarizing effect: they divide the field into
actors that support or oppose the objectives of the problem owner as if there are no posi-
tions in the middle and as if the problem has only two extreme positions (for instance an
environmental interest versus an economical interest). In reality there are often several
potential positions which make it possible to bridge conflicts that focus on one dimension
by focusing attention on other dimensions (van Eeten, 2006). Sustainability for instance
might bridge the gap between environment and economy in the earlier example.
Finally, Scholes (1998) points out that analysing dependencies, with its focus on
resources and power, entails a risk of losing sight of ethical considerations. For instance,
dependency analysis may suggest minimal effort is required in relation to non-critical
actors. However, these may well be disadvantaged groups in society for whom public
policymakers have some responsibility in terms of improving their involvement; taking
into account their interests and creating opportunities. This limitation can be addressed
by using some other actor analysis methods, such as an ‘ethical analysis grid’ (Bryson,
2004), but it also helps if the analyst is aware of this, and pays special attention not only
to the critical actors but also to those that are dedicated but non-critical.
4.6 Takeaways
– You cannot formulate a problem, and you cannot play a policy game, if you do not
know who the players are and what the main rules of the game are.
– In policy analysis, games take place in arenas, where the players are called actors and
where the rules are provided by institutions.
– Understanding actors starts with understanding the network and institutions and
each actor’s objectives, perceptions and resources.
– Actor analysis offers methods to investigate the actor characteristics to make explicit
their interdependencies, and to support problem structuring.
– The described method provides a basis for problem structuring, but should not be
treated as ‘stable truth’. Caution is needed among others around information limita-
tions and self-fulfilling prophecies.
References
Axelrod, R. (Ed.) (1976). Structure of Decision. The Cognitive Maps of Political Elites.
Princeton: Princeton University Press.
Bennet, P., Cropper, S. & Huxham, C. (1989). Modelling Interactive Decisions: The
Hypergame Focus. In: Rosenhead, J. (Ed.), Rational Analysis for a Problematic World
(pp. 283-314). Chichester: John Wiley & Sons.
Bots, P. W. G., van Twist, M. J. W. & van Duin, J. H. R. (2000). Automatic Pattern
Detection in Stakeholder Networks. In J. F. Nunamaker & R. H. Sprague (Eds.),
Proceedings HICSS-33. Los Alamitos: IEEE Press.
Bougon, M. G., Baird, N., Komocar, J. M. & Ross, W. 1990. Identifying Strategic Loops:
The Self-Q Interviews. In: A. S. Huff (Ed.), Mapping Strategic Thought. Chichester: John
Wiley & Sons.
104

srotcA
4 aCTor analysIs
Brugha, R. & Varvasovszky, Z. (2000). Stakeholder Analysis: A Review. Health Policy and
Planning, 15(3), 239-246.
Bryson, J. M. (2004). What to Do When Stakeholders Matter. Stakeholder Identification
and Analysis Techniques. Public Management Review, 6(1), 21-53.
Coleman, J. S. (1990). Foundations of Social Theory. Cambridge: Harvard University
Press.
Eden, C., & Ackermann, F. (1998). Making Strategy: The Journey of Strategic Management.
London: Sage Publications.
Enserink, B. (1993). Influencing Military Technological Innovation. Delft: Eburon.
Fraser, N. M. & Hipel, K. W. (1984). Conflict Analysis: Models and Resolutions. New York:
North-Holland.
Freeman, R. E. (1984). Strategic Management. A Stakeholder Approach. Boston: Pitman
Publishing Inc.
Grimble, R. & Chan, M. (1995). Stakeholder Analysis for Natural Resource Management
in Developing Countries. Some Practical Guidelines for Making Management More
Participatory and Effective. Natural Resources Forum, 19(2), 113-124.
Hanf, K. & Scharpf, F. W. (1978). Inter-Organizational Policy Making. Thousand Oaks:
Sage Publications.
Hermans, L. M. (2005). Actor Analysis for Water Resources Management. Putting the
Promise into Practice. Delft: Eburon.
Hermans, L. M., Beroggi, G. E. G. & Loucks, D. P. (2003). Managing Water Quality in a
New York City Watershed. Journal of Hydroinformatics, 5(3), 155-168.
Hermans, L. M. & Cunningham, S. W., with contributions by M. de Reuver and
J. S. Timmermans (2018). Actor and Strategy Models. Practical Applications and Step-
Wise Approaches. Hoboken, NJ: John Wiley & Sons.
Hermans, L. M. & Thissen, W. A. H. (2009). Actor Analysis Methods and Their Use for
Policy Analysts. European Journal of Operational Research, 196(2), 808-818.
Hipel, K. W., Fang, L. & Kilgour, D. M. (2008). Decision Support Systems in Water
Resources and Environmental Management. Journal of Hydrologic Engineering, 13(9),
761-770.
Howard, N. (1971). Paradoxes of Rationality: Theory of Metagames and Political Behavior.
Cambridge, MA: The MIT Press.
Howard, N. (1989). The Manager as Politician and General: The Metagame Approach
to Analysing Cooperation and Conflict. In Rosenhead, J. (Ed.), Rational Analysis for a
Problematic World (pp. 239-261). Chichester: John Wiley & Sons.
Jobert, B. (1989). The Normative Frameworks of Public Policy. Political Studies, 37, 376-
386.
Johnson, G., Scholes, K. & Whittington, R. (2005). Exploring Corporate Strategy. Essex:
Prentice Hall/Financial Times.
Keeney, R.L. (1992). Value-Focused Thinking. A Path to Creative Decisionmaking.
Cambridge, MA: Harvard University Press.
Kenis, P. & Schneider, V. (1991). Policy Networks and Policy Analysis: Scrutinizing a New
Analytical Toolbox. In Marin, B., Mayntz, R. (Eds.), Policy Networks. Empirical Evidence
and Theoretical Considerations. Frankfurt am Main: Campus Verlag.
Klijn, E. H. (1997). Policy Networks: An Overview. In W. J. M. Kickert, E. H. Klijn &
J. F. M. Koppenjan (Eds.), Managing Complex Networks. Strategies for the Public Sector
(pp. 14-34). Thousand Oaks: Sage.
105

Actors
Policy AnAlysis of Multi-Actor systeMs
Korbee, D., Nguyen, H. Q., Hermans, L. M. & Phi, H. L. (2019). Navigating the
Bureaucracy: An Analysis of Implementation Feasibility for the Mekong Delta Plan,
Vietnam. Journal of Environmental Planning and Management, 62(9), 1545-1561.
Kok, W. (1981). Signalering en Selectie. Achtergrondstudie nr. 3, uitgebracht aan de
Commissie Hoofdstructuur Rijksdienst, Den Haag.
Koppenjan, J. F. M. (1993). Management van de beleidsvorming. Een studie naar de
totstandkoming van beleid op het terrein van het binnenlands bestuur. Den Haag: VUGA.
MacArthur, J. (1997). Stakeholder Analysis in Project Planning: Origins, Applications and
Refinements of the Method. Project Appraisal, 12(4), 251-265.
Mayer, I. S., van Daalen, C. E. & Bots, P. W. G. (2004). Perspectives on Policy Analyses:
A Framework for Understanding and Design. International Journal on Technology, Policy
and Management, 4(2), 169-191.
McDaniels, T. L., & Thomas, K. (1999). Eliciting Preferences for Land Use Alternatives:
A Structured Value Referendum with Approval Voting. Journal of Policy Analysis and
Management, 18(2), 264-280.
McKeown, B. & Thomas, D. (1988). Q-Methodology. Newbury Park: Sage.
Mitroff, I. I. (1983). Stakeholders of the Organizational Mind. Toward a New View of
Organizational Policy Making. San Francisco: Jossey-Bass.
National Research Council (NRC). (2000). Watershed Management for Potable Water
Supply: Assessing New York City’s Approach. Washington, D.C.: National Academy
Press.
New York Times. (2018). A Billion-Dollar Investment in New York’s Water. By Winnie Hu.
New York Times, 18 January 2018. www.nytimes.com/2018/01/18/nyregion/new-york-
city-water-filtration.html
Nguyen, H. Q., Korbee, D., Ho, H. L., Weger, J., Thanh Hoa, P. T., Thanh Duyen, N. T.,
Manh Hong Luan, P. D., Luu, T. T., Phuong Thao, D. H., Thu Trang, N. T., Hermans,
L., Evers, J., Wyatt, A., Chau Nguyen, X. Q. & Phi, H. L. (2019). Farmer Adoptability for
Livelihood Transformations in the Mekong Delta: A Case in Ben Tre Province. Journal
of Environmental Planning and Management, 62(9), 1603-1618.
North, D.C. (1994). Economic Performance Through Time. The American Economic
Review, 84(3), 359–368.
Ostrom, E. (2005). Understanding Institutional Diversity. Princeton: Princeton University
Press.
Overseas Development Institute (ODI). (2010). The Alignment, Interest and Influence
Matrix (AIIM) Guidance Note. Prepared by Enrique Mendizabal. Overseas
Development Institute (ODI).
Phi, H. L., Hermans, L. M., Douven, W. J. A. M., Van Halsema, G. E. & Khan, M. F.
(2015). A Framework to Assess Plan Implementation Maturity with an Application to
Flood Management in Vietnam. Water International, 40(7): 984-1003.
Quan, N. H., Patino Guerro, J. D., Korbee, D., Luan, P. D. M. H., Dung, T. D., Hung, D. Q,
Loc, H. H. & Hermans, L. (2019). Manual for Application of the MOTA Framework.
Centre of Water Management and Climate Change (WACC) Vietnam National
University, Delft University of Technology and IHE Delft. https://strategic-delta-
planning.un-ihe.org/sites/strategic-delta-planning.un-ihe.org/files/quan_mota_
manual_-_version_1.pdf.
Rhodes, R. A. W. & Marsh, D. (1992). Policy Networks in British Government. Oxford:
Oxford University Press.
106

srotcA
4 aCTor analysIs
Roe, E. (1994). Narrative Policy Analysis: Theory and Practice. Durham: Duke University
Press.
Saaty, T. L. (1990). How to Make a Decision: The Analytic Hierarchy Process. European
Journal of Operational Research, 48, 9-26.
Sabatier, P. A. (1988). An Advocacy Coalition Framework of Policy Change and the Role of
Policy-Oriented Learning Therein. Policy Sciences, 21, 129-168.
Scharpf, F. W. (1997). Games Real Actor Play. Actor-centered Institutionalism in Policy
Research. Boulder, CO: Westview Press.
Scholes, K. (1998). Stakeholder Mapping: A Practical Tool for Managers. In V. Ambrosini,
G. Johnson & K. Scholes (Eds.), Exploring Techniques of Analysis and Evaluation in
Strategic Management (pp. 152-168). Essex: Prentice Hall/Financial Times.
Scott, J. (1991). Social Network Analysis: A Handbook. London: Sage.
Stokman, F. N. (1994). Besluitvormingsmodellen binnen beleidsnetwerken (Decision
making models in policy networks, in Dutch). In Huberts, L. W. J. C. & Kleinnijenhuis,
J. (Eds.), Methoden van Invloedsanalyse. Amsterdam: Boom uitgevers.
Thomson, R., Stokman, F. & Torenvliet, R. (2003). Models of Collective Decision-Making:
Introduction. Rationality and Society, 15(1), 5-14.
Timmermans, J. S. (2004). Purposive Interaction in Multi-Actor Decision Making. The
Netherlands: Eburon, Delft.
Toulmin, S. E. (1958). The Uses of Argument. Cambridge: Cambridge University Press.
van Eeten, M. J. G. (2006). Narrative Policy Analysis. In F. Fischer, G. J. Miller &
M. S. Sidney (Eds.), Handbook of Public Policy Analysis: Theory, Methods, and Politics
(pp. 251-269). Boca Raton: Taylor & Francis CRC Press.
Wasserman, S. & Faust, K. (1994). Social Network Analysis: Methods and Applications.
Cambridge: Cambridge University Press.
107

serutuF
5 Exploring the Future
The quotes, derived from a website about
‘Prediction is very difficult, forecasting,1 illustrate the key dilemma of
particularly if it is about the future.’ exploring the future: ‘we can’t know the future’.
Nils Bohr It is not possible to predict the future accurately,
but at the same time exploration of the future is
‘My interest is about the future, extremely relevant because most of our actions
because I am going to spend the are aimed at what lies ahead. The second quote
rest of my life there.’ indicates why exploring the future is relevant.
C.F. Kettering As we and next generations will be living this
future, it is interesting and necessary to contin-
‘If you have to forecast, forecast uously think about what lies ahead as indicated
often.’ by the third quote. One of the most urgent dem-
E.R. Fiedler onstrations of the above are of course the IPCC
Climate Change Scenarios, which are updated
continuously. Moreover, the need for change to
happen to save the world for future generations could not have been expressed more
urgently than by the then sixteen-year-old climate activist Greta Thunberg with her ‘How
dare you’ speech at the U.N.’s Climate Action Summit in New York City in September 2019.
Starting from various analytic methods for exploring our uncertain future, this chapter
gives you the basic tools to start building scenarios.
5.1 Introduction
In the context of policy analysis, we deal with expectations and explorations of the future as
opposed to predictions. Predictions are attempts to make absolute statements about the
future, while expectations and explorations are judgements about plausible future devel-
opments. When it comes to the problem analysis, we mostly speak about explorations of
the future as a way of dealing with uncertainties. It is the objective of exploration of the
future not to predict the future, but to explore plausible futures, so analysts and problem
owners become aware of the uncertainties of and around their policy problem. This explo-
ration can relate to the development of the nature and seriousness of the problem, the
effects of possible solutions in the future, as well as to the possible futures and environ-
ments of the problem.
Meijer and Korving (2001) cover these different uncertainties succinctly in their research
of maintenance and improvement of sewer systems. They sketch different types of uncer-
tainty: uncertainty about the behaviour and volumes of existing sewer systems and sewer
1 For the hobbyists: https://blogs.cranfield.ac.uk/cbp/forecasting-prediction-is-very-difficult-especially-
if-its-about-the-future/; https://www.brainyquote.com/quotes/charles_kettering_163122 ; https://www.
brainyquote.com/quotes/edgar_fiedler_130302 (all visited June 2022).
109

Futures
Policy AnAlysis of Multi-Actor systeMs
drains, and uncertainty about the future situation: rainfall volumes, size of the catchment
area, volumes of effluent as well as changing environmental norms. The first category
of uncertainties (behaviour and volumes) can be addressed through extensive measure-
ments, modelling and simulation studies. The second category of uncertainties in the
wider context of the sewer system can be studied by using other (climate) models and
more qualitative scenarios. But all these models and research will not remove all uncer-
tainty because uncertainties will continue to arise in the future. Figure 5.1 depicting the
so-called uncertainty trumpet (Rosenhead, 1989) illustrates this phenomenon.
Range of
possible
futures
Extent of the
uncertainty
Present Future
Figure 5.1 The Trumpet of Uncertainty, inspired by Rosenhead (1989)
Considering the relevance of exploring the future to problem-solving, it is not surpris-
ing that a whole spectrum of approaches is available for exploring the future. Short-term
and long-term uncertainties differ strongly in character and therefore ask for different
approaches. In this chapter, we limit ourselves to exploring the middle and long term and
start with a brief discussion of two classes of methods, namely formal methods (often
based on models) and expert methods. Thereafter, we discuss the design and use of sce-
narios for policy analysis. Different classifications of scenario methods are presented, a
process for developing context scenarios is introduced and an illustration of this process
is given.
5.2 Analysing and Classifying Uncertainties
The notion of uncertainty has taken different meanings and emphases in various fields,
including the physical sciences, engineering, statistics, economics, finance, insurance,
philosophy and psychology. Broadly speaking, uncertainty means limited knowledge
about future, past or current events. With respect to policy-making, the extent of uncer-
tainty clearly involves subjectivity, since it is related to the satisfaction with existing knowl-
edge, which is coloured by the underlying values and perspectives of the policy-maker
(and the various actors involved in the policy-making process).
110

serutuF
5 exPlorIng The fuTure
One thing to emphasize is that uncertainty is not simply the absence of knowledge.
Uncertainty is a situation of inadequate information, which can be of three sorts: inex-
actness, unreliability and bordering on ignorance (Funtowicz & Ravetz, 1990). However,
uncertainty can arise also easily in situations in which ample information is available (van
Asselt & Rotmans, 2002). For example, despite thirty years of research into the extent of
future climate change, the estimated range of possible future global mean temperatures
has only increased. Furthermore, new information can either decrease or increase uncer-
tainty. New knowledge on complex processes may reveal the presence of uncertainties
that were previously unknown or were understated. In this way, more knowledge illumi-
nates that our understanding is more limited or that the processes are more complex than
previously thought (van der Sluijs, 1997).
Uncertainty as inadequacy of knowledge has a very long history, dating back to philo-
sophical questions debated among the ancient Greeks about the certainty of knowledge
and perhaps even further. Its modern history begins around 1921, when Knight made a
distinction between risk and uncertainty (Knight, 1921). According to Knight, risk denotes
the calculable and thus controllable part of all that is unknowable. The remainder is the
uncertain, incalculable and uncontrollable. Since Knight, a wide variety or researchers
have adopted, adapted or extended this distinction between risk and uncertainty.
More recently, Walker et al. (2003) suggested understanding uncertainty as a multidi-
mensional concept. They distinguish three dimensions: level, location and nature. The
‘level’ of uncertainty has to do with the severity of the uncertainty and extends the dis-
tinction made by Knight. The level of uncertainty ranges from complete certainty to total
ignorance and Walker et al. (2003) distinguish between the levels of statistical uncertainty,
scenario uncertainty and recognized ignorance. Statistical uncertainty we know best from
the natural sciences; it is about measurement uncertainty, inaccuracy, sampling errors
and probabilities in stochastic models. Scenario uncertainty deals with the external envi-
ronment beyond the system that is studied, as scenarios do not forecast or predict the
future but indicate what might happen. Recognized ignorance is uncertainty about the
system and mechanisms being studied; we know that we do not know how the system
works. The ‘location’ dimension is used to specify what the uncertainty is about. Often
case-specific operationalizations of the location dimension are used because of this. For
example, the system diagram (see Chapter 3) can be used to specify whether one is uncer-
tain about external factors, relationships within the system, the outcomes or their relative
importance, or factors within or outside the control of the decision-maker. Finally, the
‘nature’ dimension is a bit more philosophical and has to do with whether the uncertainty
is intrinsic to the world itself or due to imperfections in our knowledge of the world.
Uncertainty intrinsic in the world includes for example the uncertainty about the toss of a
coin or the roll of a die. Uncertainty due to imperfections in our knowledge can arise either
due to not knowing enough or due to conflicting information and knowledge.
This multidimensional understanding of uncertainty has proven to be very fruitful. It for
example underpins the guidance for dealing with uncertainty used by the Dutch National
Institute for Public Health and the Environment (RIVM) when discussing COVID-19 infec-
tion-spreading models or the Netherlands Meteorological Institute (KNMI) when making
climate models. For more detailed discussions, see for example Kwakkel et al. (2010),
Walker et al. (2013) or Marchau et al. (2019).
111

Futures
Policy AnAlysis of Multi-Actor systeMs
5.3 Overview of Methods for Exploring the Future
There are many ways to structure the field of futures studies. For reasons of simplicity, we
will distinguish formal methods, expert consultation and scenario studies. The latter will
be treated to a larger extent as we find them fit better when analysing complex problems.
The final section will be on studies ‘beyond scenarios’ and showcasing more recent devel-
opments like exploratory modelling and adaptive policy pathways.
5.3.1 Formal Methods
Formal methods are methods where a formal, verifiable and, in many cases, a mathemati-
cal approach is used. Formal methods presume an often causal relation between two or
more factors of social, economic or technical nature. Most formal methods for exploring
the future are based on some form of extrapolation: past trends, based on time series
or theories about underlying mechanisms, are identified and extrapolated. Although this
approach faces many potential pitfalls (we know that the future will bring changes, just
not which ones), it is often one of the least bad alternatives (we often do not know enough
about future changes to be able to make some sensible statements about them). The
simplest approach is to presume that the near future will be like the present: ‘Tomorrow’s
weather will probably resemble today’s’. However, if we have insight into certain trends or
mechanisms behind changes, it is wise to also base the extrapolation on these insights.
This means building a model, assuming that the mechanisms that are part of the model
will also be valid in the future.
The models can be very diverse in nature depending on the existing insights into, and
knowledge, and theories of the phenomenon of interest and the objectives of the explo-
ration. Take for example weather and climate forecasting. Very complex atmospheric
models are used for daily weather forecasting. But when dealing with long-term expecta-
tions (such as forecasts for temperature and sunshine on 21 July in ten years’ time), those
complex models are pointless, and a simpler approach can be used: the long-standing
statistical average. This expectation is based on the ‘model’ of the yearly season cycle,
and the – questionable – presumption that no large climate changes will occur within this
time frame. Climate changes forecasts over an even longer term (e.g. 50 or 100 years);
others again use sophisticated mathematical models to explore possible climate changes
because of, for instance, global warming. However, these models are not used to describe
the weather at a particular location on a particular point in time, but rather to understand
the aggregate patterns at country or even larger scales.
We will limit ourselves here to several methods that are relevant in policy analysis, of
which you need to know the principles, their uses and their limitations. In policy analysis,
these methods are mostly used for investigating social developments, and environmen-
tal and technological changes, for gaining insight into how the severity of the problem
might change or how possible policies might play out. In short, it is about exploring the
gap between the present and desired situation or about the gap between the desired and
expected future situation. We discuss four classes of formal methods. With an increasing
complexity of the underlying assumptions, these are:
– trend extrapolation and regression analysis;
– analogies;
– causal modelling;
– trend impact assessment (TIA).
112

serutuF
5 exPlorIng The fuTure
Trend Extrapolation
The basic concept of trend extrapolation is simple: past trends, based on time series or
theories about underlying mechanisms, are identified and extrapolated. In mathematical
terms, a relationship between independent variables (X, X … X ) and the dependent vari-
1 2 n
able (Y) is developed:
Y = f(X, X … X )
1 2 n
This correlates well with past performance. This formula is then extrapolated to obtain a
figure for the year under examination. The result should be realistic, based on the latest
available data, reflect the current conditions of the system concerned, supported by other
information in the study, and provide an adequate justification for further analyses.
How is a trend extrapolation done? The first step is to identify the dependent variables
(the Ys) that are to be estimated through extrapolation. The next step is to gather and
analyse the data on the related independent variables (the Xs), which are assumed to
influence the variables of interest. The data should be analysed to see whether they are
appropriate and not ‘contaminated’ by unique events. For example, when estimating the
potential future traffic at an airport, major sport events like the Olympics, which create a
temporary boost to air traffic, contaminate the data.
The third step is to select a method for extrapolation. Potential methods include regres-
sion and trend analysis and share analysis. Share analysis is a straightforward method
where a higher level trend extrapolation is translated, based on historical data, into an
extrapolation for a smaller area. Regression analysis is more complicated, but the basic
concept is that the variables of interest are estimated based on other variables that explain
the estimated value. Historical data are used to develop a ‘best fit’ formula. Trend analysis
relies on projecting historic trends into the future; it is a type of regression analysis with
time being the independent variable.
After applying the selected trend extrapolation method, the results must be evaluated.
Evaluating the results is essential. The outcomes should be reasonable, and unexpected
outcomes should be justified and explained. For example, in regression analysis, the signs
of the coefficients in the equation should make logical sense.
The last step in forecasting is to summarize and document the results. The report
should explain the trend extrapolation method used, highlight the relevant assumptions,
present the outcomes of the trend extrapolation, and evaluate both the outcomes of the
extrapolation and the extrapolation process.
Trend extrapolation is commonly used, especially for making a reasonable case for
the expected occurrence of shortages or overspills in the future. An example of a trend
extrapolation can be found in Figure 5.2, which illustrates how the Food and Agriculture
Organization (FAO) of the United Nations uses extrapolation to illustrate the expected
development in the world’s feed use of cereals and oilcakes. The graph nicely shows the
historical data till 2007 and their extrapolation into the future, suggesting that the growth
in use of cereals can be expected to be steeper than the one in oilcakes. Trend extrapola-
tion is based on the idea of identifying trends and underlying mechanisms, based on the
past and the present, and extrapolating them forward. However, it might be that the phe-
nomenon to be extrapolated has recently undergone changes or is expected to undergo
changes soon (e.g. trend breaks). In such situations, it is unwise to simply extrapolate
113

Futures
Policy AnAlysis of Multi-Actor systeMs
based on past trends and known underlying mechanisms. In such cases, Trend Impact
Assessment (generally known as TIA), which is discussed later, might provide a way out.
Figure 5.2 World feed use of cereals and oilcakes (million tonnes) (Source: Nikos
Alexandratos and Jelle Bruinsma, World Agriculture Towards 2030/2050
The 2012 Revision. ESA Working Paper No. 12-03 June 2012 Agricultural
Development Economics Division Food and Agriculture Organization of the
United Nations www.fao.org/economic/esa)
More elaborate descriptions and examples of these methods can be found in, among
others, Porter et al. (1991), Bell (1997), van Daalen et al. (1999), and Guess and Farnham
(2000).
Extrapolation with the Help of Analogies
Analogies are deeply rooted in our culture and language. For example, horsepower is still
used to describe engine power. A car model introduced in 1948 at the Parisian car-salon,
and still popular today, got its name from this: the deux chevaux. The use of analogies
is strongly interwoven with our ability to reason and is a consciously or unconsciously
applied learning strategy. Examples and experiences from other fields help us to find a way
to understand new challenges and/or to come up with solutions.
Extrapolation with the help of analogies is based on the assumption that a development
in the future will run analogically to a development in the past – and that similar mechan-
isms will occur. Analogies presume that the world is less simple than often assumed in
linear trend extrapolations. Analogies try to make a statement about the structure behind
the changes. A distinction can be made between historical and growth analogies. Histori-
cal analogies presume that historical processes run analogically. An example is the way
of thinking about the rise and fall of the contemporary world powers, such as the former
Soviet Union and now the United States, by comparing them with, for example, the decline
and fall of the Roman Empire, or the collapse of British Empire. Growth analogies make an
analogy between, for example, the development of technologies with biological and other
114

serutuF
5 exPlorIng The fuTure
processes (evolutionary, quasi-evolutionary processes). The analogy between the growth
patterns of biological systems and technological functions was formulated for the first
time by Ralph Lenz in 1962 (Lenz, 1962). He used the so-called ‘Pearl’s growth law’. Pearl
based his law on his observations of the growth speed of yeast cells and the weight gain
of pumpkins and other biological processes. These Pearl growth curves are also known as
the S-curve and are often used in economics, as substitution curves (life cycle of subse-
quent products), to deduce learning curves (Marchetti, 1980) and to describe the course
of innovation processes.
More specifically, in economics the Gompertz curve, a variant of the Pearl curve, is
often applied to explain increases in product sales. In the literature, you can find different
mathematical expressions for the Gompertz law. Examples are:
ln y = p + qrtor:
t
t
y = ep+qr
t
with 0 < r < 1 and q < 0, where ln y is the natural logarithm of the variable that needs to
t
be explained, t is the value of the time variable and p, q and r are the constants that need
to be determined. The limit value L of the variable that needs to be explained is given in:
L = ep. Just as in the biological growth analogy, the increase is a function of the achieved
state and of the difference between the limit and the achieved state, because:
dy
t = – y ln|r|(ln L – ln y)
dt t t
In Figure 5.3, the result of the formula above is exhibited for p = 3, q = −3 and r = 1/4.
Limit: L
20
y
t 15
p=3
10 q=-3
r=1/4
5 t
y=ep+qr
t
0
1 2 3 4
Time: t
Figure 5.3 Graphic representation of a Gompertz curve
A modern and frequently used analogy is the quasi-evolutionary theory of technology
development, where processes of variation and selection occur in the ‘wild’ nature, analo-
gous to the evolution of species. Here a technology is placed in a selection environment,
where it looks for a niche to develop further. Analogies can also be used in the context of
115

Policy AnAlysis of Multi-Actor systeMs
trend extrapolation. The structure of the function is then derived from an analogy. There
are, however, dangers with such an approach. For example, there are the pitfalls of false
causality and false analogy. In addition, why would we assume that processes that in the
past appeared to be analogous will continue to be analogous in the future? These kinds
of deductions have no verifiable value, especially according to philosopher of science Karl
Popper. On the contrary! Let this be a warning. There is no evidence to presume that the
apparent correlation between the intensity of solar radiation and the stock exchange will
continue in the future, or even that changes in solar radiation could be the cause of fluc-
tuations in the stock exchange (see Figure 5.4). That is why the Dutch Financial Authority
obligates product suppliers to mention in all their advertising that ‘results from the past
are by no means a guarantee for future results’.
|     | Calories per |     |     |     | New York |
| --- | ------------ | --- | --- | --- | -------- |
|     | sq. cm. per  |     |     |     | London   |
minute
180
650
New York stock prices
|     | -.012 |     |     |     | 176 |
| --- | ----- | --- | --- | --- | --- |
(Barron’s averages)
600
|     | -.010 |     |     |     | 172 |
| --- | ----- | --- | --- | --- | --- |
550
|     | -.008 | Solar radiation |     |     | 168 |
| --- | ----- | --------------- | --- | --- | --- |
500
|     | -.006 |     |     |     | 164 |
| --- | ----- | --- | --- | --- | --- |
450
|     | -.004 |     |     |     | 160 |
| --- | ----- | --- | --- | --- | --- |
400
| Futures | -.002 |     |     |     | 156 |
| ------- | ----- | --- | --- | --- | --- |
350
London stock prices
|     | Normal | (Banker’s Mag. Index) |     |     | 152 |
| --- | ------ | --------------------- | --- | --- | --- |
300
|     | +.002     |                    |                |                | 148 |
| --- | --------- | ------------------ | -------------- | -------------- | --- |
|     | Jan. Feb. | Mar. Apr. May June | July Aug.Sept. | Oct. Nov. Dec. |     |
Figure 5.4  New York stock prices and solar radiation (Source: Garcia-Mata &
Schaffner, 1934)
Analogy has a strong symbolic meaning, but it also has its limitations. Wise (1976), who
investigated the use of explorations of the future in the United States, reached the follow-
ing conclusions:
Analogies cannot prove relationships but they can suggest them ‘and’ some analogies have
proved prophetic.… Television as predicted followed a course of public acceptance analo-
gous of that of radio. And both electricity and electronics had social effects analogous to
that of the steam engine…. However, past predictions also indicate clearly two main defects
of analogy as a predictive technique. Frequently, the items chosen for comparison are inap-
propriate; and frequently analogy is carried too far.
116

serutuF
5 exPlorIng The fuTure
Even when areas seem to be similar, it can be dangerous to presume an analogy. An
example is the revolutionary change in warfare by the introduction of the atom bomb at
the end of the Second World War. After Hiroshima and Nagasaki, it was clear that this
was a category of weaponry that was not suited for operational use on the battlefield. It
took almost ten years, however, before the American Air Force (USAF) also reached the
conclusion that the character of strategic warfare had changed fundamentally and that
atom bombs were not the same as conventional bombs. Until Eisenhower came forward
with his ‘New Look’ doctrine in 1953, the USAF stuck to the massive use of heavy bombers
for ‘carpet bombing’, as their leading strategic concept and many air force generals viewed
nuclear weapons as ‘just another bomb’ (Enserink, 1993).
Yet the use of analogies is still popular, mainly when it comes to technological innova-
tion and introducing new products onto markets. Here, the aforementioned S-shaped
introduction/acceptance curve is often used, where the curve is adapted to the inherent
nature of the product or market that is being explored. Marketing lifespans play an impor-
tant role here. For many technologies, a lifespan of five to ten years is characteristic from
the basic prototype to complete market penetration. However, this lifespan can be twenty
to twenty-five years from the time the first idea originated to and widespread social appli-
cation, particularly in the case of so-called ‘large technological systems’. An example of a
product type with a high rate of circulation is the computer chip. Every two to four years,
a new generation penetrates the market. In contrast, the development of a new type of
airplane takes easily ten years and market penetration even longer. There are many exam-
ples varying from large-scale public traffic and energy supply systems to technologically
complex systems such as bombers or high speed trains, with extremely long lifespans of
twenty-five years or more.
Causal Maps
Technology forecasting is usually based on the simple extrapolation of historical develop-
ments based on a presumed (often simple) connection with historical data. In the United
States, technology forecasting started in the 1950s and 1960s to develop policies regard-
ing strategic technologies. In retrospect, the approach seems rather primitive because the
uncritical extrapolation of trends leads to serious misconceptions. The technological lead
of the Soviet Union in missile technology combined with extrapolated numbers about the
composition of the Soviet weapon arsenal caused in the United States to the so-called
defence panics: the ‘bomber gap’ and the ‘missile gap’. This panic in turn caused gigantic
financial injection in the American defence industry, which in turn became a driving force
for the arms race in the following decennia (Enserink, 1993).
More advanced statistical models are open to the same criticism. They implicitly assume
that all relevant information about future developments is present in historical data, and
with that they ignore insights and knowledge about factors that can have an important
influence on the variable that needs to be explored (e.g. changes in average household
size that influence the use of drinking water per household), but that are overlooked
because no data are available, or data are not included.
In general, development is a complex process, where social, economic, political, techni-
cal and normative factors play a role. Objections to trend extrapolation can be countered
to an extent by using causal maps (instead of statistical models or simple analogies),
where available insights into the causal mechanisms behind changes are included. Since
the end of the 1960s, computer technology has offered more and more opportunities
117

Futures
Policy AnAlysis of Multi-Actor systeMs
to build and analyse complex non-linear mathematical models. Since then, we have wit-
nessed an increasing use of causal mathematical models to support the exploration of the
future. The type of models used depends on the objective, available knowledge and the
type of causal mechanisms that are presumed to be crucial. For this, we refer to related
literature. Suffice it here to mention some examples typical of causal modelling used to
support the exploration of the future.
A first example is the development of long-term ‘global models’ at the beginning of
the 1970s, inspired by the ‘Club of Rome’. By using the ‘System Dynamics’ modelling
approach, under development back then, the causal connections between economic
growth, population growth, food production, exhaustion of natural resources, and harm
to the environment were described in a complex simulation model and extrapolated far
into the future (until 2100). This led to projections that warned about exhaustion of natu-
ral resources, harm to the environment, and famine because of unrestrained economic
and population growth. The results received a lot of attention in the media and were used
mainly by environmental pressure groups. When it became clear that the model was not
predicting accurately, heated discussions about the degree of reality of the underlying
model erupted. After this, more long-term models were built, often more detailed and
aimed at one specific aspect. For example, in the last decennia, large investments were
made in the development of long-term climate models that serve as a base for the explo-
ration of possible climate changes because of greenhouse gas emissions.2 These models
are extremely complex simulation models that consist of many thousands of equations. A
second example, in a completely different area, is the Netherlands Bureau for Economic
Policy Analysis (in Dutch CPB). They make extensive use of mathematical models to sup-
port the economic exploration of the future. Almost every area has its own interpretation
of the use of mathematical models for the exploration of the future. In general, these kinds
of long-term explorations of the future are very vulnerable to criticism. For example, an
evaluation of experiences with global modelling using System Dynamics was given the
title ‘Groping in the Dark’ (Meadows et al., 1982).
Causal mathematical models have the advantage that a wide range of knowledge can
be included. However, there are also significant disadvantages: the mistaken impression
of preciseness and reliability (the results are quantitative, and computers do not make
mistakes). Furthermore, a crucial implicit assumption in these models is that the mechan-
isms that have been dominant in the past will also be dominant in the future. Moreover,
mathematical models can quickly become so complicated, opaque and incomprehensible
that it becomes hard even for experts to make statements about their reliability.
Trend Impact Assessment
An important point of criticism on the foregoing methods is the assumption of continu-
ity. TIA (sometimes also called cross-impact assessment) builds on the above-mentioned
methods. However, the explicit point of departure is that future happenings (such as pol-
icy changes, but also technological breakthroughs or changes in social norms and values)
could lead to trend breaks. TIA tries to estimate:
– which factors or sudden events could lead to changes;
– what the probability is of these kinds of factors or events;
– how large their impact could be on the central outcomes of interest.
2 See also IPCC Working Group I Fourth Assessment Report ‘The Physical Science Base’ (2007).
118

serutuF
5 exPlorIng The fuTure
TIA combines predictable extrapolation with judgements about the probability and the
possible effects of trend-breaking events. Identifying these plausible and influential events
is usually done using literature studies, and brainstorming, or a Delphi setting (see Sec-
tion 5.3.2).
For instance, in the example below, the authors of the Millennium Project report 2008
State of the Future use trend impact analysis to sketch how the State of the Future Index
(SOFI) may develop over the coming years (see Figure 5.5). SOFI is a measure of the ten-
year outlook for the future based on the previous twenty years of historical data. SOFI is
based on a set of twenty-nine variables that was identified by an international panel of
experts. The global SOFI indicates that the future over the next ten years keeps improving
although not as rapidly as it did over the past twenty years. The alternative projections
are based on the potential occurrences of events, such as ethnic wars, diseases, changing
energy demands, democratic and women’s rights and other events that can alter trends.
1.20
1.10
1.00
0.90
0.80
0.70
0.60
1980 1985 1990 1995 2000 2005 2010 2015 2020
Base UQ Med LQ
Figure 5.5 SOFI 2007 with alternative projections by trend impact analysis
(Source: Glenn et al. 2008. See: https://www.researchgate.net/
publication/265071438_Futures_Review_Looking_at_Previous_Global_
Futures/figures?lo=1)
In TIA, the analyst is forced to think about plausible important events in the future, which
obligates the analyst to make the assumptions explicit. A discussion with policy-makers
can then take place at a more detailed level. TIA provides a range of possible results
instead of one single result, which makes it possible to take future uncertainties explicitly
into account. TIA can be used for a quantitative support of scenarios; we return to this
later in this chapter.
5.3.2 Consulting Experts
Formal methods are based on fixed data and they use approaches that are seen as objec-
tive. This perceived objectivity, however, is, limited because personal judgement of the
model builders plays a major role and different experts produce different models and
119

Futures
Policy AnAlysis of Multi-Actor systeMs
results. That is why direct consultation with experts is often used as an alternative way
to gather information about possible future developments. The knowledge and insights
of experts can be collected in different ways, depending on the objective and the means
(time and money) of the researcher. The first question that needs to be asked is which
experts need to be consulted and subsequently what the most suitable research method
is considering its objectives and essential preconditions. Frequently used methods are
interviews, questionnaires, meetings, nominal group technique, the Delphi method and
workshops. All of these may be supported by computer processing for analysis. This sec-
tion deals with the choice of experts and the method of questioning that needs to be fol-
lowed. The Delphi method, which is specifically developed to support explorations of the
future, is explained in detail.
Selection of Experts
To make strategic decisions aimed at the future, it is crucial to gather information about
the existing condition of a system and about plausible future developments of the system
and its environment. Therefore, fundamentally different kinds of knowledge and expertise
are necessary to be able to take an informed decision. Schnaars (1989) labels these two
kinds of expertise as fact and opinion. It is about knowledge of the actual situation on the
one hand, and informed ideas about plausible developments on the other hand. Although
bias may exist in collecting knowledge about the existing situation, this effect can be par-
tially compensated by cross-checking of opinions (although in group situations the danger
of groupthink remains). When formulating ideas about the future, diverging opinions are
inevitable and consensus is actually not desirable! Selecting the right experts is of crucial
importance to the task at hand. A suitable expert is someone who:
– has substantial knowledge of a certain field;
– is not afraid to deal with the uncertainty and to explore the boundaries of his or her
area of expertise;
– has the power of imagination.
Relevant here is the table with criteria for self-evaluation for experts, where Lipinski and
Loveridge (1982) indicate how someone can assess for himself whether he is an expert
or just an informed layman.3 This can also be a useful lead for the analyst who needs
to select the experts. Porter (1991), for example, uses this classification within his own
comparative research of technological development and the innovative ability of countries
to be able to weigh the judgements of the experts in his international panels. Table 5.1 is
based on Lipinski and Loveridge (1982).
Table 5.1 Criteria of self-evaluation: manual for self-judgement of expertise
1. Unfamiliar You are not familiar with the subject when mentioning it does not recall any memories or it
does not give lead to saying something sensible about it.
2. Accidentally You are accidentally familiar with the subject when you know what it is about, you have read
familiar something about it or you heard or saw something about it on the radio or television.
3 See also Porter et al. (1991).
120

serutuF
5 exPlorIng The fuTure
3. Familiar You are familiar with the subject when you know most arguments pro and contra the most
controversial elements of the subject, when you have read a lot about it and when you have
formed an opinion. However, were someone to attack your opinion, you would have to
quickly admit that you do not know enough.
4. Former expert You used to be an expert on the subject some time ago, but your knowledge is somewhat
outdated because other activities came up. But you are still reasonably well informed about
recent developments, which provides you with a broad overview of the subject as opposed
to deep detailed knowledge.
5. Expert You should consider yourself as an expert when you belong to the small community of
people who, at this moment, study, work on and are dedicated to this subject. You typically
know who else works on this subject, you know the domestic literature and probably also
the international literature about this subject; you go to conferences and seminars and
when possible you publicize about the subject. Other experts can differ in opinion about
this subject with you, but that does not make you nervous.
The choice of the technique for the consultation of experts depends on the objectives and
the means of the researcher. The following factors play a role in choosing the technique
(see Porter et al., 1991: 205):
– Logistics – the available time and finances determine to a large extent the possibilities.
Financial restrictions mean that only a few interviews, a single small workshop, or a
simple questionnaire without feedback to the respondents is possible.
– The degree to which feedback and interaction are desired. When regular exchanges of
thought with and between experts are desired, interactive methods can be considered.
If this is not so important, then a questionnaire or a series of interviews may suffice.
– The range of available expertise that is considered relevant. This influences the size
of the group. Usually, the starting point is groups of eight to twelve persons to have
sufficient breadth. Sometimes, however, it is desirable to involve a much larger group
of experts, for example because, besides the different aspects, there are cultural differ-
ences that also must be considered. Questionnaires or a Delphi-like approach will usu-
ally be used in these cases. It is important that the group of experts that is consulted
is representative for the spectrum of insights and approaches that are considered rel-
evant.
The Delphi Method
The Delphi method was named after the Greek town of Delphi. Greek generals used to go
there in ancient times to consult the local oracle. Depending on omens, decisions were
made about, for example, the undertaking of military campaigns. It is a classical form of
exploring the future that looked to the supernatural for support.
The so-called Delphi method was developed in the mid-1950s in the United States,
mostly by the employees of the RAND Corporation who used this method for defence
research. American military expertise was used for this method to investigate how Soviet
forces would use their strategic nuclear weapons against American industrial centres (and
subsequently of course how the Americans could prevent this kind of attack and/or limit
the damages as much as possible).
The Delphi method is a method of questioning based on the repeated and systematic
investigation of expert opinion about a certain topic. A team of researchers carries out
121

Futures
Policy AnAlysis of Multi-Actor systeMs
the surveys. The monitor group manages the process and summarizes and interprets the
results.4 The method works according to several steps (at least eight):
– Defining and clarifying the topic on which expert opinions is required. The question
needs to be meaningful for the problem-solving process and needs to be formulated
so clearly that the experts that are being consulted will interpret it in the same way.
This phase also sets the direction for the identification of experts.
– Identifying and selecting experts.
– Drafting and mailing of questions for the first round. In general, the questions in the
first round should be open because this leaves room for the experts to put forward
their own ideas and viewpoints. So, for instance, it should include questions about the
experts’ expectations of future contribution of nuclear fusion to the energy supply as
well as their underlying reasons for their statements.
– Answering and returning the first round of questionnaires by the participants.
– Analysing and summarizing the answers from the first round by the monitor group.
– Depending on the question or questions asked, this can be a list of the aspects men-
tioned, or an overview of expert statements (anonymous) by % of those who held the
opinions (e.g. 20% thinks that nuclear fusion will make an important contribution to
the energy supply within thirty years; 40% thinks within fifty years and 40% thinks it
will never happen). An overview of the arguments is also important.
– Drafting and sending questionnaires for the second round. In the second round, the
respondents receive a summary of the results from the first round together with a
request to react to these results. Often this will include a ranking of aspects or argu-
ments (which of the mentioned aspects or arguments do you think are most impor-
tant? And next? And next?). Participants may also be asked to adjust answers that were
given in the first round, or for additional information (for instance, do you adhere to
your statement about the contribution of nuclear fusion? If so, what do you think are
the crucial conditions that have to be met to realize your vision?).
– Answering and sending back the questionnaires from the second round by the partici-
pants.
– Analysis and aggregation of the answers from the second round.
– Drafting of a questionnaire for the third round. This can run analogically to the previ-
ous round, where, depending on the statements that have been made, the focus can
shift. For example, when after the second round the conclusion is that there is no
consensus about the chances of nuclear fusion in the long term, the third round could
focus on crucial conditions.
– Analysis and aggregation of answers from the third round, and either closing by mak-
ing final conclusions, or a continuation of the process with one or two more rounds.
The decision whether to continue or not is dependent on the degree of convergence
in opinions that has occurred, whether it is useful – in terms of the solution to the
problem – to ask additional questions, assessing whether the participants are still suf-
ficiently motivated to continue, and of the available means and time.
The Delphi approach has the advantage that a large (ranging from ten to more than a hun-
dred participants) and geographically diverse group of selected experts can be involved,
and that those experts can express their opinions anonymously. That way, the ideas are
4 See: Bell (1997: 261-263); Porter et al. (1991: 214-219).
122

serutuF
5 exPlorIng The fuTure
not linked to persons and can be judged on their merits independently from the status
of the expert concerned. Furthermore, opinions cannot easily be linked to people, which
enables that person to change his or her mind during the process without having to pub-
licly announce it. It also prevents dominant people from influencing others in the group
and thwarting groupthink.
Furthermore, the Delphi approach offers the possibility to include a large spectrum of
views and in the final report there is also room for minority viewpoints.
The disadvantages are the length of time it takes, the substantial investment in man-
power (monitor group) and the risk that personal preferences of the monitor group will
strongly influence everything. Also, in practice, it is often hard to keep the respondents
motivated during consecutive rounds. In the end, the quality of the respondents and the
nature of the questionnaires are crucial success factors. The internet has substantially
shortened the processing time. Questionnaires and answers can be easily exchanged
through e-mail. It seems that non-response has become the main problem.
Delphi is also successfully applied in technical administrative research, as in the inno-
vation research of Porter et al. (1991). Another example is the collecting of insights into
possible paths of implementation for automated vehicle control in road traffic (Marchau,
2000). An international group of 117 experts was identified and approached. In the first
round, sixty-five answers were received, in the second round fifty and in the third and final
round forty. In the consecutive rounds, useful statements were made about the opportu-
nities and impediments of automated vehicle control in road traffic. This led to a reduction
in the number of feasible types of implementation, an insight that is useful when setting
policy priorities. More recently, web-based applications have been introduced and applied
successfully (Brill, 2006). Web-based versions of Delphi allow for faster exchange of ideas
and opinions, real-time scoring updates, the involvement of large numbers of participants
and parallel sessions (Cole, 2013). Nowadays Delphi is widely used in nursing and medical
peer consultation and several online Delphi platforms are offering their services.
5.3.3 Scenarios
The term ‘scenario’ is derived from the movie and theatre world. There it is used to indi-
cate the ‘course of events’ or the ‘story in its context’. The term was introduced in policy
literature at the beginning of the 1950s by the mathematician and physicist Herman Kahn
who worked for RAND Corporation at the time. His task there, among other things, con-
cerned explorations of the future – which he called scenarios – involving the consequences
of possible nuclear exchanges with the Soviet Union. Kahn’s scenarios came about during
the Cold War and mostly had a ‘worst case’ character. In the political climate of that time,
they legitimized a policy that led to an unrestrained development of nuclear weaponry in
the United States.
At the end of the 1960s and the beginning of the 1970s, the term scenario was also used
in other areas. Known examples can be found in the reports to the Club of Rome, where
exhaustion of the world’s natural resources stock is sketched, and in the energy scenarios
that played a central role in the ‘Social Discussion Energy Policy’ in the Netherlands at the
beginning of the 1980s. In that discussion, scenarios were sketched in which, based on
policy choices, an important part of Dutch electricity would be generated through nuclear
energy, coal or reusable resources (sun, wind and water). Scenarios are also used in the
business sector. The most striking example of this is Shell. Thanks to the scenarios Shell
123

Futures
Policy AnAlysis of Multi-Actor systeMs
developed, the company was better prepared than the competition for the unexpected
changes in the oil market during the oil crisis that was precipitated by OPEC in the 1970s.
During the last decennia, working with scenarios has become very popular both in the
private and in the public sector. At the same time, the use of the term has widened consid-
erably. The term ‘scenario’ is so general that it can be used to indicate every form of explo-
ration of the future, including explorations that are based on extrapolations, regression
models or causal models. For example, in international climate research, they speak of
diverging climate scenarios that are the consequence of ‘high’ or ‘low’ emission scenarios.
The latter research relies heavily on (causal) mathematical models based on the extrapola-
tion of past developments. This produces a variety of possible images of the future but
does not constitute a lot of surprises. The term is also used in other disciplines, such as
safety science. There it involves the possible combinations of disrupting circumstances
that cause failures. The consequence is that we cannot speak of ‘the’ scenario approach.
Approaches vary widely, where the terms ‘scenario’ and ‘scenario approach’ are used in
different ways. This confusing situation justifies a closer look at the approach used when
it is referred to as ‘the’ or ‘a’ scenario approach.
Types and Functions of Scenarios
There are three dimensions that can distinguish types of scenarios.
Point in Time or Time Path
A scenario can comprise either a description of a possible future situation at a certain
point in time (in the last century the year 2000 was favourite, now scenarios run until 2030
or 2050), or a sketch of a time path of the present situation to a future one. The time path
is sketched in terms of events and decisions that lead up to the possible future situation.
Explorative or Normative
Scenarios can have an exploring or a normative character. Exploring scenarios sketch one or
more possible images of the future (or developments) without any statement being made
about the desirability of it. Exploring scenarios are therefore called explorative. Projective
scenarios are often used and are also a part of explorative scenarios, where developments
from the present and the past are extrapolated to the future and where the starting point
is an assumed continuity of social development. Examples of explorative scenarios are the
projections and long-term scenarios from the CPB.
Normative scenarios use a desired image instead. They offer a sketch of a future that
is considered ideal, for example a situation of peace and tolerance, or a situation where
the environmental impact is minimized. Normative (also called prospective) scenarios are
mostly used to design the path to the starting situation from the desired future situation,
with the objective to investigate which policy could lead to the desired situation. This is
often called ‘backcasting’ – the opposite of ‘forecasting’ (Vergragt & Quist, 2011). The
term ‘trend-break scenario’ is also used here to indicate that a future path is sketched
that radically breaks with current trends. The Dutch program Sustainable Technological
Development (DTO) offers a recent example of this kind of normative approach. Going
from the desire to reduce impact on the environment drastically, normative images of the
future have been drafted where the environmental burden was reduced by a factor 10 in
comparison with current environmental burden. Subsequently research was started to
find out how this desired image of the future could be achieved. Desired images are often
124

serutuF
5 exPlorIng The fuTure
set in opposition to undesired images or ‘doom’ scenarios and/or compared with the
future situation with an unchanged policy (the so-called reference scenario).
Context, Policy and Strategic Scenarios
Scenarios either can be about the context of the problem or about policies for problem-
solving or a combination of both. Policy scenarios describe possible developments of the
problem or system itself, where the problem owner or policy-maker can influence the
choices that give direction to the development. In policy scenarios, the context of the
policy is presumed to be constant. For instance, the different urbanization scenarios for
the Dutch Randstad (PBL, 2012) concentrate on the spatial spreading patterns that can be
influenced by the government and these scenarios assume that the context stays the same
in all cases (the same population growth, the same economic growth). The same is true
for the Chinese urbanization scenarios that foresee continued growth of its megacities
and the establishment of five super regions.
Contextual scenarios provide images of possible future environments of the policy or
system to be considered. They are mainly used to make statements about the robustness
of possible policies. These scenarios focus on the environment or context of the problem
that cannot be influenced by the policy-maker, but that can significantly influence the
results of a policy. In the above-mentioned example of the urbanization scenarios of the
Netherlands and China, such contextual factors are, for instance, economic development,
immigration and climate change.
Strategic scenarios deal with images of the whole, i.e. they combine policies and contex-
tual developments. Strategic scenarios are used to clarify strategic choices between kinds
of developments or policies by providing insight into the expected effects.
Well-known examples of strategic scenarios are the ‘Mont Fleur scenarios’ that were
developed in South Africa at the beginning of the 1990s and that played an important part
in the peaceful transition from apartheid to democracy. These scenarios sketch several
diverging transition pathways in South Africa in terms of how difficult it would be to influ-
ence political and social developments in the areas affected by the policy. It turned out
from exploring the Mont Fleur scenarios that most of the possible developments would
probably lead to sharpened social conflict situations with serious negative consequences.
Only cooperation between the different racial groups and adjustment of the revolution-
ary African National Congress goals (toning down) could keep the country from an eco-
nomic downfall. This development with the appealing name ‘flight of the flamingoes’ was
considered as the most desirable scenario (see Figure 5.6). The other scenarios called
Ostrich, Lame Duck and Icarus sketched futures with non-representative, incapacitated
and populistic governments respectively. Subsequently, it fulfilled the role of an image to
strive for and was used as a normative scenario. Thanks to this Mont Fleur scenario exer-
cise, outdated ideas such as nationalizing of all businesses were quickly discarded while
the pace of the proposed changes (a dwelling and electricity for everyone within five years)
was reduced (Jaworski, 1996).
125

Futures
PolICy analysIs of mulTI-aCTor sysTems
Isa no Non-representa�ve
Current se�lement government
nego�a�ons
nego�ated?
yes
Incapacitated
government
no
Isthe
transi�on
rapidand Macro-economic
decisive? yes populism
no
Arethe
government
policies
sustainable? yes Inclusivedemocracy
andgrowth
Figure 5.6 The logic of the Mont Fleur Scenarios (Source: Own work)
To summarize, a scenario approach is specifi ed by indicating whether it is about:
– an image of a future point in time or an image of a path of development to the future;
– a possible or desired development or situation;
– an image of the future of a policy and the system, of only the environment of the
system that is being looked at, or a combination of policy, environment and resulting
system development.
5.4 Developing Scenarios
In t his section we will look at building contextual scenarios, a scenario approach that is
specifi cally developed to off er scope to views of the future that diff er from existing trends
to be able to investigate the robustness of the proposed policy. This approach usually has
a qualitative nature, and leads to global, easy recognizable descriptions of images of the
future that have the objective to stimulate discussions and reactions. Interactive group
approaches are often used to stimulate idea forming about possible or desirable futures
(Enserink, 2000a, 2004; Enserink et al., 2000; Onencan et al., 2016). In general, the focus
is not so much on exploring the probable, but on exploring the plausible.
Within problem exploration, contextual scenarios are extremely useful to evaluate
whether the demarcation of the system and its environment are right and whether all rel-
evant factors have been included and classifi ed in the right way. A scenario exercise clari-
fi es the distinction between means (available to the policy-maker) and external variables
(cannot, or only to a limited extent, be infl uenced by the policy-maker), and how they infl u-
ence (via causal relations) the criteria. To design and write creative and eff ective s cenarios
is a specialism: to write a good, i.e. a credible and groundbreaking scenario is not only
a matter of knowledge and skills, but also the result of a creative process and in-depth
intellectual discussions. In practice, scenarios are mostly designed by interdisciplinary
teams who, during the design process, put forward their ideas and results several times
to a broad forum of other creative and critical experts and clients. This is done not only to
126

serutuF
5 exPlorIng The fuTure
safeguard quality but also to gain support to increase the effectiveness of the scenarios
as a policy instrument.
All explorations of the future, and therefore scenarios too, have the goal to contribute to
learning processes of policy forming and/or system design. Scenarios are an instrument
of analysis that can be used to challenge social actors to co-think and co-design images of
the future to enlarge the social support of the policy.
The sequence of steps is described in short in Table 5.2, and every step is briefly
explained.
Table 5.2 Sequence of steps for the design of contextual scenarios
Step 1 Determine the key question Formulate the question, problem definition or proposed policy.
Determine the factors or crucial Indicate which contextual factors determine success or failure of
Step 2 powers in the environment of the measures regarding a certain policy field.
policy field
Determine the driving forces or Indicate which forces cannot be influenced by own policy, but
Step 3
mega-trends behind these factors influence the already distinguished factors.
Arrange the factors and forces Select the most important and the most uncertain forces.
Step 4 according to importance and
uncertainty
Design the scenario logic Use the selected forces as axes for designing the scenario
Step 5
skeleton that spans the scenario space (scenario logic).
Detail the scenarios Elaborate on three or more scenarios and pay attention to all
Step 6
forces and factors.
Evaluate the key question How does the key question look in each scenario? How do you
Step 7 evaluate the effects of the alternatives in different scenarios? Is
the decision robust? Which vulnerable points exist?
Monitor the developments Are there developments that make adjustment of the policy
Step 8
necessary (in time)?
Step 1: This step may seem trivial, but it is essential because the choice of the problem or
decision has an essential influence on how things progress. Here it is important to make a
statement about the relevant time frame and about the objectives of the problem owners.
Step 2: Firstly, it is essential to distinguish the system and the environment in this step
(see Figure 5.7). The system comprises those factors and mechanisms that can be influ-
enced, directly or indirectly by the problem owners, and whose development is a subject
of interest for these owners. Contextual factors are variables that influence the develop-
ment of the system (and therefore the degree to which the problem owners achieve their
goals) but that cannot be influenced by the problem owners themselves.
127

Futures
Policy AnAlysis of Multi-Actor systeMs
Environmental/Contextual
Factors
Steering Design System Output Factors
factors
Figure 5.7 Framework for system demarcation
Contextual scenarios aim explicitly at the contextual factors. Actions that can be used
by the problem owners themselves are absolutely not a part of it. Identifying important
contextual factors needs to be based on insights into the working of the system. For a
company like Shell, these are factors that cannot be influenced by the company itself,
such as the oil price on the global market, the total demand for oil products, the strategic
behaviour of the oil-producing countries, the position and strategies of competing com-
panies, etc. The latter factors all can come from causal maps and/or end-means analyses,
but brainstorming is also a good instrument to generate factors.
Step 3: This step is about identifying the so-called driving forces that determine the
developments of the factors from the previous step. In the case of Shell, consider the
international economic development, the breakthrough of alternative technologies for
finding energy, geopolitical stability (Kuwait, Iraq, USA), and so on. Brainstorming, causal
maps and/or end-means analyses combined with logic reasoning can help to identify the
driving forces.
Step 4: A creative team will quickly be able to identify a wide spectrum of factors and
driving forces. These are not all equally relevant when viewed from the problem definition
as formulated in Step 1. Only the relevant factors need to be included. These are the fac-
tors/driving forces that
– have an uncertain development and
– that can have a significant influence on the ultimate policy objectives.
In the example about Shell, this means that the demographical development is eliminated
because it is reasonably predictable, and it does not have as large an influence as some
of the other factors.
Step 5: The driving forces that are left after Step 4 will form the axes for possible future
scenarios. Every combination of different assumptions about each of the driving forces
produces in principle a potential image of the future. The chosen axes together are called
the scenario logic because they make up the skeleton or space within which the possible
futures are located. Often three axes will be elaborated because of practical reasons (i.e.
clarity, intelligibility). A choice for four, five or more axes is also defendable, however, and
not uncommon.
Step 6: This step is the translation of the abstract concept to a concrete image of the
world, elaborated in the form of a story, graphically or otherwise. It is advisable to give
every scenario an easily recognizable, catchy name. It is also important to limit the elabo-
128

serutuF
5 exPlorIng The fuTure
ration to the main lines because too many details may be distracting. It is also useful to
write from the perspective of the future situation, looking back on how it originated from
the past: The national income has risen sharply, but the division of income has become more
skewed. A sharp division in society has occurred. Neoliberal values are generally accepted:
free competition, globalization, individual responsibility and less government interference.
Environmental measures have been perceived as significantly hindering competition and have
been withdrawn under pressure of the free market.
A well-known trap is the conscious or subconscious use of probabilities in the design of
scenarios, for instance by opting for an extremely positive, an extremely negative and an
‘intermediate’ scenario. There is a fair chance that the intermediate scenario is viewed as
the most probable and that a strategy is chosen that works best with this ‘most probable’
scenario. This conflicts, however, with the basic line of thought behind the approach (tak-
ing into account the plausible, not the probable).
Step 7: Once the contextual scenarios have been elaborated, application follows.
Scenarios can be used in several ways. Scenarios are most often used while estimating
the effectiveness of alternative policy options. For each policy option, the effects in each
scenario are estimated, providing insight into the strength of the alternatives. Assessing
effectiveness can be done by a multi-criteria analysis or by filling in a scorecard for each
of the contextual scenarios. Robust policy measures are those that work positively in vari-
ous futures. If a measure is not robust, adjustments are needed, or at least by following
a ‘hedging’ strategy damage will be limited or avoided. Strategy evaluations can also lead
to preparing measures in case a threatening future development becomes reality (think of
Shell). Furthermore, insights offer leads for monitoring the strategic environment. These
monitoring strategies will have to mainly focus on developments in those contextual fac-
tors that are harmful for the chosen strategy.
A second way in which scenarios can be used is for exploring how a problem could
develop if no action is taken. The development of a problem situation in the future is
important; a problem may get worse or even disappear when the context changes; this
would have severe implications for the relevance of specific problems and knowledge gaps
and consequently impact on policy and research agendas. If a problem persists in various
future scenarios, one could see it as a robust problem that needs attention; this finding
justifies spending time and money on the issues.
To assess how a problem might evolve in a given scenario, the impact of a scenario on
the outcomes of interest has to be identified. Analytically, a given scenario is specified by
the scores on the different axes that span the scenario space. Since each axis is related
to external forces, the scores of a scenario can be translated to scores on the different
external forces. Using these scores and a system diagram, an assessment of how the dif-
ferent outcomes of interest evolve can be made. By comparing the impact of a scenario on
the outcomes of interests with the goals, one can assess whether a problem disappears
(i.e. the gap between the outcomes and the goals becomes smaller), a problem becomes
worse (i.e. the gap between the outcomes and the goals becomes larger) or the problem
changes in character (i.e. new gaps between outcomes and goals emerge). Alternatively,
if the system contains feedback or a scenario has conflicting impacts on the system (i.e.
some external factors make the problem worse while others make the problem smaller),
the analyst cannot specify what the impact of the scenario will be on the problem without
further research. This implies that there is a knowledge gap about how the problem will
be affected by the different scenarios.
129

Futures
Policy AnAlysis of Multi-Actor systeMs
Within the problem analysis, the contextual scenarios can provide insight into the uncer-
tainties surrounding the problem and the possible development of the problem in the
future. The question that the analyst will ask himself at this moment is: are there any factors
or developments in the environment of the problem that influence the nature, severity and
demarcation of the problem and if so, in what direction? These insights can lead in practice
to a better demarcation of the system. New, contextual, factors can be added to the system
diagram while other factors will turn out to be redundant or less relevant. And by making the
relations between factors explicit, the distinction between means, external factors and criteria
will become clearer. This provides insight into the occurring knowledge gaps – for instance,
that we do not know exactly what the nature of the relation between factors is – and into the
nature and urgency of the researched problem situation. To be able to identify knowledge
gaps in this and previous steps of the analysis and to have a good problem demarcation are
things that help in the formulation and prioritizing of the research questions.
Step 8: Policies should be designed and implemented that anticipate possible events;
these policies should have the character of no-regret strategies or adaptive policy-making.
At the same time, critical contextual factors should be monitored to allow for timely adap-
tations of the policy. If changes occur in the critical contextual factors, this then can lead
to adjustments of the policy or to commencing with previously prepared measures. The
latter is what gave Shell a head start on the competition in the early 1970s when the oil
crisis occurred.
5.5 Example: Scenario Analysis for Examining Civil Aviation
Infrastructure Options in the Netherlands
In the last section, we elaborated on the process of developing context scenarios. In this
section, we will further elucidate the development of scenarios using an example. This
example is derived from an actual scenario study carried out in 1997 on behalf of the
Dutch government. The scenario study was part of a larger policy analytical study into
the future of civil aviation in the Netherlands known as the TNLI study. Context scenarios
were developed to assess the robustness of different policy options that the Dutch govern-
ment was considering.
5.5.1 Step 1: Determine Key Question
A basic assumption of the TNLI study was that the Netherlands would accommodate
future air transport demand. The focus was therefore on the different policy options avail-
able for accommodating future air transport demand. To assess the robustness of these
policy options with respect to the future, context scenarios were developed. The main
question these scenarios would have to answer was: What are different plausible futures
for civil aviation? The scope of the scenarios would be the future of civil aviation in the
Netherlands and developments that could affect this. Given the long lifespan of infra-
structure, a time horizon of thirty to forty years was chosen.
5.5.2 Step 2: Determine the Contextual Factors
In order to identify the contextual factors, experts and different stakeholders were inter-
viewed. The resulting list of factors was complemented by a literature study. After several
iterations, a list of twenty-six relevant contextual factors was identified (see Table 5.3).
130

serutuF
5 exPlorIng The fuTure
Table 5.3 Contextual factors
Airport capacity
Availability of land for building new airports or expanding existing airports
Continued existence of the EU
Economic parity between countries in Europe, Far East and North America
Flexibility of labour markets
French and German High Speed Train (HST) networks are linked to each other
Global macroeconomic environment
HST network in Italy and Spain
HST network linking Paris, Brussels, Cologne, Amsterdam and London
HST speeds of up to 300 km/hour
Impact of ICT technology on the demand for business travel
Impact of oil price on the demand for air travel
Incremental improvements in technology resulting in quieter, cleaner and more fuel-efficient engines
Location of economic growth in Europe
Microwave landing systems and GPS will be in use
Night curfew at most European airports
Number and type of airlines
Potential for breakthrough technologies
Potential for multilateral negotiation of air traffic agreements
Presence of government subsidies
Presence of Mega Jumbos (i.e. A380/747-800)
Presence of Unified European Air Traffic Management System
Profitability of the aviation industry
Size of industry in terms of passenger and cargo volumes
Trade volumes within and between regions
Willingness to pay for direct vs hub flights
5.5.3 Step 3: Cluster the Contextual Factors into Driving Forces
The next step was to cluster the twenty-six factors into driving forces. Table 5.4 shows an
overview of driving forces resulting from the clustering of factors identified under Step 2.
The driving force ‘economic environment’ contains factors that describe how the economy
in Europe and the rest of the world could develop. The economic environment will shape
the size and location of demand for air transport. The oil price was kept separate from the
economic environment, for the main uncertainty here is how the oil price would affect the
demand for air travel. The driving force ‘High Speed Trains’ contains factors relating to the
rise of a HST network in Europe. The development of HST in Europe can affect the demand
for air transport within Europe because people might choose to take the train instead.
Telematics focuses on the rise of ICT technology and the extent to which this might affect
the demand for business travel. The underlying idea was that the rise of ICT could enable
teleconferencing, thereby reducing the need for business travel. Land usage emphasizes
the availability of land around the existing airports and how this limits the possibilities for
adding infrastructure. The driving force ‘airspace’ focuses on how air traffic within Europe
is organized. During the mid-nineties, attempts were made to integrate the airspace of the
different European countries into a single system, managed by a single organization. During
the TNLI study it was uncertain how this would play out. Aircraft technology contains factors
131

Futures
Policy AnAlysis of Multi-Actor systeMs
that describe the different elements of an aircraft in terms of size and propulsion. Related
to airspace, during the mid-nineties the European Union tried to privatize and liberalize the
aviation industry in Europe. The driving force ‘structure of the aviation industry’ contains
factors related to this effort. The driving force ‘behaviour of passengers’ focuses on the type
of connection that passengers would prefer. Would they prefer a cheaper hub and spoke
network, or would they be willing to pay for direct flights? The final driving force contains
factors describing the health of the worldwide aviation industry.
Table 5.4 Driving forces
Economic environment
Global macroeconomic environment
Economic parity between countries in Europe, Far East and North America
Location of economic growth in Europe
Trade volumes within and between regions
Flexibility of labour markets
Fuel market
Impact of oil price on the demand for air travel
High Speed Trains
HST network linking Paris, Brussels, Cologne, Amsterdam and London
HST network in Italy and Spain
French and German HST networks are linked to each other
HST speeds of up to 300 km/hour
Telematics
Impact of ICT technology on the demand for business travel
Land usage developments
Availability of land for building new airports or expanding existing airports
Airspace management
Presence of Unified European Air Traffic Management System
Aircraft technology
Presence of Mega Jumbos (i.e. A380/747-800)
Incremental improvements in technology resulting is quieter, cleaner and more fuel-efficient engines
Potential for breakthrough technologies
Structure of the European Airline Industry, and the Netherlands’ role in it
Microwave Landing Systems and GPS will be in use
Night curfew at most European airports
Presence of government subsidies
Potential for multilateral negotiation of air traffic agreements
Airport capacity
Number and type of airlines
Continued existence of the EU
The preferences and behaviour of passengers
Willingness to pay for direct vs. hub flights
The health of the global civil aviation industry
Size of industry in terms of passenger and cargo volumes
Profitability of the aviation industry
132

serutuF
5 exPlorIng The fuTure
5.5.4 Step 4: Classify the Driving Forces According to Their Impact and Uncertainty
Table 5.5 shows the classification of the driving forces in terms of their uncertainty and
their relative impact on the system of interest. The driving forces HST, ‘land usage’ and
‘airspace’ all have little impact on the future of civil aviation in the Netherlands and are
of low uncertainty. HST has a low impact because of the planned integration of the Neth-
erlands into the European network. It is expected that HST can only compete on short
distances where demand for aviation is already low. Land usage also has a low impact
because the different airports in the Netherlands all have excess capacity and are not sig-
nificantly affected by the limits in available land. Finally, airspace integration in Europe will
have some effect but it will not drastically change the way in which the aviation system will
function. The uncertainty for all three is insignificant because of the long-term plans that
were already in the implementation phase.
The economic environment and oil prices can have a significant impact on the demand
for aviation. However, the economic rise and fall has proven to be relatively stable over
time. Similarly, oil prices are dependent on the economic situation reducing the extent of
uncertainty surrounding the long-term fluctuations in oil prices. By contrast, experts dif-
fer in opinion on how telematics will develop and uncertainty is thus high. However, the
experts and literature agreed that there would always be a need for business travel even
if advanced telematic technology were in use. The impact was therefore judged to be low.
The three remaining driving forces were all considered to be both uncertain and have a
high impact on the future of civil aviation in the Netherlands. The structure of the Euro-
pean airline industry and the regulatory regime under which the industry will operate will
shape the ownership structure of the Dutch airports and airlines. However, in 1997 it was
unclear whether all the member states of the EU would cooperate with the planned privati-
zation and liberalization. Passenger preferences will shape the basic structure of the avia-
tion network in Europe, in turn determining how the airports in the Netherlands would be
used. The final driving force, the health of the global civil aviation industry, was judged to
be important because it would determine which airlines and which airline manufacturers
would be in the market. Given the volatile history of aviation, with airlines and manufac-
turers going bankrupt, uncertainty was high.
Table 5.5 Classification of Driving Forces
Uncertainty
Low High
Impact Low High Speed Train Telematics
Land-use developments
Airspace management
High Economic environment Structure of the European Airline Industry
Fuel market The preferences and behaviour of pas-
sengers
The health of the global civil aviation
industry
5.5.5 Step 5: Design a Scenario Logic
From Table 5.5, we can deduce that the scenario logic will consist of the following driving
forces – structure of the European Airline Industry, preferences and behaviour of passen-
gers, and the health of the global civil aviation industry. For clarity, extreme states for each
133

Futures
Policy AnAlysis of Multi-Actor systeMs
dimension were specified. For the structure of the European Airline Industry, the extreme
states are a fully liberalized market and a state-owned and state-operated industry. For
the preferences and behaviour of passengers, the extreme states are a strong preference
for direct flights on the one extreme and a strong preference for indirect flights through
hubs on the other extreme. For the third dimension, the health of the global civil aviation
industry, the extreme states are on the one hand a profitable industry and on the other
hand an unprofitable industry. Together, all this is illustrated in Figure 5.8.
Liberalized market
Unprofitable
industry
Direct flights
Hub preferred
preferred
Profitable industry
State owned and
operated
Figure 5.8 Scenario logic
5.5.6 Step 6: Detail the Scenario
For the TNLI study, five scenarios were specified further. Given the aim of using the sce-
narios for assessing the robustness of policies, the factors for the different driving forces
were quantified. Here we will focus on a single scenario, Scenario 5. Table 5.6 shows the
specification of this scenario for each of the factors. Taken together, this scenario can be
characterized as a scenario in which passengers prefer direct flights, the aviation industry
has been privatized and liberalized, and worldwide the industry is in decline.
Table 5.6 Specification of scenario 5
Structure of the European Airline Industry and the Netherlands’ role in it
Microwave Landing Systems and GPS will be in use No
Night curfew at most European airports Yes
Presence of government subsidies No
Potential for multilateral negotiation of air traffic agreements Multilateral treaties
Airport capacity Three mega hubs, none in the Netherlands
Number and type of airlines Three mega airlines, none using the Nether-
lands as its base of operations
Continued existence of the EU Yes
134

serutuF
5 exPlorIng The fuTure
The preferences and behaviour of passengers
Willingness to pay for direct vs. hub flights Strong preference for direct flights
The health of the global civil aviation industry
Size of industry in terms of passenger and cargo volumes Industry is in decline
Profitability of the aviation industry Profitability is in decline
Text box 5.1 Specification of scenario: A possible scenario story
23 January 2031
In its annual report, the Schiphol Industrial Area and Aviation Group (SIAAG) reports it
generated over 200 new jobs in commercial services and nanoelectronics. SIAAG is largely
based on real estate management (Airport City) and the applied nanosciences companies it
started twenty years ago. Airport activities contributed 32% to SIAAG’s total production volume.
The latter percentage has been more or less stable since 2020, when former Amsterdam Airport
Schiphol hit an all-time low with a passenger volume of only eighteen million after losing its
status as a European hub. In that year, Air Europe, the world’s third largest airline, completed
the relocation of its European hub activities to Milan, leaving Paris and Amsterdam as regional
hubs. Remember that at the turn of the century, Schiphol had an annual passenger number of
forty-four million and forecasts saw this rising to sixty million in 2020.
Since 2020, SIAAG has shown a stable growth in passenger numbers of about 5% annually,
largely stemming from new direct connections to short and intermediate distance
destinations. SIAAG ascribes this growth to new regional airlines opening new direct
connections to European and North African cities. The new operators are flying short haul
(up to 2,500 km), highly efficient hydro-powered planes and have limited services on board to
reduce cost. The feeder operations of the three mega airlines to London, Prague, and Milan,
which were the basis for survival during the early 2020s have started to lose market share to
these new operators as travel time savings for European and North African destinations can
be huge. The new operators are lobbying for the lifting of the night curfew and the opening of
the window of flight hours: ‘our new hydro-powered aircraft are very silent, so the night curfew
is not necessary anymore’, said Mrs Ellis Jackson, spokesperson of Cheetah, one of the fastest
growers in this market.
SIAAG’s cargo activities, which traditionally accounted for about 40% of departures, are
currently in a decline and revenues are dwindling. The long-distance haul of high value goods
has been reduced, especially now that trade in the important plant and flower sector has
become almost 100% virtual; only Dutch flowers are now flown out. Recovery of this market is
not expected.
5.5.7 Step 7: Evaluate the Key Question
The aim of the TNLI study was to identify different plausible futures for civil aviation in
the Netherlands and reflect on the implications of each of these futures on the infrastruc-
ture that would be required to accommodate demand. In case of Scenario 5 discussed
in Step 6, the implications are that no new infrastructure is needed. The airports in the
Netherlands have sufficient capacity to handle the demand for direct flights and for flights
from the Netherlands to one of the three mega hubs. If this future were to come to pass,
any new investments in expanding airport capacity in the Netherlands would be rendered
superfluous. As opposed to this, in some of the other scenarios that were analysed, there
135

Futures
Policy AnAlysis of Multi-Actor systeMs
was a clear need for additional investments in capacity at Schiphol. Given the uncer-
tainty about future demand for air transport and about the type of network that would
be in place, the advice was to develop an adaptive policy for the future of civil aviation in
the Netherlands. This adaptive policy would prepare plans for capacity investments, but
implementation would depend on how the actual situation developed.
5.6 Beyond Exploring the Future
The methods discussed in this chapter all focus on exploring the future and reflect some
of the most frequently employed methods in practice. In recent years however, due to
challenges like climate change-induced disasters, the financial crisis of 2007-2008, and
the corona pandemic, all kinds of extensions, hybrids and novel methods for exploring
uncertainty have emerged. Moreover, there is also increasing attention for dealing with
uncertainty in policy-making in addition to exploring uncertainty.
One very active area of development is the combined use of modelling and simula-
tion with scenario methods. Broadly speaking, two styles of approaches exist. On the
one hand, there is the ‘storyline and simulate’ approach. Here, qualitative scenarios are
developed first for example using the methods described in Section 5.3. Next, the sce-
nario developers work closely with modellers to translate each scenario into a set of input
parameters for a simulation model. This enables the use of scenarios with more formal
models of the system under study. This ‘storyline and simulate’ approach is for example
the way in which climate change scenarios are developed by the IPCC. First scenarios have
been created for future socio-economic conditions and for how emissions of greenhouse
gasses might develop over the coming century. These shared socio-economic pathways
and their so-called reference concentration pathways are then used as input to, for exam-
ple, global climate models to estimate how the mean average annual temperature will
change, or what this would imply for sea-level rise.
On the other hand, there is also a rich literature on ‘exploratory modelling’ and ‘sce-
nario discovery’. Here one starts with a simulation model of the system under study.
Next, one identifies the key uncertain parameters associated with this model and tries
to estimate plausible ranges for these parameters. You can think of this as a very large
n-dimensional space, or uncertainty space, where each point in this space represents one
possible parametrization of the simulation model. By running the model thousands of
times for carefully selected points in this space, you can explore this uncertainty space.
These points are computational experiments that reveal how the system would behave
if the sampled parameters would be true values. Scenario discovery is then the analysis
of these thousands of experiments. Typically, the outcomes of the experiments are first
classified based on which results are of interest and which not. For example, the analysis
can focus on those experiments where the problem becomes worse. Next, using machine
learning algorithms, you can identify from where in the uncertainty space these experi-
ments under which the problem becomes worse originate. So, within what subspace of
the uncertainty space does the problem become worse? This can then be translated into a
narrative that can be communicated more broadly (Kwakkel, 2017). Exploratory modelling
and scenario discovery are frequently used to inform climate adaptation on infrastructure
systems where models of the infrastructure system are readily available.
136

serutuF
5 exPlorIng The fuTure
While ‘storyline and simulate’ and ‘scenario discovery’ both focus on exploring the
uncertainty by combining formal models with qualitative techniques, a separate line of
work focused on dealing with uncertainty. Given that the future is fundamentally open
and uncertain, what should a decision-maker do? The focus here has been on designing
policies that can be adapted over time in response to how the future is unfolding. Popular
methods for this include adaptive policy-making and dynamic adaptive policy pathways
(Haasnoot et al., 2013). The basic premise of both is that a policy is seen as a series of
actions where new actions are taken only if certain pre-specified conditions have been
met. Developments are carefully monitored, and if key thresholds are passed, the imple-
mentation of new actions is triggered (Kwakkel et al., 2016). Dynamic adaptive policy path-
ways underpin climate adaptation policies in many countries included the Dutch Delta
Program, the Thames Estuary, The Vietnam Mekong Delta Plan and coastal adaptation
strategies in New Zealand.
5.7 Takeaways
– We cannot know the future, but we can think what it might look like and prepare for it.
– Most formal methods like trend extrapolation, causal relations and analogy are based
on the assumption of continuity.
– Expert consultation is widely used for exploring uncertainties and expectations of
future developments of which the Delphi method is growing in popularity thanks to
web-based applications.
– Explorative scenarios sketch possible images of the future; normative scenarios sketch
a desired or undesired future.
– Policy scenarios describe how a system would evolve if specific policies would be
implemented and presume the context of these polices to be constant.
– Context scenarios describe the behaviour of the system when changes in the context
influence the behaviour of the system; they are used to assess the robustness of poli-
cies under changing external conditions.
– Developing scenarios is a method (eight steps) as well as a process of building trust
and system understanding by the participants.
– Exploratory modelling and scenario discovery focus on exploring the uncertainty by
combining formal models with qualitative techniques.
– A next step in future studies is the development of adaptive policies and exploration of
adaptive policy pathways.
References
Bell, W. (1997). Foundations of Futures Studies: Human Science for a New Era. Volume 1,
History, Purposes, and Knowledge. New Brunswick: Transaction Publishers.
Brill, J., Bishop, M. & Walker, A. (2006). An Investigation into the Competencies
Required of an Effective Project Manager: A Web-based Delphi Study. Educational
Technology Research & Development, 54(2), 115-140. https://doi.org/10.1007/s11423-006-
8251-y
Cole, Z.D., Donohoe, H.M. & Stellefson, M.L. (2013) Internet-Based Delphi Research:
Case Based Discussion. Environmental Management 51, 511–523. https://doi-org.tudelft.
idm.oclc.org/10.1007/s00267-012-0005-5
137

Futures
Policy AnAlysis of Multi-Actor systeMs
Enserink, B. (1993). Influencing Military Technological Innovation: Socio-Technical
Networks and the Development of the Supersonic Bomber. Delft: Eburon.
Enserink, B. (2000). Building Scenarios for the University. International Transactions in
Operational Research, 7(6), 569-584. https://doi.org/10.1111/j.1475-3995.2000.tb00217.x
Enserink, B. (2004). Thinking the Unthinkable – the End of the Dutch River Dike System?
Exploring a New Safety Concept for the River Management. Journal of Risk Research,
7(7-8), 745-758. https://doi.org/10.1080/13669870210166185
Enserink, B., van Bemmelen, I. & Kuiper, O. (2000). RivierenLand Ex-ante evaluatie
van het Transitieproces – een scenariostudie. Rapport aan de Dienst Weg- en
Waterbouwkunde, Directoraat-Generaal Rijkswaterstaat, Ministerie van Verkeer en
Waterstaat.
Funtowicz, S. O., & Ravetz, J. R. (1990). Uncertainty and quality in science for policy
(Vol. 15). Springer Science & Business Media.Garcia-Mata, C. & Schaffner, F. I.
(1934). Solar and Economic Relationships: A Preliminary Report. Quarterly Journal of
Economics, 49, 47. https://doi.org/10.2307/1883875
Glenn, J. C., Gordon, T. J., & Florescu, E. (2008). 2008 State of the Future. World
Federation of United Nations Association., https://www.millennium-project.org/
publications-2-3
Guess, G. M. & Farnham, P. G. (2000). Cases in Public Policy Analysis. Washington:
Georgetown University Press.
Haasnoot, M., Kwakkel, J. H., Walker, W. E. & Maat, J. (2013). Dynamic Adaptive
Policy Pathways: A Method for Crafting Robust Decisions for a Deeply Uncertain
World. Global Environmental Change, 23(2), 485-498. https://doi.org/10.1016/j.
gloenvcha.2012.12.006
Jaworski, J. (1996). Synchronicity. The Inner Path of Leadership. San Francisco: Berrett-
Koehler Publishers.
Knight, F.H. (1921) Risk, Uncertainty and Profit. Boston and New York, Houghton Mifflin
Company
Kwakkel, J., Walker, W., Marchau, V. (2010) Classifying and communicating uncertainties
in model-based policy analysis. International Journal of Technology Policy and
Management 10(4):299 – 315. https://doi.org/10.1504/IJTPM.2010.036918
Kwakkel, J. H. (2017). The Exploratory Modeling Workbench: An Open Source Toolkit
for Exploratory Modeling, Scenario Discovery, and (Multi-objective) Robust Decision
Making. Environmental Modelling & Software, 96, 239-250. https://doi.org/10.1016/j.
envsoft.2017.06.054
Kwakkel, J. H., Haasnoot, M. & Walker, W. E. (2016). Comparing Robust Decision-
Making and Dynamic Adaptive Policy Pathways for Model-based Decision Support
under Deep Uncertainty. Environmental Modelling & Software, 86, 168-183. https://
doi.org/10.1016/j.envsoft.2016.09.017
Lenz, R. C. Jr. (1962). Technological Forecasting. ASD-TDR-62-414, Aeronautical Systems
Division, Air Force Systems Command (DDC Number AD 408 085).
Lipinski, A. & Loveridge, D. (1982). Multiple Perspective: Concept, Application and User
Guidelines. Systems Practice, 2(3), 307-331. https://doi.org/10.1007/BF01059977
Marchau, V. (2000). Technology Assessment Automated Vehicle Guidance. Future Prospects
for Automated Driving Implementation (dissertatie). Delft: Delftse Universitaire Pers.
138

serutuF
5 exPlorIng The fuTure
Marchau, V. A., Walker, W. E., Bloemen, P. J. & Popper, S. W. (2019). Decision Making
under Deep Uncertainty: From Theory to Practice (p. 405). Springer Nature, DMDU
OPEN
Marchetti, C. (1980). Society as a Learning System: Discovery, Invention, and Innovation
Cycles Revisited. Technological Forecasting and Social Change, 18, 267-282. https://doi.
org/10.1016/0040-1625(80)90090-6
Meadows, D., Richardson, J. & Bruckmann, G. (1982). Groping in the Dark; the First
Decade of Global Modeling. 6th IIASA symposium on global modeling, expanded
proceedings. Chichester: Wiley.
Meijer, M. H. & Korving, H. (2001). Beslissen over het Riool onder Onzekerheid. H2O,
34(20), 19-21.
Onencan, A., Enserink, B., van de Walle, B. & Chelang, J. (2016). Coupling Nile Basin
2050 Scenarios with the IPCC 2100 Projections for Climate-induced Risk Reduction.
Procedia Engineering, 159, 357-365. http://doi.org/10.1016/j.proeng.2016.08.212
Planbureau voor de Leefomgeving (2012). Nieuwe steden in de Randstad. Verstedelijking
en suburbaniteit. PBL Den Haag isbn 978-94-91506-14-7.
Porter, A.L., Roper, A.T., Mason, T.W., Rossini, F.A., Banks, J. (1991) Forecasting
and Management of Technology. ETM Wiley Series in Engineering & Technology
Management. John Wiley & Sons INc New York, Chichester, Brisbane, Toronto,
Singapore
Rosenhead, J. (1989). Robustness Analysis; Keeping Your Options Open. In J. Rosenhead
(Ed.), Rational Analysis for a Problematic World. Chichester, West Sussex: John Wiley
and Sons Ltd.
Schnaars, S. P. (1989). Megamistakes: Forecasting and the Myth of Rapid Technological
Change. New York: The Free Press.
The Futures Group International (1994). Scenarios. In J. C. Glenn (Ed.), 1999. Futures
Research Methodology Version 1.0. American Council for the United Nations University.
https://www.millennium-project.org
van Asselt, M.B.A., Rotmans, J. (2002) Uncertainty in Integrated Assessment
Modelling. Climatic Change 54, 75–105 (2002). https://doi-org.tudelft.idm.oclc.
org/10.1023/A:1015783803445
van Daalen, C., Thissen, W. & Verbraeck, A. (1999). Methods for the Modeling and
Analysis of Alternatives. In A. P. Sage & W. B. Rouse (Eds.), Handbook of Systems
Engineering and Management (Chapter 26). pp. 1037-1076. New York: Wiley. ISBN 978-
0471154051.
van der Sluijs, J.P. (1997) Anchoring Amid Uncertainty: On the Management of
Uncertainties in Risk Assessment of Antropogenic Climate Change. Universiteit
Utrecht, PhD Thesis
Vergragt, P. J. & Quist, J. (2011) Backcasting for Sustainability: Introduction to the Special
Issue. Technological Forecasting and Social Change, 78(5), 747-755. www.sciencedirect.
com/science/article/pii/S004016251100062X.
Walker, W.E., Harremoës, P., Rotmans, J., van der Sluijs, J.P., van Asselt, M.B.A., Janssen
P. & Krayer von Krauss, M.P. (2003) Defining Uncertainty: A Conceptual Basis for
Uncertainty Management in Model-Based Decision Support, Integrated Assessment,
https://doi.org/10.1076/iaij.4.1.5.16466.
139

Futures
Policy AnAlysis of Multi-Actor systeMs
Walker, W.E., Marchau, V.A.W.J., Kwakkel, J.H. (2013). Uncertainty in the Framework of
Policy Analysis. In: Thissen, W., Walker, W. (eds) Public Policy Analysis. International
Series in Operations Research & Management Science, vol 179. Springer, Boston, MA.
https://doi-org.tudelft.idm.oclc.org/10.1007/978-1-4614-4602-6_9.
Wise, G. (1976). The Accuracy of Technological Forecasts: 1890-1940. Futures, 8(5), 411-
419. https://doi.org/10.1016/0016-3287(76)90005-7.
140

sisehtnyS
6 From Synthesis to Plan of Action
In the previous chapters, we analysed various aspects of the policy problem. Now we are
facing an important challenge: synthesizing the outcomes of the individual analyses to
yield a rich and insightful problem description. Also, based on our synthesis, we need to
diagnose or characterize the problem and think up follow-on activities; we should offer
the problem owner(s) a new perspective and suggest some next steps towards a solution
of their problem.
Remember you started from the initial problem perception of the problem owner (Fig-
ure 6.1). This perception could be biased or otherwise flawed and therefore as an analyst
you are supposed to investigate and analyse the problem yourself. In the previous chap-
ters, you learnt to analyse different dimensions of a policy problem: the system, the actors
and the uncertainties. This chapter discusses how to synthesize these partial analyses,
which is supposed to lead to a rich problem understanding and subsequent rich problem
description. Most likely, the rich problem description provides new insights to the prob-
lem owner: presenting factors, actors, relations, dependencies, or concerns and issues
that had been overlooked before. It provides a solid foundation for the ‘Plan’ stage (Fig-
ure 6.1), which should lead to ideas for solving the problem as is shown in the right-hand
part of the figure. In this planning stage you have to transit to making a sensible plan; you
have to characterize or frame the problem, identify knowledge gaps and propose follow-
on activities. As a final product, you come up with a (re-)framed problem description and
a plan of action for follow-on activities. The latter products are discussed in greater detail
in the next chapters; in this chapter we will discuss how to get to a rich problem descrip-
tion and then focus on the activities in the ‘Plan’ stage.
Synthesize
Plan
Actor/ Charac-
network terizethe Propose
Ini�al C sy a s u t s e a m l/ analysis Rich problem f a o c l � lo v w i� -o es n pr F o r b am lem ed &
problem analysis problem Plan of
percep�on descrip�on
ac�on
Iden�fy
Future knowledge
scenario gaps
analysis
Result or situa�on Time sequence
Process or ac�vity Mutual influence
Figure 6.1 Steps in problem analysis
141

Synthesis
Policy AnAlysis of Multi-Actor systeMs
Before discussing how this can be done, we emphasize that synthesizing the partial analy-
ses is more than summarizing their outcomes. Instead, the aim is to generate new insights
by combining those outcomes. In doing so, you will arrive at conclusions that transcend
the outcomes of each partial analysis separately – the whole is more than the sum of its
parts. For this, you will need to adopt the role of the ‘reflective practitioner’ (Schön, 1995),
which means you should question your own experiences and insights, thus improving
those insights and increasing your value for your problem owner. What this entails in
practice is the subject of the current chapter.
Synthesizing the partial analyses is typically accomplished by taking the following steps:
1. revise the initial system diagram drawing on the actor analysis and the scenario analy-
sis, and ensure that all your diagrams and analyses are consistent with each other;
2. revise the initial problem description to yield the rich problem description.
As depicted in Figure 6.1, once the rich problem description has been developed, the time
has come to plan and think about follow-on activities. The follow-on activities should
enable the problem owner and other actors to move the problem in the direction of a
(partial) solution. It might even be just a first step in the process towards problem-solving.
Three activities are required as a preparation for writing the plan of action: characterizing
the problem, identification of knowledge gaps and deciding on suitable follow-on activi-
ties.
Characterizing the problem is what we do by taking a kind of ‘helicopter view’; we try
to discern patterns and mechanisms that may characterize the problem. We should ask
questions like: what is happening here?; what are the main characteristics of the prob-
lem?; what perspective should we take?; what problem frame would be helpful to move
towards a solution for the problem? For instance: is the problem leaning towards a dispute
on values; is it a content or (missing or disputed) knowledge problem or more institu-
tional or (political) process oriented?
Knowledge gaps are relevant when they hinder progress. Knowledge gaps can be mani-
fold ranging from uncertainties about the extent to which specific factors influence the
functioning of the system, to lack of knowledge about the values and concerns of specific
stakeholders, to disputes about the legitimacy of the decision-making process itself.
Proposing suitable follow-on activities comes next, as the characterization of the problem
and the eventual knowledge gaps determine in what direction solutions should be sought.
However, what follow-on activities should be considered suitable is also determined by
the role that the policy analyst intends to take in these follow-on activities. Depending on
their background, some analysts will be more inclined to quantitative modelling activities
while others might be great process moderators and prefer to mediate in value conflicts.
Anyway proposing follow-on activities in fact is the underlying objective of any problem
exploration as the initial analysis is intended to surface the relevant issues and to focus the
research efforts on the real causes of the problem. Clearly, the character of the problem,
the proposed (research) activities and the specialisms of the team proposed to execute
the follow-on activities should all match. Only if the problem exploration showed that the
problem actually did not exist, no follow-on activities should be suggested.
142

sisehtnyS
6 from synThesIs To Plan of aCTIon
As discussed, the rich problem description therefore is the starting point for the ‘Plan’
stage, which is accomplished by:
1. characterizing and framing the problem;
2. identifying knowledge gaps that might require further study;
3. a reflection on the role you need to take as a policy analyst to support the problem
owner in subsequent steps;
4. proposing follow-on activities that will help the problem owner to bring the problem
closer to a solution.
These steps are discussed one by one in the following sections. Beware though that in
practice planning is an iterative process. As depicted in Figure 6.1, the three activities
– characterizing the problem, identifying knowledge gaps and proposing follow-on activi-
ties – are not necessarily occurring in this sequence; but definitively they are mutually
influencing each other. Planning therefore is an iterative process and may not be as struc-
tured as depicted here.
6.1 System Diagram Revision
The synthesis draws on all three partial analyses presented in Chapters 3, 4 and 5. The
system diagram is the main conceptual model for this synthesis. The system diagram, as
presented in Chapter 3, depicts the system of interest.
A system diagram for an initial problem perception (as perceived by the problem owner)
consists of the following four components
1. a causal diagram of factors representing the system itself;
2. the means of the problem owner;
3. the external factors;
4. the criteria (outcomes of interest).
Remember that in problem explorations, the initial system diagram represents the prob-
lem as framed by the problem owner or client. This initial diagram was developed in
a number of iterative steps in which different conceptual modelling techniques were
employed: a means-ends diagram to make the first demarcation choices; an objectives
tree for the identification of criteria; and a causal map for the identification and structuring
of system factors, external factors, means and their relations. By doing so, we created a
conceptual model of the problem, thinking through the problem as framed by the problem
owner; through causal reasoning we constructed a ‘mental map’ (Rein & Schön, 1993)
of the problem from the perspective of the problem owner. This initial system diagram
was the point of departure for further problem exploration by means of two additional
partial analyses: an actor analysis (Chapter 4) and a scenario analysis (Chapter 5). After
these additional analyses, it is time to revisit and most probably revise the initial system
diagram and adapt it to our newly gained insights. As visualized in Table 6.1, this means
you have to determine if and how the initial system diagram should be modified. Below
we exemplify how the actor analysis and scenario analysis may prompt the need to revise
the initial system diagram.
143

Synthesis
Policy AnAlysis of Multi-Actor systeMs
Table 6.1 Elements of system diagrams that visualize two phases in problem descrip-
tion
System Diagram I System Diagram II
Initial Problem Perception Rich Problem Perception
System boundary Adjusted system boundary encompasses the diverging problem percep-
tions of other actors and reflects new insights about what factors can be
controlled with the available means
Causal diagram of factors New (system) factors may have become apparent or factors are found to be
representing the system itself insufficiently relevant and can be left out
Means of the problem owner New means (input factors) are added to signal that they may be available
when other actors become active allies of the problem owner, thus forming
a coalition of like-minded actors
Relevant external factors Other relevant external factors may have become apparent; the system
boundary has shifted or factors have been shown to be irrelevant
Criteria (outcomes of interest) New criteria (output factors) may be added to accommodate for the wishes
of critical actors
First, actor analysis provided additional insights into the problem and its social, institu-
tional and/or political environment. It produced an inventory of actors and their percep-
tions, objectives and resources, and identified the critical actors present in the problem
situation. You determined the resource dependencies, pinpointed critical actors, and iden-
tified potential support and opposition in the actor network. Therefore, you now know
what additional means might be available to the problem owner and what concerns should
be taken into account for creating an acceptable solution. These insights may require you
to revise the problem formulation as new dilemmas may have become part of it. Conse-
quently, the system diagram may need to be changed in one or more of the following ways:
– New criteria (output factors) may be added to accommodate for the wishes of critical
actors.
– New means (input factors) may be available as other actors become active allies of the
problem owner, thus forming a coalition of like-minded actors.
– New factors (system factors) may have become apparent.
– New external factors may have become apparent.
– The system boundary might need to be changed as the problem changed due to the
diverging perceptions and objectives (criteria) of other actors.
Second, the scenario analysis may have revealed important factors that are outside the
span of control of the problem owner or the supportive critical actors. Still, these external
factors can influence the outcome and effectiveness of policies and should therefore be
incorporated in the system diagram. In addition, new information on possible external
developments may also lead to a problem shift or even a new problem definition. In the
Netherlands, for instance, scenarios on climate change may reveal that we should expect
periods of severe drought instead of superfluous rainfall. Such insights trigger the need
for new water management policies aimed at storing water instead of focusing on water
drainage. These insights from a scenario analysis may lead to alternative problem formu-
lations and the need to adapt the system diagram in one or more of the following ways:
– New external factors that impact factors in the system may need to be added.
– New factors (system factors) may have become apparent.
144

sisehtnyS
6 from synThesIs To Plan of aCTIon
– The system boundary may need to be moved because some of the internal factors
are found to be outside the influence of the problem owner or the other way around:
external factors turn out to be under the control of the problem owner or its allies.
Beware: in this book we focused on scenario analysis as a tool or method to explore future
uncertainties, but there exists a wealth of methods for exploring the future and for dealing
with uncertainty. For some problems it might suffice to do a simple trend extrapolation or
you might need to focus on specific model uncertainties (see Chapter 5). Though taking
uncertainties into account in your analysis is a prerequisite for a decent problem analysis,
exploring the future also supports the design of potential policies and strategies. Apart
from triggering changes to the system diagram, the scenario analysis may also provide
insights into the importance of various other external factors and may be used to assess
the robustness of proposed policies. The latter may also prompt the need for adaptive poli-
cies and the design of monitoring regimes that monitor the developments in key external
forces that may spur the need for changes in policy. This may also prompt the need for
further research, for instance by additional (dynamic) exploratory modelling or scenario
studies, by designing adaptive policies and/or by the design of monitoring regimes that
monitor the developments in key external forces (Haasnoot et al., 2013; Kwakkel et al.,
2015). This further research may eventually lead to changes in policy.
6.1.1 Consistency Check
Revising the system diagram as described here is in fact an iterative process. In practice,
many analysts will be checking and updating their models time and again during the partial
analyses; after each analytical activity, new insights lead to adaptations of the previous
models. Therefore, the activities above should take place at various points in time, not only
after having finalized the partial analyses. Throughout the problem exploration process
and the various iterations, the analyst should continuously check for consistency in and
between the models and listings they produce. For instance, if specific criteria are found
to be relevant in the objectives tree, they may not lack in the system diagram and the other
way around. When checking for consistency, the analyst needs to make important concep-
tual decisions about the relevance of factors and the system’s demarcation. The scope and
framing of the problem is determined by these choices. Important choices should therefore
be made explicit and justified to allow the potential commissioner of proposed follow-on
activities to realize the consequences of these choices. They might influence the content
and scope of the problem and the expected outcome of proposed follow-on activities.
6.2 Rich Problem Description
The analysis started with an initial problem description based on the insights and per-
spectives of the problem owner. As argued before, this initial problem description may
have been biased or flawed due to the one-sided perspective that was (deliberately) cho-
sen. To provide a more thorough understanding of the problem, additional analyses were
carried out to enrich the initial problem description with, for instance, the perspectives
of other actors. Now that we have synthesized these additional analyses and drawn up a
consistent, multi-actor system diagram, it is time to produce a rich problem description
that does justice to the complexity of the (multi-actor) problem situation in a better way
than the initial problem description did.
145

Synthesis
Policy AnAlysis of Multi-Actor systeMs
A rich problem description should make explicit the difference between the problem
owner’s initial concerns as a starting point for the research and the richer picture of the
current (or future) situation, which is the result of our analytical efforts and the desired
situation. Therefore, a rich problem description should assume a multi-actor perspective,
i.e. the problem description should take into account the different concerns, objectives
and means of other important actors and position the problem owner in this field of
actors as this position and the problem owner’s dependency on other actors’ means influ-
ences the range of possible actions and solutions. In addition, a rich problem description
should take into account foreseeable future developments that could alter the problem
situation for the better or the worse and sketch the level of uncertainty.
Situations do exist where there is no problem owner (yet), for instance situations where
one knows something is going to happen or change in the (near) future, but no one is or
feels responsible (yet). For instance, technical developments like autonomous driving,
artificial intelligence, blockchain technology, or deep-sea and arctic mining are potentially
disruptive technologies that have the potential to change the world as we know it today.
The purpose of a rich problem description then is to indicate what parties should play a
role in facilitating, regulating, slowing down or preventing such developments.
Typical for a rich problem description is that the analyst also distances themselves from
the initial perspective of the problem owner. Supported by the insights gained in the addi-
tional analyses, the analyst tries to see the larger picture: what are the main causes of the
enriched problem; what are potential tensions between the critical actors; what are the
uncertainties threatening the status quo.
6.3 Characterizing and Framing the Problem
The rich problem description is the outcome or product of the analyses that have been
executed. The next challenge though is to offer a perspective for problem-solving or at
least for moving the problem into the direction of a solution by suggesting a next step.
For thinking up such a strategy, for offering a perspective for problem-solving, the practi-
cal experience and tacit knowledge of the analyst are an important basis. Practitioners
will advise you to take a so-called ‘helicopter view’ of the issue at hand. When looking at
the problem from some ‘distance’, you might be able to discern what are the main issues;
what patterns can be seen; is the problem leaning more towards the technical or organi-
zational domain; is there consensus or conflict; is the lack of knowledge determining the
outcome; an institutional mismatch or the lack of cooperation? In this way, priority issues
and/or a specific perspective can be chosen; what issues should be resolved first to move
towards a solution; and how can they be characterized? Recognizing such general patterns
and prioritizing the issues that need to be tackled first will help to frame or reframe the
problem at hand. Beware that the way of characterizing or framing the problem largely
determines what follow-on activities will be proposed as will be discussed in the remain-
der of this chapter and is illustrated in Table 6.2.
Typical frames are for instance the existence of large differences in values between the
critical actors because of which they do not agree on what the problem is about and whether
or not or in what way the problem needs to be solved. Another well-known frame is that
the solution of one problem generates new or even bigger problems as the negative con-
sequences may be affecting yet another actor. Table 6.2 provides you with some examples
of frequently used problem frames that may serve as a reference to frame other problems.
146

sisehtnyS
6 from synThesIs To Plan of aCTIon
Table 6.2 Examples of problem characterizations
Problem Characterization
Large differences in values and/or problem perception and (need for) solution
Large differences in problem perception among stakeholders about one promising solution
Trade-off to be made in choosing one out of various (technical) solutions
Uncertainty about incentives for (potential) cooperation from stakeholders needed in realization of a promising
solution
Institutional design and/or hierarchy in stakeholder arena hampers problem-solving
Large uncertainty about the future hampers problem-solving
Chicken-and-egg problem hampers reaching policy goal
As indicated, the characterizations or problem frames in Table 6.2 may apply to a wide
range of policy problems. Each frame corresponds to a different storyline that may be
used to report about the problem and about the proposed follow-on activities. In Chap-
ter 8, we will elaborate on using these problem frames to generate such storylines.
Problem framing is an iterative process; going back and forth between the rich prob-
lem description and the insights on the functioning and flaws of the system under study
and the resources and knowledge available to the analysts. Consequently, the perspective
towards solving the problem is sketched. Obviously this is not a straightforward activ-
ity; therefore, in Section 6.5, we will discuss how you might classify or characterize the
problem at hand by using the hexagon model of Mayer et al. (2004). The hexagon model
sketches the potential positions and the role of the analyst in problem-solving. This will
help to further explore how you might use the framed problem to arrive at useful follow-
on activities. But first we will discuss the need for making explicit the knowledge gaps and
discuss their role in the planning stage.
6.4 Knowledge Gaps
During the extensive problem analysis so far, the analyst most probably discovered new
issues and uncertainties that may be the starting point for further research into the com-
plex issue at hand. Moreover, the scenario analysis would have revealed which knowledge
gaps and strategic options are robust or not robust at all in most of the possible future
scenarios. In other words, which issues remain pressing under varying circumstances and
thus deserve attention. Knowledge gaps typically emerge from:
– new factors;
– unknown impacting factors and relations between factors;
– uncertainties about impacting factors and the relation between factors;
– uncertainties about system behaviour;
– new actors;
– new issues and issues voiced by concerned actors and stakeholders;
– uncertainties about actors’ perceptions or positions;
– uncertainties about the occurrence and impact of external factors;
– unknown effects and impacts of new solution alternatives/strategies.
Consequently, knowledge gaps can vary in nature: they may be technical or systemic in
character but can be of a social, political or economic nature or a combination of these.
147

Synthesis
Policy AnAlysis of Multi-Actor systeMs
Clearly the analyst has to decide which issues should be tackled and what research is
needed. Most often, moving a problem closer to its solution implies some research will be
needed. Even in severe conflicts of interest, where only mediation might work, often there
are underlying or related issues, which might be solved by scientific research.
Addressing knowledge gaps like the ones listed above most likely will be part of any pro-
posal for further activities. It is important to realize to bring forward only those gaps that
hinder progress. The to-be-acquired knowledge should contribute to problem-solving to
support the client/problem owner to move his/her problem closer to a solution. In other
words, the proposed research should be relevant and contribute to problem-solving. The
latter issues and the action of writing a research plan to handle these content- or knowl-
edge-related issues are discussed in more detail in Chapter 7.
6.5 The Role of the Analyst
In the rich problem description we have been framing the problem – we determined the
type of problem that we are dealing with; is the problem more content oriented or process
oriented or a mix of the two and what aspect gets priority? This characterization or fram-
ing of the problem will help us understand what follow-on activities are suitable for the
problem owner to move towards a solution of the problem. Also, it will help us as a policy
analyst to determine what role we need to take in subsequent steps. To determine the role
we might take as a policy analyst, we propose to use the hexagon model of policy analyti-
cal activities and styles by Mayer et al. (2004; see Figure 6.2). Below, we discuss how we
may use the hexagon model to understand the policy analyst’s role in subsequent steps.
Figure 6.2 The hexagon model of policy analytical activities (Source: Mayer et al.,
2004: 173)
148

sisehtnyS
6 from synThesIs To Plan of aCTIon
6.5.1 Six Types of Policy Analytical Activities
The hexagon model defines six types of policy analytical follow-on activities, such as
‘Research and analyse’ or ‘Mediate’ (see Figure 6.2; we refer to the article by Mayer et
al. (2004) for a complete survey of activities). To be able to further the solving of the
policy problem, we need to select one or more such types of suitable follow-on activities.
Departing from our rich problem description, we characterized the problem and listed
the knowledge gaps that may prevent progress making towards a solution. Now we need
to consider how the different types of activities mentioned in the hexagon model may
contribute to tackling the problem. Finally, we will have to select the types of activities that
seem most appropriate.
We provide two examples: first, consider a policy problem in which the problem owner
seems to be overlooking certain clever solutions and has not paid sufficient attention
to ideas and concerns of other stakeholders. This typically calls for activities of the type
‘design and recommend’ from the hexagon model: ‘design and recommend’ activities aim
to find solutions and compare their effectiveness, costs, feasibility, etc. This problem may,
therefore, be characterized as one in need of a better defined solution space.
Second, consider a policy problem in which certain groups of citizens threaten to haul
the decision-makers into court because they feel they had no say in the decision process.
This type of problem typically requires activities from the ‘democratize’ section of the
hexagon model to make the problem-solving process more inclusive. Therefore, this prob-
lem may be characterized as one that suffers from underrepresented actors.
In Section 6.3, we discussed how we might characterize problems and in Table 6.2,
we presented a list of problem characterizations we often come across in practice. Each
problem characterization or problem frame corresponds to one or more activities from
the hexagon model by Mayer et al. (2004) as shown in Table 6.3. The hexagon model and
the analytical activities depicted at its six corners will be discussed in more detail in the
next section when we focus on the role of the analyst.
Table 6.3 Examples of problem characterizations and follow-on activities
Problem Characterization Corresponding Hexagon Follow-On Activities
Large differences in values and/or problem perception Clarify Values and Arguments; Mediate
and (need for) solution
Large differences in problem perception among Clarify Values and Arguments; Design and
stakeholders about one promising solution Recommend
Trade-off to be made in choosing one out of various Design and Recommend; Research and Analyse
(technical) solutions
Uncertainty about incentives for (potential) Advise Strategically; Mediate
cooperation from stakeholders needed in realization
of a promising solution
Institutional design and/or hierarchy in stakeholder Research and Analyse; Mediate
arena hampers problem-solving
Large uncertainty about the future hampers problem- Clarify Values and Arguments; Design and
solving Recommend
Chicken-and-egg problem hampers reaching policy Advise Strategically; Research and Analyse
goal
149

Synthesis
Policy AnAlysis of Multi-Actor systeMs
The examples in Table 6.3 show how the hexagon model by Mayer et al. may be used once
there is a rich problem description and the problem has been characterized. The chosen
characterization leads us to selecting one or more suitable types of follow-on activities from
the hexagon that are likely to contribute to solving the problem that the problem owner
faces. Another way to determine subsequent steps is to consider the policy analyst’s role in
addressing the problem. For this, the hexagon model may be used as well.
As shown in Table 6.4, every type of activity in the hexagon model comes with a dif-
ferent role of the policy analyst in the follow-on process. For instance, the ‘Research and
analyse’ type of activities require the analyst to act as an independent scientist who keeps
a professional distance from clients. In contrast, analysts engaged in ‘Advise strategically’
type of activities need to be engaged client advisors with much less need of scientific
independence. For a complete description of policy analytical roles associated with the
various types of activities in the hexagon model, we refer to the original article by Mayer
et al. (2004).
Similar to selecting the type of activities, determining the role of the policy analyst may
also help to choose follow-on activities. For instance, if you decide that the problem at
hand needs a client counsellor or mediator to further it, this indicates that the problem is
essentially different from the one that requires an independent scientific researcher.
Table 6.4 Roles of the policy analyst
Activity Policy Analyst Role
Research and Analyse Independent scientist; Objective researcher
Design and Recommend Independent expert; Engineer; Impartial advisor
Clarify Values and Arguments Logician or ethicist; Narrator
Advise Strategically Involved client advisor; Client counsellor
Democratize Democratic (issue) advocate; Process designer
Mediate Facilitator; Process manager; Action researcher
Source: Mayer et al. (2004)
6.5.2 Blends of Activities and Roles
In practice, we find that the majority of policy problems cannot be addressed by a single
type of activity or a single role of the analyst. Instead, they are usually addressed by a blend
of activities and roles from the hexagon model.
For instance, we may select a blend of activities from the top half of the hexagon. The
top half of the hexagon (Figure 6.2) consists of activities that are predominantly aimed at
knowledge discovery. These activities are suitable for policy problems that require factual
questions to be answered, where evidence can be gathered and/or where additional analy-
sis can be usefully applied to reduce uncertainties and help decision-makers. Activities
from the top half of the hexagon require an analytic style in which the ‘content’ aspects
(numbers, quantification and modelling) are key and the ‘process’ (stakeholder involve-
ment and management) is supportive.
In contrast, activities for treating political or contentious issues, where there is no agree-
ment on objectives and values, may be found in the bottom half of the hexagon. Here, the
‘process’ aspects of the activities are key and the ‘content’ is supportive. These types of
problems require process-oriented types of follow-on activities, where the commitment
of actors and stakeholder management are more important for problem-solving than the
150

sisehtnyS
6 from synThesIs To Plan of aCTIon
production of factual knowledge (see also the difference between ‘Traditional Science’
and ‘Interactive Analysis’ as distinguished by De Bruijn & Porter, 2004). Consequently, if
activities from the top half of the hexagon, such as modelling and computer simulation,
are required in such problems, they need to be carefully embedded in the activity’s pro-
cess to keep all actors ‘on board’. If not, they may lead to unsuccessful outcomes that are
not accepted by all participants in the activity.
Selecting a blend of follow-on activities from either the top half or the bottom half of the
hexagon also bears consequences for the role that you as a policy analyst need to assume.
Activities from the top half call for a more rigorous, scientific approach to produce irrefut-
able, factual outcomes. In contrast, activities from the bottom half require you to be more
sensitive to issues at the personal and group level to maintain a supportive atmosphere
that promotes social learning among the participants.
Summarizing, in most cases a blend of activities from the hexagon model is required
to work towards a solution. Often activities from either the top half or the bottom half of
the hexagon are selected. The choice for either half bears consequences for the role of the
analyst as explained above. It should be noted, though, that many policy problems require
both content-oriented and process-oriented follow-on activities. For instance, assume that
our analysis showed that modelling the behaviour of vehicle owners would be worthwhile
for assessing the effectiveness of road levies and other policy measures. We know, how-
ever, that these policies are heavily contested and parties are fighting over the character of
the problem: some find it a matter of calculating the optimal tax levels (content-oriented
activity), whereas others require a debate about the fundamental justification of these
measures (process-oriented activity). Therefore, in this case it might be wise to propose a
blend of activities from both the top half and the bottom half of the hexagon. For instance,
to involve parties in a participative modelling process. This may yield the outcomes of the
modelling exercise to be accepted by all.
6.6 Proposing Follow-On Activities
As mentioned in the introduction to this chapter, our synthesis should ultimately lead to
a framed problem and a plan of action for the problem owner to allow the problem owner
to take the next steps towards a solution of their problem.
If you selected generic activities as mentioned in the hexagon model, you will need to
specify them before adding them to a plan of action. For instance, if you propose to ‘set
up a mediation effort’, you will need to specify at least which parties will be involved and
what conflict will be the topic of the mediation process. Often, detailed specifications are
needed for your client to accept your proposal. Also, you should specify what expertise,
what scientific disciplines will be needed and how you or your associates may support the
problem owner in the proposed activities. Your proposal should, therefore, convince the
problem owner that you have the skills and knowledge required to successfully support
the problem owner in the proposed subsequent steps.
We emphasize that there exist many types of plans of action. What type is suitable for
your situation depends mainly on how you framed the problem. For instance, if the prob-
lem is framed as ‘large differences in values and/or problem perception and (need for)
solution’ and, therefore, calls for follow-on activities of the type ‘Clarify Values and Argu-
ments’ or ‘Mediate’ (see Table 6.3), the plan of action should contain a process descrip-
tion aimed at overcoming these differences in values and problem perceptions. The
151

Synthesis
Policy AnAlysis of Multi-Actor systeMs
plan should convince the problem owner that your approach is most suitable to proceed
towards a solution of the problem.
Different problem frames therefore do require different types of plans of action. In the
following chapter, we elaborate on one specific type: the research proposal. As indicated
in Chapter 1, within the context of this book, particular attention is given to conducting
research as a follow-on activity; therefore, in Chapter 7, you will learn how to plan activities
aimed at generating new knowledge to fill in eventual knowledge gaps that you identified
in the policy problem. Even though a research proposal is the typical step-up towards
activities in the ‘research and analyse’ corner of the hexagon, a research proposal has a
much wider use and is also useful for most of the other research activities located in the
top half of the hexagon.
6.7 Takeaways
– Synthesis implies including in the initial system diagram all relevant factors surfacing
in the actor analysis and the scenario analysis and checking for consistency.
– The synthesis results in a revision of the initial problem description to yield the rich
problem description.
– Planning is an iterative process that includes characterizing the problem, determining
knowledge gaps and proposing follow-on activities.
– Mayer’s hexagon model is a good tool for deciding on suitable follow-on activities and
the role of the analyst in these activities.
References
De Bruijn, H. & Porter, A. L. (2004). The Education of a Technology Policy Analyst – to
Process Management. Technology Analysis & Strategic Management, 16(2), 261-274.
https://doi.org/10.1080/09537320410001682919.
Haasnoot, M., Kwakkel, J. H., Walker, W. E. & Ter Maat, J. (2013). Dynamic Adaptive
Policy Pathways: A Method for Crafting Robust Decisions for a Deeply Uncertain
World. Global Environmental Change, 23(2), 485-498. https://doi.org/10.1016/j.
gloenvcha.2012.12.006.
Kwakkel, J. H., Haasnoot, M. & Walker, W. E. (2015). Developing Dynamic Adaptive Policy
Pathways: A Computer-Assisted Approach for Developing Adaptive Strategies for a
Deeply Uncertain World. Climatic Change, 132(3), 373-386. https://doi.org/10.1007/
s10584-014-1210-4.
Mayer, I. S., Van Daalen, C. E. & Bots, P. W. G. (2004). Perspectives on Policy Analysis:
a Framework for Understanding and Design. International Journal of Technology, Policy
and Management, 4(2), 169-191. https://doi.org/10.1504/IJTPM.2004.004819
Rein, M. & Schön, D. (1993). Reframing Policy Discourse. In F. Fischer & J. Forester
(Eds.), The Argumentative Turn in Policy Analysis and Planning. Durham: Duke
University Press.
Schön, D. (1995). The Reflective Practitioner: How Professionals Think in Action. Farnham:
Ashgate.
152

nalp
hcraeseR
7 The Research Plan
In the previous chapter, we revisited the initial system diagram and the initial problem
definition and synthesized the outcomes of the individual analyses to yield a rich prob-
lem description. This enabled us to assess the character of the problem situation, and to
explore our options as analysts to do meaningful additional research, taking knowledge
gaps as a point of departure. In this chapter, we go into more detail on what constitutes a
knowledge gap, we explain what types of relevant and researchable questions can be for-
mulated, we provide considerations in choosing appropriate research methods to answer
your research questions and we explain how to write a research plan.
7.1 Introduction
Problem analysis has revealed what is important for actors. This ‘relevant part of the real
world’ is what we call the system of interest. The models used to demarcate this system,
especially the multi-actor system diagram, represent assumptions that you, the policy
analyst, have made about this system: assumptions about the present and future state of
the system, about chains of cause and effect, about actions and events that may change
the system state through these causal chains, and – last but not least – about how the
various actors perceive the system of interest and their own position, about their interests
and goals, and about the strategies they may adopt to achieve those goals.
If you have been thorough in your analysis, these assumptions will be based on ‘best
available knowledge’: empirical evidence on the current system state, scientifically sound
theories that explain the causal relations, and best practice models for projecting the
outcomes of actions and external events beyond the control of the actors involved. But
as pointed out in Section 6.4, you may discover ‘blind spots’ in your analysis (new actors,
issues, solutions or events that introduce new factors and relations), and some of your
assumptions may be uncertain ‘best guesses’ because science offers no empirical evi-
dence or sound theories on particular aspects of the system of interest that you have
demarcated. For example, data on the specific geographic area, social group or industrial
activity may be lacking, or theories and models may be too general to provide reliable
projections on the appropriate spatial and/or temporal scale.
Such ‘knowledge gaps’ might be filled by performing additional research. However,
research is costly, and takes time, so you will always need to prioritize knowledge gaps:
what is really ‘need to know’, and what is merely ‘nice to know’. You will have to convince
your client that the additional research you would like to do is worthwhile. Hence this
chapter: The Research Plan. A research plan identifies the most pressing uncertain but
researchable assumptions for your client, and then makes a convincing case on how the
validity of these assumptions can be established through scientific research.
The research plan should show that you know what you are looking for, and that you
know how the results will contribute to the broader problem-solving process. A research
plan therefore should answer the following questions:
153

Research
plan
Policy AnAlysis of Multi-Actor systeMs
– Why? Research relevance. The research plan specifies the knowledge gaps that are
addressed, and shows how the research results will contribute to problem-solving.
– What? Research scope. The research plan defines the research questions that will be
answered in order in order to acquire the knowledge which can fill the knowledge gaps.
– How? Research process. The research plan specifies the research methods that will be
employed in order to answer the research questions, and justifies why these methods
are appropriate for answering the research questions.
– When and who? Research planning. The research plan addresses the operational plan-
ning of the activities needed to conduct the research process, in terms of time, deliv-
erables and people to be involved, in order to show that the research is feasible.
In the following sections we will first further develop the notion of ‘knowledge gap’, and
then show how you can operationalize it by formulating research questions, choosing
appropriate methods and planning your research to meet time and resource constraints.
7.2 Why? – Knowledge Gaps
The first question to be answered is, ‘why’? Why is research needed? What knowledge is
currently lacking, and how will this knowledge support problem-solving? This justification
process is the first part of a research plan, and it builds directly on the main findings of your
problem analysis: you discovered a number of knowledge gaps that need to be addressed.
These knowledge gaps form the crucial justification for performing the research described
in the research plan. A knowledge gap identifies which knowledge is not yet practised
(‘expertise’, ‘know-how’) or provided in the scientific literature (‘evidence’, ‘theory’), but
relevant for the policy process and amenable to scientific enquiry. The latter condition
excludes philosophical questions (‘What is the purpose of life?’, ‘Does God exist?’) and
ideological theses (‘Individual freedom is the basis for prosperity.’) as knowledge gaps.
Even though such assumptions can be rigorously debated, they cannot be ascertained by
what we consider to be a scientific method.
You can identify knowledge gaps by critically questioning the system models and actor
models that you have used to define and demarcate the problem, by performing a thor-
ough literature review, and/or by discussing the issue with stakeholders. The type and
urgency of the knowledge gaps you discover can vary widely, depending on the phase in
the policy life cycle (Van Daalen et al., 2002). When you consider the four subprocesses in
the policy process as depicted in Figure 1.1, you will see that these subprocesses will give
rise to different questions:
1. Agenda setting: When a policy issue is discovered and put on the agenda by some
stakeholder group, this raises questions like ‘who are affected?’, ‘how many?’, ‘in what
ways?’, ‘how strongly?’ and ‘how soon?’ The factual knowledge provided by research
will inform the political debate on’ the urgency of the problem (cf. the decision tree in
Figure 2.1).
2. Decision-making: When analysts, often in consultation or collaboration with stakehold-
ers, investigate a policy issue, and explore measures that could mitigate or resolve it,
this raises questions about causal mechanisms in the system of interest. For example,
‘how much does A contribute to B?’, ‘what if C continues to increase?’, ‘how likely is
that to happen?’, ‘how effective will measure D be?’ and ‘what will be the costs and
other externalities?’ By filling this type of knowledge gap, research facilitates design
154

nalp
hcraeseR
7 The researCh Plan
and ex ante appraisal of alternative policies along the lines of systems analysis as
described in Chapter 3.
3. Policy implementation: When the political debate converges to the point that a particu-
lar policy is embraced, this policy must be translated into some institutional arrange-
ment that legitimizes its implementation (cf. Section 4.4.3). This raises questions
about formal procedures and accountability, for example ‘who should be eligible for
financial aid?’, ‘under which conditions?’, ‘who will decide on applications?’ and ‘how
will disputes be resolved?’, and also questions about efficiency, like ‘how should we
allocate budgets?’ and ‘how high will the transaction costs be?’ These questions may
be answered through applied research in fields like organizational science, law and
economics.
4. Policy impact: Assessing the impact of current policies raises not only questions like
‘how effective was measure A?’ and ‘what part of our target group have we reached?’,
but also questions like ‘is the present policy still effective?’ and ‘which adjustments
should be made?’ Research can fill this type of knowledge gap by providing perform-
ance indicators and instruments for monitoring, forecasting and periodic assessment
of performance indicators. When the problem appears to be solved, or other issues
become more urgent, stakeholder groups will raise questions like ‘do costs still out-
weigh benefits?’, ‘what if we stop?’ and ‘how well have goals been achieved?’ Ex post
evaluation research will allow lessons to be drawn from successful policies as well as
failures.
Evidently, the knowledge gap will also relate to the substance of the policy issue, e.g. flood
protection, irrigation, transport, crime prevention or social inequality. Substantive knowl-
edge is typically situated in a scientific discipline, so it makes sense to consider which dis-
ciplines might contribute relevant knowledge. Despite its image of ‘ivory tower’, academic
research is sensitive to societal needs (Fecher & Hebing, 2021), so you may also identify
relevant knowledge gaps by making a quick scan of recent publications in specific fields
of natural science and technology (e.g. hydrology, energy, logistics), behavioural sciences
(e.g. economics, sociology, history, criminology) and multidisciplinary fields of academic
research (e.g. political science, public administration, behavioural decision analysis). If
you have more time, you can identify knowledge gaps by using rigorous identification and
prioritization methods such as scoping reviews (Colquhoun et al., 2014), possibly com-
bined with stakeholder consultation (Gold et al., 2013).
The next step is then to elaborate the most relevant knowledge gaps so that you can
make a convincing argument to your client that it is not only desirable but also feasible to
obtain this knowledge.
7.3 What? – Research Questions
The second question to be answered is ‘what?’ What will be researched? This can be the
system of interest as a whole, but more typically you will want to study a specific phenom-
enon within this system. This phenomenon then is the object of your research. To crisply
define a knowledge gap, the main research question for your research plan should make
clear what this object of research is. To demonstrate that your main question is amenable
to scientific enquiry, you elaborate it in a series or hierarchy of sub-questions. These sub-
155

Research
plan
Policy AnAlysis of Multi-Actor systeMs
questions should reflect how the research can be decomposed into research activities
that, when performed successfully, will lead to an answer to the main question.
To achieve this, it is helpful to differentiate between categories of research questions.
The primary category comprises empirical questions, i.e. research questions that can be
answered through observation of some real-world phenomena. Within this broad cat-
egory, we discern descriptive questions, explanatory questions and relational questions.
Descriptive research questions serve to affirm assumptions about the past and present
state of the system of interest, for example: ‘what is the total annual consumption of
electricity of all EU countries?’, ‘has animal welfare improved significantly over the last
decade?’ and ‘how good is the water quality of the River Rhine?’ These questions will help
assess the extent to which the present situation differs from what your client finds desir-
able (cf. Section 3.3). The general form of a descriptive question is ‘what is the value of X?’
where X is a variable that represents a specific factor in the system of interest. Note that X
can also represent a criterion, e.g. the value of lost load (Schröder & Kuckshinrichs, 2015),
the highest number of large animals per hectare that is still considered acceptable or the
minimum level of dissolved oxygen required by some aquatic species.
Explanatory research questions serve to affirm assumptions about causal relations
between factors that you have identified in your system diagram (cf. Section 3.5). Although
the term ‘explanatory’ suggests that this type of question should be formulated as ‘why
does X change?’ or ‘what causes X to change?’, you are free to use different forms, for
example: ‘how will prices on the electricity spot market change when renewable power
generation capacity triples?’, ‘is biological farming good for animal welfare?’ and ‘what
part of the nitrogen and phosphate concentrations in the Rhine can be attributed to agri-
cultural practices?’ Note that each of these examples reflects that an explanatory question
addresses a causal relation between a dependent variable and one or more independent
variables, hence the general form: ‘how strongly is the value of Y affected by the value of
X?’, or even more precisely: ‘assuming that Y = f(X), what is the function f ?’ Here, Y is
the dependent variable, function f defines the causal relation X→Y, while the independent
variable X can be a vector (X, …, X ) that represents several factors in the system of inter-
1 N
est. Note that this abstraction does not exclude qualitative research questions, as X and Y
can be nominal variables, and f can be a logical proposition.
Relational research questions are similar to explanatory questions in that they question
whether factors in the system of interest relate to each other. The distinction is that they
do not assume that this relation is causal (Pearl, 2000). This type of question is relevant
when you try to find good proxies for factors of interest that cannot be measured directly
(Frost, 1979, cf. Section 3.3.2). Some examples are ‘(how) does regional electricity con-
sumption relate to population density?’, ‘do animals with elevated cortisol levels exhibit
more stressful behaviour?’ and ‘what water conditions relate to trout population size?’
Investigating such questions can help you cope efficiently with lacking data (demographic
data are often publicly available with high spatial resolution), provide an objective quan-
titative scale for a qualitative factor that is difficult to observe (cortisol levels as indicator
for stress) or single indicators for complex conditions (presence of fish as indicator for
water quality).
All empirical research questions have in common that the factors that are to be observed
must be clearly defined (otherwise they cannot be observed/measured). This condition is
generally true for physical quantities: variables such as electrical energy, the power gen-
156

nalp
hcraeseR
7 The researCh Plan
eration capacity of a wind turbine, cortisol levels and heart rates of cattle or the concentra-
tion of nutrients in water can be measured on standardized unit scales like ppm and g/l.
When well-established standards are lacking, this lack of clarity is part of the knowledge
gap, but cannot be resolved by posing empirical questions. When this is the case, you
should add sub-questions like ‘what is animal welfare?’ or ‘what standard for river water
quality is appropriate for this research?’ Such questions belong to the category of defini-
tional research questions, and answering them typically requires review and synthesis of
definitions used in the literature (cf. Hewson, 2003, on animal welfare), or a well-argued
selection of one particular standard from a larger set (cf. Tango & Batiuk, 2013, on water
quality).
Note that the subcategories of research questions do not relate to a specific purpose,
whereas your research will be prompted by specific knowledge needs of actors in a policy
process. When you look again at our examples of questions that may be raised in a policy
process (Section 7.2), they typically are empirical. Agenda setting will give rise to descrip-
tive questions that must lead to new factual knowledge about the system of interest.
Decision-making will typically give rise to explanatory questions, either evaluative (to iden-
tify the causes of the problem) or design oriented (to assess ex ante whether particular
measures will be effective). Policy implementation will raise design-oriented questions to
define efficient procedures and monitoring tools, while questions related to policy impact
will be a mix of descriptive questions and evaluative (ex post) explanatory questions like
‘how effective was the implementation of policy P to meet goal G?’
The last category we mention here comprises methodological research questions. Similar
to definitional research questions, methodological research questions become relevant
when science offers no well-established standards or best practices for measuring vari-
ables and/or the strength of the relations between these variables. This lack of method-
ological knowledge may be due not only to the novelty of a research field, but also to a
diversity of perspectives, as different scientific disciplines will favour different method-
ologies. Methodological questions generally have the form ‘how can X be (efficiently)
measured?’ or ‘which method is most appropriate to do A?’ In fact, you can see them
as ‘normal’ research questions that concern a special ‘system of interest’: your research
methodology. We will elaborate on methods in the next section, but should point out here
that you may also need to add methodological research questions when science offers a
wide range of standard methods for the same purpose (e.g. methods for statistical testing
of hypotheses, methods for preference elicitation or methods for time series analysis).
As you elaborate the main research question into more specific empirical, definitional
and methodological questions, you should also consider what is the most logical order
for these questions. A common practice is to present your sub-questions in an order
that reflects the phases in the research. For example, when your main research question
is ‘how will investments in large-scale variable renewable energy sources (vRES) affect
electricity markets?’, you can start with definitional sub-questions that focus on the clari-
fication of the key concepts, e.g. ‘what are vRES?’, ‘what makes vRES different from con-
ventional fossil-fuelled power plants?’ and ‘how do electricity markets function?’ Note
that questions that address the scope of your research, such as ‘what are the geographic
boundaries?’ and ‘what is the time frame?’, should already have been answered by your
definition of the knowledge gap.
Then you formulate empirical sub-questions to operationalize the relevant variables,
and the relation between independent variables (investments in vRES) and dependent
157

Research
plan
Policy AnAlysis of Multi-Actor systeMs
variables (market prices and producer surplus), e.g. ‘what are the average cost price and
market price of electricity, given the demand, the installed capacity of conventional power
plants and vRES assets, and seasonal conditions (wind speed, insulation)?’
Empirical questions that call for experimental research typically raise methodological
questions that relate to the implementation phase of your research, for example ‘what
confounding variables should be controlled for?’, ‘how many replications are required?’
and ‘what is an appropriate baseline scenario?’ Although it is good practice to raise meth-
odological questions down to this ‘nuts and bolts’ level, these details should not distract
from the more fundamental questions that will be addressed. Bear in mind that you can
also raise methodological questions later in your research plan, when you present the
research methods that you plan to use.
The main takeaway of this small example is that the context of a knowledge gap co-
determines how to address it: the concepts you use and the questions you pose should
connect to the knowledge that is already available, and the methods you choose should
comply with the established best practices in the scientific research community.
7.4 How? – Research Methods
The third question to be answered is ‘how?’ How will the research questions be answered?
This asks for research methods. A research method prescribes how a particular type of
research question can be answered in a way that is rigorous, transparent and reproduc-
ible. In practice, each sub-question may require its own specific research method or a
combination of methods.
Every research method comprises (1) a conceptual framework that provides a precise
and unambiguous terminology for detailing both the subject of enquiry and how it will be
studied, and (2) a step-by-step operating procedure with logically sound decision rules
that define – using the terminology provided by the conceptual framework – what the
researcher should do under various conditions. A research method is scientifically sound
when it precisely and consistently defines the meaning of concepts, and each step of its
procedure complies with acknowledged academic standards.
The term ‘research methodology’ generally refers to the study of research methods,
but you can safely use it to refer to the specific arrangement of methods that you plan
to use in your research. What research methods are suitable for answering a particular
research question not only depends on the type of question but also relates to its context,
i.e. the other sub-questions you have formulated for the main research question and the
methods you select to answer them. Your methodology must be internally consistent, i.e.
conceptual frameworks and procedures should not contradict each other. This is why we
speak of a research design (De Vaus, 2001). You can think of your methodology as if it is a
piece of engineering, an artificial system (Churchman, 1971; Simon, 1996) that you design
to produce an answer to your main research question. In this engineering metaphor, your
research methodology is like a big machine that you design to produce an answer to
your main research question, and the research methods you use to address specific sub-
questions then are like the moving parts of this machine.
In the following subsections we introduce – quite briefly – a selection of methods relat-
ing to the types of research question we distinguished in Section 7.3. Our aim here is to
show the methodological variety, to illustrate what makes a method scientifically sound,
to provide pointers to where you may look for appropriate methods, and to encourage you
158

nalp
hcraeseR
7 The researCh Plan
to be creative but also rigorous when adapting existing methods, or devising your own.
Outlining the premises and procedure for each method is beyond the scope of this chap-
ter, so we do this only selectively.
7.4.1 Methods for Definitional Enquiry
Methods in this category aim to clarify the meaning of concepts so that they can be used
to formulate assumptions. Note that this relates strongly to the methods for systems
analysis, actor analysis and scenario analysis discussed in Chapters 3, 4 and 5. Although
the strict conventions for graphical notation of concepts and relations may suggest other-
wise, these methods depend most heavily on natural language. The main challenge is to
choose the right words that capture the meaning of a concept, be it a factor, the interests
of an actor or the societal dynamics that drive external forces.
Not surprisingly, the basic method for achieving this is to scan the literature to find
how other people – not only researchers, but also your client and other stakeholders –
name and define factors of interest. When doing so, you may discover existing conceptual
frameworks that provide appealing categories of concepts. Such frameworks can be a
big help, but they may also introduce an a priori bias to your research. Bear in mind that
other researchers have developed their frameworks with a particular function in mind (cf.
Binder et al., 2013), and that this function could be incompatible with what you intend to
do.
If you want to conceptualize your research with a minimum of a priori concepts, you
may want to consider using ‘open coding’ as it is practised as part of the grounded theory
approach (Glaser & Strauss, 1999). This method provides a rigorous procedure for high-
lighting concepts and key phrases in texts (or other sources), grouping them in tentative
categories and reflecting on their meaning.
If your aim is to clarify concepts that represent complex ideas, such as ‘smart grids’,
‘natural behaviour of animals’ or ‘a natural river’, you can use basic linguistic methods
like giving examples or using analogies or metaphors, but you can also look into more
elaborate methods such as exemplar methodology (Bronk, 2012) and narrative methods
like storytelling (Moezzi et al., 2017).
As terms become meaningful only in relation to other terms, the general criterion for
validity of a conceptual model is that it is semantically coherent and consistent. For infor-
mal representations in natural language, the criterion will be consensus: people must
agree that the definitions make sense, and find that they use terms in the same meaning.
This also applies to formal representations of concepts, such as semantic networks and
ontologies, but these can be validated further by means of formal logic (Beers & Bots,
2009; Hinkel et al., 2014).
7.4.2 Methods for Descriptive Enquiry
Methods in this category aim to produce valid assumptions about properties of the object
of research. Descriptive methods are geared to measure the value of variables through
empirical observation. A variable is a property of some unit of observation. This can be
the object of research as a whole (e.g. a spot market for electricity such as the Amsterdam
Power Exchange), but more often the unit of observation is a specific entity type within
the system (e.g. a single producer or consumer). Measuring a variable entails that the
type and range of values it can have are clearly defined, and this entails that the variable
has a scale. This scale can be nominal, ordinal, interval or ratio. Table 7.1 provides some
159

Policy AnAlysis of Multi-Actor systeMs
illustrative examples. Note that the properties of the unit of observation can also be the
number entities or occurrences of discrete events within this unit of observation, such as
the number of households connected to a grid, the number of cattle in a region or the
number of trout that pass a fish ladder. Also note that the value of a variable can be a set
of entities, such as the list of Member States of the European Union.
Table 7.1  Examples of variables as properties of a unit of observation
| Unit of Observation | Property                  | Domain Scale and Range                | Unit  |
| ------------------- | ------------------------- | ------------------------------------- | ----- |
| High voltage cable  | Area                      | Ratio, 500–2500                       | mm2   |
|                     | Actual load               | Ratio, 0–1000                         | MW    |
|                     | Current carrying capacity | Ratio, 0–1500                         | A     |
|                     | Transmission type         | Nominal (AC or DC)                    | -     |
| Cow                 | Body mass                 | Ratio, 30–1500                        | kg    |
|                     | Milk yield                | Ratio, 0–60                           | l/day |
|                     | Breed                     | Nominal, ~1000 breeds, e.g. Aberdeen  | -     |
Angus, Blonde d’Aquitaine, Yurino,
Żubroń
| River          | Discharge                  | Ratio, 0–200,000       | m3/s  |
| -------------- | -------------------------- | ---------------------- | ----- |
|                | Tributaries                | Set of nominal         | -     |
| Point location | Latitude and longitude     | Ratio, 0–360           | deg   |
|                | Wind speed                 | Ratio, 0–35            | m/s   |
|                | Passing trout              | Integer                | -     |
| Country        | Unit transmission tariff   | Ratio, 0–30            | €/MWh |
|                | Stock of cattle            | Integer, 0–350 million | -     |
|                | Cultural heritage          | Nominal (narratives)   | -     |
|                | Environmental performance  | Ratio, 0–100           | -     |
index
| European Union | Member States | Set of nominal | -   |
| -------------- | ------------- | -------------- | --- |
|                | Energy policy | Nominal        | -   |
The observed values of variables are data. Data obtained on a set of entities or events
can be aggregated using descriptive statistics such as count, frequency (occurrence of
nominal scale values), sum, mean, minimum and maximum value, variance and standard
deviation. Such aggregation methods serve to measure variables representing proper-
ties of the encompassing unit of observation, for example the mean time between power
outages, the average price of electricity on the spot market, the hours per day that cows
spend ruminating or the daily variability in dissolved oxygen in water. Note that the restric-
tions on what logical and arithmetical operations are permitted on the scale of a variable
also limit how data on this variable can be aggregated.
Research plan
The general criterion for the validity of observation methods is that they comply with
the acknowledged standards of a scientific community, such as the International System
of Units. Note that this entails that a variable must be clearly defined before it can be
measured, and that this may raise additional definitional as well as methodological sub-
questions. The methods used in studies of cultural heritage (Piñeiro-Naval & Serra, 2019),
the environmental performance of countries (Hsu & Zomer, 2016) and the EU energy
policy (Eckert & Kovalevska, 2021) provide instructive examples of scientifically sound
methods for operationalizing complex qualitative variables.
160

nalp
hcraeseR
7 The researCh Plan
Factual assumptions are typically affirmed by repeated observation, e.g. by aggregat-
ing observations over a (large) sample, by using different survey questions to measure
the same variable or by means of triangulation in a case study (e.g. Ammenwerth et al.,
2003). These aggregation methods must also comply with acknowledged standards. For
example, the meaning of standard deviation as a measure for variability is (as the name
suggests) standard across scientific domains, but the definition of other variability mea-
sures such as volatility may vary across domains.
7.4.3 Methods for Relational Enquiry
Methods in this category aim to establish whether there exists a relation between a set of
variables. A relation between variables X and Y entails that a variation in the values of X
in some way corresponds to a variation in the values of Y. Note that this does not require
that X and Y are quantitative variables. The relation between qualitative variables such as
rules and regulations that structure an electricity market (X) and strategic opportunities
for energy suppliers (Y) can be investigated just as well as the relation between quantita-
tive indicators such as consumer surplus and investments in new power generation units,
but the research methods will be different.
When X and Y both have a nominal scale, relations can only be formulated as logical
propositions like ‘in context X we can expect to observe Y, whereas in context X we
1 1 2
expect to observe Y’. Ordinal scales allow propositions like ‘in contexts showing high
2
values of X we expect to observe low values of Y’. Quantitative scales allow propositions
like ‘X is proportional to Y’. When variables X and Y are both quantitative (and preferably
have a ratio scale), the extent to which variables X and Y are related can be measured using
standard indicators for covariation, typically covariance and correlation.
When you have no a priori assumptions about relations between variables, you can
induce them from observations. When you have quantitative data on a set of variables X,
1
…, X , you can construct a correlation matrix to see for which variable pairs (X, X) the
N i j
absolute value of their correlation coefficient is relatively high. If some or all variables have
nominal or ordinal scales, you can use classification methods such as logistic regression
to look for patterns that indicate covariation of variables.
Methods for affirming assumptions about relations between variables are called hypoth-
esis testing methods. The tentative proposition that a relation between variables X and Y
exists is the hypothesis, and the test consists of assessing how likely it is that the observa-
tion data obtained for X and Y could have been obtained if the relation between X and Y
would not exist. This test can be performed in many different ways (chi-square, Student-t,
ANOVA, etc.), and we refer to standard text books for guidance for selecting an appropri-
ate method.
7.4.4 Methods for Explanatory Enquiry
Explanatory research questions differ from relational research questions in that they seek
to establish a causal relation between dependent and independent variables. A causal
relation X → Y implies that a change in the independent variable X necessarily results in
a change in the dependent variable Y. For a relation to be causal, two more conditions
must be satisfied in addition to covariation as defined in the previous subsection: tem-
poral precedence and control for ‘confounding’ variables. Temporal precedence entails
that the change in Y always occurs before or simultaneously with the change in X. Control
for confounding variables means that the change in Y cannot be explained by changes in
161

Research
plan
Policy AnAlysis of Multi-Actor systeMs
variables other than X. In other words, when Y = f(X) and Y also co-varies with Z, then Z
must be part of X.
Because methods for answering explanatory research questions must verify that these
additional conditions are met, they are more elaborate. Experiments and surveys must be
designed such that potentially confounding variables are identified and controlled for, and
that observations of the system of interest permit control over time. Moreover, methods
should include mechanisms to verify that, when results suggest that a relation X → Y is
causal, this relation is not spurious, where spurious means that the observed covariation
between X and Y is actually the result of an underlying shared cause Z, i.e. X = g(Z) and
Y = h(Z), rather than Y = f(X).
Note once again that causal relations and methods for establishing them need not be
quantitative. For example, the case study method can be applied to construct qualitative
causal models. Such models will then have the form of historical narratives that give a
plausible explanation of a chronological chain of events by arguing how the actions of
actors follow logically from their motives as opportunities present themselves. Also note
that the scientific rigour of qualitative methods for explanatory enquiry can be tested, for
example by asking all interviewees whether they concur with the reconstruction and inter-
pretation of events, by actively soliciting counterfactual evidence by contrasting alterna-
tive narratives (as alternative hypotheses) or a combination of these.
Just as definitional relations form the core of conceptual frameworks, causal relations
form the core of theories. The classic example of a theory is Newtonian physics, which
defines a set of assumptions relating concepts like force, acceleration, mass, distance,
time and speed as mathematical relations, based on the assumption that force F causes
acceleration a of a mass m according to a = F/m. Likewise, economic theory assumes that
people, given the information they have, will opt for choices that maximize their utility. Do
not make the common mistake to present or refer to a conceptual framework as if it is a
theory. A framework can be used for description of (patterns in) system behaviour, but not
for explanation or prediction of this behaviour.
The focus on causality in research, especially in support of policy-making, is understand-
able: without theories, i.e. consistent sets of assumptions about causal relations between
factors, it would be impossible to determine what can be done to obtain a desired con-
sequence or to avoid an undesirable outcome. But exactly because policy-making relies
on causal assumptions, explanatory research meant to inform decision-making on a con-
troversial issue such as climate change mitigation will be scrutinized and challenged, as
exemplified by Goulet Coulombe and Göbel (2021).
7.4.5 Using Models in Research
The examples we selected in the previous subsections show that all methods involve
representing some parts or aspects of the system of interest by means of a model of
some form: qualitative or quantitative, informal verbal narratives or formal mathematical
equations, tabular data, diagrams, computer code, games or some combination of these.
Definitional models represent the meaning of terms, and hence resemble dictionaries or
encyclopaedias, or definitional equations such as, for example, the one that defines the
economic concept of weighted average cost of capital:
162

nalp
hcraeseR
7 The researCh Plan
E D
WACC = ∙ Re + ∙ Rd∙ (1− Tc),
V V
where E is the market value of the firm’s equity, D is the market value of the firm’s debt,
V = E + D, Re is the cost of equity, Rd is the cost of debt and Tc is the corporate tax rate.
Descriptive models describe the state of some part or aspect of a system. They may be
qualitative (‘the water is clear’) or quantitative (‘the water temperature is about 10 degrees
Celsius’, or ‘Tw = 283 K’), and this can be generalized to time series and more complex
data sets. Descriptive statistics such as sum, mean, mode and standard deviation that
aggregate data sets also are descriptive models because they pertain to a single variable.
Relations between variables can be represented in many ways, e.g. graphically as causal
relation diagrams (a qualitative conceptual model) or as scatter plots with a regression
line (a quantitative empirical model), but also in tabular form as in Table 2.1 (a qualitative
conceptual model) or as a correlation matrix (a quantitative empirical model). Note that
the equation for WACC defines a relation between variables in a similar way as the price-
demand function P = d(Q) = q − a∙Q − b∙Q2, whereas the former is a definitional model
0
and the latter represents a descriptive relation where the parameter values q , a and b
0
can be obtained by performing quadratic regression on a data set with paired empiri-
cal observations of price P and demand Q. Then also note that this equation represents
an observed pattern (demand goes down when price goes up and vice versa), whereas
a = F/m represents a causal relation (exerting a force on a mass will cause it to accelerate).
Knowledge of the relations between the variables in a system permits the construction
of models that can simulate the dynamic behaviour of this system. Such simulation mod-
els can be used as a substitute for the real object of research in cases where doing empiri-
cal research on the real object is too costly or too risky. Evidently, the validity of research
results obtained with simulation models depends on how well these models represent the
real object of research.
Simulation models typically comprise numerous equations, but the spectacular increase
in computing power in the past decades has enabled modelling at large scale and in
high detail. Constructing simulation models that are logically sound and empirically valid
raises methodological questions, and this has led to a variety of modelling methodologies
that provide alternative conceptual frameworks and working procedures. Some examples
are the applied general equilibrium modelling approach (Ginsburgh & Keyzer, 2002), the
system dynamics approach (Forrester, 1961) and the agent-based modelling approach
(Epstein & Axtell, 1996). If you look into these methodologies, you will find that, despite
fundamental differences in conceptual framework, they rely on the same criteria for sci-
entific validity: sound logic of the model structure, and consensus within the academic
community on the interpretation of variables, on the theories (and their limitations) that
underlie the causal assumptions, and on the measures for goodness of fit between model
behaviour and empirical data.
Note that simulation models need not be quantitative nor computer based. Thought
experiments and scenario studies that reason about potential outcomes of policies or
impacts of events, and serious games designed to observe how players can interpret regu-
lations strategically also are simulation models for answering ‘what if …?’ questions.
A model can be the final result of your research when it represents the system of inter-
est in a way that answers the main research question (e.g. a set of stories that exemplify
163

Research
plan
Policy AnAlysis of Multi-Actor systeMs
different stakeholder views on a policy issue), but more often it will be an intermediate
result that you then use to answer specific sub-questions of the main research question.
A typical sequence could be that you develop a quantitative simulation model that opera-
tionalizes your system diagram (cf. Section 3.5), use this simulation model to assess the
impacts of different alternatives under a range of scenarios, elicit stakeholder preferences,
arrange impacts and preferences in a multi-criteria, multi-scenario decision model which
you then use to rank alternatives according to a robustness metric, such as least regret (cf.
Kim & Chung, 2014 for a more elaborate research design).
When designing your research, it helps to think of models as functional components
of your methodology. Qualitative and quantitative models can reinforce each other when
developed jointly (Hérivaux et al., 2021). Note that the function of a model does not follow
one-to-one from its type or form. Decision models can be used as components of a simu-
lation model, e.g. to represent bidding strategies and market clearing (Pozo et al., 2013),
but a simulation model can also be used as component of a decision model, e.g. when
using robust optimization of policies under deep uncertainty (Bartholomew & Kwakkel,
2020). A simulation model can be part of a serious game, but a serious game can also be
used as a simulation model, which in turn can be used to perform a variety of functions in
policy research (Bots & Van Daalen 2007).
7.4.6 Data Management in Research
Empirical research will require data as the basis for analysis. These data requirements
typically follow from the research questions and the methods and models you have cho-
sen for answering them. These data can be collected as part of the research or they can
be obtained from existing sources and databases. In most cases, data needs are consid-
erable, and data collection may well be the most time-consuming step in the research.
Therefore, the research plan should make clear that data are available (by mentioning
specific sources, such as archives, reports and databases) or can be obtained (by specify-
ing data collection methods such as interviews, surveys, longitudinal studies or real-time
remote sensing).
In some cases you may also be required to specify how data will be managed, stored and
made available during the study, how data will be shared upon completion of the research
project and how you will mitigate the risk of data loss, data breach or other threats. Some
data may be confidential, for example because they allow the identification of living indi-
viduals, because they are commercially sensitive (e.g. cost prices or patentable research
results) or because they relate to national security. For such data, your research plan
should also specify how you will obtain permission to use it (e.g. a process of informed
consent) and how you will ensure that only authorized people have access to the data.
7.4.7 Involving People in Research
Research will always require people. The obvious minimum is a single researcher (you)
performing desk research, but more likely you will involve other people, and in different
capacities: fellow researcher, external advisor, reviewer, domain expert, practitioner, par-
ticipant in an experiment, respondent to a survey, interviewee, etc. Like models, people
also are functional components in your research design, so you must consider what quali-
ties these people should have to be ‘fit for purpose’. Experts should not only be knowl-
edgeable, but also be acceptable, i.e. be perceived by your client and other stakeholders as
authoritative and impartial (or at least non-controversial) in their views. When you select
164

nalp
hcraeseR
7 The researCh Plan
participants, you will want them to represent a particular stakeholder or social group, pos-
sibly in both senses of the word: to have similar perceptions, preferences and behaviours,
and also to speak on behalf of their constituency. When you select your subjects for an
experiment or for a survey, you will also think of incentives that may increase response
rates. In all cases, you should be aware of your responsibilities as a researcher, consider
how your research design will affect the people you involve and how you will communicate
with them. This communication protocol may be an important part of your research plan
(Barreteau et al., 2010).
7.5 When? Who? – Research Planning
Different types of knowledge needs may call for different research approaches, and some
will be much more elaborate and time-consuming than others. When you write a research
plan, you must consider the availability of time and other resources: research facilities,
brainpower, and of course money. The purpose of making an operational research plan-
ning is twofold: (1) to assess the feasibility of your research plan and (2) to convince your
client that the research will deliver valuable results.
A research planning is quite similar to a recipe for a cake: it specifies the type of cake
(research deliverables), the required ingredients (existing data and models, subjects)
and utensils (experts, lab facilities, monitoring systems, software tools), the intermedi-
ate products (observation data, models, results from experiments), and all the necessary
activities in a logical order and with their estimates of how much time they will take.
By research deliverables we mean research results that are consolidated in a specific
form. The content of deliverables follows from your research questions, but not their form.
Typical research deliverables are reports, but your client may want to have policy briefs,
i.e. compact documents that present research and recommendations in plain language,
and draw clear links to policy issues and options. Infographics and short video clips that
can be posted on social media can serve to reach a much broader audience. Other deliv-
erables such as observation protocols, data sets and models can enhance transparency
and reproducibility, while conference presentations and articles in academic journals can
affirm the scientific status of the research.
The methods that you have selected and/or developed should suffice to identify the
research activities that need to be planned. You can scan related literature to obtain time
estimates for these activities, but do make use of practical experience by consulting with
experts and peers. Standard project planning techniques like the critical path method
(CPM) can help you organize activities in time, assess risks and build in slack (Riol &
Thuillier, 2015). Position deliverables smartly in time to prevent peaks in workload. Keep in
mind that sharing intermediate results can help to keep the confidence of your client and
the commitment of other participants.
Knowledge, and in particular know-how, resides in people, so your plan should not only
specify what will be done and when, but also by whom. This relates not only to research-
ers, but also to subjects, participants, advisors, external reviewers and supporting staff.
Iterate through your planning to verify that your research team has all the required compe-
tences. Try to obtain intrinsic commitment from experts, advisors and reviewers based on
genuine interest in the research. Such commitment combined with good reputation and
past performance (also as a team) can lend more credibility to your plan.
165

Research
plan
Policy AnAlysis of Multi-Actor systeMs
Summarize your planning in a form that is communicative. A well-constructed Gantt
chart provides an overview of research activities and their planning in time, and can high-
light important events (deliverables) as milestones. Finally, estimate what funding you
need for the proposed research. Most likely, human resources will constitute the largest
cost item on your budget, but you should also consider what facilities you may need. Even
if you require no special lab facilities or computational resources, the cost of more mun-
dane things like meeting places, catering and travel expenses may still be considerable.
7.6 Conclusion
Evidently, all the effort you have put into your research plan will be in vain unless your
client decides to commission the proposed research. That is why it is crucial to make a
convincing case for the research you propose. Bear in mind that your client is probably
not interested in scientific research, or even in policy analysis. Your research plan will be
interesting only when it is made crystal clear to your client that the knowledge that will
be developed will be useful. First and foremost, your client must be convinced that this
knowledge will in some way allow for better decision-making. It is up to you to demon-
strate what issue is at stake, what decisions need to be made and what your client and/or
other actors should know to make well-informed choices. If you succeed, then you must
also convince your client that your research will effectively provide relevant knowledge.
With this final section, we intend to provide some additional guidance for developing a
research plan.
A good research plan starts with an introduction of no more than one page that
(1) outlines the policy problem, highlighting specific societal needs and recent develop-
ments that have brought this problem onto the political agenda; (2) characterizes the pol-
icy arena by naming and positioning the most relevant actors in this arena; (3) diagnoses
the current state of the policy process in terms of competing interests and interdependen-
cies between key players; and (4) ends by framing a decision as a dilemmatic choice that
your client will soon have to make.
Assuming that your problem diagnosis convinces your client of the relevance and
urgency of this decision, you then focus on what knowledge your client will need to make
a wise decision. If possible, refer to what is presently considered as best practice in similar
situations, and then motivate why this ‘best available knowledge’ does not suffice for the
decision at hand. Be succinct. If you identify multiple knowledge gaps, it can help to pres-
ent them in order of increasing relevance, and end with the most crucial gap. This should
lead seamlessly to the main research question of your research plan. Then presenting your
sub-questions in logical order should suffice to clarify the objective and scope of your
research.
For the following pages of your research plan, your primary concern is its credibility. To
demonstrate that your research will provide valid answers to the formulated questions,
the methods you propose must be scientifically sound, and your selection must be well
argued. Make sure that you do not embarrass yourself by presenting frameworks as theo-
ries, or software tools as methods. Where possible, refer to research projects that show
successful application of similar approaches and methods. Do not hesitate to make prag-
matic choices to cope with time pressure or other resource constraints, but make your
trade-offs explicit. While presenting your methodology, focus on why it is ‘fit for purpose’
and do not elaborate in detail; it is better to show your methodological proficiency by
166

nalp
hcraeseR
7 The researCh Plan
providing operational details when you present the planning of research activities. Then
double-check that the methods section and planning section of your research plan are
consistent. This goes two ways: the research activities should follow the methodology, but
also be feasible within time and budget constraints, or your plan loses credibility.
In the final part of your research plan, you focus on results. Here, your aim is to show
that the research outcomes will indeed fill the knowledge gap that you identified in the
introduction. This does not mean that you have to predict the answers to your research
questions, but you should be able to explain how the answers that you will produce will
affirm assumptions that are presently uncertain, but crucial for making wise decisions.
After this review of expected conclusions, also add a paragraph in which you summarize
the most important research deliverables (e.g. reports, policy briefs) and specify how and
when you will make them available, and to whom.
By anticipating how the research results will be used, you can not only improve your
arguments why your client should commission the research, but also strengthen some
weak points in your research plan. As a quick check, you can reflect on the ambition level
that you have for the actual utilization of the deliverables using the seven-point scale
defined by Knott and Wildavsky (1980). The lowest utilization level is reception (your cli-
ent accepts your deliverables and pays the bill), followed by cognition (your client reads
your reports and understands the conclusions) and then reference (the knowledge actually
changes your client’s views and this shows in how your client communicates with other
actors). Bear in mind that sound methods and valid results alone do not suffice even to
reach these lower levels of utilization. You will also have to give serious thought to effec-
tive ways of presenting your research and its outcomes.
The more ambitious utilization levels are effort (your client tries to act on your recom-
mendations or convince other actors to do so), adoption (the knowledge actually influ-
ences the outcomes of the policy-making process), implementation (the knowledge is
embedded in standards and procedures for operational processes) and finally impact
(this implementation leads to changes that are favourable for your client). To attain these
higher levels, you will have to think more deeply about how you can improve your research
plan so that the results will indeed be ‘actionable’ for your client.
Revisiting your choice of research questions and methods, and also the people you plan
to involve (as co-researchers, experts or reviewers, but also as participants or subjects)
from this ‘actionability’ perspective, will help you make your research plan better and
more convincing. It is good practice to add a paragraph to your research plan where you
outline through what follow-up actions your client can make best use of the results. While
making such recommendations, consider not only the limitations of the research, but also
how this research will be perceived by other actors in the policy arena. For all your efforts
to meet scientific standards, your definitions of concepts and your choice of theories and
methods can always be challenged by stakeholders if your conclusions do not align with
their views. Such opponents may try to discredit your research, portraying you as a tech-
nocrat, a back-seat driver or a hired gun (Mayer et al., 2004, p. 185). Anticipating their
criticism may help you make strategic recommendations as to how your client can counter
or forestall it.
Finally, you will want to verify that your research plan meets common standards for this
type of document. Always provide an abstract that summarizes the knowledge need, the
main research question, and the method, and make sure that your sources are well refer-
enced. You may also be required to provide some form of risk assessment in which you
167

Research
plan
Policy AnAlysis of Multi-Actor systeMs
identify potential hazards and ethical implications of your research, and specify how these
concerns are addressed.
7.7 Takeaways
– A research plan should make clear that the proposed research will produce knowledge
that your client needs to advance the policy decision-making process.
– The main research question and its elaboration in sub-questions must detail your
client’s most urgent knowledge need; the associated research methodology must
then demonstrate that each question can be answered through scientific enquiry. This
entails that the proposed research should uphold in peer review.
– A research method comprises a conceptual framework and an operating procedure
that produces an answer to a research question. A method is scientifically sound when
it precisely and consistently defines the meaning of concepts, and each step of its pro-
cedure complies with acknowledged academic standards.
– Models can perform multiple functions as components of your research methodol-
ogy: they can define the meaning of concepts, and how these can be observed empiri-
cally; they can describe the state of a system in terms of (aggregated) empirical obser-
vations; and they can define relations between variables, either as a hypothesis (to be
tested empirically) or as a substitute for the real system (to study its behaviour under
various conditions).
– A research plan must be a persuasive text. From the start, it must captivate the atten-
tion of your client, and then inspire confidence that the research is useful, that its
design is scientifically sound and practically feasible, and that results will be delivered
on time and merit the expense.
References
Ammenwerth, E., Iller, C. & Mansmann, U. (2003). Can Evaluation Studies Benefit from
Triangulation? A Case Study. International Journal of Medical Informatics, 70(2-3), 237-
248. https://doi.org/10.1016/S1386-5056(03)00059-5.
Barreteau, O., Bots, P. W. G. & Daniell, K. A. (2010). A Framework for Clarifying
“Participation” in Participatory Research to Prevent Its Rejection for the Wrong
Reasons. Ecology and Society, 15(2), 1-22.
Bartholomew, E. & Kwakkel, J. H. (2020). On Considering Robustness in the Search
Phase of Robust Decision Making: A Comparison of Many-Objective Robust Decision
Making, Multi-Scenario Many-Objective Robust Decision Making, and Many Objective
Robust Optimization. Environmental Modelling & Software, 127, 104699. https://doi.
org/10.1016/j.envsoft.2020.104699.
Beers, P. J. & Bots, P. W. G. (2009). Eliciting Conceptual Models to Support
Interdisciplinary Research. Journal of Information Science, 35(3), 259-278. https://doi.
org/10.1177/0165551508099087.
Binder, C. R., Hinkel, J., Bots, P. W. G. & Pahl-Wostl, C. (2013). Comparison of
Frameworks for Analyzing Social-Ecological Systems. Ecology and Society, 18(4), 26.
https://doi.org/10.5751/ES-05551-180426.
168

nalp
hcraeseR
7 The researCh Plan
Bots, P. & Van Daalen, E. (2007). Functional Design of Games to Support Natural
Resource Management Policy Development. Simulation & Gaming, 38(4), 512-532.
https://doi.org/10.1177/1046878107300674.
Bronk, K. C. (2012). The Exemplar Methodology: An Approach to Studying the Leading
Edge of Development. Psychology of Well-Being: Theory, Research and Practice, 2(5).
https://doi.org/10.1186/2211-1522-2-5.
Churchman, C. W. (1971). The Design of Inquiring Systems: Basic Concepts of Systems and
Organization. New York: Basic Books, Inc.
Colquhoun, H. L., Levac, D., O’Brien, K. K., Straus, S., Tricco, A. C., Perrier, L., Kastner,
M. & Moher, D. (2014). Scoping Reviews: Time for Clarity in Definition, Methods, and
Reporting. Journal of Clinical Epidemiology, 67(12), 1291-1294. https://doi.org/10.1016/j.
jclinepi.2014.03.013.
De Vaus, D. (2001). Research Design in Social Research. London: Sage.
Eckert, E. & Kovalevska, O. (2021). Sustainability in the European Union: Analyzing the
Discourse of the European Green Deal. Journal of Risk and Financial Management,
14(2), 80. https://doi.org/10.3390/jrfm14020080.
Epstein, J. M. & Axtell, R. L. (1996). Growing Artificial Societies: Social Science From the
Bottom Up. Washington: Brookings Institution Press.
Fecher, B. & Hebing, M. (2021) How Do Researchers Approach Societal Impact? PLoS
ONE, 16(7), e0254006. https://doi.org/10.1371/journal.pone.0254006.
Forrester, J. W. (1961). Industrial Dynamics. Cambridge, MA: MIT Press.
Frost, P. A. (1979). Proxy Variables and Specification Bias. The Review of Economics and
Statistics, 61(2), 323-325. https://doi.org/10.2307/1924606.
Ginsburgh, V. & Keyzer, M. (2002). The Structure of Applied General Equilibrium Models.
Cambridge, MA: MIT Press.
Glaser, B. G. & Strauss, A. L. (1999) The Discovery of Grounded Theory: Strategies for
Qualitative Research. New York: Routledge. https://doi.org/10.4324/9780203793206.
Gold, R., Whitlock, E. P., Patnode, C. D., McGinnis, P. S., Buckley, D. I. & Morris, C.
(2013). Prioritizing Research Needs Based on a Systematic Evidence Review: A Pilot
Process for Engaging Stakeholders. Health Expectations, 16, 338-350. https://doi.
org/10.1111/j.1369-7625.2011.00716.x.
Goulet Coulombe, P. & Göbel, M. (2021). On Spurious Causality, CO , and Global
2
Temperature. Econometrics, 9, 33. https://doi.org/10.3390/econometrics9030033.
Hérivaux, C., Vinatier, F., Sabir, M., Guillot, F. & J. D. Rinaudo (2021). Combining
Narrative Scenarios, Local Knowledge and Land-Use Change Modelling for Integrating
Soil Erosion in a Global Perspective. Land Use Policy, 105, 105406. https://doi.
org/10.1016/j.landusepol.2021.105406.
Hewson, C. J. (2003). What Is Animal Welfare? Common Definitions and Their Practical
Consequences. The Canadian Veterinary Journal, 44(6), 496-499.
Hinkel, J., Bots, P. W. G. & Schlüter, M. (2014). Enhancing the Ostrom Social-Ecological
System Framework Through Formalization. Ecology and Society, 19(3), 51. https://doi.
org/10.5751/ES-06475-190351.
Hsu, A. & Zomer, A. (2016). Environmental Performance Index. Wiley StatsRef: Statistics
Reference Online, 1-5. https://doi.org/10.1002/9781118445112.stat03789.pub2.
Kim, Y. & Chung, E. S. (2014) An Index-Based Robust Decision Making Framework for
Watershed Management in a Changing Climate. Science of the Total Environment, 473-
474, 88-102. https://doi.org/10.1016/j.scitotenv.2013.12.002.
169

Research
plan
Policy AnAlysis of Multi-Actor systeMs
Knott, J. & Wildavsky, A. (1980). If Dissemination Is the Solution, What Is the
Problem? Knowledge: Creation, Diffusion, Utilization, 4, 537-578. https://doi.
org/10.1177/107554708000100404.
Mayer, I. S., Van Daalen, C. E. & Bots, P. W. G. (2004). Perspectives on Policy Analysis:
a Framework for Understanding and Design. International Journal of Technology, Policy
and Management, 4(2), 169-191. https://doi.org/10.1504/IJTPM.2004.004819
Moezzi, M., Janda, K. B. & Rotmann, S. (2017) Using Stories, Narratives, and Storytelling
in Energy and Climate Change Research. Energy Research & Social Science, 31, 1-10.
https://doi.org/10.1016/j.erss.2017.06.034.
Pearl, J. (2000). Causality: Models, Reasoning, and Inference. New York: Cambridge
University Press.
Piñeiro-Naval, V. & Serra, P. (2019). How Do Destinations Frame Cultural Heritage?
Content Analysis of Portugal’s Municipal Websites. Sustainability, 11(4), 947. https://
doi.org/10.3390/su11040947.
Pozo, D., Sauma, E. E. & Contreras, J. (2013). A Three-Level Static MILP Model for
Generation and Transmission Expansion Planning. IEEE Transactions on Power Systems,
28(1), 202-210. https://doi.org/10.1109/TPWRS.2012.2204073.
Riol, H. & Thuillier, D. (2015). Project Management for Academic Research Projects:
Balancing Structure and Flexibility. International Journal of Project Organisation and
Management, 7(3), 251-269. https://doi.org/10.1504/IJPOM.2015.070792.
Schröder, T. & Kuckshinrichs, W. (2015). Value of Lost Load: An Efficient Economic
Indicator for Power Supply Security? A Literature Review. Frontiers in Energy Research,
3. https://doi.org/10.3389/fenrg.2015.00055.
Simon, H. A. (1996). The Sciences of the Artificial (3rd ed.). Cambridge, MA: MIT Press.
Tango, P. J. & Batiuk, R. A. (2013). Deriving Chesapeake Bay Water Quality Standards.
Journal of the American Water Resources Association, 49(5), 1007-1024. https://doi.
org/10.1111/jawr.12108.
Van Daalen, C. E., Dresen, L. & Janssen, M. A. (2002). The Roles of Computer Models
in the Environmental Policy Life Cycle. Environmental Science & Policy, 5(3), 221-231.
https://doi.org/10.1016/S1462-9011(02)00040-0.
170

repap
eussI
8 Preparing an Issue Paper
Issue papers are written for a client and intend to support the client in addressing or even
solving the problem. With that aim in mind, the authors of the issue paper present the
problem as they have framed it plus a rationale for follow-on activities. Typically, the issue
paper includes a ‘plan of action’ (Figure 1.2) such as a proposal for further research, for a
workshop with stakeholders, for a mediation initiative, etc.
The value of an issue paper lies not in the presentation of new knowledge but in the
synthesis of the gathered insights. First, authors collect information about the problem
– facts, assumptions and perceptions – from a multidisciplinary, multi-stakeholder per-
spective with attention for uncertainty and future developments, for qualitative analyses.
Sources of information are the client, other stakeholders, and (scientific) literature and
other media. Then, the collected information is analysed with methods and techniques
presented in the previous chapters. In this chapter, we will discuss how issue papers may
be written and formatted.
Text box 8.1 Positioning of client and analyst before commissioning an issue paper
Client Hi, I am so glad that we can talk. I need to hear your ideas about the following.
My organization is trying to deal with a rather difficult problem situation, problem
P. We really feel an urgency to do something, and possibly solve the problem. This
won’t be easy since it is kind of a wicked situation and there are quite a few external
parties involved, some public, some private. And we are quite uncertain about what
the future might bring.
Analyst I understand. Now how might I be of assistance in the matter?
Client Well, my organization wants to decide what our next step ought to be and I need to
draw a plan for that. I have some budget to make this plan, but I am not sure that I
have enough insight into the problem situation, let alone how to address it.
Analyst W ell, it sounds like you need somebody to analyse the situation for you or with you.
I can do that and also write a proposal as to how your organization might want to
proceed.
Client Y eah, I think this is what I need. A good analysis might help convince my
organization to act even though there is quite some uncertainty still.
Analyst I guess you have called me because I have expertise on problems like problem P.
How about if I analyse your particular situation, step by step, and develop a proposal
for further action based on my diagnosis? My final product will be a so-called issue
paper. You can use that in the communication with your and other organizations.
Client L et me tell you a bit more about problem P so that you can indicate how you might
proceed and how much time this will take. And then tell me what you need to be able
to deliver such an issue paper.
171

Issue
paper
Policy AnAlysis of Multi-Actor systeMs
The building blocks for issue papers have been discussed in the previous chapters of
this book: a well-structured, original problem statement; a system diagram that is drawn
from a multi-stakeholder perspective and its interpretation; an analysis of the stakeholder
arena; and insight in important, uncertain future developments in either the system or its
context (Chapters 3, 4 and 5). These building blocks, the results of the partial analyses, are
used to characterize the problem situation, meaning that the problem is framed or char-
acterized in such a way that it can provide a rationale for follow-up actions that the client
might take (Chapter 6). Proposals for follow-on activities are to be included with the issue
paper and written according to the guidelines in Chapter 7.
In this chapter, we first address the role of issue papers in the practice of policy analysis.
Next, we present a list of eight key elements of issue papers and describe the purpose of
the individual chapters. The framed problem is a key element of an issue paper and the
problem frame is highlighted with a storyline (Section 8.3). Issue papers must be infor-
mative, convincing, consistent and clear, and written fort the client. In Section 8.4, we
outline how the different chapters of an issue paper may be prepared. Students of policy
analysis may use the list with questions at the end of this chapter to self-assess their work
and improve it.
8.1 Role of an Issue Paper in Policy Analysis
Policy analysts typically write ‘issue papers’ to inform a problem owner, or commissioner
of a study, of their findings (Checkland, 1985; Dunn, 1994). Quade (1989) describes an
issue paper as ‘an approach to formulating a problem’. Many issue papers have been
written to provide ‘a vehicle for quick dissemination intended to stimulate discussion in a
policy community’ (RAND Corporation, n.d.). We prefer to take the concept ‘issue paper’
one step further than communicating results of a problem exploration. An issue paper is
not merely a report on what has been done; it includes a proposal for further action also
(Thissen & Walker, 2013).
Issue papers provide a systematic exploration of the problem, at a depth sufficient to
give the reader a good idea of its dimensions and the possible scope of the solution, so
that it might be possible for the management to conclude either to do nothing further or
to commission a definitive study looking toward some sort of action recommendation.
(Quade, 1989: 72)
With that goal in mind, analysts detail their vision of the problem: they present key results
of a problem analysis from a multi-stakeholder perspective and make suggestions to the
client or stakeholders to decide on the next step towards solving their problem. Follow-on
activities will depend on the problem situation, the phase in the policy cycle, knowledge
gaps and the role perception of the analyst (see Chapter 6).
Issue papers are tools that help to sketch a problem and its context, and to distinguish
the main issues from the side issues. Issue papers force analysts to indicate next actions
in addressing a problem situation and to formulate what Fujimura (1987) calls ‘do-able
problems’: solvable problems and/or researchable questions. The real challenge for the
author/policy analyst lies in this shift in focus from analysis to a proposal for action. The
policy analyst should communicate this shift properly to the client and the format of an
issue paper should support this communication.
172

repap
eussI
8 PreParIng an Issue PaPer
For the reader, and perhaps potential client, the issue paper is a document that gives
insight as to how the analyst is going to organize the follow-up project, what activities will
be undertaken and how it would contribute to solving the problem. Also, the paper reveals
the approach and analytical capacity of the analysts and functions as a showcase of their
capabilities. The quality of the issue paper is expected to play a role in the client’s decision
to award or deny the contract to conduct the proposed study or project.
In this chapter, for practical purposes, we assume that the client and problem owner are
one and the same. Nevertheless, it is important to realize that this is not always the case.
Sometimes a client may want to play a role in solving a problem while other parties have
more problem-solving power but do not (yet) assume problem-ownership for strategic
reasons. Then again, a client may want to anticipate a foreseeable future problem situa-
tion even though problem-ownership cannot yet be ascribed to a specific party. Perhaps
the impact of the situation is not yet known or the responsibilities of potential stakehold-
ers in the new situation have not been regulated. In these situations, the issue paper can
be used to critically reflect on the issue of problem-ownership and advise the client how
to act accordingly.
8.2 The Key Elements of an Issue Paper
An issue paper has value for the client if its problem analysis adds something new to exist-
ing analysis reports and studies. The analyst creates this value through structuring exist-
ing information and so creating new insights as to how the problem may be addressed or
solved. This implies that the policy analyst, the author of the issue paper, applies a critical
and reflective attitude towards information, good analytical skills and good writing skills.
These qualities are best learned by doing. The learning process can be enhanced by critical
reflection with clients and peers.
According to our own experience and that of others, an issue paper is considered a good
issue paper only when the readers, the problem owner and critical actors
– recognize the relevance and value of the provided problem analysis;
– value and accept the choices made in selecting and combining empirical and informa-
tion and theory for a diagnosis of the problem situation;
– accept the validity of the recommendation for a specified follow-on activity that aims
to contribute significantly to solving the problem;
– are convinced that the proposal for this follow-on activity can contribute to the intended
effect.
The key elements of an issue paper, its specific contents and argumentation, must sup-
port and reflect these qualities. We identify eight elements and describe these briefly in
this section starting with the outline of the paper. Section 8.3 discusses the importance
of choosing a storyline when presenting the framed problem. The process of writing an
entire issue paper is discussed in Section 8.4.
8.2.1 Effective Outline for the Issue Paper
Issue papers are brief. Its contents can be arranged in a general outline as indicated in
Table 8.1. Note that this is just one possible outline. Authors on policy analysis like Quade
(1989: 73-78), Checkland (1985: 169) and Dunn (1994: 426) provide more detailed and
more elaborate outlines.
173

Issue
paper
Policy AnAlysis of Multi-Actor systeMs
The format of the issue paper is consistent with Figure 1.2 and Chapter 6: Part 1 of the
issue paper, the introduction, presents the initial problem. This part is one to two pages
long. Part 2 is based on the results of the partial analyses. It presents the ‘framed prob-
lem’, meaning the adjusted and refined original problem and how it can be characterized
based on the analyses. This part may be four to eight pages long. The text of Part 2 may be
divided into shorter sections if this part of the paper is too long to be read as one fluent
text. The content of Part 3 justifies the proposal in Part 4 and presents a line of reasoning
that is consistent with Part 2.
Table 8.1 Standard format for an issue paper
Title Page
A foreword – The author accounts for important choices in the research and ownership of its results.
1. Introduction – Four to five paragraphs that present the context or motivation for writing the paper, the initial
problem situation as presented to the author, the complexity of solving this problem, and the dilemma that
client and/or stakeholders deal with (see 8.4.1).
2. Framed problem – a fluent text or synthesis of the main conclusions drawn from the different partial analy-
ses of the system, the stakeholder arena and the future. The storyline of this text is consistent with and builds
up to the characterization or diagnosis of the problem.
3. Conclusion and Recommendations – the characterization of the problem; knowledge gap to be addressed
in support of dealing with the dilemma; and recommendations for further action
4. A proposal for follow-on activity – a project plan. This very often entails a proposal for a research project
that addresses a knowledge gap that constraints further action or decision-making.
Bibliography – A list of sources of information that have been referred to in the text of the issue paper.
Appendices – A compilation of all conceptual and analytical models that were made for and used in this paper.
The models are presented with a short mention of the purpose of the analysis, a short explanation as to what the
model shows and what was learned from that, and a list of references used in making the model.
8.2.2 Demarcation of Initial Problem Situation
A client who commissions an issue paper has a problem situation to be addressed. Typi-
cally, this is an ill-defined problem that needs sharpening and demarcation (or scoping
or delineation) before analyses can start (Chapter 2.5). The first analyses show whether
the initial problem definition must be considered ‘misguided and erroneous’ (Brewer &
DeLeon, 1983: 155).
A well-demarcated, initial problem definition gives information about the following:
the context of the system in which the problem is situated; identification of the problem
owner; identification of critical actors and their apparent stakes with regard to the existing
situation and efforts to solve the problem; information on spatial and temporal bounda-
ries (what locality, what deadlines); and the dilemma that the problem owner (and per-
haps other stakeholders) must deal with when intervening in the problem situation. The
demarcation of the initial problem is the result of a first iteration of the analyses of system
boundaries, system diagram, stakeholder arena, client’s objectives and means that are
available to intervene in the problem situation.
8.2.3 Mutually Consistent, Partial Analyses of Multi-Actor System
Issue papers are based on insights gained from the analytical process as outlined in Chap-
ters 3, 4 and 5 of this book. If indeed the partial analyses are mutually consistent, then the
174

repap
eussI
8 PreParIng an Issue PaPer
analyst can characterize the problem situation (Chapter 6), draw conclusions and carry
these forth in following steps such as drawing recommendations for further action.
The different partial analyses are made by the analysts, preferably in collaboration with
the client and in interaction with actors in the problem environment. Consistency of the
partial analyses is best achieved by working iteratively. In this book, we present the dif-
ferent tools and methods for analysis in subsequent but separate chapters. However,
practitioners of policy analysis may start with a simultaneous download of the available
information in one or more diagrams or tables (system diagram, power-interest diagram,
etc.) and proceed with enriching one analysis with that learned or discovered in another
analysis. Each iteration serves to make or maintain the internal consistency of the set of
different in-depth analyses.
8.2.4 Storyline for the ‘Framed Problem’
The storyline of Part 2 of the issue paper, the framed problem, provides the logic for struc-
turing the multifaceted information and builds the argument leading up to the conclusion
and recommendations. Section 8.3 presents storylines for seven possible problem frames
and some further examples can be found in the Annex to this Chapter.
8.2.5 Recommendations and Related Proposal for a Follow-On Activity
At the end of the issue paper, the analyst recommends follow-on activities that enhance
the client’s capability to solve the problem. Sometimes, the analyst will recommend that
the client do nothing and wait until uncertainty about the situation has diminished. In
most situations, however, the analyst will sketch a perspective for action and identify a
promising action or follow-on activity. A list of such actions is presented in Chapter 6.
The issue paper may include a proposal for the recommended action if this action war-
rants professional support. Proposals are to be written according to standards of the field
of research or discipline in question. In the case that the analyst recommends that knowl-
edge be generated, the proposal will be a plan for qualitative or quantitative research, and
is to be written according to scientific standards (see Chapter 7). Quantitative research
may include data collection and analysis with various methods, or a simulation study that
implies the building of a model or game; qualitative research may make use of case study
research, comparative analysis and essay writing to address philosophical questions.
8.2.6 Accountability Statement
For reasons of transparency and professional integrity, the issue paper ought to give infor-
mation about the position of the author and, if applicable, name the code of conduct or
ethical principles that the work complies with. The source of funding for the work and
the relationship with particular stakeholders can be addressed here also. Depending on
the extent of the problem and the funding of the paper, this statement can be made in a
preface or presented separately, immediately after the preface.
8.2.7 A List of Resources or Bibliography
For reasons of scientific integrity, the issue paper must include a list of references and
other resources that were used in the analyses or that support the communication of
results. Often, these sources can be presented in the APA citation style, which is accepted
in education, psychology and the sciences, but the client may have own requirements for
referencing.
175

Issue
paper
Policy AnAlysis of Multi-Actor systeMs
For reasons of legitimacy, it is important to explicate how the authors have achieved a
multiple stakeholder perspective on the problem. The variety of resources used can be
shown with the bibliography, both in terms of publication types (scientific journals, books,
policy papers, annual reports, minutes of public meetings, legislation, documented inter-
views, websites, podcasts, etc.) and in terms of authorship (scientists, government, non-
governmental organizations, companies, columnists, individual stakeholders, etc.)
8.2.8 A Convincing Style of Communication
The challenge in writing a good issue paper is to convey to the client, in a concise yet
convincing manner, what insights have been gained from the problem analysis. This is
easier said than done. The format presented in Table 8.1 has a clear beginning and end,
and allows the client and other readers to follow the train of thought from the initial prob-
lem situation towards recommendations and a plan of action. The argumentative style of
writing is well suited to inform and convince the client with clear statements, supportive
arguments and examples drawn from literature and the analyses.
Also, an issue paper is more likely to persuade the reader if it focuses on the rationale
for the proposed action. To achieve this, analysts ought to focus on the main insights that
the analyses have yielded, present these and support them with arguments. Clarity about
what is and what is not important is more persuasive than a detailed report of an analysis.
A reference to the appendix where the analysis is shown in full will suffice. An extremely
detailed paper tends to end up in a drawer and miss its goal of supporting the client in
addressing a wicked problem.
Visualization and tabulation of information may aid in making the issue paper to be
both informative and concise. For instance, a map or drawing illustrates the geographical
demarcation of a problem situation better than text can. Diagrams and large tables may
not be included in the main text. Instead, clearly present the insights that were based on
such tables and diagrams and refer to the appendix for more detail.
8.3 Different Problem Diagnoses, Different Storylines
A description of the ‘framed problem’ forms the core of the issue paper. To write this
section in an informative and convincing manner, the author fist synthesizes the insights
from the rich problem description, decides how the problem situation may be understood
or framed (Chapter 6) and then decides on a storyline. The storyline enables the author
to present the main findings in a logical and concise manner and enables the reader to
understand how the conclusions and recommendations follow from the analyses that
preceded the writing of the issue paper.
A storyline shows where the tension is located in the problem situation: within the sys-
tem, within the actor arena, in future developments, in the ‘solution space’ for measures,
in the values and/or perceptions that actors hold, in the institutional design or formal
chart, or in a ‘chicken or egg’ dependency of developments. The Annex, at the end of this
chapter, presents seven such storylines, covering a presentation of the problem situation,
conclusions and recommendations to the client. These storylines can be used for the
problem characterizations that are listed in Table 6.2. See Text box 8.2 for an example.
176

repap
eussI
8 PreParIng an Issue PaPer
Text box 8.2 Storyline for problems that are characterized by large differences in perception
among stakeholders with regard to the most promising solution
1. Framed problem Briefly describe the promising solution and use performance criteria to
sketch its impact. Argue why the client cannot implement this solution unless other parties act
also (or refrain from action). Name these critical actors.
Continue by sketching the problem perception of the critical actors (objectives in relation to
task and responsibilities, cause of problem, preference for solutions, future) and their position
in the stakeholder arena (hierarchy, opponents/friends). Focus on what might change this
perception (information, incentives for action, actions of other actors, time). Present these
‘mini problem analyses’ in a logical order, e.g. present client first and then the largest ally or
opponent. Multiple options!
2. Conclusions and recommendations Present the diagnosis and a recommendation as to how
the client may proceed. Think of creating incentives in relation to exploiting or changing
interdependencies, dynamics and strategic positions in the stakeholder arena. Give the
rationale for immediate action and how this can be achieved (Chapter 6). Then present the
proposal for a follow-on activity (Chapters 6 and 7).
8.4 A Systematic Approach to Preparing Issue Papers
The problem description in issue papers should be ‘as complete as time and available data
permit’ (Dunn, 1994: 425; cf. Checkland, 1985: 168). How can this be achieved? A system-
atic approach in preparing the issue paper may help prevent that important aspects are
overlooked or inconsistent.
The different parts of the issue paper will be elaborated in the next subsections. We
present a systematic approach to preparing issue papers, meaning that both the analysis
and writing processes are structured as subsequent steps. The first steps, the preparation
of the problem analysis, are explained in Chapters 3-5 and include data collection and
information structuring with various methods and techniques. Next, the insights from the
analyses are combined as explained in Chapter 6 and conclusions are drawn in terms of
the characterization or framing of the problem and follow-on activities that the client may
want to employ. Then a proposal can be written for the follow-on activity according to the
guidelines in Chapter 7. Now all the elements for writing the issue paper are available and
the paper can be written according to the outline given in Table 8.1.
Writing an issue paper is presented as a step-by-step process, but you will experience
that it is not a linear but rather a cyclical or iterative process. Indeed, during the process of
analysing and writing, new insights will necessitate the analyst-author to revisit or reiterate
analyses and rewrite texts according to the new information. Careful preparation of the
writing process may help to cut down the number of necessary iterations. First assemble
the results and conclusions that you could draw from the literature search, interviews and
the partial analyses and characterize or frame the problem (Figure 6.1). This creates the
basis for selecting an appropriate storyline and enables you to start the (iterative!) writing
process. We recommend that you start with writing the introduction.
177

Issue
paper
Policy AnAlysis of Multi-Actor systeMs
8.4.1 Introduction: The Initial Description Problem
The introduction introduces the subject of the issue paper to the reader. Remember that
the issue paper is written for the client who commissioned the work of researching and
writing this paper. Therefore, the introduction presents problem in a way that matches
the needs and the current knowledge of the client. Where possible, quantify the extent of
causes or effects of the problem. Failing to do so may cause some readers to lose interest
in the remainder of the paper (too little information on the urgency of the problem) or
disregard its outcomes (too little information to be able to verify problem perspectives are
aligned). Make proper use of references and problem owner information to ensure that
the problems and dilemmas described form an adequate representation of the problem
owner’s perception.
A good introduction is short and concise and helps the reader get a quick understand-
ing of what the issue paper is about. For most issue papers, this means that an introduc-
tion should be no more than two pages in length, or five to eight paragraphs that cover
the following elements:
a) Motivation: A short description of the problem’s context.
b) Problem: A short description of the problem as a gap between the desirable situation
and the actual or expected situation from the client’s perspective. This initial descrip-
tion should also clarify the geographical scope and the time horizon involved.
c) Problem-ownership: Address problem-ownership. Mention the problem owner and the
problem owner’s role in addressing the problem. Or explain that the situation is such
that multiple parties are concerned about the problem but it is not yet obvious as to
who should assume responsibility in the matter. Name these parties and the roles they
could possibly take in addressing the problem.
d) Indication of solution space: A problem is interesting for policy analysis only if there is
some hope of improving the situation. Explain where can interventions be sought and
give an impression of the extent of the solution space: are there alternative solutions
to choose from? What is known about the possible benefits and drawbacks of different
solutions?
e) Complexity: Describe what makes the problem complex enough to warrant further
analysis. Provide indications of the most important complexities, be it technical, soci-
etal, managerial and political complexities. Name some readily visible interdependen-
cies and conflicting interests between different actors involved.
f) Dilemma: Based on the above elements, what is the dilemma the problem owner
faces? What is the choice or decision a problem owner needs to make for which they
are currently ill-equipped? This dilemma provides the starting point for the in-depth
problem analysis.
178

repap
eussI
8 PreParIng an Issue PaPer
Table 8.2 Elements of initial problem and writing scheme for introduction
Element Analytical Techniques that Yield this Information
1. Motivation or problem context – Means-ends analysis (upper layer, Figure 3.3)
2. Problem, the gap between current and desired situ- – Chapter 2, Figure 2.2
ation (or future situation)
3. Spatial and temporal aspects of the system bound- – Scoping of means-ends analysis (Figure 3.3)
ary, given the problem situation
4. Main stakeholders involved in relation to problem- – Power-Interest grid, Figure 4.1 (first iteration)
ownership
5. Important factors that influence system perfor- – System diagram, Figure 3.9 (first iteration)
mance or relationships among stakeholders – Power-Interest grid, Figure 4.1 (first iteration)
– Overview of the main laws or formalized agree-
ments that hamper or support system performance
or problem-solving
6. Dilemma that actors must deal with – Means-ends analysis, Figure 3.4
8.4.2 Description of the ‘Framed Problem’
This section of the issue paper is a fluent text and presents the framed problem. It pro-
vides the reader with a good understanding of the problem situation as seen from multiple
perspectives, leads logically to the conclusions about the essence of the problem and sets
the stage for your choice of the role that the client may take to further the problem-solving
process. The nature of the problem indicates how you can best structure the information
that you have accumulated and convince the reader of the need to act. We recommend
that you write this section only after you have synthesized the results of the partial analy-
sis and characterized or framed the problem. The Annex presents different storylines for
structuring the ‘framed problem’ description.
Since you use the argumentative style of writing, it is important that you indicate the
sources of information on which you base your statements or argument and refer to these
sources. You will use a mix of sources: literature, interviews with client or stakeholders
and the conceptual models that you developed yourself (e.g. causal map, means-ends
diagram, problem formulations table, formal chart). References to the literature are
presented in the bibliography but the models are placed in an appendix and should be
referred to as such. Only in exceptional cases do you include figures, maps, diagrams or
tables in the main text of the paper. A rule of thumb is that the figure or table ought to
support the reader with an illustration of a critical argument. The aim for a text is to be
independently readable, meaning that you present enough information to the reader to
understand the argument that you present. The reference to the appendix allows a reader
to investigate the source of your argument but, at the same time, your sharp text makes
this unnecessary.
8.4.3 Conclusions and Recommendations
The last part of issue papers presents the conclusion or diagnosis of the policy analysts
and links it to recommendations in support of dealing with the dilemma that was pre-
sented in the introduction. Again, ideas for recommendations may be found in Chapter 6
and Table 6.3. Typically, this section lists important knowledge gaps that are relevant for
dealing with the dilemma and/or in preparation of the follow-on activity. See Chapter 6.4
for a list of relevant knowledge gaps.
179

Issue
paper
Policy AnAlysis of Multi-Actor systeMs
This section is the linking pin between the problem analysis, which is the activity that
the client commissioned the analyst to do, and a proposal for follow-on action by the
client. Consult Chapter 7 with respect to the knowledge gaps that may be relevant for the
follow-on activity that you recommend. Knowledge gaps can be further specified in the
proposal that is included with the issue paper. If this activity involves research, knowledge
gaps will be presented as research questions in the research plan.
8.4.4 Proposal for Follow-On Action or Research Plan
The contents of a proposal for different follow-on activities have been discussed in Chap-
ter 7, with an emphasis on writing a plan for conducting research. It is important to
remember that a reader must be able to understand the proposal independent from the
remainder of the issue paper. That said, it is also important to reduce overlap between the
conclusions of the issue paper and the introduction of the proposal.
In the introduction to your proposal, you present a justification for the follow-on activ-
ity in line with the reasoning that is presented in the issue paper, and consistent with
the conclusions and knowledge gaps that are mentioned. You can use the labels of the
hexagon model to characterize the follow-on activities, for instance if the activity concerns
research, mediation, design, etc. Also, you mention the objective of the proposal: what is
the expected result and how will the proposed approach contribute to this?
Next, you present the proposal. Preferably, the approach concurs with the social and
political environment in which the follow-on activity takes place. Therefore, the proposal
addresses the general organization or adaptation of the activity to the context in which it
is to be implemented. Therefore, be specific about, for instance, how data are gathered,
about the involvement and role of different actors, or about plans to communicate the
activity. Last but not least, the proposal ought to convince the reader of its feasibility and
present a time schedule for the main (research) activities to be conducted and an over-
view of the necessary resources and how they will be obtained.
References
Brewer, G. D. & DeLeon, P. (1983). The Foundations of Policy Analysis. Homewood:
Dorsey Press.
Checkland, P. (1985). From optimizing to learning: A Development of Systems Thinking
for the 1990s. Journal of the Operational Research Society, 36(9), 757-767. https://doi.
org/10.1057/jors.1985.141.
Dunn, W. N. (1994). Public Policy Analysis: An Introduction. Englewood Cliffs: Prentice
Hall.
Fujimura, J. H. (1987). Constructing ‘Do-able’ Problems in Cancer Research:
Articulating Alignment. Social Studies of Science, 17(2), 257-293. https://doi.
org/10.1177/030631287017002003.
Quade, E. S. (1989). Analysis for Public Decisions. Amsterdam: North-Holland.
RAND Corporation. (n.d.). Issue Papers. www.rand.org/pubs/issue_papers.html.
Thissen, W. A. H. & Walker, W. E. (Eds.) (2013). Public Policy Analysis, Chapter 4.6.
https//doi.org/10.1007/978-1-4614-4602-6.
180

Annex
Storylines for framed problems that fit the frame, diagnosis or
characterization of the problem itself
A storyline for the problem description is based on the results of the policy analyst’s
work: literature search, interviews and analyses of system, system context, stakeholder
arena and (in)formal agreements that govern stakeholders’ actions and interactions, and
futures. The interpretation of the results of this work enables the analyst to frame or char-
acterize the problem. In this section, we propose storylines for seven possible problem
frames.
The storylines are presented as bullet lists. Making bullet lists is helpful in structuring
information as it invites to order and reorder, add and delete ideas for paragraphs.
Examples of problem frames (or problem diagnoses)
A. Large differences in values and/or problem perception and (need for) solution hampers problem-solving
B. Large differences in problem perception among stakeholders about one promising solution hampers problem-
solving
C. Insight needed in trade-offs related to choosing one out of various (technical) solutions to further problem-
solving
D. Uncertainty about incentives for cooperation among stakeholders hampers realization of a promising solution
E. Institutional design and/or hierarchy in stakeholder arena hampers problem-solving
F. Large uncertainty about the future hampers problem-solving
G. Chicken-and-egg problem hampers reaching policy goal
A Storyline for Problem Framed as ‘Large Differences in Values, Problem
Perception and (Need for) Solution Hampers Problem-Solving’
Problem description that explains dilemma; storyline highlights lack of shared problem
frame
– A brief description of the situation/dilemma, in terms of stakeholder perceptions (how
much do they differ?), system performance (who suffers from status quo?), trends and
cascade of effects in system behaviour.
– Name the main factors and actors that cause the stalemate situation. Indicate client’s
position: why must stalemate situation change?
– ‘Mini problem descriptions’ from the perspectives of 3-5 critical actors. Descriptions
highlight the values that motivate the actor and if these are (not) shared, explains other
barriers to cooperate and what it takes to remove these. Present mini problems in a
logical order, e.g. present client first and then the largest ally or opponent. Multiple
options!
181

Policy AnAlysis of Multi-Actor systeMs
Conclusions and recommendations
– Statement of the diagnosis or problem frame. Explicate the main differences that the
client ought to pay attention to and indicate possible follow-on activities (Chapter 6).
– Recommendation as to how the client may proceed/act. And a rationale for immediate
action and how this can be achieved.
– Objective of a recommended follow-on activity (Chapters 6 and 7). What will be achieved
if proposal for this follow-on activity is executed?
B Storyline for Problem Framed as ‘Large Differences in Problem Perception
among Stakeholders about One Promising Solution Hampers Problem-Solving’
Problem description that explains dilemma; storyline highlights various problem
perceptions
– Brief description of the one promising solution, using performance criteria to sketch
its impact.
– Explanation why (main) problem owner cannot implement this solution unless other
parties act also (or refrain from specified actions). Name these critical actors.
– ‘Mini problem analyses’ of these critical actors in a logical order, e.g. present client first
and then the largest ally or opponent. Multiple options!
• Problem perception(s) include stakeholder objectives in relation to task and
responsibilities, perception of cause of problem, preference for solutions and their
position in the actor arena (hierarchy, opponents/friends). Include perception of
future changes and consequences.
• Indicate what might change problem perception (information, incentives for action,
actions of other actors, time).
Conclusions and recommendations
– Statement of the diagnosis or problem frame. If possible, name ways to influence inter-
dependencies, dynamics and strategic positions in the stakeholder arena.
– Recommendation as to how the client may proceed/act. And a rationale for immediate
action and how this can be achieved (Chapter 6).
– Objective of a recommended follow-on activity (Chapters 6 and 7). What will be achieved
if proposal for this follow-on activity is executed?
C Storyline for Problem Framed as ‘Insight Needed in Trade-offs Related to
Choosing One Out of Various (Technical) Solutions to Further Problem-Solving’
Problem description that explains dilemma; storyline highlights differences between
solutions
– Brief description of the problem/dilemma and the main performance criteria to be
improved.
– Brief overview of the most promising solutions (with arguments pro and con).
– Mini descriptions of these solutions in a logical order, e.g. present the most satisficing
solution first. Multiple options!
182

annex
• Descriptions include measures to be employed and their effectiveness; possible
externalities; expected impact of solutions in different futures. If relevant, name
mitigating actions.
• Descriptions give an insight into the strategic position of stakeholders per solution
as well as the possibility of coalition formation in support of one of the solutions.
Conclusions and recommendations
– Statement of the diagnosis or problem frame. If possible, indication of extra measures
that the client may take either to mitigate the effect of the trade-off (compensation
measures) or to otherwise take away barriers to taking the decision about what trade-
off is most acceptable.
– Recommendation as to how the client may proceed. Is it possible to make the trade-
off or must it be postponed on order to align stakeholders and increase willingness
to accept a trade-off? Rationale for immediate action and how this can be achieved
(Chapter 6).
– Objective of a recommended follow-on activity (Chapters 6 and 7). What will be achieved
if proposal for this follow-on activity is executed?
D Storyline for Problem Framed as ‘Uncertainty about Incentives for Cooperation
among Stakeholders Hampers Realization of a Promising Solution’
Problem description that explains dilemma; storyline per ‘barrier’ for cooperation
– Brief description of the promising solution(s) and explanation why (main) problem
owner cannot implement either solution unless other parties act also (or refrain from
specified actions). Name the 2-4 most important barriers to cooperation (e.g. formal
chart regarding tasks/responsibilities, (in)formal agreements, funding, time, political
will).
– Mini analyses of these institutional barriers in a logical order, e.g. present the barrier
with largest impact first. Multiple options!
• Analysis of barriers or obstacles starts with labelling of the change or interven-
tion that cannot take place unless the barrier is removed. The nature of the bar-
rier (technical, social or both) and its function in the system, stakeholder arena or
institutional design are explained. Who benefits if the barrier continues to exist?
Questions about future action of the barrier (impact, continuation) are answered.
• For each barrier, indicate what actor(s) can take away the barrier and what incentive
may prompt them to do so (law enforcement, subsidy, penalty, exchange of costs/
benefits, compensation, information). Name supporters of and opponents to bar-
rier.
Conclusions and recommendations
– Coalition of stakeholders to be motivated to cooperate given the right incentives are in
place.
– Statement of the diagnosis or problem frame. Explain what the uncertainty about the
effectiveness of incentives means for the process of problem-solving.
183

Policy AnAlysis of Multi-Actor systeMs
– Recommendation as to how the client may proceed. Is it possible and desirable that
client motivates critical actors to remove institutional barriers or address knowledge
gaps? How?
– Rationale for immediate action and how this can be achieved (Chapter 6).
– Objective of a recommended follow-on activity (Chapters 6 and 7). What will be achieved
if proposal for this follow-on activity is executed?
E Storyline for Problem Framed as ‘Institutional Design and/or Hierarchy in
Stakeholder Arena Hampers Problem-Solving’
Problem description that explains dilemma; storyline per ‘barrier’ for problem-solving
– Brief description of the problem situation with emphasis on how either the institu-
tional design and/or stakeholder hierarchy stands in the way of solving the problem.
– Labels of the main 2-4 barriers to problem-solving and explanation if these stem from
legislation, market functioning, ownership or formalized stakeholder relationships.
– Mini analyses of these barriers in a logical order, e.g. first present the barrier that can
be lifted in a short time frame. Multiple options!
• Analysis of institutional or hierarchical barriers starts with explanation of the mech-
anism that hampers problem-solving. Next, measures (in institutional design or
stakeholder arena) are discussed to remedy situation, such as knowledge, time,
money, formation of or dissolving stakeholder coalition, extending support, politi-
cal will. Who benefits if such measures do (not) succeed? How fast can measures
be effective and how robust given uncertainties about the future?
• For each barrier, indicate what actor(s) can take such measures and name support-
ers and opponents.
Conclusions and recommendations
– Statement of the diagnosis or problem frame. Explain what aspect of institutional or
hierarchical barrier needs to be lifted first.
– Recommendation as to how the client may proceed (Chapter 6) and a rationale for
immediate action and how this can be achieved.
– Objective of a recommended follow-on activity (Chapters 6 and 7). What will be achieved
if proposal for this follow-on activity is executed?
F Storyline for Problem Framed as ‘Large Uncertainty about the Future Hampers
Problem-Solving’
Problem description that explains dilemma; storyline per ‘contextual scenario’
– Brief description of the problem situation with emphasis on uncertain developments
in system context and how this may affect stakeholder values and/or system perform-
ance.
– Three or four most important uncertain, external factors and a discussion of the driv-
ers of these uncertainties (ecological, technical, economical, social or political).
– Short presentation of four contextual scenarios as explained in Chapter 5. For each
scenario, discuss system performance and the extent to which actor(s) may suffer or
184

annex
benefit from the described circumstances. Discuss how external factors can cause a
shift in system performance or stakeholder satisfaction. Discuss the main assump-
tions and signpost: what must client and stakeholders monitor to judge in what sce-
nario the system performs.
Conclusions and recommendations
– Statement of the diagnosis or problem frame. Explain what uncertain aspects of the
future hamper problem-solving most. Discuss what is needed so that stakeholders
can proceed despite uncertainty.
– Recommendation as to how the client may proceed (Chapter 6) and a rationale for
immediate action and how this can be achieved.
– Objective of a recommended follow-on activity (Chapters 6 and 7). What will be achieved
if proposal for this follow-on activity is executed?
G Storyline for Problem Framed as ‘Chicken-and-Egg Problem Hampers Reaching
Policy Goal’
Problem description that explains dilemma; storyline per ‘phase’ of development in
demand/supply
– Short description of the services or infrastructures for which demand and supply must
be developed. Then gap analysis (for current and future situation) that elucidates the
overall policy goal, interest and role of the problem owner.
– Naming of 2-4 different phases in development of demand and supply. Description of
the interrelatedness of the phases and feedback loops between demand and supply
development.
– Mini analyses of these developmental phases in a logical order: phase 1 first. Explana-
tion of measures needed in each phase, who is responsible for their realization and
incentives to (not) act. Identification of the main interdependencies between the dif-
ferent phases in the near and far future. Insight into how external factors may acceler-
ate, hamper or neutralize progress. Indication of issues that are critical for, more or
less simultaneous, development of demand and supply.
Conclusions and recommendations
– Present the diagnosis that this is a ‘chicken-and-egg’ problem and motivate this.
– Discuss the risks that actors take when developing demand and/or supply. List the
issues that stakeholders need to address to prevent that progress stalls and highlight
client’s position.
– Recommendation as to how the client may proceed (Chapter 6), either by developing
a strategic position in the actor arena or by taking technical or institutional measures.
What knowledge gaps, if any, stand in the way of the client’s agency?
– Objective of follow-on activity (Chapters 6 and 7). What will be achieved if proposal for
this follow-on activity is executed?
185

About the Authors
Bert Enserink is associate professor of policy analysis at Delft University of Technology.
He is a specialist in action research, participatory methods, social learning and scenario
analysis. Main fields of application are water management and energy transition. He has
extensive international experience and teaches courses in policy analysis and intercultural
communication.
https://orcid.org/0000-0001-9182-3712
Pieter Bots is associate professor of policy analysis at Delft University of Technology. He
is an expert designer of methods and tools for systems analysis and decision support. His
present research focuses on multi-stakeholder modelling and simulation of energy grids
and markets. He teaches courses in modelling, policy and decision analysis, and design-
ing in socio-technical systems.
https://orcid.org/0000-0003-4569-1549
Els van Daalen is associate professor of policy analysis at Delft University of Technology.
She is involved in both teaching and research in the area of methods for systems model-
ling and analysis. Specific methods of interest are System Dynamics and serious gaming.
She has developed and taught courses on problem structuring and systems modelling at
all university levels.
https://orcid.org/0000-0001-7635-572X
Leon Hermans works as associate professor in water and environmental policy analysis at
TU Delft and IHE Delft. His work focuses on the use of actor concepts and models and
on improving the linkages between decision-making, implementation and evaluation, to
foster policy learning about complex water challenges now and in the future.
https://orcid.org/0000-0002-5294-9045
Joop Koppenjan is emeritus professor of Public Administration at the Erasmus University
Rotterdam. He worked at TU Delft’s TPM Faculty from 1996 till 2010. He is specialized in
doing comparative case study research between policy areas or countries. His research
interests include topics like public policy, network governance, public private partnerships
and public service delivery. Areas of application are infrastructure-based sectors such as
transport, water, and energy, and social sectors such as social support, care, and safety.
https://orcid.org/0000-0002-0099-5760
Rens Kortmann is assistant professor in policy gaming at Delft University of Technology.
He teaches problem analysis and policy game design. His research focuses on design-
ing and evaluating persuasive games about complex socio-technical problems. His main
application areas are sustainable development and health care.
https://orcid.org/0000-0002-7088-4222
187

Policy AnAlysis of Multi-Actor systeMs
Jan Kwakkel is a full professor in model-based support for decision making under deep
uncertainty at Delft University of Technology. His research focuses on developing and
testing innovative model-based techniques for the design of dynamic adaptive policy path-
ways. He has applied his research in a range of domains including climate adaptation,
flood risk management, transport and logistics, resource economics, and national safety
and security.
https://orcid.org/0000-0001-9447-2954
Tineke Ruijgh van der Ploeg is senior lecturer of policy analysis at Delft University of
Technology. She enjoys supervising students who write issue-papers as a preparation for
setting up their Bachelor thesis research projects. Also, she is engaged in project-based
education of designing socio-technical systems in one of TPM’s MSc programmes.
Jill Slinger is associate professor of policy analysis at Delft University of Technology. She
teaches courses on systems modelling at graduate and PhD level and is spearheading the
university's teaching on Building with Nature. As Visiting Professor at Rhodes University,
South Africa, Slinger is also involved in addressing water and coastal implementation
challenges in the developing world.
https://orcid.org/0000-0001-5257-8857
Wil Thissen is emeritus professor of policy analysis at Delft University of Technology. He
has led the development of Policy Analysis at TU Delft since 1992 until his formal retire-
ment. He currently enjoys keeping up with the field as a reviewer/editorial board member
for several academic journals, in particular in water- and environmental management,
and volunteers as a counsellor to actors in developing countries.
188