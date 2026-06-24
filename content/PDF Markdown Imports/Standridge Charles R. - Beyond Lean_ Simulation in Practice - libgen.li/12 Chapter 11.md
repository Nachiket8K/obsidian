---
title: "Chapter 11"
book: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li"
source_pdf: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li.pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 11** 

## **Cellular Manufacturing** 

## _11.1 Introduction_ 

Cellular manufacturing systems provide an alternative organization to serial lines and job shops for producing products.  Manufacturing is reorganized into cells that provide the operational benefits of a serial line.  Each cell performs all of the processing needed on one, or at most a few, similar part types.  Each part is processed in the same sequence through a series of machines or manual operations.  Cellular manufacturing is effective whenever production volumes are sufficiently high to justify dedicated equipment and only a short series of production steps are required. 

For example, the job shop discussed in chapters 8 and 10 could be reorganized into 3 cells, one for each of the three part types.  Each cell would behave like the serial line discussed in chapter 7. Each cell would have a sufficient number of each kind of machine to process the type of part for which it was responsible. 

Notice that the cellular manufacturing approach eliminates, or at least reduces, the need for setups, since only one part or a small number of similar parts are processed in a particular cell. 

Cellular manufacturing seeks to minimize the movement distance of parts within a cell.  In addition, each worker in a cell may support multiple operations at several workstations.  Thus, each workstation and its machines must be placed in close proximity with all other workstations. A straight line layout results in the first workstation being too distant from the last workstation. Alternative, a U-shaped layout is often used to meet the workstations close together requirement. This is illustrated in Figure 11-1. 

11 **-** 1 

**==> picture [48 x 49] intentionally omitted <==**

**==> picture [242 x 69] intentionally omitted <==**

**==> picture [55 x 49] intentionally omitted <==**

**==> picture [142 x 64] intentionally omitted <==**

**==> picture [55 x 49] intentionally omitted <==**

**==> picture [55 x 49] intentionally omitted <==**

**==> picture [49 x 55] intentionally omitted <==**

Some companies, such as Innotech, organize all production into cells.  Each cell is operated by its workers as an independent business.  The businesses share some common resources such as shipping docks and material handling equipment.  Rubich and Watson (1998) give some advantages of this approach. 

- Improved communication and teamwork – operators are close enough to talk and help each other if necessary. 

- An understanding of the entire manufacturing process from raw material to finished product 

- An opportunity to meet and discuss issues with customers if any customer concerns develop 

- An environment where cell operators have a greater sense of control in how their business (cell) is run 

- Responsibility and ownership for producing high quality products on time 

- Higher job satisfaction through increased job responsibility and variety 

Another goal of cellular manufacturing is to minimize the work-in-process inventory.  This is accomplished using the principle of one piece flow that seeks to move individual parts through a work cell as quickly as possible.  A worker seeks to keep one piece or part moving through the entire cell.  This is the opposite approach to processing multiple parts (a batch) at one workstation and then moving the entire batch to the next workstation for processing.  In other words, one piece flow uses a batch size of one. 

One piece flow can be used to minimize WIP which results in shorter lead time according to Little’s Law.  Required manufacturing space is reduced through better layouts and WIP reduction, which also simplifies material handling. 

11 **-** 2 

One piece flow works as shown for two stations in Figure 11-2.  Initially, the diamond part has completed processing at WS1 and the circle part is waiting in the buffer.  The worker arrives to WS1.  First the worker removes the diamond part from the machine.  Next the worker initiates the circle part on the machine.  Finally, the worker moves the diamond part to WS2 and then initiates that part on the machine. 

Cellular manufacturing employs a pull strategy.  The number of parts the cell must produce per day (or week or month) is established based on the known or forecasted demand for parts.  The number of available work hours is set.  Then the takt time is computed using equation 11-1. 

available work hours per day takt time  (11-1) demand per day 

The takt time is the maximum time between parts completed by the work cell if demand is to be met.  It is also in a sense the mimimum time.  If the cell completes parts faster than the takt time, too many parts are made. 

The time between completion of parts at the slowest workstation in the cell should not exceed the takt time.  This means that the operation time at that workstation should be less than the takt time. Furthermore, one piece flow is assisted greatly by making the operation time at each workstation as close to the same as possible. 

