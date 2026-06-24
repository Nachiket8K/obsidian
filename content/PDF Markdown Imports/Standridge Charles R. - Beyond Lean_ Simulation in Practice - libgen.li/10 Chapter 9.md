---
title: "Chapter 9"
book: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li"
source_pdf: "Standridge Charles R. - Beyond Lean_ Simulation in Practice - libgen.li.pdf"
tags:
  - pdf-import
  - split-book
---

## **Chapter 9** 

## **Inventory Organization and Control** 

## _9.1 Introduction_ 

Even before a full conversion to lean manufacturing, a facility can be converted to a pull production strategy.  Such a conversion is the subject of chapter 10.  An understanding of the nature of inventories is pre-requisite for a conversion to pull.  Thus, the organization and control of inventories is the subject of this chapter.  Traditional inventory models are presented first.  Next the lean idea of the control of inventories using kanbans is described.  Finally, a generalization of the kanban approach called constant work in process (CONWIP) is discussed.  In addition, a basic simulation model for inventories is shown. 

## _9.2 Traditional Inventory Models_ 

## 9.2.1 Trading off Number of Setups (Orders) for Inventory 

Consider the following situation, commonly called the economic order quantity problem.  A product is produced (or purchased) to inventory periodically.  Demand for the product is satisfied from inventory and is deterministic and constant in time.  How many units of the product should be produced (or purchased) at a time to minimize the annual cost, assuming that all demand must be satisfied on time?  This number of units is called the batch size. 

The analysis might proceed upon the following lines. 

1. What costs are relevant? 

   - a. The production (or purchase) cost of each unit of the product is sunk, that is the same no matter how many are made at once. 

   - b. There is a fixed cost per production run (or purchase) no matter how many are made. 

   - c. There is a cost of holding a unit of product in inventory until it is sold, expressed in $/year. Holding a unit in inventory is analogous to borrowing money.  An expense is incurred to produce the product.  This expense cannot be repaid until the product is sold.  There is an “interest charge” on the expense until it is repaid.  This is the same as the holding cost. Thus, the annual holding cost per unit is often calculated as the company minimum attractive rate of return times the cost of one unit of the product. 

2. What assumptions are made? 

   - a. Production is instantaneous.  This may or may not be a bad assumption.  If product is removed from inventory once per day and the inventory can be replenished by a scheduled production run of length one day every week or two, this assumption is fine.  If production runs cannot be precisely scheduled in time due to capacity constraints or competition for production resources with other products or production runs take multiple days, this assumption may make the results obtained from the model questionable. 

   - b. Upon completion of production, the product can be placed in inventory for immediate delivery to customers. 

   - c. Each production run incurs the same fixed setup cost, regardless of size or competing activities in the production facility. 

   - d. There is no competition among products for production resources.  If the production facility has sufficient capacity this may be a reasonable assumption.  If not, production may not occur exactly at the time needed. 

The definitions of all symbols used in the economic order quantity (EOQ) model are given in Table 9-1. 

9-1 

**Table 9-1:  Definition of Symbols for the Economic Order Quantity Model** 

|**Term**|**Definition **|
|---|---|
|Annual demand rate (D)|Units demanded per year|
|Unit production cost (c)|Production cost per unit|
|Fixed cost per batch (A)|Cost of setting up to produce or purchase one batch|
|Inventory cost per unit per year (h)|h=i*c where i is the corporate interest rate|
|Batch size (Q)|Optimal value computed using the inventory model|
|Orders per year (F)|D/Q|
|Time between orders|1/F=Q/D|
|Cost per year|Run (order) setup cost + inventory cost =<br>A * F+h *Q/2|



The cost components of the model are the annual inventory cost and the annual cost of setting up production runs.  The annual inventory cost is the average number of units in inventory times the inventory cost per unit per year.  Since demand is constant, inventory declines at a constant rate from its maximum level, the batch size Q, to 0.  Thus, the average inventory level is simply Q/2.  This idea is shown in Figure 9-1. 

**==> picture [321 x 257] intentionally omitted <==**

The number of production runs (orders) per year is the demand divided by the batch size.  Thus the total cost per year is given by equation 9-1. 

**==> picture [455 x 25] intentionally omitted <==**

Finding the optimal value of Q is accomplished by taking the derivative with respect to Q, setting it equal to 0 and solving for Q.  This yields equation 9-2. 

9-2 

(9-2) 

_Q_ *  2 * _A_ * _D_  _A_ * 2 * _D h h_ 

Notice that the optimal batch size Q depends on the square root of the ratio of the fixed cost per batch, A, to the inventory holding cost, h.  Thus, the cost of a batch trades off with the inventory holding cost in determining the batch size. 

Other quantities of interest are the number of orders per year (F) and the time between orders (T). 

**==> picture [93 x 43] intentionally omitted <==**

(9-3) (9-4) 

It is important to note that: 

_Mathematical models help reveal tradeoffs between competing system components or parameters and help resolve them._ 

Even if values are not available for all model parameters, mathematical models are valuable because they give insight into the nature of tradeoffs.  For example in equation 9- 2, as the holding cost increases the batch size decreases and more orders are made per year.  This makes sense, since an increase in inventory cost per unit should lead to a smaller average inventory. 

As the fixed cost per batch increases, batch size increases and fewer orders are made per year.  This makes sense since an increase in the cost fixed cost per batch results in fewer batches. 

