---
title: "Chapter 7"
book: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li"
source_pdf: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li.pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 7** 

## **Serial Lines** 

## _7.1 Introduction_ 

A workstation performs one, or one set of, operations on an item.  Multiple workstations are required to perform all operations necessary to produce a finished product or perform a required service.  Suppose one, or at most a few, types of items need to be processed and that this can be accomplished by processing all items in the same sequence.  In this case, a set of single workstations organized into a serial line is appropriate, possibly with a material handling device moving items between the workstations. 

In Figure 7-1, a material handling device such as a conveyor lies between seven workstations that comprise a serial line.  Items enter at the far left and depart at the far right.  Each workstation in left to right sequence performs particular operations on the item.  A finished product leaves the system after completing the operation at the right most workstation. 

**==> picture [391 x 67] intentionally omitted <==**

**Figure 7-1:  Typical Serial Line** 

An assembly line is one kind of serial system that typically employ human workers.  A transfer line is another type of serial system whose workstations consist of automatic machines with a common control system. 

In a lean system, the work to be done in processing an item would be balanced between the workstations.  The the average operating time at each workstation should be as close to the same as possible.  However, it is possible that these average times vary or due to random variation the processing time for an individual part varies between the workstations and the operation time for different parts vary at any particular workstation. 

Thus when a workstation completes its operation on an item, the following workstation may still be processing another item.  By placing the completed item in a buffer between the stations, the preceding workstation may begin processing another item.  If the buffer is full, the preceding station has no where to place the completed item and cannot begin working on another.  In this case, the workstation is in the BLOCKED state.  Time in the BLOCKED state is unproductive and may increase lead time.  Preventing blocking requires buffer space that may be scarce (or a reduction in variability).  Thus, minimizing lead time and minimizing buffer between workstations space trade off against each other. 

## _7.2 Points Made in the Case Study_ 

This application study shows how the trade-off between competing factors such as minimizing lead time and minimizing buffer space can be assessed using simulation. 

Generally accepted analytic and experimental results are applied in the design of a first simulation experiment.  Justification for using equally sized buffers is based on these results.  Performance measure values from this first experiment are used in designing additional experiments. 

7-1 

Sometimes a statistically significant improvement in system performance is not operationally meaningful.  Doubling the buffer size leads to a small reduction in lead time.  Though statistically significant, the amount of the increase is not operationally meaningful. 

The benefit of evolving new models from existing models is shown.  Models of serial systems are evolved from the model of the single workstation presented in chapter 6. 

## _7.3 The Case Study_ 

In this application study, we consider a serial line where it is essential to minimize buffer space between workstations without compromising lead time. 

## 7.3.1 Define the Issues and Solution Objective 

A new three workstation serial line process is being designed for an electronics assembly manufacturing system.  The line produces one type of circuit card with some small design differences between cards allowed.  The line must meet a lead time requirement that is yet undetermined.  Circuit cards are batched into relatively large trays for processing before entering the line. 

Only a small amount of space is available in the plant for the new line, so inter-station buffer space must be kept to a minimum.  A general storage area with sufficient space can be used for circuit card trays prior to processing at the first workstation.  Engineers are worried that the small inter-station buffer space will result in severe blocking that will prevent the lead time target from being reached.  The objective is to determine the relationship between buffer size and lead time noting the amount of blocking that occurs.  This knowledge will aid management in determining the final amount of buffer space to allocate.  Management demands that production requirements be met weekly.  Overtime will be allowed if necessary. 

The layout of the line is shown in Figure 7-2.  A single circuit card is used to represent a tray.  All cards in the tray are processed simultaneously by each machine.  Three circuit card trays are shown waiting in the general storage area for the solder deposition station, which is busy.  The component placement station is idle and its buffer is empty.  The solder reflow station is busy with one circuit card tray waiting. 

The time between the arrival of circuit card trays to the first workstation is exponentially distributed with mean 3.0 minutes.  The processing time distribution is the same at each workstation: uniformly distributed between 0.7 and 4.7 minutes.[1] This indicates that the line is balanced, as it should be. 

