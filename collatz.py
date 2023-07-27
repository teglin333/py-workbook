#!/usr/bin/env python3
from uniplot import plot


def collatz_iterate(integer: int) -> int:
    """
    Given an integer n, iterate through the collatz function until f(n) is 1.
    """
    iterations = 0
    while integer > 1:
        iterations += 1
        if not integer % 2:
            integer = integer / 2
        else:
            integer = 3 * integer + 1
    return iterations


#  User Input and Plot
while True:
    try:
        input_integer = int(input('Enter an integer greater than 0: '))
        iteration_values = []
        for x in range(1, input_integer):
            iteration_values.append(collatz_iterate(input_integer))
            input_integer -= 1
        # print(list(iteration_values))
        plot(ys=list(iteration_values))
        break
    except ValueError:
        print('Invalid input.')
        continue
