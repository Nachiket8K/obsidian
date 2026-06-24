---
title: "Chapter 5 The Simulation Engine"
book: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li"
source_pdf: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li.pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 5 The Simulation Engine** 

## _5.1 Introduction_ 

This chapter discusses the computations necessary to simulate a model on a computer.  These computational tasks are performed by software that can be referred to as a **simulation engine.** The engine produces performance measure values as output.  It does this transparently to the simulation user whose primary concern is performing the steps of the simulation process including model building and experiment design as well as the statistical analysis of performance measure values and drawing conclusions about system behavior.  Nevertheless, a basic understanding of how a simulation engine does its computation tasks is fundamental. 

All models are mapped, transparently to the modeler, into a set of events within the simulation engine.  The mapping may be complex and not straightforward.  An event is a point in simulation time when the value of one or more the state variables changes. In addition an event is used to specific when in simulated time, or under what conditions, other events, including itself, next occur. 

The basic operations that a simulation engine must perform are presented in the context of the two workstation example model that was presented in previous chapters.  Fundamentally, the engine must conduct the simulation step by step from start to finish.  This requires 

1. Sequencing the events. 

2. Processing each event. 

3. Organizing entities waiting for resources. 

4. Generating individual samples from probability distributions to obtain values for entity attributes and times between entity arrivals as well as operation and transportation times. 

A discussion of the events in the two workstation example will precede a discussion of each of the activities of the simulation engine. 

## _5.2 Events and Event Graphs_ 

Event graphs (Schruben, 1983; 1995) are a diagramming technique for showing the events comprising a model.  An event graph consists of nodes and arcs.  Nodes correspond to events. Arcs tell the relationships between events: the other events, including itself, that an event can cause to occur and the logical conditions that may restrict such occurrences. The logical conditions make use of the state variables.  An arc also tells the time from now when an event will take place. 

The event graph for the two station serial system is shown in Figure 5-1.  There are four state variables: the number in the buffer of each station and the state (busy, idle) of each station. Three events are associated with each station: _Entity arrives, Start service,_ and _End service_ . 

The entity arrives event associated with station A causes itself to occur again, that is the next entity to arrive, after a time interval specified by the time between arrivals.  The number in the buffer of workstation A is incremented by 1. 

The entity arrives event causes the start service event to begin processing the arriving entity immediately if the machine is IDLE.  The start service event decreases the number in the buffer of workstation A by 1 and makes the workstation BUSY. 

The end service event follows the start service event and occurs after a time interval that is the item processing time.  The end service event will initiate processing of the first entity waiting in the buffer if there is one by scheduling the start service event at the current time.  The end service event makes the workstation IDLE. 

5-1 

The time between arrivals to station A and the item processing time could be random variables. 

Figure 5-1:  Event Graph for Two Workstations in a Series Model 

## _5.3 Time Advance and Event Lists_ 

This section discusses how the simulation proceeds through time by scheduling event occurrences and processing each of them in turn.  In general, a model is simulated as a time ordered sequence of the occurrences of the events.  Event occurrences are processed one at a time.  Each event occurrence changes the value of one or more state variables and may schedule other events.  This simulation approach is illustrated by one possible simulation of the two workstations in sequence model. 

The **event list** is the time ordered list of all event occurrences scheduled at the current time and in the future.  The simulation proceeds by removing the first event occurrence on the list and processing it.  This processing may result in one or more event occurrences being added to the list to be processed at the current time or in the future.  Note that only one event occurrence at a time is removed from the list.  All others remain on the list.  After the processing of the event occurrence, the list will consist of the event occurrences already on the list when the first event occurrence was removed plus those added by processing this event occurrence. 

For the two workstation model, the simulation engine must deal with six events that change the values of the state variables.  Each of these events must be scheduled in time and processed. These events are the arrival of an entity (part) to each station as well as the start and end of processing. 

At any point in time, the event list could contain the following event occurrences at future points in time: 

   - Entity arrives to workstation A event. 

   - Entity ends service at workstation A event. 

   - Entity ends service at workstation B event. 

