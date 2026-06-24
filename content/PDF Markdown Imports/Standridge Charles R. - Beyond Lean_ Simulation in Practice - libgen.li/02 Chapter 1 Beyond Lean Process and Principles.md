---
title: "Chapter 1 Beyond Lean: Process and Principles"
book: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li"
source_pdf: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li.pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 1 Beyond Lean: Process and Principles** 

## _1.1 Introduction_ 

The application of lean concepts to the transformation of manufacturing and other systems has become ubiquitous and is still expanding (Learnsigma, 2007).  The use of lean concepts has yielded impressive results.  However, there seems to be a growing recognition of the limitations of lean and for a need to overcome them, that is to build upon lean successes or in other words to get beyond lean.[1] Getting beyond lean is the subject of this book. 

Ferrin, Muller, and Muthler (2005) identify an important goal of any process improvement or transformation: find a correct, or at least a very good, solution that meets system design and operation requirements before implementation.  Lean seems to be unable to meet this goal.  As was pointed out by Marvel and Standridge (2009), a lean process does not typically validate the future state before implementation.  Thus, there is no guarantee that a lean transformation will meet measurable performance objectives. 

Marvel, Schaub & Weckman (2008) give one example of the consequences of not validating the future state before implementation in a case study concerning a tier-two automotive supplier. Due to poor performance of the system, a lean transformation was performed.  One of the important components of the system was containers used to ship product to a number of customers.  Each customer had a dedicated set of containers.  The number of containers needed in the future state was estimated using a tradition lean static (average value) analysis, without taking the variability of shipping time to and from customers nor the variability in the time containers spent a customers into account.  Thus, the number of containers in the future state was too low.  Upon implementation, this resulted in the production system being idled due to the lack of containers.  Thus, customer demand could not be met. 

Standridge and Marvel (2006) describe the lean transformation of a system consisting of three processes.  The second process, painting, was outsourced and performed in batches of 192 parts.  Fearful of starving the third step in the process, the lean supply chain team deliberately over estimated the number of totes used to transport parts to and from the second step.  In this system, totes are expensive and have a large footprint.  Thus, the future state was systematically designed to be more expensive that necessary. 

It seems obvious that in both these examples, the lean transformation resulted in a future state that was less than lean because it was not validated before implementation.  Miller, Pawloski, and Standridge (2010) present a case study that further emphasizes this point and shows the benefits of such a validation.  Marvel and Standridge (2009) suggest a modification of the lean process that includes future state validation as well as proposing that discrete event computer simulation be the primary tool for such a transformation because this tool has the following capabilities. 

1. A simulation model can be analyzed using computer based experiments to assess future state performance under a variety of conditions. 

2. Time is included so that dynamic changes in system behavior can be represented and assessed. 

3. The behavior of individual entities such as parts, inventory levels, and material handling devices can be observed and inferences concerning their behavior made. 

4. The effects of variability, both structural and random, on system performance can be evaluated. 

5. The interaction effects among components can be implicitly or explicitly included. 

1 It is assumed that the reader has some familiarity with lean manufacturing / Toyota Production System concepts . 

1-1 

The discussion in this book focuses on how to build and use models to enhance lean transformations, that is to get beyond lean or to make lean more lean.  The modeling perspective used incorporates the steps required to operate the system and how these steps are connected to each other.  Models include the equipment and other resources needed to perform each step as well as the decision points and decision rules that govern how each step is accomplished and is connected to other steps.  These models can include the sequencing procedures, routing, and other logic that is needed for a system to effectively operate. 

Computer simulation models provide information about the temporal dynamics of systems that is available from no other source.  This information is necessary to determine whether a new or transformed system will perform as intended before it is put into everyday use.  Simulation leads to an understanding of why a system behaves as it does.  It helps in choosing from among alternative system designs and operating strategies. 

When a new system is designed or an existing system substantially changed, computer simulation models are used to generate information that aids in answering questions such as the following: 

1. Can the number of machines or workers performing each operation adequate or must the number be increased? 

2. Will throughput targets be reached that is will the required volume of output per unit time be achieved? 

