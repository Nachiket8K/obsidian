---
title: "Chapter 16[1]"
book: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li"
source_pdf: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li.pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 16[1]** 

## **Transfer Hubs** 

## _16.1 Introduction_ 

Companies such as FedEx and United Parcel Service specialize in the delivery of packages often when time is critical.  The network of trucks and airplanes employed by such a company transports millions of packages to both business and personal customers each year. 

The ground based shipping methods employed by these companies typically rely on a network of terminals and hubs to move packages throughout the country.  Vans are used to pick up packages from customers and deliver them to a small terminal.  If a package needs to be sent outside of the terminal’s delivery area, it is loaded onto a tractor-trailer truck and sent to a hub. 

Most hubs are located in major cities with hundreds of the smaller terminals located in smaller cities.  Tractor-trailers containing packages to be shipped a great distance across the country can be loaded onto railcars to reduce cost.  When the tractor-trailer arrives at a hub, the packages it contains are sorted by destination.  Outbound packages can be loaded into vans for local delivery or sent to other hubs throughout the network. 

At the heart of the hub is the material handling system usually a conveyor system.  The conveyor system is used to unload, sort and transport packages throughout the hub.  Hub facilities may be of enormous size, some containing 8 miles of conveyor.  The hub material handling system is built up in phases.  Each phase typically adds a copy of the original system as well as expanding it.  Phased development reduces the financial risk associated with installing the complete system before the demand to support it exists. 

The material handling structure employed by a typical hub is shown in Figure 16-1.  A truck arrives to one of many docks that comprise the unload area.  A large conveyor is extended into the truck.  A worker manually unloads each truck and places the packages it contains on the conveyor. 

A set of conveyors, usually four in number, used in truck unloading is called a bank.  Typically, each pair of unload banks feeds a primary sorter, which processes packages from multiple unloading doors at once.  A variety of logic is used to merge packages on to a single conveyor before reaching the primary sorter. 

Each of the primary sorters routes packages to one of many secondary sorters.  A secondary sorter routes each package to a particular lane and hence to an outbound truck.  A worker removes each package from a lane and places it in the proper truck.  A lane corresponds to a particular zip code or truck destination.  A typical secondary sorter supports 20 lanes. 

> 1 Mr. Joel Oostdyk assisted with the development of this application study. 

16-1 

**==> picture [44 x 55] intentionally omitted <==**

**==> picture [74 x 41] intentionally omitted <==**

**==> picture [37 x 55] intentionally omitted <==**

**==> picture [35 x 34] intentionally omitted <==**

**==> picture [34 x 34] intentionally omitted <==**

**==> picture [35 x 35] intentionally omitted <==**

**==> picture [34 x 35] intentionally omitted <==**

**==> picture [35 x 34] intentionally omitted <==**

**==> picture [139 x 40] intentionally omitted <==**

**==> picture [34 x 34] intentionally omitted <==**

_16.2 Points Made in the Case Study_ 

This case study deals with modeling issues concerning conveyors.  A conveyor is viewed as consisting of multiple segments.  Certain segments, such as the exit points for work stations, are key.  Key segments are modeled as resources with the number of units equal to the capacity of the segment.  When all resource units are busy, the key segment is full and other items “back up” along preceding segments of the conveyor.  The non-key segments are modeled as time delays only. 

Key segments and operations are modeled similarly.  A scarce system object is modeled as a resource constraining the movement of an entity.  An entity uses this object for a length of time and then releases it for use by other entities. 

Package travel time on a conveyor is determined from specifications of the speed of the conveyor and the distance the package must travel. 

Many simulation languages have special modeling constructs for representing conveyor systems in a model.  These constructs contain the logic for modeling key and other segments.  Thus, this logic can be included in a model transparently to its developer. 

In some cases, an operation may be performed by any of several workers or machines.  In the model, this implies a choice between resources.  The logic for making this choice must be specified. 

Multiple individually distinguishable resources may be identified by the same name.  The individual resources each have a unique ID number or index.  For example a model could represent 10 workers with the resource WORKER and worker 7 could be referenced by WORKER(7). 

16-2 

Ergonomic considerations can be included in a model.  In this case, worker walking time as well as allowances for rest and other personal time are taken into account. 

Performance measures can be computed from other performance measures.  In this case, the average utilization for a group of workers is computed from the utilization of each individual worker. 