- Other events can occur only at the same point in time as another event. 

   - The start of service at workstation A event that can occur either when a entity arrives to workstation A (arrives to workstation A event) or when a entity completes processing at workstation A (ends service at workstation A event). 

5-2 

- The entity arrives to workstation B event that occurs every time an entity ends service at workstation A event occurs.  (Recall there is no time delay for moving between workstations.) 

- The start of service at workstation B event that can occur either when a entity arrives to workstation B (arrives to workstation B event) or when an entity completes processing at workstation B (ends service at workstation B event). 

To illustrate, consider one possibility for the event list at the start of the simulation. 

|**Current Simulation Time: 0**<br>**Next Simulation Time = Time of first event occurrence in list = 0.0**|**Current Simulation Time: 0**<br>**Next Simulation Time = Time of first event occurrence in list = 0.0**|
|---|---|
|**Event**|**Time of Occurrence**<br>**Entity ID**|
|**Entity Arrives to A**|0.0<br>1|



The simulation will begin with the arrival of the first entity at time 0. 

Thus, the first task of the simulation engine is to process the Entity Arrives to A event at time 0. This task involves removing the Entity Arrives to A event from the list and performing the actions associated with the event: scheduling the next Entity Arrives to A event and scheduling the Entity Start Service event, if workstation A is idle (which it is initially).  After the entity arrives to A event is processed the event list is as follows, assuming the next arrival to workstation A is at time 5.0: 

## **Current Simulation Time: 0 Next Simulation Time = Time of first event occurrence in list = 0.0** 

|**Event**|**Time of Occurrence**<br>**Entity ID**|
|---|---|
|**Start Service at A**<br>**Entity Arrives to A**|0.0<br>1<br>5.0<br>2|



Next, the simulation engine removes the Start Service at A event from the list.  The Entity Arrives to A event remains on the list.  Processing the event removed from the list results in scheduling the End Service at A event as shown in the following. 

|**Current Simulation Time: 0**<br>**Next Simulation Time = Time of first event occurrence in list = 5.0**|**Current Simulation Time: 0**<br>**Next Simulation Time = Time of first event occurrence in list = 5.0**|
|---|---|
|**Event**|**Time of Occurrence**<br>**Entity ID**|
|**Entity Arrives to A**<br>**End Service at A**|5.0<br>2<br>8.0<br>1|



The entity with ID number 2 will arrive at time 5.0 and the End of Service at workstation A for the entity with ID number 1 will occur at time 8.0. 

The simulation engine advances time to the next event occurrence at time 5.0 and processes the Entity Arrives to A event for the entity with ID 2.  This means that the Entity Arrives to A event will be removed from the list and End Service at A event will remain on the list. 

At time 5.0, the workstation A resource is in the busy state.  Thus, the entity with ID 2 enters the queue for the workstation A resource.  No entry for this entity is placed on the event list.  In addition, processing this event causes the Entity Arrives to A event to be scheduled at time 32.5 for the entity with ID 5.  This means that the next occurrence of the Entity Arrives to A event is placed on the event calendar at time 32.5. 

Thus, after processing the Entity Arrives at A event occurrence at time 5.0, the event list consists of the End Service at A event which was previously on the list plus the next Entity Arrives to A event that was newly placed on the list as shown in the following. 

5-3 

## **Current Simulation Time: 5.0** 

|**Current Simulation Time: 5.0**|**Current Simulation Time: 5.0**|
|---|---|
|**Next Simulation Time = Time of first event occurrence in list = 8.0**||
|**Event**|**Time of Occurrence**<br>**Entity ID**|
|**End Service at A**<br>**Entity Arrives to A**|8.0<br>1<br>32.5<br>3|



Next, the simulation engine advances time to the 8.0 to process the end of service at A event for entity 1.  The entity with ID number 1 will arrive at workstation B at time 8.0 since there is no movement delay.  The entity with ID number 2 will leave the queue of the workstation A resource and start processing using the workstation A resource that has just become idle.  Thus, the workstation A resource becomes busy. 

