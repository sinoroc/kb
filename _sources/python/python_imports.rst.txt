..


**************
Python imports
**************


#. Identify clearly what you want your top level modules and packages to be.

#. Make all imports absolute.

#. Either:

    * make your project a real installable project, so that those top level
      modules and packages are installed in the environment's ``site-packages``
      directory;

    * or make sure that the current working directory is the one containing the
      top level modules and packages.

#. Make sure to call your code via the *executable module* method instead of
   the *script* method:

    * DO

        * ``path/to/pythonX.Y -m toplevelpackage.module``
        * ``path/to/pythonX.Y -m toplevelmodule``
        * ``path/to/pythonX.Y -m toplevelpackage.subpackage``
          (assuming there is a ``toplevelpackage/subpackage/__main__.py`` file)

    * DON'T

        * ``path/to/pythonX.Y toplevelpackage/module.py``
        * ``path/to/pythonX.Y toplevelmodule.py``

#. Later on, once it all works well and everything is under control, you might
   decide to change some or all imports to relative. (If things are done right,
   I believe it could be possible to make it so that it is possible to call the
   executable modules from any level within the directory structure as the
   current working directory.)

**References:**

* Old reference, possibly outdated, but assuming I interpreted it right, it
  says that running *scripts* that live in a package is an anti pattern, and
  one should use ``python -m package.module`` instead:
  
    * https://mail.python.org/pipermail/python-3000/2007-April/006793.html
    * https://www.python.org/dev/peps/pep-3122/


.. EOF
