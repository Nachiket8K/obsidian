---
title: "Chapter 4"
book: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li"
source_pdf: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li.pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 4** 

## **Conducting Simulation Experiments** 

## _4.1 Introduction_ 

This chapter provides the information necessary to design, carry out, and analyze the results of a **simulation experiment** .  Experimentation with a simulation model, as opposed to an exact analytic solution obtained using mathematics, is required.  Principle 2 states that simulation models conform both to system structure and to available system data.  Conditional logic is employed.  Thus, these models usually cannot be solved by analytic methods.  Simulation experiments must be properly designed and conducted as would any field or laboratory experiment.  The design of simulation experiments leads to the benefits of simulation described by principle 3: lower cost and more flexibility than physical prototypes as well as less risk of negative consequence on day-to-day operations than direct experimentation with existing, operating systems as the plan-do-check-act (PDCA) cycle of lean would do. 

The design of a simulation experiment specifies how model processing generates the information needed to address the issues and to meet the solution objectives identified in the first phase of the simulation process.  An approach to the analysis of results is presented, including ways of examining simulation results to help understand system behavior as well as the use of statistical methods such as confidence interval estimation to help obtain evidence about performance, including the comparison of scenarios. 

Prerequisite issues to the design and analysis of any simulation experiment are discussed. These include verification and validation as well as the need to construct independent observations of simulation performance measures and to distinguish between probability and degree of confidence. 

Verification and validation are discussed first followed by a discussion of the need to construct independent observations of performance measures.  The design elements of simulation experiments are explained.  Finally, an approach to the analysis of terminating simulation results is given along with an explanation of how probability and degree of confidence are differentiated. 

The discussion in this chapter assumes some prior knowledge of data summarization, probability, and confidence interval estimation. 

## _4.2 Verification and Validation_ 

This section discusses the verification and validation of simulation models.  Verification and validation, first described in principle 6 of chapter 1, have to do with building a high level of confidence among the members of a project team that the model can fulfill is objectives. Verification and validation are an important part of the simulation process particularly with respect to increasing model credibility among managers and system experts. 

Verification has to do with developing confidence that the computer implementation of a model is in agreement with the conceptual model as discussed in chapter 1.  In other works, the computer implementation of the model agrees with the specifications given in the conceptual model. Verification includes debugging the computer implementation of the model. 

Validation has to do with developing confidence that the conceptual model and the implemented model represent the actual system with sufficient accuracy to support making decision about project issues and to meet the solution objectives.  In other works, the computer implementation of the model and the conceptual model faithfully represent the actual system. 

4-1 

As described by many authors (Balci, 1994; Balci, 1996; Banks, Carson, Nelson, and Nicol, 2009; Carson, 2002; Law, 2007; Sargent, 2009), verification and validation require gathering evidence that the model and its computer implementation accurately represent the system under study with respect to project issues and solution objectives.  Verification and validation are a matter of degree.  As more evidence is obtained, the greater the degree of confidence that the model is verified and valid increases.  It should be remember however that absolute confidence (100%) cannot be achieved.  There will always be some doubt as to whether a model is verified and validated. 

How to obtain verification and validation evidence and what evidence to obtain is case specific and requires knowledge of the problem and solution objectives.  Some generally applicable strategies are discussed and illustrated in the following sections.  The application studies, starting in chapter 6, provide additional examples.  Application problems in the same chapters give students the opportunity to practice verification and validation. 

Verification and validation strategies are presented separately for clarity of discussion.  However in practice, verification and validation tasks often are intermixed with little effort to distinguish verification from validation.  The focus of both verification and validation is on building confidence that the model can be used to meet the objectives of the project. 

## **A pre-requisite to a proper simulation experiment is verifying and validating the model.** 

Throughout this chapter, including the discussion of verification and validation, illustrations and examples will make use of a model of two stations in a series with a large buffer between the stations as well as the industrial example presented in section 1.2.  A diagram of the former is shown in Figure 4-1.  A part enters the system, waits in the buffer of workstation A until the machine at this workstation is available.  After processing at workstation A, a part moves to workstation B where it waits in the buffer until the workstation B machine is available.  After processing at workstation B, a part leaves the system.  Note that because it is large, the buffer between the stations is not modeled. 

**==> picture [87 x 45] intentionally omitted <==**

**==> picture [87 x 45] intentionally omitted <==**

## 4.2.1 Verification Procedures 

Some generally applicable techniques for looking for verification evidence follow. 

## **1. What goes into a model must come out or be consumed.** 

For example, in the two workstations in a series model, the following “entity balance” equation should hold: 

Number of entities entering the system = 

the number of entities departing the system + the number of entities still in the system at the end of the simulation 

4-2 

The latter quantity consists of the number of entities in each workstation buffer (A and B) plus the number of entities being processed at workstations A and B.  If the entity balance equality is not true, there is likely an error in the model that should be found and corrected. 

The number of entities entering the system consists of the number of entities initially there at the beginning of the simulation plus the number of entities arriving during the simulation. 

For example, for one simulation of the two workstations in a series model, there were 14359 entities arriving to the model of which 6 were there initially.  There were 14357 entities that departed and two entities in the system at the end of the simulation.  One of the two entities was in the workstation A operation and the other was in the workstation B operation. 

## **2. Compare the process steps of the computer model and the conceptual model.** 

The process steps in the model implemented in the computer version of the model and the conceptual model should correspond and any differences should be corrected or justified. 

The process steps in the two workstations in a series model are as follows: 

1. Arrive to the system. 

2. Enter the input buffer of workstation A. 

3. Be transformed by the workstation A operation. 

4. Be moved to and enter the input buffer of workstation B. 

5. Be transformed by the workstation B operation. 

6. Depart the system. 

## **3. Check all model parameter values input to the model.** 

The model implementation should include the checking required to assure that input parameter values are correctly input and used. 

For example in the industrial application discussed in section 1.2, customer demand volume is input.  The volume of product shipped is output.  Enough information is included in the reports generated by the model to easily determine if all of the input volume is shipped or is awaiting shipment at the end of the simulation. 

## **4. Check all entity creations.** 

The time between arrivals is specified as part of the model.    The average number of arrivals can be computed given the ending time of the simulation.  In addition, the number of arrivals during the simulation run is usually automatically reported.  These two quantities can be compared to assure that entities are being created as was intended. 

For example, suppose model of the two stations in a series was simulated for 40 hours with an average time between arrivals of 10 seconds.  The expected number of arrivals would be 14400 (= 40 hours / 10 seconds).  Suppose 20 independent simulations were made and the number of arrivals ranged from 14128 to 14722.  Since this range includes 14400, verification evidence would be obtained.  How to do the independent simulations is discussed in section 4.3 and following. 

