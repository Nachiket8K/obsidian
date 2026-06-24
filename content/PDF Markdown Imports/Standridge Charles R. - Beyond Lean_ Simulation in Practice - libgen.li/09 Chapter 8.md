---
title: "Chapter 8"
book: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li"
source_pdf: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li.pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 8** 

## **Job Shops** 

## _8.1 Introduction_ 

In this chapter, we consider another possible configuration of workstations called a job shop.  A serial system processes one or at most a few types of parts that visit all of the system's workstations in sequence.  Thus, serial systems are organized around required production operations.  A job shop serves a wide variety of parts or jobs.  Each type of job may use a different subset of the workstations and visit those stations in a unique sequence.  Taken all together, the movement of jobs of all types between workstations appears to be random. Workstations are designed around common operations.  For example, all of the milling machines may be gathered together at one workstation. 

Several unique aspects of job shops must be taken into account.  When a part using a machine is of a different type than its predecessor, the machine may require a setup task to change its operating parameter values or tooling.  Different jobs may require significantly different amounts of processing time at a workstation.  The routing of each type of job through the shop must be specified. 

## _8.2 Points Made in the Case Study_ 

This case study illustrates principle 2 of chapter 1.  Modeler defined performance measures are extracted from standard simulation results to help assess system behavior.  In this case, the performance measure of interest is the service level to customers, the percent of jobs completed on time.  The shop has defined on time as a lead time of 8 hours or less. 

This case study illustrates how analytic computations, such as those defined in principle 11 of chapter 1, can be used to set simulation experiment parameter values.  The average number of busy machines of each type is determined using Little’s law.  Cycle time is a function of machine utilization, as seen in the VUT equation.  Thus, increasing the number of machines of each type would lower utilization and reduce cycle time.  Therefore additional machines may be necessary to achieve an acceptable service level. 

The experimental design is sequential.  The results of initial simulations are used to set the parameter values for subsequent simulations.  Additional machines are added at the bottleneck station identified by initial simulations.  Subsequent simulations are run to assess the effect on the service level of the additional machines. 

The model adapts to the information that is available about the shop in accordance with principle 2 of chapter 1.  Jobs are classified into three types with the arrival rate and distribution known for each type only.  Each job within a type will be modeled as having the same route through the shop.  Processing times are known only by station, independent of job type.  Thus, processing times are modeled as random variables with a large variance. 

Simulation results illustrate how relieving one bottleneck in a system can create and expose other bottlenecks in the system.  As the number of machines of one type is increased, another type of machine becomes the bottleneck. 

The job shop model includes several components.  The arrival process for each of the three job types is modeled in the same manor.  The operation process for each workstation is modeled in the same way.  Routing of jobs is included. 

8-1 

## _8.3 The Case Study_ 

This case study deals with determining the number of machines needed at each workstation to meet a particular level of demand with a satisfactory service level.  The average number of busy machines can be determines using Little’s law.  However, due to waiting time for busy machines, lead time may exceed management’s target.  In other words, the service level is too low. Additional machines at a station reduce utilization and thus reduce lead time. 

## 8.3.1 Define the Issues and Solution Objective 

A job shop consists of four workstations each having one kind of machine: lathe, planer, shaper, and polisher as shown in Figure 8-1.  There is one route through the job shop for each of the three job types.  Machines may be either in a busy or idle state. 

Management desires that each job spends less than 8 hours in the shop.  The service level is the percent of jobs that meet this target.  The objective is to find the minimum number of machines, and thus capital equipment cost, that allows the shop to reach a high, but yet unspecified service level.  Management reviews shop performance each month. 

The shop processes three types of jobs that have the following routes through the shop: 

Type 1: lathe, shaper, polisher Type 2: planer, polisher Type 3: planer, shaper, lathe, polisher 

8-2 

Each type of job has its own arrival process, that is its own distribution of time between arrivals. Job processing time data was not available by job type.  Thus, a single distribution is used to model operation time at a station.  Setup issues can be ignored for now. 

Relevant data are as follows.  The time between arrivals for each job type is exponentially distributed.  The mean time between arrivals for job type 1 is 2.0 hours, for type 2 jobs 2.0 hours, and for type 3 jobs 0.95 hours.  Processing times are triangularly distributed with the following parameters (minimum, mode, maximum), given in hours. 

