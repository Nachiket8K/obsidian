---
title: "Chapter 14"
book: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li"
source_pdf: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li.pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 14** 

## **Logistics** 

## _14.1 Introduction_ 

Logistics has to do with the procurement, storage, transportation, and delivery of goods or people. A logistics system deals with the way finished products move from producer to customer or raw material moves from a supplier to the producer.  Logistics systems must be responsive to customer requirements for short lead times.   That is the amount of time between the placement of an order and its delivery should be minimized.  Using excessive amounts of inventory or capital equipment to accomplish this objective increases costs and thus is inconsistent with lean principals. 

Movement of goods may involve truck, rail, water, and air transportation.  Facilities for loading and receiving products by each mode of transporation employed are necessary.  Evaluating trade-offs between using various transporation modes can be a part of a simulation study. 

Inspection and repair of transportation equipment is important.  Inspection is often required after each round trip to a customer and returning to the shipping site.  Inspection delays and subsequent repair times if necessary must be included in a simulation model. 

Determining how many trucks, rail cars, or aircraft are needed must be accomplished.  This is known as fleet sizing.  Fleet size estimates are often made using simple algebra based on the expected round trip time to a customer, including inspection and repair as well as the number of round trips needed per planning period.  This result is the lower bound on the fleet size. Simulation allows the effects of variability on meeting customer requirements for timely deliveries to be considered when sizing a fleet so that a more precise esitimate is obtained.  Variability sources include transportation times and customer demands. 

Staffing plans for logistics systems are necessary.  A lack of staff may prove to be a constraint on the number of loads shipped.  Staff may work only certain shifts during the day and only certain days of the week.  Such scheduling may result in structural variability that causes the need for additional inventory or capital equipment. 

Logistics systems add no value to products.  Thus, their cost needs to be minimized.  On the other hand, they are critical to making sure customers are satisfied by receiving products on time. 

A simple logistic system is shown in Figure 14-1.  A factory creates product which is stored in an inventory.  Customer demands result in shipments via truck to the customer site.  After the shipment is unloaded into the customer’s inventory, the truck returns to the factory for inspection and repair as well as to await its next shipment. 

This chapter discusses a basic and straightforward logistic system with an emphasis on fleet sizing.  A more complex logistic system as required in a supply chain is discussed in the next chapter. 

14-1 

**==> picture [223 x 91] intentionally omitted <==**

**==> picture [57 x 64] intentionally omitted <==**

**==> picture [57 x 64] intentionally omitted <==**

**==> picture [152 x 72] intentionally omitted <==**

Figure 14-1:  Simple Logistics System 

## _14.2 Points Made in the Case Study_ 

Arrivals represent daily shipping demand.  There is one arrival per day at the beginning of the day. The number of shipments per day is modeled as a random variable. 

Trucks used in shipping are modeled with a single resource.  Each unit of the resource represents a truck.  The number of trucks (resource units) required can be determined dynamically in the model during execution.  An additional truck (resource unit) is created whenever needed to make a shipment,  subject to an upper limit.  Thus, the number of trucks needed to meet a performance level can be determined. 

A sequence of experiments can be used to determine the relationship between the maximum number of trucks (resource units) available and system performance.  The values of the number of trucks depend on the results of previous simulation experiments.  After the number of trucks is established, the number of workers is set in the same way. 

Simulation experiments can be run to determine the affect of structural variability on system performance.  Various staff schedules with regard to shifts worked per day and days worked per week can be tested to determine their relationship to system performance and to estimate the number of workers required.  This is left as an exercise for the reader. 

## _14.3 The Case Study_ 

Resource requirements in a logistics system include capital expenditures for transportation mechanisms such as trucks and operating costs such as personnel salaries.  Minimizing capital and operating expenditures while providing the level of service demanded by customers is a fundamental issue. 

14-2 

## 14.3.1 Define the Issues and Solution Objective 

A new logistics system is being designed to deliver truck loads of finished product over a large area from a main terminal supporting a manufacturing plant.  The logistics system works in a similar way to the one shown in Figure 14-1.  Truck loads are shipped seven days per week every day of the year.  For the next year, the daily shipping volume is estimated as follows: a minimum of 20, a mode of 35 and a maximum of 65.  Thus, the average daily shipping volume is 40 loads 

  20  35  65   per day    .  This means that there are 14600 loads shipped per year on the  3  

average. 