Alternatively a confidence interval for the true mean number of arrivals could be computed.  If this confidence interval includes the expected number of arrivals verification evidence is obtained.  In the same example, the 95% confidence interval for the mean number of arrivals is 14319 to 14457.  Again, verification evidence is obtained. 

4-3 

## **5. Check the results of all logical decisions.** 

Sufficient checking should be built into the simulation model to assure that all logical decisions are correctly made that is all conditional logic is correctly implemented. 

For example in the industrial problem discussed in section 1.2, each product could be shipped from one of a specified set of loads spots.  Output reports showed the volume of shipments by product and load spot combination.  Thus, it could be easily seen if a product was shipped from the wrong load spot. 

## **6. Implement the simplest possible version of the model first and verify it.  Add additional capabilities to the model one at a time.  Perform verification after each capability is added.** 

Verifying that any complex computer program was implemented as intended can be difficult. Implementing the smallest possible model helps simplify the verification task, and perhaps more importantly, results in a running model in relatively little time.  Verifying one capability added to an already verified model is relatively straightforward. 

For example, the model of the industrial problem presented in section 1.2, has been developed over a number of years with new capabilities added to support addressing new issues and solution objectives. 

## **7. For models developed by multiple individuals, used structured walk-throughs.** 

Each individual implements an assigned portion of the model, or sub-model.  Each individual presents the implementation to all of the other team members.  The team as a whole must agree that the implementation faithfully represents the conceptual model. 

For example, one strategy is to build and implement an initial model as quickly as possible from the specifications in the conceptual model.  If the conceptual model is incomplete, assumptions are made to complete model construction and implementation.  The assumptions may be gross or inaccurate.  The entire team reviews the initial model, especially the assumptions, and compares it to the conceptual model.  The assumptions are corrected as necessary.  This may require team members to gather additional information about how certain aspects of the system under study work. 

## **8.** 

## **Use the model builders available in most simulation environments.** 

Model builders implement the standard modeling constructs available in a simulation language. They provide a standard structure for model building and help guard against model building errors such as inconsistent or incomplete specification of modeling constructs. 

## **9. Output and examine voluminous simulation results.** 

Sufficient information should be output from the simulation to verify that the different components of the system are operating consistently with each other in the model. 

For example in the industrial problem of section 1.2, both the utilization of each load spot and summary statistics concerning the time to load each product are reported.  If the load spots assigned to a product have high utilization, the average product loading time should be relatively long. 

4-4 

## **10. Re-verify the model for each set of model parameter values tested.** 

A model implementation can be verified only with respect to the particular set of model parameter values tested.  Each new set of parameter values requires re-verification.  However after many sets of parameter values have been tested, confidence is gained that the implementation is correct for all sets of parameter values in the same range. 

For example for the industrial problem of section 1.2, verification information is carefully examined after each simulation experiment. 

## 4.2.2 Validation Procedures 

Some generally applicable techniques for looking for validation evidence follow. 

## **1. Compare simulation model results to those obtained from analytic models.** 

This is a restatement of principle 11 of chapter 1. For example, the mean number of busy units of a resource can be computed easily as discussed in chapter 6. 

In the two workstations in a series model, suppose the operation time at the second workstation is a constant 8.5 seconds and the mean time between arrivals is 10 seconds.  The percentage busy time for workstation B is equal to 8.5 / 10 seconds or 85%.  The simulation of the workstation provides data from which to estimate the percent busy time.  The range of workstation B utilization over multiple independent simulations is 83% to 87%.  A confidence interval for the true mean utilization could be computed as well.  The 95% confidence interval is 84.4 to 85.4.  Thus, validation evidence is obtained. 

## **2. Use animation to view simulation model dynamics, especially those involving complex conditional logic.** 

Reviewing all the implications of complex decisions using voluminous information in a static medium, such as a report, or even in an interactive debugger, is difficult and possibly overwhelming.  Animation serves to condense and simplify the viewing of such information. 

Consider the following illustration.  In the early 1980’s, a particular simulation company was developing its first commercial animator product.  Having completed the implementation and testing, the development team asked an application consultant for an industrial model to animate. The consultant supplied a model that included a complex control system for a robot. 

The developers completed the animation and presented it to the consultant.  The response of the consultant was that there must be something wrong with the new animation software as the robot could not engage in the sequence of behavior displayed. 

Try as they might, the development team could not find any software error in the animator.  To aid them, the team asked the consultant to simulate the model, printing out all of the information about the robot’s behavior.  The error was found not in the animator, but in the model.  The disallowed behavior pattern occurred in the simulation! 

This is not a criticism of the consultant.  Rather it points out how easy it was to see invalid behavior in an animation though it was infeasible to detect it through a careful examination of the model and output information. 

4-5 

## **3. Involve system experts and managers** 

System experts should review the model, parameter values and simulation results for consistency with system designs and expectations.  Reports of simulation results should be presented in a format that is understandable to system experts without further explanation from the modelers. Animation can help in answering questions such as: How was the system represented in the model?  Inconsistencies and unmet expectations must be resolved as either evidence of an invalid model or unexpected, but valid, system behavior. 

For example the development process for the industrial model discussed in section 1.2 was as follows.  A first cut model was developed as quickly after the start of the project as possible.  It was clear during the development of this model that some components of the system had not been identified or had incomplete specifications that is the first draft conceptual model was incomplete.  The modelers made gross assumptions about how these components operated. The first cut model was reviewed by the entire project team including system experts and managers.  Based on this review, tasks for completing the conceptual model were assigned. When these tasked were completed, the conceptual model was updated and the implemented model was revised accordingly. 

## **4. If some quantities are estimated by system experts and managers, test their effect on system outputs.** 

As discussed in chapter 3, there may be a lack of data available for estimating time delays or other quantities needed in a model.  This is common when the simulation model is being used to assist in the design of a new system.  For such quantities, it is essential to perform a sensitivity analysis.  This involves running the model with a variety of values of each estimated quantity and observing the effect on performance measures.  Estimated quantities that greatly effect system performance should be identified.  Further study may be necessary to obtain a more precise estimate of their value. 

For example, there was little data concerning shipping times, the time between when a product left the plant and when it arrived at a customer, for the industrial model discussed in section 1.2. These times were believed to be directly related to some of the key performance measures estimated by the model.  Thus, it was thought to be wise to refine them over time.  Initially, shipping times were specified as triangularly distributed with estimates of the minimum, maximum, and modal times for all products in general supplied by logistics experts.  Later additional data was available so that shipment times were available for each group of products. Still later, an analysis of data in the corporate information system was done to provide product specific shipping times.  The simulation model was modified to allow any of the three shipping time options to be used for any product. 

## **5. Carefully review a trace of a simulation run.** 

