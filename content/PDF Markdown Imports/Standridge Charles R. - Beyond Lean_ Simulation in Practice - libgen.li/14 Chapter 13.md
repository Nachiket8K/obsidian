---
title: "Chapter 13"
book: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li"
source_pdf: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li.pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 13** 

## **Automated Inventory Management** 

## _13.1 Introduction_ 

An inventory is a collection of parts or finished products that are waiting for use or shipment. Inventories increase costs by requiring storage space that could otherwise be productively used or simply not constructed.  The cost of producing or purchasing what is stored cannot be recovered until the final product is delivered.  Thus, minimizing inventories is important.  On the other hand, not having a part or finished product when needed may lead to a stoppage of production or a dissatisfied customer who takes business elsewhere, thus decreasing revenue.  Thus, having enough inventory is essential. 

Lean demand management requires that manufacturers work with suppliers so that raw material or purchased parts are delivered precisely when needed.  Manufacturers co-operate with large volume retailers to manage their inventories and ship product when sales records indicate that current inventory levels are low.  Information gathered from scanning product bar codes at customer checkout can be aggregated and transferred electronically to the manufacturer nightly to enable this procedure. 

This case study deals with an automated inventory system for a single product.   The retail seller electronically collects information at the point of sale and transmits total daily sales to the supplier. The supplier must organize production and delivery to the seller such that the seller’s inventory is not excessive and sales are not lost due to a lack of inventory. 

## _13.2 Points Made in the Case Study_ 

The automatic inventory system in this case study illustrates a fundamental consideration of demand and inventory management: the cost of holding inventory trades off with the need to meet customer demands. 

Entities sometimes do not represent physical entities.  In this case, a entity represents control information flowing within the inventory system. 

A system can respond to changes in state variable values.  The inventory system responds to changes in the amount of inventory on hand.  When critical values are reached, state events, in the form of arriving entities, occur and initiate appropriate responses.  The ability to model the dynamic response of a system to state variable values changes is a unique simulation capability. 

A **Monte Carlo** simulation is usually defined as taking samples of one or more random variables, manipulating the samples, and gleaning information from the results in a situation where time plays no substantive role.  This simulation experiment has these Monte Carlo characteristics. However, multiple points in time, each separated by one day, are considered.  Changes in state variable values from day to day, determined by the random samples, are significant components of the simulation. 

In previous case studies, detailed operations effecting individual entities are modeled.  In this system, the aggregate affect of production and sales on inventory management are described. Statistical distributions are used to quantify this aggregate behavior.  Manipulations of these distributions based on principles of probability and statistics assist in determining system and model parameter values. 

The model used in this case study illustrates a simulation capability of fundamental importance. The model consists of three processes.  Each process changes the values of the same state variables.  The processes independently determine what actions to take based on the current 

13-1 

state variable values.  However, no information is explicitly transmitted between the processes. The simulation engine transparently performs all co-ordination tasks. 

## _13.3 The Case Study_ 

A large manufacturer of office supplies (pens, pencils, tape, etc.) sells in large volume to a discount office supply retailer.  In order to retain this customer, the manufacturer must manage the customer's inventory and automatically generate shipments of products when necessary. Missing any shipment due to a lack of available product results in a large financial penalty. However, management wishes to minimize the amount of inventory on hand to keep storage space costs and investment in unsold product low.  In addition, it is in the best interest of the manufacturer if the retailer does not lose any sales due to a lack of product on hand.  At the same time, the manufacturer cannot expect the retailer to keep excessive inventory. 

## 13.3.1 Define the Issues and Solution Objective 

We will consider only one product.  Others can be assessed in a similar manner.  Sales data supplied by the customer can be analyzed and the daily sales volume characterized by a statistical distribution.  The sales data concerns one region with 37 stores.  Thus, this data is a sum of 37 values.  As was discussed in Chapter 5, the normal distribution may provide a good fit to such data.  Using software for fitting data to distributions, it was found that a normal distribution with mean 180 cartons and standard deviation 30 cartons fits the actual daily regional sales data. 

