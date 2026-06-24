---
title: "Chapter 17"
book: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li"
source_pdf: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li.pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 17** 

## **Automated Guided Vehicle Systems** 

## _17.1 Introduction_ 

An automated guided vehicle (AGV) system can transport material between a finite number of pre-defined locations at work stations with little or no human assistance.  Barrett Electronics Corporation invented the world’s first AGV for industrial applications in 1954. In the United States there have been over 3,000 AGV systems installed during the last 50 years. These systems range from one vehicle to well over 100 vehicles. 

An AGV system consists of vehicles that move along predetermined paths to move loads between workstations and storage areas.  Vehicles operate without the need for an onboard operator or driver, pick up loads at designated pick-up points and transport them to designated drop-off points.  Each workstation has a pick-up point and a drop-off point.  These two points can be the same. 

There are several major categories of vehicles: 

1. **Tow Type** vehicles that pull carts, trailers, dollies and the like. 

2. Self-contained **Unit Load Type** vehicles that carry products on their built-in load decks. 

3. **Fork Type** vehicles that utilize a fork/mast lift mechanism for interfacing with loads at various elevations. 

4. Smaller **Commercial/Office Type** vehicles that have capacities of less than 500 pounds. 5. **Heavy Carrier Type** vehicles designed to transport large or very heavy loads such as dies, rolls, coils, ingots weighing in excess of 250,000 pounds. 

Vehicles move between work stations by traversing control segments.  Each control segment is relatively short.  The intersection point between control segments is a control point.  Pickup and dropoff points are control points as well. 

Vehicles in most existing systems follow an inductive guide path consisting of a wire embedded in the floor carrying alternating current that induces a magnetic field detected by antenna mounted on the bottom of the vehicles.  Other control mechanisms include surface mounted magnetic or optical strips as well as inertial or laser guidance.  Vehicles have controllers that respond to instructions and ensure safety. 

AGV systems must be able to perform routing, traffic control and communications functions. Routing is the method by which an AGV determines how to go from its current location to a designated destination. Different approaches to routing logic can be implemented such as shortest time, shortest distance and fixed pattern.  Traffic control assures that AGVs do not collide with each other.  Either fixed or variable distances between vehicles can be used. 

Communication is needed between vehicles, between a vehicle and a central device or for local interfaces.  The communication mechanism provides the means by which vehicles are informed of routing and traffic control decisions. 

17-1 

A simple AGV system is shown in Figure 17-1.  There are four control segments that form a loop in the shape a rectangle with rounded corners.  Rounded corners allow the AGV to continue at full speed instead of stopping to make a 90 degree turn as would be the case if square corners were used.  There are four stations each with its own control point indicating the place where loads are picked up or dropped off.  AGV’s move in only one direction, clockwise, around the loop. 

Requests come to move loads from one workstation to another.  In response, an idle AGV moves from the parking area to the pickup point of the workstation where the load currently resides.  The AGV moves from this pickup point to the drop off point of the destination workstation.  After unloading, the AGV remains idle at the dropoff point. 

17-2 

## _17.2 Points Made in the Case Study_ 

Simulation can be used to assess the operational behavior of a system designed by other means. In this case, the AGV system is designed using standard, analytic methods.  Simulation is used to assess the behavior of the system as designed relative to operational performance criteria as well as to determine the number of vehicles the system needs. 

The structure of a system can be described using data inputs to a model.  This allows changes in system structure to be assessed without changing the model.  In this case, the control segments and control points are defined by input data.  This data input most often takes the form of a graphical drawing. 

The models originally developed for operations can be directly applied to material handling situations as well.  This illustrates how models developed for one domain may be directly applied to another domain where system components behavior and interact in an analogous way.  In an AGV system, the control points constrain the movement of the vehicles to assure that there are no collisions at interactions.  Thus, control points can be modeled as a single machine station where the processing time is the time to traverse the control point. 

Increasing the number of resources that can perform an activity, such as the number of machines at a workstation, normally lessens entity waiting time for that activity.  Thus, it might be assumed that increasing the number of vehicles in an AGV system would increase the responsiveness to movement requests.  This might not be the case since the contention between the AGV’s for control segments, intersections, and control points will increase. 