3. Can routing schemes or production schedules be improved? 

4. Which sequencing scheme for inputs is best? 

5. What should be the work priorities of material handling devices? 

6. What decision rules work best? 

7. What tasks should be assigned to each worker? 

8. Why did the system behave that way? 

9. What would happen if we did “this” instead? 

## _1.2 An Industrial Application of Simulation_ 

In order to better understand what simulation is and what problems it can be used to address, consider the following industrial application, which can was used to validate the future state of a plant expansion (Standridge and Heltne, 2000).  A particular plant is concerned about the capital resources needed to load and ship rail cars in a timely fashion.  A major capital investment in the plant will be made but the chance for future major expansions is minimal.  Thus, all additional loading facilities, called load spots, needed for the foreseeable future must be built at the current time and must be justified based on product demand forecasts. 

Each product can be loaded only at specific load spots.  A load spot may be able to load more than one product.  However, it is not feasible to load all products on all load spots.  Cleverly assigning products to load spots may reduce the number of new load spots needed. Furthermore, maintenance of loading equipment is required.  Thus, a load spot is not available every day. 

The structure of the product storage and loading portion of the plant is shown in Figure 1-1. Products are stored in tanks with each tank dedicated to a particular product.  Tanks are connected with piping to one or more load spots that serve one or two rail lines for loading. These numerous connections are not shown. 

The primary measure of system performance is the percent of shipments made on time.  The number of late shipments and the number of days each is late are also of interest.  Shipping patterns are important so the number of pounds shipped each day for each product must be recorded.  The utilization of each load spot must be monitored. 

1-2 

The plant must lease rail cars to ship product to customers.  Different products may require different types of rail cars, so the size of multiple rail car fleets must be estimated.  In addition, the size of the plant rail yard must be determined as a function of the number of rail cars it must hold. 

The model must account for customer demand for each product.  Monthly demand ranges from 80% to 120% of its expected value.  The expected demand for some products varies by month. In addition, each load spot must be defined by its capacity in rail cars loaded per day as well as the products it can load.  Rail car travel times to customers from the plant and from the customer to the plant as well as rail car residence time at the customer site must be considered.  Rail car maintenance specifications must be included. 

Model logic is as follows.  Each day the number of rail cars to ship is determined for each product.  A rail car of the proper type waiting at the plant is assigned to the shipment.  If no such rail car exists, the model simply creates a new one and the fleet size is increased by one. 

Product loading of each rail car is assigned to a load spot.  Load spots that can load the product are searched in order of least utilized first until an available load spot is assigned.  A load spot may have been previously assigned loading tasks up to its capacity or may be in maintenance and unavailable for loading.  Note that searching the load spots in this order tends to balance load spot utilization.  The car is loaded and waits for the daily outbound train to leave the plant. The rail car proceeds to the customer, remains at the customer site until it is unloaded, and then returns to the plant.  Maintenance is performed on the car if needed. 

1-3 

Analysts formulate alternatives by changing the assignment of products to load spots, the number of load spots available, and the demand for each product.  These alternatives are based, in part, on model results previously obtained. 

This example shows some of the primary benefits and unique features of simulation.  Unique system characteristics, such as the assignment of particular products to particular load spots, can be incorporated into models.  System specific logic for assigning a shipment to a load spot is used.  Various types of performance measures can be output from the model such as statistical summaries about on time shipping and time series of values about the amount of product shipped.  Statistics other than the average can be estimated.  For example, the size of the rail yard must accommodate the maximum number of rail cars that can be there not the average. Random and time varying quantities, such as product demand, can be easily incorporated into a model. 

## _1.3 The Process of Validating a Future State with Models_ 

The simulation process used throughout this book is presented in this section. 

Using simulation in designing or improving a system is itself a process.  We summarize these steps into five strategic process phases (Standridge and Brown-Standridge, 1994; Standridge, 1998), which are similar to those in Banks, Carson, Nelson, and Nicol (2009).  The strategic phases and the tactics used in each are shown in Table 1-1. 