This application study presents the use of simulation in determining the staffing for a manufacturing cell.  Alternative assignments of workers to machines in the cell are considered. The effect of variation on cell operations is assessed.  The use of simulation to evaluate and enhance the original cell staffing plan developed using standard cellular manufacturing computations is shown. 

11 **-** 3 

**==> picture [115 x 88] intentionally omitted <==**

**==> picture [73 x 73] intentionally omitted <==**

**==> picture [153 x 72] intentionally omitted <==**

**==> picture [73 x 72] intentionally omitted <==**

**==> picture [215 x 217] intentionally omitted <==**

## _11.2 Points Made in the Case Study_ 

Some benefits of using simulation to enhance lean manufacturing techniques are illustrated.  The effect of random variation in raw material (part) arrival times as well as worker walking times is taken into account.  Performance of the cell, in terms of the maximum work-in-process and throughput, is predicted.  The simulation model and experiment are used to validate the cell design generated by traditional cellular manufacturing computations.  Operating rules to coordinate part arrivals and the movement of the cell operators are tested. 

The movement of both a part through the operations of the cell and a worker from workstation to workstation within a cell must be included in the model.  The movement of workers is used as the perspective for model building.  The number of parts in each area of each cell is counted.  Part movement results in changes in the counts.  The average part cycle time in the cell can be estimated from the average number of parts in the cell using Little’s Law.  This approach is based on a technique developed by Hyden, Roeder and Schruben (2001). 

11 **-** 4 

Random variation in worker walking time may be significant since waiting while a worker walks between machines may cause a delay in the start of an operation.  Such delays could effectively reduce the capacity of the cell.  Thus, the cell could fail to meet its throughput target. 

The work done at a workstation must be modeled as multiple tasks: initiating an operation, the operation itself, and removing the part from the machine after the operation is completed. Different resource combinations, machines and workers, are required for each task.  Thus, the joint allocation of machine and worker resources must be accomplished. 

More than one worker is required to staff the cell.  The effectiveness of alternate assigments of workers to workstations can be determined using simulation experiments. 

A trace of worker activities can be generated to aid in model validation.  The trace is used to provide evidence that the worker moves through the cell as was intended. 

## _11.3 The Case Study[1]_ 

This application study has to do with validating the design of a new manufacturing cell particularly with respect to staffing requirements as well as work in process inventory levels and throughput. An initial value for the number of workers required as well as an initial assignment of workers to workstations can be determined by standard, straightforward cellular manufacturing computations. 

A simulation study is required to validate that the number of workers and their assignment to workstations determined by the cellular manufacturing analysis will allow the cell to meet its throughput requirements.  The effect on throughput as well as WIP due to other assignments and numbers of workers can be evaluated. 

Factors not included in the initial calculations can be taken into account in the simulation model. Task and walking times as well as the time between arrivals of parts may be random variables. Cell operating rules for co-ordination between the activities of multiple workers as well as part arrivals to the cell is necessary. 

## 11.3.1 Define the Issues and Solution Objective 

A new manufacturing cell is being implemented.  The design of the cell is shown in Figure 11-3. The cell consists of seven workstations each with one machine as well as a raw material inventory of parts to process.  A completed finished goods inventory is included. 

The work area at each work station is shown by a heavy dot.  The worker walking path in the cell is shown by a line.  Note that a worker may walk directly between workstation M2 and workstation M6.  The worker who is responsible for a machine also walks the part from the immediately preceding workstation or inventory.  The worker responsible for workstation M7 also walks a completed part to the finished goods inventory. 

Table 11-1 provides basic data concerning the operation at each workstation.  All times are in seconds.  Manual times represent the constant standard times. 

> 1 Professor Jon Marvel defined this application problem as well as providing other invaluable assistance.  Mr. Joel Oostdyk implemented a prototype model.  Ms. Michelle Vette provided some excellent insight for improving the application problem. 

11 **-** 5 

**Table 11-1: Workstation Processing Information (Times in Seconds)** 

|**Workstation / Task Name**|**Workstation**<br>**/ Task ID**|**Initiation**<br>**Time**<br>**(Manual)**|**Operation**<br>**Time**<br>**(Automated)**|**Removal**<br>**Time**<br>**(Manual)**|**Total**<br>**Time**|
|---|---|---|---|---|---|
|PickUpRaw Material|RM|4|||4|
|TurnOuter Diameter|M1|4|23|3|30|
|BoreInner Diameter|M2|5|41|4|50|
|FaceEnds|M3|4|32|4|40|
|Grind Outer Diameter|M4|3|29|3|35|
|Grind Outer Diameter|M5|3|29|3|35|
|Inspect|M6|14|||14|
|Drill|M7|3|24|3|30|
|Placein Finished GoodsInv.|FG|5|||5|
|Total||45|168|20|233|