A model specific report of the step-by-step actions taken during a run can be generated by the simulation in a format that can be read by system experts and managers.  A careful examination of such a report, though tedious, can help assure that the process steps included in the simulation model are complete and correctly interact with each other. 

For example, the sponsors of an industrial inventory management simulation required such a trace to assure that the model correctly captured the response of the actual system to certain disturbances.  The trace was carefully examined by the sponsors and other system experts to gain confidence that the model was valid. 

4-6 

## **6. Compare performance measure values to system data to see if any operationally significant differences can be observed.** 

The same performance measures computed in the model may be estimated from data collected from an existing system.  Summary statistics, such as the average, computed from performance measure values may be compared by inspection to summary statistics computed from the data collected from an existing system.  If no operationally significant differences are observed, then validation evidence is obtained. 

Law (2007) discusses the difficulty of using statistical tests to compare performance measure values and real world data as well as making some recommendations in this regard. 

For example, in the industrial model of section 1.2, system experts believed that empty rail cars spent 6 to 7 days in the plant.  Simulation results estimated that empty rail cars spent an average of 6.6 days in the plant.  Thus, validation evidence was obtained. 

## _4.3 The Problem of Correlated Observations_ 

Most statistical analysis procedures require independent (and identically distributed) observations of performance measure values.  However, the observations in a simulation experiment are typically dependent (correlated).  This section illustrates why a simulation experiment generates correlated observations.  Approaches to dealing with this issue are presented later in this chapter. 

Consider the time the nth part arriving to workstation A in the two stations in a series model would spend at the workstation: 

Time at workstation An = Time in buffern + Operation timen 

The time in the buffer for the nth part is composed of the operation times for the parts that preceded it in processing while the nth part was in the buffer.  For example, suppose the fourth part to arrive does so while the second part to arrive is being processed.  So the time the fourth part spends in the buffer is equal to a portion of the operation time for the second part and the entire operation time for the third part: 

Time at workstation4 = f(operation time2, operation time3) + Operation time4 

Thus, the time spent at the workstation by the fourth part is correlated with the time spent by the second and the third parts. 

Rather than using correlated performance measure observations directly in statistical analysis computations, independent observations are constructed.  How to do this is discussed later in this chapter. 

**The statistical analysis of simulation results is greatly aided by the construction of independent observations of the performance measures.** 

4-7 

## _4.4 Common Design Elements_ 

The elements common to all simulation experiments are discussed in the following sections. These include model parameters and their values, performance measures, and random number streams. 

## 4.4.1 Model Parameters and Their Values 

Model parameters correspond to system control variables or operational rules whose values can be changed to meet the solution objectives defined in the first step of the simulation process. Values of model parameters can be quantitative such as the size of a buffer or qualitative such as which routing policy to use. 

Often in traditional experimental design and analysis, time and cost constraints result in the use of only two or three values of each model parameter.  Simulation affords the opportunity to test as many values as time and computing resources allow.  For example, various sizes of an interstation buffer could be simulated.  A very large size could represent an infinite buffer.  A buffer size of one or two would be minimal.  Intermediate buffer sizes such as five and ten could be evaluated. 

Which values are used may depend on the results of preceding simulations.  For example, results of the initial simulations may indicate that a buffer size in the range 10 to 20 is needed.  Additional simulations would be run with for buffer sizes between 10 and 20. 

## **Model parameters must be defined and their values specified.** 

## 4.4.2 Performance Measures 

Performance measures are quantities used to evaluate system behavior.  They are defined in accordance with principle 9 of chapter 1: “Simulation experimental results conform to unique system requirements for information.”  Thus, each simulation experiment could have different performance measures. 

Possible performance measures for experiments with the two stations in a series model could be as follows: 

1. The number of items waiting in each buffer. 

2. The percentage of time each workstation is busy. 

3. The percentage of time each workstation is idle. 

4. The time an item spends in the system (lead time). 

5. The total number of items processed by the workstation. 

Note that state variable values are used as performance measures along with the time taken by entities in one, more than one, or all of the processing steps.  A count of the number of entities completing processing is desired as well.  These kinds of performance measures are typical of many simulation experiments. 

## **Performance measures must be defined, including how each is computed.** 

## 4.4.3 Streams of Random Samples 

One purpose of a simulation experiment is comparing scenarios.  Suppose that no statistically significant difference between two scenarios is found.  This could occur because the scenarios do not cause distinct differences in system performance.  A second and undesirable possibility is that the variance of the observations made during the simulation is too high to permit true differences in system observations to be confirmed statistically. 

4-8 

Suppose we wished to assess a change in the operation of workstation A in the two stations in a series model where the range of the operation time is reduced to uniformly distributed between 7 and 11 seconds from uniformly distributed between 5 and 13 seconds.  The same arrivals could be used in simulating both scenarios.  Thus, the comparison could be made with respect to the same set of entities processed by the workstation.  In general, this approach is referred to as the method of **common random numbers** since simulations of the two scenarios have the same pattern of arrivals in common.  Each time between arrivals was determined by taking a random sample from the exponential distribution modeling this quantity.  How this is done will be discussed in the next chapter. 

To better understand the effect of common random numbers, consider what happens when they are not used.  There would be a different set of arrivals in the simulation of the first scenario than in the simulation of the second scenario. Observed differences in performance measure values between the two scenarios could be due to the differences in the arrivals or true differences between the scenarios.  Thus, the variance associated with summary statistics of differences in values, such as the mean lead time, would likely be higher than if common random numbers were used.  This higher variance might result in a failure to detect a true difference between the scenarios with respect to a given performance measure such as lead time even if such a difference existed. 

The method of common random numbers requires distinct streams of samples for each quantity modeled by a probability distribution.  While this does not guarantee a reduction in the variance of the difference, experience has shown that a reduction often occurs.  In practice for most simulation languages, this means that the stream of samples associated with each quantity modeled by a probability distribution must be given a distinct name. 

Law (2007) more details concerning the common random number approach as well as other experiment design techniques to control the variance.  Banks, Carson, Nelson, and Nicol (2009) discuss these techniques as well. 

## **The quantities modeled by probability distributions in a model must be identified and uniquely named the method of common random numbers may be employed.** 

## _4.5 Design Elements Specific to Terminating Simulation Experiments_ 

A **terminating simulation experiment** ends at a specified simulation time or event that is derived from the characteristics of the system under study and is stated as a part of the experiment design.  This is the distinguishing characteristic of such as an experiment. 

This section presents the design elements that are specific to terminating simulation experiments. These include setting initial conditions, specifying the number of replications of the experiment, and specifying the ending time or event of the simulation. 

## 4.5.1 Initial Conditions 

To begin a simulation, the initial values of the state variables and the initial location in the model of any entities, along with their attribute values, must be specified.  Together, these are called the **initial conditions** . 