Suppose cost information is unknown and cannot be determined.  What can be done in this application? One approach is to construct a graph of the average inventory level versus the number of production runs (orders) per year.  An example graph is shown in Figure 9-2.  The optimal tradeoff point is in the “elbow” of the curve.  To the right of the elbow, increasing the number of production runs (orders) does little to lower the average inventory.  To the left of the elbow, increasing the average inventory does little to reduce the number of production runs (orders). 

In Figure 9-2, an average inventory of about 20 to 40 units leads to about 40 to 75 production runs a year. This suggests that optimal batch size can be changed within a reasonably wide range without changing the optimal cost very much.  This can be very important as batch sizes may be for practical purposes restricted to a certain set of values, such as multiples of 12, as order placement could be restricted to weekly or monthly. 

Example.  Perform an inventory versus batch size analysis on the following situation.  Demand for medical racks is 4000 racks per year.  The production cost of a single rack is $250 with a production run setup cost of $500.  The rate of return used by the company is 20%.  Production runs can be made once per week, once every two weeks, or once every four weeks. 

The optimal batch size (number of units per production run) is given by equation 9-2: 

**==> picture [194 x 25] intentionally omitted <==**

**----- Start of picture text -----**<br>
* 2 * A * D 2 * 500 * 4000<br>Q    283<br>h 250 * 20 %<br>**----- End of picture text -----**<br>


9-3 

**==> picture [363 x 266] intentionally omitted <==**

**----- Start of picture text -----**<br>
Inventory vs Production Run Tradeoff<br>180<br>160<br>140<br>120<br>100<br>80<br>60<br>40<br>20<br>0<br>0 50 100 150 200 250<br># of Runs<br>Average inventory<br>**----- End of picture text -----**<br>


Figure 9- 2:  Inventory versus Production Run Tradeoff Graph 

The number of production runs per year and the time between production runs is given by equations 9-3 and 4: 

* * _F_  _D_ / _Q_  14 .1 * * * _T_  1 / _F_  _Q_ / _D_  3 .7 _weeks_ 

The optimal cost is given by equation 9-1: 

**==> picture [372 x 29] intentionally omitted <==**

Applying the constraint on the time between production runs yields the following. 

' _T_  4 _weeks_ ' _F_  52 _weeks_ / 4 _weeks_  13 ' ' _Q_  4000 / _F_  308 ' ' _Q D_ 308 _Y_ ( _Q_ )  _h_ * 2  _A_ * _Q_ '  250 * 20 % * 2  500 * 13  7700  6500  14200 

Note that when the optimal value of Q is used the inventory cost and the setup cost of production runs are approximately equal.  When the constrained value is used, the inventory cost increases since batch sizes are larger but the setup cost decreases since fewer production runs are made.  The total cost is about the same. 

9-4 

## 9.2.2 Trading Off Customer Service Level for Inventory 

Ideally, no inventory would be necessary.  Goods would be produced to customer order and delivered to the customer in a timely fashion.  However, this is not always possible.  Wendy’s can cook your hamburger to order but a Christmas tree cannot be grown to the exact size required while the customer waits on the lot.  In addition, how many items customers demand and when these demands will occur is not known in advance and is subject variation 

Keeping inventory helps satisfy customer demand on-time in light of the conditions described in the preceding paragraph.  The **service level** is defined as the percent of the customer demand that is met on time. 

Consider the problem of deciding how many Christmas trees to purchase for a Christmas tree lot.  Only one order can be placed. The trees may be delivered before the lot opens for business.  How many Christmas trees should be ordered if demand is a normally distributed random variable with known mean and standard deviation? 

There is a trade-off between: 

1. Having unsold trees that are not even good for firewood. 

2. Having no trees to sell to a customer who would have bought a tree at a profit for the lot. 

Relevant quantities are defined in Table 9-2. 

**Table 9-2;  Definition of Symbols for Service Level – Inventory Trade-off Models** 

|**Term**|**Definition **|
|---|---|
|cs|Cost of a stock out, for example not having a Christmas tree when a customer wants<br>one.|
|co|Cost ofanoverage,forexamplehavingleft overChristmas trees|
|SL|Servicelevel|
|Q|Batchsize or numberofunits to order|
||Mean demand|
||Standard deviation of demand|
|zp|Percent point of the standard normal distribution: P(Zzp) = p.  In Excel this is given by<br>NORMSINV(p)|



Then it can be shown that the following equation holds: 

**==> picture [454 x 27] intentionally omitted <==**

This equation states that the cost-optimal service level depends on the ratio of the cost of a stock out and the cost of an overage. 

In the Christmas tree example, the cost of an overage is the cost of a Christmas tree.  The cost of a stock out is the profit made on selling a tree.  Suppose the cost of Christmas tree to the lot is $15 and the tree is sold for $50 (there’s the Christmas spirit for you).  This implies that the cost of a stock out is $50 - $15 = $35.  The cost-optimal service level is given by equation 9-5. 

**==> picture [140 x 27] intentionally omitted <==**

9-5 

If demand is normally distributed, the optimal number of units to order is given by the general equation: 

**==> picture [76 x 13] intentionally omitted <==**

(9-6) 

Thus, the optimal number of Christmas trees to purchase if demand is normally distributed with mean 100 and standard deviation 20 is 

**==> picture [210 x 12] intentionally omitted <==**

There are numerous similar situations to which the same logic can be applied.  For example, consider a store that sells a particular popular electronics product.  The product is re-supplied via a delivery truck periodically. 