**==> picture [47 x 49] intentionally omitted <==**

**==> picture [48 x 118] intentionally omitted <==**

**==> picture [47 x 118] intentionally omitted <==**

**==> picture [47 x 95] intentionally omitted <==**

**==> picture [47 x 51] intentionally omitted <==**

**==> picture [48 x 50] intentionally omitted <==**

**==> picture [47 x 50] intentionally omitted <==**

**==> picture [47 x 118] intentionally omitted <==**

**==> picture [104 x 47] intentionally omitted <==**

The cell is responsible for producing 1000 units of one part each day.  The cell will operate for two shifts of 460 minutes each.  Thus the takt time is computed using equation 11-1 to be: 

available work time per day 460 _X_ 2 takt time    0 .920 minutes  55 .2 seconds demand per day 1000 

11 **-** 6 

The number of workers needed in the cell can be determined as follows.  Notice that the total manual operation time, the time a worker is required, is shown in Table 11-1 to be 65 ( = 45 + 20) seconds.  This total time divided by the takt time (65 / 55.2) is between 1 and 2.  Thus, a minimum of two workers is required. 

In addition, worker walking time must be taken into account.  It is highly desirable to have workers walk a circular route.  Walking time plus manual task time for the route must be less than the takt time.  Any assignment should seek to balance the manual operation plus walking time among the workers.  Workers walk on the average of 2 feet per second. 

Table 11-2 shows the walking distance between adjacent workstations. 

**Table 11-2: Walking Distances Between Workstations** 

|**Workstation / Task ID**|**Workstation / Task ID**|**Walking Distance (feet)**|
|---|---|---|
|RM|M1|7|
|M1|M2|7|
|M2|M3|7|
|M2|M6|8|
|M3|M4|8|
|M4|M5|8|
|M5|M6|7|
|M6|M7|7|
|M7|FG|10|



One possible assignment using two workers is the following (Assignment A): 

Worker 1:  RM, M1, M2, M7, FG 

(Task time, 31 seconds; walking time, 21.5 seconds; total time, 52.5 seconds) 

Worker 2:  M3, M4, M5, M6 

(Task time, 34 seconds; walking time, 19 seconds; total time, 53 seconds) 

The standard work cell design procedures did not take into account the following factors that may proof to be significant in the operation of the cell: 

1. Walking times are modeled as triangularly distributed random variables with the minimum equal to 75% of the mean and the maximum equal to 125% of the mean.  Based on the VUT equation, this could add to the cycle time and WIP in the cell.  Thus, the effect of random walking times needs to assessed. 

2. There is concern as to whether a constant time between arrivals of parts from another area of the plant can be achieved.  The practical worst case assumptions (Hopp and Spearman, 2007) lead to modeling the time between arrivals as exponentially distributed with mean equal to the takt time.  Again by the VUT equation, considering the time between arrivals to be a random variable could add to the cycle time and WIP in the cell. Thus, the performance of the cell for the case of a constant interarrival time for parts must be compared to the case of an exponentially distributed interarrival time. 

3. The following operational rule will be employed.  Worker 1 will wait at the raw material station and worker two will wait at station M2 until a part is available to walk to the next station. 

The simulation study must show that the above assignment is feasible, given the three operational factors.  Furthermore, the utilization of workers in the proposed assignment scheme is very high, 95% for worker 1 and 96% for worker 2.  It is possible that it is not feasible to effectively co- 

11 **-** 7 

ordinate the tasks of both workers and the operations of the machines.  Thus as alternative assignment was proposed (Assignment B). 

Worker 1: RM, M1, M2 (Total time, 41 seconds) 

Worker 2: M3, M4, M5 (Total time, 43 seconds) 

Worker 3: M6, M7, FG (Total time, 42 seconds) 

Each worker has several tasks.  Each task must be performed in sequence as the worker walks around the cell.  For example, worker 1 in assignment A has the following sequence of tasks: 

1. Wait for part at RM 

2. Process part at RM 

