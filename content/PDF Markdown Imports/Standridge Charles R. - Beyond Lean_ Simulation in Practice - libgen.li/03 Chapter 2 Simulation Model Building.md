---
title: "Chapter 2 Simulation Model Building"
book: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li"
source_pdf: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li.pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 2 Simulation Model Building** 

## _2.1 Introduction_ 

How simulation models are constructed is the subject of this chapter.  A **simulation model** consists of a description of a system and how it operates.  The model is expressed in the form of mathematical and logical relationships among the system components.  Model building is the act and art of representing a system with a model (principle 1) to address a well-defined purpose (principle 5). 

Since simulation models conform to system structure and available data (principle 2), model building involves some significant judgment and art.  Thus, learning to build simulation models includes learning typical ways system components are represented in models as well as how to adapt and embellish these modeling strategies to each system. 

Model building is greatly aided by using a **simulation language** that provides a set of standard, pre-defined modeling constructs.  These modeling constructs are combined to construct models. A simulation software environment provides the user interface and functionality for model construction. 

This chapter presents common system components: arrivals, operations, routing, batching, and inventories, as well as describing typical models of each component.  These models of components can be combined, extended and embellished to form models of entire systems. Elementary modeling constructs commonly found in simulation languages are presented.  The use of these constructs in modeling the common system components is illustrated. 

## _2.2 Elementary Modeling Constructs_ 

This section presents the model building perspective taken in this text.  Basic modeling constructs are presented. 

The operation of many systems can be effectively described by the sequence of steps taken to transform the inputs to the outputs as shown in a value stream map.  This will be our perspective for model building.  A sequence of steps specified in a model is called a **process** .  A model consists of one or more such processes. 

The modeling construct used to represent the part, customer, information, etc. that is transformed from an input to an output by the sequence of processing steps is an **entity.** Each individual entity is tracked as it moves through the processing steps.  Processing can be unique for each entity with respect to such things as processing times and route through the steps.  Thus, it is essential to be able to differentiate among the entities.  This is accomplished by associating a unique set of quantities, called **attributes** , with each entity. Typical attributes include time of arrival to the system and type of part, customer, or other information. 

Note that a value stream map shows in general how parts flow through a system.  This might be viewed as a “macro” or big picture view of how a system operates.  One characteristic of beyond lean is the use of models that give a more detailed or “micro” representation of a system.  This helps in gaining of understanding of how a future state will actually operate and aids in ensuring a successful transformation. 

Certain components of a system are required in performing a processing step on an entity. However, such a component may be scarce, that is of insufficient number to be available to every entity upon demand.  Such a component is called a **resource** .  Waiting or queuing by entities for a resource may be required.  Typical resources may be machines or workers.  Other system components, totes or WIP racks, may be scarce and modeled using resources. 

2-1 

A resource has at least two **states** , unique circumstances in which it can be.  One of these is **busy** , for example in use operating on an entity.  Another is **idle** , available for use.  Typical model logic requires an entity to wait for the resource (or resources) required for a particular processing step to be in the idle state before beginning that step.  When the processing step is begun, the resources enter the busy state.  As many resource states as necessary may be defined and used in a model.  Other common resource states are broken and under repair, off shift and unavailable, and in setup for a new part type. 

Consider a workstation consisting of two machines.  A basic modeling issue is: Should each machine be modeled using a distinct resource?  Often, it does not matter which of the two machines is used to process an entity and operating information such as utilization is not required for each machine.  In such a case, it is simpler to use a single resource to model the two machines.  However, an additional concept: **number of units** , is necessary to model two (or mores) machines with one resource.  There is one unit of the resource for each machine, two in this example. 

**State variables** , and their values, describe the conditions in a system at any particular time. State variables must be included in a simulation model and typically include the number of units of each resource in each possible resource state as well as the number of entities waiting for idle units of each resource, the number of entities that have completed processing, and inventory levels. 

**Time** is a significant part of simulation models of systems.  For example, when in simulated time each process step begins and ends for each entity processed by that step must be determined. Sequencing what happens to each entity correctly in time, and thus correctly with respect to what happens to all other entities, must be accomplished. 

In summary, modeling the behavior of a system over **time** requires specifying how the **entities** use the **resources** to perform the steps of a **process** as well as how the values of the entity **attributes** and of the **state variables** , including the state of the **units of each resource** , change. 

## _2.3 Models of System Components_ 

