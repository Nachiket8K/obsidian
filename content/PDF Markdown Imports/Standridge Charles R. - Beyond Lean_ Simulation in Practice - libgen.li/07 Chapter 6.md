---
title: "Chapter 6"
book: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li"
source_pdf: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li.pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 6** 

## **The Workstation** 

## _6.1 Introduction_ 

Previously, the effect on part lead time when the current machine at a workstation was replaced with a new machine with less variance in operating time was studied.  In this chapter, a more extensive study of a single workstation is performed using both analytic and simulation models in a complementary fashion.  The effects of operational detractors, batching with setup, machine downtime, and part reworking are analyzed.  Again, such a study can be done before a new machine is acquired to help validate the future state in a lean transformation.  The workstation operates on one independently identifiable part at a time.  The part resides in an input buffer while waiting for processing. 

## _6.2 Points Made in the Case Study_ 

This case shows how a new workstation, that is a part of a lean transformation, can be studied and its operation validated before implementation by using a combination of analytic and simulation models. 

The results of the analytic models are compared to the results of the simulation models to provide validation evidence for the simulation models. 

The use of models to quantify performance using both average and maximum values is shown. 

The average time between arrivals to a workstation should be equal to the takt time in order to produce the quantity of product demanded by a customer.  Variation could result in the time between arrivals being greater than the takt time for any particular part.  This could have a short term negative impact on the ability to meet customer demands. 

The average processing time at a workstation must be less than the takt time in order to produce the quantity of product demanded by a customer.  Variation could result in the processing time being greater than the takt time for some items.  This could have a short term negative impact on the ability to meet customer demands. 

The iterative nature of the simulation process is shown.  A review of the initial study of the workstation leads to a request to include the three detractors in the simulation study, both individually and in combination.  These detractors are batching with setup, breakdowns, and rejection and rework of a completed part. 

Statistical analysis is used to determine if the detractors have a significant effect on the lead time at the workstation when the detractors are present. 

## _6.3 The Case Study_ 

The case study shows the process of using simulation and analytic models together to address issues concerning a new workstation before acquisition and implementation. 

## 6.3.1 Define the Issues and Solution Objective 

A lean team has been studying the operation of a particular workstation.  A replacement machine with less variation in processing time, but the same average processing time, has been proposed as a part of a future state definition.  Management is requiring a study to determine the average and maximum lead times at the workstation if the replacement machine is acquired. 

6-1 

The workstation operates 168 hours per month.  Customer demand per month is 1680 parts or 10 parts per hour, resulting in a takt time of 6 minutes.  The processing time for the new machine is triangularly distributed with a mean of 5 minutes, a minimum of 3 minutes and a maximum of 8 minutes.  Thus, the mode is 4 minutes.  (See the discussion in chapter 3 for the computation of the mode.)  Inbound arrival of parts is not well controlled, which will be modeled using the practical worst case: Exponentially distributed with a mean equal to the takt time of 6 minutes. 

## 6.3.2 Build Models 

The model in pseudo-English is shown below. 

Define Arrivals: // mean must equal takt time Time of first arrival: 0 Time between arrivals: Exponentially distributed with a mean of 6 minutes Exponential (6) minutes Number of arrivals: Infinite // Note: The average number of arrivals is 1680 Define Resources: WS/1 with states (Busy, Idle) Define Entity Attributes: ArrivalTime // part tagged with its arrival time; each part has its own tag Process Workstation Begin Set ArrivalTime = Clock // record time part arrives on tag Wait until WS/1 is Idle in Queue QWS // part waits for its turn on the machine Make WS/1 Busy // part starts turn on machine; machine is busy Wait for Triangular (3, 4, 8) minutes // part is processed Make WS/1 Idle // part is finished; machine is idle Tabulate (Clock-ArrivalTime) in LeadTime // keep track of part time on machine End 