> 1 Alternatively, some simulation languages such as Automod express the uniform distribution as mean and half range instead of minimum and maximum.  Thus, a uniform distribution between 0.7 and 4.7 can be equivalently expressed as 2.7 ± 2.0. 

7-2 

## 7.3.2 Build Models 

The model of the serial system includes the arrival process for circuit cards, operations at the three stations, and tray movement into and out of the two inter-station buffers. 

There are four entity attributes.  One entity attribute is arrival time to the system, ArrivalTime.  The other three entity attributes store the operation times for that particular entity at each station. 

Assigning all operating times when the entity arrives assures that the first entity has the first operating time sample at each station, the second the second and so forth.  This assignment is the best way to ensure that the use of common random numbers is most effective in reducing the variation between system alternative scenarios, which aids in finding statistical differences between the cases.  In general, the nth arriving entity may not be the nth entity processed at a particular station.  In the serial line model, this will be the case since entities can’t “pass” each other between stations. 

The processing of a circuit card tray at the deposition station is done in the following way.  A circuit card tray uses the station when the latter becomes idle.  The operation is performed.  The circuit card tray then must find a place in the inter-station buffer before leaving the deposition station.   Thus, the deposition station enters the blocked state until the circuit card tray that has just been processed enters the inter-station buffer.  Then the station enters the idle state.  This logic is repeated for the placement station.  The tray departs the line following processing at the reflow station. 

The pseudo-English for the model follows.  Note that there is one process for arriving entities, one for departing entities and one for each of the three workstations. 

7-3 

|// Serial Line Model|||
|---|---|---|
|Define Arrivals:|||
|Time of first arrival:|0||
|Time between arrivals:|Exponentially distributed with a mean of 3 minutes||
||Exponential (3) minutes||
|Number of arrivals:|Infinite||
|Define Resources:|||
|WS_Deposition/1|with states (Busy, Idle, Blocked)||
|WS_Placement/1|with states (Busy, Idle, Blocked)||
|WS_Reflow/1|with states (Busy, Idle)||
|WS_BufferDP/?|with states (Busy, Idle)||
|WS_BufferPR/?|with states (Busy, Idle)||
|Define Entity Attributes:|||
|ArrivalTime|// part tagged with its arrival time; each part has its own tag||
|OpTimeDes|// operation time at deposition station||
|OpTimePlace|// operation time at placement station||
|OpTimeReflow|// operation time at reflow station||
|Process Arrive|||
|Begin|||
|Set ArrivalTime = Clock||// record time part arrives on tag|
|Set OpTimeDes|= uniform(0.7, 4.7)2<br>// set operations times at each station||
|Set OpTimePlace|= uniform(0.7, 4.7)||
|Set OpTimeReflow|= uniform(0.7, 4.7)||
|Send to Process Deposition||// start processing|
|End|||
|Process Deposition|||
|// Deposition Station|||
|Begin|||
|Wait until WS_Deposition/1 is Idle in Queue Q_Deposition  // wait its turn on the machine|||
|Make WS_Depostion/1|Busy|// tray starts turn on machine; machine is busy|
|Wait for OpTimeDes minutes||// tray is processed|
|Make WS_Deposition/1|Blocked|// tray is finished; machine is Blocked|
|Wait until WS_BufferDP/1 is Idle||// wait for interstation buffer space|
|Make WS_Deposition/1|Idle|// free deposition machine|
|Send to Process Placement||// Send to placement machine|
|End|||
|Process Placement|||
|// Placement Station|||
|Begin|||
|Wait until WS_Placement/1 is Idle||// wait its turn on the machine|
|Make WS_BufferDP/1  Idle||// leave interstation buffer|
|Make WS_Placement/1|Busy|// tray starts turn on machine; machine is busy|
|Wait for OpTimePlace minutes||// tray is processed|
|Make WS_Placement/1|Blocked|// tray is finished; machine is Blocked|
|Wait until WS_BufferPR/1 is Idle||// wait for interstation buffer space|
|Make WS_Placement/1|Idle|// free placement machine|



> 2 In Automod this would be written using the midpoint, half-range style: uniform 2.7, 2.0 

7-4 

Send to Process Reflow 

// Send to reflow machine 