## _16.3 The Case Study_ 

The following case study is a subset of one described by Warber and Standridge (2002).  A package sorting hub is entering an expansion phase.  The number of unloading banks, primary sorters and secondary sorters is increasing to support processing an increased volume of packages.  Secondary sorter operations are of particular interest. 

## 16.3.1 Define the Issues and Solution Objective 

The level of staffing is a significant cost component for a transfer hub.  Thus, the number of workers assigned to loading out bound trucks is at issue.  Management believes that a worker can support more than one secondary sorter lane at a time.  For example, a worker supporting two lanes would wait until a package arrives to one of the two lanes, walk to that lane, place the package on the truck, and return to look for the next arriving package on either lane.  Note that in addition to the time to load a package into a truck, the walking time to a lane must be taken into account. 

The number of workers to assign to the secondary sorter must be determined.  The number of workers should be minimized to reduce costs.  At the same time, loading delays are detrimental to hub operations.  Thus, the time to load a package should be minimized.  These two operating criteria are in conflict and a suitable balance between the two must be found. 

A simulation study will be done to determine the number of workers to assign per secondary sorter.  Trucks containing packages arrive to the terminal between 4:00 P.M. and 8:00 P.M. each day.  It is estimated that on the average 8000 of these packages will be processed by the secondary sorter of interest.  Since many packages are also sent to other secondary sorters, the time between arrivals the secondary sorter of interest is considered to be an exponentially distributed random variable with mean 4 hours / 8000 packages or 1.8 seconds. 

The secondary sorter serves 20 loading lanes each leading to a loading dock.  A package is equally likely to be routed to any of the loading lanes.  The distance between loading lanes is 10 feet measured from the center point of one loading lane to the center point of the next.  A detailed drawing of the secondary sorter of interest is given in Figure 16-2. 

The distance from the secondary sorter to a loading door is 37 feet.  The total length of the secondary sorter conveyor is 250 feet.  Conveyor speed is 1 foot per second. 

Loading time consists of two components:  the time for a worker to remove a package from the end of the loading lane and place it properly in the a truck and the time for the worker to walk to a loading lane.  The former can be modeled as a random variable since the location of a particular package in a truck depends on the packages currently in the truck.  Experience has found the loading time to be highly variable with a mean of 8 seconds.  Thus, loading time is considered to be exponentially distributed. 

The time for a worker to walk to a loading lane depends on how many lanes the worker serves.  If the worker serves two lanes and waits half way between them for an arriving package,  the walking distance is five feet.  Assuming the average walking speed is 2 miles per hour, the 

16-3 

average walking time is about 1.7 seconds.   This time is about 21% of the average time to place a package on a truck and thus is a significant factor in determining system performance. 

**==> picture [358 x 114] intentionally omitted <==**

**==> picture [421 x 57] intentionally omitted <==**

## 16.3.2 Build Models 

The model of the secondary sorter operations must take into account the following system components. 

1. Arrival of packages to the secondary sorter between 4 P.M. and 8 P.M. with an exponentially distributed time between arrivals with a mean of 8 seconds. 

2. Package movement along the secondary sorter conveyor until the lane corresponding to the loading door is reached. 

3. Package movement to the end of the lane. 

4. Loading of the package on the truck. 

5. Worker assignment to lanes including walking time to a lane. 

Arriving entities model packages and have the following attributes. 

1. Lane: Loading lane assignment, 1, 2, …, 20. 2. TimeArriveLane: Time of arrival to the end of a lane. 3. LaneWorker: ID of the particular worker resource assigned to lane Lane. 

The latter attribute allows the time a package waited for a worker for loading to be collected. 

Model logic is shown in the following pseudocode.  Packages arrive according to an exponential distribution with mean 1.8 seconds.  The lane from which the package will be loaded is computed as a sample from a uniform distribution between 1 and 21.  Thus, each of the lanes 1 through 20 is equally likely.  The package moves on the secondary sorter conveyor at the rate of 1 foot per 

16-4 

second to the selected lane.  Then the package moves down the lane to its end at the same rate. The arrival time at the end of the lane is noted.  The package waits at the end of the lane for the worker serving that lane.  The waiting time is collected.  The worker walks to the lane in 1.7 seconds and then loads the package in an exponentially distributed time with a mean of 8 seconds.  After this task, the worker becomes IDLE again. 

