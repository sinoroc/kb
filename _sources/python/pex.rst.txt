..


***
pex
***

.. contents::
    :backlinks: none
    :local:


Introduction
============

In a couple of words: ``pex`` helps create *self-contained executable Python
virtual environments*.

https://pex.readthedocs.io/

https://www.youtube.com/watch?v=NmpnGhRwsu0


Bootstrap
=========

Bootstrap ``pex`` with these steps:

* create a short lived Python virtual environment;
* install ``pex`` in this environment;
* use the newly installed ``pex`` to create a ``pex`` file:

  * containing the ``pex`` project as well as the dependencies; *and*
  * having the ``pex`` console script as its entry point.

With Python 3 and the ``~/bin`` directory on the ``PATH`` this could look like
this:

.. code-block:: console
    :caption: shell console
    :emphasize-lines: 4-7

    $ python3 -m venv pexenv
    $ . pexenv/bin/activate
    (pexenv) $ pip install pex
    (pexenv) $ pex \
    > 'pex[requests,cachecontrol]' \
    > --console-script=pex \
    > --output-file=~/bin/pex
    (pexenv) $ deactivate
    $ rm --force --recursive pexenv
    $ which pex
    $ pex --version

The ``pexenv`` Python virtual environment can be deleted immediately
afterwards. ``pex`` can be used directly since it is self contained in its own
Python virtual environment within the ``~/bin/pex`` file.


Overview
========

Per default pex starts the Python interpreter in a dynamically created empty
virtual environment.

.. code-block:: console
    :caption: shell console

    $ pex
    Python 2.7.12 (default, Nov 19 2016, 06:48:10)
    [GCC 5.4.0 20160609] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> exit()

It is possible to select which Python interpreter should be used.

.. code-block:: console
    :caption: shell console

    $ pex --python=python3
    Python 3.5.2 (default, Nov 17 2016, 17:05:23)
    [GCC 5.4.0 20160609] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> exit()

``pex`` allows to specify which Python projects should be installed in the
virtual environment.

.. code-block:: console
    :caption: shell console

    $ pex 'requests<2.0.0' 'setuptools==30'
    Python 3.5.2 (default, Nov 17 2016, 17:05:23)
    [GCC 5.4.0 20160609] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    (InteractiveConsole)
    >>> import requests
    >>> requests.__version__
    '1.2.3'
    >>> import setuptools
    >>> setuptools.__version__
    '30.0.0'
    >>> exit()

The dependencies can be specified via a ``pip`` ``requirements.txt`` file.

.. code-block:: console
    :caption: shell console

    $ pex --requirement=requirements.txt

``pex`` also allows to specify an entry point that should be executed from
within the virtual environment.

.. code-block:: console
    :caption: shell console

    $ pex 'httpie==0.9.6' --console-script=http -- --version
    0.9.6
    $ pex --python=python3 --entry-point=http.server
    Serving HTTP on 0.0.0.0 port 8000 ...

Finally ``pex`` allows to write this self-contained executable virtual
environment into a single file.

.. code-block:: console
    :caption: shell console

    $ pex --python=python3 --entry-point=http.server --output-file=server.pex
    $ ./server.pex
    Serving HTTP on 0.0.0.0 port 8000 ...


Inspect
=======

Since ``pex`` files are ``ZIP`` archives, inspecting their content is very
straighforward.

.. code-block:: console
    :caption: shell console

    $ python -m zipfile -l example.pex
    $ unzip -l example.pex

It is a good idea to check that only the required and necessary dependencies
are included. Nothing more and nothing less should be found in the ``.deps``
directory.


setuptools
==========

To easily build a ``pex`` executable with ``setuptools`` use the ``bdist_pex``
command. ``bdist_pex`` will use the ``console_scripts`` entry point bearing the
exact name of the Python project itself.

.. code-block:: python
    :caption: setup.py
    :emphasize-lines: 3,6,9

    import setuptools

    NAME = 'Example'

    setuptools.setup(
        name=NAME,
        entry_points={
            'console_scripts': [
                '{}=example.app:run'.format(NAME),
            ],
        },
        # ...
    )


Requirements
------------

For a stricter control over the dependencies added to the ``pex`` file, a
``requirements.txt`` file can be specified via the ``--pex-args`` option.

.. code-block:: console
    :caption: shell console

    $ python setup.py bdist_pex --pex-args='--requirement=requirements.txt'


.. EOF
