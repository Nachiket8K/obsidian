---
title: "Source code for mesa.visualization.user_param"
source: "https://mesa.readthedocs.io/latest/_modules/mesa/visualization/user_param.html"
imported_from: "Python library documentation"
library: "Mesa"
---

# Source code for mesa.visualization.user\_param

```
"""Solara visualization related helper classes."""

[docs]
class UserParam:
    """UserParam."""

    _ERROR_MESSAGE = "Missing or malformed inputs for '{}' Option '{}'"

[docs]
    def maybe_raise_error(self, param_type, valid):  # noqa: D102
        if valid:
            return
        msg = self._ERROR_MESSAGE.format(param_type, self.label)
        raise ValueError(msg)

[docs]
class Slider(UserParam):
    """A number-based slider input with settable increment.

    Example:
    slider_option = Slider("My Slider", value=123, min=10, max=200, step=0.1)

    Args:
        label: The displayed label in the UI
        value: The initial value of the slider
        min: The minimum possible value of the slider
        max: The maximum possible value of the slider
        step: The step between min and max for a range of possible values
        dtype: either int or float
    """

    def __init__(
        self,
        label="",
        value=None,
        min=None,
        max=None,
        step=1,
        dtype=None,
    ):
        """Initializes a slider.

        Args:
            label: The displayed label in the UI
            value: The initial value of the slider
            min: The minimum possible value of the slider
            max: The maximum possible value of the slider
            step: The step between min and max for a range of possible values
            dtype: either int or float
        """
        self.label = label
        self.value = value
        self.min = min
        self.max = max
        self.step = step

        # Validate option type to make sure values are supplied properly
        valid = not (self.value is None or self.min is None or self.max is None)
        self.maybe_raise_error("slider", valid)

        if dtype is None:
            self.is_float_slider = self._check_values_are_float(value, min, max, step)
        else:
            self.is_float_slider = dtype is float

    def _check_values_are_float(self, value, min, max, step):  # D103
        return any(isinstance(n, float) for n in (value, min, max, step))

[docs]
    def get(self, attr):  # noqa: D102
        return getattr(self, attr)
```

---

Original source: https://mesa.readthedocs.io/latest/_modules/mesa/visualization/user_param.html
