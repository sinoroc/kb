..


****************
Python packaging
****************

Introduction
============

About proper packaging of Python projects...


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