In this application, the overage cost is equal to the inventory holding cost that can be computed from the cost of the product and the company interest rate as was done in the EOQ model.  The shortage cost could be computed as the unit profit on the sale of the product. 

However, the manager of the store feels that if the product is out of stock, the customer may go elsewhere for all their shopping needs and never come back.  Thus, a pre-specified service level, usually in the range 90% to 99% is required.  What is the implied shortage cost?  This is given in general terms by equation 9- 7. 

_SL c s_  _c o_ * (9-7) 1  _SL_ 

Notice that this is equation is highly non-linear with respect to the service level. 

Suppose deliveries are made weekly, the overage cost (inventory holding cost) is $1/per week, and that a manager specifies the service level to be 90%.  What is the implied cost of a stock out?  From equation 9- 7, this cost is computed as follows: 

**==> picture [169 x 24] intentionally omitted <==**

Note that if the service level is 99%, the cost of a stock out is $99. 

## _9.3 Inventory Models for Lean Manufacturing_ 

In a lean manufacturing setting, the service level is most often an operating parameter specified by management.  Inventory is kept to co-ordinate production and shipping, to guard against variation in demand, and to guard against variation in production.  The latter could be due to variation in supplier shipping times, variation in production times, production downtimes and any other cause that makes the completion of production on time uncertain. 

A very important idea is that the target inventory level needed to achieve a specified service level is a function of the variance in the process that adds items to the inventory, production, as well as the process the removes items from the inventory, customer demand.  If there is no variation in these processes, then there is no need for inventory.  Furthermore, the less the variation, the less inventory is needed.  Variation could be random, such as the number of units demanded per day by customers, or structural: product A is produced on Monday and Wednesday and product B is produced on Tuesday and Thursday but there is customer demand for each product each day. 

9-6 

We will confine our discussion to the following situation of interest.  Product is shipped to the customer early in the morning from inventory and is replaced by a production run during the day.  Note that if the production run completes before the next shipment time, production can be considered to be instantaneous.  In other words, as long as the production run is completed before the next shipment, how long before is not relevant. 

Suppose demand is constant and production is completely reliable. If demand is 100 units per day, then 100 units reside in the inventory until a shipment is made.  Then the inventory is zero.  The production run is for 100 units, which are placed in the inventory upon completion.  This cycle is completed every day. 

The following discussion considers how to establish the target inventory level to meet a pre-established service level when demand is random, when production is unreliable, and when both are true. 

## 9.3.1 Random Demand – Normally Distributed 

In lean manufacturing, a buffer inventory is established to protect against random variation in customer demand.  Suppose daily demand is normally distributed with a mean of  units and a standard deviation of  units.  Production capacity is such that the inventory can be reliably replaced each day. Management specifies a service level of SL. 

Consider equation 9-8, 

P(X  x) ≤ SL (9-8) 

This equation says that the probability that the random variable, X, daily demand, is less than the target inventory, the constant x, must be SL.  Solving for the target inventory, x, yields equation 9-9. 

x =  +  * zSL (9-9) Exercise. 

Customer demand is normally distributed with a mean of 100 units per day and a standard deviation of 10 units.  Production is completely reliable and replaces inventory every day.  Determine the target inventory for service levels of 90%, 95%, 99% and 99.9%. 

Suppose production is reliable but can occur only every other day.  The two-day demand follows a normal distribution with a mean of 2 *  units and a standard deviation of 2 *  units.  The target inventory level is still SL. 

Consider the probability of sufficient inventory on the first of the two days.  Since the amount of inventory is sufficient for two days, we will assume that the probability of having enough units in inventory on the first day to meet customer demand is very close to 1. 

Thus, the probability of sufficient inventory on the second day need only be enough such that the average of this quantity for the first day and the second day is SL.  Thus, the probability of sufficient inventory on the second day is SL2 = 1 – [(1 - SL) * 2]. 

This means that the target inventory for replenishment every two days is given by equation 9-10. 

x2 = 2 *  + 2 * zSL2 

This approach can be generalized to n days between production, so long as n is small, a week or less. This condition will be met in lean production situations. 

9-7 

Exercise. 

Customer demand is normally distributed with a mean of 100 units per day and a standard deviation of 10 units.  Production is completely reliable and replaces inventory every two days.  Determine the target inventory for service levels of 90%, 95%, 99% and 99.9%. 

## 9.3.2 Random Demand – Discrete Distributed 

In many lean manufacturing situations, customer demand per day is distributed among a relative small numbers of batches of units.  For example, a batch of units might be a pallet or a tote. 

This situation can be modeled using a discrete distribution.  The general form of a discrete distribution for this situation is: 

 pi  = 1 

(9-11) 

where i is the number of batches demanded and pi is the probability of the customer demand being exactly i batches. The value of i ranges from 1 to n, the maximum customer demand.  If n is small enough, then a target inventory of n batches is not unreasonable and the service level would be 1. 

Suppose a target inventory of n batches is too large.  Then the target inventory, x, is the smallest value of x for which equation 9-12 is true. 

_x_  _p i_[] _SL i_  1 

(9-12) 

## Exercise 

Daily customer demand is expressed in batches as follows: 

(4, 20%), (5, 40%), (6, 30%), (7, 10%). 

Production is completely reliable and replaces inventory every day.  Determine the target inventory for service levels of 90%, 95%, 99% and 99.9%. 

Suppose production is reliable but can occur only every other day.  The two-day demand distribution is determined by convolving the one-day demand distribution with itself.  Convolving has to do with considering all possible combinations of the demand on day one and the demand on day two.  Demand amounts are added and probabilities are multiplied.  This is shown in Table 9-3 for the example in the preceding box. 

