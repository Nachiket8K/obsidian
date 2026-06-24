---
title: "Machine Shop"
source: "https://simpy.readthedocs.io/en/latest/examples/machine_shop.html"
imported_from: "Python library documentation"
library: "SimPy"
---

# Machine Shop

Covers:

- Interrupts
- Resources: PreemptiveResource

This example comprises a workshop with *n* identical machines. A stream of jobs
(enough to keep the machines busy) arrives. Each machine breaks down
periodically. Repairs are carried out by one repairman. The repairman has
other, less important tasks to perform, too. Broken machines preempt theses
tasks. The repairman continues them when he is done with the machine repair.
The workshop works continuously.

A machine has two processes: *working* implements the actual behaviour of the
machine (producing parts). *break\_machine* periodically interrupts the
*working* process to simulate the machine failure.

The repairman’s other job is also a process (implemented by *other\_job*). The
repairman itself is a [`PreemptiveResource`](../api_reference/simpy.resources.html#simpy.resources.resource.PreemptiveResource "simpy.resources.resource.PreemptiveResource")
with a capacity of *1*. The machine repairing has a priority of *1*, while the
other job has a priority of *2* (the smaller the number, the higher the
priority).

```
"""
Machine shop example

Covers:

- Interrupts
- Resources: PreemptiveResource

Scenario:
  A workshop has *n* identical machines. A stream of jobs (enough to
  keep the machines busy) arrives. Each machine breaks down
  periodically. Repairs are carried out by one repairman. The repairman
  has other, less important tasks to perform, too. Broken machines
  preempt these tasks. The repairman continues them when he is done
  with the machine repair. The workshop works continuously.

"""

import random

import simpy

# fmt: off
RANDOM_SEED = 42
PT_MEAN = 10.0         # Avg. processing time in minutes
PT_SIGMA = 2.0         # Sigma of processing time
MTTF = 300.0           # Mean time to failure in minutes
BREAK_MEAN = 1 / MTTF  # Param. for expovariate distribution
REPAIR_TIME = 30.0     # Time it takes to repair a machine in minutes
JOB_DURATION = 30.0    # Duration of other jobs in minutes
NUM_MACHINES = 10      # Number of machines in the machine shop
WEEKS = 4              # Simulation time in weeks
SIM_TIME = WEEKS * 7 * 24 * 60  # Simulation time in minutes
# fmt: on

def time_per_part():
    """Return actual processing time for a concrete part."""
    t = random.normalvariate(PT_MEAN, PT_SIGMA)
    # The normalvariate can be negative, but we want only positive times.
    while t <= 0:
        t = random.normalvariate(PT_MEAN, PT_SIGMA)
    return t

def time_to_failure():
    """Return time until next failure for a machine."""
    return random.expovariate(BREAK_MEAN)

class Machine:
    """A machine produces parts and may get broken every now and then.

    If it breaks, it requests a *repairman* and continues the production
    after the it is repaired.

    A machine has a *name* and a number of *parts_made* thus far.

    """

    def __init__(self, env, name, repairman):
        self.env = env
        self.name = name
        self.parts_made = 0
        self.broken = False

        # Start "working" and "break_machine" processes for this machine.
        self.process = env.process(self.working(repairman))
        env.process(self.break_machine())

    def working(self, repairman):
        """Produce parts as long as the simulation runs.

        While making a part, the machine may break multiple times.
        Request a repairman when this happens.

        """
        while True:
            # Start making a new part
            done_in = time_per_part()
            while done_in:
                start = self.env.now
                try:
                    # Working on the part
                    yield self.env.timeout(done_in)
                    done_in = 0  # Set to 0 to exit while loop.

                except simpy.Interrupt:
                    self.broken = True
                    done_in -= self.env.now - start  # How much time left?

                    # Request a repairman. This will preempt its "other_job".
                    with repairman.request(priority=1) as req:
                        yield req
                        yield self.env.timeout(REPAIR_TIME)

                    self.broken = False

            # Part is done.
            self.parts_made += 1

    def break_machine(self):
        """Break the machine every now and then."""
        while True:
            yield self.env.timeout(time_to_failure())
            if not self.broken:
                # Only break the machine if it is currently working.
                self.process.interrupt()

def other_jobs(env, repairman):
    """The repairman's other (unimportant) job."""
    while True:
        # Start a new job
        done_in = JOB_DURATION
        while done_in:
            # Retry the job until it is done.
            # Its priority is lower than that of machine repairs.
            with repairman.request(priority=2) as req:
                yield req
                start = env.now
                try:
                    yield env.timeout(done_in)
                    done_in = 0
                except simpy.Interrupt:
                    done_in -= env.now - start

# Setup and start the simulation
print('Machine shop')
random.seed(RANDOM_SEED)  # This helps to reproduce the results

# Create an environment and start the setup process
env = simpy.Environment()
repairman = simpy.PreemptiveResource(env, capacity=1)
machines = [Machine(env, f'Machine {i}', repairman) for i in range(NUM_MACHINES)]
env.process(other_jobs(env, repairman))

# Execute!
env.run(until=SIM_TIME)

# Analysis/results
print(f'Machine shop results after {WEEKS} weeks')
for machine in machines:
    print(f'{machine.name} made {machine.parts_made} parts.')
```

The simulation’s output:

```
Machine shop
Machine shop results after 4 weeks
Machine 0 made 3251 parts.
Machine 1 made 3273 parts.
Machine 2 made 3242 parts.
Machine 3 made 3343 parts.
Machine 4 made 3387 parts.
Machine 5 made 3244 parts.
Machine 6 made 3269 parts.
Machine 7 made 3185 parts.
Machine 8 made 3302 parts.
Machine 9 made 3279 parts.
```

---

Original source: https://simpy.readthedocs.io/en/latest/examples/machine_shop.html
