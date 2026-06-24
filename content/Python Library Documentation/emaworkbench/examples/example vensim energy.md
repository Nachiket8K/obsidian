---
title: "example_vensim_energy.py"
source: "https://emaworkbench.readthedocs.io/en/latest/examples/example_vensim_energy.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# example\_vensim\_energy.py

```
  1"""Another vensim example."""
  2
  3from ema_workbench import (
  4    CategoricalParameter,
  5    MultiprocessingEvaluator,
  6    RealParameter,
  7    Sample,
  8    TimeSeriesOutcome,
  9    ema_logging,
 10)
 11from ema_workbench.connectors.vensim import VensimModel
 12
 13# Created on 27 Jan 2014
 14#
 15# @author: jhkwakkel
 16
 17
 18def get_energy_model():
 19    """Teturn the model instance."""
 20    model = VensimModel(
 21        "energy_transition",
 22        wd="./models",
 23        model_file="RB_V25_ets_1_policy_modified_adaptive_extended_outcomes.vpm",
 24    )
 25
 26    model.outcomes = [
 27        TimeSeriesOutcome(
 28            "cumulative_carbon_emissions", variable_name="cumulative carbon emissions"
 29        ),
 30        TimeSeriesOutcome(
 31            "carbon_emissions_reduction_fraction",
 32            variable_name="carbon emissions reduction fraction",
 33        ),
 34        TimeSeriesOutcome("fraction_renewables", variable_name="fraction renewables"),
 35        TimeSeriesOutcome("average_total_costs", variable_name="average total costs"),
 36        TimeSeriesOutcome(
 37            "total_costs_of_electricity", variable_name="total costs of electricity"
 38        ),
 39    ]
 40
 41    model.uncertainties = [
 42        RealParameter(
 43            "demand_fuel_price_elasticity_factor",
 44            0,
 45            0.5,
 46            variable_name="demand fuel price elasticity factor",
 47        ),
 48        RealParameter(
 49            "economic_lifetime_biomass",
 50            30,
 51            50,
 52            variable_name="economic lifetime biomass",
 53        ),
 54        RealParameter(
 55            "economic_lifetime_coal", 30, 50, variable_name="economic lifetime coal"
 56        ),
 57        RealParameter(
 58            "economic_lifetime_gas", 25, 40, variable_name="economic lifetime gas"
 59        ),
 60        RealParameter(
 61            "economic_lifetime_igcc", 30, 50, variable_name="economic lifetime igcc"
 62        ),
 63        RealParameter(
 64            "economic_lifetime_ngcc", 25, 40, variable_name="economic lifetime ngcc"
 65        ),
 66        RealParameter(
 67            "economic_lifetime_nuclear",
 68            50,
 69            70,
 70            variable_name="economic lifetime nuclear",
 71        ),
 72        RealParameter(
 73            "economic_lifetime_pv", 20, 30, variable_name="economic lifetime pv"
 74        ),
 75        RealParameter(
 76            "economic_lifetime_wind", 20, 30, variable_name="economic lifetime wind"
 77        ),
 78        RealParameter(
 79            "economic_lifetime_hydro", 50, 70, variable_name="economic lifetime hydro"
 80        ),
 81        RealParameter(
 82            "uncertainty_initial_gross_fuel_costs",
 83            0.5,
 84            1.5,
 85            variable_name="uncertainty initial gross fuel costs",
 86        ),
 87        RealParameter(
 88            "investment_proportionality_constant",
 89            0.5,
 90            4,
 91            variable_name="investment proportionality constant",
 92        ),
 93        RealParameter(
 94            "investors_desired_excess_capacity_investment",
 95            0.2,
 96            2,
 97            variable_name="investors desired excess capacity investment",
 98        ),
 99        RealParameter(
100            "price_demand_elasticity_factor",
101            -0.07,
102            -0.001,
103            variable_name="price demand elasticity factor",
104        ),
105        RealParameter(
106            "price_volatility_global_resource_markets",
107            0.1,
108            0.2,
109            variable_name="price volatility global resource markets",
110        ),
111        RealParameter(
112            "progress_ratio_biomass", 0.85, 1, variable_name="progress ratio biomass"
113        ),
114        RealParameter(
115            "progress_ratio_coal", 0.9, 1.05, variable_name="progress ratio coal"
116        ),
117        RealParameter(
118            "progress_ratio_gas", 0.85, 1, variable_name="progress ratio gas"
119        ),
120        RealParameter(
121            "progress_ratio_igcc", 0.9, 1.05, variable_name="progress ratio igcc"
122        ),
123        RealParameter(
124            "progress_ratio_ngcc", 0.85, 1, variable_name="progress ratio ngcc"
125        ),
126        RealParameter(
127            "progress_ratio_nuclear", 0.9, 1.05, variable_name="progress ratio nuclear"
128        ),
129        RealParameter(
130            "progress_ratio_pv", 0.75, 0.9, variable_name="progress ratio pv"
131        ),
132        RealParameter(
133            "progress_ratio_wind", 0.85, 1, variable_name="progress ratio wind"
134        ),
135        RealParameter(
136            "progress_ratio_hydro", 0.9, 1.05, variable_name="progress ratio hydro"
137        ),
138        RealParameter(
139            "starting_construction_time",
140            0.1,
141            3,
142            variable_name="starting construction time",
143        ),
144        RealParameter(
145            "time_of_nuclear_power_plant_ban",
146            2013,
147            2100,
148            variable_name="time of nuclear power plant ban",
149        ),
150        RealParameter(
151            "weight_factor_carbon_abatement",
152            1,
153            10,
154            variable_name="weight factor carbon abatement",
155        ),
156        RealParameter(
157            "weight_factor_marginal_investment_costs",
158            1,
159            10,
160            variable_name="weight factor marginal investment costs",
161        ),
162        RealParameter(
163            "weight_factor_technological_familiarity",
164            1,
165            10,
166            variable_name="weight factor technological familiarity",
167        ),
168        RealParameter(
169            "weight_factor_technological_growth_potential",
170            1,
171            10,
172            variable_name="weight factor technological growth potential",
173        ),
174        RealParameter(
175            "maximum_battery_storage_uncertainty_constant",
176            0.2,
177            3,
178            variable_name="maximum battery storage uncertainty constant",
179        ),
180        RealParameter(
181            "maximum_no_storage_penetration_rate_wind",
182            0.2,
183            0.6,
184            variable_name="maximum no storage penetration rate wind",
185        ),
186        RealParameter(
187            "maximum_no_storage_penetration_rate_pv",
188            0.1,
189            0.4,
190            variable_name="maximum no storage penetration rate pv",
191        ),
192        CategoricalParameter(
193            "SWITCH_lookup_curve_TGC",
194            (1, 2, 3, 4),
195            variable_name="SWITCH lookup curve TGC",
196        ),
197        CategoricalParameter(
198            "SWTICH_preference_carbon_curve",
199            (1, 2),
200            variable_name="SWTICH preference carbon curve",
201        ),
202        CategoricalParameter(
203            "SWITCH_economic_growth",
204            (1, 2, 3, 4, 5, 6),
205            variable_name="SWITCH economic growth",
206        ),
207        CategoricalParameter(
208            "SWITCH_electrification_rate",
209            (1, 2, 3, 4, 5, 6),
210            variable_name="SWITCH electrification rate",
211        ),
212        CategoricalParameter(
213            "SWITCH_Market_price_determination",
214            (1, 2),
215            variable_name="SWITCH Market price determination",
216        ),
217        CategoricalParameter(
218            "SWITCH_physical_limits", (1, 2), variable_name="SWITCH physical limits"
219        ),
220        CategoricalParameter(
221            "SWITCH_low_reserve_margin_price_markup",
222            (1, 2, 3, 4),
223            variable_name="SWITCH low reserve margin price markup",
224        ),
225        CategoricalParameter(
226            "SWITCH_interconnection_capacity_expansion",
227            (1, 2, 3, 4),
228            variable_name="SWITCH interconnection capacity expansion",
229        ),
230        CategoricalParameter(
231            "SWITCH_storage_for_intermittent_supply",
232            (1, 2, 3, 4, 5, 6, 7),
233            variable_name="SWITCH storage for intermittent supply",
234        ),
235        CategoricalParameter(
236            "SWITCH_carbon_cap", (1, 2, 3), variable_name="SWITCH carbon cap"
237        ),
238        CategoricalParameter(
239            "SWITCH_TGC_obligation_curve",
240            (1, 2, 3),
241            variable_name="SWITCH TGC obligation curve",
242        ),
243        CategoricalParameter(
244            "SWITCH_carbon_price_determination",
245            (1, 2, 3),
246            variable_name="SWITCH carbon price determination",
247        ),
248    ]
249    return model
250
251
252if __name__ == "__main__":
253    ema_logging.log_to_stderr(ema_logging.INFO)
254    model = get_energy_model()
255
256    policies = [
257        Sample("no policy", model_file="RB_V25_ets_1_extended_outcomes.vpm"),
258        Sample("static policy", model_file="ETSPolicy.vpm"),
259        Sample(
260            "adaptive policy",
261            model_file="RB_V25_ets_1_policy_modified_adaptive_extended_outcomes.vpm",
262        ),
263    ]
264
265    n = 100000
266    with MultiprocessingEvaluator(model) as evaluator:
267        experiments, outcomes = evaluator.perform_experiments(n, policies=policies)
268    #
269    # outcomes.pop("TIME")
270    # results = experiments, outcomes
271    # save_results(results, f"./data/{n}_lhs.tar.gz")
```

---

Original source: https://emaworkbench.readthedocs.io/en/latest/examples/example_vensim_energy.html
