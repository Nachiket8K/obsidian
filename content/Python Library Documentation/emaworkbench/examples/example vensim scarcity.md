---
title: "example_vensim_scarcity.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/example_vensim_scarcity.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# example\_vensim\_scarcity.py

```
  1"""A resource scarcity model in vensim.
  2
  3This is a slightly more sophisticated example where we translate some of the uncertainties
  4on the python side, prior to running the vensim model.
  5
  6"""
  7
  8from math import exp
  9
 10from ema_workbench.connectors.vensim import VensimModel
 11from ema_workbench.em_framework import (
 12    CategoricalParameter,
 13    RealParameter,
 14    TimeSeriesOutcome,
 15    perform_experiments,
 16)
 17from ema_workbench.util import ema_logging
 18
 19# Created on 8 mrt. 2011
 20#
 21# .. codeauthor:: jhkwakkel <j.h.kwakkel (at) tudelft (dot) nl>
 22#                 epruyt <e.pruyt (at) tudelft (dot) nl>
 23
 24
 25class ScarcityModel(VensimModel):
 26    """Scarcity model."""
 27
 28    def returns_to_scale(self, x, speed, scale):
 29        """Translate uncertainties to lookup."""
 30        return (x * 1000, scale * 1 / (1 + exp(-1 * speed * (x - 50))))
 31
 32    def approx_learning(self, x, speed, scale, start):
 33        """Translate uncertainties to lookup."""
 34        x = x - start
 35        loc = 1 - scale
 36        a = (x * 10000, scale * 1 / (1 + exp(speed * x)) + loc)
 37        return a
 38
 39    def f(self, x, speed, loc):
 40        """Translate uncertainties to lookup."""
 41        return (x / 10, loc * 1 / (1 + exp(speed * x)))
 42
 43    def price_substite(self, x, speed, begin, end):
 44        """Translate uncertainties to lookup."""
 45        scale = 2 * end
 46        start = begin - scale / 2
 47
 48        return (x + 2000, scale * 1 / (1 + exp(-1 * speed * x)) + start)
 49
 50    def run_model(self, scenario, policy, constants):
 51        """Method for running an instantiated model structure."""
 52        kwargs = scenario
 53        loc = kwargs.pop("lookup_shortage_loc")
 54        speed = kwargs.pop("lookup_shortage_speed")
 55        lookup = [self.f(x / 10, speed, loc) for x in range(100)]
 56        kwargs["shortage price effect lookup"] = lookup
 57
 58        speed = kwargs.pop("lookup_price_substitute_speed")
 59        begin = kwargs.pop("lookup_price_substitute_begin")
 60        end = kwargs.pop("lookup_price_substitute_end")
 61        lookup = [self.price_substite(x, speed, begin, end) for x in range(0, 100, 10)]
 62        kwargs["relative price substitute lookup"] = lookup
 63
 64        scale = kwargs.pop("lookup_returns_to_scale_speed")
 65        speed = kwargs.pop("lookup_returns_to_scale_scale")
 66        lookup = [self.returns_to_scale(x, speed, scale) for x in range(0, 101, 10)]
 67        kwargs["returns to scale lookup"] = lookup
 68
 69        scale = kwargs.pop("lookup_approximated_learning_speed")
 70        speed = kwargs.pop("lookup_approximated_learning_scale")
 71        start = kwargs.pop("lookup_approximated_learning_start")
 72        lookup = [
 73            self.approx_learning(x, speed, scale, start) for x in range(0, 101, 10)
 74        ]
 75        kwargs["approximated learning effect lookup"] = lookup
 76
 77        super().run_model(kwargs, policy, constants)
 78
 79
 80if __name__ == "__main__":
 81    ema_logging.log_to_stderr(ema_logging.DEBUG)
 82
 83    model = ScarcityModel(
 84        "scarcity", wd="./models/scarcity", model_file="MetalsEMA.vpm"
 85    )
 86
 87    model.outcomes = [
 88        TimeSeriesOutcome(
 89            "relative_market_price", variable_name="relative market price"
 90        ),
 91        TimeSeriesOutcome("supply_demand_ratio", variable_name="supply demand ratio"),
 92        TimeSeriesOutcome("real_annual_demand", variable_name="real annual demand"),
 93        TimeSeriesOutcome(
 94            "produced_of_intrinsically_demanded",
 95            variable_name="produced of intrinsically demanded",
 96        ),
 97        TimeSeriesOutcome("supply", variable_name="supply"),
 98        TimeSeriesOutcome(
 99            "Installed_Recycling_Capacity", variable_name="Installed Recycling Capacity"
100        ),
101        TimeSeriesOutcome(
102            "Installed_Extraction_Capacity",
103            variable_name="Installed Extraction Capacity",
104        ),
105    ]
106
107    model.uncertainties = [
108        RealParameter(
109            "price_elasticity_of_demand",
110            0,
111            0.5,
112            variable_name="price elasticity of demand",
113        ),
114        RealParameter(
115            "fraction_of_maximum_extraction_capacity_used",
116            0.6,
117            1.2,
118            variable_name="fraction of maximum extraction capacity used",
119        ),
120        RealParameter(
121            "initial_average_recycling_cost",
122            1,
123            4,
124            variable_name="initial average recycling cost",
125        ),
126        RealParameter(
127            "exogenously_planned_extraction_capacity",
128            0,
129            15000,
130            variable_name="exogenously planned extraction capacity",
131        ),
132        RealParameter(
133            "absolute_recycling_loss_fraction",
134            0.1,
135            0.5,
136            variable_name="absolute recycling loss fraction",
137        ),
138        RealParameter(
139            "normal_profit_margin", 0, 0.4, variable_name="normal profit margin"
140        ),
141        RealParameter(
142            "initial_annual_supply",
143            100000,
144            120000,
145            variable_name="initial annual supply",
146        ),
147        RealParameter(
148            "initial_in_goods", 1500000, 2500000, variable_name="initial in goods"
149        ),
150        RealParameter(
151            "average_construction_time_extraction_capacity",
152            1,
153            10,
154            variable_name="average construction time extraction capacity",
155        ),
156        RealParameter(
157            "average_lifetime_extraction_capacity",
158            20,
159            40,
160            variable_name="average lifetime extraction capacity",
161        ),
162        RealParameter(
163            "average_lifetime_recycling_capacity",
164            20,
165            40,
166            variable_name="average lifetime recycling capacity",
167        ),
168        RealParameter(
169            "initial_extraction_capacity_under_construction",
170            5000,
171            20000,
172            variable_name="initial extraction capacity under construction",
173        ),
174        RealParameter(
175            "initial_recycling_capacity_under_construction",
176            5000,
177            20000,
178            variable_name="initial recycling capacity under construction",
179        ),
180        RealParameter(
181            "initial_recycling_infrastructure",
182            5000,
183            20000,
184            variable_name="initial recycling infrastructure",
185        ),
186        # order of delay
187        CategoricalParameter(
188            "order_in_goods_delay",
189            (1, 4, 10, 1000),
190            variable_name="order in goods delay",
191        ),
192        CategoricalParameter(
193            "order_recycling_capacity_delay",
194            (1, 4, 10),
195            variable_name="order recycling capacity delay",
196        ),
197        CategoricalParameter(
198            "order_extraction_capacity_delay",
199            (1, 4, 10),
200            variable_name="order extraction capacity delay",
201        ),
202        # uncertainties associated with lookups
203        RealParameter(
204            "lookup_shortage_loc", 20, 50, variable_name="lookup shortage loc"
205        ),
206        RealParameter(
207            "lookup_shortage_speed", 1, 5, variable_name="lookup shortage speed"
208        ),
209        RealParameter(
210            "lookup_price_substitute_speed",
211            0.1,
212            0.5,
213            variable_name="lookup price substitute speed",
214        ),
215        RealParameter(
216            "lookup_price_substitute_begin",
217            3,
218            7,
219            variable_name="lookup price substitute begin",
220        ),
221        RealParameter(
222            "lookup_price_substitute_end",
223            15,
224            25,
225            variable_name="lookup price substitute end",
226        ),
227        RealParameter(
228            "lookup_returns_to_scale_speed",
229            0.01,
230            0.2,
231            variable_name="lookup returns to scale speed",
232        ),
233        RealParameter(
234            "lookup_returns_to_scale_scale",
235            0.3,
236            0.7,
237            variable_name="lookup returns to scale scale",
238        ),
239        RealParameter(
240            "lookup_approximated_learning_speed",
241            0.01,
242            0.2,
243            variable_name="lookup approximated learning speed",
244        ),
245        RealParameter(
246            "lookup_approximated_learning_scale",
247            0.3,
248            0.6,
249            variable_name="lookup approximated learning scale",
250        ),
251        RealParameter(
252            "lookup_approximated_learning_start",
253            30,
254            60,
255            variable_name="lookup approximated learning start",
256        ),
257    ]
258
259    results = perform_experiments(model, 1000)
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/example_vensim_scarcity.html