|Planer:|(1.0,|1.2,|2.4)|
|---|---|---|---|
|Shaper:|(0.75,|1.0,|2.0)|
|Lathe:|(0.40,|0.80,|1.25)|
|Polisher:|(0.5,|0.75,|1.5)|



## 8.3.2 Build Models 

The model of the job shop uses the following logic: 

1. A job arrives as modeled in the arrival process. 

2. The job is routed according to the routing process. A. If the job needs more operations, it is sent to the station corresponding to its next operation. 

   - B. If the job has completed all operations, its lead time is computed and the service level for this job recorded. Then the job leaves the shop.  Note that the service level is either 100 for acceptable (less than 8 hours) or 0 for not acceptable (greater than 8 hours). 

3. The job is processed at the selected workstation as modeled by an operation process. 4. The job returns to step 2. 

Job routing corresponds to the routing matrix shown in Figure 8-2, with Depart indicating that the end of the route has been reached. 

|**Job Type**|**First Operation**|**Second**<br>**Operation **|**Third**<br>**Operation **|**Fourth**<br>**Operation **|**Last**|
|---|---|---|---|---|---|
|1|Lathe|Shaper|Polisher|Depart||
|2|Planer|Polisher|Depart|||
|3|Planer|Shaper|Lathe|Polisher|Depart|



**Figure 8-2. Job Shop Routing Matrix.** 

Enitities represent jobs and have the following attributes: JobType = type of job ArriveTime = simulation time of arrival Location = location of a job relative to the start of its route: 1st..4th OpTimei = operation time at the ith station on the route of a job: i = 1..4 Routei = station at the ith location on the route of a job ArriveStation = time of arrival to a station, used in computing the waiting time at a station 

There is an arrival process for each job type.  The arrival processes for the job types are similar. All of the attributes are assigned including each operation time.  The operation time is assigned to assure that the ith arriving job (entity) will be assigned the ith sample from each random number stream for each alternative tested.  This is the best implementation of the common random numbers method discussed in chapter 4.  The values assigned to the Route attribute are the names of the stations that comprise the route in the order visited.  The last station is called Depart to indicate that the entity has completed processing.  Whatever performance measure 

8-3 

observations are needed are made in the Depart process.  At the end of the arrival process, the entity is sent to the routing process. 

The routing process is as follows.  The Location relative to the start of the route is incremented by 1.  The entity is sent to the process whose name is given by RouteLocation.  The routing process requires zero simulation time. 

The process as each station is like that of the single workstation discussed in chapter 6.  An arriving entity waits for the planer resource.  The operation is performed and the resource is made idle.  The entity is sent to the routing process. 

Upon departure from the shop (Process Depart), the lead time is computed.  Thus, the service level can be computed and collected. 

The pseudo-English form of the model including the arrival process for type 1 jobs, the operation process for the planer, the routing process and the depart process follows. 

|Define Arrivals:|||
|---|---|---|
|Type1|||
|Time|of first arrival:<br>0||
|Time|between arrivals: Exponentially distributed|with a mean of 2 hours|
||Number of arrivals:|Infinite|
|Type2|||
|Time|of first arrival:<br>0||
|Time|between arrivals: Exponentially distributed|with a mean of 2 hours|
||Number of arrivals:|Infinite|
|Type3|||
|Time|of first arrival:<br>0||
|Time|between arrivals: Exponentially distributed|with a mean of 0.95 hours|
||Number of arrivals:|Infinite|
|Define Resources:|||
|Lathe/?|with states (Busy, Idle)||
|Planer/?|with states (Busy, Idle)||
|Polisher/?|with states (Busy, Idle)||
|Shaper/?|with states (Busy, Idle)||



8-4 