Thus after processing the End Service at A event, the Entity Arrives to A event remains on the list and the Entity Arrives to B event as well as the Start Service at A event are added. 

## **Current Simulation Time: 8.0** 

**Next Simulation Time = Time of first event occurrence in list = 8.0** 

|**Event**|**Time of Occurrence**<br>**Entity ID**|
|---|---|
|**Entity Arrives to B**<br>**Start Service at A**<br>**Entity Arrives to A**|8.0<br>1<br>8.0<br>2<br>32.5<br>3|



Simulation engines typically use the strategy that all possible processing of one entity at the current simulation time will be done before any processing of any other entity.  Another way of saying this is that the entity will proceed as far as possible until obstructed by a time delay or by waiting for a currently unavailable resource.  This implies that new events at the current simulation time for this entity are placed first on the event list.  Thus in the above list, the entity arrives to B event for the entity with ID 1 at time 8.0 precedes the start service at A event for the entity with ID number 2. 

The remainder of the simulation is processed in a similar fashion. 

## _5.4 Simulating the Two Workstation Model_ 

This section discusses and illustrates the record of the time ordered sequence of events that are processed by a simulation engine for a particular model.  This record is called a **trace** and includes the changes in state variable values that occur as well as other relevant information such as entity attributes.  All simulation engines provide a trace that the modeler can examine to determine the step-by-step behavior of a simulation for verification and validation. 

Consider one possible simulation of the two workstations in sequence model.  Let’s follow the sequence of events processed in time order when only one entity moves through the two workstations, assuming that no other entities arrive in the meantime. 

The trace for the simulation with one entity is shown Table 5-1.  Only the new values of state variables whose values are changed by an event are shown.  At the start of the simulation there are no entities in the model, the buffers are empty and the workstation resources are in the IDLE state.  The entity with ID number 1 arrives at time 0 and enters the buffer of workstation A.  Since the workstation A resource is IDLE, the start service at A event occurs at time 0.  This event removes the entity from the buffer of workstation A and makes the workstation A resource BUSY. 

## **Table 5-1:  Simulation Trace for One Entity** 

5-4 

|**Current**<br>**Simulation**<br>**Time**|**Event**|**Entity**<br>**ID**|**Number**<br>**in Buffer**<br>**–**<br>**Station**<br>**A**|**State of**<br>**Workstation**<br>**A Resource**|**Number**<br>**in Buffer**<br>**–**<br>**Station**<br>**B**|**State of**<br>**Workstation**<br>**B Resource**|
|---|---|---|---|---|---|---|
|0.0|InitialConditions||0|IDLE|0|IDLE|
|0.0|Entity Arrives to<br>A|1|1||||
|0.0|Start Service atA|1|0|BUSY|||
|8.0|End Service atA|1||IDLE|||
|8.0|Entity Arrives to<br>B|1|||1||
|8.0|Start Service atB|1|||0|BUSY|
|16.5|End Service atB|1||||IDLE|



The simulation engine must determine the duration of processing at workstation A for this particular entity.  This is done by computing a random sample from the processing time distribution: uniform (5,13).  Suppose the value turns out to be 8.0.  Thus, the end of service at A event is placed at time 8.0.  At this time, the workstation A resource becomes IDLE. 

The entity arrives at B event occurs at time 8.0 as well since there is no time delay for movement between the workstations.  The entity enters the buffer of workstation B.  Since the workstation B resource is IDLE, the start service at B event occurs at time 8.0.  The duration of processing at workstation B is a constant 8.5.  Thus, the end of service at B event is placed at time 16.5. 

Now, suppose a second entity arrives in the simulation at time 5.0.  This time is determined by computing a value from the time between arrivals distribution: exponential (10) when the entity arrives at A event is processed for entity 1 at time 0.  Suppose further that the simulation engine computes the service time at workstation A to be 7.0.  Table 5-2 shows the trace of the simulation for this situation. 

Note the events involving entity 2.  Since the workstation A resource is BUSY when entity 2 arrives at time 5.0, it remains in the buffer of station A.  At time 8.0, all events concerning entity 1 are processed first.  After these events are processed, the start service at A event is processed for entity 2.  Since the processing time is computed to be 7.0, the end of service at A event is placed at time 15.0. 