Typical system components include arrivals, operations, routing, batching, and inventories. Models of these components are presented in this section.  The models may be used directly, modified, extended, and combined to support the construction of new models of entire systems. 

## 2.3.1 Arrivals 

Consider a workstation with a single machine in a manufacturing facility as shown in Figure 2-1. One issue encountered when modeling the workstation is specifying at what simulated time each entity arrives.  This specification includes the following: 

- When the first entity arrives. 

- The time between arrivals of entities, which could be a constant or a random variable modeled with a probability distribution.  In a lean environment, the time between arrivals should equal the takt time as will be discussed in chapter 6. 

- How many entities arrive during the simulation, which could be infinite or have an upper limit. 

Suppose the first entity arrives at time 0, a common assumption in simulation modeling, and the time between arrivals is the same for all entities, a constant 10 seconds. Then the first arrival is at time 0, the second at time 10 seconds, the third at time 20 seconds, the fourth at time 30 seconds, and so forth. 

2-2 

**==> picture [132 x 67] intentionally omitted <==**

Suppose that time between arrivals varies.  This implies that the time between arrivals is described by some probability distribution whose mean is the average time between arrivals.  The variance of the distribution characterizes how much the individual times between arrivals differ from each other.  For example, suppose the time between arrivals is exponentially distributed with mean 10 seconds, implying a variance of 10*10 = 100 seconds[2] .  The first arrival is at time 0. The second arrival could be at time 25 seconds, the third at time 31 seconds, the fourth at time 47 seconds, and so forth.  Thus, the arrival process is a source of outer noise. 

An example specification in pseudo-English follows. 

|Define|Arrivals:|// mean must equal takt time|
|---|---|---|
||Time of first arrival:|0|
||Time between arrivals:|Exponentially distributed with a mean of 10 seconds|
|||Exponential (6) seconds|
||Number of arrivals:|Infinite|
|2.3.2|Operations||



The next issue encountered when modeling the single machine workstation in Figure 2-1 is specifying how the entities are processed by the workstation.   Each entity must wait in the buffer (queue) preceding the machine.  When available, the machine processes the entity.  Then the entity departs the workstation. 

A workstation resource is defined with the name WS to have 1 unit with states BUSY and IDLE using the notation WS/1: States(BUSY, IDLE).  It is assumed that all units of a resource are initially IDLE.  The operation of the machine is modeled as follows.  Each entity waits for the single unit of the WS (workstation) resource to be available to operate on it that is the WS resource to be in the IDLE state.  At the time processing begins WS becomes BUSY.  After the operation time, the entity no longer needs WS, which becomes IDLE and available to operate on the next entity. 

This may be expressed with the following statements: 

2-3 

Define Resources: 

WS/1 with states (Busy, Idle) Process Single Workstation Begin Wait until WS/1 is Idle in Queue QWS // part waits for its turn on the machine Make WS/1 Busy // part starts turn on machine; machine is busy Wait for OperationTime // part is processed Make WS/1 Idle // part is finished; machine is idle End 

Note the pattern of resource state changes.  For every process step that makes a resource enter the busy state, there must be a corresponding step that makes the resource enter the idle state. However, there may be many process steps between these two corresponding steps.  Thus, many operations may be performed in sequence on an entity using the same resource. 

Note also the two types of wait statements that delay entity movement through a process.  Wait for means wait for a specified amount of simulation time to pass.  Wait unit means wait until a state variable value meets a specified logical condition.  This is a very powerful construct that also is consistent with ideas in event-based programming. 

Consider another variation on the single machine workstation operation that illustrates the use of conditional logic in a simulation model.  The machine requires a setup operation of 1.5 minutes duration whenever the Type of an entity differs from the Type of the preceding entity processed by the machine.  For example, the machine may require one set of operational parameter settings when operating on one type of part and a second set when operating on a second type of part. The model of this situation is as follows. 

Define Resources: WS/1 with states (Busy, Idle, Setup) Define State Variables: LastType Define Entity Attributes: Type Process Single Workstation with Setup Begin Wait until WS/1 is Idle in Queue QWS // part waits for its turn on the machine Make WS/1 Busy // part starts turn on machine; machine is busy If LastType ! = Type then Begin Make WS/1 Setup Wait for SetupTime LastType = Type Make WS/1 Busy End Wait for OperationTime // part is processed Make WS/1 Idle // part is finished; machine is idle End 

A state variable, LastType stores the type of the last entity operated upon by the resource WS. Notice the use of conditional logic.  Setup is performed depending on the sequence of entity 