Define Entity Attributes: ArrivalTime // part tagged with its arrival time; each part has its own tag JobType // type of job Location // location of a job relative to the start of its route: 1..4 OpTime(4) // operation time at the ith station on the route of a job Route(5) // station at the ith location on the route of a job ArriveStation // time of arrival to a station, used in computing the waiting time Process ArriveType1 Begin Set ArrivalTime = Clock // record time job arrives on tag Set Location     = 0 // job at start of route Set JobType    = 1 // Set route and processing times Set Route(1) to Lathe Set OpTime(1) to triangular 0.40, 0.80, 1.25 hr Set Route(2) to Shaper Set OpTime(2) to triangular 0.75, 1.00, 2.00 hr Set Route(3) to Polisher Set OpTime(3) to triangular 0.50, 0.75, 1.50 hr Set Route(4) to End Send to P_Route End Process Planer Begin Set ArriveStation = Clock // record time job arrives at station Wait until Planer/1 is Idle in Queue QPlaner // job waits for its turn on the machine Make Planer/1 Busy // job starts on machine; machine is busy Tabulate (Clock-ArriveStation) in WaitTimePlaner// keep track of job waiting time Wait for OpTime(Location) hours // job is processed Make Planer/1 Idle // job is finished; machine is idle Send to P_Route End Process Route Begin Location++ // Increment location on route Send to Route(Location) // Send to next station or depart End Process Depart Begin //Lead time in hours by job type and for all job types if type = Job1 then tabulate (Clock-ArrivalTime) in LeadTime(1) if type = Job2 then tabulate (Clock-ArrivalTime) in LeadTime(2) if type = Job3 then tabulate (Clock-ArrivalTime) in LeadTime(3) tabulate ((Clock-ArrivalTime) in LeadTimeAll if ((Clock-ArrivalTime) <= 8 tabulate 100 in Service // Service level recorded else tabulate 0 in Service End 

8-5 

## 8.3.3 Identify Root Causes and Assess Initial Alternatives 

Management reviews the system monthly.  Thus, a terminating experiment with an ending time of one month was chosen.  Furthermore, management is interested in the percent of jobs that spend less than 8 hours in the shop, the service level, as well as job waiting time at each station.  These quantities are the performance measures of interest. 

There are seven random number streams, one for the arrival process for each of three types of jobs and one for each of four operation times.   Twenty replicates will be made.  The initial conditions reflect a typical state of the shop:  two jobs of each type at each station. 

The model parameters are the number of machines at each station.  The expected number of busy machines at each station will be used as the parameter value for the first simulation. Management is able to provide more machines at workstations where the maximum waiting time is excessive in order to meet the service level target. 

Table 8-1 summarizes the simulation experiment. 

**Table 8-1:  Simulation Experiment Design for the Job Shop** 

|**Element of the Experiment**|**Values for This Experiment**|
|---|---|
|Type of Experiment|Terminating|
|Model Parameters and Their Values|Number of machines at each station:<br>1.  Average number busy as shown in Table 8-2<br>following|
|Performance Measures|1.  Percent of jobs whose cycle time is less than 8<br>hours (Service Level)<br>2.  Waiting time at eachstation|
|Random Number Streams|1.  Time between arrivals - job type 1<br>2.  Time between arrivals - job type 2<br>3.  Time between arrivals - job type 3<br>4.  Operation time station 1<br>5.  Operation time station 2<br>6.  Operation time station 3<br>7.Operationtime station 4|
|Initial Conditions|2 parts of each type that can be at a station in the<br>bufferofeachstation|
|Numberof Replicates|20|
|Simulation EndTime|184 hours (onemonth)|



The expected number of machines needed by each part type at each station is computed as shown in Table 8-2. 

1. The mean service time is the mean of the triangular distribution of the service time at each station.  This quantity is the arithmetic average of the minimum, mode, and maximum. 

2. The expected number of machines is the quotient of the mean operation time divided by the mean time between arrivals (Little’s Law). 

3. The total expected number of machines at a station is the sum over the three part types. This value is rounded to the next higher whole number to yield the number of machines at each station. 

4. Raw processing time is the sum of the mean processing times at each station on the route of a job. 

8-6 

**Table 8-2:  Expected Number of Machines Needed at Each Workstation** 