End Process Reflow // Reflow Station Begin Wait until WS_Reflow1 is Idle // wait its turn on the machine Make WS_BufferPR/1  Idle // leave interstation buffer Make WS_Reflow/1 Busy // tray starts turn on machine; machine is busy Wait for OpTimeReflow minutes // tray is processed Make WS_Reflow/1 Idle // free placement machine Send to Process Depart // Send to reflow machine End Process Depart Tabulate (Clock-ArrivalTime) in LeadTime // keep track of part time on machine End 

## 7.3.3 Identify Root Causes and Assess Initial Alternatives 

The experiment design is summarized in Table 7-1. 

**Table 7-1:  Simulation Experiment Design for the Serial System** 

|**Element of the Experiment**|**Values for This Experiment**|
|---|---|
|Type of Experiment|Terminating|
|Model Parameters andTheir Values|Size ofeachbuffer --(1,2,4, 8,16)|
|Performance Measures3|1.  Lead Time<br>2.  Percent blocked time depostion station<br>3.  Percent blocked time placement station|
|Random Number Streams|1.  Time between arrivals<br>2.  Operation time deposition station<br>3.  Operation time placement station<br>4.Operationtimereflowstation|
|Initial Conditions|1 circuit card tray in each inter-station buffer with the<br>following stationbusy|
|Numberof Replicates|20|
|Simulation EndTime|2400minutes (oneweek)|



Since management assesses production weekly, a terminating experiment with a simulation time interval of one week was chosen.  The size of each of the two buffers is of interest.  Note that the workstations in this study have the same operation time distribution, indicating that the line is balanced as it should be.  Analytic and empirical research have shown that for serial systems whose workstations have the same operation time distribution that buffers of equal size are preferred (Askin and Standridge, 1993; Conway et al., 1988). 

There was some debate as to whether throughput, WIP, or lead time should be the primary performance measure.  Since all circuit card trays that arrive also depart eventually the throughput rate in-bound to the system is the same as the throughput rate out-bound from the system, at least in the long term.  Note that by Little’s Law, the ratio of the WIP to the lead time (LT) is equal to the (known) throughput rate.  Thus, either the total WIP, including that preceding the first workstation, or the lead time could be measured. 

3 The problems at the end of the chapter reference the performance measures not discussed in the text. 

7-5 

The lead time is easy to observe since computing it only requires recording the time of arrivals as a entity attribute.  Thus, the lead time can be computed when a entity leaves the system. Computing the WIP requires counting the number of entities within the line.  This also is straightforward.  We will choose to compute the lead time for this study. 

Buffer size is the model parameter of interest.  The relationship between buffer size and lead time is needed.  Thus, various values of buffer size will be simulated and the lead time observed. Average lead time is one performance measure statistic of interest along with the percent blocked time of each station. 

There are four random variables in the model, the time between arrivals and three operation times, with one stream for each.  The simulated time interval is the same as the management review period for production, one week.  Twenty replicates will be made.  Since the utilization of the stations is high, a busy station with one circuit card tray in the preceding inter-station buffer seems like a typical system state.  Thus, the initial conditions were determined. 

Verification and validation evidence were obtained from a simulation experiment with the interstation buffer size set to the maximum value in the experiment, 16.  Results show almost no blocking in this case.  Verification evidence consists of balancing the number of arrivals with the number of departures and the number remaining in the simulation at the end of the run for one replicate.  These values are shown in Table 7-2. 

**Table 7-2:  Verification Evidence for Replicate 1** 

||**Circuit Trays**<br>**Arriving**|**Circuit Trays Departing or**<br>**Remaining at the end**<br>**of the Simulation **|
|---|---|---|
|Initialconditions|6||
|Arrivalprocess|794||
|Completed processing||785|
|Inbuffers||12|
|Inprocessing||3|
|Total|800|800|



Validation evidence is obtained by comparing the percent busy time of the deposition station as estimated from the simulation results with the expected value computed as follows.  The average operation time is (0.7 + 4.7)/2 = 2.7 minutes.  The average time between arrivals is 3 minutes. Thus, the expected percent busy time is 2.7 / 3.0 = 90%.  The approximate 99% confidence interval for the true percent busy time computed from the simulation results is 86.7 % - 91.7%. Since this interval contains the analytical determined busy time value, validation evidence is obtained. 