The manufacturer and the retailer have agreed that one shipment every three days on the average is acceptable.  The distribution of three days sales can be determined using probability theory as follows.  The distribution of the sum of three normally distributed random variables is also normally distributed with the mean equal to the sum of the three means and variance equal to the sum of the three variances.  (Standard deviations don’t add.)  Thus, three days sales is normally distributed with mean 540 cartons and standard deviation 52 cartons.  The 99% percent point of a normal distribution with mean 540 and standard deviation 52 is approximately 660. Thus, the amount of inventory needed to meet three days of sales with probability 99% is 660 cartons. 

The reorder point, the inventory level that triggers a shipment from the manufacturer, must be set. Since shipments take one day, it is tempting to set the reorder point to the amount of inventory to meet one day’s demand with probability of 99%, approximately 250 cartons.  However, consider the consequences if the inventory at the end of a day is 300 cartons.  No shipment is sent.  The next day suppose the demand is 120 cartons leaving 180 cartons in inventory and triggering a shipment.  The probability of the following day’s demand exceeding 180 cartons is 50%.  Thus, sales could be lost while the shipment is being processed. 

The reorder point will be set at the amount of inventory to meet two days demand with probability of 99%.  Two days demand is normally distributed with mean 360 and standard deviation 42. Thus the reorder point is set to be 460 cartons. 

The nominal maximum production level for the product is 240 cartons per day.  Actual data shows the production level to be uniformly distributed between 220 and 235 due to units that fail to pass inspection and random equipment failures. 

There is no production on any day if inventory at the manufacturer is sufficiently high to meet the next shipment.  A range for this inventory level, called the production cut-off point, can be computed as follows. The target number of units in inventory at the retailer after a shipment is received is 660.  An order, which takes one day to receive, is placed when there are 460 cartons in inventory.  The average number of sales in one day is 180 cartons.  Thus, the average shipment has (660 - 460) + 180 = 380 cartons.  The maximum shipment to the retailer is 660 cartons. 

13-2 

There are two important parameters of the inventory system: 

1. The number of cartons in the inventory of the retailer, the reorder point, that triggers a new shipment from the manufacturer, currently proposed to be 460 cartons. 

2. The number of cartons in inventory at the manufacturer that allows the following day’s production to be canceled, the production cut-off point, currently proposed to be in the range 380 to 660 cartons. 

Figure 13-1 summarizes the inventory system.  Inventory is generated by production at the manufacturer and moved to the retailer as needed.  Inventory levels, product movement, and production status are shown.  Note again how this system is driven by dynamic decisions based on the values of state variables. 

**==> picture [336 x 192] intentionally omitted <==**

**----- Start of picture text -----**<br>
50 units of inventory Production  Production  Truck<br>or fraction thereof on-going Idle<br>[CSS] Es<br>; [ow] oh ch ZA<br>Production<br>Status<br>Be GA fz<br>Retailer<br>Manufacturer<br>**----- End of picture text -----**<br>


**==> picture [176 x 7] intentionally omitted <==**

**----- Start of picture text -----**<br>
Figure 13-1:  Automated Inventory Management System<br>**----- End of picture text -----**<br>


## 13.3.2 Build Models 

The model consists of three parallel processes: 

1. Production at the manufacturer. 

2. Sales at the retailer. 

3. Shipments from the manufacturer to the retailer. 

The first two processes schedule entity arrivals every day.  The latter processes event triggered arrivals that occur when the retailers inventory drops below 460 cartons. First the variables used throughout the model will be defined. 

13-3 

|Define Variables||
|---|---|
|ProductionInv|// Amount of inventory at the manufacturing plant|
|RetailInv|// Amount of inventory at the retail plant|
|Cutoff|// Production cut off level|
|DailyProd|// Daily production at the manufacturing facility|
|Sold|// Daily sales|
|Demand|// Daily demand|
|Reorder|// Reorder Point|
|Ordered|// Order volume from retailer|
|Shipped|// Number of units shipped from the manufacturing|



Consider production at the manufacturer.  A entity arrives once per day to control the production of new units.  If the number of units in inventory is less than the production cut-off point, new units are made and added to the inventory.  The model of this process follows. 

