..


**************************************
Python project version single-sourcing
**************************************

Problem
=======

It is not entirely straightforward where the version string should be written
within a Python project.

A couple of things are sure:

* the version must be written in a ``__version__`` attribute as a string
  (see `PEP 396 <https://www.python.org/dev/peps/pep-0396/>`_)

* the version string must be available from the setup script

* the version string should be in the changelog


It is annoying to have to keep the version string up to date in these three
locations. A solution for single-sourcing the project version would fix that.


Solution
========

This solution shows how to keep the Python project version string in just one
place. The suggested location is in the change log:

.. code-block:: restructuredtext
    :caption: CHANGELOG.rst
    :emphasize-lines: 1
    :linenos:
    :lineno-start: 0

    1.2.3
    =====

    * More bugs fixed

    1.2.2
    =====

    * Bugs fixed

The current version string should always be on the same line and on its own so
that the setup script can easily find it and extract it:

.. code-block:: python
    :caption: setup.py
    :emphasize-lines: 4,5,8,9

    import os
    import setuptools

    with open(os.path.join(HERE, 'CHANGELOG.rst')) as file_:
        changelog = file_.read()

    setuptools.setup(
        name='Example',
        version=changelog.splitlines()[0],
        # ...
    )

From the actual code of the project the version number should be accessed via
``importlib.metadata``. Knowing the name of the project it is easy to get the
version string:

.. code-block:: python
    :caption: src/example/__init__.py
    :emphasize-lines: 3

    import importlib.metadata

    __version__ = importlib.metadata.version('Example')


The ``importlib.metadata`` package is part of the standard library starting
with *Python 3.8*. For earlier versions use importlib-metadata_ instead.

.. _importlib-metadata: https://pypi.org/project/importlib-metadata/

As a positive side effect, changing the version number forces the project
maintainer to modify the change log and thus they always get at least one
chance to keep it up to date.


.. EOF