Since the other stations can be blocked, their percent busy time is not as straightforward to compute analytically.  Thus, validation evidence with regard to the deposition and placement stations is more difficult to obtain. 

Simulation results for the various values of inter-station buffer capacity will be compared and differences noted.  Statistical analysis will be performed to confirm differences that affect what buffer capacity is chosen.  Table 7-3 shows the average lead time for each buffer capacity for each replicate as well as summary statistics. 

7-6 

**Table 7-3:  Average Lead Time Summary (minutes)** 

|||Buffer Capacity|Buffer Capacity|Buffer Capacity||
|---|---|---|---|---|---|
|Replicate|1|2|4|8|16|
|1|75.4|46.3|36.6|33.9|33.2|
|2|121.3|65.7|40.9|38.2|38.1|
|3|97.7|66.8|48.6|39.6|39.4|
|4|41.5|29.9|25.1|25.0|25.0|
|5|45.8|27.5|23.6|23.5|23.5|
|6|93.7|45.8|28.9|27.9|27.9|
|7|47.1|35.6|29.1|28.2|28.2|
|8|36.5|24.6|21.8|21.7|21.7|
|9|45.2|28.5|25.3|25.0|25.0|
|10|52.1|26.7|23.6|23.1|23.1|
|11|137.2|87.4|57.6|48.8|48.8|
|12|102.6|44.9|36.1|34.1|34.1|
|13|70.6|41.3|28.8|26.9|26.9|
|14|44.7|33.9|26.9|25.5|25.5|
|15|97.4|54.6|35.0|30.9|30.4|
|16|46.9|29.9|27.1|26.4|26.4|
|17|39.1|31.6|28.5|27.2|27.2|
|18|95.9|69.7|51.6|43.4|43.4|
|19|28.7|23.5|21.9|21.9|21.9|
|20|80.2|44.5|35.0|34.0|34.0|
|Average|70.0|42.9|32.6|30.3|30.2|
|Std. Dev.|31.5|17.7|10.2|7.5|7.5|
|99% CI<br>Lower Bound|49.8|31.6|26.1|25.5|25.4|
|99% CI<br>Upper Bound|90.2|54.3|39.1|35.1|35.0|



Figure 7-3 shows a graph of the average time in the system versus the buffer capacity.  From Table 7-3 and Figure 7-3 it is easily seen that the average time in the system decreases significantly when the buffer capacity is increased from 1 to 2 as well as from 2 to 4.  Smaller decreases are seen when the buffer capacity is increased further.  The statistical significance of these latter differences will be determined. 

7-7 

**Figure 7-3:  Average Time in the System versus Buffer Capacity** 

The minimum possible average time in the system is the sum of the average processing times at each station 2.7 + 2.7 + 2.7 = 8.1 minutes.  Note that for buffer sizes of 4, 8, and 16, the average time in the system is 4 to 5 times the minimum average cycle time.  This is due to the high degree of variability in the system: exponential arrival times and uniformly distributed service times with a wide range as well as the high utilization of the work stations.  This result is consistent with the VUT equation that shows that the lead time increases as the variability of the time between arrivals, the variability of the service time, and the utilization increase. 

The paired-t method is used to compute approximate 99% confidence intervals for the average difference in lead time for selected buffer sizes.  These results along with the approximate 99% confidence intervals for the average lead time for each buffer size are shown in Table 7-4.  Note that average lead time reduction using 16 buffers instead of 8, is not statistically significant since the approximate 99% confidence interval for the difference in average lead time contains 0. 

Table 7-5 summarizes the percent blocked time for the deposition station as well as the differences in percent block time including paired-t confidence intervals for the mean difference for neighboring values of buffer sizes of interest. 

The percentage of time that the deposition station is blocked decreases as the buffer size increases as would be expected.  The paired-t confidence interval for the difference in percentage of blocked time for 16 buffers versus 8 buffers does not contain 0.  Thus, the reduction in percent blocked time due to the larger buffer size is not statistically significant.  Further note that the 99% confidence intervals for the percent of time blocked for the case of 8 and 16 buffers both contain 0.  Thus, the percent of blocked time for these cases is not significantly different from zero. 