In a terminating simulation, the initial conditions should be the same as conditions that occur in the actual system (Law, 2007).  The work of Wilson and Pritsker (1978) leads toward using the modal or, at least, frequently occurring conditions.  This must be done to ensure there is not a statistically significant greater portion of performance measure values in any given range gathered from the simulation than would occur in the actual system.  Thus, **statistical bias** is 

4-9 

collecting performance measure values that could not have occurred, or in greater (lesser) proportion in one range than could have occurred, in the actual system. 

Consider again the two work stations in a series model.  For example, suppose it is known that parts are almost always in the buffer of workstation A and of workstation B.  Thus possible initial conditions are: 

1. The workstation A resource is in the BUSY state processing one part. 

2. The workstation B resource is in the BUSY state processing one part. 

3. Two parts are in the buffer of workstation A. 4. Two parts are in the buffer of workstation B. 

Note that the time spent at either workstation by a part will consist of the time spent in the input buffer plus the operation time.  If the simulation experiment begins with no parts in either input buffer, the time the first part spends at each workstation is equal to the operation time because the time spent in the input buffer will be zero.  The observed lead time for this part will be less than for any part processed by the actual system. 

Statistical bias is illustrated in Figure 4-2 that shows example histograms of part time in the system collected from the actual system and from a simulation.  The simulation has improper initial conditions of no parts at the workstation.  Some of the simulation observations are biased low.  Calculations of statistics based on statistically biased observations may also be biased and inaccurate conclusions about problem root causes or the performance of proposed solutions drawn. 

## **The initial conditions must be specified as a part of the experimental design and must be actual conditions that occur in the system.** 

**==> picture [345 x 190] intentionally omitted <==**

**----- Start of picture text -----**<br>
Lead Time: Simulated and Actual Values<br>14<br>12<br>10<br>8 Simulated Values<br>6 Actual Values<br>4<br>2<br>0<br>0-10 11-20 21-30 31-40<br>Lead Time<br>Number of Observations<br>**----- End of picture text -----**<br>


**Figure 4-2:  Illustration of Statistical Bias** 

## 4.5.2 Replicates 

This section discusses the idea of replication to construct independent observations of simulation performance measures. **Replicates** of a simulation experiment differ from each other only in the sample values of the quantities modeled by probability distributions.  Replicates are treated as independent of each other since the sample values exhibit no statistical correlation. 

4-10 

Each replicate is one possibility of how the random behavior of the system actually occurred. Multiple possibilities for system behavior should be examined in detail to draw conclusions about the effectiveness of system scenarios in meeting solution objectives. 

Consider again the two work stations in a series model.  There is a stream of sample values for the time between arrivals and another stream for operation times at workstation A.  A replicate is defined by the particular samples taken in these two streams.  Examining system performance for other streams of the time between arrivals and of service times is necessary.   These other streams define additional replicates. 

Observations of the same performance measure from different replicates are statistically independent of each other.  In addition, performance measure observations from different replicates are identically distributed for the same reason.  Thus replication is one way of constructing independent observations for statistical analysis.  However, since performance measures may be arbitrarily defined, the underlying probability distribution of the performance measure observations cannot be determined in general. 

During each replicate, one or more observations of the values of a performance measure are made.  For example, the number of entities that complete processing in the two work stations in series model is incremented each time processing is finished, the lead time is recorded each time an entity completes processing, and the number of entities in either workstation buffer is updated each time an entity arrives at a workstation as well as each time an entity begins processing. 

For the reasons discussed in section 4.3, each replicate can produce only one independent sample, xi. This independent sample is often a statistic computed from the observations of a performance measure, usually the average, minimum, or maximum.  For example, one average of the number in the buffer at a workstation A is computed from all of observations made during one replicate.  This average is one independent sample of the average number in the buffer. 

Statistical summaries are estimated from the xi’s.  These summaries typically include the average, standard deviation, minimum, and maximum.  Confidence intervals are also of interest. 

In summary, each simulation experiment consists of n replicates.  Within each replicate and for each performance measure, one or more observations are made.  From the observations, one or more statistics are typically computed.  Each such statistic is the independent observation, xi, produced by the replicate. 

For example, a simulation experiment concerning the two work stations in a series model could consist of 20 replicates.  The number of entities in the workstation A buffer could be observed. Each time the number in the buffer changes an observation is made.  The average number in the buffer as well as the maximum number in the buffer is computed.  There are 20 independent observations of the average number in the buffer as well as 20 independent observations of the maximum number in the buffer. 

The number of replicates initially made is generally determined by experience and the total amount of real (“clock”) time needed to compute the simulation.  Most of the time, this number is in the range 10-30.  More replicates may be needed if the width of a confidence interval computed from the performance measure observations is considered to be too wide.  Confidence interval estimation is discussed later in this chapter. 

## **The number of replications of the simulation experiment must be specified.** 

4-11 

## 4.5.3 Ending the Simulation 

This section discusses the time or condition that determines when to end a replicate. 

An ending time for a replicate arises naturally from an examination of most systems.  A manufacturer wants to know if its logistic equipment will suffice for the next budget period of one year.  So the end of the budget year becomes the simulation ending time.  A fast food restaurant does most of its business from 11:30 A.M to 12:30 P.M.  Thus the simulation ending time is one hour.  The experiment for a production facility model could cover the next planning period of three months.  After that time, new levels of demand may occur and perhaps new production strategies implemented.  The simulation experiment for a production facility could end when 100 parts are produced. 

## 4.5.4 Design Summary 

The specification of design elements for a terminating simulation experiment can be accomplished by completing the template shown in Table 4-1. 

**Table 4-1:  Terminating Simulation Experiment Design** 

|**Element of the Experiment**|**Values for a Particular Experiment**|
|---|---|
|Model Parameters andTheir Values||
|PerformanceMeasures||
|Random NumberStreams||
|InitialConditions||
|Numberof Replicates||
|Simulation EndTime /Event||



Consider a terminating simulation experiment for the two workstations in a series model.  The time between arrivals and the operation time at workstation A are modeled using probability distributions.  Performance measures include the number in the buffer at each workstation, the state of the each workstation (BUSY or IDLE), and entity lead time.  The model parameter is the machine used at workstation A, either the current machine with operation time uniformly distributed between 5 and 13 seconds or a new machine with operation time uniformly distributed between 7 and 11 seconds.  The initial conditions are two items in each buffer and both workstations busy.  Twenty replicates will be made for the planning horizon of one work week. The experimental design is shown in Table 4-2. 

**Table 4-2:  Simulation Experiment Design for the Two Workstations in Series Model** 

