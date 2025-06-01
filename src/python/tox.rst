..


***
tox
***

.. contents::
    :backlinks: none
    :local:


Introduction
============

The ``tox`` tool allows to easily create multiple Python virtual environments
while specifying a list of Python dependencies to install in each environment
as well as a list of commands to run in each environment.

The original purpose of the tool is to test the source distribution (``sdist``)
of a Python project against multiple combinations of Python interpreters and
Python dependencies.

* https://tox.readthedocs.io/


Defaults
========

.. code-block:: ini
    :caption: tox.ini

    [tox]
    envlist =
        py37
        py38
    isolated_build = True
    # ...

    [testenv]
    commands =
        python3 -m pytest
    extras =
        dev_test
    # ...


Development environment
=======================

It is a good idea to setup an environment for interactive use. The purpose of
this environment is to be actually activated from the interactive shell in
order to do the actual development.

The ``commands`` configuration setting should be relatively neutral.
It can also be left empty.
There is no need to trigger any test suite or linting, since those should be triggered manually once the environment is active.

The environment should contain the dependencies for all use cases: test, build,
distribute, and then eventually some more to develop.

.. code-block:: ini
    :caption: tox.ini

    # ...
    [testenv:develop]
    commands =
    deps =
        dev_doc
        dev_lint
        dev_package
        dev_test
    usedevelop = True
    # ...


Notes
=====

GitLab CI
---------

Automatically set the ``TOXENV`` environment variable based on the job name:

.. code-block:: yaml
    :caption: .gitlab-ci.yml

    '.review':
      script:
        - 'export TOXENV="${CI_JOB_NAME##review}"'
        - 'python3 -m pip install tox'
        - 'python3 -m tox'

    'review py37':
      extends: '.review'
      image: 'python:3.7'

    'review py38':
      extends: '.review'
      image: 'python:3.8'


.. EOF