7-8 

**Table 7-4: Paired t Test for Average Lead Time (minutes)** 

||||Buffer Capacity|Buffer Capacity||
|---|---|---|---|---|---|
|Replicate|4|8|Diff 4 - 8|16|Diff 8 -16|
|1|36.6|33.9|2.7|33.2|0.7|
|2|40.9|38.2|2.7|38.1|0.1|
|3|48.6|39.6|9.0|39.4|0.3|
|4|25.1|25.0|0.2|25.0|0.0|
|5|23.6|23.5|0.1|23.5|0.0|
|6|28.9|27.9|0.9|27.9|0.0|
|7|29.1|28.2|0.9|28.2|0.0|
|8|21.8|21.7|0.1|21.7|0.0|
|9|25.3|25.0|0.4|25.0|0.0|
|10|23.6|23.1|0.5|23.1|0.0|
|11|57.6|48.8|8.9|48.8|0.0|
|12|36.1|34.1|2.0|34.1|0.0|
|13|28.8|26.9|1.9|26.9|0.0|
|14|26.9|25.5|1.4|25.5|0.0|
|15|35.0|30.9|4.1|30.4|0.5|
|16|27.1|26.4|0.7|26.4|0.0|
|17|28.5|27.2|1.3|27.2|0.0|
|18|51.6|43.4|8.2|43.4|0.0|
|19|21.9|21.9|0.0|21.9|0.0|
|20|35.0|34.0|1.0|34.0|0.0|
|Average|32.6|30.3|2.34|30.2|0.08|
|Std. Dev.|10.2|7.5|2.92|7.5|0.19|
|99% CI<br>Lower Bound|26.1|25.5|0.47|25.4|-0.04|
|99% CI<br>Upper Bound|39.1|35.1|4.21|35.0|0.21|



7-9 

**Table 7-5:  Paired-t Confidence Intervals for Deposition Percent Blocked Time** 

||||Buffer Capacity|Buffer Capacity||
|---|---|---|---|---|---|
|Replicate|4|8|Diff 4 - 8|16|Diff 8 -16|
|1|2.51%|1.11%|1.41%|0.00%|1.11%|
|2|1.57%|0.00%|1.57%|0.00%|0.00%|
|3|1.12%|0.29%|0.83%|0.00%|0.29%|
|4|0.84%|0.00%|0.84%|0.00%|0.00%|
|5|0.53%|0.00%|0.53%|0.00%|0.00%|
|6|1.48%|0.11%|1.37%|0.00%|0.11%|
|7|2.19%|0.00%|2.19%|0.00%|0.00%|
|8|0.69%|0.00%|0.69%|0.00%|0.00%|
|9|0.66%|0.10%|0.56%|0.00%|0.10%|
|10|0.49%|0.00%|0.49%|0.00%|0.00%|
|11|3.62%|1.65%|1.96%|0.20%|1.45%|
|12|0.90%|0.00%|0.90%|0.00%|0.00%|
|13|0.61%|0.00%|0.61%|0.00%|0.00%|
|14|1.33%|0.12%|1.21%|0.00%|0.12%|
|15|1.46%|0.12%|1.33%|0.00%|0.12%|
|16|1.30%|0.29%|1.01%|0.00%|0.29%|
|17|0.69%|0.16%|0.53%|0.00%|0.16%|
|18|2.74%|1.26%|1.47%|0.17%|1.09%|
|19|0.66%|0.10%|0.57%|0.00%|0.10%|
|20|2.35%|0.42%|1.92%|0.00%|0.42%|
|Average|1.39%|0.29%|1.10%|0.02%|0.27%|
|Std. Dev.|0.87%|0.48%|0.53%|0.06%|0.43%|
|99% CI Lower<br>Bound||-0.02%|0.76%|-0.02%|-0.01%|
|99% CI Upper<br>Bound||0.59%|1.44%|0.06%|0.54%|



## 7.3.4 Review and Extend Previous Work 