2-4 

types.  Such logic is common in simulation models and makes most of them analytically intractable.  A new state, SETUP, is defined for WS.  This resource enters the SETUP state when the setup operation begins and returns to the BUSY state when the setup operation ends. 

Often a workstation is subject to interruptions.  In general, there are two types of interruptions: scheduled and unscheduled.  Scheduled interruptions occur at predefined points in time. Scheduled maintenance, work breaks during a shift, and shift changes are examples of scheduled interruptions.  The duration of a scheduled interruption is typically a constant amount of time.  Unscheduled interruptions occur randomly.  Breakdowns of equipment can be viewed as unscheduled interruptions.  An unscheduled interruption typically has a random duration. 

A generic model of interruptions is shown in Figure 2-2.  An interruption occurs after a certain amount of operating time that is either constant or random.  The duration of the interrupt is either constant or random.  After the end of the interruption, this cycle repeats. 

Note that the transition to the INTERRUPTED state is modeled as occurring from the IDLE state. Suppose the resource is in the BUSY state when the interruption occurs.  Typically, a simulation engine will assume that the resource finishes a processing step before entering the INTERRUPTED state.  However, the end time of the interruption will be the same that is the amount of time in the INTERRUPTED state will be reduced by the time spent after the interruption occurs in the BUSY state.  This approximation normally has little or no effect on the simulation results.  In many systems, interruptions are often only detected or acted upon at the end of an operation.  Using this approximation avoids having to include logic in the model as to what to do with the entity being processed when the interruption occurs.  On the other hand, such logic could be included in the model if required. 

This breakdown-repair process may be expressed in statements as follows: 

Define Resource: WS/1: States(Busy, Idle, Unavailable) Process Breakdown—Repair Begin Do While 1=1 // Do forever Wait for TimeBetweenBreakdowns Wait until WS/1 is Idle Make WS/1 Unavailable Wait for RepairTime Make WS/1 Idle End Do End 

Consider an extension of the model of the single machine workstation with breakdowns (random interruptions) added.  This model combines the process model for the single workstation with the process model for breakdown and repair. The WS resource now has three states: BUSY operating on an entity, IDLE waiting for an entity, and UNAVAILABLE during a breakdown.  This illustrates how a model can consist of more than one process. 

This model illustrates one of the most powerful capabilities of simulation.  Two processes can change the state of the same resource but otherwise do not transfer information between each other.  Thus, processes can be built in parallel and changed independently of each other as well as added to the model or deleted from the model as necessary.  Thus, simulation models can be built, implemented, and evolved piece by piece. 

2-5 

**==> picture [146 x 498] intentionally omitted <==**

2-6 

## 2.3.3 Routing Entities 

In many systems, decisions must be made about the routing of entities from operation to operation.  This section discusses typical ways systems make such routing decisions as well as techniques for modeling them.  A distinct process for making the routing decision can be included in the model. 

Consider a system that processes multiple item types using several workstations.  Each workstation performs a unique function.  Each job type is operated on by a unique sequence of workstations called a route.  In a manufacturing environment, this style of organization is referred to as a job shop.  It could also represent the movement of customers through a cafeteria where different foods: hot meals, sandwiches, salads, desserts, and drinks are served at different stations.  Customers are free to visit the stations in any desired sequence. 

Each entity in the model of a job shop organization could have the following attributes: 

ArrivalTime: Time of arrival Type: The type of job, which implies the route. Location: The current location on the route relative to the beginning of the route. 

In addition, the model needs to store the route for each type of job. 

Suppose there are four workstations and three job types in a system.  Figure 2-3 shows a possible set of routings in matrix form. 

|**Job Type **|**First Operation**|**Second Operation**|**Third Operation**|**Fourth Operation**|
|---|---|---|---|---|
|**1**|Workstation 1|Workstation 2|Workstation3|Workstation 4|
|**2**|Workstation3|Workstation 4|None|None|
|**3**|Workstation 4|Workstation 2|Workstation3|None|



**Figure 2-3:  Example Routing Matrix for A Manufacturing Facility.** 

A routing process is included in the simulation model to direct the entity to the workstation performing the next processing step.  The routing process requires zero simulation time. 

Define State Variable: Route(3, 4) Define Attribute: Location Define Attribute: Type Process Routing Begin Location += 1 If Route(Type, Location) != None Then Begin Send to Process Route(Type, Location) End Else Begin Send to Process Depart End End 

2-7 