Table 9-4 adds together the probabilities for the same values of the two-day demand (day one + day two demand).  For example, the probability that the two day demand is exactly 9 batches is 16%, (8% + 8%) 

9-8 

**Table 9-3:  Possible Combinations of the Demand on Day One and Day Two** 

|Day One Demand|Day One Demand|Day Two Demand|Day Two Demand|Day One + Day Two Demand|Day One + Day Two Demand|
|---|---|---|---|---|---|
|Demand|Probability|Demand|Probability|Demand|Probability|
|4|20%|4|20%|8|4%|
|5|40%|4|20%|9|8%|
|6|30%|4|20%|10|6%|
|7|10%|4|20%|11|2%|
|4|20%|5|40%|9|8%|
|5|40%|5|40%|10|16%|
|6|30%|5|40%|11|12%|
|7|10%|5|40%|12|4%|
|4|20%|6|30%|10|6%|
|5|40%|6|30%|11|12%|
|6|30%|6|30%|12|9%|
|7|10%|6|30%|13|3%|
|4|20%|7|10%|11|2%|
|5|40%|7|10%|12|4%|
|6|30%|7|10%|13|3%|
|7|10%|7|10%|14|1%|



. 

9-9 

## **Table 9-4:  Two-Day Demand Distribution** 

|**Demand**|**Probability**|
|---|---|
|8|4%|
|9|16%|
|10|28%|
|11|28%|
|12|17%|
|13|6%|
|14|1%|



Exercise 

Daily customer demand is expressed in batches as follows: 

(4, 20%), (5, 40%), (6, 30%), (7, 10%). 

Production is completely reliable and replaces inventory every two days.  Determine the target inventory for service levels of 90%, 95%, 99% and 99.9%. 

## 9.3.3 Unreliable Production – Discrete Distributed 

Suppose production is not reliable.  That is the number of days to replace inventory is a discrete random variable.  Further suppose that demand is a constant value. 

Let qj be the probability of taking exact j days to replace inventory.  Then the number of days, d, of inventory that should be kept is the smallest value of d that makes equation 9-13 true. 

_d_  _q j_[] _SL j_  1 

(9-13) 

## Exercise 

Daily customer demand is a constant 10 batches. 

The number of days to replenish the inventory is distributed as follows: (1, 75%), (2, 15%), (3, 7%), (4, 3%). 

Determine the target inventory for service levels of 90%, 95%, 99% and 99.9%. 

## 9.3.4 Unreliable Production and Random Demand – Both Discrete Distributed 

Now consider the application where production is unreliable and demand is random.  Both the number of days in which the inventory is re-supplied and the customer demand are discrete random variables.  Note that the question of interest is:  What is the distribution of the demand in the time taken to replenish the inventory? 

Consider the simplest application:  Production will take either one or two days to replenish the inventory. Thus, it is appropriate to use the one day demand for setting the inventory level with probability q1 and it is appropriate to use the two day demand for setting the inventory level with probability q2.  This means that the combined distribution of the demand and the number of days to replenish the inventory must be computed. 

9-10 

This will be illustrated with a numeric example.  Suppose customer demand expressed in batches is:  (1, 40%), (2, 30%), (3, 20%), (4, 10%).  Inventory can be replaced in either one day with probability 60% or two days with probability 40%. 

1. Compute the two day demand distribution. 

|Units|Probability|
|---|---|
|2|16.00%|
|3|24.00%|
|4|25.00%|
|5|20.00%|
|6|10.00%|
|7|4.00%|
|8|1.00%|
||100.00%|



2. Compute the one and two day conditional distributions.  The condition is that the inventory is replaced in that number of days.  The demand distribution is multiplied by the probability that the inventory is replaced in that number of days. 

||One dayDemand|One dayDemand||
|---|---|---|---|
|Units|Probability|Condition|Conditional<br>Probability|
|1|40%|60%|24.0%|
|2|30%|60%|18.0%|
|3|20%|60%|12.0%|
|4|10%|60%|6.0%|
||100%||60.0%|



||Two DayDemand|Two DayDemand||
|---|---|---|---|
|Units|Probability|Condition|Conditional<br>Probability|
|2|16%|40%|6.4%|
|3|24%|40%|9.6%|
|4|25%|40%|10.0%|
|5|20%|40%|8.0%|
|6|10%|40%|4.0%|
|7|4%|40%|1.6%|
|8|1%|40%|0.4%|
||100%||40.0%|



9-11 

3. Combine the two conditional distributions into a single distribution.  Add the conditional probabilities for all entries with the same number of units. 

|Combined Distribution|Combined Distribution|
|---|---|
|Units|Probability|
|1|24.0%|
|2|24.4%|
|3|21.6%|
|4|16.0%|
|5|8.0%|
|6|4.0%|
|7|1.6%|
|8|0.4%|
||100.0%|



Note that for a customer service level of 98%, six units would be kept in inventory. 

Exercise 

Daily customer demand is expressed in batches as follows: 

(4, 20%), (5, 40%), (6, 30%), (7, 10%). 

Production is completely not reliable is distributed as follows: (1, 80%), (2, 20%). 

Determine the target inventory for service levels of 90%, 95%, 99% and 99.9%. 

## 9.3.5 Production Quantities 

Replacing inventory means that the production volume each day is the same random variable as customer demand.  Thus, the quantity to produce varies from day to day (or every other day to every other day).  This can cause capacity and scheduling issues. 

