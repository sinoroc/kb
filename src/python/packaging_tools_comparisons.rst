..


***************************
Packaging tools comparisons
***************************

.. contents::
    :local:


Use cases
=========

.. csv-table::
    :align: left
    :header-rows: 1
    :stub-columns: 1

    ,Install Python,Install packages,Build distributions,Upload distributions,Manage virtual environments,Lock files
    build,no,no,yes,no,no,no
    Flit,no,yes,yes,yes,yes,yes
    Hatch,no,yes,yes,yes,yes,no
    PDM,no,yes,yes,yes,yes,yes
    pip,no,yes,yes,no,no,yes
    pip-tools,no,yes,no,no,no,yes
    Pipenv,no,yes,no,no,yes,yes
    pipx,no,yes,no,no,no,no
    Poetry,no,yes,yes,yes,yes,yes
    pyenv,yes,no,no,no,no,no
    Pyflow,yes,yes,yes,yes,yes,yes
    setuptools,no,yes,yes,no,no,no
    twine,no,no,no,yes,no,no
    venv,no,no,no,no,yes,no
    virtualenv,no,no,no,no,yes,no
    virtualenvwrapper,no,no,no,no,yes,no
    wheel,no,no,yes,no,no,no

Build back-ends are not listed here, but they are in a dedicated section below.


Comparisons
===========

Development workflow tools
--------------------------

.. csv-table::
    :align: left
    :header-rows: 1
    :stub-columns: 1

    ,``[build-system]`` (PEP-517),Build,Upload,Env,Interchangeable build back-end,Plugins,Lock file
    Flit,yes,yes,yes,no,no,no,no
    Hatch,yes,yes,yes,yes,no,yes,no
    PDM,yes,yes,yes,yes,yes,yes,yes
    Poetry,yes,yes,yes,yes,no,yes,yes
    Pyflow,no,yes,yes,yes,no,no,yes
    
See also build back-end features in dedicated section.

There is no standard for lock files.


Install Python interpreters
---------------------------

.. csv-table::
    :align: left
    :header-rows: 1
    :stub-columns: 1

    ,Install Python interpreters
    pyenv,yes
    Pyflow,yes


Install packages
----------------

.. csv-table::
    :align: left
    :header-rows: 1
    :stub-columns: 1

    ,Dependency resolution,Editable
    pip,yes,yes
    pip-tools,yes,yes
    Pipenv,yes,yes
    pipx,yes,no

``pipx`` is intended to be used to install standalone applications
rather than to install packages in a virtual environment.


Build distributions
-------------------

These tools are also called "*build front-ends*".

.. csv-table::
    :align: left
    :header-rows: 1
    :stub-columns: 1

    ,``[build-system]`` (PEP-517),sdist,wheel
    build,yes,yes,yes
    pip,yes,no,yes
    wheel,no,no,yes
    "dev workflow tools (Hatch, Flit, PDM, Poetry, etc.)",yes,yes,yes


Build back-ends
---------------

.. csv-table::
    :align: left
    :header-rows: 1
    :stub-columns: 1

    ,``[build-system]`` (PEP-517),``[project]`` (PEP-621),editable (PEP-660),C extensions
    ``enscons``,yes,yes,yes,yes
    ``flit-core``,yes,yes,yes,no
    ``hatchling``,yes,yes,yes,no
    ``pdm-backend``,yes,yes,yes,no
    ``poetry-core``,yes,no,yes,[#]_
    ``pymsbuild``,yes,no,no,yes
    ``trampolim``,yes,yes,no,no
    ``setuptools``,yes,yes,yes,yes
    ``whey``,yes,yes,yes,no

.. [#]  Poetry has an undocumented feature allowing
        the customization of the build process via a ``build.py`` file,
        which indirectly allows the handling of C extensions
        (this is  comparable to ``setuptools`` own `setup.py`).


Upload distributions
--------------------

.. csv-table::
    :align: left
    :header-rows: 1
    :stub-columns: 1

    ,Upload
    Flit,yes
    Hatch,yes
    PDM,yes
    Poetry,yes
    twine,yes


Manage virtual environments
---------------------------

.. csv-table::
    :align: left
    :header-rows: 1
    :stub-columns: 1

    ,For any Python interpreter,Description in file
    Hatch,yes,yes [#]_
    nox,yes,yes [#]_
    PDM,yes,no
    Pipenv,yes,no
    Poetry,yes,no
    tox,yes,yes [#]_
    venv,no,no
    virtualenv,yes,no
    virtualenvwrapper,yes,no
 
Unlike all the other tools here,
``venv`` is part of Python's own standard library,
it is always available without having to be installed separately.

.. [#] ``[tool.hatch.envs]`` section of ``pyproject.toml``
.. [#] ``noxfile.py``
.. [#] ``tox.ini``


Lock files
----------

There is no PyPA standard for the concept of "*lock files*".
There is some kind of a *de facto* convention
around *pip*'s ``requirements.txt`` file format
but it can not be considered a good enough *lock file* format.

.. csv-table::
    :align: left
    :header-rows: 1
    :stub-columns: 1

    ,Format
    pip,``requirements.txt``
    pip-tools,``requirements.txt``
    Pipenv,``Pipfile.lock``
    poetry,``poetry.lock``
    PDM,``pdm.lock``


..
    EOF