3. Move part from RM to M1 

4. Unload previous part from M1 

5. Initiate part on M1 

6. Move unloaded part from M1 to M2 

7. Remove part from M2 

8. Initiate part unloaded from M1 on M2 

9. Walk without a part to M6 

10. Wait for an inspected part 

11. Walk with an inspected part from M6 to M7 

12. Remove part from M7 

13. Initiate inspected part on M7 

14. Walk with part removed from M7 to FG 

15. Process part at FG 

16. Walk with no part to RM 

The following priorities are of fundamental importance in achieving one piece flow and not loosing machine capacity.  These are reflected in the worker task sequence. 

1. After removing a part from a machine, a worker will start another part on the same machine if one is available before performing any other task. 

2. After walking a part from a preceding workstation or inventory and upon arriving at the next workstation, the worker will initiate the operation on a part, if the machine is available. 

From the point of view of a part, the work cell will operate in the following way.  Parts arrive to the raw material inventory from another area of the plant.  The average time between arrivals is equal to the takt time. 

Parts move through the same processing steps at each workstation except M6:  initiation on the machine by a worker, automated processing by the machine, and removal from the machine by a worker.  Processing at M6 is consists of one manual inspection step. 

Workers move parts between machines as well as from the raw materials inventory to the first workstation and from the last workstation to the finished good inventory.  Part processing and movement is constrained by the availability of workers and machines. 

## 11.3.2 Build Models 

The model will be built from the perspective of worker movement.  A worker walks between stations in a prescribed route and performs one or two tasks at each station.  Parts reside in inventories.  A typical station has the following inventories:  waiting for initiation on a machine, waiting for unloading from a machine, and waiting to be walked to the next station.  A worker action changes the number of parts in one of the inventories. 

11 **-** 8 

The model consists of four processes: 

1. Arrival of parts to the raw material inventory. 

2. Worker 1 

3. Worker 2 

4. Automated processing on a machine which does not require worker assistance. 

The following inventories exist in the model. 

1. Workstations M1 – M5 and M7:  waiting for initiation on a machine (WaitInitialize), waiting for unloading from a machine (WaitUnload), and waiting to be walked to the next station (WaitWalk). 

2. Workstation M6:  waiting to be walked to the next station (WaitWalk). 

3. Raw materials: (RMInv) 

4. Finished goods: (FGInv) 

Entities in the arrival of parts process and the automated processing process represent parts.  For the latter process, entity attributes are: 

1. ID:  ID number of the workstation station where automated processing occurs:  1, 2, 3, 4, 5, or 7. 

2. OpTime:  Processing time at the workstation. 

The worker is the only entity in the worker process.  This entity has one attribute: 

1. WithPart:  1, if the worker has a part when walking between workstations and zero otherwise. 

The following variables are used in the model. 

1. WIPCell: The total number of parts in the work cell 2. WalkTime (9, 9): Average walking time between each pair of stations, FG (8), and RM(9). 

The part arrival process follows. A part arrives and the RM inventory is increased by 1 as well as the total WIP in the cell. 

11 **-** 9 

Define Arrivals: Parts Time of first arrival: 0 Time between arrivals: Exponentially distributed with a mean of 55.2 seconds Number of arrivals: Infinite 

Define Resources: M(7)/1 with states (Busy, Idle) // Workstation resources Define Entity Attributes: WorkstationID // ID number (1, …, 7) of workstation to process a part OperationTime // Time to process a part at a workstation WithPart // The number of parts carried by a worker from station to station (0, 1) Define State Variables WIPCell // The amount of work-in-process in the cell RMInv // Raw material inventory FGInv // Finished goods inventory WaitInitialze(7) // Number of items waiting for initialization at a workstation WaitUnload(7) // Number of items waiting unloading at a workstation WaitWalk(7) // Number of items wating to be walked to the next workstation WalkTime (9, 9) // Inter-station walk times Process PartArrival Begin WIPCell ++ RMInv ++ End 

The automated processing process is exactly the same as the single worker station process discussed previously.  Upon the completion of processing, the number of parts waiting to unload is increased by one. 

Process AutomatedMachine Begin WaitUntil M(WorkstationID)/1 is Idle in Queue QM(WorkstationID) Make M(WorkstationID)/1 Busy Wait for OperationTime Make M(WorkstationID)/1 Idle WaitUnload(WorkstationID) ++ End 