## 9.3.6 Demand in Fixed Time Period 

Suppose the number of units (batches) demanded in fixed period of time, T, is of interest.  Suppose the time between demands is exponentially distributed.  It follows mathematically that the number of demands in a period of time T is Poisson distributed: 

_e_  _mean_ * _mean x p_ ( _x_ )  ; _x_ is a non - negative integer (9-14) x! 

where x is the number of units demanded and mean is the average number units demanded in time T. Often the mean must be computed by multiplying two quantities: 

1. The average number of units demanded per hour. 2. The number of hours in T. 

The Excel function Poisson can be used to compute probabilities using equation 9-14. 

Poisson(x, mean, FALSE). 

9-12 

A product has a mean demand of 1.5 units per hour.  Suppose production is constant with a takt time of 40 minutes (= 60 minutes / 1.5 units).  What is the distribution of the demand in the takt time? 

|Demand per<br>hour|1.5||
|---|---|---|
|Hours in T|0.666667||
|Mean demand in<br>T|1||
||||
|X|Probability|Cumulative|
|0|0.368|0.368|
|1|0.368|0.736|
|2|0.184|0.920|
|3|0.061|0.981|
|4|0.015|0.996|
|5|0.003|0.999|
|6|0.001|1.000|



How many units are needed in inventory for a 95% service level the takt time that is such that the probability of running out of inventory before a unit is replaced is 5%? 

## 9.3.7 Simulation Model of an Inventory Situation 

Consider a simulation model and experiment to validate the 95% service level in the previous example. Production produces an item to inventory at a constant rate of 1.5 units per hour, one unit every 40 minutes.  Since the demand is Poisson distributed it follows that the time between demands is exponentially distributed with a mean equal to the takt time of 40 minutes. 

The model is as follows.  There is one process for demands that take items from the inventory and one process for adding items back to the inventory. 

The initial conditions for any simulation experiment involving inventory must include the initial inventory level which is set to the target inventory value.  Determining the target inventory value was discussed in the previous sections in this chapter.  Each simulation language has its own requirements for setting the initial value of state variables such inventory levels. 

9-13 

Inventory demand and replenishment model 

|Define Arrivals:|||
|---|---|---|
|Demand Process|||
|Time of first arrival:|0||
|Time between arrivals: Exponentially distributed with a mean of 40 minutes|||
||Number of arrivals:|Infinite|
|Replenishment process|||
|Time of first arrival:|0||
|Time between arrivals: Constant 40 minutes|||
||Number of arrivals:|Infinite|
|Define Attributes:|||
|ArrivalTime|// Time of demand||
|Define State Variables:|||
|CurrentInventory=3|// Number of items inventory with an initial value of three||
|Demand Process|||
|Begin|||
|ArrivalTime = Clock|||
|Wait until CurrentInventory > 0 // Wait for an item in inventory|||
|CurrentInventory--|// Remove one item from inventory||
|// Record Service Level|||
|if ArrivalTime = Clock then|tabulate 100 in ServiceLevel||
|else|tabulate     0 in ServiceLevel||
|End|||
|Replenishment Process|||
|Begin|||
|CurrentInventory++|// Add item to inventory||
|End|||
|____________________________________________________________________________________|||



## **9.4 Introduction to Pull Inventory Management** 

The inventor of just-in-time manufacturing, Taiichi Ohno, defined the term _pull_ as follows: 

```
Manufacturers and workplaces can no longer base production on desktop
planning alone and then distribute, or push, them onto the market.  It
has become a matter of course for customers or users, each with a
different value system, to stand in the frontline of the marketplace
and, so to speak, pull the goods they need, in the amount and at the
time they need them.
```

A supermarket (grocery store) has long been a realization of a pull system.  Consider a shelf filled with cans of green beans.  As customers purchase cans of green beans, less cans remain on the shelf.  The staff of the grocery store restocks the shelf whenever too few cans remain.  New cans are taken from boxes of cans in the store room.  Whenever the number of boxes of cans in the store room becomes too few, additional boxes are ordered from the supplier of green beans. 

Note than in this pull system, shelves are restocked and consequently new cases of green beans are ordered depending on the number of cans on the shelves.  The number of cans on the shelves depends on current customer demand for green beans. 

9-14 

The alternative to a pull system, which is no longer commonly used, is a push system.  In a push system supermarket, the manager would forecast customer demand for green beans for the next time period, say a month.  The forecasted number of green beans would be ordered from the supplier.  The allocated shelf space would be stocked with cans of green beans.  If actual customer demand was less than the forecasted demand, the manager would need to have a sale to try to sell the excess cans of green beans. If the actual demand was greater than the forecasted demand, the manager would somehow need to acquire more green beans. 

This illustration points out one fundamental breakthrough of lean manufacturing: inventory levels, both work-in-process (WIP) and finished goods, are controlled characteristics of how a production system operates instead of a result of how it operates as in a push system. 

## 9.4.1 Kanban Systems:  One Implementation of the Pull Philosophy 

The most common implementation of the pull philosophy is kanban systems.  The Japanese word _kanban_ is usually translated into English as _card_ .  A kanban or card is attached to each part or batch of parts (tote, WIP rack, shelf, etc.).  To understand the significance of such cards, consider a single workstation followed by a finished goods inventory and proceeded by a raw materials inventory as shown in Figure 9- 3.  The following items shown in Figure 9-3 are specific to kanban systems. 