|**Element of the Experiment**|**Values for a Particular Experiment**|
|---|---|
|Model Parameters andTheir Values|Workstation A Machine:Currentvs. New|
|Performance Measures|Number in the buffer at each workstation<br>State of each workstation<br>LeadTime|
|Random Number Streams|Time between arrivals<br>Operation Time|
|Initial Conditions|Two entities in each buffer<br>One entity in service at each workstation<br>(State of each workstation resource is<br>BUSY)|
|Numberof Replicates|20|
|Simulation EndTime /Event|1 week(40hours)|



4-12 

## _4.6 Examining the Results for a Single Scenario_ 

This section presents a strategy for examining the simulation results of a single system scenario as defined by one set of model parameter values.  Results are examined to gain an understanding of system behavior.  Statistical evidence in the form of confidence intervals is used to confirm that what is observed is not just due to the random nature of the simulation model and experiment and thus provides a valid basis for understanding system behavior. 

Simulation results are displayed and examined using graphs and histograms as well as summary statistics such as the mean, standard deviation, minimum, and maximum.  Patterns of system behavior are identified if possible.  Animation is used to display the time dynamics of the simulation.  This is in accordance with principle 8: Looking at all the simulated values of performance measures helps. 

How the examination of simulation results is successfully accomplished is an art as stated in principle 1.  Thus, this topic will be further discussed and illustrated in the context of each application study. 

The discussion in this session is presented in the context of the two work stations in a series model. 

## 4.6.1 Graphs, Histograms, and Summary Statistics 

Observed values for each performance measure can be examined via plots, histograms, and summary statistics.  To illustrate, each of these will be shown for the number of entities in the buffer of workstation A in the two workstations in a series model. 

A plot of the observed values of the number in this buffer from replicate one of the simulation experiment defined in Table 4-2 is shown in Figure 4-3.  The x-axis is simulated time and the y- axis is the number in the buffer of workstation A.  Note from the plot that most of the time the number in the buffer varies between 0 and 10.  However, there are several occasions that the number in the buffer exceeds 20.  This shows high variability at workstation A. 

**==> picture [425 x 201] intentionally omitted <==**

**----- Start of picture text -----**<br>
Station A Buffer<br>30<br>25<br>20<br>15<br>10<br>5<br>0<br>0 5 10 15 20 25 30 35 40 45<br>Simulation Hour<br>Number in Buffer<br>**----- End of picture text -----**<br>


**Figure 4-3:  Plot of the Number of Entities in the Workstation A Buffer** 

A histogram of the same observations is shown in Figure 4-4.  The percent of time that a certain number of entities is in the buffer is shown on the y-axis.  The number of entities is shown on the 

4-13 

x-axis.  Note that about 91% of the time there are 10 or less entities in the buffer of workstation A. However about 9% of the time there are more than 10 entities in the buffer. 

It would be wise to examine these same graphs from other replicates to see if the same pattern of behavior is observed.  If the software capability is available, a histogram combining the observations from all of the replicates would be of value. 

**==> picture [426 x 195] intentionally omitted <==**

**----- Start of picture text -----**<br>
Station A Buffer<br>60%<br>50%<br>40%<br>30%<br>20%<br>10%<br>0%<br>0 5 10 15 20 25 30<br>Number in Buffer<br>Percent of Time<br>**----- End of picture text -----**<br>


**Figure 4-4:  Histogram of the Number of Entities in the Workstation A Buffer** 

Summary statistics can be computed from the observations collected in each replicate.  However, these observations are likely not independent, so their standard deviation is not very useful.  The average, minimum, and maximum of the observations of the number in the buffer of workstation A from replicate 1 are given in Table 4-3.  The average number of entities is relatively low but the maximum again shows the high variability in the number in the buffer. 

**Table 4-3:  Summary Statistics for the Number of Entities in the Buffer of Workstation A – Replicate 1** 

|**Statistic**|**Value**|
|---|---|
|**Average**|4.1|
|**Minimum **|0|
|**Maximum **|26|



As was previously discussed, one independent observation each of the average, minimum, and maximum is generated by each replicate.  Suppose the average and maximum number in the buffer of workstation A are of interest.  The average corresponds to the average work-in-process (WIP) at the workstation and the maximum to the buffer capacity needed at the workstation. Table 4-4 summarizes the results for 20 replicates.  The average ranges from 3.1 to 6.6 with an overall average of 4.4.  This shows that the average number in the buffer has little variability.  The maximum shows significant variability ranging from 21 to 43 with an average of 31. 

4-14 

**Table 4-4:  Summary Statistics for the Number of Entities in the Buffer of Workstation A – Replicate 1 through 20** 

|**Replicate**|**Average Number in**<br>**the Workstation A**<br>**Buffer **|**Maximum Number in**<br>**the Workstation A**<br>**Buffer **|
|---|---|---|
|1|4.1|28|
|2|4.6|27|
|3|4.1|30|
|4|3.2|24|
|5|3.8|24|
|6|4.3|29|
|7|4.0|25|
|8|4.4|34|
|9|4.3|40|
|10|4.1|28|
|11|4.1|26|
|12|4.5|38|
|13|4.5|31|
|14|4.3|30|
|15|4.8|37|
|16|4.2|28|
|17|5.2|40|
|18|4.3|38|
|19|4.3|26|
|20|4.4|36|
|**Average**|4.3|31.0|
|**Std. Dev.**|0.39|5.4|
|**Minimum **|3.2|24|
|**Maximum **|5.2|40|



4.6.2 Confidence Intervals 

One purpose of a simulation experiment is to estimate the value of a parameter or characteristic of the system of interest such as the average or maximum number in the buffer of workstation A. The actual value of such a parameter or characteristic is most likely unknown.  Both a point estimator and an interval estimator are needed. The point estimator should be the center point of the interval. 

The average of the set of independent and identically distributed observations, one from each replicate, serves as a point estimator.   For example, the values in the “average” row of Table 4-4 are point estimators, the first of the average WIP in the buffer of workstation A and the second of the needed buffer capacity. 

The confidence interval estimation procedures recommend by Law (2007) will be used to provide an interval estimator.  The **t-confidence interval** given by equation 4-1 is recommended. 

**==> picture [418 x 28] intentionally omitted <==**

where tn is the 1-percentage point of the Student’s t distribution with n-1 degrees of freedom, n is the number of replicates, _X_ is the average (the values on the “average” row of Table 4-4 for example), and s is the standard deviation (the values on the “std. dev.” row of Table 

4-15 

4-4 for example).  The  sign means approximately.  The symbol  represents the actual but unknown value of the system parameter or characteristic of interest. 

The result of the computations using equation 4-1 is the interval shown in equation 4-2: 