## _17.3 The Case Study[1]_ 

The case study has to do with confirming the operational effectiveness of the design of a new AGV system as well as determining the number of vehicles needed.  Load movement requests can be modeled as having a constant time between arrivals.  However, the orgin and destination points are stochastic.  That is not all requests for material movement can be predetermined.  The discussion and examples of AGV systems in Askin and Standridge (1993) form the basis for this case study. 

## 17.3.1 Define the Issues and Solution Objective 

The design of a new AGV system to serve nine workstations as shown in Figure 17-2.  Each shorter edge corresponds to 50 feet and each longer edge to 100 feet.  AGV's move in one direction only on each bold edge as indicated by the arrows.  There is no AGV movement on dashed edges.  The letters in the center of a square are the work station ID's.  The numbers near the edges are the control segment ID's.  Idle AGV’s wait where at the dropoff point of their last load. 

The pickup and dropoff points for each workstation are indicated using the letters P and D respectively.  Note that stations 5 and 6 share these points. 

Table 17-1 gives the average number of material moves between workstations per 16 hour day. This information forms the distribution of pickup point to dropoff point AGV movements.  Each individual movement can be determined as a random sample from this distribution.  The time between material moves is a constant 90 seconds (57600 seconds per day / 640 moves). 

A material move requires an AGV to move from it current location to the pickup point and then from the pickup point to the dropoff point.  Each AGV moves at the rate of 5 feet per second and takes 30 seconds for each drop-off and each pick-up. 

- 1 Todd Frazee assisted with the development of this case study. 

17-3 

**==> picture [65 x 56] intentionally omitted <==**

**==> picture [123 x 33] intentionally omitted <==**

The design shown in Figure 17-2 was developed using analytic methods.  The following principles were applied. 

1. Vehicles move in only one direction on path. 

2. The dropoff point for a station should precede the pickup point with respect to vehicle movement. 

3. Dropoff and pickup points should be placed on control segments with low utilization to avoid other vehicles waiting for dropoffs and pickups to be completed. 

4. Movement of empty vehicles should be minimized.  Thus after a dropoff is completed, the vehicle should wait on the same control segment for a possible pickup on that segment. 

Other analytic methods were used to estimate that 2 AGV’s would be needed in the system. These analytic methods were used to compute each of the five components of total vehicle utilization time:  loaded travel time, travel time while empty, blocked time, load time, and unload time.   These computations are based on knowledge of the number of loads to be moved between each pair of workstations (the information shown in Table 17-1) as well as AGV travel speeds and the shortest path between each pair of workstations. 

Loaded travel time, load time, and unload time are straightforward to compute.  A lower bound on travel time while empty can be computed using an optimization algorithm.  Blocked time was assumed to be zero for this system since the number of AGV’s need was only 2. 

17-4 

**Table 17-1:  Average Number of Material Moves between Work Stations** 

|**From Work**<br>**Station**|**To Work**<br>**Station**|**Average Number**<br>**of Moves**|
|---|---|---|
|A|B|40|
|A|C|25|
|A|D|30|
|A|E|10|
|A|F|10|
|A|G|20|
|A|H|5|
|A|I|10|
|B|C|40|
|B|E|30|
|B|G|10|
|B|H|10|
|C|G|50|
|C|I|10|
|D|B|5|
|D|C|10|
|D|F|10|
|E|D|100|
|F|D|60|
|G|F|40|
|G|I|40|
|H|D|10|
|H|F|5|
|I|E|60|
|Total||640|



Management wishes to confirm the operationally effectiveness of AGV system as designed.  The primary performance criteria is time between the request for a load to be moved and the completion of the move.  Both the maximum and average time are interest.  Assessing the number of AGV’s needed is also important since blocked time was ignored and only a lower bound on travel time while empty was obtained.  There is concern that 2 AGV’s are not sufficient. 

## 17.3.2 Build Models 

It is helpful to take a generic perspective to modeling AGV systems.  The control segments and control points that comprise the paths taken by the vehicles between workstations can be data input, expressed most often as a graphical drawing.  In this case, the graphical drawing used for input this information is the one in Figure 17-2.  Other inputs include where vehicles park when they become idle and vehicle speed.  Vehicles can be viewed as resources.  This generic view is implemented in some simulation environments. 