Define Arrivals: Time of first arrival: 0 Time between arrivals: 1 day Number of arrivals: Infinite Process Manufacture Begin If ProductionInv > CutOff then Begin // No need for production today Tabulate 0 in Production End Else Begin // Produce today Tabulate  100 in T_Production Set           DailyProd = uniform 220, 235 Increment ProductionInv by DailyProd end End 

Next consider the process for sales at the retailer.  One entity representing sales information is created each day.  The number of units demanded may exceed those available in inventory.  This is an undesirable situation.  The number of units demanded beyond those that are available in inventory represents lost sales.  The model of the sales process follows. 

Final consider the order process. A state event occurs when the number of units in the retail inventory becomes less than 460.  The time till delivery is one day.  The ordering process follows. 

13-4 

Define Arrivals: Time of first arrival: 0 Time between arrivals: 1 day Number of arrivals: Infinite Process Sales Begin Set Demand = normal 180, 30 If  RetailInv  > Demand then Begin // Sufficient Inventory to meet demand Tabulate 100 in DailySales Set Sold = Demand End Else Begin  // Insufficient Inventory to meet demand Tabulate   0 in DailySales Set  Sold = RetailInv End 

Decrement RetailInv current by Sold End 

Define Arrivals: When RetailInv becomes less than Reorder Number of arrivals: Infinite Process Ship Begin Set Ordered = min (660, 660 - RetailInv + 180) 

If   Ordered  > ProductionInv then Begin // Insufficient inventory for today's order Tabulate 0 in Shipments Set  Shipped = ProductionInv End Else Begin  // Sufficient Inventory Tabulate 100 in Shipments Set Shipped = Ordered End // Make shipment Decrement ProductionInv by Shipped Wait for 24 hr Increment RetailInv by Shipped End 

## 13.3.3 Identify Root Causes and Assess Initial Alternatives 

Table 13-1 gives the experiment design for the inventory system simulation. 

13-5 

**Table 13-1:  Simulation Experiment Design for the Inventory System** 

|**Element of the Experiment**|**Values for This Experiment**|
|---|---|
|Type of Experiment|Terminating|
|Model Parameters and Their Values|1.  Re-order point for retailers inventory, 460 units<br>2.  Production cancellation point based on<br>manufacturer’s inventory (380, 660) units|
|Performance Measures|1.  Number of days with lost sales<br>2.  Amount of inventory at the retailer<br>3.  Number of days with no production<br>4.  Amount of inventory at the manufacturer<br>5.  Number of shipments<br>6.  Number of shipments with insufficient units|
|Random Number Streams|1.  Number of units manufactured<br>2.  Number of units demanded|
|Initial Conditions|1.  Inventory at the retailer – average of the reorder<br>point and the maximum desirable inventory, 560 units<br>2.  Inventory at the manufacturer -- Mid-point of the<br>product cancellation range, 520 units|
|Numberof Replicates|20|
|Simulation EndTime|365 days (one year)|



Management felt that demand data would be valid for no more than one year.  Thus, a terminating experiment with a time period of one year was used.  The number of units demanded each day and the number of units produced each day that production occurs are modeled as random variables.  Thus, two random number streams are needed.  Twenty replicates will be performed. 

The initial inventory at the manufacturer and at the retailer must be set.  Management believed that typical conditions are as follows.  The number of units at the retailer should most often be between the re-order point and the intended maximum inventory level or 460 - 660.  The average of these values, 560, will be used for the initial conditions.  A typical number of units at the manufacturer should be within the range of the cut-off level for production, 380 - 660 units.  The mid-point of the range, 520, is used. 

As discussed previously, model parameters are the re-order point for the retailers inventory, whose value in the first experiment will be 460 units, and the production cancellation point.  The values used for this latter quantity are the average shipment size, 380 units, and the maximum shipment size, 660 units. 

There are several performance measures.  The number of days with lost sales measures how well the inventory management system helps the retailer meet demand for the product.  In addition, the inventory level at the retailer is of concern.  At the manufacturer, the number of days without production and the inventory level are of interest.  Finally, the total number of shipments from the manufacturer to the retailer, as well as the number of shipments with less than the requested number of units, should be estimated.  The latter results from a lack of inventory at the manufacturer. 

