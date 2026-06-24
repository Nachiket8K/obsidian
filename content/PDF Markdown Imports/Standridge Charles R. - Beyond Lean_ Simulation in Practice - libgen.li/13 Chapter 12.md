---
title: "Chapter 12"
book: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li"
source_pdf: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li.pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 12** 

## **Flexible Manufacturing Systems** 

## _12.1 Introduction_ 

Consider a manufacturing facility that is required to produce multiple part types.  Demand is insufficient to warrant a dedicated work cell for any part type.  However, demand for all part types together is sufficient to potentially justify automating the production process. 

What is needed in this case is a flexible manufacturing system (FMS).  Such a system operates efficiently and cost effectively regardless of the mix of part types produced.  It is comprised of flexible machines that perform a range of operations on a variety of parts with only minor setup required when switching between part types.  Such machines must be programmable or computer numerically controlled (CNC).  They must be capable of storing, automatically setting up (loading), and using a variety of tools.  A new part type could be introduced without significant additional capital investment, at least if it was sufficiently similar to existing part types. 

An FMS requires automated material handling capabilities to move parts between machines as well as into and out of the system.  An FMS must be highly automated and thus requires coordinated, computer based control. 

The initial capital cost of an FMS is high relative to a work cell dedicated to a single part.  This investment is worthwhile if the FMS can effectively produce a mix of part types more economically than can a set of dedicated work cells, one per type of part.  A flexible manufacturing system could have as many as 20 machines.  A system consisting of one or two flexible machines is called a cell. 

An FMS operates in a similar manner to a work cell.  A part arrives to a single load-unload station where it is attached to a fixture that is mounted on a pallet.  More than one part could be attached to the fixture.  Parts need not be batched by type upon arrival since machines are able to adapt to processing different part types with relatively little setup time.  Measuring the WIP is important since the WIP level is proportional to the number of pallets and fixtures needed. 

Since machines are flexible, more than one machine can perform each operation the part requires.  Thus, breakdowns do not hamper the operation of an FMS to the same degree as for a dedicated work cell. 

One aspect of the design of an FMS is the scheduling of parts on specific machines.  In this case study, the assignment of parts to machines using an optimization algorithm is compared with the use of a heuristic dynamic scheduling rule.  The performance measure of interest is the total time to produce a given number of parts. 

## _12.2 Points Made in the Case Study_ 

This FMS case study shows how optimization models and simulation models can be used together to address system design and operation issues.  An optimization model is used to assign parts, and consequently the tools need to operate on the parts, to machines.  A simulation model is used to assess how well the system operates using this assignment. 

In modeling an FMS system, each machine and each tool is modeled as a resource.  In addition, the model must keep track of which tool is on which machine.  Thus, complex logic for assigning resources representing machines and tools to work on parts represented by entities is required. How to choose between alternative resources must be specified.  Here, a choice between machines to perform the same operation must be made. 

12 **-** 1 

The simulation model must include the concurrent use of two resources, one a machine and another a tool.  Furthermore, a selection among available machines must be made.  Such logic may be coded in a high level programming language, such as C, and referenced from the simulation model. 

Complex system control logic may be included in a simulation model.  In this FMS model, a part waits to begin an operation until the required tool and any of the machines that can operate on it are available.  A list of such waiting parts must be maintained.  When tool and machines resources enter the free state, the model must search the entire list of waiting parts until one that can be processed by the newly freed resources is found.  It is possible that no such part will be found.  If the simulation engine does not examine each entity waiting for a resource, then logic to search the entire list of waiting transactions must be specified by the modeler. 

Previously, arrivals in a model represented a single entity entering a system.  In this case study, parts arrive to the FMS in a batch.  Thus, an entity arrival in the model represents a batch of parts. An arriving entity is cloned to create one entity for each part. 

A system may be sufficiently complex that simulation is necessary for analysis, design, and understanding even if no quantities are modeled using probability distributions.  This is due to the structural variability in the system.  Pritsker (1989) estimated that about one-third of all simulation projects employ deterministic models.  In this case study, the assignment of tools and part operations to machines over time is sufficiently complex that an intuitive understand of system dynamics is not possible.  Simulation is necessary to assess the affect of proposed assignments on system operations. 