System experts reviewed the results developed in the previous section.  They concluded that a buffer size of four should be used in the system.  The small, approximately 10%, decrease in average lead time obtained with a buffer size of 8 did not justify the extra space.  The difference was statistically significant in the simulation experiment.  The average percent blocked time for the deposition station is about 1.4% percent for a buffer size of 4. 

It was noted that for some replicates the average lead time was near an hour.  This was of some concern. 

## 7.3.5 Implement the Selected Solution and Evaluate 

The system was implemented with 4 buffers.  Average lead will be monitored.  Causes of long average lead time will be identified and corrected. 

7-10 

## _7.5 Summary_ 

The model of a serial line is evolved from the model of a single workstation.  Analytic results are employed in designing simulation experiments.  Simulation results help in selecting the interstation buffer sizes to use in the serial system and thus help ensure that the system is as lean as possible upon implementation. 

## **Problems** 

1. Based on the simulation experiment results that follow for one replicate of the simulation in section 7.3.1 with a buffer size of 4, verify that the number of entities entering the system are all accounted for at the end of the simulation. 

|Number of entities created through the arrival process:|807|
|---|---|
|Number of entities created through initial conditioins:|6|
|Number of entities completing processing at the solder deposition station:|808|
|Number of entities completing processing at the component placement station:|804|
|Number of entities completing processing at the solder reflow station:|799|
|Number of entities waiting for the deposition station resource||
|at the end of the simulation:|2|
|State of the deposition station resource at the end of the simulation:|Busy|
|Number of entities waiting for the placement station resource||
|at the end of the simulation:|5|
|State of the placement station resource at the end of the simulation:|Busy|
|Number of entities waiting for the reflow station resource||
|at the end of the simulation:|4|
|State of the reflow station resource at the end of the simulation:|Busy|



2. Based on the simulation results presented in this chapter, provide an argument for using 8 buffers instead of 4. Without simulation would a lean team have been more inclined to use a larger buffer size due to a lack of information? 

3. Complete the following table of the percentage blocked times for the placement station for the simulation in section 7.3.  What statistically significant results are obtained?  How do these compare to the lead time and percent blocked time for the deposition station results? 

## **Percent Blocked Time the Placement Station** 

|**Buffer Size**|**Buffer Size**|**Buffer Size**|**Buffer Size**|**Buffer Size**|**Buffer Size**|
|---|---|---|---|---|---|
|**Replication**|<br>**4**|<br>**8**|<br>**8-4**|<br>**16**|<br>**16-8**|
|1|<br>2.78|1.32||0.00||
|2|<br>1.85|0.19||0.00||
|3|<br>1.90|0.00||0.00||
|4|<br>2.12|<br>0.52||0.00||
|5|<br>1.28|0.00||0.00||
|6|<br>1.48|0.09||0.00||
|7|<br>1.88|0.40||0.00||
|8|<br>1.57|<br>0.14||0.00||
|9|<br>1.01|<br>0.00||0.00||
|10|<br>2.29|0.00||0.00||
|**Average **||||||
|**Std. Dev.**||||||
|**99% CI Lower Bound**||||||
|**99% CI Upper Bound**||||||



7-11 

4. Develop and compute the results from an analytic model of the serial line using the 2 

equations in chapter 6.  Note that the equation for cd gives the squared co-efficient of variation of the time between arrivals to the next workstation.  Assume no blocking of workstations. 

5. Develop and implement in a simulation environment a model of a the system described in the manufacturing case problem below but assuming that the system will have all the space that is needed between stations.  This means that modeling the interstation buffers is not necessary.  Note that a single workstation is simply a serial line with one station. Verify the model. 

6. Develop a model of a fast food restaurant that works as follows.  The time between customer arrivals is exponentially distributed with mean 0.5 minutes.  If the line is longer than 20, an arriving customer goes somewhere else to eat.  A customer places an order and pays the cashier.  The time to order and pay is uniformly distributed between 0.25 and 0.45 minutes.  Next the customer waits for the food gatherer to prepare the order. This time is exponentially distributed with mean 0.4 minutes.  There is space for only two people who have ordered and paid to wait for the food gatherer.  Finally, the customer waits for the drink dispensing machine.  The time to get a drink is 0.4 minutes.  Develop a process model of this situation. 

