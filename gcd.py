#!/usr/bin/env python3
# gcd.py

def validate(func):
    def wrapper(*args):
        for arg in args:
            if arg < 1:
                raise ValueError('Positive integers only.')
        return func(*args)
    return wrapper


@validate
def gcd(m: int, n: int, /) -> int:
    """
    Find the greatest common denominator (GCD), given two integers.
    """
    d = m if m > n else n
    while m % d or n % d:
        d -= 1
    return d


try:
    print(gcd(5, 10))
except ValueError as e:
    print('Invalid input: %s' % e)