||**Planer**|**Shaper**|**Lathe**|**Polisher**|**Raw**<br>**Processing**<br>**Time**|
|---|---|---|---|---|---|
|Job Type 1||||||
|Mean Time Between<br>Arrivals<br>(TBA = 1/TH)||2|2|2||
|Mean Operation<br>Time (CT)||1.25|0.82|0.92|2.99|
|Expected Number of<br>Machines<br>(= CT / TBA)||0.63|0.41|0.46||
|Job Type 2||||||
|Mean Time Between<br>Arrivals (TBA)|2|||2||
|Mean Operation<br>Time (CT)|1.53|||0.92|2.45|
|Expected Number of<br>Machines<br>(= CT / TBA)|0.77|||0.46||
|Job Type 3||||||
|Mean Time Between<br>Arrivals (TBA)|0.95|0.95|0.95|0.95||
|Mean Operation<br>Time (CT)|1.53|1.25|0.82|0.92|4.52|
|Expected Number of<br>Machines<br>(= ST / TBA)|1.61|1.32|0.86|0.97||
|||||||
|Total Expected<br>Number of Machines|2.38|1.94|1.27|1.89||
|Number of Machines<br>to Use|3|2|2|2||



The mean raw processing time for the job types are 1.45 hours, 2.99 hours, and 4.52 hours. Thus, a cycle time in the shop criteria of one day (8 hours) represents approximate 2 to 5 times the raw processing time which seems reasonable. 

Table 8-3 gives the service level for the shop and the maximum waiting time at each station. Notice that the service level is highly variable, ranging from 19.8% to 97.3%.  Maximum waiting times are much larger for the shaper than any of the other three machines.  The maximum waiting times at the polisher and the planer are also long. 

8-7 

**Table 8-3:  Simulation Results - Expected Number of Machines Case.** 

|**Replicate**|**Service**<br>**Level**|<br> <br>**Maximum**<br>**Waiting Time**<br>**at the Lathe**<br>**(Hours)**|<br> <br> <br>**Maximum**<br>**Waiting Time**<br>**at the Planer**<br>**(Hours)**|<br> <br> <br>**Maximum**<br>**Waiting Time**<br>**at the Polisher**<br>**(Hours)**|<br> <br> <br>**Maximum**<br>**Waiting Time**<br>**at the Shaper**<br>**(Hours)**|
|---|---|---|---|---|---|
|1|<br>21.2|<br>1.1|<br>4.4|<br>4.6|23.0|
|2|<br>42.7|<br>1.6|3.3|4.0|10.7|
|3|<br>22.8|1.2|<br>8.6|9.8|17.1|
|4|<br>40.1|<br>1.4|<br>5.1|<br>3.4|<br>11.2|
|5|<br>97.3|1.0|2.6|3.4|<br>2.8|
|6|<br>73.4|<br>0.8|5.0|4.4|<br>4.4|
|7|<br>62.4|<br>2.2|<br>2.9|2.8|13.9|
|8|<br>74.0|1.5|3.9|4.0|9.1|
|9|<br>24.7|<br>2.2|<br>4.1|<br>4.9|14.0|
|10|<br>37.6|1.3|4.8|3.3|13.0|
|11|<br>57.8|1.5|3.6|3.4|<br>7.8|
|12|<br>19.8|1.1|<br>8.8|9.2|<br>13.3|
|13|<br>38.0|1.1|<br>7.0|3.7|<br>10.0|
|14|<br>70.8|1.0|3.1|<br>4.2|<br>9.0|
|15|<br>36.9|1.1|<br>4.1|<br>6.5|11.5|
|16|<br>76.2|<br>1.1|<br>3.1|<br>3.5|8.3|
|17|<br>59.3|1.0|3.0|6.0|7.9|
|18|<br>60.6|1.5|5.3|4.5|6.3|
|19|<br>31.1|<br>1.4|<br>3.8|9.1|<br>7.0|
|20|<br>24.4|<br>1.1|<br>5.3|4.5|16.8|
|**Average **|48.6|1.3|4.6|5.0|10.9|
|**Std. Dev.**|22.5|0.4|<br>1.8|2.1|<br>4.7|
|**99% CI Lower Bound**|34.2|<br>0.1|<br>0.4|<br>0.5|1.1|
|**99% CI Upper Bound**|62.9|2.9|2.9|2.9|2.9|



## 8.3.4 Review and Extend Previous Work 