The first strategic phase in the simulation project process is the definition of the system design or improvement issues to be resolved and the characteristics of a solution to these issues.  This requires identification of the system objects and system outputs that are relevant to the problem as well as the users of the system outputs and their requirements.  Alternatives thought to result in system improvement are usually proposed.  The scope of the model is defined, including the specification of which elements of a system are included and which are excluded.  The quantities used to measure system performance are defined.  All assumptions on which the model is based are stated.  All of the above items should be recorded in a document.  The contents of such a document is often referred to as the **conceptual model.** A team of simulation analysts, system experts, and managers performs this phase. 

The construction of models of the system under study is the focus of the second phase. Simulation models are constructed as described in the next chapter.  If necessary to aid in the construction of the simulation model, descriptive models such as flowcharts may be built. 

Gaining an understanding of a system requires gathering and studying data from the system if it exists or the design of the system if it is proposed.  Simulation model parameters are estimated using system data. 

The simulation model is implemented as a computer program.  Simulation software environments include model builders that provide the functionality and a user interface tailored to model building as well as automatically and transparently preparing the model for simulation. 

1-4 

**Table 1-1:  Phases and Tactics of the Simulation Project Process** 

|**Strategic Phase**|**Tactics**|
|---|---|
|1.  Define the Issues and<br>Solution Objective|1.  Identify the system outputs as well as the people who use<br>them and their requirements.<br>2.  Identify the systems that produce the outputs and individuals<br>responsible for these systems.<br>3.  Propose initial system alternatives that offer solution<br>possibilities.<br>4.  Identify all elements of the system that are to be included in<br>the model.<br>5.  State all modeling assumptions.<br>6.Specify systemperformancemeasures.|
|2.  Build Models|1.  Construct and implement simulation models.<br>2.  Acquire data from the system or its design and estimate<br>modelparameters.|
|3.  Identify Root Causes and<br>Assess Initial Alternatives|1.  Verify the model<br>2.  Validate the model.<br>3.  Design and perform the simulation experiments.<br>4.  Analyze and draw inferences from the simulation results<br>about system design and improvement issues.<br>5.  Examine previously collected system data to aid in inference<br>drawing.|
|4.  Review and Extend<br>Previous Work|1.  Meet with system experts and managers.<br>2.  Modify the simulation model and experiment.<br>3.  Make additional simulation runs, analyze the results and<br>draw inferences.|
|5.  Implement Solutions and<br>Evaluate|1.  Modify system designs or operations.<br>2.  Monitorsystemperformance.|



The third strategic phase involves identifying the system operating parameters, control strategies, and organizational structure that impact the issues and solution objectives identified in the first phase.  Cause and effect relationships between system components are uncovered.  The most basic and fundamental factors affecting the issues of interest, the root causes, are discovered. Possible solutions proposed during the first phases are tested using simulation experiments. Verification and validation are discussed in the next section as well as in Chapter 3. 

Information resulting from experimentation with the simulation model is essential to the understanding of a system.  Simulation experiments can be designed using standard design of experiments methods.  At the same time, as many simulation experiments can be conducted as computer time and the limits on project duration allows.  Thus, experiments can be replicated as needed for greater statistical precision, designed sequentially by basing future experiments on the results of preceding ones, and repeated to gather additional information needed for decision making. 

The fourth strategic phase begins with a review of the work accomplished in phases one through three.  This review is performed by a team of simulation analysts, system experts, and managers. The results of these meetings are often requests for additional alternatives to be evaluated, additional information to be extracted from simulation experiments, more detailed models of system alternatives, and even changes in system issues and solution objectives.  The extensions and embellishments defined in this phase are based on conclusions drawn from the system data, simulation model, and simulation experiment results.  The fourth stage relies on the ability to adapt simulation models during the course of a project and to design simulation experiments 

1-5 

sequentially.  Alternative solutions may be generated using formal ways for searching a solution space such as a response surface method.  In addition, system experts may suggest alternative strategies, for example alternative part routings based on the work-in-process inventory at workstations.  Performing additional experiments involves modifications to the simulation model as well as using new model parameter values. 

Physical experiments using the actual system or laboratory prototypes of the system may be performed to confirm the benefits of the selected system improvements. 