Define Arrivals Time of first arrival: 0 Time between arrivals: Exponential 1.8 seconds Number of arrivals: Infinite Define Attributes Lane // Loading lane assignment, 1, 2, …, 20. TimeArriveLane // Time of arrival to the end of a lane. LaneWorker // ID of the particular worker resource assigned to lane Lane. Define Resources Worker(2) // Lane workers Process SecondarySorter Begin Lane = Integer (Uniform 1, 21) // Select Lane Wait for (1 sec * distance to lane in feet) // Move to lane Wait for (1 sec * length of lane conveyor in feet) // Move to load area TimeArriveLane = Clock LaneWorker = (Lane+1)/2 // Select lane worker Wait until Worker(LaneWorker)/1 is IDLE Make Worker(LaneWorker)/1 BUSY Tabulate (Clock-LaneArrivalTime) in WaitforWorker Wait for 1.7 seconds // Worker walks to lane Wait for Exponential 8 seconds // Worker loads truck Make Worker(LaneWorker)/1 IDLE End 

Model logic for a conveyor deserves more detailed discussion.  Consider a lane conveyor.  The conveyor is divided into segments.  Each segment can contain one package so each segment is the size of a package.  The segment at the end of the lane is called a key segment.  The key segment is modeled as a resource so that only one package can occupy the key segment at a time.  Packages waiting for the key segment to become idle occupy the segments physically preceding the key segment.  If enough packages are waiting, the lane could become full and block the secondary sorter conveyor. 

When modeling a conveyor, the size of entities traveling on the conveyor and the key segments must be specified along with the conveyor speed.  The use of the non-key segments as queuing space for a key segment must be included in the model.  Figure 16-3 summarizes these ideas. An entity moves on the lane until it reaches the non-key segment closest to the key segment that is not occupied by another entity.  Each entity waits to enter the key segment.  As an entity departs the key segment, all remaining waiting entities move one non-key segment closer to the key segment. 

Fortunately, the above logic is included in the modeling constructs of many simulation languages. Thus, the modeler is required only to specify the conveyor parameters, for example package size, conveyor speed, conveyor length, and key segment location. 

16-5 

16-6 

## 16.3.3 Identify Root Causes and Assess Initial Alternatives 

Management desires that the workers be kept as busy as possible.  On the other hand, ergonomic considerations require worker rest and personal time to be about 20% of the work period.  Thus, an average worker utilization of 80% is sought and this quantity is one performance measure.  The time a package waits for a worker before loading is also of interest. 

One model parameter will be varied, the number of lanes server by a worker, either 2 or 3.  Note that worker walking time to a lane will increase when 3 lanes are served.  The worker will stand at the middle lane of the three being served.  The walking distance to the middle lane is therefore neglibile.  The walking distance to each of the other two lanes is 10 feet.  Thus, the average walking distance increases from 5 feet to 6.67 feet and the average walking time increases from 1.7 seconds to 2.3 seconds.  Having each worker serve 3 lanes instead of 2 reduces the number of workers from ten to seven.  Six of the seven workers serve 3 lanes and the seventh server the remaining two lanes. 

Since trucks arrive with packages between 4 P.M. and 8 P.M. each day, a terminating simulation experiment of duration 4 hours is employed.  Twenty replicates will be made.  Since there are no packages at the secondary sorter at 4 P.M., the initial conditions are all lanes empty and all workers idle. 

There are three random number streams used in the model, one for package arrivals, one for lane assignments, and one for package loading time onto trucks. 

The experiment is summarized in Table 16-1. 

**Table 16-1:  Simulation Experiment Design for the Secondary Sorter** 

|**Element of the Experiment**|**Values for This Experiment**|
|---|---|
|Type of Experiment|Terminating|
|Model Parameters andTheir Values|Numberof lanes served by oneworker(2or3)|
|Performance Measures|1.  Average utilization over all workers<br>2.  Waiting timeforaworker|
|Random Number Streams|1.  Time between arrivals<br>2.  Lane assignment for a package (1-20)<br>3.  Loading time|
|InitialConditions|Empty andidle|
|Numberof Replicates|20|
|Simulation EndTime|4 hours|