In addition, a process model describing the movement of loads through the AGV system, perhaps including processing at workstations, is needed.  A request to move a load is the entity flowing through the process.  The following are the major steps in the process model. 

1. Arrival of a request for an AGV to move a load from one workstation to another. 2. Waiting for an idle AGV. 

3. Selection of the idle AGV nearest to the pickup point for the load. 

4. Movement of that AGV from where it is parked to the pickup point. 

5. Movement of the same AGV from the pickup point to the dropoff point. 

17-5 

Attributes of the entity are the following: 

FromStation The station where the load is to be picked up. ToStation The station where the load is to be dropped off. ArriveTime Simulation time that the request for load movement is made. 

Analytic algorithms for determining the shortest path from one workstation to another are known and can be implemented within a simulation environment that supports modeling AGV systems. In most cases, the number of feasible paths between any pair of workstation should be few in number.  Otherwise, the system would be too complex to operate.  For example, consider the number of paths from workstation A in Figure 17-2 to each of the other eight workstations.  There is only one path to workstations B, C, E, F, and G.  There are two paths to the other workstations: D, H, and I.  However, one of the two paths is obviously shorter. 

One issue that is unique to modeling AGV systems is contention among the vehicles for the same control segment or control point.  All vehicles travel at the same speed so one cannot overtake another as long as both are moving in the same direction.  Contention occurs when one vehicle is stopped at a pickup or dropoff point and another vehicle needs to pass through such a point enroute somewhere else.  In this case, the second vehicle needs to stop to wait for the first vehicle to leave the pickup or dropoff point. 

In addition, contention can occur when two vehicles coming from opposite directions arrive at the same intersection at the same time.  One vehicle needs to stop or slow down to let the other vehicle pass.  There are two such intersections in the AGV system shown in Figure 17-2.  One is at the right side of the boundary between workstations G and I.  The other is at the center of the upper boundary of workstation H where the path dividing workstations E and F ends. 

One system performance criterion is the time between the request for moving a load and completion of the move.  Thus, it may seen desirable to have as many AGV’s in the system as possible to minimize this time.  This strategy is similar to increasing the number of machines at a workstation to minimize cycle time at the station that was employed in previous chapters. However, increasing the number of AGV’s also increases the contention for control points and control segments.  Thus, such increases may be counter productive and must be tested using simulation. 

The modeling logic described above follows in pseudo English.  AGV’s are modeled as resources as are pickup and dropoff points.  Each AGV has an attribute, CurrentLoc, giving its current location.  Resources are also used to model intersections where vehicles can enter from more than one direction. 

Travel along a path is comprised of a series of steps as modeled by Process MoveOnPath with parameters FromLoc and ToLoc.  Each step represents travel between the current AGV location and the next pickup point, dropoff point, or intersection on the path.  Each of these is modeled as resource that must be acquired to traverse that part of the path and freed after such movement is accomplished. 

The next pickup point, dropoff point, or intersection and the distance to it are exacted from the data input describing the AGV system that was given as a graphical drawing.  In this case, travel time can be modeled as distance traveled * AGV speed.  It is possible to include acceleration and deacceleration if desired.  When the destination control point is reached, travel ends.  Otherwise travel to the next pickup point, dropoff point, or intersection commences. 

The process AGV System makes use of the process MoveOnPath.  Arrivals to the process are requests for load movement that occur every 90 seconds in this case.  Entity attributes are assigned:  the workstation where the load currently resides, the workstation to which the load 

17-6 

must be transported, and the simulation time the request arrives.  The idle AGV closest to the workstation station where the load currently resides is chosen.  If there are no idle AGV’s the movement request must wait.  The AGV moves empty workstation to the where the load is residing, picks of the load, moves to the destination station, and drops off the load.  The AGV become IDLE and the current location of the AGV is recorded. 

