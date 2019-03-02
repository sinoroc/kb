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


GitLab CI
---------

.. code-block:: yaml
    :caption: .gitlab-ci.yml

    '.test_common': &job_test_common
      script:
        - 'JOB_NAME=( ${CI_JOB_NAME} )'
        - 'export TOXENV="${JOB_NAME[1]}"'
        - 'pip install tox'
        - 'tox'

    'test py35':
      <<: *job_test_common
      image: 'python:3.5'

    'test py36':
      <<: *job_test_common
      image: 'python:3.6'


The job name is read as a ``bash`` array split at the whitespaces. The second
item is one of the names automatically recognised by ``tox``. This name is set
in the ``TOXENV`` environment variable, that ``tox`` reads to choose which
virtual environment should be used.


.. EOF