|(lower bound||upper|upper|upper|upper|upper|upper|upper|upper|upper|upper|upper||bound) with 1-confidence|bound) with 1-confidence|bound) with 1-confidence|bound) with 1-confidence|bound) with 1-confidence|bound) with 1-confidence|(4-2)|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|where|||||||||||||||||||||
||||||||||||||||||||_s_||
|lower bound =|_X_||_t_|1||||||/|2||,|_n_||||*<br>1||(4-3)|
||||||||||||||||||||_n_||
||||||||||||||||||||_s_||
|upper bound =|_X_||_t_||1||||||/|2||,|_n_||||*<br>1|(4-4)|
||||||||||||||||||||_n_||



Equations 4-1 and 4-2 show the need to distinguish between probability and confidence. Understanding this difference may require some reflection since in everyday, non-technical language the two ideas are often used interchangeably and both are expressed as a percentage. 

A probability statement concerns a random variable.  Equation 4-1 contains the random variables 

_X_ and _s_ and thus is a valid probability statement.  The interpretation of equation 4-1 relies on the long run frequency interpretation of probability and is as follows:  If a very large number of confidence intervals are constructed using equation 4-1, the percentage of them that include the actual but unknown value of  is approximately 1-This percentage is called the **coverage** . 

The interval expressed in equation 4-2 contains two numeric values: lower bound and upper bound plus the constant  whose value is unknown.  Since there are no random variables in equation 4-2, it cannot be a probability statement.  Instead, equation 4-2 is interpreted as a statement of the degree of confidence (1-) that the interval contains the value of the system parameter or characteristic of interest.  Typical values for (1-) are 90%, 95%, and 99%.  A higher level of confidence implies more evidence that the interval contains the value of  

Some thoughts on how to interpret the level of confidence with respect to the kind of evidence provided is worthwhile.  Keller (2001) suggests the following, which will be used in this text. 

**Table 4-5. Interpretation of Confidence Values** 

|**Confidence (1-****) Range**|**Interpretation**|
|---|---|
|(1-)99%|Overwhelmingevidence|
|95%(1-) > 99%|Strongevidence|
|90%(1-) > 95%|Weak evidence|
|90% > (1-)|No evidence|



Note that the higher the level of confidence the greater the value of _t_ 1   / 2 , _n_  1 and thus the wider 

the confidence interval.  A narrow confidence interval is preferred so that the value of  is more precisely bounded.  However, it is clear that a high level of confidence must be balanced with the desire for a narrow confidence interval. 

Why equation 4-1 is approximate and not exact is worthy of discussion.  For equation 4-1 to be exact, the observations on which the confidence interval computations are based must come from a normal distribution as well as being independent and identically distributed.  As was previously discussed, the latter two conditions are met by the definition of a replicate while the first condition cannot be guaranteed since the performance measures in a simulation are arbitrarily defined. 

4-16 

Thus, equation 4-1 is approximate.  Approximate means that the coverage produced using equation 4-1 will likely be less than 1- 

Given that equation 4-2 provides only an approximate (not exact) level of confidence (not a probability), it is natural to ask why it should be used.  Law (2007) concludes that experience has shown that many real-world simulations produce observations of the type for which equation 4-1 works well, that is the coverage produced using equation 4-1 is close enough to 1- to be useful in conducting simulation studies.  In the same way, Vardeman and Jobe (2001) state that confidence intervals in general have great practical use, even though no probability statement can be made as to whether a particular interval contains the actual value of the system characteristic or parameter of interest.  Since confidence intervals seem to work well in general and in simulation studies, they will be used throughout this text. 

As an example, Table 4-6 contains the 99% confidence intervals computed from equation 4-2 for the average and maximum number of entities in the buffer of workstation A based on the results shown in Table 4-4. 

**Table 4-6:  99% Confidence Intervals for the Number of Entities in the Buffer of Workstation A Based on 20 Replicates** 

||**Average Number in**<br>**the Workstation A**<br>**Buffer **|**Maximum Number in**<br>**the Workstation A**<br>**Buffer **|
|---|---|---|
|**Average**|4.3|31.0|
|**Std. Dev.**|0.39|5.4|
|**99% CI –**<br>**Lower Bound**|4.0|27.5|
|**99% CI –**<br>**Upper Bound**|4.5|34.4|



The confidence interval for the average is small.  It would be safe to conclude that the average number in the buffer of workstation A was 4 (in whole numbers).  The confidence interval for the maximum number in the buffer ranges from 27 to 34 (in whole numbers).  If this range is deemed too wide to establish a buffer size additional replicates, say another 20, could be made. 

## 4.6.3 Animating Model Dynamics 

As discussed in chapter 1, simulation models and experiments capture the temporal dynamics of systems.  However, reports of models and experimental behavior are often confined to static mediums such as reports and presentations like those shown in the preceding sections.  The simulation process includes system experts and managers who may not be knowledgeable about modeling methods and may be skeptical that a computer model can represent the dynamics of a complex system.  In addition, complex systems may include complex decision rules.  All behavioral consequences resulting from these rules may be difficult to predict. 

Addressing these concerns involves answering the question: What system behavior was captured in the model?  One very effective way of meeting this requirement is seeing the behavior graphically.  This is accomplished using animation. 

4-17 

Typical ways of showing simulated behavior using animation follow: 

1. State of a resource with one unit: The resource is represented as a graphical object that physically resembles what the resource models.  For example, if the resource models a lathe, then the object looks like a lathe.  Each state of the resource corresponds to a different color.  For example, yellow corresponds to IDLE, green to BUSY, and red to BROKEN.  Color changes during the animation indicate changes in the state of the resource in the simulation. 

2. Entities:  An entity is represented in the frame as a graphical object that physically resembles what the entity models.  Different colors may be used to differentiate entities with different characteristics.  For example if there are two types of parts, graphical objects representing part type 1 may be blue and those representing part type 2 may be white. 

3. Number of entities in a buffer: A graphical object, which may be visually transparent, represents the buffer.  An entity graphical object is placed in the same location as the buffer graphical object whenever an entity joins the buffer in the simulation.  The buffer graphical object accommodates multiple entity graphical objects. 

4. Material transportation: Any movement, such as between workstations, of entities in the simulation can be shown on the animation.  The location of an entity graphical object can be changed at a rate proportional to the speed or time duration of the movement. Movement of material handling equipment can be shown in a similar fashion.  As for other resources, a piece of material handling equipment is represented by a graphical object that resembles that piece of equipment.  For example, a forklift is represented by a graphical object that looks like a forklift. 

An animation of the two-stations in a series system should be viewed at this time. 

## _4.7 Comparing Scenarios_ 

This section presents a strategy for determining if simulation results provide evidence that one scenario is better than another.  Often one scenario represents current system operations for an existing system or a baseline design for a proposed system.  Improvements to the current operations or to a baseline design are proposed.  Simulation results are used see if these improvements are significant or not.  In addition, it may be necessary to compare one proposed improvement to another.  This is an important part of step 3 Identify Root Causes and Assess Initial Scenarios as well as step 4 Review and Extend Previous Work of the simulation project process. 