The length of the simulation run need not be specified as a constant time but could be specified as a condition to be met.  In this case, the ending simulation time is the makespan of a production run, a performance measure of interest. 

## _12.3 The Case Study_ 

A flexible manufacturing cell consists of three types of flexible machines.  Each type of machine performs a different set of operations.  The cell must process three part types.  Each operation required by a part type uses one particular tool and can be performed on any of multiple machine types.  Not all machine types can perform all operations on all part types.  Operation times vary by machine type.  A tool is loaded on one of the machines at a time and may be moved between machines as needed. 

Figure 12-1 shows the system completely idle before a production run is made.  Tool bins hold the tools currently assigned to each machine.  The state of each machine, in terms of the type of part being processed, is shown.  The system contains two type A machines, two type B machines, and one type C machine. 

Production of 240 parts in one day is of interest.  Parts arrive in batches of 24 every 75 minutes starting at the beginning of the day.  The mix of part types in each batch is the same: 4 of type 1; 10 of type 2; and 10 of type. 

12 **-** 2 

**==> picture [298 x 194] intentionally omitted <==**

**----- Start of picture text -----**<br>
Machine Busy Part  1 Machine Idle<br>Tool<br>Bin<br>Machine Busy Part 2 Machine Busy Part  3<br>A B C<br>A B<br>Part Buffer<br>Type A Machine                  Type B Machine               Type C Machine<br>**----- End of picture text -----**<br>


**Figure 12-1:  Flexible Manufacturing System** 

Management wishes to minimize the makespan for the 240 parts as well as in-process inventory. Recall that the in-process inventory level is proportional to the number of fixtures and pallets the FMS requires.  The lead time for parts in the FMS is of interest.  The utilization of each machine is important. 

Part and tool movement between machines requires 30 seconds.  Machine setup time is minimal and can be ignored. 

Table 12-1 presents the operation time data. 

**Table 12-1:  Operation Times for the FMS System** 

||||**Operation Time (Min)**|**Operation Time (Min)**|**Operation Time (Min)**||
|---|---|---|---|---|---|---|
|**Part**<br>**Type**|**Parts to**<br>**Produce / Day**|**Operation**<br>**ID**|**Machine**<br>**Type A**|**Machine**<br>**Type B**|**Machine**<br>**Type C**|**Tool**|
|1|40|1|12|11|10|A|
|||2|13|15||B|
|||3|14|14||C|
||||||||
|2|100|1|2|4||A|
|||2|2|6|6|C|
||||||||
|3|100|1|4|||D|
|||2|5||8|E|
|||3|||4|F|



## 12.3.1 Define the Issues and Solution Objective 

The method for assigning a part operation, as well as the tool required by that operation to a machine, must be determined.  Two schemes are proposed. 

12 **-** 3 

1. Assign the part operation and tool to the IDLE machine with the shortest processing time for that operation at the time the part is ready to begin the operation.  (Dynamic Scheduling). 

2. Assign each part operation to one and only one machine type using the machine loading heuristic in Askin and Standridge (1993), pp. 144-153. 

Regardless of the scheme used, movement of parts and tools between machines will be minimized.  The subsequent operation on a part will be performed on the same machine as the current operation if subsequent operation is allowed on that machine and the required tool is already loaded on the machine.  Whether the same machine can perform the subsequent operation will be determined when the current operation is completed. 

Note that the first scheme uses any machine that can perform the operation on a part.  It selects between IDLE machines based on operation time, smallest time first.  It seeks to avoid part waiting and to minimize the waiting time for each operation. 

The second scheme seeks to balance the work load among the machines.  It will make a part wait for its assigned machine type even if a machine of another type is IDLE and could process the part. 

The priority order of machines for each operation on each part type using the dynamic scheduling approach with the machine having the shortest processing time given priority is shown in Table 12 **-** 2, which directly results from the data in Table 12-1. 

**Table 12-2:  Machine Priority -- Shortest Processing Time First Scheme** 

|**Part Type**|**Operation ID**|**First Priority**|**Second Priority**|**Third Priority**|
|---|---|---|---|---|
|1|1|C|B|A|
||2|A|B||
||3|B|A||
||||||
|2|1|A|B||
||2|A|C|B|
||||||
|3|1|A|||
||2|A|C||
||3|C|||