The inventory level at the retailer must be examined.  Figures 13-2 and 13-3 show the inventory level at the retailer over time from the first replicate for each value of the cut-off point.  In both graphs, the majority of the values are between 100 and 500 cartons. 

13-6 

**Figure 13-2:  Inventory at Retailer – Production Cut-off Point of 660** 

**Figure 13-3:  Inventory at Retailer – Production Cut-off Point of 380** 

Figures 13-4 and 13-5 show the inventory levels at the manufacturer for each value of the production cut-off point.  The higher cut-off value, 660, results in an inventory between 400 and 800 cartons most of the time.  The lower value, 380, results in an inventory between 200 and 500 cartons most of the time. 

13-7 

**Figure 13-4:  Inventory at Manufacturer – Production Cut-off Point of 660** 

**Figure 13-5:  Inventory at Manufacturer – Production Cut-off Point of 380** 

There were only 4 days of lost sales over all 20 replicates when the cut-off point was 660 and 3 days when the cut-off point was 380.  This indicates that the reorder point was set correctly, or at least not too low. 

Table 13-2 summarizes the other performance measure values resulting from the simulation experiment. 

The number of days with no production is approximately the same for both values of the production cut-off point.  The number of days per year without production is about 78 or 1.5 days per week.  Thus, 5.5 days of production per week should be sufficient. 

When the higher production cut-off point is used, all shipments contain the number of units requested by the retailer.  When the lower cut-off point is used, slightly less than half of the shipments have an insufficient number of units, that is fewer units than requested by the retailer. The lower cut-off value leads to an average of 10.4 additional shipments per year. 

13-8 

**Table 13-2:  Results of the Inventory System Experiment** 

||**Days with No**<br>**Production **|**Days with No**<br>**Production **|**Days with No**<br>**Production **|**# of Insufficient**<br> **Shipments**|**# of Insufficient**<br> **Shipments**|**# of Insufficient**<br> **Shipments**|**Total # of**<br>**Shipments**|**Total # of**<br>**Shipments**|**Total # of**<br>**Shipments**|
|---|---|---|---|---|---|---|---|---|---|
|Replicate|Cut-<br>off<br>Point<br>660|<br> <br>Cut-<br>off<br>Point<br>380|<br> <br> <br>Difference|<br>Cut-<br>off<br>Point<br>660|<br> <br>Cut-<br>off<br>Point<br>380|<br> <br> <br>Difference|<br>Cut-<br>off<br>Point<br>660|<br> <br> <br>Cut-<br>off<br>Point<br>380|<br> <br> <br>Difference|
|1|<br>80|81|<br>1|<br>0|73|73|133|143|10|
|2|<br>75|76|1|<br>0|66|66|137|<br>147|<br>10|
|3|<br>74|<br>75|1|<br>0|76|76|136|146|10|
|4|<br>79|80|1|<br>0|64|<br>64|<br>135|145|10|
|5|<br>79|80|1|<br>0|79|79|132|<br>144|<br>12|
|6|<br>73|74|<br>1|<br>0|78|78|136|146|10|
|7|<br>76|77|<br>1|<br>0|65|65|133|145|12|
|8|<br>76|77|<br>1|<br>0|57|<br>57|<br>136|146|10|
|9|<br>76|77|<br>1|<br>0|60|60|135|146|11|
|10|<br>78|79|1|<br>0|79|79|134|<br>144|<br>10|
|11|<br>75|77|<br>2|<br>0|68|68|134|<br>147|<br>13|
|12|<br>72|<br>74|<br>2|<br>0|60|60|138|148|10|
|13|<br>74|<br>75|1|<br>0|55|55|135|147|<br>12|
|14|<br>78|79|1|<br>0|67|<br>67|<br>136|145|9|
|15|<br>72|<br>74|<br>2|<br>0|74|<br>74|<br>137|<br>148|11|
|16|<br>74|<br>75|1|<br>0|71|<br>71|<br>138|146|8|
|17|<br>78|79|1|<br>0|73|73|134|<br>146|12|
|18|<br>81|<br>82|<br>1|<br>0|72|<br>72|<br>135|144|<br>9|
|19|<br>72|<br>73|1|<br>0|61|<br>61|<br>137|<br>148|11|
|20|<br>77|<br>78|1|<br>0|76|76|137|<br>145|8|
|**Average **|75.9|77.1|<br>1.2|<br>0|68.7|<br>68.7|<br>135.4|<br>145.8|10.4|
|**Std. Dev.**|2.7|<br>2.6|0.4|<br>0|7.5|7.5|1.7|<br>1.4|<br>1.4|
|**99% CI**<br>**Lower**<br>**Bound**|74.2|<br>75.4|<br>0.9|0|63.9|63.9|134.3|144.9|9.5|
|**99% CI**<br>**Upper**<br>**Bound**|77.7|<br>78.8|1.4|<br>0|73.5|73.5|136.5|146.7|<br>11.3|