Often, pair-wise comparisons are made.  This will be the scope of our discussion.  Law (2007) provides a summary of methods for ranking and selecting the best from among all of the scenarios that are considered. 

The job of comparing scenario A to scenario B is an effort to find evidence that scenario A is better than scenario B.  This evidence is found first by examining observations of performance measures to see if any operationally significant differences or unexpected differences can be seen.  If such differences are seen, an appropriate statistical analysis is done to confirm them. Confirm means to determine that the differences are not due to random variation in the simulation experiment. 

Many times a scenario is better with respect to one performance measure and the same or worse with respect to others.  Evaluating such tradeoffs between scenarios is a part of the art of simulation. 

4-18 

Each of the ways of comparing scenarios will be discussed in the context of the simulation experiment concerning the two stations in a series model.  This experiment is presented in Table 4-2.  The primary performance measure of interest will be entity lead time. 

## 4.7.1 Comparison by Examination 

Some ways of comparing two scenarios by examination of performance measure observations follow. 

## **1. For each replicate (or at least several replicates), graph all observations of a performance measure.** 

For example, the graph of the number in the buffer of workstation A for the scenario for the current machine in use at workstation A is shown in Figure 4-3.  This could be compared to the graph of the same quantity for the scenario where the new machine is used at workstation A.  If the latter graph consistently showed fewer entities in the buffer, then there would be evidence that that using the new machine at workstation A is an improvement: less WIP. 

Graphing lead time observations is not usually done since lead time is not a state variable and does not have a value at every moment in simulation time. 

## **2. For each replicate or over all replicates, compare the histograms of the observations of a performance measure.** 

For example, histograms of lead time can be compared.  If the histogram for the new machine at workstation A scenario clearly shows a greater percentage of entities requiring less time on the line versus the current machine scenario, then there would be evidence that using the new machine at workstation A lowers cycle time. 

## **3. Compare the averages of the sample values, xi, gathered from the replicates.  Note whether the difference in the averages is operationally significant.** 

For example, the average lead time for the current machine scenario is 62.7 seconds and for the new machine scenario is 58.5 seconds.  These values are for all replicates of the experiment. Thus, the new machine reduces cycle time by about 6%, which is operationally significant. 

## **4. Compare the range [minimum, maximum] of the sample values, xi.  Note whether the ranges overlap.** 

For example, the range of cycle time averages over the replicates of the experiment for the current machine scenario is (52.5, 71.7) and for the new machine scenario is (48.8, 68.9).  The ranges overlap and thus provide no evidence that the new machine reduces cycle time verses the existing machine at workstation A. 

## 4.7.2 Comparison by Statistical Analysis 

This section discusses the use of confidence intervals to confirm that perceived differences in the simulation results for two scenarios are not just due to random variation in the experiment. 

Note that the experiment design assures that scenarios share random number streams in common.  Thus, the scenarios are not statistically independent.  Furthermore, the same number of replicates is made for each scenario.  Thus, an approach that compares the simulation results 

4-19 

on a replicate by replicate basis is required and helpful.  This approach is called the paired-t method.[1] 

Table 4-7 provides the organization to support the paired-t method.  Each row corresponds to a replicate.  The difference between the performance measure values for each replicate is shown in the fourth column.  These differences are independent observations.   A 1- confidence interval for the population mean of the difference in the fourth column is computed.  If this confidence interval does not contain zero, it will be concluded that there is a statistically significant difference between the scenarios with confidence 1-.  This confidence interval is constructed and interpreted using the same reasoning as was given in section 4.6.2. 

To illustrate, Table 4-8 compares, based on entity lead time, the use of the new machine at workstation A versus the current machine using the paired-t method.  A 99% confidence interval for the mean difference is constructed: (3.7, 4.7) with 99% confidence.  Thus, with 99% confidence the new machine at workstation A reduces mean cycle time in the range (3.7, 4.7) seconds. 

It is also helpful to examine the data in Table 4-8 on a replicate-by-replicate basis.  Notice that in all of the replicates, cycle time was less using the new machine at workstation A.  It should be noted however that it is still quite possible that in any particular 40 hour period, the two stations in a series line would perform better with respect to cycle time using the current machine at workstation A instead of the new machine.  The simulation results show that on the average over many 40 hour periods the line will perform better with respect to cycle time using the new machine at workstation A. 

**Table 4-7:  Format of the Paired-t Method** 

|**Replicate**|**Scenario**<br>**A**|**Scenario**<br>**B**|**Difference (Scenario A – Scenario**<br>**B)**|
|---|---|---|---|
|**1**||||
|**2**||||
|**3**||||
|**4**||||
|**.**<br>**.**<br>**.**||||
|**n**||||
|**Average **||||
|**Std. Dev.**||||
|**1-****C. I.**<br>**Lower Bound**||||
|**1-****C.I.**<br>**Upper Bound**||||



> 1 Law (2007) provides a more in depth discussion of the comparison of alternatives using confidence intervals, including the generation of confidence intervals when common random numbers are not used. 

4-20 

**Table 4-8:  Comparison of Scenarios Using the Paired-t Method (1-**  **= 99%)** 

|**Replicate**|**Current Machine**|**New Machine**|**Difference**<br>**(Current  – New)**|
|---|---|---|---|
|**1**|61.1|57.3|3.8|
|**2**|66.0|62.2|3.9|
|**3**|60.6|57.6|3.0|
|**4**|52.5|48.8|3.7|
|**5**|58.3|55.0|3.3|
|**6**|63.4|59.3|4.0|
|**7**|59.7|55.0|4.8|
|**8**|63.9|59.2|4.7|
|**9**|62.7|58.5|4.2|
|**10**|61.1|56.7|4.4|
|**11**|60.7|56.6|4.1|
|**12**|65.2|59.8|5.4|
|**13**|64.7|58.3|6.4|
|**14**|63.6|59.5|4.1|
|**15**|67.3|63.5|3.8|
|**16**|61.7|57.2|4.5|
|**17**|71.7|68.9|2.8|
|**18**|63.3|59.0|4.3|
|**19**|62.3|58.1|4.2|
|**20**|64.6|59.9|4.7|
|**Average **|62.7|58.5|4.2|
|**Std. Dev.**|3.82|3.8|0.8|
|**99% C. I. Lower Bound**|60.9|56.7|3.7|
|**99% C.I. Upper Bound**|64.5|60.3|4.7|



## 4.7.2.1 A Word of Caution about Comparing Scenarios 

In comparing scenarios, many confidence intervals may be constructed.  For each pair of scenarios, several performance measures may be compared.  Many scenarios may be tested as well. 

