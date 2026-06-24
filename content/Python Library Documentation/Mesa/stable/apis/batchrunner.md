---
title: "Batchrunner"
source: "https://mesa.readthedocs.io/stable/apis/batchrunner.html"
imported_from: "Python library documentation"
library: "Mesa"
---

# Batchrunner

batchrunner for running a factorial experiment design over a model.

To take advantage of parallel execution of experiments, batch\_run uses
multiprocessing if `number_processes` is larger than 1. It is strongly advised
to only run in parallel using a normal python file (so don’t try to do it in a
jupyter notebook). This is because Jupyter notebooks have a different execution
model that can cause issues with Python’s multiprocessing module, especially on
Windows. The main problems include the lack of a traditional \_\_main\_\_ entry
point, serialization issues, and potential deadlocks.

Moreover, best practice when using multiprocessing is to
put the code inside an `if __name__ == '__main__':` code black as shown below:

```
from mesa.batchrunner import batch_run

params = {"width": 10, "height": 10, "N": range(10, 500, 10)}

if __name__ == '__main__':
    results = batch_run(
        MoneyModel,
        parameters=params,
        iterations=5,
        max_steps=100,
        number_processes=None,
        data_collection_period=1,
        display_progress=True,
    )
```

batch\_run(*model\_cls: [type](https://docs.python.org/3/library/functions.html#type "(in Python v3.14)")[[Model](../mesa.html#mesa.model.Model "mesa.model.Model")]*, *parameters: [Mapping](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)") | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]]*, *number\_processes: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = 1*, *iterations: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*, *data\_collection\_period: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = -1*, *max\_steps: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") = 1000*, *display\_progress: [bool](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)") = True*, *rng: [int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | integer | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | SeedSequence | [Iterable](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterable "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)") | integer | [Sequence](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "(in Python v3.14)")[[int](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")] | SeedSequence] | [None](https://docs.python.org/3/library/constants.html#None "(in Python v3.14)") = None*) → [list](https://docs.python.org/3/library/stdtypes.html#list "(in Python v3.14)")[[dict](https://docs.python.org/3/library/stdtypes.html#dict "(in Python v3.14)")[[str](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)"), [Any](https://docs.python.org/3/library/typing.html#typing.Any "(in Python v3.14)")]][[source]](../_modules/batchrunner.html#batch_run)
:   Batch run a mesa model with a set of parameter values.

    Parameters:
    :   - **model\_cls** (*Type**[*[*Model*](../mesa.html#mesa.model.Model "mesa.model.Model")*]*) – The model class to batch-run
        - **parameters** (*Mapping**[*[*str*](https://docs.python.org/3/library/stdtypes.html#str "(in Python v3.14)")*,* *Union**[**Any**,* *Iterable**[**Any**]**]**]*) – Dictionary with model parameters over which to run the model. You can either pass single values or iterables.
        - **number\_processes** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) – Number of processes used, by default 1. Set this to None if you want to use all CPUs.
        - **iterations** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) – Number of iterations for each parameter combination, by default 1
        - **data\_collection\_period** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) – Number of steps after which data gets collected, by default -1 (end of episode)
        - **max\_steps** ([*int*](https://docs.python.org/3/library/functions.html#int "(in Python v3.14)")*,* *optional*) – Maximum number of model steps after which the model halts, by default 1000
        - **display\_progress** ([*bool*](https://docs.python.org/3/library/functions.html#bool "(in Python v3.14)")*,* *optional*) – Display batch run process, by default True
        - **rng** – a valid value or iterable of values for seeding the random number generator in the model

    Returns:
    :   List[Dict[str, Any]]

    Notes

    batch\_run assumes the model has a datacollector attribute that has a DataCollector object initialized.

On this page

### This Page

- [Show Source](../_sources/apis/batchrunner.md.txt)

---

Original source: https://mesa.readthedocs.io/stable/apis/batchrunner.html
