---
title: "example_flu.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/example_flu.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# example\_flu.py

```
  1"""An illustration of the use of the workbench for a model specified in Python itself.
  2
  3The example is based on `Pruyt & Hamarat <https://www.systemdynamics.org/conferences/2010/proceed/papers/P1253.pdf>`_.
  4For comparison, run both this model and example_flu_vensim_no_policy.py.
  5
  6"""
  7
  8import matplotlib.pyplot as plt
  9import numpy as np
 10from numpy import exp, min, sin
 11
 12from ema_workbench import (
 13    Model,
 14    RealParameter,
 15    SequentialEvaluator,
 16    TimeSeriesOutcome,
 17    ema_logging,
 18    perform_experiments,
 19)
 20from ema_workbench.analysis import Density, lines
 21
 22# Created on 20 dec. 2010
 23# .. codeauthor:: jhkwakkel <j.h.kwakkel (at) tudelft (dot) nl>
 24#                 chamarat <c.hamarat  (at) tudelft (dot) nl>
 25
 26
 27# =============================================================================
 28#
 29#    the model itself
 30#
 31# =============================================================================
 32
 33FINAL_TIME = 48
 34INITIAL_TIME = 0
 35TIME_STEP = 0.0078125
 36
 37switch_regions = 1.0
 38switch_immunity = 1.0
 39switch_deaths = 1.0
 40switch_immunity_cap = 1.0
 41
 42
 43def lookup_function_x(variable, start, end, step, skew, growth, v=0.5):
 44    """A basic lookup function."""
 45    return start + (
 46        (end - start) / ((1 + skew * exp(-growth * (variable - step))) ** (1 / v))
 47    )
 48
 49
 50def flu_model(
 51    x11=0,
 52    x12=0,
 53    x21=0,
 54    x22=0,
 55    x31=0,
 56    x32=0,
 57    x41=0,
 58    x51=0,
 59    x52=0,
 60    x61=0,
 61    x62=0,
 62    x81=0,
 63    x82=0,
 64    x91=0,
 65    x92=0,
 66    x101=0,
 67    x102=0,
 68):
 69    """The overall model."""
 70    # Assigning initial values
 71    additional_seasonal_immune_population_fraction_r1 = float(x11)
 72    additional_seasonal_immune_population_fraction_r2 = float(x12)
 73
 74    fatality_rate_region_1 = float(x21)
 75    fatality_rate_region_2 = float(x22)
 76
 77    initial_immune_fraction_of_the_population_of_region_1 = float(x31)
 78    initial_immune_fraction_of_the_population_of_region_2 = float(x32)
 79
 80    normal_interregional_contact_rate = float(x41)
 81    interregional_contact_rate = switch_regions * normal_interregional_contact_rate
 82
 83    permanent_immune_population_fraction_r1 = float(x51)
 84    permanent_immune_population_fraction_r2 = float(x52)
 85
 86    recovery_time_region_1 = float(x61)
 87    recovery_time_region_2 = float(x62)
 88
 89    susceptible_to_immune_population_delay_time_region_1 = 1
 90    susceptible_to_immune_population_delay_time_region_2 = 1
 91
 92    root_contact_rate_region_1 = float(x81)
 93    root_contact_rate_region_2 = float(x82)
 94
 95    infection_rate_region_1 = float(x91)
 96    infection_rate_region_2 = float(x92)
 97
 98    normal_contact_rate_region_1 = float(x101)
 99    normal_contact_rate_region_2 = float(x102)
100
101    ######
102    susceptible_to_immune_population_flow_region_1 = 0.0
103    susceptible_to_immune_population_flow_region_2 = 0.0
104    ######
105
106    initial_value_population_region_1 = 6.0 * 10**8
107    initial_value_population_region_2 = 3.0 * 10**9
108
109    initial_value_infected_population_region_1 = 10.0
110    initial_value_infected_population_region_2 = 10.0
111
112    initial_value_immune_population_region_1 = (
113        switch_immunity
114        * initial_immune_fraction_of_the_population_of_region_1
115        * initial_value_population_region_1
116    )
117    initial_value_immune_population_region_2 = (
118        switch_immunity
119        * initial_immune_fraction_of_the_population_of_region_2
120        * initial_value_population_region_2
121    )
122
123    initial_value_susceptible_population_region_1 = (
124        initial_value_population_region_1 - initial_value_immune_population_region_1
125    )
126    initial_value_susceptible_population_region_2 = (
127        initial_value_population_region_2 - initial_value_immune_population_region_2
128    )
129
130    recovered_population_region_1 = 0.0
131    recovered_population_region_2 = 0.0
132
133    infected_population_region_1 = initial_value_infected_population_region_1
134    infected_population_region_2 = initial_value_infected_population_region_2
135
136    susceptible_population_region_1 = initial_value_susceptible_population_region_1
137    susceptible_population_region_2 = initial_value_susceptible_population_region_2
138
139    immune_population_region_1 = initial_value_immune_population_region_1
140    immune_population_region_2 = initial_value_immune_population_region_2
141
142    deceased_population_region_1 = [0.0]
143    deceased_population_region_2 = [0.0]
144    run_time = [INITIAL_TIME]
145
146    # --End of Initialization--
147
148    max_infected = 0.0
149
150    for time in range(int(INITIAL_TIME / TIME_STEP), int(FINAL_TIME / TIME_STEP)):
151        run_time.append(run_time[-1] + TIME_STEP)
152        total_population_region_1 = (
153            infected_population_region_1
154            + recovered_population_region_1
155            + susceptible_population_region_1
156            + immune_population_region_1
157        )
158        total_population_region_2 = (
159            infected_population_region_2
160            + recovered_population_region_2
161            + susceptible_population_region_2
162            + immune_population_region_2
163        )
164
165        infected_population_region_1 = max(0, infected_population_region_1)
166        infected_population_region_2 = max(0, infected_population_region_2)
167
168        infected_fraction_region_1 = (
169            infected_population_region_1 / total_population_region_1
170        )
171        infected_fraction_region_2 = (
172            infected_population_region_2 / total_population_region_2
173        )
174
175        impact_infected_population_on_contact_rate_region_1 = 1 - (
176            infected_fraction_region_1 ** (1 / root_contact_rate_region_1)
177        )
178        impact_infected_population_on_contact_rate_region_2 = 1 - (
179            infected_fraction_region_2 ** (1 / root_contact_rate_region_2)
180        )
181
182        #        if ((time*TIME_STEP) >= 4) and ((time*TIME_STEP)<=10):
183        #            normal_contact_rate_region_1 = float(x101)*(1 - 0.5)
184        #        else:normal_contact_rate_region_1 = float(x101)
185
186        normal_contact_rate_region_1 = float(x101) * (
187            1 - lookup_function_x(infected_fraction_region_1, 0, 1, 0.15, 0.75, 15)
188        )
189
190        contact_rate_region_1 = (
191            normal_contact_rate_region_1
192            * impact_infected_population_on_contact_rate_region_1
193        )
194        contact_rate_region_2 = (
195            normal_contact_rate_region_2
196            * impact_infected_population_on_contact_rate_region_2
197        )
198
199        recoveries_region_1 = (
200            (1 - (fatality_rate_region_1 * switch_deaths))
201            * infected_population_region_1
202            / recovery_time_region_1
203        )
204        recoveries_region_2 = (
205            (1 - (fatality_rate_region_2 * switch_deaths))
206            * infected_population_region_2
207            / recovery_time_region_2
208        )
209
210        flu_deaths_region_1 = (
211            fatality_rate_region_1
212            * switch_deaths
213            * infected_population_region_1
214            / recovery_time_region_1
215        )
216        flu_deaths_region_2 = (
217            fatality_rate_region_2
218            * switch_deaths
219            * infected_population_region_2
220            / recovery_time_region_2
221        )
222
223        infections_region_1 = (
224            susceptible_population_region_1
225            * contact_rate_region_1
226            * infection_rate_region_1
227            * infected_fraction_region_1
228        ) + (
229            susceptible_population_region_1
230            * interregional_contact_rate
231            * infection_rate_region_1
232            * infected_fraction_region_2
233        )
234        infections_region_2 = (
235            susceptible_population_region_2
236            * contact_rate_region_2
237            * infection_rate_region_2
238            * infected_fraction_region_2
239        ) + (
240            susceptible_population_region_2
241            * interregional_contact_rate
242            * infection_rate_region_2
243            * infected_fraction_region_1
244        )
245
246        infected_population_region_1_next = infected_population_region_1 + (
247            TIME_STEP
248            * (infections_region_1 - flu_deaths_region_1 - recoveries_region_1)
249        )
250        infected_population_region_2_next = infected_population_region_2 + (
251            TIME_STEP
252            * (infections_region_2 - flu_deaths_region_2 - recoveries_region_2)
253        )
254
255        if (
256            infected_population_region_1_next < 0
257            or infected_population_region_2_next < 0
258        ):
259            pass
260
261        recovered_population_region_1_next = recovered_population_region_1 + (
262            TIME_STEP * recoveries_region_1
263        )
264        recovered_population_region_2_next = recovered_population_region_2 + (
265            TIME_STEP * recoveries_region_2
266        )
267
268        if fatality_rate_region_1 >= 0.025:
269            qw = 1.0
270        elif fatality_rate_region_1 >= 0.01:
271            qw = 0.8
272        elif fatality_rate_region_1 >= 0.001:
273            qw = 0.6
274        elif fatality_rate_region_1 >= 0.0001:
275            qw = 0.4
276        else:
277            qw = 0.2
278
279        if (time * TIME_STEP) <= 10:
280            normal_immune_population_fraction_region_1 = (
281                additional_seasonal_immune_population_fraction_r1 / 2
282            ) * sin(4.5 + (time * TIME_STEP / 2)) + (
283                (
284                    (2 * permanent_immune_population_fraction_r1)
285                    + additional_seasonal_immune_population_fraction_r1
286                )
287                / 2
288            )
289        else:
290            normal_immune_population_fraction_region_1 = max(
291                (
292                    float(qw),
293                    (additional_seasonal_immune_population_fraction_r1 / 2)
294                    * sin(4.5 + (time * TIME_STEP / 2))
295                    + (
296                        (
297                            (2 * permanent_immune_population_fraction_r1)
298                            + additional_seasonal_immune_population_fraction_r1
299                        )
300                        / 2
301                    ),
302                )
303            )
304
305        normal_immune_population_fraction_region_2 = switch_immunity_cap * min(
306            (
307                (
308                    sin((time * TIME_STEP / 2) + 1.5)
309                    * additional_seasonal_immune_population_fraction_r2
310                    / 2
311                )
312                + (
313                    (
314                        (2 * permanent_immune_population_fraction_r2)
315                        + additional_seasonal_immune_population_fraction_r2
316                    )
317                    / 2
318                ),
319                (
320                    permanent_immune_population_fraction_r1
321                    + additional_seasonal_immune_population_fraction_r1
322                ),
323            ),
324        ) + (
325            (1 - switch_immunity_cap)
326            * (
327                (
328                    sin((time * TIME_STEP / 2) + 1.5)
329                    * additional_seasonal_immune_population_fraction_r2
330                    / 2
331                )
332                + (
333                    (
334                        (2 * permanent_immune_population_fraction_r2)
335                        + additional_seasonal_immune_population_fraction_r2
336                    )
337                    / 2
338                )
339            )
340        )
341
342        normal_immune_population_region_1 = (
343            normal_immune_population_fraction_region_1 * total_population_region_1
344        )
345        normal_immune_population_region_2 = (
346            normal_immune_population_fraction_region_2 * total_population_region_2
347        )
348
349        if switch_immunity == 1:
350            susminreg1_1 = (
351                normal_immune_population_region_1 - immune_population_region_1
352            ) / susceptible_to_immune_population_delay_time_region_1
353            susminreg1_2 = (
354                susceptible_population_region_1
355                / susceptible_to_immune_population_delay_time_region_1
356            )
357            susmaxreg1 = -(
358                immune_population_region_1
359                / susceptible_to_immune_population_delay_time_region_1
360            )
361            if (susmaxreg1 >= susminreg1_1) or (susmaxreg1 >= susminreg1_2):
362                susceptible_to_immune_population_flow_region_1 = susmaxreg1
363            elif (susminreg1_1 < susminreg1_2) and (susminreg1_1 > susmaxreg1):
364                susceptible_to_immune_population_flow_region_1 = susminreg1_1
365            elif (susminreg1_2 < susminreg1_1) and (susminreg1_2 > susmaxreg1):
366                susceptible_to_immune_population_flow_region_1 = susminreg1_2
367        else:
368            susceptible_to_immune_population_flow_region_1 = 0
369
370        if switch_immunity == 1:
371            susminreg2_1 = (
372                normal_immune_population_region_2 - immune_population_region_2
373            ) / susceptible_to_immune_population_delay_time_region_2
374            susminreg2_2 = (
375                susceptible_population_region_2
376                / susceptible_to_immune_population_delay_time_region_2
377            )
378            susmaxreg2 = -(
379                immune_population_region_2
380                / susceptible_to_immune_population_delay_time_region_2
381            )
382            if (susmaxreg2 >= susminreg2_1) or (susmaxreg2 >= susminreg2_2):
383                susceptible_to_immune_population_flow_region_2 = susmaxreg2
384            elif (susminreg2_1 < susminreg2_2) and (susminreg2_1 > susmaxreg2):
385                susceptible_to_immune_population_flow_region_2 = susminreg2_1
386            elif (susminreg2_2 < susminreg2_1) and (susminreg2_2 > susmaxreg2):
387                susceptible_to_immune_population_flow_region_2 = susminreg2_2
388        else:
389            susceptible_to_immune_population_flow_region_2 = 0
390
391        susceptible_population_region_1_next = susceptible_population_region_1 - (
392            TIME_STEP
393            * (infections_region_1 + susceptible_to_immune_population_flow_region_1)
394        )
395        susceptible_population_region_2_next = susceptible_population_region_2 - (
396            TIME_STEP
397            * (infections_region_2 + susceptible_to_immune_population_flow_region_2)
398        )
399
400        immune_population_region_1_next = immune_population_region_1 + (
401            TIME_STEP * susceptible_to_immune_population_flow_region_1
402        )
403        immune_population_region_2_next = immune_population_region_2 + (
404            TIME_STEP * susceptible_to_immune_population_flow_region_2
405        )
406
407        deceased_population_region_1_next = deceased_population_region_1[-1] + (
408            TIME_STEP * flu_deaths_region_1
409        )
410        deceased_population_region_2_next = deceased_population_region_2[-1] + (
411            TIME_STEP * flu_deaths_region_2
412        )
413
414        # Updating integral values
415        if max_infected < (
416            infected_population_region_1_next
417            / (
418                infected_population_region_1_next
419                + recovered_population_region_1_next
420                + susceptible_population_region_1_next
421                + immune_population_region_1_next
422            )
423        ):
424            max_infected = infected_population_region_1_next / (
425                infected_population_region_1_next
426                + recovered_population_region_1_next
427                + susceptible_population_region_1_next
428                + immune_population_region_1_next
429            )
430
431        recovered_population_region_1 = recovered_population_region_1_next
432        recovered_population_region_2 = recovered_population_region_2_next
433
434        infected_population_region_1 = infected_population_region_1_next
435        infected_population_region_2 = infected_population_region_2_next
436
437        susceptible_population_region_1 = susceptible_population_region_1_next
438        susceptible_population_region_2 = susceptible_population_region_2_next
439
440        immune_population_region_1 = immune_population_region_1_next
441        immune_population_region_2 = immune_population_region_2_next
442
443        deceased_population_region_1.append(deceased_population_region_1_next)
444        deceased_population_region_2.append(deceased_population_region_2_next)
445
446        # End of main code
447
448    return {
449        "TIME": run_time,
450        "deceased_population_region_1": deceased_population_region_1,
451    }
452
453
454if __name__ == "__main__":
455    ema_logging.log_to_stderr(ema_logging.INFO)
456
457    model = Model("mexicanFlu", function=flu_model)
458    model.uncertainties = [
459        RealParameter("x11", 0, 0.5),
460        RealParameter("x12", 0, 0.5),
461        RealParameter("x21", 0.0001, 0.1),
462        RealParameter("x22", 0.0001, 0.1),
463        RealParameter("x31", 0, 0.5),
464        RealParameter("x32", 0, 0.5),
465        RealParameter("x41", 0, 0.9),
466        RealParameter("x51", 0, 0.5),
467        RealParameter("x52", 0, 0.5),
468        RealParameter("x61", 0, 0.8),
469        RealParameter("x62", 0, 0.8),
470        RealParameter("x81", 1, 10),
471        RealParameter("x82", 1, 10),
472        RealParameter("x91", 0, 0.1),
473        RealParameter("x92", 0, 0.1),
474        RealParameter("x101", 0, 200),
475        RealParameter("x102", 0, 200),
476    ]
477
478    model.outcomes = [
479        TimeSeriesOutcome("TIME"),
480        TimeSeriesOutcome("deceased_population_region_1"),
481    ]
482
483    nr_experiments = 500
484
485    with SequentialEvaluator(model) as evaluator:
486        experiments, outcomes = perform_experiments(
487            model, nr_experiments, evaluator=evaluator
488        )
489
490    lines(
491        experiments,
492        outcomes,
493        outcomes_to_show="deceased_population_region_1",
494        show_envelope=True,
495        density=Density.KDE,
496        titles=None,
497        experiments_to_show=np.arange(0, nr_experiments, 10),
498    )
499    plt.show()
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/example_flu.html