The value of the Location attribute is incremented by one.  The next workstation to process the entity is the one at matrix location (Type, Location).  If this matrix location has a value of None, then processing of the entity is complete.  Note again that the ability to compose a model of multiple processes is important. 

Alternatively, routes may be selected dynamically based on current conditions in a system as captured in the values of the state variables.  Such decision making may be included in a simulation model.  This is another unique and very powerful capability of simulation modeling. 

Consider a highly automated system in which parts wait in a central storage area for processing at any workstation.  A robot moves the parts between the central storage area and the workstations.  Alternatively if the following workstation is IDLE when an operation is completed, the robot moves the part directly to the next workstation instead of the storage area.  The routing process for this situation follows, where WSNext is the resource modeling the following workstation. 

_____________________________________________________________________________ Define Resource: WSNext/1:   States(Busy, Idle) Define State Variable: CentralStorage 

Process Conditional Routing Begin If WSNext/1 is Idle Then Begin Send to Process ForWSnext End Else Begin CentralStorage += 1 End End 

## 2.3.4 Batching 

Many systems use a strategy of grouping items together and then processing all the items in the group jointly.  This strategy is called batching.  Batching may occur preceding a machine on the factory floor.  Parts of the same type are grouped and processed together in order to avoid frequent setup operations.  Other examples include: 

- Bags of product may be stacked on a pallet until its capacity is reached.  Then a forklift could be used to load the pallet on a truck for shipment. 

- All deposits and checks received by a bank during the day are sent together to a processing center where bank account records are updated overnight. 

- A tram operating from the parking lot in an amusement park to the entrance gate waits at the stop until a certain number of passengers have boarded. 

Batching is the opposite of the lean concept of one-piece flow or one part per batch.  There is a trade-off between batching and one-piece flow.  Batching minimizes set up times and can make individual machines more productive.  One-piece flow minimizes lead time, the time between starting production on a part and completing it, as well as in-process inventories. 

Batching may be modeled by creating one group entity consisting of multiple individual entities. The group entity can be operated upon and routed as would an individual entity.  Batching can be undone, that is the group can be broken up into the original individual entities. 

2-8 

Returning to the single server workstation example of Figure 2-2, suppose that completed parts are transported in groups of 20 from the output buffer to input buffer of a second workstation some distance away.  At the second workstation, items are processed individually.  In the simulation model of this situation, the first 19 entities, each modeling an item to be transported, must wait until the twentieth entity arrives.  Then the 20 entities are moved together as a group. Each group is referred to as a **batch** .  Upon arrival at the second workstation, each entity individually enters the workstation buffer.  The batching and un-batching extension to the single server workstation model is as follows. 

Define Resource:  WS/1: States(Busy, Idle) Define List:            OutputBuffer Process Single Workstation with Output Buffer Begin Wait until WS/1 is Idle Make WS/1 Busy Wait for Operation Time Make WS/1 Idle If Length (OutputBuffer) < 19 then Begin Add to List(OutputBuffer) End Else Begin Wait for Transportation Time Send All Entities on List(OutputBuffer) to Process WS2 End End 

Consider the case where each of the types of items processed by the workstation must be transported separately.  In this situation, batching, transportation, and un-batching can be done as above except one batch is formed for each type of item. 

## 2.3.5 Inventories 

In many systems, items are produced and stored for subsequent use.  A collection of such stored items is called an inventory, for example televisions waiting in a store for purchase or hamburgers under the hot lamp at a fast food restaurant.  Customers desiring a particular item must wait until one is inventory. 

Inventory processes have to do with adding items to an inventory and removing items from an inventory.  The number of items in an inventory can be modeled using a state variable, for example INV_LEVEL.  Placing an item in inventory is modeled by adding one to the state variable:   INV_LEVEL += 1.  Modeling the removal of an item from an inventory requires two steps: 

1. Wait for an item to be in the inventory:  WAIT UNTIL INV_LEVEL > 0 

2. Subtract one from the number of items in the inventory:  INV_LEVEL -= 1 

## _2.4 Summary_ 

Simulation model construction approaches have been presented.  System components: arrivals, operations, routing, batching, and inventory management have been identified.  How each component is commonly represented in simulation models has been discussed and illustrated. 

2-9 

## **Problems** 

1. Discuss why it is important to be able to employ previously developed models of system components in addition to the more basic modeling constructs provided by a simulation language in model building. 

2. Discuss the importance of allowing multiple, parallel processes in a model. 

