..


**************
Python imports
**************


1. Identify clearly what you want your top level modules and packages to be.

2. Make all imports absolute.

3. Either:

    * make your project a real installable project, so that those top level
      modules and packages are installed in the environment's ``site-packages``
      directory;

    * or make sure that the current working directory is the one containing the
      top level modules and packages.

4. Make sure to call your code via the *executable module* method instead of
   the *script* method:

    * ``path/to/pythonX.Y -m toplevelpackage.module`` DO
    * ``path/to/pythonX.Y toplevelpackage/module.py`` DON'T
    * ``path/to/pythonX.Y -m toplevelmodule`` DO
    * ``path/to/pythonX.Y toplevelmodule.py`` DON'T
    * ``path/to/pythonX.Y -m toplevelpackage.subpackage`` DO (assuming there is
      a ``toplevelpackage/subpackage/__main__.py`` file)

5. Later on, once it all works well and everything is under control, you might
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