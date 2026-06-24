---
title: "Process Communication"
source: "https://simpy.readthedocs.io/en/latest/examples/process_communication.html"
imported_from: "Python library documentation"
library: "SimPy"
---

# Process Communication

Covers:

- Resources: Store

This example shows how to interconnect simulation model elements together using
“resources.Store” for one-to-one, and many-to-one asynchronous processes. For
one-to-many a simple BroadCastPipe class is constructed from Store.

When Useful:
:   When a consumer process does not always wait on a generating process
    and these processes run asynchronously. This example shows how to
    create a buffer and also tell is the consumer process was late
    yielding to the event from a generating process.

    This is also useful when some information needs to be broadcast to
    many receiving processes

    Finally, using pipes can simplify how processes are interconnected to
    each other in a simulation model.

Example By:
:   Keith Smith

```
"""
Process communication example

Covers:

- Resources: Store

Scenario:
  This example shows how to interconnect simulation model elements
  together using :class:`~simpy.resources.store.Store` for one-to-one,
  and many-to-one asynchronous processes. For one-to-many a simple
  BroadCastPipe class is constructed from Store.

When Useful:
  When a consumer process does not always wait on a generating process
  and these processes run asynchronously. This example shows how to
  create a buffer and also tell is the consumer process was late
  yielding to the event from a generating process.

  This is also useful when some information needs to be broadcast to
  many receiving processes

  Finally, using pipes can simplify how processes are interconnected to
  each other in a simulation model.

Example By:
  Keith Smith

"""

import random

import simpy
import simpy.core

RANDOM_SEED = 42
SIM_TIME = 100

class BroadcastPipe:
    """A Broadcast pipe that allows one process to send messages to many.

    This construct is useful when message consumers are running at
    different rates than message generators and provides an event
    buffering to the consuming processes.

    The parameters are used to create a new
    :class:`~simpy.resources.store.Store` instance each time
    :meth:`get_output_conn()` is called.

    """

    def __init__(self, env, capacity=simpy.core.Infinity):
        self.env = env
        self.capacity = capacity
        self.pipes = []

    def put(self, value):
        """Broadcast a *value* to all receivers."""
        if not self.pipes:
            raise RuntimeError('There are no output pipes.')
        events = [store.put(value) for store in self.pipes]
        return self.env.all_of(events)  # Condition event for all "events"

    def get_output_conn(self):
        """Get a new output connection for this broadcast pipe.

        The return value is a :class:`~simpy.resources.store.Store`.

        """
        pipe = simpy.Store(self.env, capacity=self.capacity)
        self.pipes.append(pipe)
        return pipe

def message_generator(name, env, out_pipe):
    """A process which randomly generates messages."""
    while True:
        # wait for next transmission
        yield env.timeout(random.randint(6, 10))

        # messages are time stamped to later check if the consumer was
        # late getting them.  Note, using event.triggered to do this may
        # result in failure due to FIFO nature of simulation yields.
        # (i.e. if at the same env.now, message_generator puts a message
        # in the pipe first and then message_consumer gets from pipe,
        # the event.triggered will be True in the other order it will be
        # False
        msg = (env.now, f'{name} says hello at {env.now}')
        out_pipe.put(msg)

def message_consumer(name, env, in_pipe):
    """A process which consumes messages."""
    while True:
        # Get event for message pipe
        msg = yield in_pipe.get()

        if msg[0] < env.now:
            # if message was already put into pipe, then
            # message_consumer was late getting to it. Depending on what
            # is being modeled this, may, or may not have some
            # significance
            print(
                f'LATE Getting Message: at time {env.now}: '
                f'{name} received message: {msg[1]}'
            )

        else:
            # message_consumer is synchronized with message_generator
            print(f'at time {env.now}: {name} received message: {msg[1]}.')

        # Process does some other work, which may result in missing messages
        yield env.timeout(random.randint(4, 8))

# Setup and start the simulation
print('Process communication')
random.seed(RANDOM_SEED)
env = simpy.Environment()

# For one-to-one or many-to-one type pipes, use Store
pipe = simpy.Store(env)
env.process(message_generator('Generator A', env, pipe))
env.process(message_consumer('Consumer A', env, pipe))

print('\nOne-to-one pipe communication\n')
env.run(until=SIM_TIME)

# For one-to many use BroadcastPipe
# (Note: could also be used for one-to-one,many-to-one or many-to-many)
env = simpy.Environment()
bc_pipe = BroadcastPipe(env)

env.process(message_generator('Generator A', env, bc_pipe))
env.process(message_consumer('Consumer A', env, bc_pipe.get_output_conn()))
env.process(message_consumer('Consumer B', env, bc_pipe.get_output_conn()))

print('\nOne-to-many pipe communication\n')
env.run(until=SIM_TIME)
```

The simulation’s output:

```
Process communication

One-to-one pipe communication

at time 6: Consumer A received message: Generator A says hello at 6.
at time 12: Consumer A received message: Generator A says hello at 12.
at time 19: Consumer A received message: Generator A says hello at 19.
at time 26: Consumer A received message: Generator A says hello at 26.
at time 36: Consumer A received message: Generator A says hello at 36.
at time 46: Consumer A received message: Generator A says hello at 46.
at time 52: Consumer A received message: Generator A says hello at 52.
at time 58: Consumer A received message: Generator A says hello at 58.
LATE Getting Message: at time 66: Consumer A received message: Generator A says hello at 65
at time 75: Consumer A received message: Generator A says hello at 75.
at time 85: Consumer A received message: Generator A says hello at 85.
at time 95: Consumer A received message: Generator A says hello at 95.

One-to-many pipe communication

at time 10: Consumer A received message: Generator A says hello at 10.
at time 10: Consumer B received message: Generator A says hello at 10.
at time 18: Consumer A received message: Generator A says hello at 18.
at time 18: Consumer B received message: Generator A says hello at 18.
at time 27: Consumer A received message: Generator A says hello at 27.
at time 27: Consumer B received message: Generator A says hello at 27.
at time 34: Consumer A received message: Generator A says hello at 34.
at time 34: Consumer B received message: Generator A says hello at 34.
at time 40: Consumer A received message: Generator A says hello at 40.
LATE Getting Message: at time 41: Consumer B received message: Generator A says hello at 40
at time 46: Consumer A received message: Generator A says hello at 46.
LATE Getting Message: at time 47: Consumer B received message: Generator A says hello at 46
at time 56: Consumer A received message: Generator A says hello at 56.
at time 56: Consumer B received message: Generator A says hello at 56.
at time 65: Consumer A received message: Generator A says hello at 65.
at time 65: Consumer B received message: Generator A says hello at 65.
at time 74: Consumer A received message: Generator A says hello at 74.
at time 74: Consumer B received message: Generator A says hello at 74.
at time 82: Consumer A received message: Generator A says hello at 82.
at time 82: Consumer B received message: Generator A says hello at 82.
at time 92: Consumer A received message: Generator A says hello at 92.
at time 92: Consumer B received message: Generator A says hello at 92.
at time 98: Consumer B received message: Generator A says hello at 98.
at time 98: Consumer A received message: Generator A says hello at 98.
```

---

Original source: https://simpy.readthedocs.io/en/latest/examples/process_communication.html
