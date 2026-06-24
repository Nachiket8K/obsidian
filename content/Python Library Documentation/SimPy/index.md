---
title: "Overview"
source: "https://simpy.readthedocs.io/en/latest/index.html"
imported_from: "Python library documentation"
library: "SimPy"
---

![_images/simpy-logo-small.png](_images/simpy-logo-small.png)

Discrete event simulation for Python

[PyPI](https://pypi.python.org/pypi/simpy) |
[GitLab](https://gitlab.com/team-simpy/simpy/) |
[Issues](https://gitlab.com/groups/team-simpy/-/issues) |
[Mailing list](https://groups.google.com/forum/#!forum/python-simpy)

# Overview

SimPy is a process-based discrete-event simulation framework based on standard
Python.

Processes in SimPy are defined by Python [generator functions](http://docs.python.org/3/glossary.html#term-generator) and may, for example,
be used to model active components like customers, vehicles or agents. SimPy
also provides various types of [shared resources](topical_guides/resources.html#shared-resources) to
model limited capacity congestion points (like servers, checkout counters and
tunnels).

Simulations can be performed [“as fast as possible”](topical_guides/environments.html#simulation-control),
in [real time](topical_guides/real-time-simulations.html#realtime) (wall clock time) or by manually [stepping](topical_guides/environments.html#simulation-step) through the events.

Though it is theoretically possible to do continuous simulations with SimPy, it
has no features that help you with that. On the other hand, SimPy is overkill
for simulations with a fixed step size where your processes don’t interact with
each other or with shared resources.

A short example simulating two clocks ticking in different time intervals looks
like this:

```
>>> import simpy
>>>
>>> def clock(env, name, tick):
...     while True:
...         print(name, env.now)
...         yield env.timeout(tick)
...
>>> env = simpy.Environment()
>>> env.process(clock(env, 'fast', 0.5))
<Process(clock) object at 0x...>
>>> env.process(clock(env, 'slow', 1))
<Process(clock) object at 0x...>
>>> env.run(until=2)
fast 0
slow 0
fast 0.5
slow 1
fast 1.0
fast 1.5
```

The documentation contains a [tutorial](simpy_intro/index.html#intro), [several guides](topical_guides/index.html#guides) explaining key concepts, a number of [examples](examples/index.html#examples) and the [API reference](api_reference/index.html#api).

SimPy is released under the MIT License. Simulation model developers are
encouraged to share their SimPy modeling techniques with the SimPy community.
Please post a message to the [SimPy mailing list](https://groups.google.com/forum/#!forum/python-simpy).

There is an introductory talk that explains SimPy’s concepts and provides some
examples: [watch the video](https://www.youtube.com/watch?v=Bk91DoAEcjY) or
[get the slides](http://stefan.sofa-rockers.org/downloads/simpy-ep14.pdf).

SimPy has also been reimplemented in other programming languages. See the
[list of ports](about/ports.html#ports) for more details.

---

Original source: https://simpy.readthedocs.io/en/latest/index.html