1. A move kanban shown as a half-moon shaped card attached to the items in the raw material inventory. 

2. A production kanban shown as diamond shaped card attached to the items in the finished goods inventory. 

3. Stockpoints: locations where kanbans are stored after removal from an item. 

The dynamics of this kanban system are as follows. 

1. A customer demand causes an item to be removed from the finished goods inventory.  The item is given to the customer and the diamond shaped kanban attached to the item is placed in the stockpoint near the finished goods inventory. 

2. Periodically, the diamond shaped kanbans are collected from the stockpoint and moved to the workstation.  The workstation must produce exactly one item for each diamond shaped kanban it receives.  Thus, the finished goods inventory is replenished.  Note only the inventory removed by customers is replaced. 

3. In order to produce a finished goods item, the workstation must use a raw material item.  The workstation receives a raw material item by taking a half-moon shaped kanban to the raw material inventory. 

Note the following characteristics of a kanban system. 

1. The amount of inventory in a kanban system is proportional to the number of kanbans in the system. 

2. Kanban cards and parts flow in oppose directions.  Kanbans flow from right to left and parts flow from left to right. 

3. The amount of finished goods inventory required depends on the time the workstation takes to produce a part and customer demand.  A lower bound on the finished goods inventory can be set given a customer service level, the expected time for the workstation to produce a part, and the probability distribution used to model customer demand. 

9-15 

Kanban systems can be implemented in a variety of ways.  As a second illustration, consider a modified version of the single workstation kanban system.  Suppose only one kanban type is used and information is passed electronically.  Such a system is shown in Figure 9-4 and operates as follows: 

1. A customer demands an item from the finished goods inventory.  The kanban is removed from the item and sent to the workstation immediately. 

2. The workstation takes the kanban to the raw material inventory to retrieve an item.  The kanban is attached to the item. 

3. The workstation processes the raw material into the finished good. 

4. The item with the kanban attached is taken to the finished goods inventory. 

The number of kanbans can be set using standard methods for establishing inventory levels that have been previously discussed.  Try the following problems. 

1. Demand for finished goods is Poisson distributed at the rate of 10 per hour.  Once an item has been removed from finished goods inventory, the system takes on the average 30 minutes to replace it.  How much finished goods inventory should be maintained for a 99% service level? 

2. Suppose for problem 1, the time in minutes to replace the inventory is distributed as follows:  (30, 60%; 40, 30%; 50, 10%).  How much inventory should be kept in this application? 

3. Suppose for problem 1, all inventory is kept in containers of size 4 parts.  There is one kanban per container.  How many kanbans are needed for this situation? 

Simulation of a kanban system is discussed in the next chapter. 

9-16 

## 9.4.2 CONWIP Systems:  A Second Implementation of the Pull Philosophy 

One simple way to control the maximum allowable WIP in a production area is to specify its maximum value.  This can be accomplished by using a near constant work-in-process system, or CONWIP system. A production area could be a single station, a set of stations, an entire serial line, an entire job shop, or an entire work cell. 

Figure 9.5 shows a small CONWIP system with maximum number of jobs in the production area equal to 2.  The rectangle encloses the production system that is under the CONWIP control.  Two jobs are in processing, one at each workstation.  Thus, the third job cannot enter the production system due to the CONWIP control limit of 2 jobs on the production line even though there is space for the job in the buffer of the first workstation.  This job should be waiting in an electronic queue of orders as opposed to occupying physical space outside of the CONWIP area. 

**Figure 9-5:  CONWIP System Illustration** 

9-17 

The following are some important characteristics or traits of a CONWIP system. 

1. The CONWIP limit is the only parameter of a CONWIP system. 

   - a. This parameter must be greater than or equal to the number of workstations in the production area.  If not, at least one of the workstations will always be starved. 

   - b. The ideal CONWIP limit is the smallest value that does not constrain throughput. 

   - c. In a _multiple_ product production area, each job, regardless of type, counts toward the capacity imposed by the _single_ CONWIP limit. 

2. A CONWIP system controls the maximum WIP in a production area. 

   - a. The maximum amount of waiting space before any work station is equal to the CONWIP limit or less.  It is possible, but unlikely, that all jobs are at the same station at the same time.  Thus, buffer sizes before workstations are usually not a constraint on system operation. 

   - b. If defective parts are detected at the last station on a production line, the CONWIP limit is the upper bound on the number of defective parts produced. 

   - c. A smaller footprint is needed for WIP storage. 

3. Jobs waiting to enter a production area are organized on an electronic or paper list.  No parts are waiting. 

   - a. The list can be re-ordered as needed so that the highest priority jobs are always at the head of the list.  For example, if an important customer asks for a rush job it can always be put at the head of the list.  The most number of jobs preceding the highest priority job is given by the CONWIP limit. 

   - b. If the mix of jobs changes, the CONWIP system dynamically adapts to the mix since the system has only one parameter. 

   - c. Recall Little’s Law: WIP = LT * TH.  In CONWIP system, WIP is almost constant. Thus, the lead time to produce is easy to predict given a throughput (demand) rate. With the WIP level controlled, the variability in the cycle time is reduced. 

4. For a given value of throughput, the average and maximum WIP level in a CONWIP system is less than in a non-CONWIP (push) system. 

5. In a CONWIP system, machines with excess capacity will be idle a noticeable amount of the time, which makes some managers very nervous and makes balancing the work between stations more important. 