In the fifth phase, the selected improvements are implemented and the results monitored. 

The iterative nature of the simulation project process should be emphasized.  At every phase, new knowledge about the system and its behavior is gained.  This may lead to a need to modify the work performed at any preceding phase.  For example, the act of building a model, phase 2, may lead to a greater understanding of the interaction between system components as well as to redoing phase 1 to restate the solution objectives.  Analyzing the simulation results in phase 3 may point out the need for more detailed information about the system.  This can lead to the inclusion of additional system components in the model as phase 2 is redone. 

Sargent (2009) states that model **credibility** has to do with creating the confidence managers and systems experts require in order to use a model and the information derived from that model for decision making.  Credibility should be created as part of the simulation process.  Managers and systems experts are included in the development of the conceptual model in the first strategic phase.  They review the results of the second and third phases including model verification and validation as well as suggesting model modifications and additional experimentation.  Simulation results must include quantities of interest to managers and systems experts as well as being reported in a format that they are able to review independently.  Simulation input values should be organized in a way, such as a spreadsheet, that they understand and can review.  Thus, managers and systems experts are an integral part of a simulation project and develop a sense of ownership in it. 

Performing the first and last steps in the improvement process requires knowledge of the context in which the system operates as well as considerable time, effort, and experience.  In this book, the first step will be given as part of the statement of the application studies and exercises and the last step assumed to be successful.  Emphasis is given to building models, conducting experiments, and using the results to help validate and improve the future state of a transformed or new system. 

## _1.4 Principles for Simulation Modeling and Experimentation_ 

Design (analysis and synthesis) applies the laws of basic science and mathematics.  Ideally, simulation models would be constructed and used for system design and improvement based on similar laws or principles.  The following are some general principles that have been found to be helpful in conceiving and performing simulation projects, though derivation from basic scientific laws or rigorous experimental testing is lacking for most of them. 

## **1. Simulation is both an art and a science** (Shannon, 1975). 

One view of the process of building a simulation model and applying it to system design and improvement is given in Figure 1-2. 

1-6 

**==> picture [385 x 241] intentionally omitted <==**

**----- Start of picture text -----**<br>
Simulation<br>Model<br>Simulation<br>System<br>Experiment<br>Inference<br>Drawing<br>**----- End of picture text -----**<br>


Figure 1-2:  Simulation for Systems Design and Improvement. 

A mathematical-logical form of an existing or proposed system, called a simulation model, is constructed (art).  Experiments are conducted with the model that generates numerical results (science).  The model and experimental results are interpreted to draw conclusions about the system (art).  The conclusions are implemented in the system (science and art). 

## **2. Computer simulation models conform both to system structure and to available system data** (Pritsker, 1989). 

Simulation models emphasize the direct representation of the structure and logic of a system as opposed to abstracting the system into a strictly mathematical form. The availability of system descriptions and data influences the choice of simulation model parameters as well as which system objects and which of their attributes can be included in the model.  Thus, simulation models are analytically intractable, that is exact values of quantities that measure system performance cannot be derived from the model by mathematical analysis.  Instead, such inferencing is accomplished by experimental procedures that result in statistical estimates of values of interest.  Simulation experiments must be designed as would any laboratory or field experiment.  Proper statistical methods must be used in observing performance measure values and in interpreting experimental results. 

## **3. Simulation supports experimentation with systems at relatively low cost and at little risk.** 

Computer simulation models can be implemented and experiments conducted at a fraction of the cost of the P-D-C-A cycle of lean used to improve the future state to reach operational performance objectives.  Simulation models are more flexible and adaptable to changing requirements than P-D-C-A.  Alternatives can be assessed without the fear that negative consequences will damage day-to-day operations.  Thus, a great variety of options can be considered at a small cost and with little risk. 

For example, suppose a lean team want to know if a new proposed layout for a manufacturing facility would increase the throughput and reduce the cycle time.  The existing layout could be 

1-7 

changed and the results measured, consistent with the lean approach.  Alternatively, simulation could be used to assess the impact of the proposed new layout. 