Define Resources AGV/2 // Two AGV’s ControlPointIntersection (n)/1 // Control Points and Path Intersections Define Attributes FromStation // The station where the load is to be picked up. ToStation // The station where the load is to be dropped off. ArriveTime // Time the request for load movement is made. Define Variables StartTrip (NStations) // Distribution of trip starting point stations EndTrip  (NStations, NStations) //  Distribution of trip end point stations by starting station CurrentLoc(2) // Current location of an AGV Process AGV_System Define Arrivals Time of first arrival: 0 Time between arrivals: 90 seconds Number of arrivals: Infinite Begin Set TimeArrive = Clock FromStation = Sample (StartTrip) EndStation = Sample(EndTrip(FromStation)) Wait until AGV is IDLE in WaitforAGV   // IDLE AGV closest to From Station is chosen Make AGV Busy Send to MoveOnPath (CurrentLoc, FromStation) with return Wait for 30 seconds // Pick up load Send to MoveOnPath (FromStation, ToStation) with return Wait for 30 seconds // Drop off load Make AGV IDLE CurrentLoc (AGV) = ToStation Tabulate Clock – TimeArrive in CompleteMovementTime End Process MoveOnPath (FromLoc, ToLoc) Begin While CurrentLoc(AGV) != ToLoc Begin CurrentLoc (AGV) = FromLoc Wait for Distance*AGVSpeed to Next Control Point or Intersection from CurrentLoc CurrentLoc (AGV) = Next Control Point or Intersection Wait until ControlPointIntersection (CurrentLoc(AGV)) is IDLE Make ControlPointIntersection (CurrentLoc(AGV)) BUSY Wait for Distance through Control Point or Intersection * AGVSpeed Make ControlPointIntersection (CurrentLoc(AGV)) IDLE 

End 

End 

17-7 

_____________________________________________________________________________ 

_ 

## 17.3.3 Identify Root Causes and Assess Initial Alternatives 

The simulation experiment can be described as follows.  The system operates for one 16 hour day.  Thus, a terminating simulation of length one day is appropriate.  The proper initial conditions are all AGV’s idle since no load movement requests occur before the work day begins.  Their initial location is randomly assigned.  There is one random number stream to aid in selecting the pair of workstations for pickup and dropoff.  Twenty replicates are made. 

Management wishes to minimize the time to complete a movement request.  Thus, performance measures include this quantity as well as the utilization of AGV’s and AGV capacity lost to contention for control segments and control points.  AGV congestion will be measured as the average number of AGV’s waiting due to contention for control points and intersections. 

The number of AGV’s required must be determined, either the 2 previously recommend or 3 to improve the time to complete a movement request.  The model parameter is the number of AGV’s to employ.  Table 17-2 summarizes the experimental design. 

**Table 17-2:  Simulation Experiment Design for the AGV System** 

|**Element of the Experiment**|**Values for This Experiment**|
|---|---|
|Type of Experiment|Terminating|
|Model Parameters andTheir Values|1.  Number of AGV’s(2 or 3)|
|Performance Measures|1.  Time to complete a move request<br>2.  AGV utilization<br>3.  AGVcongestion|
|Random NumberStreams|1.  From-to pairof workstations|
|InitialConditions|AGV’srandomly assigned to controlpoints|
|Numberof Replicates|20|
|SimulatedEndTime|57600 seconds (one day)|



Tables 17-3 through 17-5 give the simulation results for the above experiment, including a comparison between system operations when 2 and 3 AGV’s are used. 

17-8 

**Table 17-3:  Simulation Results for Two AGV’s** 

||**AGV’s**|**AGV’s**|**Time to Complete a Move(min)**|**Time to Complete a Move(min)**|
|---|---|---|---|---|
|**Replicate**|**Idle Percent**|**Percent**<br>**Congested**|**Maximum**|**Average **|
|1|0.7%|2.6%|80.9|8.7|
|2|1.4%|2.0%|60.8|5.9|
|3|0.5%|2.1%|114.6|15.5|
|4|0.4%|2.6%|92.3|11.5|
|5|1.6%|2.2%|99.1|9.8|
|6|1.4%|2.2%|71.0|6.8|
|7|1.3%|2.5%|88.8|9.0|
|8|0.6%|2.2%|100.6|10.0|
|9|1.2%|2.3%|75.9|8.4|
|10|0.4%|2.0%|120.2|14.4|
|11|2.8%|2.5%|43.9|5.1|
|12|0.5%|2.0%|105.5|13.0|
|13|0.4%|2.3%|94.9|11.3|
|14|1.9%|1.9%|45.4|5.5|
|15|1.9%|2.6%|60.7|6.0|
|16|2.5%|2.5%|24.9|4.4|
|17|1.2%|2.1%|125.3|14.3|
|18|1.2%|2.2%|52.1|5.8|
|19|0.9%|2.3%|93.2|12.9|
|20|0.4%|2.2%|79.7|10.4|
|**Average **|1.2%|2.3%|81.5|9.4|
|**Std. Dev.**|0.7%|0.2%|27.2|3.4|
|**99% CI Lower Bound**|0.7%|2.1%|64.1|7.2|
|**99% CI Upper Bound**|1.6%|2.4%|98.9|11.6|