System experts reviewed the results developed in the previous section.  The average service level of 48.6% was thought to be too low.  A service level of at least 95% is needed.  A machine will be added to the the shaper station to reduce the maximum waiting time.  Additional machines will be added one at a time to the station with the greatest maximum waiting time until the 95% service level is achieved. 

## _8.4 The Case Study with Additional Machines_ 

The need to add one or more machines causes a re-start of the simulation process at the third step, Identify Root Causes and Assess Initial Alternatives. 

## 8.4.1 Identify Root Causes and Assess Initial Alternatives 

The simulation experiment uses the same design as in Table 8-1.  However, the number of machines at the shaper station is increased by one.  Table 8-4 shows the results.  The average service level of 56.4% is less than the required 95%.  The maximum waiting time at the polisher is much higher than at any of the other stations.  Thus, an additional polisher will be added. 

8-8 

**Table 8-4:  Simulation Results –Additional Shaper Case** 

|**Replicate**|**Service**<br>**Level**|<br> <br>**Maximum**<br>**Waiting Time**<br>**at the Lathe**<br>**(Hours)**|<br> <br> <br>**Maximum**<br>**Waiting Time**<br>**at the Planer**<br>**(Hours)**|<br> <br> <br>**Maximum**<br>**Waiting Time**<br>**at the Polisher**<br>**(Hours)**|<br> <br> <br>**Maximum**<br>**Waiting Time**<br>**at the Shaper**<br>**(Hours)**|
|---|---|---|---|---|---|
|1|<br>17.6|1.9|4.4|<br>10.2|<br>1.5|
|2|<br>65.6|1.7|<br>3.3|7.3|1.4|
|3|<br>22.1|<br>1.9|8.6|20.3|1.2|
|4|<br>56.7|<br>1.1|<br>5.1|<br>7.5|1.3|
|5|<br>98.0|1.2|<br>2.6|3.8|1.0|
|6|<br>81.1|<br>1.2|<br>5.0|5.1|<br>1.1|
|7|<br>72.1|<br>1.7|<br>2.9|6.7|<br>1.9|
|8|<br>76.7|<br>1.9|3.9|7.2|<br>1.2|
|9|<br>1.3|1.3|4.1|<br>13.6|1.4|
|10|<br>39.1|<br>1.2|<br>4.8|8.6|1.8|
|11|<br>78.6|1.7|<br>3.6|5.9|1.1|
|12|<br>47.5|1.1|<br>8.8|7.7|<br>1.1|
|13|<br>61.7|<br>1.3|7.0|7.0|1.9|
|14|<br>78.4|<br>1.3|3.1|<br>5.9|1.8|
|15|<br>43.8|1.5|4.1|<br>12.3|2.0|
|16|<br>83.2|<br>1.6|3.1|<br>6.7|<br>1.6|
|17|<br>81.7|<br>1.7|<br>3.0|7.0|1.2|
|18|<br>67.6|2.0|5.3|7.8|1.4|
|19|<br>43.5|1.4|<br>3.8|10.5|1.6|
|20|<br>12.1|<br>1.6|5.3|13.8|1.8|
|**Average **|56.4|<br>1.5|4.6|8.7|<br>1.5|
|**Std. Dev.**|27.1|<br>0.3|1.8|3.8|0.3|
|**99% CI Lower Bound**|39.1|<br>1.3|3.5|6.3|1.3|
|**99% CI Upper Bound**|73.8|1.7|<br>5.7|<br>11.2|<br>1.7|



The simulation results for the case of an additional polisher and shaper are shown in Table 8-5. The average service level, 95.1%, now exceeds 95%.  The approximate 99% confidence interval for the service level is 91.1% to 99.2%.  Thus with approximately 99% confidence, it can be concluded that the true service level is in a range that includes 95%. 

In two of the replicates the service level was less than 80%.  In these replicates, the maximum waiting time at the planer exceeded 8 hours.  In addition, the average maximum waiting time at the planer was 4.6 hours. 

8-9 

**Table 8-5:  Simulation Results –Additional Shaper and Polisher Case** 