Simulation results for the cases where a worker serves 2 and 3 lanes are shown in Table 16-2. Average worker utilization is the average utilization of all workers in the first case and of only those workers serving 3 lanes in the second case. 

16-7 

**Table 16-2:  Average Worker Utilization and Package Waiting Time for a Worker at the Secondary Sorter** 

||**Worker Serves Two Lanes**|**Worker Serves Two Lanes**|**Worker Serves**|**Three Lanes**|
|---|---|---|---|---|
|**Replicate**|**Average Package**<br>**Waiting Time(sec)**|**Average Worker**<br>**Utilization**|**Average Package**<br>**Waiting Time(sec)**|**Average Worker**<br>**Utilization**|
|1|<br>3.1|0.533|10.7|0.843|
|2|<br>2.8|0.520|9.8|0.832|
|3|<br>2.9|0.529|10.3|0.839|
|4|<br>2.9|0.535|10.8|0.845|
|5|<br>2.8|0.529|10.4|0.845|
|6|<br>2.9|0.528|10.4|0.842|
|7|<br>2.9|0.527|10.4|0.837|
|8|<br>3.0|0.527|10.1|0.839|
|9|<br>3.0|0.535|10.3|0.844|
|10|<br>3.1|0.538|10.6|0.855|
|11|<br>3.0|0.530|10.2|0.841|
|12|<br>2.9|0.527|9.9|0.835|
|13|<br>3.1|0.533|10.4|0.844|
|14|<br>3.2|0.546|11.3|0.870|
|15|<br>2.9|0.537|10.8|0.853|
|16|<br>2.9|0.530|10.3|0.843|
|17|<br>2.9|0.536|10.7|0.852|
|18|<br>3.1|0.536|11.4|0.858|
|19|<br>2.9|0.534|10.7|0.849|
|20|<br>3.0|0.526|10.3|0.836|
|**Average**|3.0|0.532|10.5|0.845|
|**Std. Dev.**|0.096|0.00560|0.398|0.00903|
|**99% CI Lower**<br>**Bound**|2.9|0.528|10.2|0.839|
|**99% CI Upper**<br>**Bound**|3.0|0.535|10.7|0.851|



Note that in neither case does the approximate 99% confidence interval contain the target utilization of 80%.  Package average waiting time increases by about 3.5 times when a worker serves three lanes instead of 2. 

## 16.3.4 Review and Extend Previous Work 

Management was disappointed that neither assigning 2 or 3 lanes to a worker produced the desired utilization of 80%.  The slightly higher utilization of 84.5% on the average was deemed unacceptable since upper bound of the 99% confidence interval was 85.1%.  A worker utilization of 53.2% was deemed too low and thus too costly. 

The following alternative was proposed.  Each worker would serve 2 lanes alone plus sharing the responsibility for a third lane with another worker.  This would increase the number of workers from seven serving 3 lanes each to eight serving 2.5 lanes each.  Thus, the simulation project process was restarted at the Build Models step. 

16-8 

## 16.4.1 Build Models 

The average walking time when a worker serves two lanes and shares responsibility for a third lane was computed as follows.  A worker stands in the same position as when serving 2 lanes. Thus, the average walking time is 1.7 seconds for 80% of the package loading operations.  For the other 20% of the package loads, the walking distance is 15 feet, which requires 5.1 seconds on the average.  Thus, two walking times must be included in the model. 

A new version of the model was created to model two workers sharing responsibility for every third lane.  The shared lanes are 3, 8, 13, and 18.  No changes to model logic are required for non-shared lanes.  For shared lanes, the changes to model logic are as follows. 

1. Wait for either lane worker to perform the loading operation, whichever one becomes IDLE first. 

2. Use the walking time to a shared lane, 5.1 seconds. 

3. Free whichever worker performed the loading operation. 

## 16.4.2 Identify Root Causes and Assess Initial Alternatives 

The experiment is the same as the one define in Table 16-1 except for the performance measures.  Waiting time for each of two types of packages is required:  those using lanes served by one worker alone and those using lanes servered by two workers. 

Simulation results comparing the two cases are shown in Table 16-3. 

In the shared lanes scenario, all workers serve the same number of lanes, 2.5.  The average worker utilization is 66.4%, less than the desired 80% target but more than in the case where each worker serves only two lanes.  Average package waiting time is about half of that in the workers serve 3 lanes case.  Average package waiting time is less on the shared lanes than on the lanes that do not share a worker. 

