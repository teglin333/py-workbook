#!/usr/bin/env python3
# primefactors.py

def validate(f: any) -> any:
    def wrapper(*args):
        for arg in args:
            if arg < 2:
                raise ValueError('Integer must be greater than 2.')
        return f(*args)
    return wrapper


@validate
def primefactors(integer: int, /) -> list:
    """
    Determine the prime factorization of an integer.
    """
    factor = 2
    res = []
    while factor <= integer:
        if integer % factor:
            res.append(factor)
            integer = integer // factor
        else:
            factor += 1
    return res


while True:
    try:
        userinput = int(input('Enter an integer greater than 2: '))
        print('The prime factors of %d are:' % userinput)
        list(map(print, primefactors(userinput)))
        break
    except ValueError as e:
        print('Invalid input: %s' % e)
        continue
