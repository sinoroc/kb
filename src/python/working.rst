..


Working with Python
===================

No *pip*
--------

Do not install a global system-wide version of *pip* at all.

There is almost never a good reason to install global system-wide packages via
*pip* to begin with. Especially on Linux where the default version of Python
is part of the system and used by the system. So mixing this with Python
projects that the user install install themselves via *pip* is very likely to
cause conflicts sooner rather than later.


Use isolation
-------------

If Python tools are needed to be always available from the command line, then
isolate them with *zapp*, *shiv*, or *pex*.

* *zapp* https://pypi.org/project/zapp/
* *shiv* https://pypi.org/project/shiv/
* *pex* https://pypi.org/project/pex/

Those are all *zipapp* single-file Python executables.

* https://www.python.org/dev/peps/pep-0441/
* https://docs.python.org/3/library/zipapp.html

*shiv* and *pex* applications are self extractable. *zapp* does not need to be
extracted. The code is executed directly from within the zip-compressed
archive.

*pex* applications are executed from their own virtual environment. *zapp*
applications are not executed in a virtual environment. Not sure about *shiv*.

*shiv* applications show up somehow in the current environment. Whereas *zapp*
applications do not, so they are perfect for tools such as *deptree*, and
*pipdeptree*.


Use *toolmaker*
---------------

To automate the creation of single file Python applications with *zapp*,
*shiv*, or *pex*, one can use *toolmaker*.

* https://pypi.org/project/toolmaker/


Use *venv*
----------

Python 3 has the module *venv* in its standard library since version 3.3.

* https://docs.python.org/3/library/venv.html

So the need for the third party library *virtualenv* is much less pressing.

.. code::

    $ python3 -m venv .venv
    $ . .venv/bin/activate


Do not activate virtual environments
------------------------------------

The scripts that are installed in a virtual environment (with *setuptools* at
least) get a shebang with the full path to the Python interpeter from the
virtual environment. So there is no need to activate the virtual environment
to call such scripts.

.. code::

    $ .venv/bin/myscript
    $ .venv/bin/python3 -m mymodule


.. EOF