## 16.4.3 Implement the Selected Solution and Evaluate 

Management was disappointed that the target worker utilization of 80% could not be achieved but satisfied with the using eight workers instead of the ten required by the case in which a worker servers two lanes only.  Average package waiting time was deemed satisfactory. 

## _16.5 Summary_ 

This chapter discusses the modeling and analysis of a package transfer hub.  Specifically techniques for modeling conveyor systems have been presented.  The choice between alternative resources for performing an operation has been illustrated.  Ergonomic considerations have been included in the model.  The number of workers to serve a loading operation was determined. 

16-9 

**Table 16-3. Average Worker Utilization and Package Waiting Time for a Worker at the Secondary Sorter – Shared Lanes Case** 

||**Worker Serves Three Lanes**|**Worker Serves Three Lanes**|**Worker Serves Two Lanes Plus a Shared Lane**|**Worker Serves Two Lanes Plus a Shared Lane**|**Worker Serves Two Lanes Plus a Shared Lane**|
|---|---|---|---|---|---|
|**Replicate**|<br>**Average**<br>**Package**<br>**Waiting Time**|<br> <br> <br>**Average**<br>**Worker**<br>**Utilization**|<br> <br> <br>**Average**<br>**Package**<br>**Waiting Time**<br>**Non-Shared**<br>**Lanes**|<br> <br> <br> <br> <br>**Average**<br>**Package**<br>**Waiting Time**<br>**Shared Lanes**|<br> <br> <br> <br>**Average**<br>**Worker**<br>**Utilization**|
|1|<br>10.7|0.843|5.3|5.0|0.664|
|2|<br>9.8|0.832|4.9|4.2|0.650|
|3|<br>10.3|0.839|5.1|3.8|0.661|
|4|<br>10.8|0.845|5.2|4.5|0.669|
|5|<br>10.4|0.845|5.3|4.4|0.661|
|6|<br>10.4|0.842|5.3|4.4|0.660|
|7|<br>10.4|0.837|5.1|4.1|0.659|
|8|<br>10.1|0.839|5.2|4.3|0.659|
|9|<br>10.3|0.844|5.2|4.1|0.669|
|10|<br>10.6|0.855|5.2|4.2|0.671|
|11|<br>10.2|0.841|5.2|4.2|0.663|
|12|<br>9.9|0.835|5.2|4.2|0.658|
|13|<br>10.4|0.844|5.4|4.5|0.666|
|14|<br>11.3|0.870|5.7|4.8|0.683|
|15|<br>10.8|0.853|5.5|4.3|0.670|
|16|<br>10.3|0.843|5.5|4.7|0.662|
|17|<br>10.7|0.852|5.2|4.1|0.670|
|18|<br>11.4|0.858|5.7|4.7|0.670|
|19|<br>10.7|0.849|5.2|4.2|0.667|
|20|<br>10.3|0.836|5.2|4.2|0.657|
|**Average**|10.5|0.845|5.3|4.3|0.664|
|**Std. Dev.**|0.398|0.00903|0.193|0.284|0.00702|
|**99% CI Lower**<br>**Bound**|10.2|0.839|5.1|4.2|0.660|
|**99% CI Upper**<br>**Bound**|10.7|0.851|5.4|4.5|0.669|



## **Problems** 

1. Explain how sampling from the continuous uniform distribution with minimum 1 and maximum 21 gives equal probability to the integers 1 through 20 and no probability to the integer 21 when samples from truncated to integer values. 

2. Why is the time between the arrival of a package to the secondary sorter and completion of loading on a truck not a good performance measure?  Supply an improved definition for this performance measure. 

3. Develop a model for a lane served by either of two workers. 

16-10 

4. Perform a formal statistical analysis using paired confidence intervals and the data in Table 16-3 to confirm that package waiting time is less in the workers share lanes case than in the case where a worker serves 3 lanes. 

   - a. Compare average package waiting time with each worker serving 3 lanes (2[nd] column) with the average waiting time for lanes served by only one worker, the non-shared lanes (4[th] column). 

   - b. Compare average package waiting time in the shared lines (5[th] column) and the non-shared lanes (4[th] column). 

5. Explain why the average waiting time for packages for a shared lane served by two workers (5[th] column) is less than for lanes served by one worker (4[th] column) as seen in Table 16-3. 