The process for Worker 1 starting at RM through arrival at workstation M2 follows.  Note that the worker waits at RM for a part to carry to workstation M1.  Otherwise, the worker will carry a part between workstations, unload a part or initialization a part only if a part is available.  Each inventory is updated as the worker acts. 

11 **-** 10 

Process Worker1 Begin // From raw material inventory to M1 Wait until RMInv > 0 // Wait for the next part Wait for 4 seconds // Processing at raw material inventory RMInv – // Update raw material inventory WithPart = 1 // Worker carrying one part Wait for triangular WalkTime(9,1)*75%, WalkTime(9,1), WalkTime(9,1)*125%  // To M1 WaitInitialize (1) ++ // Add to initialize inventory at M1 

// Processing at M1 If WaitUnload(1) > 0 then Begin // Unload Part at M1 Wait until M(1)/1 is Idle in Queue QM(1) Make M(1)/1 Busy Wait for 3 seconds Make M(1)/1 Idle WaitUnload(1)-WaitWalk(1)++ End If WaitInitialize(1) > 0 then Begin // Initialize Part at M1 Wait until M(1)/1 is Idle in Queue QM(1) Make M(1)/1 Busy Wait for 4 seconds Make M(1)/1 Idle WaitInitialize(1)— // Process part in parallel with worker walking ID = 1 OperationTime = 23 Clone to AutomatedMachine End If WaitWalk(1) > 0 then Begin // Walk with part WaitWalk(1) – WithPart = 1 End Else WaitPart = 0 // No part Wait for triangular WalkTime(1,2)*75%, WalkTime(1,2), WalkTime(1,2)*125%  // To M2 WaitInitialize(2) ++ // Arrive at M2 and Update Inventory End 

11.3.3 Identify Root Causes and Assess Initial Alternatives 

Experimentation with the model is used to address the issues previously raised with respect to performance of the cell. 

11 **-** 11 

1. The effect of random walking times. 

2. The effect of random times between arrivals. 

3. The number of workers used in the cell: 2 or 3. 

4. The effect of operational rules for workers. 

The amount of work in process in the cell should be very low.  Thus, the total WIP in the cell will be used as a performance measure.  The WIP at RM is also of interest.  In addition, a trace showing the time sequence of worker movements and activities is desired for both model and cell design validation. 

The design of the simulation experiment is shown in Table 11-3.  Since the cell is assigned a certain volume of work each day, a terminating experiment of duration one work day (920 minutes) is used.  Twenty replicates are used.  Random number streams are needed for worker walking time as well as the time between arrivals. 

**Table 11-3: Simulation Experiment Design for the Manufacturing Cell** 

|**Element of the Experiment**|**Values for This Experiment**|
|---|---|
|Type of Experiment|Terminating|
|Model Parameters and Their Values|1.  Time between arrivals (random or constant)<br>2.  Numberof workers (2or3)|
|Performance Measures|1.  WIP in the cell<br>2.  WIPatRM|
|Random Number Streams|1.  Worker walking time<br>2.  Time betweenarrivals|
|InitialConditions|One part at eachstation|
|Numberof Replicates|20|
|Simulation EndTime|920minutes (one day)|



Initial conditions of that reflect the principle of one piece flow are appropriate.  Thus, there is one part at each station initially.  At all stations except M6, the part is placed in the WaitUnload inventory.  At station M6, the part is placed in the WaitWalk inventory. 

Simulation results for the cases when 2 workers are used are shown in Table 11-4. 

The cell performs very well when the time between arrivals is constant.  The maximum number of parts in the cell is 9, one more than the number of stations plus the raw material inventory.  At most 1 part is in the raw material inventory.  However, when the time between arrivals is exponentially distributed, large maximum WIP sizes are seen both in the cell in general and in the raw material inventory.  Note, however, that the difference between the maximum WIP in the cell and the maximum WIP in the raw material inventory for each replicate is either 7 or 8.  Thus, WIP is properly restricted to the raw material inventory. 

11 **-** 12 

**Table 11-4:  Work in Process in the Cell and in RM – Two Workers Cases** 

