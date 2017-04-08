..


**********
``pytest``
**********

Introduction
============

Python test runner

http://pytest.org/


``pep8`` and ``pylint``
=======================

.. sidebar:: ``pep8`` vs. ``pycodestyle``

    The Python project ``pep8`` has actually be renamed to ``pycodestyle``. But
    there is no ``pytest-pycodestyle`` project yet.

    https://bitbucket.org/pytest-dev/pytest-pep8/issues/15


Use the plugins ``pytest-pep8`` and ``pytest-pylint``.


``pep8`` only
-------------

Run only the ``pep8`` linting.

.. code-block:: console
    :caption: shell console

    $ pytest --pep8 -m pep8


``pylint`` only
---------------

Run only the ``pylint`` linting.

.. code-block:: console
    :caption: shell console

    $ pytest --pylint -m pylint


Both ``pep8`` and ``pylint``
----------------------------

Run both linting tools but not the tests themselves.

.. code-block:: console
    :caption: shell console

    $ pytest --pep8 --pylint -m 'pep8 or pylint'

Run all the tests including the linting tools.

.. code-block:: console
    :caption: shell console

    $ pytest


.. EOF