At time 15.0, the end of service at A event occurs for entity 2 as well as the entity arrives to B event.  Since workstation B resource is busy, entity 2 waits in the buffer of station B. 

At time 16.5, the end of service at B event occurs for entity 1.  Since the workstation B resource becomes IDLE, start of service at B event occurs for entity 2.  At time 25.0, entity 2 completes processing at workstation B. 

5-5 

**Table 5-2:  Simulation Trace for Two Entities** 

|**Current**<br>**Simulation**<br>**Time**|**Event**|**Entity**<br>**ID**|**Number**<br>**in Buffer**<br>**–**<br>**Station**<br>**A**|**State of**<br>**Workstation**<br>**A Resource**|**Number**<br>**in Buffer**<br>**–**<br>**Station**<br>**B**|**State of**<br>**Workstation**<br>**B Resource**|
|---|---|---|---|---|---|---|
|0.0|InitialConditions|--|0|IDLE|0|IDLE|
|0.0|Entity Arrives to<br>A|1|1||||
|0.0|Start Service atA|1|0|BUSY|||
|5.0|Entity Arrives to<br>A|2|1||||
|8.0|End Service atA|1||IDLE|||
|8.0|Entity Arrives to<br>B|1|||1||
|8.0|Start Service atB|1|||0|BUSY|
|8.0|Start Service atA|2|0|BUSY|||
|15.0|End Service atA|2||IDLE|||
|15.0|Entity Arrives to<br>B|2|||1||
|16.5|End Service atB|1||||IDLE|
|16.5|Start Service atB|2|||0|BUSY|
|25.0|End Service at B|2||||IDLE|



## _5.5 Organizing Entities Waiting for a Resource_ 

Notice from the discussion in section 5.2 that there is either zero or one event occurrence on the event list corresponding to each entity.  If there is no event occurrence, the entity is waiting usually for a resource to become available.  Multiple entities may be waiting for the same resource.  Thus, it is necessary to maintain lists of waiting entities as well as lists of event occurrences. 

Entities wait for a resource that is currently not in the idle state in an ordered list similar to the event list.  When a unit of the resource completes its current task or otherwise becomes idle, it will process the first entity in the list.  The list is sequenced either by order of entity entry in the list (first-in-first-out or last-in-first-out) or by an entity attribute value (high-value-first or low-valuefirst). 

Suppose entities in the two workstation model have the following attributes: 

1. Time of arrival to the system 

2. Estimated processing time at workstation A 

Suppose that at a particular moment in simulation time there are three entities waiting for the workstation A resource.  The waiting entities are ordered first-in-first-out as follows. 

|**Entity**|**Time of Arrival**<br>**Estimated**<br>**Processing Time**|
|---|---|
|**101**<br>**102**<br>**103**|100.0<br>15.0<br>110.5<br>9.8<br>120.5<br>21.0|



5-6 

Alternatively, suppose the entities were sorted by the lowest value of estimated processing time first as follows. 

|**Entity**|**Time of Arrival**<br>**Estimated**<br>**Processing Time**|
|---|---|
|**102**<br>**101**<br>**103**|110.5<br>9.8<br>100.0<br>15.0<br>120.5<br>21.0|



Note that the sequence in which entities are processed at workstation A is the same as their order in the queue of workstation A. 

## _5.6 Random Sampling from Distribution Functions_ 

In chapter 2, entity attribute values and the time between entity arrivals as well as operation and transportation times were modeled using probability distributions.  Furthermore, values for these variables need to be assigned to each entity.  To accomplish this assignment, a random sample must be taken from the corresponding probability distribution.   This subject is worthy of a lengthy and thorough discussion such as that provided in Law (2007) as well as Carson, Banks, Nelson, and Nicol (2009).  Here one approach for taking random samples is presented to illustrate how this issue is addressed. 

Consider the time between entity arrivals in the two workstations in a series model: exponential (10) seconds, where 10 is the average time between arrivals, TBA.  This quantity follows the cumulative distribution function: 

