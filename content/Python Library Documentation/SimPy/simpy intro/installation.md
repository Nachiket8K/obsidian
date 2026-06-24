---
title: "Installation"
source: "https://simpy.readthedocs.io/en/latest/simpy_intro/installation.html"
imported_from: "Python library documentation"
library: "SimPy"
---

# Installation

SimPy is implemented in pure Python and has no dependencies. SimPy runs on
Python 3 (>= 3.8). PyPy3 is also supported. If you have [pip](http://pypi.python.org/pypi/pip) installed, just type

```
$ pip install simpy
```

and you are done.

## Installing from source

Alternatively, you can [download SimPy](http://pypi.python.org/pypi/SimPy/)
and install it manually. Extract the archive, open a terminal window where you
extracted SimPy and type:

```
$ python setup.py install
```

You can now optionally run SimPy’s tests to see if everything works fine. You
need [pytest](http://pytest.org) for this. Run the following command within
the source directory of SimPy:

```
$ py.test --pyargs simpy
```

## Upgrading from SimPy 2

If you are already familiar with SimPy 2, please read the Guide
[Porting from SimPy 2 to 3](../topical_guides/porting_from_simpy2.html#porting-from-simpy2).

## What’s Next

Now that you’ve installed SimPy, you probably want to simulate something. The
[next section](basic_concepts.html#basic-concepts) will introduce you to SimPy’s basic
concepts.

---

Original source: https://simpy.readthedocs.io/en/latest/simpy_intro/installation.html
