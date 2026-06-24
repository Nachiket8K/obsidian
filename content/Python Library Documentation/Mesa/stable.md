---
title: "Mesa: Agent-based modeling in Python"
source: "https://mesa.readthedocs.io/stable/index.html"
imported_from: "Python library documentation"
library: "Mesa"
---

# Mesa: Agent-based modeling in Python

[![https://joss.theoj.org/papers/10.21105/joss.07668/status.svg](https://joss.theoj.org/papers/10.21105/joss.07668/status.svg)](https://doi.org/10.21105/joss.07668)
[![https://github.com/mesa/mesa/workflows/build/badge.svg](https://github.com/mesa/mesa/workflows/build/badge.svg)](https://github.com/mesa/mesa/actions)
[![https://codecov.io/gh/mesa/mesa/branch/main/graph/badge.svg](https://codecov.io/gh/mesa/mesa/branch/main/graph/badge.svg)](https://codecov.io/gh/mesa/mesa)
[![https://img.shields.io/badge/code%20style-black-000000.svg](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![https://img.shields.io/matrix/project-mesa:matrix.org?label=chat&logo=Matrix](https://img.shields.io/matrix/project-mesa:matrix.org?label=chat&logo=Matrix)](https://matrix.to/#/#project-mesa:matrix.org)

[Mesa](https://github.com/mesa/mesa/) is an Apache2 licensed agent-based modeling (or ABM) framework in Python.

Mesa allows users to quickly create agent-based models using built-in core components (such as spatial grids and agent schedulers) or customized implementations; visualize them using a browser-based interface; and analyze their results using Python’s data analysis tools. Mesa’s goal is to make simulations accessible to everyone, so humanity can more effectively understand and solve complex problems.

![A screenshot of the Wolf Sheep model in Mesa|100%](_images/wolf_sheep.png)
*A visualisation of the Wolf Sheep model build with Mesa. An online demo is [available here](https://py.cafe/app/EwoutH/mesa-solara-basic-examples).*

## Features

- Built-in core modeling components
- Flexible agent and model management through AgentSet
- Browser-based Solara visualization
- Built-in tools for data collection and analysis
- Example model library

## Using Mesa

### Installation Options

To install our latest stable release, run:

```
pip install -U mesa
```

To also install our recommended dependencies:

```
pip install -U mesa[rec]
```

The `[rec]` option installs additional recommended dependencies needed for visualization, plotting, and network modeling capabilities.

On a Mac, this command might cause an error stating `zsh: no matches found: mesa[all]`.
In that case, change the command to `pip install -U "mesa[rec]"`.

Furthermore, if you are using `nix`, Mesa comes with a flake with devShells and a runnable app:

```
nix run github:project-mesa/mesa # for default Python shell
```

For development shell, clone the repository and run the following command from
repository root:

```
nix develop .#uv2nix # pure shell
```

### Resources

For help getting started with Mesa, check out these resources:

- [Getting started](getting_started.html) - Learn about Mesa’s core concepts and components
- [Migration Guide](migration_guide.html) - Upgrade to Mesa 3.0
- [Mesa Examples](https://mesa.readthedocs.io/stable/examples.html) - Browse user-contributed models and implementations
- [Mesa Extensions](mesa_extension.html) - Overview of mesa’s Extensions
- [GitHub Discussions](https://github.com/mesa/mesa/discussions) - Ask questions and discuss Mesa
- [Matrix Chat Room](https://matrix.to/#/#project-mesa:matrix.org) - Real-time chat with the Mesa community

### Development and Support

Mesa is an open source project and welcomes contributions:

- [GitHub Repository](https://github.com/mesa/mesa/) - Access the source code
- [Issue Tracker](https://github.com/mesa/mesa/issues) - Report bugs or suggest features
- [Contributors Guide](https://github.com/mesa/mesa/blob/main/CONTRIBUTING.md) - Learn how to contribute
- [GSoC at Mesa — Candidates Guide](GSoC.html) - For candidates interested in participating in the Google Summer of Code at Mesa

### Citing Mesa

To cite Mesa in your publication, you can refer to our peer-reviewed article in the Journal of Open Source Software (JOSS):

- ter Hoeven, E., Kwakkel, J., Hess, V., Pike, T., Wang, B., rht, & Kazil, J. (2025). Mesa 3: Agent-based modeling with Python in 2025. Journal of Open Source Software, 10(107), 7668. https://doi.org/10.21105/joss.07668

Our [CITATION.cff](https://github.com/mesa/mesa/blob/main/CITATION.cff) can be used to generate APA, BibTeX and other citation formats.

The original Mesa conference paper from 2015 is [available here](http://conference.scipy.org.s3-website-us-east-1.amazonaws.com/proceedings/scipy2015/jacqueline_kazil.html).

# Indices and tables

- [Index](genindex.html)
- [Module Index](py-modindex.html)
- [Search Page](search.html)

On this page

### This Page

- [Show Source](_sources/index.md.txt)

---

Original source: https://mesa.readthedocs.io/stable/index.html
