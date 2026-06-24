---
title: "Best practices"
source: "https://emaworkbench.readthedocs.io/en/latest/best_practices.html"
imported_from: "Python library documentation"
library: "emaworkbench"
---

# Best practices

## Separate experimentation and analysis

It is strongly recommended to cleanly separate the various steps in your
exploratory modeling pipeline. So, separately execute your experiments or
perform your optimization, save the results, and next analyze these results.
Moreover, since parallel execution can be troublesome within the Jupyter Lab
/ notebook environment, I personally run my experiments and optimizations
either from the command line or through an IDE using a normal python file.
Jupyter Lab is then used to analyze the results.

## Keeping things organized

A frequently recurring cause of problems when using the workbench stems from
not properly organizing your files. In particular when using multiprocessing
it is key that you keep things well organized. The way the workbench works
with multiprocessing is that it copies the entire working directory of the
model to a temporary folder for each subprocess. This temporary folder is
located in the same folder as the python or notebook file from which you are
running. If the working directory of your model is the same as the directory
in which the run file resized, you can easily fill up your hard disk in
minutes. To avoid these kinds of problems, I suggest to use a directory
structure as outlined below.

project

├─ model\_files

├── a\_model.nlogo

└── some\_input.csv

├─ results

├── 100k\_nfe\_seed1.csv

└── 1000\_experiments.tar.gz

├─ figures

└── pairwise\_scatter.png

├─experiments.py

├─optimization.py

├─analysis.ipynb

└─model\_definition.py

Also, if you are not familiar with absolute and relative paths, please read
up on that first and only use relative paths when using the workbench. Not
only will this reduce the possibility for errors, it will also mean that
moving your code from one machine to another will be a lot easier.

---

Original source: https://emaworkbench.readthedocs.io/en/latest/best_practices.html
