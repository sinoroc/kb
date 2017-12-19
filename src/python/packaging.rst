..


****************
Python packaging
****************

Introduction
============

About proper packaging of Python projects...


Nomenclature
============

Module
------

Commonly a Python file (``mymodule.py``). Multiple Python modules are usually
gathered in a Python package.


Package
-------

A Python package is a directory containing at least a Python package
initializer: the ``__init__.py`` module. A package also usually contains
multiple other modules.

It is possible for a package to contain other sub-packages in a tree-like
structure. The outermost package is then called the top-level package.


Project
-------

A Python project is usually a collection of code (and sometimes also data) that
is intended to be distributed as a single unit. Typically a Python project is a
library, an application, a plugin, a framework, or a toolkit. In most cases
this corresponds to a single source code repository (for example a *git*,
*SVN*, or *CVS* repository).

It is not often the case, but a Python project can contain multiple top-level
packages. So of course the name of a top-level package is not always the same
as the name of the project itself. It would be otherwise impossible to have
more than one top-level package per project.

Some Python projects are only made of one or more Python modules directly at
the root without tree-like package structure.


Distribution
------------

.. sidebar:: Python distribution vs. Python project distribution

    *Project distributions* are not to be confused with *Python distributions*
    such as *CPython*, *Anaconda*, *SciPy*, etc.

A Python project distribution corresponds to a snapshot of a Python project
that is distributed to other Python users. Each snapshot is labeled with a
version string. Each snapshot (or project version) is made available in one or
multiple formats. Users can then obtain their preferred format.

There are two common types of distribution formats: *source* and *binary*.


Source distribution
^^^^^^^^^^^^^^^^^^^

A source distribution, often abbreviated *sdist*, is a relatively raw type of
distribution. It is not compiled, which is both an advantage and an
inconvenient.

The inconvenient is that a source distribution is not always immediately
usable. That is why source distributions typically contain the setup script.
For example if the project contains a *C* extension, then this code must be
compiled before running.

The advantage is that a source distribution is universal. It is not tied to a
specific operating system, CPU architecture, etc. The source distribution is
the *purest* form of distribution, it can be used to build all the binary
distributions for all targets.

Source distributions can be found in multiple formats::

    $ python setup.py sdist --help-formats
    List of available source distribution formats:
      --formats=bztar  bzip2'ed tar-file
      --formats=gztar  gzip'ed tar-file
      --formats=tar    uncompressed tar file
      --formats=zip    ZIP file
      --formats=ztar   compressed tar file


.. attention::
    It is strongly recommended to always offer at least the *sdist* on PyPI.
    It can always be used as a fall back in case the user can not find a
    *bdist* suitable for its own target system.

    It might not be straightforward but there is almost always a way to build
    any *bdist* from the *sdist*. Whereas it is most likely impossible to
    build a *bdist* from another.


Binary distribution
^^^^^^^^^^^^^^^^^^^

A binary distribution, often abbreviated *bdist*, is a more advanced type of
distribution.

There are multiple types of binary distributions, for example *egg*
(``bdist_egg``) and *wheel* (``bdist_wheel``).


Wheel
^^^^^

*wheel* is the preferred format of distribution. It offers the best user
experience, as it is the format that is the closest to the specifics of the
target system.


Python package index
--------------------

The Python package index, commonly called *PyPI* is the main repository of
Python projects.

.. note::
    The name Python *package* index is confusing since PyPI does not directly
    contains *packages*, but *project distributions*.


There are currently two instances of PyPI running in parallel:

* https://pypi.python.org/pypi

* https://pypi.org/


Version
=======

Keep the version of the Python project in just one place.

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

The current version number should always be on the same line and on its own so
that the setup script can easily parse it. As a positive side effect, changing
the version number forces to keep the change log up to date.

.. code-block:: python
    :caption: setup.py
    :emphasize-lines: 4,8,9

    import os
    import setuptools

    with open(os.path.join(HERE, 'CHANGELOG.rst')) as f:
        CHANGELOG = f.read()

    setuptools.setup(
        name='Example',
        version=CHANGELOG.splitlines()[0],
        # ...
    )

From the actual code of the project the version number should be accessed via
``pkg_resources``. Knowing the name of the Python project it easy to get the
version of the currently loaded project ditribution.

.. code-block:: python
    :caption: src/example/__init__.py
    :emphasize-lines: 2

    __version__ = pkg_resources.get_distribution(
        'Example',
    ).version


.. EOF
