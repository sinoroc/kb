..


**********
setuptools
**********

.. contents::
    :backlinks: none
    :local:


Tests
=====

Place the tests in the ``test`` directory. Per default ``setuptools`` adds the
``test`` directory to the source distribution ``sdist``. This can be disabled
in the ``MANIFEST.in``.


Commands dependencies
=====================

Graph showing the dependencies between the common ``setuptools`` commands:

.. graphviz:: setuptools.dot


Extend install command
======================

.. warning::

    This is a work in progress that needs to be improved on.

This shows how to add a subcommand to the ``install`` command. This also shows
how the subcommand can add to the list of files to be installed (packaged in a
``bdist``).

.. code-block:: python

    class install_something(setuptools.Command):
        user_options = [
            ('install-dir=', 'd', "directory to install to"),
        ]
        def initialize_options(self):
            self.install_dir = None
        def finalize_options(self):
            self.outputs = []
            self.set_undefined_options(
                'install',
                ('install_lib', 'install_dir'),
            )
        def run(self):
            self.outputs.append('package/something.bin')
            self.mkpath(self.install_dir + 'package')
            self.copy_file(
                'src/package/something.bin',
                self.install_dir + 'package/something.bin',
            )
        def get_outputs(self):
            return self.outputs


    class install(distutils.command.install.install):
        _sub_command = (
            'install_something',
            None,
        )
        _sub_commands = distutils.command.install.install.sub_commands
        sub_commands = [_sub_command] + _sub_commands


.. EOF