A truck waits at the terminal until it is loaded.  Loading time is uniformly distributed between 2 and 4 hours.  A sufficient number of workers are available for loading.  The truck will make all of its deliveries and then return to the terminal.  The time from the terminal to the customer site, in either direction, is triangularly distributed with a minimum of 4 hours, a mode of 12 hours and a maximum of 30 hours.  The time at the customer site is triangularly distributed with a minumum of 2 hours, a mode of 4 hours, and a maximum of 8 hours. 

Upon its return to the terminal, the truck must be inspected by a worker.  Inspection time is uniformly distributed between 1 and 2 hours.  Approximately 90% of the trucks pass inspection or require only minor adjustments and are then ready for another load.  The other 10% require significant maintenance that is performed by the same worker.  Repair time is triangularly distributed with a minimum of 4 hours, a mode of 8 hours and a maximum of 12 hours.  Workers are available 16 hours per day. 

Management does not want to significantly constrain the number of loads delivered each year.  At the same time the number of trucks and number of workers needs to be minimized for cost reasons.  Management has determined that differences of more than 1% in the number of round trips completed are operationally significant.  This difference can affect company profitability. Difference of less than 1%, even if statistically significant, are considered to be operationally unimportant. 

The objective is to determine the number of trucks and workers required for the effective operation of the product delivery system.  Effective operation requires minimizing costs without significantly reducing the number of loads delivered. 

## 14.3.2 Build Models 

The expected number of trucks and workers needed can be estimated using simple algebra.  This is a lower bound on the actual number of trucks and workers needed  Simulation is used to determine if additional trucks and workers are needed to meet the delivery criteria established by management. 

The expected time for a truck to complete the delivery process and be ready to begin another delivery is shown in Table 14-1. 

14-3 

**Table 14-1:  Expected Time to Complete Delivery Process** 

||**Expected Time**<br>**(Hours)**|
|---|---|
|**Load Truck **|3.0|
|**Travel to Customer **|15.3|
|**At Customer **|4.7|
|**Travel to Terminal **|15.3|
|**Inspection **|1.5|
|**Repair**|0.8|
|**Total **|40.6|



There are approximately 8760 hours in a year.  Thus, a truck could be expected to make 215 deliveries per year ( = 8760 / 40.6).  Thus, the number of trucks required to make 14600 deliveries is 68 ( = 14600 / 215). 

The expected number of workers needed can be determined in the same way.  A worker is required for inspection and repair with an expected time of 2.3 hours per delivery.  Thus, a single worker who works 16 hours per day could inspect and repair on the average of 2539 trucks per year.  Thus, 6 workers on each shift ( = 14600 / 2539) are needed. 

The model of the logistics system can be divided into the following processes. 

1. Daily generation of loads. 

2. Truck loading and round trip to the customer site. 

3. Truck inspection and repair. 

4. Worker shift changes. 

The first process Daily Loads operates as follows.  The number of loads per day is generated as a sample from a triangular distribution with the appropriate minimum, mode, and maximum: 20, 35, 65.  While the daily number of loads is an integer, it is also sufficiently large to model as a continuous random variable. 

In order to avoid “loosing” fractional loads, the fractional part of the sample for one day is added to the number of loads for the next day.  For example, suppose the value for the number of loads is 30.6.  Then, 30 loads are created today and 0.6 is added to the number of loads for the following day.  Suppose the value for the number of loads on the following day is 40.7.  Next, 0.6 is added. Thus, 41 loads are created and 0.3 is added to the number of loads for the next day. 

In this process, the variable LoadsWaiting contains the quantity described above and the variable NLoads contains the integer portion of LoadsWaiting.  NLoads loads are sent to the second process, RoundTrip, each day. 

14-4 

Define Arrivals: Time of first arrival: 0 Time between arrivals: 1 day Number of arrivals: Infinite Define Variables LoadsWaiting // Number of loads to ship NLoads: Integer // Integer number of loads to ship Process Daily Begin Set LoadsWaiting += Triag 20, 35, 65 Set NLoads = LoadsWaiting Set LoadsWaiting -= NLoads Clone NLoads to RoundTrip End 

The process model for truck loading and load delivery, RoundTrip, consists of four time delays, one each for truck loading, movement to the customer site, time at the customer site, and return to the terminal.  Then the truck goes to the inspection process.  Preceding the time delays, each load acquires a truck. 

Preceding truck acquisition, the model determines whether an additional unit of the truck resource should be created.  If the number of truck resource units is less than a specified limit, contained in the variable MaxTrucks, and there are no free units of the truck resource, then a new unit is created.  Thus, the load would not wait for a truck.  Else, the load must wait for a truck to return from a delivery as well as being inspected and repaired. 

