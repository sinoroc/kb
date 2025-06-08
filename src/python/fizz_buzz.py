#!/usr/bin/env python3


class Injector:

    def __init__(self, multiple, word):
        self._multiple = multiple
        self._output = '{}!'.format(word)

    def __call__(self, value):
        result = None
        if value % self._multiple == 0:
            result = self._output
        return result


def fizz_buzz(start, end):
    injectors = [
        Injector(3, 'Fizz'),
        Injector(5, 'Buzz'),
    ]
    #
    for i in range(start, end + 1):
        items = []
        output = None
        #
        for injector in injectors:
            item = injector(i)
            if item:
                items.append(item)
        #
        if items:
            output = ' '.join(items)
        else:
            output = str(i)
        #
        print(output)


def main():
    fizz_buzz(1, 50)


if __name__ == '__main__':
    main()

# EOF
