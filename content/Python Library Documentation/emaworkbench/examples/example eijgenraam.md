---
title: "example_eijgenraam.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/example_eijgenraam.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# example\_eijgenraam.py

```
  1"""Eigenraam model with the workbench.
  2
  3This showcases how you can use the workbench with non-uniform distributions.
  4
  5"""
  6
  7# Created on 12 Mar 2020
  8#
  9# .. codeauthor::  jhkwakkel
 10
 11import bisect
 12import functools
 13import math
 14import operator
 15
 16import numpy as np
 17import scipy as sp
 18
 19from ema_workbench import (
 20    Model,
 21    MultiprocessingEvaluator,
 22    RealParameter,
 23    ScalarOutcome,
 24    ema_logging,
 25)
 26
 27##==============================================================================
 28## Implement the model described by Eijgenraam et al. (2012)
 29# code taken from Rhodium Eijgenraam example
 30##------------------------------------------------------------------------------
 31
 32# Parameters pulled from the paper describing each dike ring
 33params = ("c", "b", "lam", "alpha", "eta", "zeta", "v_0", "p_0", "max_Pf")
 34raw_data = {
 35    10: (16.6939, 0.6258, 0.0014, 0.033027, 0.320, 0.003774, 1564.9, 0.00044, 1 / 2000),
 36    11: (42.6200, 1.7068, 0.0000, 0.032000, 0.320, 0.003469, 1700.1, 0.00117, 1 / 2000),
 37    15: (
 38        125.6422,
 39        1.1268,
 40        0.0098,
 41        0.050200,
 42        0.760,
 43        0.003764,
 44        11810.4,
 45        0.00137,
 46        1 / 2000,
 47    ),
 48    16: (
 49        324.6287,
 50        2.1304,
 51        0.0100,
 52        0.057400,
 53        0.760,
 54        0.002032,
 55        22656.5,
 56        0.00110,
 57        1 / 2000,
 58    ),
 59    22: (
 60        154.4388,
 61        0.9325,
 62        0.0066,
 63        0.070000,
 64        0.620,
 65        0.002893,
 66        9641.1,
 67        0.00055,
 68        1 / 2000,
 69    ),
 70    23: (26.4653, 0.5250, 0.0034, 0.053400, 0.800, 0.002031, 61.6, 0.00137, 1 / 2000),
 71    24: (71.6923, 1.0750, 0.0059, 0.043900, 1.060, 0.003733, 2706.4, 0.00188, 1 / 2000),
 72    35: (49.7384, 0.6888, 0.0088, 0.036000, 1.060, 0.004105, 4534.7, 0.00196, 1 / 2000),
 73    38: (24.3404, 0.7000, 0.0040, 0.025321, 0.412, 0.004153, 3062.6, 0.00171, 1 / 1250),
 74    41: (
 75        58.8110,
 76        0.9250,
 77        0.0033,
 78        0.025321,
 79        0.422,
 80        0.002749,
 81        10013.1,
 82        0.00171,
 83        1 / 1250,
 84    ),
 85    42: (21.8254, 0.4625, 0.0019, 0.026194, 0.442, 0.001241, 1090.8, 0.00171, 1 / 1250),
 86    43: (
 87        340.5081,
 88        4.2975,
 89        0.0043,
 90        0.025321,
 91        0.448,
 92        0.002043,
 93        19767.6,
 94        0.00171,
 95        1 / 1250,
 96    ),
 97    44: (
 98        24.0977,
 99        0.7300,
100        0.0054,
101        0.031651,
102        0.316,
103        0.003485,
104        37596.3,
105        0.00033,
106        1 / 1250,
107    ),
108    45: (3.4375, 0.1375, 0.0069, 0.033027, 0.320, 0.002397, 10421.2, 0.00016, 1 / 1250),
109    47: (8.7813, 0.3513, 0.0026, 0.029000, 0.358, 0.003257, 1369.0, 0.00171, 1 / 1250),
110    48: (35.6250, 1.4250, 0.0063, 0.023019, 0.496, 0.003076, 7046.4, 0.00171, 1 / 1250),
111    49: (20.0000, 0.8000, 0.0046, 0.034529, 0.304, 0.003744, 823.3, 0.00171, 1 / 1250),
112    50: (8.1250, 0.3250, 0.0000, 0.033027, 0.320, 0.004033, 2118.5, 0.00171, 1 / 1250),
113    51: (15.0000, 0.6000, 0.0071, 0.036173, 0.294, 0.004315, 570.4, 0.00171, 1 / 1250),
114    52: (49.2200, 1.6075, 0.0047, 0.036173, 0.304, 0.001716, 4025.6, 0.00171, 1 / 1250),
115    53: (69.4565, 1.1625, 0.0028, 0.031651, 0.336, 0.002700, 9819.5, 0.00171, 1 / 1250),
116}
117data = {i: dict(zip(params, raw_data[i])) for i in raw_data}
118
119# Set the ring we are analyzing
120ring = 15
121max_failure_probability = data[ring]["max_Pf"]
122
123
124#
125def exponential_investment_cost(
126    u,  # increase in dike height
127    h0,  # original height of the dike
128    c,  # constant from Table 1
129    b,  # constant from Table 1
130    lam,
131):  # constant from Table 1
132    """Compute the investment cost to increase the dike height."""
133    if u == 0:
134        return 0
135    else:
136        return (c + b * u) * math.exp(lam * (h0 + u))
137
138
139def eijgenraam_model(
140    x_1,
141    x_2,
142    x_3,
143    x_4,
144    x_5,
145    x_6,
146    t_1,
147    t_2,
148    t_3,
149    t_4,
150    t_5,
151    t_6,
152    t=300,
153    p_0=data[ring]["p_0"],
154    v_0=data[ring]["v_0"],
155    alpha=data[ring]["alpha"],
156    delta=0.04,
157    eta=data[ring]["eta"],
158    gamma=0.035,
159    rho=0.015,
160    zeta=data[ring]["zeta"],
161    c=data[ring]["c"],
162    b=data[ring]["b"],
163    lam=data[ring]["lam"],
164):
165    """Python implementation of the Eijgenraam model.
166
167    Params
168    ------
169    Xs : list
170         list of dike heightenings
171    Ts : list
172         time of dike heightenings
173    T : int, optional
174        planning horizon
175    p_0 : <>, optional
176         constant from Table 1
177    v_0 : <>, optional
178         constant from Table 1
179    alpha : <>, optional
180            constant from Table 1
181    delta : float, optional
182            discount rate, mentioned in Section 2.2
183    eta : <>, optional
184          constant from Table 1
185    gamma : float, optional
186            paper says this is taken from government report, but no indication
187            of actual value
188    rho : float, optional
189          risk-free rate, mentioned in Section 2.2
190    zeta : <>, optional
191           constant from Table 1
192    c : <>, optional
193        constant from Table 1
194    b : <>, optional
195        constant from Table 1
196    lam : <>, optional
197         constant from Table 1
198
199    """
200    t_s = [t_1, t_2, t_3, t_4, t_5, t_6]
201    x_s = [x_1, x_2, x_3, x_4, x_5, x_6]
202
203    t_s = [
204        int(t_s[i] + sum(t_s[:i])) for i in range(len(t_s)) if t_s[i] + sum(t_s[:i]) < t
205    ]
206    x_s = x_s[: len(t_s)]
207
208    if len(t_s) == 0:
209        t_s = [0]
210        x_s = [0]
211
212    if t_s[0] > 0:
213        t_s.insert(0, 0)
214        x_s.insert(0, 0)
215
216    s_0 = p_0 * v_0
217    beta = alpha * eta + gamma - rho
218    theta = alpha - zeta
219
220    # calculate investment
221    investment = 0
222
223    for i in range(len(x_s)):
224        step_cost = exponential_investment_cost(
225            x_s[i], 0 if i == 0 else sum(x_s[:i]), c, b, lam
226        )
227        step_discount = math.exp(-delta * t_s[i])
228        investment += step_cost * step_discount
229
230    # calculate expected losses
231    losses = 0
232
233    for i in range(len(x_s) - 1):
234        losses += math.exp(-theta * sum(x_s[: (i + 1)])) * (
235            math.exp((beta - delta) * t_s[i + 1]) - math.exp((beta - delta) * t_s[i])
236        )
237
238    if t_s[-1] < t:
239        losses += math.exp(-theta * sum(x_s)) * (
240            math.exp((beta - delta) * t) - math.exp((beta - delta) * t_s[-1])
241        )
242
243    losses = losses * s_0 / (beta - delta)
244
245    # salvage term
246    losses += (
247        s_0
248        * math.exp(beta * t)
249        * math.exp(-theta * sum(x_s))
250        * math.exp(-delta * t)
251        / delta
252    )
253
254    def find_height(t):
255        if t < t_s[0]:
256            return 0
257        elif t > t_s[-1]:
258            return sum(x_s)
259        else:
260            return sum(x_s[: bisect.bisect_right(t_s, t)])
261
262    failure_probability = [
263        p_0 * np.exp(alpha * eta * t) * np.exp(-alpha * find_height(t))
264        for t in range(t + 1)
265    ]
266    total_failure = 1 - functools.reduce(
267        operator.mul, [1 - p for p in failure_probability], 1
268    )
269    mean_failure = sum(failure_probability) / (t + 1)
270    max_failure = max(failure_probability)
271
272    return (
273        investment,
274        losses,
275        investment + losses,
276        total_failure,
277        mean_failure,
278        max_failure,
279    )
280
281
282if __name__ == "__main__":
283    model = Model("eijgenraam", eijgenraam_model)
284
285    model.responses = [
286        ScalarOutcome("TotalInvestment", ScalarOutcome.INFO),
287        ScalarOutcome("TotalLoss", ScalarOutcome.INFO),
288        ScalarOutcome("TotalCost", ScalarOutcome.MINIMIZE),
289        ScalarOutcome("TotalFailureProb", ScalarOutcome.INFO),
290        ScalarOutcome("AvgFailureProb", ScalarOutcome.MINIMIZE),
291        ScalarOutcome("MaxFailureProb", ScalarOutcome.MINIMIZE),
292    ]
293
294    # Set uncertainties
295    model.uncertainties = [
296        RealParameter.from_dist("p_0", sp.stats.lognorm(scale=0.00137, s=0.25)),
297        # @UndefinedVariable
298        RealParameter.from_dist("alpha", sp.stats.norm(loc=0.0502, scale=0.01)),
299        # @UndefinedVariable
300        RealParameter.from_dist("eta", sp.stats.lognorm(scale=0.76, s=0.1)),
301    ]  # @UndefinedVariable
302
303    # having a list like parameter were values are automagically wrappen
304    # into a list can be quite useful.....
305    model.levers = [RealParameter(f"x_{i}", 0, 500) for i in range(1, 7)] + [
306        RealParameter(f"t_{i}", 0, 300) for i in range(1, 7)
307    ]
308
309    ema_logging.log_to_stderr(ema_logging.INFO)
310
311    with MultiprocessingEvaluator(model, n_processes=-1) as evaluator:
312        results = evaluator.perform_experiments(1000, 4)
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/example_eijgenraam.html