The machine loading heuristic of scheme 2 seeks to equalize the workload between machine types.  Results of applying the optimization algorithm to assign operations to machine types are given in Table 12 **-** 3. 

**Table 12-3:  Machine Priority -- Equalize Workload Among Machine Types Scheme** 

|**Part Type**|**Operation ID**|**First Priority**|**Second Priority**|**Third Priority**|
|---|---|---|---|---|
|1|1|C|||
||2|B|||
||3|B|||
||||||
|2|1|A|||
||2|A|||
||||||
|3|1|A|||
||2|A|||
||3|C|||



12 **-** 4 

Note the difference between the two schemes.  The first priority machine type for each is the same, except for operation 2 on part type 1.  In the first scheme, a part proceeds to a second or third priority machine if the first priority machine is busy.  In the second scheme, a part simply waits if the first priority machine is busy. 

## 12.3.2 Build Models 

The model includes arrivals of batches of parts as well as decomposing the batches into individual parts.  Thus, arriving entities represent batches of parts and subsequent entities represent parts. The part entities have the following attributes: 

ArrivalTime = Time of arrival to the FMS PartType = Part type Machine = Machine used in current operation Tool = Tool used in current operation OpTime = Operation time for current operation = f(machine used) CurrentOp = ID number of the current operation (1, 2, 3) 

The model of an operation on a part requires two resources, one representing a machine and the other a tool.  Movement between machines must be included in the model both for parts and tools.  An procedure to select the machine to perform an operation on a part is included as well as a second procedure to determine whether the machine on which a part currently resides can perform the next operation. 

Each tool resource has an attribute: ToolLocation = The machine on which it currently resides. 

The pseudo code for the arrival process follows. A batch of 24 parts arrives every 75 minutes. Ten batches arrive in total.  Each batch is separated into component parts: 4 of type 1, 10 of type 2, and 10 of type 3.  Each part is sent to a process that models the first operation that is performed on it. 

Define Arrivals: Batches Time of first arrival: 0 Time between arrivals: 75 minutes Number of arrivals: 10 Define Resources: // Flexible Machine Resources MachA_1/1 with states (Busy, Idle) MachA_2/1 with states (Busy, Idle) MachB_1/1 with states (Busy, Idle) MachB_2/1 with states (Busy, Idle) MachC_1/1 with states (Busy, Idle) // Tool Resources ToolA/1 with states (Busy, Idle) ToolB/1 with states (Busy, Idle) ToolC/1 with states (Busy, Idle) ToolD/1 with states (Busy, Idle) ToolE/1 with states (Busy, Idle) ToolF/1 with states (Busy, Idle) 

12 **-** 5 

Define StateVariables: WIPCount // Number of parts in FMS ToolLocation(5) // Tool location 

Define Lists: OpOneList OpTwoList OpThreeList 

Define Entity Attributes: ArrivalTime // Time of arrival to the FMS PartType //  Part type Machine //  Machine used in current operation Tool //  Tool used in current operation OpTime //  Operation time for current operation = f(machine used) CurrentOp //  ID number of the current operation (1, 2, 3) Process BatchArrival Begin ArrivalTime = Clock // arrival of a batch of 24 parts CurrentOp  =  1 PartType = 1 // type 1 parts Clone 4 OpFirst PartType = 2 // type 2 parts Clone 10 OpFirst PartType = 3 // type 3 parts Clone 10 OpFirst End 

Each part requires either two or three operations.  The processes for each of the operations are similar but not identical.  Each includes two essential steps:  the transportation of the part and tool to the machine, if required, followed by the actual operation on the part.  Two resources, a machine and a tool, are required.  Which machine is determined by the machine assignment scheme employed. 

At the beginning of the model of the first operation, the machine selection procedure is used to determine if the required tool is available.  If so, the procedure determines if any machine is available to process the part and if so which one should be employed.  The machine selection procedure is as follows: 