## **4. Simulation models adapt over the course of a project.** 

As was discussed in the previous section, simulation projects can result in the iterative definition of models and experimentation with models.  Simulation languages and software environments are constructed to help models evolve as project requirements change and become more clearly defined over time. 

## **5. A simulation model should always have a well-defined purpose.** 

A simulation model should be built to address a clearly specified set of system design and operation issues.  These issues help distinguish the significant system objects and relationships to include in the model from those that are secondary and thus may be eliminated or approximated.  This approach places bounds on what can be learned from the model.  Care should be taken not to use the model to extrapolate beyond the bounds. 

## **6. "Garbage in - garbage out" applies to models and their input parameter values** (Sargent, 2009). 

A model must accurately represent a system and data used to estimate model input parameter values must by correctly collected and statistically analyzed.  This is illustrated in Figure 1-3. 

**==> picture [332 x 170] intentionally omitted <==**

**----- Start of picture text -----**<br>
System<br>--------------------<br>Model-Related<br>Data<br>Validation Validation<br>Model:  Verification Model:<br>Computer  Specification<br>Implementation (Conceptual<br>Model)<br>**----- End of picture text -----**<br>


Figure 1-3:  Model Validation and Verification. 

There are two versions of a simulation model, the one specified "on paper" (the conceptual model) in the first strategic phase of the project process and the one implemented in the computer in the second strategic phase.  Verification is the process of making sure these two are equivalent.  Verification is aided, at least in part, by expressing the "on paper" model in a graphical drawing whose computer implementation is automatically performed. 

Validation involves compiling evidence that the model is an accurate representation of the system with respect to the solution objectives and thus results obtained from it can be used to make decisions about the system under study.  Validation has to do with comparing the system and the data extracted from it to the two simulation models and experimental results.  Conclusions drawn from invalid models could lead to system "improvements" that make system performance worse 

1-8 

instead of better.  This makes simulation and system designers who use it useless in the eyes of management. 

## **7. Variation matters.** 

A story is told of a young university professor who was teaching an industrial short course on simulation.  He gave a lengthy and detailed explanation of a sophisticated technique for estimating the confidence interval of the mean.  At the next break, a veteran engineer took him aside and said "I appreciate your explanation, but when I design a system I pretty much know what the mean is.  It is the variation and extremes in system behavior that kill me." 

Variation has to do with the reality that no system does the same activity in exactly the same way or in the same amount of time always.  Of course, estimating the mean system behavior is not unimportant.  On the other hand, if every aspect of every system operation always worked exactly on the average, system design and improvement would be much easier tasks.  One of the deficiencies of lean is that such an assumption is often implicitly made. 

Variation may be represented by the second central moment of a statistical distribution, the variance.  For example, the times between arrivals to a fast food restaurant during the lunch hour could be exponentially distributed with mean 10 seconds and, therefore, variance 100 seconds. Variation may also arise from decision rules that change processing procedures based on what a system is currently doing or because of the characteristics of the unit being processed.  For instance, the processing time on a machine could be 2 minutes for parts of type A and 3 minutes for parts of type B. 

There are two kinds of variation in a system: special effect and common cause.  Special effect variation arises when something out of the ordinary happens, such as a machine breaks down or the raw material inventory becomes exhausted because of an unreliable supplier.  Simulation models can show the step by step details of how a system responds to a particular special effect. This helps managers respond to such occurrences effectively. 

Common cause variation is inherent to a normally operating system.  The time taken to perform operations, especially manual ones, is not always the same.  Inputs may not be constantly available or arrive at equally spaced intervals in time.  They may not all be identical and may require different processing based on particular characteristics.  Scheduled maintenance, machine set up tasks, and worker breaks may all contribute. Often, one objective of a simulation study is to find and assess ways of reducing this variation. 

Common cause variation is further classified in three ways.  Outer noise variation is due to external sources and factors beyond the control of the system.  A typical example is variation in the time between customer orders for the product produced by the system.  Variational noise is indigenous to the system such as the variation in the operation time for one process step.  Inner noise variation results from the physical deterioration of system resources.  Thus, maintenance and repair of equipment may be included in a model. 