y = F(x) = 1 - e[- x / TBA] = 1 - e[- x / 10] 

and therefore 

x = -TBA ln (1 - y) = -10 ln (1-y) 

(5-1) 

In the same way, the service time at workstation A is uniformly distributed between a minimum and a maximum value (5 and 13 seconds) and therefore follows the cumulative distribution function: 

y = F(x) = (x-minimum) / (maximum – minimum) = ( x - 5 ) / ( 13 - 5 ) 

and therefore 

x = y * ( maximum - minimum )  + minimum = y * (13 – 5) + 5 (5-2) 

Notice that taking the inverse of the cumulative distribution reduces each case to the same problem, determining the value of y.  Thus, this approach for taking a random sample is called the **inverse-transformation method.** 

Figure 5-2 shows how this method works for the service time at workstation A.  Any value of y in the range 0-1 is equally likely.  (This is because y is a cumulative distribution.)  Good experimental procedure requires a random sample and so a random sample of y must be chosen. Once a random value is selected for y, the random sample of x is straightforward to compute. 

5-7 

**==> picture [214 x 522] intentionally omitted <==**

5-8 

The inverse-transformation method is summarized as follows: 

1. Determine the inverse of the cumulative distribution function, F[-1] (x). 

2. Each time a sample is needed: 

   - a. Generate a random sample, r, uniformly distributed in the range 0 to 1. b. x = F[-1] (r). 

Using the inverse-transformation method requires that the inverse of the cumulative distribution function exists.  This is true for the following distributions commonly used in simulation models: uniform, triangular, exponential, weibull, and any discrete distribution where the mass function is enumerated as well as a heuristic distribution in histogram form. 

As an example, consider the use of the inverse-transformation method with equation 5-2. Suppose r is selected to be 0.45.  Then x = -10 ln (1 – 0.43) = 5.62.  Next the inversetransformation method is applied to equation 5-5.  Suppose r is selected to be 0.88.  Then x = 0.88 * ( 13 - 5 )  + 5 = 12.04. 

## _5.7 Pseudo-random Number Generation_ 

All of the random sampling strategies discussed in the previous section require a random sample uniformly distributed in the range (0,1).  Fortunately, there are several well known algorithms for generating such samples, called **pseudo - random** numbers.  These algorithms are deterministic.  However, the properties of the sequence of pseudo-random numbers make them look random.  These properties include the following: 

1. The numbers do not exhibit any statistical correlation with each other. 

2. The numbers appear to be uniformly distributed in the range (0,1). 

3. There are many, many (at least 1,000,000) numbers in sequence. 

4. All possible numbers in the sequence are generated before any number repeats. 

Because the pseudo-random number generation algorithms are deterministic, a sequence of numbers can be regenerated whenever necessary.  This is important in simulation both for debugging and experimentation using common random numbers.  Imagine the difficulty of removing a bug from a model if the results were randomly different each time the model was executed! 

A sequence of pseudo-random numbers is called a stream.  Having multiple streams of random numbers allows sampling from each particular probability distribution used in a model to be associated with a particular stream.  For example in the two stations in a series model, the time between arrivals and the operation time at station A would be assigned different streams.  This means for example that if the probability distribution modeling the operation time at station A were changed, the times between arrivals would remain the same. 

As in the previous section, one approach to pseudo-random number generation will be presented. Other approaches for generating pseudo-random numbers are given in Banks, Carson, Nelson, and Nicol (2009) as well as Law (2007).  Schmeiser (1980) provides a comprehensive survey. 

Perhaps the most common type of pseudo-random number generation algorithm, with respect to use in simulation languages, is the linear congruential generator (Lehmer, 1951).   The linear congruential generator (LCG) has the form: 

Zi = (a*Zi-1 + c) mod(m) (5-3) ri = Zi / m (5-4) 

5-9 

The Zi’s are a set of integers that range from 0 to m-1.  The integer Zi is a remainder and m is the divisor.  Other parameters of the generator are a multiplier a, an increment c, and the first integer Z0.  The pseudo-random number ri is obtained by dividing Zi by m.  Fortunately for our purposes, values for the parameters (a, c, m, and Z0) that result in the desirable properties listed above are used by commercial simulation languages. 

