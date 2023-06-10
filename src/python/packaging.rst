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

There are two common types of distribution formats: *source* and *built*.


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
specific operating system, CPU architecture, etc.
The source distribution
can be used to build all the built distributions
for all targets.

Source distributions are *gzip*'ed *tar* files with the ``.tar.gz.`` extension.


.. attention::

    It is strongly recommended to always offer at least the *sdist* of a Python
    project (for example on PyPI). The reason is that it is always possible to
    use the *sdist* on any platform. On the other hand it is most likely
    impossible to use a *bdist* targetted for another platform.

    So if no *bdist* of the project is available for the target platform, the
    *sdist* can still be used and eventually a target specific *bdist* can be
    built locally.


Built distribution
^^^^^^^^^^^^^^^^^^

A built distribution, often abbreviated *bdist*,
is a more advanced type of distribution.
This distribution format is designed
so that the installation step is as straightforward as possible.
In short: files only need to be extracted from the built distribution archive
and copied to the right locations on disk.
It does not require any kind of build step,
as all files in a built distribution are already built
for the specific target environment.

Nowadays the only kind of built distributions
one should know about
is the *wheel*.
The *egg*
is another kind of built distribution
that is now rarely used.


Wheel
^^^^^

The built distribution format called *wheel*
is the current preferred format of distribution for a project.
It is defined by a `standard specification`__.

__ https://packaging.python.org/en/latest/specifications/binary-distribution-format/


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
