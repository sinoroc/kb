..


****************
Python packaging
****************

.. contents::
    :backlinks: none
    :local:


Introduction
============

About proper packaging of Python projects...


Terminology
===========

Module
------

Commonly a Python file (``mymodule.py``). Multiple Python modules are usually
gathered in a Python package.


Package
-------

.. sidebar:: Confusion #1: *Import package* vs. *distribution package*

    One of the biggest confusion in the Python packaging terminology is around
    the meaning of the term *package*. Sometimes the terms *import package* and
    *distribution package* are used to clarify this.

It is sometimes named *import package*, as opposed to *distribution package*
(see below).

A Python package is a directory containing
at least one Python module ``__init__.py`` (the package initializer)
and zero or more additional Python modules.
The package initializer can be completely empty, but it has to be there.

It is possible for a package to contain other sub-packages in a tree-like
structure. The outermost package is then called the *top-level package*.


Project
-------

A Python project is usually a collection of code (and sometimes also data) that
is intended to be distributed as a single unit. Typically a Python project is a
library, an application, a plugin, a framework, or a toolkit. In most cases
this corresponds to a single source code repository (for example a *git*,
*SVN*, or *CVS* repository).

.. sidebar:: Multiple *top-level* packages and modules

    For example *setuptools* (version ``46.1.2`` as of this writing) has two
    *top-level packages* ``setuptools`` and ``pkg_resources``. It additionally
    seems to have one *top-level module* ``easy_install``.

It is not often the case, but a Python project can contain multiple top-level
packages. So of course the name of a top-level package is not always the same
as the name of the project itself. It would be otherwise impossible to have
more than one top-level package per project.

Some Python projects are only made of one or more Python modules directly at
the root without tree-like package structure.


Distribution
------------

.. sidebar:: Confusion #2: Python distribution vs. Python project distribution

    *Project distributions* are not to be confused with *Python distributions*
    such as *CPython*, *Anaconda*, *SciPy*, etc.

It is sometimes named *distribution package*, as opposed to *import package*
(see above).

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

    It is strongly recommended to always offer at least the *sdist* of a Python
    project (for example on PyPI). The reason is that it is always possible to
    use the *sdist* on any platform. On the other hand it is most likely
    impossible to use a *bdist* targetted for another platform.

    So if no *bdist* of the project is available for the target platform, the
    *sdist* can still be used and eventually a target specific *bdist* can be
    built locally.


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

.. sidebar:: Confusion #3: About the PyPI name

    The name Python *package* index is confusing since PyPI does not directly
    contains *packages*, but *distributions* of Python projects.


The *Python package index*, commonly called *PyPI* is the main repository of
Python project distributions. It can be found at following URL:

* https://pypi.org/


References
==========

David Beazley "*Modules and Packages: Live and Let Die!*":

*  http://www.dabeaz.com/modulepackage/ModulePackage.pdf


.. EOF
