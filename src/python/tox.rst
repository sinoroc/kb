..


*******
``tox``
*******

Introduction
============

The ``tox`` tool allows to easily create multiple Python virtual environments
while specifying a list of Python dependencies to install in each environment
as well as a list of commands to run in each environment.

The original purpose of the tool is to test the source distribution (``sdist``)
of a Python project against multiple combinations of Python interpreters and
Python dependencies.

https://tox.readthedocs.io/


Defaults
========

.. code-block:: ini
    :caption: tox.ini
    
    # ...
    [testenv]
    basepython = python3
    commands =
        python setup.py check test
    deps =
        -rrequirements/test.txt
    # ...


Development environment
=======================

.. code-block:: ini
    :caption: tox.ini

    # ...
    [testenv:develop]
    commands =
        python setup.py check
    deps =
        -rrequirements/develop.txt
    usedevelop = True
    # ...


Notes
=====

``setuptools`` and ``sdist``
----------------------------

``tox`` builds the ``sdist`` independently from the virtual environments. So it
is not directly possible to specify which version of ``setuptools`` should be
used to build the ``sdist``.


.. EOF
