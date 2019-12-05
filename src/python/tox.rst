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

It is a good idea to setup an environment for interactive use. The purpose of
this environment is to be actually activated from the interactive shell in
order to do the actual development.

The commands should be relatively neutral. There is no need to trigger any test
suite or linting, since those should be triggered manually once the environment
is active.

The environment should contain the dependencies for all use cases: test, build,
distribute, of course install, and then eventually some more to develop.

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

setuptools and sdist
--------------------

``tox`` builds the ``sdist`` independently from the virtual environments. So it
is not directly possible to specify which version of ``setuptools`` should be
used to build the ``sdist``.

Since ``tox`` version ``3.2.0`` the configuration option ``requires`` can help
making sure that the version of ``setuptools`` is appropriate.

* https://tox.readthedocs.io/en/3.2.0/config.html#confval-requires=LIST


One step further is possible since version ``3.3.0`` and the configuration
option ``isolated_build``.

* https://tox.readthedocs.io/en/3.3.0/config.html#confval-isolated_build=True|False(default)


tox-venv
--------

Since Python 3.3 the standard library includes the module ``venv`` that can
replace the ``virtualenv`` package. Install ``tox-venv`` alongside ``tox`` to
take advantage of this feature. See also the ``requires`` configuration option
of ``tox`` to make sure ``tox-venv`` is available.

* https://pypi.org/project/tox-venv/

.. code-block:: ini
    :caption: tox.ini

    [tox]
    requires =
        tox-venv


GitLab CI
---------

Automatically set the ``TOXENV`` environment variable based on the job name:

.. code-block:: yaml
    :caption: .gitlab-ci.yml

    '.review':
      script:
        - 'export TOXENV="${CI_JOB_NAME##review }"'
        - 'python3 -m pip install tox'
        - 'python3 -m tox'

    'review py37':
      extends: '.review'
      image: 'python:3.7'

    'review py38':
      extends: '.review'
      image: 'python:3.8'


.. EOF