## 13.3.4 Review and Extend Previous Work 

Management felt that the foremost objective is to satisfy the retailer.  The automated inventory management system appears to meet the objective.  The retailer is able to meet all customer demand without carrying excessive inventory.  Most of the time, the inventory is less than three days average demand for the product. 

The higher value for the cut-off point is preferred.  This results in no shipments with less units than the retailer demanded as well as fewer total shipments.  Management is willing to accept a larger inventory at the manufacturer to better satisfy the customer. 

Management noted that the variance between replicates is small.  This small variance should make the automated inventory system easier to operate and control. 

13-9 

Production of the product 5.5 days a week will be scheduled. 

## 13.3.5 Implement the Selected Solution and Evaluate 

The automated inventory system will be installed and will operate with a reorder point of 460 units and a production cut-off point of 660 units.  The retailer was assured by the simulation results of the ability to meet customer demand completely and consistently as well as holding a relatively low inventory.  System performance will be monitored using the measures defined for the simulation experiment. 

## _13.4 Summary_ 

This chapter illustrates how dynamic decision making based on state variables may be incorporated into models.  System details are not modeled directly.  Aggregate behavior is modeled using statistical distributions.  Graphs show the dynamics of inventory levels.  System behavior due to alternative values of inventory system parameters is assessed. 

## **Problems** 

1. Provide verification evidence for the inventory system experiment based on the following results. 

Number of days processed: 365 Number of days without production: 77 Number of days with production: 288 Number of shipments: 145 Number of shipments of sufficient quantity: 78 Number of shipments of insufficient quantity: 67 

2. Provide validation evidence for the inventory system experiment based on the simulation results presented in this case study. 

3. One possibility that could arise during the simulation experiment is the following. Suppose a shipment of insufficient units failed to bring the inventory at the retailer above the reorder point.  What would be the consequences for the simulation experiment? What conclusions could be drawn about operating the system with the particular reorder and cut-off point values? 

4. Discuss management’s decision to use the higher cut-off point value.  Defend using the lower value since the customer can still meet all demand. 

5. Include detection and response of the condition described in problem 3 in the model and resimulate the using the lower value of the cut-off point. 

6. Find a cut-off point value between 380 and 660 that improves system operation.  Use a reorder point of 460 units. 

7. Find a reorder point lower than 460 units that either improves system operation or makes it no worse. 

8. Print out a trace of the inventory at the retailer.  For each day, include the inventory at the start of the day, the deliveries, the demand, and the inventory at the end of the day. 

9. Modify the model so that product occurs Monday through Friday at the current rate and Saturday at half the current rate.  This implements the conclusion of the analysis that 5.5 

13-10 

days per week production on the average is sufficient.  At the same time, customer demand at the retailer occurs 7 days per week.  Would you expect more or less inventory to be needed at the retailer?  Defend your expectation. 

## **Case Problem** 

A product inventory changes daily due to customer demand that withdraws from it and production that replenishes it on the days when it is operating.  Customer demands and production are random variables.  Production is subject to down times of random frequency and duration. Customers due not backorder.  Thus, any customer demand that cannot be met results in a lost sale. 

Periodically, an analyst can review the inventory and make adjustments by purchasing or selling product on the spot market.  The time between these reviews is called the review period.  At each review, the analyst can do the following: 

- a. If the current inventory is less than the safety stock, buy a quantity of product equal to (safety stock – current inventory) on the spot market. 

- b. If the current inventory is greater than the maximum inventory, sell a quantity of product equal to (current inventory – maximum inventory) on the spot market. 