6. Some CONWIP systems arise naturally as result of the material handling devices employed. For example, the amount of WIP may be limited by the number racks or totes available in the production area. 

A simulation model of a CONWIP control would include two processes: one for entering the CONWIP area and one for departing the CONWIP area as shown in the following. 

9-18 

CONWIP Processes Define State Variables: CONWIPLimit // Number of items allowed in CONWIP area CONWIPCurrent // Number of items currently in CONWIP area EnterCONWIPArea Process Begin Wait until CONWIPCurrent < CONWIPLimit // Wait for a space in the CONWIP area CONWIPCurrent++ // Add 1 to number in CONWIP area End Leave CONWIPArea Process Begin CONWIPCurrent-// Give back space in CONWIP Area End ____________________________________________________________________________________ 

Consider the average lead time of jobs in a production area with M workstations.  Each workstation has process time tj.  Then the average total processing time is given by summing the average processing times for all work stations yielding the raw processing time, equation 9-15. 

**==> picture [461 x 28] intentionally omitted <==**

Suppose the following: 

1. The CONWIP limit is set at N  M. 

2. The production area is balanced, that is the processing time at each station is about the same. 

3. Processing times are near constant. 

Then the following are true: 

_N_  _M_ 1. On the average at each workstation, a job will wait for other jobs.  M jobs are in _M_ 

processing, one at each station.  Thus N-M jobs must be waiting for processing.  It is equally likely that a job will be at any station.  Thus, the average number of jobs waiting at any station is given by the above quantity. 

**==> picture [426 x 27] intentionally omitted <==**

3. The total lead time at each station is: 

**==> picture [407 x 32] intentionally omitted <==**

9-19 

Suppose instead that processing times are random and exponentially distributed.  This is for practical purposes the practical worst case processing time since cT = 1. 

Then the following are true: 

- _N_  1 

- 1. On the average at each workstation, a job will wait for other jobs.  The other N -1 jobs _M_ 

- are each equally likely to be at any workstation. 

**==> picture [426 x 77] intentionally omitted <==**

## 9.4.3 POLCA: An Extension to CONWIP 

Suri (2010) proposes the Paired-cell Overlapping Loops of Cards with Authorization (POLCA) approach to control the maximum allowable WIP for jobs processed by any pair of Quick Response Manufacturing (QRM) cells.  POLCA can be viewed as an extension of CONWIP and is illustrated in Figure 9.6. 

**Figure 9-6:  POLCA Illustration** In Figure 9-6, there are two types of jobs: 1) those that are processed by QRM Cell A and QRM Cell B (AB jobs) as well as 2) those that are processed by QRM Cell A and QRM Cell C (A-C jobs).  The WIP for each type of job is controlled separately.  There is one maximum WIP value for A-B jobs and a second maximum WIP value for A-C jobs.  Thus, there are A-B cards in the system and A-C cards in the system. 

9-20 

To start processing a job, two criteria must be met. 

1. There is a card available for that job type, i.e. an A-B card for an A-B job, similar to CONWIP. 

2. The current date is at or after the projected start date for the job.  The start date is computed as the delivery date minus the allowed time to complete the job. 

The card is released for reuse when the job is completed in the second of the pair of cells.  That is an A-B card must be acquired before the job starts processing in QRM cell A and is released upon completion of processing in QRM cell B. 

The time allowed to complete the job could be determined by expert opinion, experience, the VUT equation or simulation. 

Suri suggests estimating the number of POLCA cards needed using Little’s Law. 

WIP = LT * TH 

WIP = # of POLCA cards LT = Lead time in the first QRM cell + Lead time in the second QRM Cell TH = Demand rate for jobs for example the number of jobs required per week. 

For example, if the average lead time in QRM cell A is 30 minutes, the average lead time in QRM cell B is 25 minutes, the demand per day is 30 units, and the working day is 16 hours then the number of A-B POLCA cards needed is  as follows: 

LT = (30 + 25)/60 = 0.92 hours TH = 30/16 = 1.875 units per hour Number of A-B POLCA cards = LT * TH = 2 

The following are some important characteristics or traits of a POLCA system. 

7. The POLCA limits are the only parameters of a POLCA system. 

   - a. If each of the QRM cells in a pair has only one POLCA card type, then POLCA is just like CONWIP. 

   - b. The ideal POLCA limits are the smallest values that do not constrain throughput, which may be greater than the limit estimated using Little’s Law. 

   - c. In a _multiple_ product QRM cell pair, each job, regardless of type, counts toward the capacity imposed by the _single_ POLCA limit for that pair of cells.  For example, there is one limit on the number of A-B POLCA cards regardless of the number of job types flowing from QRM cell A to QRM cell B. 

8. A POLCA system controls the maximum WIP in a production area. 

9. Jobs waiting to enter a production area are organized on an electronic or paper list.  No parts are waiting. 

   - a. The list can be re-ordered as needed so that the highest priority jobs are always at the head of the list.  For example, if an important customer asks for a rush job it can always be put at the head of the list.  The most number of jobs preceding the highest priority job is given by the sum of the POLCA limits. 

   - b. If the mix of jobs changes for any cell pair, the POLCA system dynamically adapts to the mix since there is only one parameter for the cell pair. 

10. In a POLCA system, machines with excess capacity will be idle a noticeable amount of the time, which makes some managers very nervous and makes balancing the work between stations more important. 

9-21 

A simulation model of a POLCA control would include two processes: one for entering the first POLCA cell and one for departing the second POLCA cell.  Note this is similar to the simulation model for a CONWIP system except there must be one variable for the POLCA limit for each cell pair.  In the following example there are two cell pairs:  A-B and A-C. 