||**Maximum WIP in Cell**|**Maximum WIP in Cell**|**Maximum WIP in Cell**|**Maximum WIP in RM**|**Maximum WIP in RM**|**Maximum WIP in RM**|
|---|---|---|---|---|---|---|
|**Replicate**|**Constant**<br>**Time**<br>**between**<br>**Arrivals**|<br> <br> <br>**Random**<br>**Time**<br>**between**<br>**Arrivals**|<br> <br> <br>**Difference**|**Constant**<br>**Time between**<br>**Arrivals**|<br> <br>**Random**<br>**Time**<br>**between**<br>**Arrivals**|<br> <br> <br>**Difference**|
|1|<br>9|52|<br>43|1|<br>44|<br>43|
|2|<br>9|65|56|1|<br>58|57|
|3|<br>9|89|80|1|<br>81|<br>80|
|4|<br>9|51|<br>42|<br>1|<br>43|42|
|5|<br>9|30|21|<br>1|<br>22|<br>21|
|6|<br>9|37|<br>28|1|<br>29|28|
|7|<br>9|75|66|1|<br>67|<br>66|
|8|<br>9|39|30|1|<br>31|<br>30|
|9|<br>9|31|<br>22|<br>1|<br>23|22|
|10|<br>9|47|<br>38|1|<br>39|38|
|11|<br>9|51|<br>42|<br>1|<br>44|<br>43|
|12|<br>9|62|<br>53|1|<br>54|<br>53|
|13|<br>9|72|<br>63|1|<br>64|<br>63|
|14|<br>9|48|39|1|<br>40|39|
|15|<br>9|22|<br>13|1|<br>14|<br>13|
|16|<br>9|37|<br>28|1|<br>29|28|
|17|<br>9|31|<br>22|<br>1|<br>23|22|
|18|<br>9|25|16|1|<br>17|<br>16|
|19|<br>9|79|70|1|<br>71|<br>70|
|20|<br>9|31|<br>22|<br>1|<br>23|22|
|**Average **|9|48.7|<br>39.7|<br>1|<br>40.8|39.8|
|**Std. Dev.**|0|19.4|<br>19.4|<br>0|19.5|19.5|
|**99% CI**<br>**Lower**<br>**Bound**|9|36.3|27.3|1|<br>28.3|27.3|
|**99% CI**<br>**Upper**<br>**Bound**|9|61.1|<br>52.1|<br>1|<br>53.3|52.3|



Table 11-5 contains a portion of the trace for worker 1 for one replicate of the constant time between arrivals case.  The trace shows the actions the worker takes from processing a part at RM to processing the next part at RM.  The time between starting the processing of a part at RM and return was 52.06 seconds, only slightly less than the expected time of 55.2 seconds.  Thus, there is some evidence that the worker can perform all assigned tasks in less than the takt time. The trace shows that worker performs all assigned tasks in the required sequence.  Thus, model and system design validation evidence is obtained. 

11 **-** 13 

**Table 11-5:  Worker 1 Action Trace** 

|**Simulation Time**|**Worker **|**Workstation **|**Action **|
|---|---|---|---|
|55.20|Worker1|RM|Start|
|59.20|Worker1|RM|End|
|62.64|Worker1|M1|Arrive|
|62.64|Worker1|M1|Unload Start|
|65.64|Worker1|M1|Unload End|
|65.64|Worker1|M1|Initialize Start|
|69.64|Worker1|M1|Initialize End|
|73.46|Worker1|M2|Arrive|
|73.46|Worker1|M2|Unload Start|
|77.46|Worker1|M2|Unload End|
|77.46|Worker1|M2|Initialize Start|
|82.46|Worker1|M2|Initialize End|
|85.98|Worker1|M6|Arrive|
|89.86|Worker1|M7|Arrive|
|89.86|Worker1|M7|Unload Start|
|92.86|Worker1|M7|Unload End|
|92.86|Worker1|M7|Initialize Start|
|97.86|Worker1|M7|Initialize End|
|103.13|Worker1|FG|Arrive|
|108.13|Worker1|FG|End|
|110.26|Worker1|RM|Arrive|
|110.40|Worker1|RM|Start|



The same results for the case where three workers are used are shown in Table 11-6 along with a comparison to the two workers case.  For the random time between arrivals case, the average maximum WIP in the cell is 32.0 when three workers are used.  This is notably less than the average when two workers are used: 48.7.  Similarly, the average maximum WIP at RM is less when three workers are used: 22.0 versus 40.8.  The reductions in WIP in the cell and at station RM due to using three workers instead of two are statistically significant at an approximate 99% confidence level.  The approximate 99% confidence intervals of the difference do not contain zero. 