The following can be noted from Table 17-3 when 2 AGV’s are used. 

1. The AGV’s are almost always busy. 

2. There is very little congestion. 

3. The average time to complete a move is 9.4 minutes with an approximate 99% confidence interval for the true average of (7.2, 11.6) minutes. 

4. The maximum time to complete a move is over an hour with an approximate 99% confidence interval of (64.1, 98.9) minutes. 

Thus it can be concluded from Table 17-3 that using only 2 AGV’s is ineffective since the average time and maximum times to complete a move are too high.  This is not unexpected since the AGV’s are almost always busy.  On the other hand, there is very little contention. 

17-9 

**Table 17-4:  Simulation Results for Three AGV’s** 

||**AGV’s**|**AGV’s**|**Time to Complete a Move(min)**|**Time to Complete a Move(min)**|
|---|---|---|---|---|
|**Replicate**|**Idle Percent**|**Percent**<br>**Congested**|**Maximum**|**Average**|
|1|21.3%|12.8%|7.8|3.1|
|2|21.0%|12.0%|7.5|3.1|
|3|22.8%|11.7%|9.0|3.0|
|4|21.5%|11.5%|12.0|3.1|
|5|21.3%|12.1%|8.5|3.1|
|6|21.1%|12.0%|9.9|3.1|
|7|20.8%|11.8%|8.1|3.1|
|8|21.5%|11.5%|9.3|3.1|
|9|21.3%|12.0%|9.3|3.1|
|10|22.1%|11.5%|9.0|3.1|
|11|20.7%|12.6%|9.1|3.1|
|12|22.1%|10.9%|8.2|3.1|
|13|21.2%|12.0%|8.8|3.1|
|14|20.5%|12.6%|8.5|3.1|
|15|22.3%|11.4%|9.5|3.1|
|16|22.9%|11.8%|8.5|3.0|
|17|21.4%|11.8%|9.2|3.1|
|18|21.4%|12.0%|10.5|3.1|
|19|21.2%|11.8%|9.3|3.1|
|20|23.0%|10.5%|8.4|3.0|
|**Average **|21.6%|11.8%|9.0|3.1|
|**Std. Dev.**|0.7%|0.5%|1.0|0.04|
|**99% CI Lower Bound**|21.1%|11.5%|8.4|3.1|
|**99% CI Upper Bound**|22.0%|12.2%|9.7|3.1|



The following can be noted from Table 17-4 when 3 AGV’s are used. 

1. AGV utilization is near 80%. 

2. Significant congestion occurs since about 1/3 of the available time of 1 AGV is lost (11.8 % * 3 AGV’s = 1/3 of 1 AGV). 

3. The average time to move a load is about 3 minutes. 4. The maximum time to move a load is about (8.4, 9.7) minutes with approximately 99% confidence. 

Thus it can be concluded from Table 17-4 that using 3 AGV’s allows movement to occur in a sufficiently small amount of time.  AGV utilization is neither too high or too low.  However, contention among the three AGV’s is significant. 

17-10 

**Table 17-5:  Comparison of Simulation Results for Two and Three AGV’s** 