The question arises as to the resulting  level for all confidence intervals together, overall.  This overall level is the probability that all confidence intervals simultaneously cover the actual difference in value between the scenarios of the system parameter or characteristic each estimates. 

A lower bound on overall is computed using the Bonferroni inequality where a total of k confidence intervals are conducted: 

**==> picture [420 x 29] intentionally omitted <==**

and thus: 

**==> picture [420 x 29] intentionally omitted <==**

Suppose we compare two scenarios using two performance measures with  = 0.05.  A confidence interval of the difference between the scenarios is computed for each performance measure.  The lower bound on the probability that both confidence intervals cover the actual difference in the performance measures is given by equation 4-5:  overall <= 0.05 + 0.05 = 0.10. 

4-21 

Consider comparing two scenarios with respective to 10 performance measures.  Each confidence interval is computed using  = 0.05.  Then the probability all confidence intervals cover the actual difference in the performance measures might be as low as 0.05*10 = 0.50. That is the error associated with all our work would be 0.5.  Thus, when making many comparisons, a small value of j for each confidence interval is necessary.  For example with all j = 0.01, the overall error associated with ten comparisons is 0.1, which is acceptably low. 

Unfortunately if a large number of performance measures are used or many scenarios are compared, overall will always be large.  Thus, it is likely that for at least one confidence interval that the true difference between the performance measure values will not be covered.  So a difference between two scenarios will not be detected. 

## _4.8 Summary_ 

This chapter discusses the design and analysis of simulation experiments.  Elements are defined and organized into a design. A method to construct statistically independent observations to avoid correlation difficulties is described. 

The need to gather evidence that a model is valid and verified is presented.  Possible strategies in this regard are given.  Ways to compare scenarios, both through statistical analysis and the examination of data, are discussed. 

**Problems** (Similar problems are associated with each of the case studies for further practice). 

1. Suppose 4 scenarios were compared in a pair-wise fashion with respect to one performance measure.  How many comparisons are made?  If  = 0.01 is used for all comparisons, what is the upper bound on the for all the comparisons made?  What if  = 0.05 is used?  Which of the two values for  should be used? 

2. Consider the following table of simulation results. 

|**Replicate**|**Workstation % Busy Time –**<br>**Scenario One**|**Workstation % Busy Time –**<br>**Scenario Two**|
|---|---|---|
|1|87|78|
|2|80|72|
|3|79|71|
|4|80|72|
|5|78|71|



- a. Construct 95% confidence intervals for the workstation % busy time for each scenario. 

- b. Construct a paired-t confidence interval,  = 0.05, to compare the percent busy time of a workstation for two scenarios. 

4-22 

3. Consider the following table of simulation results. 

|**Replicate**|**Maximum Time –**<br>**Scenario One**|**Maximum Time –**<br>**Scenario Two**|
|---|---|---|
|1|241.8|122.0|
|2|61.1|62.6|
|3|122.1|94.7|
|4|111.6|73.1|
|5|154.4|105.2|



   - a. Construct 95% confidence intervals for the maximum time for each scenario. 

   - b. Construct a paired-t confidence interval,  = 0.05, to compare the maximum time at the workstation for the two scenarios. 

   - c. Are the confidence intervals constructed in a. and b. approximate or exact? Defend your answer. 

4. Develop the design of a terminating simulation experiment for problem 2-10. 

5. Defend the use of approximate confidence intervals. 

6. Consider the simulation of a single workstation consisting of a single machine with an operation time uniformly distributed between 5 and 10 minutes.  The time between part arrivals is exponentially distributed with a mean of 9 minutes. 

   - a. What verification evidence could be sought? 

   - b. What validation evidence could be sought? 

7. Conduct a complete analysis of a simulation experiment regarding a single workstation with one machine based on the data that follow. The mean time between arrivals is 10 minutes and the operation time is 8 minutes.  The simulation was run for 168 hours. Management wishes to achieve a production quota of 1000 items per 168 hours. 

   - a. Provide evidence for the verification and validation of the simulation based only on the data in the following table and the problem statement. 

|**Replicate**|**Workstation**<br>**% Busy**<br>**Time**|**Number of**<br>**Entities**<br>**Arriving**|**Number of**<br>**Entities**<br>**Departing**|**Number of**<br>**Entities in**<br>**Processing at**<br>**the End of the**<br>**Simulation**|**Number of**<br>**Entities in the**<br>**Buffer at the**<br>**End of the**<br>**Simulation**|
|---|---|---|---|---|---|
|1|87|1044|1044|0|0|
|2|80|961|960|1|0|
|3|79|944|943|1|0|
|4|80|965|959|1|5|
|5|78|942|942|0|0|



4-23 

- b. Compare the two scenarios using first the average number in the buffer and then the maximum as described below.  Use only the data that follows and items i-iv. i. Compute appropriate statistical summaries (average, standard deviation, minimum, maximum, range, and confidence intervals) and state any evidence found from this information. 

   - ii. Compute and display appropriate histograms and state any evidence seen in them. 

   - iii. In how many replicates is the new case better than the current operations?  What evidence does this information provide? 

   - iv. Perform the appropriate statistical analysis to compare the scenarios. 

## **Number in Buffer** 

||**Number in Buffer**|**Number in Buffer**|**Number in Buffer**|**Number in Buffer**|
|---|---|---|---|---|
||**Current Operations**||**New Case**||
|**Replicate**|**Average**|**Maximum**|<br>**Average **|<br>**Maximum**|
|1|<br>12.8|<br>28|<br>4.3|<br>15|
|2|<br>1.2|<br>8|<br>1.1|<br>7|
|3|<br>4.3|<br>16|<br>2.6|<br>16|
|4|<br>2.9|<br>10|<br>1.9|<br>8|
|5|<br>3.6|<br>17|<br>2.1|<br>12|
|6|<br>3.7|<br>10|<br>2.0|<br>8|
|7|<br>2.1|<br>12|<br>1.2|<br>7|
|8|<br>3.5|<br>17|<br>1.6|<br>11|
|9|<br>2.7|<br>13|<br>1.4|<br>9|
|10|<br>2.0|<br>10|<br>1.2|<br>9|
|11|<br>1.4|<br>8|<br>1.3|<br>10|
|12|<br>2.0|<br>12|<br>1.4|<br>10|
|13|<br>1.4|<br>7|<br>1.4|<br>9|
|14|<br>2.7|<br>17|<br>2.0|<br>12|
|15|<br>1.7|<br>16|<br>1.2|<br>9|
|16|<br>1.5|<br>7|<br>0.9|<br>8|
|17|<br>5.2|<br>26|<br>4.2|<br>17|
|18|<br>3.2|<br>15|<br>2.0|<br>9|
|19|<br>3.1|<br>14|<br>2.0|<br>9|
|20|<br>2.2|<br>11|<br>1.2|<br>8|



4-24
