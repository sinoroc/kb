#!/usr/bin/env python3

"""Fizz buzz."""

import sys


class Injector:  # pylint: disable=too-few-public-methods
    """Callable to inject a word if value is a multiple."""

    def __init__(self, multiple: int, word: str) -> None:
        """Initializer."""
        self._multiple = multiple
        self._output = f'{word}!'

    def __call__(self, value: int):
        """Callable."""
        result = None
        if value % self._multiple == 0:
            result = self._output
        return result


def fizz_buzz(start: int, end: int) -> None:
    """Fizz buzz."""
    injectors = [
        Injector(3, 'Fizz'),
        Injector(5, 'Buzz'),
    ]

    for i in range(start, end + 1):
        items = []
        output = None

        for injector in injectors:
            if (item := injector(i)):
                items.append(item)

        output = ' '.join(items) if items else str(i)

        print(output)


def _main() -> int:
    fizz_buzz(1, 50)
    return 0


if __name__ == '__main__':
    sys.exit(_main())