|**Replicate**|**Service**<br>**Level**|<br> <br>**Maximum**<br>**Waiting Time**<br>**at the Lathe**<br>**(Hours)**|<br> <br> <br>**Maximum**<br>**Waiting Time**<br>**at the Planer**<br>**(Hours)**|<br> <br> <br>**Maximum**<br>**Waiting Time**<br>**at the Polisher**<br>**(Hours)**|<br> <br> <br>**Maximum**<br>**Waiting Time**<br>**at the Shaper**<br>**(Hours)**|
|---|---|---|---|---|---|
|1|<br>95.6|1.9|4.4|<br>2.0|1.5|
|2|<br>98.9|1.7|<br>3.3|1.5|1.4|
|3|<br>79.4|<br>1.9|8.6|1.4|<br>1.2|
|4|<br>96.0|1.1|<br>5.1|<br>1.3|1.3|
|5|<br>99.0|1.2|<br>2.6|1.7|<br>1.0|
|6|<br>96.6|1.2|<br>5.0|1.5|1.1|
|7|<br>99.2|<br>1.7|<br>2.9|1.5|1.9|
|8|<br>97.5|1.9|3.9|1.4|<br>1.2|
|9|<br>96.3|1.3|4.1|<br>1.8|1.4|
|10|<br>94.5|1.2|<br>4.8|1.6|1.8|
|11|<br>98.7|<br>1.7|<br>3.6|1.3|1.1|
|12|<br>76.5|1.1|<br>8.8|1.6|1.1|
|13|<br>92.0|1.3|7.0|1.6|1.9|
|14|<br>99.2|<br>1.3|3.1|<br>2.0|1.8|
|15|<br>98.4|<br>1.5|4.1|<br>1.6|2.0|
|16|<br>99.2|<br>1.6|3.1|<br>1.7|<br>1.6|
|17|<br>99.4|<br>1.7|<br>3.0|1.4|<br>1.2|
|18|<br>93.5|2.0|5.3|1.9|1.4|
|19|<br>99.2|<br>1.4|<br>3.8|1.4|<br>1.6|
|20|<br>93.9|1.6|5.3|1.3|1.8|
|**Average **|95.1|<br>1.5|4.6|1.6|1.5|
|**Std. Dev.**|6.3|0.3|1.8|0.2|<br>0.3|
|**99% CI Lower Bound**|91.1|<br>1.3|3.5|1.4|<br>1.3|
|**99% CI Upper Bound**|99.2|<br>1.7|<br>5.7|<br>1.7|<br>1.7|



8.4.2 Review and Extend Previous Work 

Management was pleased that the addition of two machines was sufficient to meet the service level requirement.  It was decided that the job shop would have the following configuration of machines: 

|Lathes|--|2|
|---|---|---|
|Planers|--|3|
|Polishers|--|3|
|Shapers|--|3|



In addition, the congestion, in terms of work in process, at the planer station would be monitored. Action would be taken to help avoid excessive waiting time at this station, which now appears to be the bottleneck. 

## 8.4.3 Implement the Selected Solution and Evaluate 

The job shop was implemented with the number of machines decided upon at the management review meeting.  A monitoring system for work in process at the planer station was put in place. 

8-10 

## _8.5 Summary_ 

Modeling the flow of multiple job types in a job shop has been presented.  Each type of job has a unique route through the workstations. 

Simulation experiments are used to set the number of machines at each workstation in order to meet a service level criteria.  Little’s law is applied to determine the average number of busy machines at each station.  These values are used as the initial number of machines at each station in the simulation.  After each experiment, the bottleneck station is identified.  The next experiment involves increasing the number of machines at this station by one.  The series of experiments ends when the service level criteria is met. 

Simulation results show how the bottleneck station changes as the result of adding capital equipment. 

## **Problems** 

1. Based on the simulation experiment results that follow for a job shop similar to the one discussed in this chapter, give verification evidence. Arrivals: 

Type 1 --  581 Type 2 --  373 Type 3 --  482 Number completing operations Lathe -- 1063 Shaper -- 1065 Polisher -- 1426 Planer --   859 Number waiting for operations at the end of the simulation Lathe --      0 Shaper --      0 Polisher --      5 Planer --      0 State of resource at the end of the simulation Lathe --  2 busy Shaper --  6 busy Polisher --  8 busy Planer --  7 busy Total number of jobs completed --1426 