|POLCA Processes|||
|---|---|---|
|Define Attributes|||
|JobType|// Type of job: either A-B|or A-C|
|Define State Variables:|||
|POLCALimitAB|// Number of items allowed in  QRM Cells A-B Processing||
|POLCACurrentAB|// Number of items currently in QRM Cells A-B Processing||
|POLCALimitAC|// Number of items allowed in  QRM Cells A-C Processing||
|POLCACurrentAC|// Number of items currently in QRM Cells A-C Processing||
|EnterPOLCAPair Process|||
|Begin|||
|If JobType = AB|||
|Begin|||
|Wait until POLCACurrentAB < POLCALimitAB||// Wait for a space in the QRM Cell Pair|
|POLCACurrentAB++||// Add 1 to number in QRM Cell Pair|
|End|||
|If JobType = AC|||
|Begin|||
|Wait until POLCACurrentAC < POLCALimitAC||// Wait for a space in the QRM Cell Pair|
|POLCACurrentAC++||// Add 1 to number in QRM Cell Pair|
|End|||
|End|||
|Leave CONWIPArea Process|||
|Begin|||
|If JobType = AB POLCACurrentAB--||// Give back space in QRM Cell Pair|
|If JobType = AC POLCACurrentAC--||// Give back space in QRM Cell Pair|
|End|||



**==> picture [467 x 1] intentionally omitted <==**

9-22 

## **Problems** 

1. If you were assigned problem 5 in chapter 7 then do the following. 

      - a. Add two inventories to the model one for each part type.  Arrivals represent demands for one part from a finished goods inventory.  One completion of production a part is added to the inventory. 

      - b. Add a CONWIP control to the model.  The control is around the three workstations. 

2. Suppose that demand for a product is forecast to be 1,000 units for the year.  Units may be obtained from another plant only on Fridays.  Create a graph of the average inventory level (Q/2) versus the number of orders per year to determine the optimal value of Q. 

3. Suppose the programs for a Lions home game cost $2.00 to print and sell for $5.00.  Program demand is normally distributed with a mean of 30,000 and a standard deviation of 2000. 

   - a. Based on the shortage cost and the overage cost, how many programs should be printed? 

   - b. Suppose the service level for program sales is 95%. i. How many programs should be printed? ii. What is the implied shortage cost? 

   - c. Construct a graph showing the number of programs printed and the implied shortage cost for service levels from 90% to 99% in increments of 1%. 

4. Suppose the Tigers print programs for a series at a time.  A three game weekend series with the Yankees is expected to draw 50,000 fans per game.  For **each** game, the demand for the programs is normally distributed with a mean of 30,000 and a standard deviation of 3,000.  How many programs should be printed for the **weekend** series for a service level of 99%?  Note:  You must determine the three day demand distribution first. 

5. Daily demand in pallets for a particular product made for a particular customer is distributed as follows: 

   - (5, 75%), (6, 18%), (7, 7%) 

   - a. How many pallets should be kept in inventory for a 90% service level?  For a 95% service level? 

   - b. Compute the 2-day distribution of demand. 

   - c. Suppose the inventory can only be re-supplied every 2-days.  How many pallets should be kept in inventory for each of the following service levels: 90%, 95%, 99%, and 99.5%? 

   - d. Suppose the inventory replenishment is unreliable.  The replenishment occurs in one day 75% of the time and in 2 days 25% of the time.  How many pallets should be kept in inventory for each of the following service levels: 90% and 99%? 

6. The inventory for a part is replaced every 4 hours.  Demand for the part is at the rate of 0.5 parts per hour.  How much inventory should be kept for a 99% service level?  Assume that demand is Poisson distributed. 

7. Consider a CONWIP system with 3 workstations.  The line is nearly balanced with constant processing times as follows (2.9, 3.2, 3.0) minutes. 

   - a. Derive an equation for the throughput rate given the equation for average part time in the system and Little’s Law. 

   - b. Construct a graph showing the cycle time as a function of the CONWIP limit N. 

9-23 

   - c. Construct a graph showing the throughput rate as a function of the CONWIP limit. d. Based on the graphs, select a CONWIP limit. 

8. Consider a CONWIP system with 3 workstations.  The line is nearly balanced with exponentially distributed processing times with means as follows (2.9, 3.2, 3.0) minutes. 

   - a. Derive an equation for the throughput rate given the equation for average part time in the system and Little’s Law. 

   - b. Construct a graph showing the cycle time as a function of the CONWIP limit N. 

   - c. Construct a graph showing the throughput rate as a function of the CONWIP limit. d. Based on the graphs, select a CONWIP limit. 

9. Consider a Kanban system with a finished goods inventory.  Inventory is stored in containers of size 6 items.  Customer demand is Poisson distributed with a rate of 10 per hour.  Replacement time is uniformly distributed between 2 and 4 hours.  Construct a curve showing the number of kanbans required for a 95% service level.  (Hint:  Consider replacement times of 2 hours, 2.25 hours, 2.50 hours, …, 4 hours). 

10. Estimate the number of POLCA cards needed using Little’s Law for the following pair of workstations. 

Demand:  100 pieces per 8 hour day, which is constant. 

QRM Cell A with one workstation:  Processing time is 4 minutes, exponentially distributed. 

QRM Cell B with one workstation:  Processing time is constant, 4 minutes. 

9-24