7. Design and perform an experiment to determine if reallocating the 8 total buffer spaces so that more were in front of the reflow station and less were in front of the placement station would decrease part time in the system. 

## **Case Problems** 

## _Manufacturing_ 

A new serial system consists of three workstations in the following sequence: mill, deburr, and wash.  There are buffers between the mill and the deburr stations and between the deburr and the wash stations.  It is assumed that sufficient storage exists preceding the mill station.  In addition, the wash station jams frequently and must be fixed.  The line will serve two part types.  The production requirements change from week to week.  The data below reflect a typical week.  You have been assigned the task of finding the minimum buffer space that doesn't significantly effect lead time. 

Relevant data are as follows with all times in minutes: 

Time between arrivals - Part type 1: Exponentially distributed with mean 2.0 Part type 2: Exponentially distributed with mean 3.0 Time at the mill station - Part type 1: 0.9 Part type 2: 1.4 Time at the deburr station - Uniform (0.9, 1.3) for each part type Time at wash station - 1.0 for each part type Time between wash station jams - Exponentially distributed with mean 30.0 Time to fix a wash station jam - Exponentially distributed with mean   3.0 

Embellishment:  In the meeting to review your work, it is suggested that the two buffers may be of different sizes but the total amount of buffer space used should not increase.  Perform the appropriate simulation experiment. 

7-12 

## Case Problem Issues 

1. Discuss how arrivals to the system will be modeled. 

2. Discuss how verification evidence will be obtained. 

3. Discuss how validation evidence can be obtained. 

   - a. Compute the expected number of arrivals of each type. 

   - b. Compute the expected number of arrivals per hour of both types together. 

   - c. Compute the utilization of each workstation. 

4. List the important performance measures. 

5. What initial conditions should be used? 

6. For the simulation language that you are using, discuss how to implement the initial conditions. 

7. List the buffer sizes to consider in the simulation experiment and tell why these sizes were chosen. 

8. (Embellishment)  Discuss whether it is better to have more buffer space between the mill and the deburr station to avoid blocking at the front of the line or to have buffer space between the deburr and the wash stations to avoid blocking at the deburr station when the wash station jams. 

Terminating experiment: Use an end time of 168 hours. 

_Service System_ 

Consider the design of the drive through service area of a fast food restaurant.  There are three stations:  place order, pay cashier, and pick up food.  There is sufficient space for cars preceding the place order station.  Your job is to determine the amount of space between the place order and pay cashier stations as well as the pay cashier and pick up food stations in terms of the number of cars.  Serving the maximum number of customers possible during the lunch period, 11:00 A.M. to 1:00 P.M., is management’s objective.  Thus, minimal customer lead time must be achieved.  Based on previous experience, customers are classified into types, depending on the size of their order. 

Relevant data are as follows with all times in minutes: 

|Time between arrivals --|Customer type 1:|Exponentially distributed with mean 1.0|
|---|---|---|
||Customer type 2:|Exponentially distributed with mean 1.5|
|Time at the order station --|Customer type 1:|Exponentially distributed with mean 0.45|
||Customer type 2:|Exponentially distributed with mean 0.70|



Time at the pay station - Uniform (0.45, 0.65) for each customer type 

Time at pickup station -- 0.5 for each customer type 

Embellishment:  In the meeting to review your work, it is suggested that the two buffers may be of different sizes but the total amount of buffer space used cannot increase due to physical constraints.  Perform the appropriate simulation experiments. 

7-13 

Case Problem Issues 

1. Discuss how arrivals to the system will be modeled. 

2. Discuss how verification evidence will be obtained. 

3. Discuss how validation evidence can be obtained. 

   - a. Compute the expected number of arrivals of each type. 

   - b. Compute the expected number of arrivals per hour of both types together. c. Compute the utilization of each workstation. 

4. List the important performance measures. 

5. What initial conditions should be used? 

6. For the simulation language that you are using, discuss how to implement the initial conditions. 

7. List the buffer sizes to consider in the simulation experiment and tell why these sizes were chosen. 

7-14