11 **-** 14 

**Table 11-6:  Work in Process in the Cell and in RM – Three Workers Case with Comparison to the Two Workers Case for Random Times Between Arrivals** 

||**Maximum WIP in Cell**|**Maximum WIP in Cell**|**Maximum WIP in Cell**|**Maximum WIP at RM**|**Maximum WIP at RM**|**Maximum WIP at RM**|
|---|---|---|---|---|---|---|
|**Replicate**|**Two**<br>**Workers**|<br>**Three**<br>**Workers**|<br>**Difference**|**Two**<br>**Workers**|<br>**Three**<br>**Workers**|<br>**Difference**|
|1|<br>52|<br>37|<br>15|44|<br>27|<br>17|
|2|<br>65|32|<br>33|58|22|<br>36|
|3|<br>89|49|40|81|<br>39|42|
|4|<br>51|<br>31|<br>20|43|21|<br>22|
|5|<br>30|24|<br>6|22|<br>14|<br>8|
|6|<br>37|<br>35|2|<br>29|25|4|
|7|<br>75|48|27|<br>67|<br>38|29|
|8|<br>39|28|11|<br>31|<br>18|13|
|9|<br>31|<br>24|<br>7|<br>23|14|<br>9|
|10|<br>47|<br>25|22|<br>39|15|24|
|11|<br>51|<br>28|23|44|<br>18|26|
|12|<br>62|<br>37|<br>25|54|<br>27|<br>27|
|13|<br>72|<br>38|34|<br>64|<br>28|36|
|14|<br>48|32|<br>16|40|22|<br>18|
|15|<br>22|<br>22|<br>0|14|<br>12|<br>2|
|16|<br>37|<br>31|<br>6|29|21|<br>8|
|17|<br>31|<br>26|5|23|16|7|
|18|<br>25|25|0|17|<br>15|2|
|19|<br>79|39|40|71|<br>29|42|
|20|<br>31|<br>28|3|23|18|5|
|**Average **|48.7|<br>32.0|16.8|40.8|22.0|18.9|
|**Std. Dev.**|19.4|<br>7.6|13.3|19.5|7.6|13.4|
|**99% CI**<br>**Lower**<br>**Bound**|36.3|27.1|<br>8.2|<br>28.3|17.1|<br>10.3|
|**99% CI**<br>**Upper**<br>**Bound**|61.1|<br>36.8|25.3|53.3|26.8|27.4|
|11.3.4|Review and Extend Previous Work||||||



Management was pleased with the results of the simulation experiments.  The cell appears to work as designed using standard cellular manufacturing calculations when the time between arrivals is constant. 

Exponentially distributed times between arrivals result in large maximum WIP levels. Controls placed on cell operations, in particular requiring a worker to wait at RM for a part, resulted in the all of the excess WIP residing in the RM.  Thus, the cell appears to be capable of operating effectively even in the presence of random variation in part arrival. 

## 11.3.5 Implement the Selected Solution and Evaluate 

It was decided to implement the cell with two workers.  If the high utilization of the two workers constrained the actual operation of the cell, a third worker could be added. 

11 **-** 15 

## _11.4 Summary_ 

Manufacturing work cells can be designed using standard calculations.  Simulation can be used to validate that the designed cell will operate as intended, in part using a trace of worker actions. The effect of random behavior, such as random times between arrivals and random walking times, can be assessed.  WIP levels can be estimated.  The use of alternative numbers of workers can be evaluated. 

## **Problems** 

1. Compare the cellular manufacturing organization presented in this chapter with the serial line discussed in chapter 7. 

2. Write down the task sequence for Worker 2 for worker assignment A. 

3. Model using pseudo – code part of the process for Worker 2 from picking up a part at workstation M2 through arriving at workstation M4, for worker assignment A. 

4. For the case of two workers and random time between arrivals, estimate the average cycle time for a part to traverse the cell using Little’s Law.  The cycle time is the time between entering the raw material inventory and entering the FGI.  Suppose the average WIP in the cell is 30.8 with a 95% confidence interval for the mean: (22.6, 38.9). 

5. Does the work cell behave like a CONWIP system?  Why or why not? 