Define Variables MaxTrucks // Maximun number of trucks Define Resources Truck // Trucks Process RoundTrip Begin If Truck/1 is Idle is FALSE then Begin // Add another truck if possible If Truck Units < MaxTruck then Increment Truck Units by 1 End Wait Until Truck/1 is Idle in QTruck Make Truck/1 Busy Wait for uniform 2,  4 hours //Loading Time Wait for triangular 4, 12, 30 hours //To Customer Wait for triangular 2,  4,  8 hours //At Customer Wait for triangular 4, 12, 30 hours //From Customer Send to Inspect End 

Similar logic is used to model the worker resource in the truck inspection and repair process, Inspect.  After an entity acquires the worker resource, there is time delay for inspection.  Ten percent of the entities also require a time delay for repair. 

14-5 

Define Variables MaxWorkers // Maximun number of workers Define Resources Worker // Inspection and repair workers Process RoundTrip Begin If Worker/1 is Idle is FALSE then Begin // Add another worker if possible If Worker Units < MaxWorker then Increment Worker Units by 1 End Wait Until Worker/1 is Idle in QWorker Make Worker/1 Busy Wait for uniform 3,  1 hr //Inspection If uniform 0, 1 < 10% then Wait for triangular 4, 8, 12 //Repair Make Worker/1 Idle Make Truck/1   Idle End 

The worker shift process is as was discussed in chapter 2.  All units of the worker resource are put into the off-shift state after 16 hours of work and returned to the idle state after 8 hours. 

Notice that this results in an approximation in the model.  If a worker is inspecting or repairing a truck at the beginning of the off shift period, the inspection or repair will continue until completed. This worker will again be available for work at the beginning of the on-shift period.  Thus, the number of workers required could be underestimated. 

## 14.3.3 Identify Root Causes and Assess Initial Alternatives 

The experimental strategy to determine the number of trucks and workers is as follows.  First the number of trucks will be determined.  After the number of trucks is established, the number of workers will be determined for that number of trucks. 

The minimum number of trucks is the expected number, 68, as determined in the previous section.  The maximum number will be determined through simulation by not constraining the number of units of the truck resource used, that is requiring that no load ever waits for a truck. Various values of the number of trucks between the minimum and the maximum will be simulated. 

The number of workers is not constrained so that no returning truck waits for a worker. 

For each of these values, 20 replicates will be made and the average number of completed round trips over the replicates computed.  A graph showing the average number of completed trips versus the number of trucks can be constructed.  Thus, the number of trucks to use is determined. 

The experimental design for determining the number of trucks is shown in Table 14-2. 

A terminating experiment of duration 1 year (8760 hours), the planning period for the logistics system is used.  There is one random number stream for each time delay modeled as a random variable as well as a random number stream for determining the daily number of loads.  An 

14-6 

additional random number stream is needed to model the random choice as to whether a truck passes inspection. 

The primary system performance measure is the number of round trips completed.  The utilization of trucks and workers are of interest.  The experiment will begin with all trucks at the terminal waiting to make a trip. 

**Table 14-2:  Simulation Experiment Design for Determining the Number of Trucks** 

|**Element of the Experiment**|**Values for This Experiment**|
|---|---|
|Type of Experiment|Terminating|
|Model Parameters and Their Values|1.  Number of trucks – Various values between the<br>minimum needed and themaximumused.|
|Performance Measures|1.  Number of round trips completed<br>2.  Utilization of trucks<br>3.Utilizationof workers|
|Random Number Streams|1.  Number of pallets each day<br>2.  Truck loading time<br>3.  Travel time to customer<br>4.  Time at customer site<br>5.  Travel time from customer to terminal<br>6.  Time to inspect returning truck<br>7.  Decision:  Did truck pass inspection?<br>8.  Time torepairtruck|
|InitialConditions|Empty buffers andidleresources|
|Numberof Replicates|20|
|Simulation EndTime|1year|



First the simulation is run with 68 trucks and then with maximum number of trucks used as determined by the simulation to be 144 with an approximate 99% confidence interval of (141.3, 146.3). 

The maximum number of trucks case results in an average of 662 more round trip completions per year.  This is an increase of 4.8% over case where 68 trucks are used.  Furthermore, this difference is statistically significant as seen by the approximate 99% confidence interval for the difference. 

Thus, it can be concluded that more than 68 trucks are needed and that the number of trucks needed is between 68 and 144. 