||**AGV’s (3-2)**|**AGV’s (3-2)**|**Time to Complete a Move (min)**<br>**(2-3)**|**Time to Complete a Move (min)**<br>**(2-3)**|
|---|---|---|---|---|
|**Replicate**|**Idle Percent**|**Percent**<br>**Congested**|**Maximum**|**Average**|
|1|20.6%|10.2%|73.1|5.6|
|2|19.6%|10.0%|53.3|2.8|
|3|22.3%|9.6%|105.6|12.5|
|4|21.1%|8.9%|80.3|8.4|
|5|19.7%|9.9%|90.6|6.7|
|6|19.7%|9.8%|61.2|3.7|
|7|19.5%|9.3%|80.7|5.8|
|8|20.9%|9.3%|91.3|6.9|
|9|20.1%|9.7%|66.6|5.3|
|10|21.7%|9.5%|111.2|11.4|
|11|17.9%|10.1%|34.8|2.0|
|12|21.6%|8.9%|97.3|9.9|
|13|20.8%|9.7%|86.2|8.1|
|14|18.6%|10.7%|36.9|2.4|
|15|20.4%|8.8%|51.3|2.9|
|16|20.4%|9.3%|16.4|1.4|
|17|20.2%|9.7%|116.2|11.1|
|18|20.2%|9.8%|41.6|2.7|
|19|20.3%|9.5%|83.9|9.8|
|20|22.6%|8.3%|71.4|7.4|
|**Average **|20.4%|9.6%|72.5|6.3|
|**Std. Dev.**|1.1%|0.5%|27.2|3.4|
|**99% CI Lower Bound**|19.7%|9.2%|55.1|4.1|
|**99% CI Upper Bound**|21.1%|9.9%|89.9|8.5|



Table 17-5 shows that the difference between using 2 AGV’s and 3 AGV’s is statistically significant with approximately 99% confidence for all performance measures.  AGV utilization is lowered when 3 AGV’s are used as well as the average and maximum time to move a load. Congestion increases as well. 

## 17.3.4 Review and Extend Previous Work 

Management was pleased with the results of the simulation experiment.  It was decided that three AGV’s should be used. 

The amount of contention between the three AGV’s was of concern.  It was felt that if load volumes increased and the addition of a fourth AGV was necessary that contention might cause the AGV system to take too long to respond to and complete transportation requests. 

Thus, a redesign of the AGV system was proposed.  The pickup and dropoff points for each workstation would be located within the station.  Workstations E and F would have distinct pickup and dropoff points. 

## _17.4 Assessment of Alternative Pickup and Dropoff Points_ 

The impact of alternative pickup and dropoff points was assessed as follows. 

17-11 

## 17.4.1 Identify Root Causes and Assess Initial Alternatives 

The assessment of the new AGV system design can be done in the following way.  Note from Figure 17-2 that there are two types of workstations.  The pickup and dropoff points for workstations B, C, D, E, and F are located near each other.  The pickup and dropoff points for workstations G, H, and I are separate.  Workstation A has only a pickup point. 

Figure 17-3 shows the redesign of the pickup and dropoff points for workstations B, C, D, E, and F.  Figure 17-4 shows the redesign for the remaining stations.  Note that the AGV’s have a greater distance to travel to both pickup and dropoff a load since a loop of about 15 feet must be traversed into each workstation. 

**==> picture [76 x 119] intentionally omitted <==**

17-12 

**==> picture [79 x 83] intentionally omitted <==**

**==> picture [90 x 92] intentionally omitted <==**

A new simulation experiment can be executed.  The design is the same as shown in Table 17-2 except that the operation of the modified AGV layout with three AGV’s only will be assessed. Note that the model does not need to be modified since the AGV layout is input data expressed as a graphical drawing.  Simulation results for this experiment are shown in Table 17-6. 

The following can be noted from Table 17-6. 

1. AGV utilization is near 72%. 

2. Only a little congestion occurs since about 13% of the available time of 1 AGV is lost. 

3. The average time to move a load is about 3 minutes. 

4. The maximum time to move a load is about (10.3, 28.1) minutes with approximately 99% confidence.  The average maximum is 19.2 minutes.  The range of the maximum times across the replicates is (5.3, 56.8) minutes. 

17-13 

## **Table 17-6:  Simulation Results for Three AGV’s with Dropoff and Pickup Points within Each Workstation** 