The safety stock level is an operating parameter of the inventory system set such that the probability of meeting all customer demand between periodic reviews is at least a specified value, typically 90%, 95%, or 99%.  This probability is called the effective service level. 

The maximum inventory level is less that the physical limit on inventory storage, called the capacity, to avoid having no place to store items. 

Figure 13-6 summarizes the inventory control system.  Note the following definitions and notation. 

**==> picture [275 x 225] intentionally omitted <==**

**----- Start of picture text -----**<br>
Shut Down<br>Capacity<br>sd*z(1-Lshut) Sell Inventory<br>Maximum<br>Inventory<br>No Action<br>Target<br>Inventory<br>sd*zL No Action<br>Safety Stock<br>sd*zL Buy Inventory<br>0 Inventory<br>Reject Orders<br>**----- End of picture text -----**<br>


Figure 13-6:  Inventory Management System Summary 

13-11 

Target inventory – The desired inventory to avoid purchases and sales on the spot market, in the range [safety stock, maximum inventory]. 

Delta inventory – The change in inventory each day due to production (+) and demand (-). 

Nominal service level – The probability that the inventory will be greater than the safety stock at the time of a review given that it was equal to the target at the time of the last review.  As well, the probability that the inventory will be greater than zero at the time of a review given that it was equal to the safety stock at the time of the last review. 

d = number of days in the review period 

d = the mean of the delta inventory distribution for a review period of d days 

2 sd = the variance of the delta inventory distribution for a review period of d days 

p = the mean of the conditional daily production distribution (given that production is greater than zero). 

2 sp = the variance of the daily production distribution 

c = the mean of the daily customer demand distribution 

2 sc = the variance of the daily customer demand 

A = the percent of days that production occurs (the availability of production) 

L = the nominal service level as a percent 

Leff = the effective service level 

_L_  1  (1  _L eff_ ) 

Lshut = the probability of exceeding the capacity during the next review period given that the inventory level is equal to the maximum inventory at the current review 

zL = The L% point of the standard normal distribution 

The average demand is equal to the average production over a long period of time such as a year.   This means that c = p * A.  In other words, the expected production each day (including an allowance for down time) is equal to the expected daily demand. 

Ignoring down times, the delta inventory can be viewed approximately normally distributed with parameters: 

 _d_  0 

**==> picture [158 x 28] intentionally omitted <==**

13-12 

The problem is to determine the review period, safety stock, maximum inventory, and target inventory given an effective service level.  Performance measures should include the service level as well as the number of purchases and sales made to the spot market by the analyst. 

Consider the following specifications. 

Capacity: 10,000. Distribution of customer demand: Normal (1000,   250). Distribution of production when production occurs: Normal(1000/A, 300). A=Availability: 30/(30+1.92) Review period: 7, 10, or 14 days. Effective service level: 0.95 or 0.99. 

First, determine the required quantities assuming that there is no production downtime.  Use analytic models to compute the safety stock, target inventory, and maximum inventory for each review period.  Use simulation to validate the analytic computations.  Make adjustments to the analytically computed quantities if necessary.  Validate your final recommendation using simulation.  Validate means to show that the required effective service level is met. 

Next, consider production downtime.  Establish and validate quantities for the safety stock, target inventory, and maximum inventory using simulation.  The average time between periods of no production is 30 days.   The average length of each period of no production is 1.92 days.  The distribution of the period of no production follows. 

Distribution of the Length of Periods of No Production 

|Days<br>Down|Percent|
|---|---|
|1|<br>50%|
|2|<br>25%|
|3|<br>13%|
|4|<br>7%|
|5|<br>5%|
|Total|100%|



Case Problem Issues 

1. Identify the processes that are needed in the model. 

2. Specify all of the combination of the values of the parameters that should be simulated. 

3. Compute the safety stock, target inventory level, and maximum inventory level for each parameter value combination using a spreadsheet. 

4. Specify the initial conditions for the simulation. 

5. In addition to service level, define the performance measures. 

6. Determine how production downtime should be modeled. 

7. Discuss how verification and validation evidence will be obtained. 

The time period of interest is one year. 

13-13