14-7 

**Table 14-3:  Number of Round Trips – Average Trucks and Maximum Trucks** 

|**Replicate**|**Maximum**<br>**Trucks**|**Maximum**<br>**Average**<br>**Trucks**|**Average**<br>**Difference**|
|---|---|---|---|
|1|1<br>14738|13863|875|
|2|2<br>14374|74<br>13850|524|
|3|3<br>14697|7<br>13839|858|
|4|4<br>14564|4<br>13800|764|
|5|5<br>14345|13853|492|
|6|6<br>14527|27<br>13823|704|
|7|7<br>14278|13804|4<br>474|
|8|8<br>14421|14421<br>13877|77<br>544|
|9|9<br>14638|13825|813|
|10|10<br>14357|7<br>13854|4<br>503|
|11|11<br>14611|11<br>13858|753|
|12|12<br>14791|1<br>13828|963|
|13|13<br>14507|7<br>13755|752|
|14|14<br>14477|14477<br>13754|4<br>723|
|15|15<br>14442|14442<br>13872|72<br>570|
|16|16<br>14447|14447<br>13868|579|
|17|17<br>14397|7<br>13810|587|
|18|18<br>14308|13839|469|
|19|19<br>14501|1<br>13820|681|
|20|20<br>14469|13860|609|
|**Average **|14494.5|13832.6|661.9|
|**Std. Dev.**|142.7|142.7<br>35.0|147.5|
|**99% CI Lower Bound**|14403.2|.2<br>13810.2|.2<br>567.5|
|**99% CI Upper Bound**|14585.7|.7<br>13855.0|756.2|



Furthermore simulation experiments are run with 68, 70, 75, …, 140, and 144 trucks.  Results are shown in the following graph, Figure 14-3. 

**Figure 14-3:  Round Trips versus Number of Trucks** 

14-8 

It appears from the graph that the number of roundtrips increases significantly up to 75 trucks. The difference in round trips when 80 trucks are used instead of 75 is only 14 on the average and thus is not operationally significant.  Thus, 75 trucks will be used if there is a statistically and operationally significant difference in the number of roundtrips versus when 70 trucks are used. The simulation results are summarized in Table 14-4. 

**Table 14-4:  Number of Round Trips – 75 Trucks versus 70 Trucks** 

|**Replicate**|**75 Trucks**|<br>**70 Trucks**|**Difference**<br>**(75 vs 70**<br>**Trucks)**|
|---|---|---|---|
|1|<br>14268|14715|447|
|2|<br>14197|<br>14351|<br>154|
|3|<br>14238|14669|431|
|4|<br>14198|14558|360|
|5|<br>14235|14341|<br>106|
|6|<br>14222|<br>14527|<br>305|
|7|<br>14104|<br>14273|169|
|8|<br>14258|14385|127|
|9|<br>14208|14601|<br>393|
|10|<br>14169|14320|151|
|11|<br>14226|14604|<br>378|
|12|<br>14212|<br>14704|<br>492|
|13|<br>14123|14497|<br>374|
|14|<br>14174|<br>14477|<br>303|
|15|<br>14276|14433|157|
|16|<br>14262|<br>14439|177|
|17|<br>14189|14397|<br>208|
|18|<br>14231|<br>14307|<br>76|
|19|<br>14191|<br>14486|295|
|20|<br>14239|14435|196|
|**Average **|14211.0|14476.0|265.0|
|**Std. Dev.**|45.1|<br>132.9|127.4|
|**99% CI Lower Bound**|14182.1|<br>14390.9|183.5|
|**99% CI Upper Bound**|14239.9|14561.0|346.4|



On the average, the number of roundtrips increases by 265, 1.9%, when 75 trucks are used versus 70 trucks.  Thus, the difference is operationally significant since it is greater than 1%.  The approximate 99% confidence interval for the difference is (183.5, 346.4).  Thus, the difference is statistically significant. 

Thus 75 trucks should be used.  For this case, the truck utilization is 94.9% with an approximate 99% confidence interval of (94.1%, 95.3%).  Utilization includes time spent in inspection and repair. 

Given that 75 trucks should be used, the number of workers must be determined.  The average maximum number of workers determined by the simulation experiments using 75 trucks is 30. This is the maximum number of workers that could be needed.  The average number of workers computed with algebra was 6.  The actual number of workers needed is somewhere between these two values.  The simulation experiment to determine the number of workers is the same as that shown in Table 14-2 except that the model parameter is the number of workers instead of the number of trucks.  Conducting this experiment is left as an exercise for the reader. 