||**AGV’s**|**AGV’s**|**Time to Complete a Move(min)**|**Time to Complete a Move(min)**|
|---|---|---|---|---|
|**Replicate**|**Idle Percent**|**Percent**<br>**Congested**|**Maximum**|**Average**|
|1|26.4%|4.9%|3.3|38.3|
|2|27.6%|3.9%|2.8|10.0|
|3|28.1%|4.4%|2.8|12.2|
|4|28.6%|4.5%|2.9|33.2|
|5|27.9%|4.5%|2.8|5.3|
|6|28.4%|3.6%|2.8|12.5|
|7|28.6%|3.5%|2.7|5.3|
|8|28.2%|4.0%|2.9|23.3|
|9|28.6%|4.1%|2.9|32.9|
|10|28.3%|3.6%|2.8|16.3|
|11|28.3%|4.3%|2.9|22.4|
|12|26.6%|3.9%|3.2|32.5|
|13|27.3%|4.9%|3.5|56.8|
|14|28.4%|4.2%|2.8|11.5|
|15|28.4%|4.8%|2.8|18.6|
|16|28.4%|4.2%|2.7|7.5|
|17|28.3%|5.8%|2.9|25.5|
|18|28.5%|3.9%|2.7|7.8|
|19|27.6%|3.7%|2.8|5.4|
|20|27.8%|4.4%|2.8|6.8|
|**Average **|28.0%|4.3%|2.9|19.2|
|**Std. Dev.**|0.6%|0.6%|0.2|13.9|
|**99% CI Lower Bound**|27.6%|3.9%|2.8|10.3|
|**99% CI Upper Bound**|28.4%|4.6%|3.0|28.1|



Table 17-7 contains a comparison of AGV system operations using the initial system design and the new system design each employing 3 AGV’s. 

17-14 

**Table 17-7.  Comparison of Simulation Results for the Original and Modified System Designs** 

||**AGV’s (New-Original)**|**AGV’s (New-Original)**|**Time to Complete a Move (min)**<br>**(New-Original)**|**Time to Complete a Move (min)**<br>**(New-Original)**|
|---|---|---|---|---|
|**Replicate**|**Idle Percent**|**Percent**<br>**Congested**|**Maximum**|**Average**|
|1|5.1%|-7.9%|-4.5|35.2|
|2|6.6%|-8.1%|-4.8|6.9|
|3|5.3%|-7.3%|-6.3|9.2|
|4|7.1%|-7.0%|-9.1|30.1|
|5|6.6%|-7.6%|-5.8|2.2|
|6|7.3%|-8.4%|-7.1|9.4|
|7|7.8%|-8.3%|-5.4|2.2|
|8|6.7%|-7.5%|-6.4|20.2|
|9|7.3%|-7.9%|-6.4|29.8|
|10|6.2%|-7.9%|-6.2|13.2|
|11|7.6%|-8.3%|-6.2|19.2|
|12|4.5%|-7.0%|-5.1|29.4|
|13|6.1%|-7.1%|-5.3|53.7|
|14|7.9%|-8.4%|-5.7|8.3|
|15|6.1%|-6.6%|-6.7|15.5|
|16|5.5%|-7.6%|-5.8|4.5|
|17|6.9%|-6.0%|-6.2|22.3|
|18|7.1%|-8.1%|-7.8|4.7|
|19|6.4%|-8.1%|-6.5|2.3|
|20|4.8%|-6.1%|-5.6|3.8|
|**Average **|6.4%|-7.6%|-6.1|16.1|
|**Std. Dev.**|1.0%|0.7%|1.0|13.8|
|**99% CI Lower Bound**|5.8%|-8.0%|-6.8|7.2|
|**99% CI Upper Bound**|7.1%|-7.1%|-5.5|25.0|



The following can be noted from Table 17-7. 

1. AGV utilization increases as the average congestion increases for the new system configuration versus the original configuration.  These difference are both significant with approximately 99% confidence.  Note that both differences are small. 

2. There is little difference in the average time to move a load between the two designs, though the difference is statistically significant. 

3. The difference in the maximum time to move a load is operationally and statisically significant. The approximate 99% confidence interval is wide.  The maximum difference is at least 29 minutes in 5 of 20 replicates. 