(For each of the modeling problems that follow, use the pseudo-English code that has been presented in this chapter.) 

3. Develop a model of a single workstation whose processing time is a constant 8 minutes. The station processes two part types, each with an exponentially distributed interarrival time with mean 20 minutes. 

4. Embellish the model developed in 3 to include breakdowns.  The time between breakdowns in exponentially distributed with mean 2 days.  Repair time is uniformly distributed between 1 and 3 hours. 

5. Build a model of a two-station assembly line serving three types of parts.  The sequence of part types is random.  The part types are distributed as follows: part type 1, 30%; part type 2; 50%, and part 3, 20%.  Inter-arrival time is a constant 5 minutes.  The first station requires a setup task of 1.5 minutes duration whenever the current part type is different from the preceding one.  The operation times are the same regardless of part type: station 1, 3 minutes and station 2, 4 minutes. 

6. Embellish the model in problem 5 for the case where there are two stations that perform the second operation.  The part goes to the station with the fewer number of waiting parts. 

7. Embellish the model in problem 5 for the case where a robot loads and unloads the second station.  Loading and unloading each take 15 seconds. 

8. Combine problems 5, 6, and 7 in one model. 

9. Consider Bob’s Burger Barn.  Bob has a simple menu: burgers made Bob’s way, french fries (one size), and soft drinks (one size).  Customers place orders with one cashier who enters the order and collects the payment.  They then wait near the counter until the order is filled.  The time between customer arrivals during the lunch hour from 11:30 to 1:00 P.M. is exponentially distributed with mean 30 seconds.  It takes a uniformly distributed time between 10 seconds and 40 seconds for order placement and payment at the cashier.  The time to fill an order after the payment is completed is normally distributed with mean 20 seconds and standard deviation 5 seconds. 

- a. Build a model of Bob’s Burger Barn. 

- b. Embellish the model for the case where a customer will leave upon arrival if there are more than 7 customers waiting for the cashier. 

10. Consider the inside tellers at a bank.  There is one line for 3 tellers.  Customers arrive with an exponentially distributed time between arrivals with mean 1 minute.  There are three customer types: 1, 10%; 2, 20%; and 3, 70%.  The time to serve a customer depends on the type as follows: 1, 3 minutes; 2, 2 minutes; and 3; 30 seconds.  Build a model of the bank. 

11. Modify the model in problem 10 for the case where there is one line for each teller. Arriving customers choose the line with the fewest customers. 

2-10 

12. Develop a process model of the following situation.  Two types of parts are processed by a station.  A setup time of one minute is required if the next part processed is of a different type that the preceding part.  Processing time at the station is the same for both part types: 10 minutes.  Type 1 parts arrive according to an exponential distribution with mean 20 minutes. Type 2 parts arrive at the constant rate of 2 per hour. 

13. Develop a process model of the following situation.  A train car is washed and dried in a rail yard between each use.  The same equipment provides for washing and drying one car at a time.  Washing takes 30 minutes and drying one hour.  Cars arrive at the constant rate of one each hour and three-quarters. 

14. Develop a model of a service station with 10 self-service pumps.  Each pump dispenses each of three grades of gasoline.  Customer service at the pump time is uniformly distributed between 30 seconds and two minutes.  One-third of the customers pay at the pump using a credit card.  The remainder must pay a single inside cashier which takes an additional 1 minute to 2 minutes, uniformly distributed.  The time between arrivals of cars is exponentially distributed with mean 1 minute. 

15. Mike’s Market has three check out lanes each with its own waiting line.  One check out lane is for customers with 10 items or fewer.  The check out time is 10 seconds plus 2 seconds per item.  The number of items purchased is triangularly distributed with minimum 1, mode 10, and maximum 100.  The time between arrivals to the check-out lanes is exponentially distributed with mean 1 minute. 

16. Develop a more detailed model of Bob’s Burger Barn (discussed in problem 9).   Add an inventory for completed burgers and another inventory for completed bags of fries.  Filling an order is an assembly process that requires removing a burger from its inventory and a bag of fries from its inventory.  The burgers are completed at a constant rate of 2 per minute.  It takes three minutes to deep fry six bags of fries. 

17. Develop a model of the following inventory management situation.  A part completes processing on one production line every 2 minutes, exponentially distributed and is placed in an inventory.  A second production line removes a part from this inventory every two minutes. 

18. Visit a fast food restaurant in the university student union and note how it serves customers.  Specify a model of the customer service aspect of the restaurant using the component models in this chapter. 

2-11
