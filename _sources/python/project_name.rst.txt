..


*******************
Python project name
*******************

Problem
=======

How to get the name of the project containing the current module (or package)?

* https://stackoverflow.com/a/60363617
* https://stackoverflow.com/a/60351412
* https://stackoverflow.com/a/60975978
* https://stackoverflow.com/a/63849982


Solution
========

.. code::

    #!/usr/bin/env python3

    import importlib.util
    import pathlib

    import importlib_metadata

    def get_distribution(file_name):
        result = None
        for distribution in importlib_metadata.distributions():
            try:
                relative = (
                    pathlib.Path(file_name)
                    .relative_to(distribution.locate_file(''))
                )
            except ValueError:
                pass
            else:
                if relative in distribution.files:
                    result = distribution
        return result

    def _alpha():
        file_name = importlib.util.find_spec('alpha').origin
        distribution = get_distribution(file_name)
        print("alpha", distribution.metadata['Name'])

    def _bravo():
        import bravo
        file_name = bravo.__file__
        distribution = get_distribution(file_name)
        print("bravo", distribution.metadata['Name'])

    if __name__ == '__main__':
        _alpha()
        _bravo()


.. EOF