The definitions tell about arrivals, the machine including its states, and the entity (part) attributes. The comments (denoted by //) describe the steps the part goes through for processing on the machine as well as recording the arrival time and tabulating its individual lead time just before departure. 

## 6.3.3 Identify Root Causes and Assess Initial Alternatives 

In this section, the simulation experimental design and results are presented.  First, an analytic model of the single work station is discussed in the next section. 

## 6.3.3.1 Analytic Model of a Single Workstation 

The time between arrivals is characterized by both a mean, Ta, and by a standard deviation, a and the processing time is characterized by both its mean CT and by its standard deviation, T. The coefficient of variation of the time between arrivals is ca = a / Ta.  The coefficient of variation of the processing time is cT = T / CT. 

The average number of parts in the buffer is WIPq and WIPq plus the utilization of the machine (equal the average number of parts in processing) is the WIP. 

The average time spent at the workstation can be broken into two parts: the average time in processing, CT, and the average time in the buffer, CTq. Their sum is the total is the lead time LT. 

6-2 

The relationship between WIP, lead time and throughput is known as Little’s Law. 

Work in process (WIP) = Throughput (TH) X Lead Time (LT) 

(6-1) 

Examples: 

Number of parts at a workstation = Parts completed per hour at the work station X Total time at the workstation 

Number of customers at Burger King =  Customers served per hour at Burger King X Time from entry to completion of service at BK 

Number of pallets on a holding conveyor = Pallets entering the main line conveyor per hour X Time till entry to the holding conveyor to entry to the main line conveyor 

Number of units in a transfer center = Number of units entering the transfer center per hour X Average processing time in the transfer center 

Number of students enrolled at GVSU = Number of students entering per year X Average number of years enrolled at GVSU 

Here are some ideas that can be extracted from Little’s Law. 

1. In order for the WIP (a bad thing to have lots of) to decrease, either the throughput must decrease (for a constant lead time) or the cycle time must decrease for a constant throughput.  Since throughput often depends on requirements for finished goods and is the reciprocal of the takt time, decreasing lead time is most likely necessary to decrease WIP. 

2. Another way of writing Little’s Law is TH = WIP / LT.  This means that increasing throughput can be achieved by increasing WIP or decreasing LT.  However, increasing WIP (a bad thing to have lots of) may increase lead time.  Thus, increasing throughput most often requires decreasing lead time.  Note that the same throughput can be achieved with large WIP and large lead times or small WIP and small lead times. 

3. A third way of writing Little’s Law is LT = WIP / TH.  Decreasing LT can be achieved by decreasing WIP or increasing throughput if the WIP does not increase. 

Next we will consider all of the information that can be computed about the behavior of a single workstation that has one machine or one worker.  We will include **means and variances** in evaluating **average** behavior.  Notice that variation in measures of behavior is not, an often cannot, be determined analytically. 

Consider the workstation shown in Figure 6-1, with computed quantities shown in **boldface** . Quantities that are known are the time between arrivals (mean and variance) as well as the processing time (mean and variance).  Quantities that can be computed are: 

1. time in the input buffer of the station (CTq) 

2. lead time at the station (LT) 

3. average number of parts in the input buffer (WIPq) 

4. average number of parts at the station (WIP) 

5. utilization of the station, the percent of time the workstation is busy processing a part.  

6. time between departures (mean and standard deviation) (Td and d 

6-3 

Figure 6-1:  Computation of Workstation Quantities 

Equation 6-2 is called the VUT equation, for Variance – Utilization – Time and is used to approximate the average cycle time in the queue.  This equation is presented and further discussed in Hopp and Spearman (2007). 

**==> picture [419 x 31] intentionally omitted <==**

The following insights can be gained by examining equation 6-2. 

1. The cycle time in the buffer depends on the variance of the time between arrivals and the variance of the processing time, expressed as the squared coefficient of variation.  As the variance of either increase, the average cycle time in the queue increases.  The coefficient of variation is the standard deviation / mean. 

2. The cycle time in the buffer increases in a highly non-linear fashion as the utilization increases.  The utilization term for a utilization of 90% is 9, for a utilization of 95% is 19, and for a utilization of 99% is 99. 

3. The only way to effectively run a workstation with high utilization is to eliminate the variation in the time between arrivals and the processing time. 

4. A utilization of 100% cannot be achieved unless the variance in both the processing time and the time between arrivals is zero. 

5. The mean and the standard deviation of the exponential distribution are equal.  Thus, the coefficient of variation for an exponential distribution is equal to 1.  Thus, the “good” range for the V term is 0 to 1. 

6. The distributions of the time between arrivals and the processing times are not required, only the mean and the standard deviation. 

Once the average cycle time in the buffer is determined, the average number in the buffer can be determined using Little’s Law: 

**==> picture [420 x 27] intentionally omitted <==**

The lead time at the station is simply the cycle time in the buffer plus the processing time: 

**==> picture [65 x 10] intentionally omitted <==**

(6-4) 

6-4 

The number at the station can be obtained from equation 6-4 using Little’s Law: 

**==> picture [420 x 27] intentionally omitted <==**

The mean of the time between departures should equal the mean of the time between arrivals. This is simply a law of the conservation of parts:  All entering parts must depart.  The conservation law applies between workstations as well:  The mean and variation of the time between departures from one workstation are the same as the mean and variation of the time between arrivals to the next work station. 

The squared coefficient of determination of the time between departures is given by equation 6-6: 

**==> picture [105 x 13] intentionally omitted <==**

**==> picture [24 x 10] intentionally omitted <==**

The following insights can be gained by examining equation 6-6. 

1. The variation in the departures for a high utilization workstation depends mostly on the variation in the processing time.  Thus, a low variation processing time results in a low variation in the departures, which results in a low variation in the arrivals to the next workstation. 

2. A workstation with high utilization and low variation in processing time will, to a great extent, eliminate high variation in the time between arrivals. 

3. A workstation with high utilization and high variation in processing time will cause high variation in the time between arrivals to the next station.  Thus, the cycle time in the buffer at the next station will tend to be high. 

4. A workstation with low utilization will tend to result in the variation of the time between arrivals at the next workstation equaling the variation in the time between departures at the current workstation. 

The results from the analytic model of the workstation of interest are shown in Table 6-1. 

**Table 6-1:  Analytic Model of Workstation – Results** 

|Inputs|Average time between arrivals|6|
|---|---|---|
||Average processing time|5|
||Std. Dev. time between arrivals|6|
||Std. Dev. processing time|3|
|Utilization|Utilization|83.3%|
|Average Times|ca-- Time between arrivals|1|
||cT-- Processing time|0.6|
||Variance term|0.68|
||Utilization term|5.0|
||Average time in buffer|17.0|
||Average lead time|22.0|
|Average Number of Parts|Average number in the buffer|2.8|
||Average number at the station|3.7|
|Departure Information|Average time between departures<br>|6|
||cd<br>~~2~~-- Time between departures|0.56|



6-5 

Note that the inputs to the analysis are the average and standard deviation of the time between arrivals as well as the average and standard deviation of the processing time.  The averages are typically obtained through value stream mapping.  The standard deviations must typically be obtained through additional data collection and analysis. 

## 6.3.3.2 Simulation Analysis of the Single Workstation 

Next, the design for the simulation experiment must be specified.  This design will make use of the results of the analytic model. 

The experimental design contains the elements discussed in chapter 4.  This is a terminating simulation of duration 168 hours, the monthly planning period.  There are two streams required, one for the time between arrivals and one for the processing time.  The initial conditions are set based the results of the analytic model: 2 parts in the buffer and thus one additional part on the machine.  Lead time is the primary performance measure of interest.   Some of the other quantities computed by the analytic model are also of interest: utilization of the machine and average number of parts in the buffer.  These will be used in obtaining validation evidence for the simulation model and experiment.  Twenty replications will be performed.  There are no model parameters in the first experiment. 

In summary, the experiment design is as follows: 

**Table 6-2:  First Simulation Experiment Design for the Workstation.** 

|**Element of the Experiment**|**Values for This Experiment**|
|---|---|
|Type of Experiment|Terminating|
|Model Parameters andTheir Values|None|
|Random Number Streams|1.  Time between arrivals<br>2.Operationtime|
|Performance Measures|1.  Part lead time<br>2.  Utilization of the machine<br>3.  Number of parts waiting for the machine<br>inthe buffer|
|Numberof Replicates|20|
|Initial Conditions|2 parts in the buffer implying one part on<br>themachine|
|Simulated Time Interval<br>(Beginning time–ending time)|0 – 168 hours|



Verification evidence is obtained using the balance equation: 

Number of entities entering = 

Number of entities leaving + Number of entities remaining at the end 

The number of entities entering the model is the sum of those arriving and the initial entities. Thus for the first replicate: 

1717 + 3 = 1719 + 1. 

Thus, validation evidence is obtained. 

Table 6-3 shows the simulation results.  These results are consistent with the results from the analytic model.  The 99% confidence intervals for the utilization, the average number of parts 

6-6 

waiting at the station, and the average lead time all contain the corresponding values resulting from the analytic model.  Thus, model validation evidence is obtained. 

**Table 6-3: Simulation Results for Base Experiment** 

|Replicate|Average<br>Number<br>at Station|Average<br>Lead<br>Time|Max<br>Lead<br>Time|Utilization|
|---|---|---|---|---|
|1|3.20|18.80|74.70|0.86|
|2|2.99|18.11|79.15|0.83|
|3|3.40|20.36|83.38|0.83|
|4|3.70|21.15|61.29|0.88|
|5|2.28|14.13|54.11|0.80|
|6|2.76|16.79|61.17|0.82|
|7|3.39|20.17|75.93|0.84|
|8|2.57|15.66|60.89|0.82|
|9|3.17|18.52|79.15|0.86|
|10|3.36|20.34|97.58|0.83|
|11|2.92|16.99|60.50|0.86|
|12|4.51|26.07|104.61|0.87|
|13|3.11|18.97|81.80|0.82|
|14|2.63|16.46|67.19|0.80|
|15|3.23|18.89|75.20|0.86|
|16|2.75|16.62|90.52|0.82|
|17|2.56|15.49|62.29|0.83|
|18|2.53|15.66|68.35|0.80|
|19|5.52|31.55|138.89|0.88|
|20|4.45|25.75|129.22|0.87|
|Average|3.25|19.32|80.30|0.84|
|Std. Dev.|0.79|4.24|22.63|0.02|
|99% CI<br>Lower Bound|2.74|16.61|65.82|0.82|
|99% CI<br>Upper Bound|3.76|22.03|94.77|0.85|



## 6.3.4 Review and Extend Previous Work 

Management reviewed the simulation model and experiment, concluding that the model was a validated as a tool for assessing the future state before implementation. 

The lead time results from the models were of concern with respect to how the workstation would operate.  The average lead time was about four times the processing time.  The average maximum lead time estimated by the simulation model was about 16 times the processing time. These high values are entirely due to the variation in the arrival of inbound parts or orders (expressed by modeling the time between arrivals as exponentially distributed) as well as the variation in processing time as seen in the coefficient of variation of 0.60.  Thus, reducing this variation by identifying and addressing root causes seems fundamental to making the workstation operation leaner. 

6-7 

At the review meeting, a request was made to assess the effects of three detractors on workstation performance.  The assessment of each was to be made independently of the others. 

The nature of these detractors is discussed in the following section. 

## 6.3.4.1 Detractors to Workstation Performance 

The first detractor is breakdowns.  Breakdowns reduce the amount of available production time. A period of operation for a single machine ends in a breakdown.  The length of this period is highly variable.  Some time is needed to repair the machine, which could vary by the type of breakdown.  This breakdown-repair cycle repeats as shown in Figure 6-2. 

**Figure 6-2:  Operation and Repair Cycle** 

Let TB denote the average time between the end of a repair and the next breakdown and T R denote the average repair time.  Then the quantity TB + TR is the length in time of the breakdownrepair cycle.  The availability is defined as the percent of time the machine is not broken and is computed as follows. 

**==> picture [48 x 23] intentionally omitted <==**

**==> picture [24 x 11] intentionally omitted <==**

The following should be noted concerning availability: 

1. The time to complete all work (operations on parts) is reduced to A% of the original time. 2. The lead time for parts waiting for the workstation while it is being repaired will be much longer than for parts that don’t wait for a repair.  Thus, the average, maximum, and standard deviation of the lead time will increase. 

In this case, the machine breaks down on the average once per week (40 hours) and takes between 30 minutes and 2 hours to repair.  Since the time between breakdowns is highly variable, it is modeled as exponentially distributed with a mean of 40 hours.  The time to repair is modeled as uniformly distributed between 30 minutes and 2 hours (120 minutes). 

The second detractor is defective parts.  Either additional parts need to be made or the defective parts need to be reworked to meet the demand.  This increases the amount of work that needs to be done to produce the number of parts needed to meet the demand.  If additional parts need to be made or the average rework time is the same as the average production time, the number of parts that need to be made is given by equation 6-8 where p is the percent of parts that are defective. 

**==> picture [82 x 10] intentionally omitted <==**

(6-8) 

6-8 

The following should be noted concerning defective parts. 

1. The increase in work will increase the utilization of the workstation, which in turn increases the lead time as shown in the VUT equation (6-2). 

2. Effectively, there are more arrivals to the workstation which decreases the time between arrivals to TBA * (1-p). 

In the case, let p = 5%. 

The final detractor is setup and the resulting batching of parts.  The setup and batching process is as follows.  As they arrive, parts are gathered into a group called a batch until the number of parts in the group equals the predetermined batch size (b).  The newly formed batch enters the buffer of the machine to wait processing.  Processing the batch means performing a setup operation on the machine and then processing all items in the batch. 

The following should be noted concerning setup and batching. 

1. Waiting for a batch to form will increase the average, maximum, and standard deviation of lead time. 

2. The following must be true:  b*takt time >= setup time + b * operation time 

3. The minimum feasible batch size may be greater than one, given the preceding item in the list. 

This leads to the following question:  What is the smallest value of the batch size such that the utilization, which now includes the setup time, is as close as possible to a given value? Decreasing the batch size increases the number of setups and thus the amount of time spent doing setup work, which is not productive.  However, decreasing the batch size decreases the work in process and finished goods inventories and supports a more flexible production schedule. These goals are consistent with achieving a lean production environment. 

The utilization should be computed as shown in equation 6-9. 

 = (setup time + b * CT) / (b * Ta) 

(6-9) 

Then the smallest batch size for a given value of the utilization is given by equation 6-9a. 

⁄ 

(6-9a) 

This problem also can be formulated and solved using a spreadsheet to facilitate evaluating alternative values of the batch size.  These alternatives could include complying with constraints such as the batch size must be a multiple of 10.  The evaluation is done by computing the utilization and number of batches as a function of the selected batch size. 

The target utilization is entered.  The absolute deviation between the actual utilization and the target is minimized.  In other words, the batch size n is changed until the actual utilization is as close as possible to the target.  This may be done manually or with one of the spreadsheet tools: solver and goal seek.  Note: if goal seek is used, start with a very small batch size. 

In this case, the target utilization is set to 95% and the setup time is 30 minutes.  Table 6-4 shows the how a batch size of 42 was determined.  Note the value of the batch size computed using equation 6-9a is 42.9. 

6-9 

**Table 6-4:  Result of Finding a Target Batch Size** 

|Inputs|Target Utilization|95%|
|---|---|---|
||Average Time Between Arrivals|6|
||CT|5|
||Setup Time|30|
||Demand|1680|
|Result|Batch size (b)|42|
|Computations|Numerator|240|
||Denominator|252|
||Utilization|95.2%|
||Deviation|0.2%|
||Number of Batches|40|



## _6.4 The Case Study for Detractors_ 

The simulation process is restarted to analyze the effect on lead time of each detractor separately. 

## 6.4.1 Define the Issues and Solution Objective 

The effect of random downtimes on part lead time for parts processed by the workstation is to be assessed.  As discussed in the previous section, the time between breakdowns is modeled as exponentially distributed with a mean of 40 hours and the time to repair is modeled as uniformly distributed between 30 and 120 minutes. 

The effect of defective parts on part lead time at the workstation is to be assessed.  Five percent of completed parts are found to be effective and must be reworked.  The time for reworking is the same as the original processing time. 

The effect of setup and batching on part lead time at the workstation is to be assessed.  For a target utilization of 95%, the batch size was determined to be 42 parts. 

## 6.4.2 Build Models 

The modeling of random downtimes was discussed in chapter 2 and will not be repeated here. To summarize, recall a distinct process is created which models an ongoing cycle of breakdowns and repairs.  After the time between breakdowns, the resource representing the workstation enters the broken state from the idle state.  After the time for repair, the resource enters the idle state to be ready to process another part. 

The model in section 6.3.2 is modified as follows to include defective parts.   After a part has completed processing, it is identified as needing rework with probability 5%.  If rework is needed, the part is sent back to start the workstation process over again.  Parts now arrive to Process Arrive where the arrival time is set.  This avoids resetting the arrival time for defective parts. 

6-10 

// Workstation model with defective parts 

Define Arrivals: // mean must equal takt time Time of first arrival: 0 Time between arrivals: Exponentially distributed with a mean of 6 minutes Exponential (6) minutes Number of arrivals: Infinite // Note: The average number of arrivals is 1680 Define Resources: WS/1 with states (Busy, Idle) Define Entity Attributes: ArrivalTime // part tagged with its arrival time; each part has its own tag Define State Variable PercentDefective = 0.05 // Percent of defective parts Process Arrive Begin Set ArrivalTime = Clock // record time part arrives on tag Send to Process Workstation // start processing End Process Workstation Begin Wait until WS/1 is Idle in Queue QWS // part waits for its turn on the machine Make WS/1 Busy // part starts turn on machine; machine is busy Wait for Triangular (3, 4, 8) minutes // part is processed Make WS/1 Idle // part is finished; machine is idle If (Uniform(0,1) < 0.05) then Send to Process Workstation // part is defective rework Tabulate (Clock-ArrivalTime) in LeadTime // keep track of part time on machine End 

The model in section 6.3.2 is modified as follows to include batching and setup.  Entities in the workstation process now represent batches.  Thus, an entity is not sent from the arrival process to the workstation process until a batch is formed.  In the arrival process, the first 41 entities in the batch wait on a list.  The 42[nd] entity is sent to the workstation process.  The time delay in the workstation process is now the setup time plus 42 different samples of the processing time.  After the batch is processed, all 42 entities go to the depart process so that each lead time can be recorded. 

6-11 

// Workstation model with batching and setup 

Define Arrivals: // mean must equal takt time Time of first arrival: 0 Time between arrivals: Exponentially distributed with a mean of 6 minutes Exponential (6) minutes Number of arrivals: Infinite // Note: The average number of arrivals is 1680 Define Resources: WS/1 with states (Busy, Idle) Define Entity Attributes: ArrivalTime // part tagged with its arrival time; each part has its own tag Define State Variable BatchSize = 42 // Percent of defective parts SetupTime = 30 // Setup time Processed // Number of parts processed Define List BatchList // List of parts waiting for batching Process Arrive Begin Set ArrivalTime = Clock // record time part arrives on tag If TotalArrivals(Arrive) %  BatchSize ! = 0 then Add entity to list BatchList // stop entity processing for now Send to Process Workstation // start processing End Process Workstation // An entity in this process represents a batch Begin Wait until WS/1 is Idle in Queue QWS // batch waits for its turn on the machine Make WS/1 Busy // part starts turn on machine; machine is busy Wait for SetupTime // Setup machine // Processing time for batch as sum of processing times for each part Processed = 0 do while Processed < Batchsize Begin Wait for Triangular (3, 4, 8) minutes // part is processed Processed++ End Make WS/1 Idle // part is finished; machine is idle // Send all entities in batch to record lead time Send Batchsize – 1 from BatchList to Process Depart Send to Process Depart End Process Depart Tabulate (Clock-ArrivalTime) in LeadTime // keep track of part time on machine End 

6-12 

## 6.4.3 Assessment of the Impact of the Detractors on Part Lead Time 

The experimental design shown in Table 6-2 can be used with additions as follows: 

1. For the case of breakdowns, add two random streams: one for the time between breakdowns and the other for the time till repair. 

2. For the case of defective parts, add a random stream for determining whether or not parts are defective. 

3. For setup and batching, no additions are needed. 

Table 6-5 shows the simulation results assessing the effect on lead time of breakdowns. 

**Table 6-5: Simulation Results for Breakdown Experiment** 

|Replicate|Average<br>Number at<br>Station|Average<br>Lead<br>Time|Maximum<br>Lead<br>Time|Utilization|
|---|---|---|---|---|
|1|4.33|25.41|94.28|0.86|
|2|5.28|32.03|186.20|0.83|
|3|3.49|20.90|83.38|0.83|
|4|8.48|48.58|270.39|0.87|
|5|3.91|24.29|138.08|0.80|
|6|3.67|22.36|116.80|0.82|
|7|3.89|23.15|141.18|0.84|
|8|3.51|21.39|121.25|0.82|
|9|6.07|35.46|124.02|0.86|
|10|5.40|32.74|164.23|0.83|
|11|4.30|25.06|149.75|0.86|
|12|14.79|85.83|264.19|0.86|
|13|3.57|21.78|91.78|0.82|
|14|4.52|28.31|134.16|0.80|
|15|4.14|24.25|148.00|0.86|
|16|2.76|16.71|90.52|0.82|
|17|7.06|42.84|213.73|0.83|
|18|3.41|21.14|128.25|0.80|
|19|10.59|60.52|218.28|0.88|
|20|7.17|41.47|221.30|0.86|
|Average|5.52|32.71|154.99|0.84|
|Std. Dev.|2.94|16.68|56.37|0.02|
|Lower<br>Bound|3.64|22.04|118.93|0.82|
|Upper<br>Bound|7.40|43.38|191.05|0.85|



Note that there is an operational significant increase in the average number at the station, the average lead time, and the maximum lead time versus the base experiment.  Notice the increase in the standard deviation of these quantities as well. 

6-13 

This statistical significance of this difference is confirmed for the average lead time using the paired-t test shown in Table 6-6. 

**Table 6-6:  Paired-t test for Difference in Average Lead Time** 

||Average Lead Time|Average Lead Time|Average Lead Time|
|---|---|---|---|
|Replicate|Base|Breakdowns|Increase|
|1|18.80|25.41|6.62|
|2|18.11|32.03|13.92|
|3|20.36|20.90|0.54|
|4|21.15|48.58|27.42|
|5|14.13|24.29|10.15|
|6|16.79|22.36|5.56|
|7|20.17|23.15|2.98|
|8|15.66|21.39|5.73|
|9|18.52|35.46|16.94|
|10|20.34|32.74|12.40|
|11|16.99|25.06|8.07|
|12|26.07|85.83|59.76|
|13|18.97|21.78|2.81|
|14|16.46|28.31|11.85|
|15|18.89|24.25|5.36|
|16|16.62|16.71|0.09|
|17|15.49|42.84|27.36|
|18|15.66|21.14|5.48|
|19|31.55|60.52|28.97|
|20|25.75|41.47|15.71|
|Average|19.32|32.71|13.39|
|Std. Dev.|4.24|16.68|13.96|
|Lower Bound|16.61|22.04|4.46|
|Upper Bound|22.03|43.38|22.31|



The application of the paired-t test to the other simulation results is left as an exercise for the reader. 

Table 6-7 shows the simulation results for the case of defective parts. 

6-14 

**Table 6-7:  Simulation Results for Defects Experiment** 

|Replicate|Average<br>Number at<br>Station|Average<br>Lead<br>Time|Max<br>Lead<br>Time|Utilization|
|---|---|---|---|---|
|1|4.42|25.96|92.01|0.90|
|2|3.93|23.78|109.29|0.86|
|3|4.95|29.68|115.86|0.89|
|4|6.25|35.80|116.02|0.92|
|5|2.76|17.08|57.05|0.83|
|6|3.71|22.61|89.94|0.87|
|7|4.34|25.81|86.87|0.88|
|8|3.23|19.67|69.43|0.86|
|9|4.56|26.64|96.35|0.90|
|10|4.46|27.02|105.34|0.87|
|11|3.51|20.49|70.55|0.89|
|12|6.45|37.28|151.03|0.91|
|13|4.59|27.99|120.01|0.87|
|14|3.77|23.62|110.85|0.84|
|15|5.55|32.52|97.14|0.91|
|16|3.44|20.82|109.64|0.87|
|17|4.22|25.56|107.08|0.87|
|18|3.08|19.13|74.60|0.84|
|19|9.26|52.91|210.05|0.92|
|20|7.47|43.21|202.32|0.91|
|Average|4.70|27.88|109.57|0.88|
|Std. Dev.|1.61|8.83|39.26|0.03|
|Lower Bound|3.67|22.23|84.46|0.86|
|Upper Bound|5.73|33.53|134.69|0.90|



The average and maximum lead times have increased noticeably.  The utilization has increased as would be expected as has the average number at the station.  Recall from the VUT equation that average time in the buffer increases in a highly non-linear fashion as the utilization increases. 

Table 6-8 shows the simulation results for the case of setting up the machine and batching parts. 

6-15 

**Table 6-8:  Simulation Results for the Batching and Setup Experiment** 

|Replicate|Average<br>Number at<br>Station|Average<br>Lead<br>Time|Max<br>Lead<br>Time|Utilization|
|---|---|---|---|---|
|1|1.07|385.04|569.01|0.95|
|2|1.04|396.15|600.01|0.92|
|3|1.02|387.67|574.46|0.92|
|4|1.34|447.70|725.87|0.96|
|5|0.92|372.75|576.90|0.89|
|6|1.02|388.70|601.50|0.92|
|7|1.07|394.96|584.17|0.94|
|8|0.99|380.84|570.58|0.92|
|9|1.07|388.28|610.56|0.96|
|10|1.05|396.50|587.92|0.92|
|11|1.19|416.94|610.85|0.95|
|12|1.29|443.08|720.79|0.96|
|13|1.01|387.51|609.96|0.90|
|14|0.96|385.28|576.22|0.89|
|15|1.22|429.32|685.80|0.95|
|16|0.98|380.15|591.23|0.92|
|17|0.99|385.66|581.59|0.92|
|18|0.98|391.68|586.99|0.89|
|19|1.86|579.34|950.53|0.97|
|20|1.24|425.28|696.60|0.97|
|Average|1.12|408.14|630.58|0.93|
|Std. Dev.|0.21|45.65|90.67|0.03|
|Lower Bound|0.98|378.94|572.58|0.91|
|Upper Bound|1.25|437.35|688.58|0.95|



The following effects of setup and batching can be noted in table 6-8. 

1. The average number at the station now represents batches instead of individual parts. The average value of 1.12 indicates that on the average a new batch forms in a shorter time than it takes to process the preceding batch. 

2. The average and maximum lead times of a part increase greatly versus the case with no detractors reflecting the time to form a batch and setup time. 

3. The utilization is consistent with that specified to find the best batch size, 95%. 

6-16 

## _6.5 Summary_ 

This chapter discusses a beyond lean analysis of the operation of a single workstation, both with and without operations detractors: breakdowns, part reworking, as well as setup and batching. An analytic model is used to compute the workstation utilization as well as the average time and number of parts in the buffer of the workstation for the case of no detractors.  This model provides validation evidence for a simulation model of the workstation which estimates the same quantities plus the maximum lead time.  The different replications of the simulation experiment show a wide range of different system behavior possibilities and the corresponding performance measure values.  Details of system behavior could be extracted from the simulation as well. 

Simulation models and experiments were conducted individually for each detractor.  Results were compared to the no detractors case.  An analytic model was used to set the best batch size given a utilization of 95%. 

Problems 

1. Perform a complete comparison of the breakdowns case to the no detractors case using paired-t statistical tests. 

2. Perform a complete comparison of the part reworking case to the no detractors case using paired-t statistical tests. 

3. Perform a complete comparison of the setup and batching case to the no detractors case using paired-t statistical tests. 

4. Find the best batch size for a target utilization of 95% for a workstation with average time between arrivals of 10 minutes, cycle time of 9 minutes, and setup time of 1 hour. Production is 1000 parts. 

5. Based on the simulation results that follow, provide validation evidence for a model of a single workstation with utilization of 80% 

|**Replicate**|**Utilization**|
|---|---|
|1|80.2%|
|2|79.5%|
|3|80.4%|
|4|80.6%|
|5|79.2%|



6. Based on the simulation results that follow, provide verification evidence for a model of a single workstation. 

|Initial items:|10|
|---|---|
|Items remaining at the end of the simulation:|15|
|Arriving items:|150|
|Departing items:|145|



6-17 

7. Consider a single server workstation for which the average time between arrivals is 10 minutes and the average processing time is 9 minutes.  Suppose a group modeling the workstation is trying to determine the distributions for the time between arrivals and the processing time in absence of data.  Use the VUT equation to determine the average waiting time in the queue for the following possibilities. 

||**Time Between Arrivals**|**Processing Time**|
|---|---|---|
|a.|Exponential|Exponential|
|b.|Constant|Exponential|
|c.|Exponential|Uniform(6,12)|
|d.|Constant|Uniform(6,12)|
|e.|Exponential|Triangular(6, 9,12)|
|g.|Constant|Triangular(6, 9,12)|
|h.|Exponential|Triangular(6,7,14)|
|i.|Constant|Triangular(6,7,14)|



Case Problem 

A new workstation is being designed and a complete analysis is needed as described in this chapter.  The workstation operates 168 hours per month.  Parts are modeled as arriving according to an exponential distribution with mean 10 minutes.  Processing time is uniformly distributed between 6 and 9 minutes. 

Detractors are as follows. 

Breakdowns: The average time between breakdowns is 40 hours.  Repair time is uniformly distributed between 30 and 150 minutes. 

Defective parts: Five percent of parts are defective and require rework. 

Setup and batching: The setup time is 45 minutes.  A utilization of 95% is targeted.  The best batch size should be determined. 

First perform a complete study of the new workstation with no detractors.  Use an analytic model as well as a simulation model and experiment.  Part lead time is the primary performance measure.  Verification and validation evidence for the simulation model must be obtained. 

Second, use a simulation model and experiment to assess the joint effect of all three detractors. Verification and validation evidence should be obtained. 

How to do this case study will be described in tutorial style for the simulation environment that you are using in a separate document. 

6-18
