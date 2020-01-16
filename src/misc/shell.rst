..


*****
Shell
*****

Create a temporary directory and change to it:

.. code-block:: console

    $ cd ($mktemp --directory)
    $ cd ($mktemp -d)


List directories by disk usage:

.. code-block:: console

    $ du --human-readable | sort --human-numeric-sort --reverse | less
    $ du -h | sort -hr | less

.. code-block:: console

    $ sudo du --all --human-readable --max-depth=1 / 2>/dev/null | sort --human-numeric-sort --reverse
    $ sudo du -a -d 1 -h / 2>/dev/null | sort -hr


.. EOF