6. Perform a formal statistical analysis using paired confidence intervals and the data in Tables 16-2 and 16-3 to compare the average package waiting time between the worker serves two lanes scenario (2[nd] column) and the shared lanes scenario (5[th] column). 

7. Explain why average package waiting time increases in a non-linear fashion as the utilization of the workers increases. 

8. Go to a manufacturing lab, transfer hub, or a local manufacturing plant to observe a conveyor system in operation.  List the number of different conveyor types found. 

9. Embellish the model to make package loading time a function of how many packages are on a truck.  Assume 8 seconds is the mean time to load the package in the center of the truck and each truck holds 200 packages. The mean loading time varies linearly from 12 seconds for a completely empty truck to 4 seconds for the last package on a truck.  After the 200[th] package is loaded on a truck, the fully loaded truck swaps positions with an empty truck in 3 minutes.  No package loading can occur during this time.  Determine the number of workers needed under these conditions. 

10. Suppose that packages are not uniformly distributed across final destinations but the distribution by destination is shown in the following table.  Use simulation to assign the package destinations to lanes as well as workers to lanes.  The destinations may be assigned to lanes in any way that is helpful. 

|**Package**<br>**Destination**|<br>**Percent of**<br>**Packages**|<br> <br>**Package**<br>**Destination**|<br>**Percent of**<br>**Packages**|
|---|---|---|---|
|1|0.48%|11|<br>5.24%|
|2|0.95%|12|<br>5.71%|
|3|1.43%|13|6.19%|
|4|1.90%|14|<br>6.67%|
|5|2.38%|15|7.14%|
|6|2.86%|16|7.62%|
|7|3.33%|17|<br>8.10%|
|8|3.81%|18|8.57%|
|9|4.29%|19|9.05%|
|10|4.76%|20|9.52%|



16-11 

## **Case Study** 

Some packages that pass through a primary sorter cannot be routed to a secondary sorter for a variety of reasons and must be manually processed.  Suppose such packages are routed to a circular conveyor as shown in Figure 16-4.  Packages proceed around the conveyor to a workstation.  There is no package waiting area or buffer at a workstation.  If a package arrives to a station that is processing another package, it stays on the conveyor to the next station.  If the package is not processed by the last station, it recirculates to the first station. 

The purpose of the simulation study is to specify the parameters of the manual system to minimize package lead time.  There may be either 1, 2, 3, or 4 workstatons employed.  In addition, waiting areas for up to three packages may be placed in any fashion among the workstations.  Cost considerations make more buffer spaces and fewer workstations the preferred design.  Determine the number of workstations, the number of buffer spaces, and the location of the buffer spaces. 

Relevant information is as follows: 

Time between package arrivals: Package processing time: 

Exponentially distributed with mean 1.6 minutes. Exponentially distributed with mean 4.0 minutes. 

## **Conveyor Segments (Assuming a Four Workstation Configuration).** 

|**Conveyor Segment**|**Conveyor**<br>**Distance(Feet)**|
|---|---|
|Arrival Point toFirstWorkStation Exit|18|
|Station Exit Segment|2|
|Inter-StationSegment (toExit Segment)|13|
|Last StationtoArrival Point (4stations case)|45|



Assume that conveyor speed is 0.25 feet / second and that packages are 2 feet in length.  The time period of interest is 40 hours. 

16-12 

## Case Problem Issues 

1. Count the number of possible alternatives.  Is it reasonable to simulate all of these? 

2. Which alternatives should be simulated to make sure the best or at least a good alternative is identified? 

3. What performance measures in addition to package lead time are of interest? 

4. What operating rules could be added to the system to guard against excessive lead times for individual packages? 

5. What is the minimum number of workstations required by the system? 

6. Discuss how verification and validation evidence can be obtained. 

7. What is the purpose of having buffer space in front of workstation? 

8. How is the arrival of a package to a workstation modeled if: 

   - a. There is no buffer space at the workstation. 

   - b. There is at least one buffer space at the workstation. 

9. What is your initial guess as to the best placement for the buffer spaces?  Does the simulation study confirm your guess? 

10. Tell how to compute the lead time for a package as a function of the number times it travels completely around the conveyor within the simulation. 

11. What is the radius of the conveyor:  radius = circumference / 2 ? 

16-13
