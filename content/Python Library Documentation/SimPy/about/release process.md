---
title: "Release Process"
source: "https://simpy.readthedocs.io/en/latest/about/release_process.html"
imported_from: "Python library documentation"
library: "SimPy"
---

# Release Process

This process describes the steps to execute in order to release a new version
of SimPy.

## Preparations

1. Close all [tickets for the next version](https://gitlab.com/team-simpy/simpy/-/issues).
2. Update the *minimum* required versions of dependencies in `setup.cfg`.
   Update the development dependencies in `requirements-dev.txt`.
3. Run **tox** from the project root. All tests for all supported
   versions must pass:

   ```
   $ tox
   [...]
   ________ summary ________
   py38: commands succeeded
   pypy3: commands succeeded
   docs: commands succeeded
   ruff: commands succeeded
   mypy: commands succeeded
   congratulations :)
   ```
4. Build the docs (HTML is enough). Make sure there are no errors and undefined
   references.

   ```
   $ tox -e sphinx
   ```
5. Check if all authors are listed in `AUTHORS.txt`.
6. Update the change log (`CHANGES.rst`). Only keep changes for the
   current major release in `CHANGES.rst` and reference the history page
   from there.
7. Write a draft for the announcement mail with a list of changes,
   acknowledgements and installation instructions. Everyone in the team should
   agree with it.

## Build and release

1. Make *local* tag for new release. This tag will be pushed *later*, after
   checking the build artifacts. If anything is not right, this tag can be
   deleted and recreated locally *before* pushing to GitLab.

   ```
   $ git tag -a -m "Tag a.b.c release" a.b.c
   ```
2. Test the build process. Build a source distribution and a [wheel](https://pypi.python.org/pypi/wheel) package and test them:

   ```
   $ python -m build
   $ ls dist/
   simpy-a.b.c-py2.py3-none-any.whl simpy-a.b.c.tar.gz
   ```

   Try installing them:

   ```
   $ rm -rf /tmp/simpy-sdist  # ensure clean state if ran repeatedly
   $ virtualenv /tmp/simpy-sdist
   $ /tmp/simpy-sdist/bin/pip install dist/simpy-a.b.c.tar.gz
   ```

   and

   ```
   $ rm -rf /tmp/simpy-wheel  # ensure clean state if ran repeatedly
   $ virtualenv /tmp/simpy-wheel
   $ /tmp/simpy-wheel/bin/pip install dist/simpy-a.b.c-py2.py3-none-any.whl
   ```

   It is also a good idea to inspect the contents of the distribution files:

   ```
   $ tar tzf dist/simpy-a.b.c.tar.gz
   ```

   ```
   $ unzip -l dist/simpy-a.b.c-py2.py3-none-any.whl
   ```
3. Create or check your accounts for the [test server](https://test.pipi.org/)
   and [PyPI](https://pypi.org/). Update your `~/.pypirc` with your
   current credentials:

   ```
   [distutils]
   index-servers =
       pypi
       testpypi

   [pypi]
   username = <your pypi username>

   [testpypi]
   repository = https://test.pypi.org/legacy/
   username = <your testpypi username>
   ```
4. Upload the distributions for the new version to the test server and test the
   installation again:

   ```
   $ twine upload -r testpypi dist/simpy*a.b.c*
   $ pip install -i https://test.pypi.org/simple/ simpy
   ```
5. Check if the package is displayed correctly on the test PyPI:
   <https://test.pypi.org/project/simpy/>
6. Push tag for a.b.c release to GitLab. Upon successful build and test, the
   GitLab CI pipeline will deploy the tagged release to the production PyPI
   service.

   ```
   $ git push origin master a.b.c
   ```
7. Check the status of the GitLab CI pipeline:
   <https://gitlab.com/team-simpy/simpy/pipelines>
8. Check if the package is displayed correctly on PyPI:
   <https://pypi.org/project/simpy/>
9. Finally, test installation from PyPI:

   ```
   $ pip install -U simpy
   ```

## Post release

1. Activate the [documentation build](https://readthedocs.org/dashboard/simpy/versions/) for the new version.
2. Send the prepared release announcement to the [SimPy group](https://groups.google.com/forum/#!forum/python-simpy).
3. Update [Wikipedia](http://en.wikipedia.org/wiki/SimPy) entries.

---

Original source: https://simpy.readthedocs.io/en/latest/about/release_process.html
