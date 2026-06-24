---
title: "plotting_util"
source: "https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/plotting_util.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# `plotting_util`

Plotting utility functions.

ema\_workbench.analysis.plotting\_util.COLOR\_LIST = [(0.12156862745098039, 0.4666666666666667, 0.7058823529411765), (1.0, 0.4980392156862745, 0.054901960784313725), (0.17254901960784313, 0.6274509803921569, 0.17254901960784313), (0.8392156862745098, 0.15294117647058825, 0.1568627450980392), (0.5803921568627451, 0.403921568627451, 0.7411764705882353), (0.5490196078431373, 0.33725490196078434, 0.29411764705882354), (0.8901960784313725, 0.4666666666666667, 0.7607843137254902), (0.4980392156862745, 0.4980392156862745, 0.4980392156862745), (0.7372549019607844, 0.7411764705882353, 0.13333333333333333), (0.09019607843137255, 0.7450980392156863, 0.8117647058823529)]
:   Default color list

class ema\_workbench.analysis.plotting\_util.Density(*\*values*)
:   Enum for different types of density plots.

    BOXENPLOT = 'boxenplot'
    :   constant for plotting density as a boxenplot.

    BOXPLOT = 'boxplot'
    :   constant for plotting density as a boxplot.

    HIST = 'hist'
    :   constant for plotting density as a histogram.

    KDE = 'kde'
    :   constant for plotting density as a kernel density estimate.

    VIOLIN = 'violin'
    :   constant for plotting density as a violin plot, which combines a
        Gaussian density estimate with a boxplot.

class ema\_workbench.analysis.plotting\_util.LegendEnum(*\*values*)
:   Enum for different styles of legends.

class ema\_workbench.analysis.plotting\_util.PlotType(*\*values*)
:   Enum for different types of plots.

    ENVELOPE = 'envelope'
    :   constant for plotting envelopes.

    ENV\_LIN = 'env\_lin'
    :   constant for plotting envelopes with lines.

    LINES = 'lines'
    :   constant for plotting lines.

---

Original source: https://emaworkbench.readthedocs.io/en/latest/ema_documentation/analysis/plotting_util.html