The generator is recursive that is Zi is a function of Zi-1.  Note that at most, m distinct Zi’s and thus ri’s (pseudo-random numbers) can be obtained.  Once Z0 is generated a second time, the entire sequence of Zi’s, and thus ri’s, will be repeated and in the same sequence as the first time. 

Consider the example LCG shown in Table 5-3.  The LCG parameter values are shown in the table.  Note that the Zi’ s range from 0-8.  All nine of the Zi’s are generated before any value repeats.  Thus, the ri’s appear to be as uniformly distributed in the range (0,1) as nine numbers can be.  The statistical correlation between the ri’s is low, 0.030.  Since the number of values generated is only 9, the value of m is too small for an effective LCG.  However, it suffices for an example. 

**Table 5-3:  Example LCG** 

|||**i**|<br>**Zi **|<br>**ri **|
|---|---|---|---|---|
|**M**|9|0|8|0.889|
|**A**|4|<br>1|<br>1|<br>0.111|
|**C**|5|2|<br>0|0.000|
|||3|5|0.556|
|||4|<br>7|<br>0.778|
|||5|6|0.667|
|||6|2|<br>0.222|
|||7|<br>4|<br>0.444|
|||8|3|0.333|
|||9|8|0.889|
|||10|1|<br>0.111|
|||11|<br>0|0.000|
|||12|<br>5|0.556|



## _5.8 Summary_ 

This chapter discusses the basic operations of a simulation engine.  While these operations are performed transparently to the modeler, an understanding of them helps clarify how simulation experiments work.  Events are organized and processed in time sequence.  Entities waiting for resources are sorted and maintained.  Random samples from distribution functions are generated and pseudo-random number streams are managed. 

5-10 

## **Problems** 

1. State a procedure for generating a random sample from each of the following distributions using the inverse transformation method.  Use the procedure in section 5.6 as a guide. 

**==> picture [367 x 73] intentionally omitted <==**

**----- Start of picture text -----**<br>
x  minimum<br>a.  Uniform distribution:  F ( x ) <br>maximum  minimum<br>x / mean<br>b.  Exponential distribution:  F ( x )  1  e<br>c.  Weibull distribution:  F ( x )  1  e   x / c  m  where c and m are the scale and<br>**----- End of picture text -----**<br>


   - shape parameters of the distribution respectively. 

- d. Triangular distribution: 

**==> picture [366 x 64] intentionally omitted <==**

**----- Start of picture text -----**<br>
2<br>  x  minimum <br>, minimum  x  mode<br>F ( x )   []   mode  minimum  *  maximum 2  minimum <br> 1   maximum -  x  , mode  x  maximum<br>  maximum  -mode  *  maximum  minimum <br>**----- End of picture text -----**<br>


e. Discrete distribution: F(x) = 0.1, x = 1 = 0.4, x = 2 = 0.6, x = 3 = 0.9, x = 4 = 1.0, x = 5 

2. Create a new trace based on the one shown in Table 5-2 by adding a entity with ID number 4 that arrives at time 2.0 with a processing time at workstation A of 6.4. 

3. Consider the properties of pseudo-random number generators presented in section 5-8. Does property four imply property two? 

4. Consider the two workstation in a series model and the last event list shown in section 5- 5. 

## **Current Simulation Time: 8.0** 

**Next Simulation Time = Time of first event occurrence in list = 8.0** 

|**Event**|**Time of Occurrence**<br>**Entity ID**|
|---|---|
|**Entity Arrives to B**<br>**Start Service at A**<br>**Entity Arrives to A**|8.0<br>1<br>8.0<br>2<br>32.5<br>3|



Use the event graph shown in Figure 5-1 as well as the trace shown in Table 5-2 as a guide. 

- a. Show the event list after the processing of the entity arrives to B event for the entity with ID number 1.  What single event occurrence was removed from the list?  What event occurrences remain on the list?  What event occurrences are added to the list? 

