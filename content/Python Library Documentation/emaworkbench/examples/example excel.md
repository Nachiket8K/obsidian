---
title: "example_excel.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/example_excel.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# example\_excel.py

```
 1"""Illustration of the use the EMA classes for a model in Excel.
 2
 3It uses the excel file provided by
 4`A. Sharov <https://home.comcast.net/~sharov/PopEcol/lec10/fullmod.html>`_
 5
 6This excel file implements a simple predator prey model.
 7
 8"""
 9
10from ema_workbench import (
11    RealParameter,
12    TimeSeriesOutcome,
13    ema_logging,
14    perform_experiments,
15)
16from ema_workbench.connectors.excel import ExcelModel
17from ema_workbench.em_framework.evaluators import MultiprocessingEvaluator
18
19# Created on 27 Jul. 2011
20#
21# .. codeauthor:: jhkwakkel <j.h.kwakkel (at) tudelft (dot) nl>
22
23
24if __name__ == "__main__":
25    ema_logging.log_to_stderr(level=ema_logging.INFO)
26
27    model = ExcelModel(
28        "predatorPrey", wd="./models/excelModel", model_file="excel example.xlsx"
29    )
30    model.uncertainties = [
31        RealParameter("K2", 0.01, 0.2),
32        # we can refer to a cell in the normal way
33        # we can also use named cells
34        RealParameter("KKK", 450, 550),
35        RealParameter("rP", 0.05, 0.15),
36        RealParameter("aaa", 0.00001, 0.25),
37        RealParameter("tH", 0.45, 0.55),
38        RealParameter("kk", 0.1, 0.3),
39    ]
40
41    # specification of the outcomes
42    model.outcomes = [
43        TimeSeriesOutcome("B4:B1076"),
44        # we can refer to a range in the normal way
45        TimeSeriesOutcome("P_t"),
46    ]  # we can also use named range
47
48    # name of the sheet
49    model.default_sheet = "Sheet1"
50
51    with MultiprocessingEvaluator(model) as evaluator:
52        results = perform_experiments(
53            model, 100, reporting_interval=1, evaluator=evaluator
54        )
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/example_excel.html