6. An extremely long time between arrivals, say triple the mean, is possible when using the exponential distribution to model this quantity.  What is the potential effect of such long times between arrivals on the capacity of the cell? 

7. Consider the probability distribution of the time worker two takes to complete all tasks once. Assume walking times are normally distributed with same mean and variance as the triangularly distributed times.  The mean and variance of a triangular distribution are computed as follows: 

Mean: 

Variance: 

**==> picture [265 x 64] intentionally omitted <==**

**----- Start of picture text -----**<br>
min  mode  max<br>3<br>min 2  mode 2  max 2  min * mode  min * max  mode * max<br>18<br>**----- End of picture text -----**<br>


   - a. The time for worker two to complete all tasks once is normally distributed. Compute the mean and standard deviation of this distribution.  Assume that the minimum is 75% of the mean and the maximum is 125% of the mean as stated on page 11-5.  Thus, the distribution is symmetric implying mean = mode. 

   - b. What is the probability that the time to complete all tasks once is greater than the takt time? 

8. Perform a gross capacity analysis for each station in the cell.  This means computing the maximum number of parts each station can produce in one work day. 

11 **-** 16 

9. Print out a trace of the events effecting worker 2 in task assignment A.  Does this provide validation evidence? 

10. Add an additional performance measure to the model:  The percent of times a worker traverses an assigned route in more than the takt time.  Rerun the model to estimate this performance measure. 

11. Model the time between arrivals as gamma distributed with mean 55.2 seconds and standard deviation 27.6 seconds.  Compare the maximum WIP in the cell to the values in Table 11-4. 

## **Case Problem[2]** 

An injector is produced in two steps:  assembly and calibration.  This study will focus on the calibration area only.  The assembly area can produce a batch of 24 parts in 82 minutes.  Each batch is placed on a WIP cart.  A batch is only produced if a WIP cart is available.  Injectors must be cured for 24 hours after assembly before they can enter the calibration area. 

To control work in process, the number of WIP carts is limited to the fewest number need to avoid constraining throughput. Only one WIP cart can be in the calibration area at a time. 

The calibration area consists of four workstations that can be labeled W1, W2, W3, and W4. Each workstation processes one injector at a time.  A worker is not needed for automated operations and thus is free to due other tasks. 

At workstation W1, the worker initiates the injector in 25 seconds.  The workstation performs an automated test in 10 seconds.  Finally, the worker removes the part in 5 seconds.  A manual operation is performed at workstation W2.  The operation time is triangularly distributed with minimum 4.0 minutes, mode 5.0 minutes, and maximum 7.8 minutes.  At workstation W3, the worker initiates the part in 5 seconds.  An automated operation is performed in 4.1 minutes.  The worker removes the part in 2 seconds.  Workstation W4 is a packing operation performed by the worker in 5 seconds. 

The calibration area is served by one worker.  Worker walking times between stations are as follows: 

|**Station **|**W1**|**W2**|**W3**|**W4**|
|---|---|---|---|---|
|**W1**|0|3|7|10|
|**W2**||0|4|7|
|**W3**|||0|3|
|**W4**||||0|



Determine the number of WIP carts required.    Generate a trace of worker tasks to validate the model. 

Case Problem Issues 

1. How should the WIP carts be modeled? 

2. How should the constraint on the number of WIP carts in the calibration area be modeled? 

3. How should the injector curing requirement be modeled? 

2  This application problem is derived from the capstone masters degree project performed by Carrie Grimard. 

11 **-** 17 

4. Write down the sequence of tasks for the calibration area worker. 

5. Discuss how the number of WIP carts can effect cycle time. 

6. Beside throughput, are any other performance measures important?  If so, what are they? 

7. An entity moving through the assembly area represents a WIP cart while an entity moving through the calibration area represents an individual injector.  How is the conversion from WIP cart to injector accomplished? 

8. Specify the experimental strategy for determining the number of WIP carts. 

9. Discuss how to obtain verification and validation evidence. 

10. Determine how to model arrivals to the assembly process. 

11. Determine how to model batch processing times in the assembly area.  Note that the batch processing times are the sum of 24 individual processing time.  Should this sum be explicitly computed?  Can the central limit theorem be applied? 

12. Compute the expected number of WIP carts needed to maximize throughput. 

13. What are the initial conditions for the experiment? 

Terminating Experiment: The simulation time interval is 5 days (120 hours of work time). 

11 **-** 18