```
MACHINE SELECTION PROCEDURE (OPERATION_NUMBER, PART_TYPE)
{
IF THE REQUIRED TOOL RESOURCE FOR THE PART_TYPE FOR
OPERATION_NUMBER IS IN THE IDLE STATE
{
FOR EACH MACHINE TYPE IN PRIORITY ORDER
{
IF ANY MACHINE OF THAT TYPE IS IN THE IDLE STATE
{
Machine = RESOURCE ID OF SELECTED MACHINE
Tool    = RESOURCE ID NUMBER OF REQUIRED TOOL
OpTime  = OPERATION TIME FOR PART FOR OPERATION_NUMBER
RETURN
}
}
}
}
```

12 **-** 6 

If the required tool is not free or no machine is available to perform the operation, the part entity must wait in a buffer.  There is one buffer in the model for each of the three operations.  When a tool or machine resource becomes free, the model will search each buffer to find a part to process. 

If the required tool and a machine are available to process the part, the tool and machine resources enter the busy state.  Part entity attributes are assigned the name of the tool and machine as well as the process time for the operation on the selected machine.  A time delay to move the tool and or part to the selected machine is incurred.  The tool attribute recording its location (ToolLocation) is assigned the name of the selected machine.  The operation is performed on the part.  When the operation is completed, the tool resource enters the IDLE state. The lists of part entities waiting for operations 1, 2 or 3 are searched and the processing of another part is begun if possible. 

The pseudo code modeling the first operation follows. 

Process OpFirst Begin WIPCount ++ // Add one to number of parts in FMS MachineSelection (CurrentOp, PartType) If Machine is Null then Add entity to list Op1List Else Begin // Perform first operation Get Tool Get Machine ToolLocation (Tool) = Machine Wait for 30 seconds  // Tool and part movement Wait for OpTime       //  Perform operation Free Tool SearchforNextPart   // Procedure to search all lists for next part to use tool End Send to OpSecond End 

The model of the second operation begins by determining if the part can remain on the same machine using the subsequent machine procedure.  This will be the case if the machine is able to perform the operation and the tool required for that operation is available. 

If the part cannot remain on the machine used for the first operation, the resource modeling this machine enters the idle state.  The lists of part entities waiting for operations 1, 2 or 3 are searched and the processing of another part is begun if possible.  The machine selection procedure is used to attempt to find a machine to process the part entity completing the first operation in the same way as was done for the first operation. 

If the second operation can be performed on the same machine as the first, the tool resource for this operation enters the busy state, the operation is performed, and the tool resource enters the idle state.  The lists of part entities waiting for operations 1, 2 or 3 are searched and the processing of another part is begun if possible.  Type 2 parts do not require a third operation. Thus, at the end of the second operation, the machine resource processing a type 2 part enters the idle state and the search of the lists of waiting parts is conducted.  The pseudo code for the second operation follows.  The model of the third operation is similar to the model of the second operation. 

12 **-** 7 

`SUBSEQUENT MACHINE PROCEDURE (OPERATION_NUMBER, PART_TYPE, CURRENT_MACHINE) { IF THE REQUIRED TOOL RESOURCE FOR OPERATION_NUMBER ON THIS PART IS IN THE IDLE STATE { IF THE REQUIRED TOOL RESOURCE FOR OPERATION_NUMBER ON PART_TYPE IS LOADED ON CURRENT_MACHINE AND CURRENT_MACHINE CAN PERFORM OPERATION_NUMBER ON THIS PART_TYPE { THE REQUIRED TOOL RESOURCE ENTERS THE BUSY STATE Tool = RESOURCE ID NUMBER OF REQUIRED TOOL OpTime = OPERATION TIME FOR PART_TYPE FOR OPERATION_NUMBER } } }` Process OpSecond Begin CurrentOp = 2 SubsequentMachine (CurrentOp, PartType, Machine) If Tool is Null then Begin // Move to another machine Free Machine SearchforNextPart   // Procedure to search all lists for next machine to use tool MachineSelection (CurrentOp, PartType) // Find another machine If Machine is Null then Add entity to list Op2List Else Begin // Perform second operation on another machine Get Tool Get Machine ToolLocation (Tool) = Machine Wait for 30 seconds  // Tool and part movement Wait for OpTime       //  Perform operation Free Tool SearchforNextPart   // Procedure to search all lists for next part to use tool End End Else Begin // Perform second operation on current machine Get Tool Wait for OpTime       //  Perform operation Free Tool SearchforNextPart   // Procedure to search all lists for next part to use tool End Send to OpThird End 

