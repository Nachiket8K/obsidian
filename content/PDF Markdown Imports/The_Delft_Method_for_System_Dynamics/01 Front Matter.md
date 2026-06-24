---
title: "Front Matter"
book: "The_Delft_Method_for_System_Dynamics"
source_pdf: "The_Delft_Method_for_System_Dynamics.pdf"
tags:
  - pdf-import
  - split-book
---

Willem
Auping,
Floortje
d’Hont,
Merla
Kubli,
Jill
Slinger,
Patrick
Steinmann,
Floris
van
der
Heijde,
Els
van
Daalen,
Erik
Pruyt,
Wil
Thissen
|
The
Delft
Method
for
System
Dynamics
scimanyD
metsyS
rof
dohteM
tfleD
ehT
nessihT
liW
,tyurP
kirE
,nelaaD
nav
slE
,edjieH
red
nav
sirolF
,nnamnietS
kcirtaP
,regnilS
lliJ
,ilbuK
alreM
,tnoH’d
ejtroolF
,gnipuA
melliW

The Delft Method for System Dynamics
W.L. Auping, F.M. d’Hont, M.D. Kubli, J.H. Slinger, P. Steinmann, F.T. van der
Heijde, C. Van Daalen, E. Pruyt, W.A.H. Thissen

|     |     |     |
| --- | --- | --- |

Version: November 2024
|     | 2   |     |
| --- | --- | --- |

Colophon
The Delft Method for System Dynamics
Authors:
W.L. Auping1, F.M. d’Hont1, M. D. Kubli1, J.H. Slinger1, P. Steinmann1, F.T. van der Heijde1, C. Van Daalen1,
E. Pruyt2, W.A.H. Thissen1
1 Faculty of Technology, Policy and Management, Delft University of Technology
2 Center for Policy Exploration, Analysis and Simulation (PEAS)
Willem Auping w.l.auping@tudelft.nl 0000-0003-1898-643X
Floortje d’Hont f.m.dhont@tudelft.nl 0000-0002-6966-023X
Merla Kubli m.d.kubli@tudelft.nl 0009-0007-3948-3491
Patrick Steinmann p.steinmann@tudelft.nl 0000-0002-6204-6253
Jill Slinger j.h.slinger@tudelft.nl 0000-0001-5257-8857
Floris van der Heijde 0009-0003-6142-726X
Erik Pruyt 0000-0001-8332-5422
Els van Daalen 0000-0001-7635-572X
Wil Thissen 0000-0003-3288-4675
Contributions
W.L. Auping (Original Idea, Theory, Exercises, Review & Editing, Images), F.M. d’Hont (Original Idea,
Theory, Exercises, Review & Editing, Images), M. D. Kubli (Theory, Review & Editing), J.H. Slinger (Review
& Editing), P. Steinmann (Review & Editing), F.T. van der Heijde (Editing, Images), C. van Daalen (Theory,
Images), E. Pruyt (Original Idea, Theory, Exercises, Images), W.A.H. Thissen (Theory).
The order of the authors is based on the legacy of Delft SD education materials and not on the relative
size of their contributions.
Keywords:
system dynamics, education, simulation modelling, complex systems, vensim, stella, powersim
Published by:
TU Delft OPEN Publishing | Delft University of Technology, The Netherlands
DOI: https://doi.org/10.59490/tb.97
ISBN paperback/softback: 978-94-6366-893-4
ISBN eBook/PDF: 978-94-6366-894-1
Copyright statement:
This work is licensed under a Creative Commons Attribution 4.0 International
(CC BY 4.0) licence, unless otherwise stated.
© 2024 published by TU Delft OPEN Publishing on behalf of the authors
Cover design made by Willem Auping
Copyright clearance made by the TU Delft Library copyright team
Disclaimer:
Every attempt has been made to ensure the correct source of images and other potentially copyrighted
material was ascertained, and that all materials included in this book have been attributed and used ac-
cording to their license. If you believe that a portion of the material infringes someone else’s copyright,
please contact w.l.auping@tudelft.nl
3

|     |     |     |
| --- | --- | --- |

|     | 4   |     |
| --- | --- | --- |

Preface
System Dynamics (SD) was developed in the 1960s by J. Forrester, since many of
the existing methods for solving problems did not offer a sufficient understanding of
strategic problems in complex systems. The objective of SD modelling is, therefore,
to clarify the relation between the behaviour of a system as a function of time and the
underlying processes, which is referred to as the system structure in SD. The
method consists of observing and identifying the behaviour of a system as a function
of time and developing a model with the possibility of explaining existing system
behaviour and designing improved system behaviour (Wolstenholme, 1989a).
SD modelling can be used to understand complex systems in a wide variety of fields,
such as healthcare, energy transition, environmental management, safety and
security, public order, social dynamics, education, economics, business
management, and operations and supply chain management. It is therefore essential
for anyone working in these fields to have a basic understanding of what System
Dynamics are, and gain some working skills in SD modelling.
This e-book introduces System Dynamics Modelling to novice modellers. It is
specifically designed to support courses on simulation methods at the Faculty of
Technology, Policy and Management (TPM) at Delft University of Technology (TU
Delft) in the Netherlands, including Systems Modelling 3 and Introduction to TPM
Modelling. However, it can also be used by other institutions that follow a practice-
oriented and skill-oriented approach to learning, while it also offers sufficient
theoretical information to support autonomous learning.
We choose to publish the e-book under an open access license so that SD learners
from all over the world can study the material, independent of their study
programmes or university access.
Authors
The System Dynamics education team of TU Delft has developed and published this
book. The material builds on decades of System Dynamic teaching experience at TU
Delft, where Bachelor and Master students are trained in various methods for
modelling and simulating complex challenges (Pruyt, 2013; Van Daalen, Thissen, &
Phaff, 2006). All co-authors have contributed to the development of System
Dynamics education at TU Delft. This e-book builds on earlier theory-oriented syllabi,
materials drawn from Pruyt (2013) and experience built in decades of System
Dynamics education.
The Delft Method: a teaching philosophy for learning by doing
Modelling is difficult and learning how to build simulation models is even harder.
There are a many excellent books that provide methods for learning System
5