2. Suppose the situation in the job shop is changed as follows.  The time between arrivals jobs is 0.25 hours.  Two thirds of the jobs are of job type 1 and one-third are of job type 3. Develop an analytic estimate of the required number of each type of machine. 

3. Develop a process model of the following small job shop.  The shop processes two types of jobs in equal numbers.  The time between job arrival is exponentially distributed with a mean of 3 hours.  The first type of job visits stations 1 and 2.  The second type of job visits stations 2, 1, and 3.  Processing times are constant and as follows: 

|JobType|First Station Time|Second Station Time|Third Station Time|
|---|---|---|---|
|1|2.0|1.2||
|2|0.8|1.7|2.6|



4. Model the serial line discussed in the application study of Chapter 7 using the job shop model developed in this chapter. 

8-11 

5. List systems with job shop organizations that you deal with in the course of your everyday life.  Develop a single list for the entire class. 

6. Provide validation evidence based on the outputs presented in this chapter. 

7. Add an additional planer as well as a shaper and a polisher to the job shop in the case study in this chaper.  Is the improvement due to the additional shaper worthwhile? 

8. The lower limit of the approximate 99% confidence interval for the service level in Table 8-5 is less than the required average service level of 99%.  As an alternative, estimate and interpret the approximate 90% confidence interval. 

9. Re-run the simulation experiment with the following performance measure added:  lead time for entities who lead time exceed the service level target cycle time.  Interpret your results. 

## **Case Problem** 

Management wishes to move the job shop toward a lean system in which there would be three workcells, one for each job type.  Due to current budget constraints, no more machines than were found necessary in the case study above can be used, a total of 11.  As a first step toward lean in the short term, the following options are to be evaluated with respect to service level and total number of machines. 

1. A serial line to produce type 3 jobs and smaller job shop to produce type 1 and 2 jobs with 10 total machines. 

2. A serial line to produce type 3 jobs and smaller job shop to produce type 1 and 2 jobs with 11 total machines. 

3. Three serial lines, one for each type of job, with 11 total machines. 

Build the simulation models and conduct the simulation experiments to evaluate the above options. 

Case Problem Issues 

1. Suppose each type of job is run on its own dedicated serial line (#3 above).  How many machines of each kind are needed for each type of job? 

2. Can this analysis be done using the model developed in this chapter?  If so, tell how. 

3. For item 1 above, how would the 10 total machines be allocated by machine type and location (serial line for jobs of type 3 and job shop for jobs of type 1 and 2)? 

4. For item 2 above, how would the 11 total machines be allocated by machine type and location (serial line for jobs of type 3 and job shop for jobs of type 1 and 2)? 

8-12 

## **Part III** 

## **Lean and Beyond Manufacturing** 

The application studies in part three illustrate sophisticated strategies for operating systems, typically manufacturing systems, to effectively meet customer requirements in a timely fashion while concurrently meeting operations requirements such as keeping inventory levels low and utilization of equipment and workers high.  These strategies incorporate both lean techniques as well as beyond lean modeling and analysis. 

Before presenting the application studies in chapters 10, 11, and 12, inventory control and organization strategies are presented in chapter 9.  These include both traditional and lean strategies. 

Chapter 10 deals with flowing the product at the pull of the customer as implemented in the pull approach. How to concurrently model the flow of both products and information is discussed.  Establishing inventory levels as a part of controlling pull manufacturing operations is illustrated. 

Chapter 11 discusses the cellular manufacturing approach to facility layout.  A typical manufacturing cell involving semi-automated machines is studied.  The assignment of workers to machines is of interest along with a detailed assessment of the movement of workers within the cell. 

Chapter 12 shows how flexible machines could be used together for production.  Flexible machines are programmable and thus can perform multiple operations on multiple types of parts.  Alternative assignments of operations and part types to machines are compared.  The importance of simulating complex, deterministic systems is discussed. 

The application studies in this and the remaining parts of the book are more challenging than those in the previous part.  They are designed to be metaphors for actual or typical problems that can be addressed using simulation.  The applications problems make use of the modeling and experimentation techniques from the corresponding application studies but vary significantly from them.  Thus some reflection is required in accomplishing modeling, experimentation, and analysis.  Questions associated with application problems provide guidance in accomplishing these activities.