## 12.3.3 Identify Root Causes and Assess Initial Alternatives 

The simulation experiment will determine both the makespan for 240 parts as well as the number of pallets and fixtures required.  The latter can be accomplished by measuring the number of parts in the FMS as was previously discussed. 

12 **-** 8 

The design of the simulation experiment is summarized in Table 12-4.  We are interested in the time to produce 240 parts.  Thus, a terminating experiment with initial conditions of no parts in the system is appropriate.  Since no quanities are modeled using probability distributions, no random number streams are needed and one replicate is sufficient.  The two schemes for assigning parts to machines identified above are to be simulated.  Performance measures have to do with the time to complete production on 240 parts, the lead time for parts, the number of parts in the FMS (WIP), and the utilization of the machines. 

Results are shown in Table 12 **-** 5. 

**Table 12-4:  Simulation Experiment Design for FMS Machine Loading** 

|**Element of the Experiment**|**Values for This Experiment**|
|---|---|
|Type of Experiment|Terminating|
|Model Parameters and Their Values|Machine load scheme used:<br>1.  Available machine with the shortest processing<br>time<br>2.  Machine loading heuristic from Askin and<br>Standridge|
|Performance Measures|1.  Time to produce 240 parts<br>2.  Number of parts in the FMS (WIP)<br>3.  Part Lead Time<br>4.  Machine Utilization|
|Random NumberStreams|None|
|InitialConditions|Empty buffers andidle stations|
|Numberof Replicates|1|
|Simulation EndTime|Time to produce240 parts|



**Table 12-5:  Simulation Results for FMS Machine Loading** 

||**Loading Scheme**|**Loading Scheme**|
|---|---|---|
|**Performance Measure**|**Shortest Processing Time**<br>**First**|**Balance Machine Type**<br>**Workloads**|
|Makespan(Minutes)|1099|900|
|WIP –<br>Average<br>Maximum|30.8<br> 63|46.2<br>86|
|Lead Time (Minutes) –<br>Average<br> Standard deviation|141<br>114|173<br>74|
|Machine Utilization –<br>Type A<br>Type B<br>Type C|69.5%<br>72.5%<br>70.0%|82.8%<br>67.5%<br>96.0%|



The makespan for the balance machine type workloads approach is 199 minutes less than for the shortest processing time first approach.  The former approach results in higher utilizations for machine types A and C as well as a lower utilization for machine type B.  Recall that operations were assigned to machine types A and C instead machine type B since the operation times for machine type B most often were higher than for the other two types. 

Recall from the VUT equation that increasing the utilzation results in a longer lead time at a station.  Thus, it could be expected that the balance machine type workloads approach would have a longer lead time than the shortest processing time first approach.  In addition, Little’s Law 

12 **-** 9 

indicates that the WIP is proportional to the lead time and thus could also be larger.  However, the balance machine type workloads scheme reduces the standard deviation of the lead time. 

The maximum number of parts in the FMS is higher under the balance machine type workloads approach.  This means that more fixtures and pallets are required using this approach. 

## 12.3.4 Review and Extend Previous Work 

Management accepted the simulation results presented in the previous section and decided to use the balance machine type workloads scheme.  This decision was primarily based on the need to mimimize makespan.  The cost of additional fixtures and pallets will be bourn to support this approach. 

## 12.3.5 Implement the Selected Solution and Evaluate 

During system operation, the time to produce a required batch of parts and the number of parts in the FMS will be monitored. 

## _12.4 Summary_ 

This case study shows how ad hoc operating rules, such as use the idle machine with the shortest processing time, are often inferior to operation rules developed using formal models.  Simulation is used to test alternative rules and quantify the difference in their effects.  Because systems are complex, simulation is needed even when such system operating models are deterministic. Complexity arises from the concurrent use of multiple resources such as tools and machines as well as the ability of resources such as machines to serve multiple tasks.  The need for the model to organize and manage entities waiting for such resources instead of relying on the simulation engine to do so transparently to the model has been demonstrated. 

## **Problems** 

1. Provide validation evidence for the FMS machine loading simulation based on the tool and machine utilization.  Compute the expected utilization of each tool and machine type. Compare these results to the simulation results for the balance machine type workloads case.  The machine utilization is shown in Table 12-5. 

