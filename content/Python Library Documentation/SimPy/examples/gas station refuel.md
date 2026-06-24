---
title: "Gas Station Refueling"
source: "https://simpy.readthedocs.io/en/latest/examples/gas_station_refuel.html"
imported_from: "Python library documentation"
library: "SimPy"
---

# Gas Station Refueling

Covers:

- Resources: Resource
- Resources: Container
- Waiting for other processes

This examples models a gas station and cars that arrive at the station for
refueling.

The gas station has a limited number of fuel pumps and a fuel tank that is
shared between the fuel pumps. The gas station is thus modeled as
[`Resource`](../api_reference/simpy.resources.html#simpy.resources.resource.Resource "simpy.resources.resource.Resource"). The shared fuel tank is modeled
with a [`Container`](../api_reference/simpy.resources.html#simpy.resources.container.Container "simpy.resources.container.Container").

Vehicles arriving at the gas station first request a fuel pump from the
station. Once they acquire one, they try to take the desired amount of fuel
from the fuel pump. They leave when they are done.

The gas stations fuel level is regularly monitored by *gas station control*.
When the level drops below a certain threshold, a *tank truck* is called to
refuel the gas station itself.

```
"""
Gas Station Refueling example

Covers:

- Resources: Resource
- Resources: Container
- Waiting for other processes

Scenario:
  A gas station has a limited number of gas pumps that share a common
  fuel reservoir. Cars randomly arrive at the gas station, request one
  of the fuel pumps and start refueling from that reservoir.

  A gas station control process observes the gas station's fuel level
  and calls a tank truck for refueling if the station's level drops
  below a threshold.

"""

import itertools
import random

import simpy

# fmt: off
RANDOM_SEED = 42
STATION_TANK_SIZE = 200    # Size of the gas station tank (liters)
THRESHOLD = 25             # Station tank minimum level (% of full)
CAR_TANK_SIZE = 50         # Size of car fuel tanks (liters)
CAR_TANK_LEVEL = [5, 25]   # Min/max levels of car fuel tanks (liters)
REFUELING_SPEED = 2        # Rate of refuelling car fuel tank (liters / second)
TANK_TRUCK_TIME = 300      # Time it takes tank truck to arrive (seconds)
T_INTER = [30, 300]        # Interval between car arrivals [min, max] (seconds)
SIM_TIME = 1000            # Simulation time (seconds)
# fmt: on

def car(name, env, gas_station, station_tank):
    """A car arrives at the gas station for refueling.

    It requests one of the gas station's fuel pumps and tries to get the
    desired amount of fuel from it. If the station's fuel tank is
    depleted, the car has to wait for the tank truck to arrive.

    """
    car_tank_level = random.randint(*CAR_TANK_LEVEL)
    print(f'{env.now:6.1f} s: {name} arrived at gas station')
    with gas_station.request() as req:
        # Request one of the gas pumps
        yield req

        # Get the required amount of fuel
        fuel_required = CAR_TANK_SIZE - car_tank_level
        yield station_tank.get(fuel_required)

        # The "actual" refueling process takes some time
        yield env.timeout(fuel_required / REFUELING_SPEED)

        print(f'{env.now:6.1f} s: {name} refueled with {fuel_required:.1f}L')

def gas_station_control(env, station_tank):
    """Periodically check the level of the gas station tank and call the tank
    truck if the level falls below a threshold."""
    while True:
        if station_tank.level / station_tank.capacity * 100 < THRESHOLD:
            # We need to call the tank truck now!
            print(f'{env.now:6.1f} s: Calling tank truck')
            # Wait for the tank truck to arrive and refuel the station tank
            yield env.process(tank_truck(env, station_tank))

        yield env.timeout(10)  # Check every 10 seconds

def tank_truck(env, station_tank):
    """Arrives at the gas station after a certain delay and refuels it."""
    yield env.timeout(TANK_TRUCK_TIME)
    amount = station_tank.capacity - station_tank.level
    station_tank.put(amount)
    print(
        f'{env.now:6.1f} s: Tank truck arrived and refuelled station with {amount:.1f}L'
    )

def car_generator(env, gas_station, station_tank):
    """Generate new cars that arrive at the gas station."""
    for i in itertools.count():
        yield env.timeout(random.randint(*T_INTER))
        env.process(car(f'Car {i}', env, gas_station, station_tank))

# Setup and start the simulation
print('Gas Station refuelling')
random.seed(RANDOM_SEED)

# Create environment and start processes
env = simpy.Environment()
gas_station = simpy.Resource(env, 2)
station_tank = simpy.Container(env, STATION_TANK_SIZE, init=STATION_TANK_SIZE)
env.process(gas_station_control(env, station_tank))
env.process(car_generator(env, gas_station, station_tank))

# Execute!
env.run(until=SIM_TIME)
```

The simulation’s output:

```
Gas Station refuelling
  87.0 s: Car 0 arrived at gas station
 105.5 s: Car 0 refueled with 37.0L
 129.0 s: Car 1 arrived at gas station
 148.0 s: Car 1 refueled with 38.0L
 284.0 s: Car 2 arrived at gas station
 305.0 s: Car 2 refueled with 42.0L
 385.0 s: Car 3 arrived at gas station
 398.5 s: Car 3 refueled with 27.0L
 459.0 s: Car 4 arrived at gas station
 460.0 s: Calling tank truck
 481.0 s: Car 4 refueled with 44.0L
 705.0 s: Car 5 arrived at gas station
 750.0 s: Car 6 arrived at gas station
 760.0 s: Tank truck arrived and refuelled station with 188.0L
 779.0 s: Car 6 refueled with 38.0L
 781.5 s: Car 5 refueled with 43.0L
 891.0 s: Car 7 arrived at gas station
 904.0 s: Car 7 refueled with 26.0L
```

---

Original source: https://simpy.readthedocs.io/en/latest/examples/gas_station_refuel.html
