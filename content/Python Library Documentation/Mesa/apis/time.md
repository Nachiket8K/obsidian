---
title: "Time"
source: "https://mesa.readthedocs.io/latest/apis/time.html"
imported_from: "Python library documentation"
library: "Mesa"
---

# Time

Underlying modules for event scheduling and time advancement.

This module provides the foundational data structures and classes needed for event-based
simulation in Mesa. The EventList class is a priority queue implementation that maintains
simulation events in chronological order while respecting event priorities. Key features:

- Priority-based event ordering
- Weak references to prevent memory leaks from canceled events
- Efficient event insertion and removal using a heap queue
- Support for event cancellation without breaking the heap structure

class Event(*time: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")*, *function: [Callable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Callable "(in Python v3.14)")[[...], [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *priority: [Priority](#mesa.time.Priority "mesa.time.events.Priority") = Priority.DEFAULT*, *function\_args: [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *function\_kwargs: [dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/mesa/time/events.html#Event)
:   A simulation event.

    The callable is wrapped using weakref, so there is no need to explicitly cancel event if e.g., an agent
    is removed from the simulation.

    time
    :   The simulation time of the event

        Type:
        :   [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)")

    fn
    :   The function to execute for this event

        Type:
        :   Callable

    priority
    :   The priority of the event

        Type:
        :   [Priority](#mesa.time.Priority "mesa.time.Priority")

    unique\_id
    :   Type:
        :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")

    function\_args list[Any]
    :   Argument for the function

    function\_kwargs dict[str, Any]
    :   Keyword arguments for the function

    Notes

    Simulation events use a weak reference to the callable.
    If the callback no longer exists at execution time (e.g., because an agent
    has been removed), execution will fail silently.
    Lambda callbacks are rejected at Event creation.

    Initialize a simulation event.

    Parameters:
    :   - **time** – the instant of time of the simulation event
        - **function** – the callable to invoke
        - **priority** – the priority of the event
        - **function\_args** – arguments for callable
        - **function\_kwargs** – keyword arguments for the callable

    execute() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/time/events.html#Event.execute)
    :   Execute this event.

    cancel() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/time/events.html#Event.cancel)
    :   Cancel this event.

class EventGenerator(*model: [Model](../mesa.html#mesa.model.Model "mesa.model.Model")*, *function: Callable[..., [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")]*, *schedule: [Schedule](#mesa.time.Schedule "mesa.time.Schedule")*, *priority: [Priority](#mesa.time.Priority "mesa.time.Priority") = Priority.DEFAULT*)[[source]](../_modules/mesa/time/events.html#EventGenerator)
:   A generator that creates recurring events based on a Schedule.

    Unlike a single Event, an EventGenerator is persistent and can be
    stopped or configured with stop conditions.

    model
    :   The model this generator belongs to

    function
    :   The callable to execute for each generated event

    schedule
    :   The Schedule defining when events occur

    priority
    :   Priority level for generated events

    Notes

    Event generators use a weak reference to the callable. Therefore, you cannot pass a lambda function in fn.
    A simulation event where the callable no longer exists (e.g., because the agent has been removed from the model)
    will fail silently. If you want to use functools.partial, please assign the partial function to a variable
    prior to creating the generator.

    Initialize an EventGenerator.

    Parameters:
    :   - **model** – The model this generator belongs to
        - **function** – The callable to execute for each generated event.
          Use functools.partial to bind arguments.
        - **schedule** – The Schedule defining timing
        - **priority** – Priority level for generated events

    property is\_active: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")
    :   Return whether the generator is currently active.

    property execution\_count: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")
    :   Return the number of times this generator has executed.

    property next\_scheduled\_time: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")
    :   Return the time of the next scheduled execution, or None if not scheduled.

    start() → [EventGenerator](#mesa.time.EventGenerator "mesa.time.events.EventGenerator")[[source]](../_modules/mesa/time/events.html#EventGenerator.start)
    :   Start the event generator.

        Returns:
        :   Self for method chaining

    stop() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/time/events.html#EventGenerator.stop)
    :   Stop the event generator immediately.

    pause() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/time/events.html#EventGenerator.pause)
    :   Pause the event generator temporarily.

        This cancels the currently scheduled event but keeps the generator
        active in the model. Execution can be resumed later using resume().

    resume() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/time/events.html#EventGenerator.resume)
    :   Resume a paused event generator.

class EventList[[source]](../_modules/mesa/time/events.html#EventList)
:   An event list.

    This is a heap queue sorted list of events. Events are always removed from the left, so heapq is a performant and
    appropriate data structure. Events are sorted based on their time stamp, their priority, and their unique\_id
    as a tie-breaker, guaranteeing a complete ordering.

    Initialize an event list.

    add\_event(*event: [Event](#mesa.time.Event "mesa.time.events.Event")*)[[source]](../_modules/mesa/time/events.html#EventList.add_event)
    :   Add the event to the event list.

        Parameters:
        :   **event** ([*Event*](#mesa.time.Event "mesa.time.Event")) – The event to be added

    peek\_ahead(*n: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[Event](#mesa.time.Event "mesa.time.events.Event")][[source]](../_modules/mesa/time/events.html#EventList.peek_ahead)
    :   Look at the first n non-canceled event in the event list.

        Parameters:
        :   **n** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")) – The number of events to look ahead

        Returns:
        :   list[Event]

        Raises:
        :   [**IndexError**](https://docs.python.org/3/library/exceptions.html#IndexError "(in Python v3.14)") – If the eventlist is empty

        Notes

        this method can return a list shorted then n if the number of non-canceled events on the event list
        is less than n.

    pop\_event() → [Event](#mesa.time.Event "mesa.time.events.Event")[[source]](../_modules/mesa/time/events.html#EventList.pop_event)
    :   Pop the first element from the event list.

    compact() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/time/events.html#EventList.compact)
    :   Remove all canceled events from the heap and rebuild it.

        If there are many canceled events, compaction can speed up performance substantially.

    is\_empty() → [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")[[source]](../_modules/mesa/time/events.html#EventList.is_empty)
    :   Return whether the event list is empty.

    remove(*event: [Event](#mesa.time.Event "mesa.time.events.Event")*) → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/time/events.html#EventList.remove)
    :   Remove an event from the event list.

        Parameters:
        :   **event** ([*Event*](#mesa.time.Event "mesa.time.Event")) – The event to be removed

    clear() → [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)")[[source]](../_modules/mesa/time/events.html#EventList.clear)
    :   Clear the event list.

class Priority(*\*values*)[[source]](../_modules/mesa/time/events.html#Priority)
:   Enumeration of priority levels.

    conjugate()
    :   Returns self, the complex conjugate of any int.

    bit\_length()
    :   Number of bits necessary to represent self in binary.

        ```
        >>> bin(37)
        '0b100101'
        >>> (37).bit_length()
        6
        ```

    bit\_count()
    :   Number of ones in the binary representation of the absolute value of self.

        Also known as the population count.

        ```
        >>> bin(13)
        '0b1101'
        >>> (13).bit_count()
        3
        ```

    to\_bytes(*length=1*, *byteorder='big'*, *\**, *signed=False*)
    :   Return an array of bytes representing an integer.

        length
        :   Length of bytes object to use. An OverflowError is raised if the
            integer is not representable with the given number of bytes. Default
            is length 1.

        byteorder
        :   The byte order used to represent the integer. If byteorder is ‘big’,
            the most significant byte is at the beginning of the byte array. If
            byteorder is ‘little’, the most significant byte is at the end of the
            byte array. To request the native byte order of the host system, use
            sys.byteorder as the byte order value. Default is to use ‘big’.

        signed
        :   Determines whether two’s complement is used to represent the integer.
            If signed is False and a negative integer is given, an OverflowError
            is raised.

    classmethod from\_bytes(*bytes*, *byteorder='big'*, *\**, *signed=False*)
    :   Return the integer represented by the given array of bytes.

        bytes
        :   Holds the array of bytes to convert. The argument must either
            support the buffer protocol or be an iterable object producing bytes.
            Bytes and bytearray are examples of built-in objects that support the
            buffer protocol.

        byteorder
        :   The byte order used to represent the integer. If byteorder is ‘big’,
            the most significant byte is at the beginning of the byte array. If
            byteorder is ‘little’, the most significant byte is at the end of the
            byte array. To request the native byte order of the host system, use
            sys.byteorder as the byte order value. Default is to use ‘big’.

        signed
        :   Indicates whether two’s complement is used to represent the integer.

    as\_integer\_ratio()
    :   Return a pair of integers, whose ratio is equal to the original int.

        The ratio is in lowest terms and has a positive denominator.

        ```
        >>> (10).as_integer_ratio()
        (10, 1)
        >>> (-10).as_integer_ratio()
        (-10, 1)
        >>> (0).as_integer_ratio()
        (0, 1)
        ```

    is\_integer()
    :   Returns True. Exists for duck type compatibility with float.is\_integer.

    real
    :   the real part of a complex number

    imag
    :   the imaginary part of a complex number

    numerator
    :   the numerator of a rational number in lowest terms

    denominator
    :   the denominator of a rational number in lowest terms

class Schedule(*interval: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | Callable[[[Model](../mesa.html#mesa.model.Model "mesa.model.Model")], [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] = 1.0*, *start: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *end: [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *count: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*)[[source]](../_modules/mesa/time/events.html#Schedule)
:   Defines when something should happen repeatedly.

    interval
    :   Time between executions (fixed value or callable returning value)

        Type:
        :   [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | Callable[[[Model](../mesa.html#mesa.model.Model "mesa.model.Model")], [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")]

    start
    :   Absolute time to begin (None = use current model time + interval)

        Type:
        :   [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | None

    end
    :   Absolute time to stop (None = no end)

        Type:
        :   [float](https://docs.python.org/3/library/functions.html#float "(in Python v3.14)") | None

    count
    :   Maximum executions (None = unlimited)

        Type:
        :   [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | None

On this page

[Show Source](../_sources/apis/time.md.txt)

---

Original source: https://mesa.readthedocs.io/latest/apis/time.html