Tool Utilization A 74.2% B 68.9% C 93.8% D 50.5% E 59.8% F 49.5% 

2. Tell why the standard deviation of the time parts spend in the FMS (lead time) is greater than 0 since there are no random variables in the model. 

3. Is it proper to compute a t-confidence interval for the mean part lead time?  Why or why not? 

4. Defend the use of the shortest processing time first loading scheme based on the simulation results shown in Table 12-5. 

5. List service systems that you have encountered that have the flexibility characteristics of the manufacturing system discussed in this chapter. 

12 **-** 10 

6. Compare the model of the FMS to the model of the serial system discussed in chapter 7. 

7. Write the model of third operation on a part in pseudo-code. 

8. The model in this case study assumes that tools and parts can be moved concurrently to a machine.  Modify the process model so that first the part is moved then the tool. Movements occur only if the part or tool is not resident on the selected machine. 

9. Resimulate the model with all parts available for processing at time 0 and compare the results to those in Table 12 **-** 5. 

10. Simulate the following improved version of the shortest processing time first rule and **-** 

compare the results with those in Table 12 5.  Don’t allow operation 1 on machine type A. 

11. Assess the effect of operation clustering on machine loading.  Operations are assigned to specific machines, not just machine types.  All part type 2 operations are assigned to one type A machine along with the first operation for part type 3.  The second operation for part type 3 is assigned to the other A machine.  The third operation for part type 3 is assigned to the type C machine.  The first operation for part type 1 is assigned to the type C machine, the second to one type B machine, and the third to the other type C machine. 

12. Develop and test heuristics that embellish the operation clustering based assignment given in the previous problem.  For example, allow the least utilized machine to be a second priority for the most utilized machine if feasible. 

13. Management will purchase one more tool of any of the six tool types if that will help shorten makespan.  Which tool should be purchased?  Evaluate your choice using the simulation model developed in this chapter. 

14. Test the idea that a part should stay on the same machine as long as it is feasible for that machine to perform the next operation on the part.  In this case, the required tool is moved to that machine as soon as it is idle. 

## **Case Problem** 

A flexible manufacturing facility must produce 1680 parts of one type per 80-hour lead (Wortman and Wilson, 1984; Kleijnen and Standridge, 1988).  The part flow through the facility is follows. 1. Parts arrive to the facility from a lathe at a constant rate of 21 per hour. 

2. Parts require three operations in the following sequence: Op10, Op20, and Op30. 

3. A part is washed before and after each operation. 

Each operation is performed either by a fixed machine or a flexible machine.  A fixed machine can perform one and only one of three operations but a flexible machine can perform any of the three operations.  Parts are moved between machines and the wash station by a single automated guided vehicle (AGV).  The AGV system transports parts with little or no human assistance.  The vehicle picks up loads at designated pick-up points and transports them to designated drop-off points.  Each pick-up and drop-off point is associated with a machine or work station.  A central computer assigns material movement tasks to the AGV and monitors the vehicle position.  The AGV moves in one direction on a fixed track around the center of the system. 

Operation processing times are 14.0, 5.0, and 8.0 minutes respectively for Op10, Op20, and Op30.  Washing time is 18 seconds. 

AGV travel time is 20 seconds around the entire loop.  The following table shows AGV travel time between each pair of workstations. 

12 **-** 11 

||**Wash Station **|**OP 10**|**OP 20**|**OP 30**|**Flexibile**|
|---|---|---|---|---|---|
|**Wash Station **|0|5|9|15|11|
|**OP10**|5|0|4|10|6|
|**OP20**|9|4|0|15|11|
|**OP30**|15|10|15|0|16|
|**Flexible**|11|6|11|16|0|



Figure 12-2 gives an overview of the system at the beginning of the production period with all machines idle and no parts in the system.  Part movement by the AGV is indicated.  The particular operation performed by each machine is displayed. 

**==> picture [405 x 284] intentionally omitted <==**

**----- Start of picture text -----**<br>
Operation 30 Machines<br>Op. 10               Op. 20<br>Op. 30               Idle<br>Machine States<br>Flexible<br>Machines Wash<br>Station<br>=| | }<br>AGV Track<br>a e<br>Operation 20<br>Machines<br>3) | | |<br>From<br>Lathe<br>faa<br>Operation 10 Machines<br>|<br>**----- End of picture text -----**<br>


