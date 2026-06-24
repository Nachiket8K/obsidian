---
title: "b_and_w_plotting"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/b_and_w_plotting.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `b_and_w_plotting`

Basic functionality for converting a matplotlib figure to black and white.

The provided functionality is largely determined by what is needed for the workbench.

ema\_workbench.analysis.b\_and\_w\_plotting.set\_fig\_to\_bw(*fig*, *style='hatching'*, *line\_style='continuous'*)
:   Take each axes in the figure and transform its content to black and white.

    Lines are transformed based on different line styles. Fills such as can
    be used in meth:envelopes are gray-scaled. Heathmaps are also gray-scaled.

    derived from and expanded for my use from:
    <https://stackoverflow.com/questions/7358118/matplotlib-black-white-colormap-with-dashes-dots-etc>

    Parameters:
    :   - **fig** (*figure*) – the figure to transform to black and white
        - **style** (*{HATCHING**,* *GREYSCALE}*) – parameter controlling how collections are transformed.
        - **line\_style** (*str**,* *{'continuous'**,* *'black'**,* *None}*)

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/b_and_w_plotting.html