- b. Show the event list after the first event on the list resulting from 2a is processed. What single event occurrence was removed from the list?  What event occurrences remain on the list?  What event occurrences are added to the list? 

5-11 

5. Implement a (bad) LCG generator in Excel with the following parameters: 

a = 5; m = 16; c = 3; Z0 = 0. 

Generate the first 20 samples from the generator.  Assess its behavior using the four properties in section 5.7. 

6. Compute the following table using a spreadsheet. 

   - a. Generate the two random number streams, corresponding to interarrival time and operation time at station A, for the first ten arriving entities in the two workstation in a series model.  Do this by using the random number generator built into your spreadsheet program.  In Excel, this would be accomplished by entering the function rand() into each cell of the Pseudo-random Number / Bet. Arrivals and the Pseudorandom Number / Service Time columns. 

   - b. Use the inverse-transformation method to generate the time between arrivals and service time samples.  This means entering equation 5-1 into each cell in the Sample / Bet. Arrivals column and entering equation 5-2 into each cell in the Sample / Service Time column.  The corresponding pseudo-random number in the columns should be referenced for each cell. 

## **Table for Problem 6** 

|**Entity**<br>**ID**|**Pseudo-random Number**|**Pseudo-random Number**|**Sample**|**Sample**|
|---|---|---|---|---|
||**Bet. Arrivals**|**Service Time**|**Bet. Arrivals**|**Service Time**|
|1|||||
|2|||||
|3|||||
|4|||||
|5|||||
|6|||||
|7|||||
|8|||||
|9|||||
|10|||||



7. Considering only the first two entities from the data generated in the solution to number 6, create a trace similar to Table 5-2 for the two workstations in a series model. 

5-12 

## **Part II Basic Organizations for Systems** 

Traditionally, there have been two basic approaches to organizing systems.  A serial system processes one, or at most a few, types of customers, parts, or anything else.   Each item visits each of the workstations in a predefined sequence.  There are many contexts in which serial systems occur.  An assembly line may be used to manufacture an automobile.  Customers using a fast food restaurant drive through first order food via a microphone, drive to one window to pay, and then proceed to a second window where the food is delivered. Serial systems are discussed in chapter 7. 

A job shop processes many different types of jobs.  Each job type has a unique route through a set of workstations.  Like serial systems, job shops occur in a wide variety of contexts.  A job enters the shop and is routed through one or more of the stations of the shop for processing.  A customer enters the cafeteria and proceeds in whatever order seems to make sense to the customer through the stations where the various types of food can be acquired. 

A simulation based analysis of a job shop evolves through chapter 8 as well as chapter 10 in part III.  Chapter 8 discusses how the number of machines at each station in the job shop can be determined.  Chapter 10 examines the conversion of the job shop from a push to a pull operating strategy. 

Serial lines and job shops consist of multiple workstations.  Thus before studying these, a study of a single workstation is presented in Chapter 6.  Mathematical models as well as simulation models are employed. 

The terminating simulation experiment design is applied in all three application studies.  The iterative nature of the simulation process is demonstrated. 

The application studies in this part of the book are straightforward.  The applications problems follow directly from the corresponding application studies.  These provide basic practice in using the simulation process for problem solving including model building, experimentation and analysis as well as the use of simulation environment software.  The application studies and problems in the subsequent parts of the book are intended to be more challenging and to show the breadth of the use of simulation. 

The application study chapters are intended to be used in the following way.  Modeling and experimentation information needed to perform the application problem at the end of the chapter is introduced in and illustrated by the application study.  Thus, the application study is presented in a straightforward way.  Questions at the end of the chapter aid in the understanding of the application study.  Some questions require extensions of the model or the simulation experiment and are labeled as laboratory exercises. 

Additional questions at the end of the chapter concern the application problems.  These questions raise issues concerning modeling, experimentation, and the interpretation of results that must be resolved in completing the study.  The student may perform all of the simulation process steps, including model building, verification and validation, experimentation, analysis of simulation results, and conclusion drawing.  Alternatively, the questions may be used simply to discuss how the study should be performed.