Figure 12-2:  Overview of the Flexible Manufacturing System: (4,2,2,1) Configuration. 

The objective is to find the minimum cost combination of fixed machines (Op10, Op20, or Op30 only) and flexible machines (all three operations) that meets the throughput requirement.  Flexible machines cost more than fixed machines.  Thus, all possible work should be done by fixed machines.  Flexible machines are employed to avoid buying an excessive number of fixed machines.  In addition, management is also interested in minimizing lead time for a part.  Thus, management will consider a configuration of machines that includes flexible machines and increases cost in order to reduce lead time as long as the total number of machines does not exceed the total number of fixed machines required to do the work by more than one. 

The following operating rule is employed for each operation to select between fixed and flexible machines.  A part will use a fixed machine if it is available.  If not, it will use a flexible machine if one is available.  If neither a fixed machine nor a flexible machine is available, the part will use the first machine of either type, fixed or flexible, that becomes available. 

One possibility that should be considered is using the minimum number of fixed machines needed to process all parts in a timely fashion with no flexible machines utilized. 

12 **-** 12 

Assess the structural variability seen in this system.  Generate a trace of all system activities.  Use the trace to identify the structural variability. 

Case Problem Issues 

1. What performance measure are important in this problem? 

2. How will the AGV system be modeled? 

3. Describe how to model the choice between a fixed and a flexible machine for an operation in the simulation language you are using. 

4. When does a part entity acquire and free a machine resource relative to acquiring and freeing the AGV resource? 

5. How can the effect on system operations of part waiting for the AGV be determined. 

6. How many fixed machines of each type are needed if no flexible machines are used? 

7. Construct an alternative to the machine configuration in number 6 as follows. Replace one fixed machine of each type with a sufficient number of flexible machines.  Determine the number of flexible machines in this case. 

8. 

- Why tell why all parts do not have the same time in the system. 

12 **-** 13 

## **Part IV Supply Chain Logistics** 

Previous parts of this book discussed fundamental organizations of systems and strategies for operating those systems.  This part deals with supply chain management which is defined by Hopp and Spearman (2007) to be: The overall system wide co-ordination of inventory stocks and flows to ensure the purpose of inventories is met with minimal dollar investment. 

A publication from Jones-Lang-LaSalle (2008) defines the lean supply chain as “a set of organizations directly linked by upstream and downstream flows of products, services, finances and information that collaboratively work to reduce cost and waste by efficiently and effectively pulling what is required to meet the needs of the individual customer.”  The focus of part IV is on lean supply chain logistics that is the flow of product between organizations to minimize inventory and the cost of movement, particularly transportation equipment such as trucks and rail cars.  A key element of lean supply chain logistics is demand management: Providing products and services when requested (pulled) by the customer.  Thus, movement of product is a function of customer demand. 

The use of modeling and analysis in achieving lean supply chain logistics with proper demand management is discussed. Ideally, there would be zero inventory.  Product would be instantaneously delivered to customers who would immediately consume it upon arrival.  There would be no in process inventory except for items currently being operated upon. 

However, inventory must be kept to deal with variation, both random and structural (generated by design), in demand, production, and delivery.  All inventory raises costs without adding value to a product.  Thus, the management of inventory involves trading off lower costs with having enough product, raw material, and partially finished goods to meet customer demands and keep operations working. 

Chapter 13 discusses the management of a retail store inventory by a supplier.  Detailed operations are not included.  Only daily demand and production volumes are modeled.  Inventory levels as well as production schedules are determined.  Analytic computations aid in setting inventory levels. 

Chapter 14 discusses the logistics of moving goods and maintaining a fleet of trucks to do so. The use of simulation in determining the number of trucks required to meet customer service level expections is shown.  This is known as fleet sizing. 

Chapter 15 discusses maintaining inventory at multiple locations in a complex supply chain.  Rail movements between locations are described.  Time varying expected demand for product is included.  Building inventory in advance for periods when the expected demand exceeds production capacity is described.  The use of customer services levels as the primary driver of supply chain logistics is discussed.