## **8. Looking at all the simulated values of performance measures helps.** 

Computer-based simulation experiments result in multiple observations of performance measures.  The variation in these observations reflects the common cause and special effect variation inherent in the system.  This variation is seen in graphs showing all observations of the performance measures as well as histograms and bar charts organizing the observations into categories.  Summary statistics, such as the minimum, maximum, and average, should be computed from the observations. Figure 1-4 shows three sample graphs. 

1-9 

**==> picture [369 x 407] intentionally omitted <==**

**----- Start of picture text -----**<br>
Example Throughput Graph<br>96<br>throughput<br>50<br>0<br>0<br>0 20 40 60 80 100<br>0 time2 96<br>Time<br>Example Number of Busy Machines Graph<br>6 6<br>4<br>busy<br>2<br>1<br>0<br>0 10 20 30 40 50<br>0 time1 41.062<br>Time<br>#  o f U n it s<br>be r<br>N u m<br>**----- End of picture text -----**<br>


**==> picture [323 x 187] intentionally omitted <==**

**----- Start of picture text -----**<br>
Example Work in Process Inventory Graph<br>12<br>10<br>wip i<br>5<br>0<br>0<br>0 10 20 30 40 50 60 70<br>0 time i 70<br>Time<br>#  o f U n it s<br>**----- End of picture text -----**<br>


Figure 1-4:  Example Graphs for Performance Measure Observations 

1-10 

The first shows how a special effect, machine failure, results in a build up of partially completed work.  After the machine is repaired, the build up declines.  The second shows the pattern of the number of busy machines at one system operation over time.  The high variability suggests a high level of common cause variation and that work load leveling strategies could be employed to reduce the number of machines assigned to the particular task.  The third graph shows the total system output, called throughput, over time.  Note that there is no increase in output during shutdown periods, but otherwise the throughput rate appears to be constant. 

Figure 1-5 shows a sample histogram and a sample bar chart.  The histogram shows the sample distribution of the number of discrete parts in a system that appears to be acceptably low most of the time.  The bar chart shows how these parts spend their time in the system.  Note that one-half of the time was spent in actual processing which is good for most manufacturing systems. 

**==> picture [332 x 172] intentionally omitted <==**

**----- Start of picture text -----**<br>
Example Work in Process Histogram<br>35 40<br>30<br>range l<br>20<br>10<br>3<br>0<br>1 0 1 2 3 4 5 6<br> 1 l 6<br>Number of Units<br>P e rce n t a g e  o f T i m e<br>**----- End of picture text -----**<br>


**==> picture [370 x 204] intentionally omitted <==**

**----- Start of picture text -----**<br>
Example Cycle Time Bar Chart<br>60%<br>50%<br>40%<br>30%<br>20%<br>10%<br>0%<br>Processing Time Wait Processing Transport Time Wait Transport<br>**----- End of picture text -----**<br>


Figure 1-5:  Example Histogram and Bar Charts for Performance Measure Observations 

1-11 

## **9. Simulation experimental results conform to unique system requirements for information.** 

Using simulation, the analyst is free to define and compute any performance measure of interest, including those unique to a particular system.  Transient or time varying behavior can be observed by examining individual observations of these quantities.  Thus, simulation is uniquely able to generate information that leads to a thorough understanding of system design and operation. 

Though unique performance measures can be defined for each system, experience has shown that some categories of performance measures are commonly used: 

1. System outputs per time interval (throughput) or the time required to produce a certain amount of output (makespan). 

2. Waiting for system resources, both the number waiting and the waiting time. 

3. The amount of time, lead time, required to convert individual system inputs to system outputs. 

4. The utilization of system resources. 

5. Service level, the ability of the system to meet customer requirements. 

## **10. What goes into a model must come out or be consumed.** 

Every unit entering a simulation model for processing should be accounted for either as exiting the model or assembled with other units or destroyed.  Accounting for every unit aids in verification. 

## **11. Results for analytic models should be employed.** 

