---
title: "simpy.util — Utility functions for SimPy"
source: "https://simpy.readthedocs.io/en/latest/api_reference/simpy.util.html"
imported_from: "Python library documentation"
library: "SimPy"
---

# `simpy.util` — Utility functions for SimPy

A collection of utility functions:

|  |  |
| --- | --- |
| [`start_delayed`](#simpy.util.start_delayed "simpy.util.start_delayed")(env, generator, delay) | Return a helper process that starts another process for *generator* after a certain *delay*. |

simpy.util.start\_delayed(*env: [Environment](simpy.core.html#simpy.core.Environment "simpy.core.Environment")*, *generator: [Generator](https://docs.python.org/3/library/typing.html#typing.Generator "(in Python v3.14)")[[Event](simpy.events.html#simpy.events.Event "simpy.events.Event"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]*, *delay: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*) → [Process](simpy.events.html#simpy.events.Process "simpy.events.Process")
:   Return a helper process that starts another process for *generator*
    after a certain *delay*.

    [`process()`](simpy.core.html#simpy.core.Environment.process "simpy.core.Environment.process") starts a process at the current
    simulation time. This helper allows you to start a process after a delay of
    *delay* simulation time units:

    ```
    >>> from simpy import Environment
    >>> from simpy.util import start_delayed
    >>> def my_process(env, x):
    ...     print(f'{env.now}, {x}')
    ...     yield env.timeout(1)
    ...
    >>> env = Environment()
    >>> proc = start_delayed(env, my_process(env, 3), 5)
    >>> env.run()
    5, 3
    ```

    Raise a [`ValueError`](https://docs.python.org/3/library/exceptions.html#ValueError "(in Python v3.14)") if `delay <= 0`.

---

Original source: https://simpy.readthedocs.io/en/latest/api_reference/simpy.util.html
