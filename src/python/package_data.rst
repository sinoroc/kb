..


*******************
Python package data
*******************

Further down is a minimal example showing how to achieve both:

* packaging a data file ``file.src`` in ``sdist`` only;
* and packaging another data file ``file.bin`` in ``bdist`` only;
* additionally it shows how ``file.all`` is packaged in both distribution
  packages and ``file.not`` in none of them.


.. sidebar:: ``file.bin`` and built files

    Files such as ``file.bin`` are not in the original source code of the
    project (i.e. not in the `git` source code repository for example) but
    should still be installed. Typically these files are created during a build
    step such as ``./setup.py build`` for example (think ``gettext`` ``*.mo``
    messages catalogs).


The gist of it is:

* first and foremost, always thoroughly clean up the working directory between
  two packaging attempts while tweaking these packaging options (in particular
  empty the ``src/Thing.egg-info`` directory containing the ``SOURCES.txt``
  file as well as the ``build``, and ``dist`` directories) or the results will
  be inconsistent;
* set the ``include_package_data`` option to ``True``;
* ``file.all`` and files that belong in both ``sdist`` and ``bdist`` are
  specified in ``MANIFEST.in``;
* ``file.bin`` and files that belong in ``bdist`` only are specified in
  ``package_data``;
* ``file.src`` and files that belong in ``sdist`` only are specified in both
  ``MANIFEST.in`` and ``exclude_package_data``;
* ``file.not`` and files that do not belong in any distribution package are not
  specified anywhere.


The directory structure for our example:

.. code-block:: none

    .
    ├ MANIFEST.in
    ├ setup.py
    └ src
        └ thing
            ├ __init__.py
            └ data
                ├ file.all
                ├ file.bin
                ├ file.not
                └ file.src


In ``MANIFEST.in``:

.. code-block:: none

    recursive-include src/thing *.all
    recursive-include src/thing *.src


In ``setup.py``:

.. code-block:: python
    :emphasize-lines: 6-8

    #!/usr/bin/env python3

    import setuptools

    setuptools.setup(
        exclude_package_data={'thing': ['data/*.src']},
        include_package_data=True,
        package_data={'thing': ['data/*.bin']},
        #
        name='Thing',
        version='1.0.0',
        #
        package_dir={'': 'src'},
        packages=setuptools.find_packages(where='src'),
    )


This has been tested with:

* Python 3.6.7
* setuptools 39.0.1
* wheel 0.33.1


.. EOF