Analytic models can be used to enhance simulation modeling and experimentation.  Result of analytic models can be used to set lower and upper bounds on system operating parameters such as inventory levels.  Simulation experiments can be used to refine these estimates.  Analytic models and simulation models can compute the same quantities, supporting validation efforts. 

## **12. Simulation rests on the engineering heritage of problem solving.** 

Simulation procedures are founded on the engineering viewpoint that solving the problem is of utmost importance.  Simulation was born of the necessity to extract information from models where analytic methods could not.  Simulation modeling, experimentation, and software environments have evolved since the 1950’s to meet expanding requirements for understanding complex systems. 

Simulation assists lean teams in building a consensus based on quantitative and objective information.  This helps avoid “design by argument”.  The simulation model becomes a valuable team member and is often the focus of team discussions. 

This principle is the summary of the rest.  Problem solving requires that models conform to system structure and data (2) as well as adapting as project requirements change (4).  Simulation enhances problem solving by minimizing the cost and risk of experimentation with systems (3). Information requirements for problem solving can be met (9).  Analytic methods can be employed where helpful (11). 

1-12 

## _1.5 Approach_ 

The fundamental premise of this book is that learning the problems that simulation solves, as well as well as the modeling and experimental methods needed to solve these problems, is fundamental to understanding and using this technique. 

Simulation models are built both from knowledge of basic simulation methods and by analogy to existing models.   Similarly, computer-based experiments are constructed using basic experiment design techniques and by analogy to previous experiments.  This premise is the foundation of this book.  First, simulation methods for model building, simulation experimentation, modeling time delays and other random quantities as well as the implementation of simulation experiments on a computer are presented in the remaining chapters in this part of the book. 

While each simulation model of each system can be unique, experience has shown that models have much in common.  These common elements and their incorporation into models are discussed in chapter 2.  These elementary models, as well as extensions, embellishments, and variations of them, are used in building the models employed in the application studies. 

Starting in the next part of the book, the simulation project process discussed in section 1.4 is used in application studies involving a wide range of systems.  Basic simulation modeling, experimentation, and system design principles presented in part 1 are illustrated in the application study.  Additional simulation modeling and experimental methods applicable to particular types of problems are introduced and illustrated.  Readers are asked to solve application problems based on the application studies and related simulation principles. 

## _1.6 Summary_ 

Simulation is a widely applicable modeling and analysis method that assists in understanding the design and operations of diverse kinds of systems. A simulation process directs the step by step activities that comprise a simulation project.  Basic methods, principles, and experience guide the development and application of simulation models and experiments. 

## **Questions for Discussion** 

1. List ways of validating a simulation model. 

2. Why might building a model graphically be helpful? 

3. List the types of variation and tell why dealing with each is important in system design. 

4. Differentiate "art" and "science" with respect to simulation. 

5. What is the engineering heritage influence on the use of models? 

6. Why does variation matter? 

7. Why is the simulation project process iterative? 

8. How does the simulation project process foster interaction between system experts and simulation modelers? 

9. Why must simulation experiments be designed? 

10. Why does a simulation project require both a model and an experiment? 

11. List the steps in the simulation process. 

1-13 

12. List three ways in which the credibility of a simulation model could be established with managers and system experts. 

13. Distinguish between verification and validation. 

14. Make two lists, one of the simulation project process activities that managers and system experts participate in and one of those that they don’t. 

## **Active Learning Exercises.** 

1. Create a paper clip assembly line.  A worker at the first station assembles two small paper clips.  A worker at the second station adds one larger paper clip.  One student feeds the first station with two paper clips at random intervals.  Another student observes the line to note the utilization of the stations, the number of assemblies in the inter-station buffer, and the number of completed assemblies.  Run the assembly line for 2 minutes.  Discuss how this exercise is like a simulation model and experiment. 

2. Have the students act out the operation of the drive through window of a fast food restaurant in the following steps. 

a. Enter line of cars b. Place order c. Move to pay window d. Pay for order e. Move to pick-up window f. Wait for order to be delivered g. Depart 

Before beginning, define performance measures and designate students to keep track of them. Emphasize that the actions taken by the students are the ones performed by the computer during a simulation. 

1-14