## 17.4.2 Review and Extend Previous Work 

Management rejected the new AGV system design.  It was recognized that this design is more complex than the orginal which will require a more complex control system.  AGV utilization and congestion as well as the average load delivery time were about the same for either design.  The possible increase in maximum delivery time was of concern. 

17-15 

## 17.4.3 Implement the Selected Solution and Evaluate 

The original system configuration with three AGV’s will be implemented and the maximum time to move a load monitored. 

## _17.5 Summary_ 

The modeling and analysis of an AGV system design has been discussed in this chapter.  The use of the graphical representation of the pathways traveled by the AGV’s as data input to a simulation model has been presented.  The conflict between improving response time to load movement requests and congestion by increasing the number of AGV’s in the system has been examined.  The need to confirm designs developed using analytic methods through simulation has been illustrated. 

## **Problems** 

1. Compare and contrast the approach to modeling conveyors discussed in chapter 16 with the approach to modeling AGV systems presented in this chapter. 

2. Tell why bi-directional AGV movement on a path is not desirable. 

3. Tell why the dropoff point for a workstation should preceed the pickup point. 

4. Visit a manufacturing facility and observe the automated material handling equipment that is in use. 

5. Make a list of the automated material handling equipment you have observed in the service systems you encounter regularly. 

6. List the advantages and disadvantages of adding additional AGV’s to a system. 

7. List the advantages and disadvantages of having distinct pickup and dropoff points at each workstation versus having a single pickup-dropoff point. 

8. Consider the following modification to the original configuration with pickup and dropoff points on the main AGV path.  All AGV’s return to a parking area where maintenance and recharging is performed immediately after completing the movement of a load.  Assess this design. 

9. Consider the following modification to the new system configuration with pickup and dropoff points within each department.  The pickup and dropoff points for each station are the same.  Assess this design. 

10. Reassess each design proposed in this chapter for the case where the time between request to move loads is exponentially distributed with mean 90 seconds. 

11. Generate a customized trace of events and state variable values for the new design to determine why the maximum time to move a load sometimes becomes large. 

17-16 

## **Case Problem** 

Consider the following manufacturing system described in Askin and Standridge (1993) and shown in Figure 17-5.  There are five departments.  Material movement between departments is performed using an AGV system. 

Material flow volumes between departments per eight hour day are shown in the following table. 

## **Material Flow Volumes Between Departments per 8 Hour Day** 

|**From/To**|**1**|**2**|**3**|**4**|**5**|**Total**<br>**From**|
|---|---|---|---|---|---|---|
|**1**||10|25|||35|
|**2**|||10||25|35|
|**3**|15|||10||25|
|**4**||40|||20|60|
|**5**|24|10||50||84|



Note that each department uses the same point for dropoffs and pickups.  AGV travel time is 3 feet/second.  Assume that the sequence of interdepartmental moves is essentially random but that the time between move requests can be modeled as a constant value. 

17-17 

Each department is 30 feet by 30 feet in size except department 1 which is 30 feet by 60 feet. Pickup and dropoff times are 15 seconds. 

The problem is to determine the routes taken by AGV’s between each pair of stations.  In addition, the number of AGV’s required in this system as well as the effectiveness of the system as measured by the time from the request to move a load until load movement is completed must be determined.  Both the average and maximum times are of interest. 

If the AGV system as designed proves ineffective, it may be improved by moving pickup and dropoff points.  The redesign could include having separate pickup and dropoff point.  A new AGV path could be defined as well. 

The simulation study should answer the following questions: 

1. Is one AGV sufficient for the current demand or are two AGV’s necessary? 

2. If demand increases uniformly across all stations by 20%, what adjustments to the system are necessary? 

Case Problem Issues 

1. Can the same model developed in this chapter be used as is or slightly modified to apply to the case problem?  What would the modifications be? 

2. What alternative AGV paths should be considered? 

3. For each department, what pickup and dropoff point locations should be considered? 

4. Are there any other performance measures besides load movement time and AGV utilization that could be important? 

5. How will verification and validation evidence be obtained? 

6. What is the expected number of AGV’s required? 

7. 

- How will the arrival of load movement requests be modeled? 

17-18
