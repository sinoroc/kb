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


Distribution package
--------------------

.. sidebar:: Confusion #2: *Distribution package* of a Python project
    vs. *Python distribution*

    The term *Python distribution* is used to describe a specific
    implementation or build of a Python interpreter.
    *CPython* is probably the most famous one,
    but there are plenty of others such as *ActiveState Python* and *Anaconda*.
    Further examples: https://wiki.python.org/moin/PythonDistributions

Not to be confused with *import package* (see above)
or *Python distribution* (see aside).

A distribution package contains a specific release of a project.
A release being a snapshot of the Python project at a certain point in time.
A distribution package is always labelled with
the name of the project
and the version string for the snapshot.

There are two common types of distribution formats:
*source distribution* and *built distribution*.


Source distribution
^^^^^^^^^^^^^^^^^^^

A source distribution, sometimes abbreviated as *sdist*,
is a distribution format.

A source distribution is meant to be installable on all Python interpreters
and platforms that the project supports.
It is not tied to a specific
Python interpreter implementation,
Python interpreter version,
operating system,
CPU architecture,
CPU bitness.
A source distribution can be used to build
all the built distributions for all targets the project supports.

Source distributions are *gzip*'ed *tar* files with the ``.tar.gz.`` extension.


.. attention::

    It is strongly recommended to always offer at least the *sdist* of a Python
    project (for example on PyPI). The reason is that it is always possible to
    use the *sdist* on any platform. On the other hand it is most likely
    impossible to use a *bdist* targeted for another platform.

    So if no *bdist* of the project is available for the target platform, the
    *sdist* can still be used and eventually a target specific *bdist* can be
    built locally.


Built distribution
^^^^^^^^^^^^^^^^^^

A built distribution, sometimes abbreviated as *bdist*,
is a distribution format.
It is designed
so that the installation step is as straightforward as possible.
In short: files only need to be extracted from the built distribution archive
and copied to the right locations on disk.
It does not require any kind of build step,
as all files in a built distribution are already built
for the specific target environment.
Build distributions can be platform-specific.

Nowadays the only kind of built distributions
one should know about is the *wheel*.
The *egg* is an older kind of built distribution
that should not be used anymore (use *wheel* instead).


Wheel
"""""

*Wheel* is a *built distribution* format.
It is the preferred format of *distribution package*.
It is defined by a `standard specification`__.
A *wheel* is a file with the ``.whl`` extension.

__ https://packaging.python.org/en/latest/specifications/binary-distribution-format/


Python package index
--------------------

The *Python package index*, commonly called *PyPI*,
is the main repository of
Python project distributions packages.

It can be found at following URL:

* https://pypi.org/


References
==========

* David Beazley "*Modules and Packages: Live and Let Die!*"

    * http://www.dabeaz.com/modulepackage/ModulePackage.pdf

* Glossary — Python Packaging User Guide

    * https://packaging.python.org/en/latest/glossary/


.. EOF