14-9 

## 14.3.4 Review and Extend Previous Work 

Management was pleased with the results as presented above and 75 trucks will be acquired. 

## 14.3.5 Implement the Selected Solution and Evaluate 

The number of completed roundtrips will be monitored.  Additional trucks can be obtained and workers can be hired if needed. 

## _14.4 Summary_ 

This case study emphasizes a sequentially designed simulation experiment to determine the level of resources needed to operate a truck based logistics system.  Minimizing the cost of the system in terms of trucks and workers trades off with the need to meet delivery targets.  The idea of a level of indifference is employed.  Alternatives may statistically differ significantly, but the difference may not be large enough, greater than the level of indifference, to impact system operations. 

## **Problems** 

1. Validate the computation of the expected time a truck spends in repair per roundtrip. 

2. Tell what the entity in each of the processes in the model discussed in this chapter represents. 

3. Give verification evidence based on the information resulting from one replicate of the simulation experiment as follows: 

|Number of truck round trips started:|14335|
|---|---|
|Number of truck round trips completed:|14203|
|Number of truck round trips on going at the end of the simulation:|104|
|Number of trucks waiting or in inspection and repair at the end of the simulation:       28||



4. Compare the modeling and experimental issues of the logistics system discussed in this chapter to those concerning the serial line discussed in chapter 7. 

5. Tour the operation of the local office of an overnight delivery service.  Write down a process model of their logistics system for organizing and delivering in bound packages. 

6. Modify the model presented in this chapter so that no worker inspects or repairs a truck during the off-shift period.  Assess the effect of making the model more precise on the number of workers required. 

7. Suppose that workers were available 24 hours per day but the total number of hours worked per day could not increase.  That is, there would be 2/3rds of the number of workers determine above would work each shift.  Use the model developed in this chapter to determine if the number of trucks needed could be lowered. 

8. Modify the model and simulation experiment to estimate the needed capacity of the parking area for trucks at the terminal.  Include trucks that are in inspection or repair. 

9. Modify the model and simulation experiment to give a profile of truck location.  Estimate the average number of trucks in each possible location:  in route to the customer, at the customer, in route to the terminal, in inspection, in repair, and waiting for a load. 

14-10 

10. Conduct a simulation experiment to determine the number of workers needed. 

## **Case Study** 

A new logistics system is being designed to transport one product from a factory to a terminal by rail.  A simulation study is needed to estimate the following: 

1. The rail fleet size. 

2. The size of the rail yard at the factory. 

3. The size of the rail yard at the terminal. 

4. The size of the inventory needed at the terminal. 

Customer demand is satisfied each day from the terminal.  Demand is normally distributed with a mean of 1000 units and a standard deviation of 200 units.  Production at the factory is sufficient to meet demand on a daily basis.  Policy is to ship an average of 1000 units each day from the factory to the terminal.  Each rail car holds 150 units.  Partial rail car loads are not shipped but included with the demand for the the next day. 

The customer service level provided at the terminal should be at least 99%.  The time period of interest is one year. 

Transportation time from the factory to the terminal is triangularly distributed with a minimum of 3 days, a mode of 7 days, and a maximum of 14 days.  At the terminal, a car must wait for a single unload point to unload.  Unloading takes one hour.  Upon return to the plant, a rail car is inspected.  Inspections take 2 hours.  Maintence is required for 3% of returning cars. Maintenance requires 4 days. 

Embellishment:  All cars leaving the factory in a day join a single train leaving at 4:00 A.M. the next morning and have the same transportation time to the terminal.  A single train containing all empty cars leaves the terminal at 4:00 A.M. each morning. 

Case Study Issues. 

1. What initial conditions concerning the arrival of trains to the terminal should be used? 

2. What target inventory level should be used? 

3. How is the policy to ship 1000 units each day from the factory implemented if rail cars hold 150 units? 

4. Embellishment: How is the requirement that all rail cars leaving the factory or terminal join a single train with a single transporation time to the other site modeled? 

5. How is the unloading constraint for rail cars modeled? 

6. In what order should the system parameters listed above be determined by the simulation experiments? 

7. What is the primary performance measure for the simulation experiments? 

8. How will verification and validation evidence be obtained? 

9. How is the size of a rail yard modeled? 

10. How is the size of the rail fleet modeled? 

14-11 

11. Computed the expected fleet size and use the result in providing validation evidence. 

12. Define the processes that comprise the model. 

14-12