Dynamics (SD) (e.g., Bossel, 2007a, 2007b, 2007c; Coyle, 1996; Duggan, 2016;
Ford, 2009; Meadows, 2008; Morecroft, 2015; Pruyt, 2013; Richardson & Pugh,
1981; Sterman, 2000; Warren, 2002). Most of these books primarily focus on
understanding theory first and practicing modelling skills later (cf., Carver, 1996).
Others only focus on theory and hardly offer any (modelling) exercises. This book
offers a unique approach to learning SD modelling, and therefore is a valuable
addition to other works already available.
The starting point of this is book is our conviction that modelling is best learnt by
doing and practicing one’s skills. This book, The Delft Method for System Dynamics,
is inspired by the Dutch language learning method “Delftse Methode” (the "Delft
Method", Sciarone & Montens, 1985), which is used in courses for internationals at
TU Delft and beyond. In these language courses, students are encouraged to learn
Dutch by doing, following what is often called a ‘natural’ approach to language
learning. Instead of learning the rules first and make sentences later, students build
their language skills by ‘doing’: by speaking, by writing, by making mistakes, by
many repetitions and constant feedback. Theory, and grammar and spelling rules
stand in service to active language abilities. The method is particularly well suited for
kinaesthetic learners: students who prefer to learn based on experiences – moving,
touching, doing (Fleming, 1995; Gardner, 1983). Owing to the engineering focus of
TU Delft, students flourishing with this type of learning are particularly frequent.
Students at TU Delft also often do not have much linguistic knowledge, making the
Delft Method particularly useful.
This pedagogical philosophy inspired the System Dynamics modelling courses
taught at TU Delft and this e-book. Indeed, there is overlap between learning spoken
languages on the one hand and learning modelling and programming languages on
the other. There are of course differences, not in the least the fact that spoken
languages are vastly more complex, but the same language learning strategies can
apply to both. In the Delft Method, the underlying logic of a language (the rules or
‘syntax’) is revealed through practice. In our translation of the Delft Method to
System Dynamics, we apply the same method: learning by doing.
How to use this the e-book
Focus on modelling
In this e-book, we keep the theory sections short. Theoretical concepts are explained
briefly and pragmatically; the emphasis, however, lies on the actual practice of
modelling. Learners are encouraged to try the exercises early on, without fully
understanding the theory. Exploring, struggling and reflecting are key components in
the learning process. You are encouraged to try to do the exercises and don’t worry
if you struggle at bit and must find some things out by yourself.
6

Working together works
Modelling is not easy to do by yourself, although it is possible. We find that it works
best if learners work together. It often helps to discuss things with classmates or in
peer groups. You can also learn a lot from explaining things to others.
Try first, but help is not far away
If you get stuck, do not waste time worrying. Software documentation of the different
modelling languages (e.g., Vensim, Stella, or Powersim) and fellow students can
often be of help. For students following System Dynamics courses at TU Delft,
teaching assistants (first line) and teachers (second line) are available for questions
during the computer labs.
Follow best practices in modelling
It is important that you get used to good modelling practices. These are:
• Define all units as soon as you formulate a variable.
• Formulate the model variable by variable, equation by equation. Do not build
the whole structure at once, before entering the equations. Finish the equation
before you go to a next variable.
• Always have a running model.
• Save your model frequently. Backup versions may be helpful when modelling
advances don’t work out as planned.
• When you get stuck with modelling: take a walk.
Reading guide
Chapter 1 introduces the basic principles and background of System Dynamics.
Chapter 0 through Chapter 5 describe the exercises. Each exercise chapter consists
of two parts: theory and modelling questions. The theory questions are qualitative
exercises in which concepts like diagramming conventions, transferring stock-flow
diagrams into CLDs, and recognising the order (1st, 3rd, or infinite) and type (material
or information) of delays. You should be able to make the theory exercises without
using SD software (e.g., Vensim, Stella), but it is not forbidden to use software to
solve them. The theory exercises are in the form of short answer questions.
All modelling exercises contain a model. In this model description, all variables are
given in italics. Emphasis lies on learners being able to distinguish different types of
variables (e.g., stocks, flows and auxiliaries). The text generally only allows a single
interpretation: if you model the description correctly, you should get a model that
generates exactly the same behaviour as the exemplar. Also, the stock-flow
7

structure of your model should be the same as the example model. For most
exercises, answers are available (see Auping et al., 2024).
The theory in this book follows a typical modelling cycle: problem articulation and
conceptualization are discussed in Chapter 0, model formulation in Chapter 0,
evaluation including verification in Chapter 0, and model use and policy testing in
Chapter 9.
We hope you will enjoy this book and share the joy of systems thinking and
modelling with us. We prepared the material in this e-book with care and foresee
regular updates to the material. Please don’t hesitate to contact us with any remarks
or feedback.
Delft, August 2024,
The authors.
8

Contents
Preface ....................................................................................................................... 5
Authors ................................................................................................................... 5
The Delft Method: a teaching philosophy for learning by doing .............................. 5
How to use this the e-book ..................................................................................... 6
Reading guide ........................................................................................................ 7
