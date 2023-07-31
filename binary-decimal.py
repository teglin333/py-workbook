#!/usr/bin/env python3
# bintodec.py

def bintodec(bin: bytes) -> int:
    """
    Given a string representing a binary number, convert it to base 10.
    """
    i = 0
    res = 0
    while i <= len(bin)- 1:
        if bin[len(bin) - 1 - i]:
            res += (2 ** i)
        i += 1
    return res

def dectobin(integer: int) -> str:
    """
    Given an integer, return a binary string representation.
    """
    res = []
    while True:
        res.insert(0, str(integer % 2))
        integer = integer // 2
        if not integer:
            break
    return ''.join(res)

def main():
    while True:
        try:
            binary_string = input('Enter a binary number: 0b')
            for bit in binary_string:
                if bit not in '01':
                    raise ValueError('Not a binary number.')
            binary_data = bytes([int(bit) for bit in binary_string])
            decimal = bintodec(binary_data)
            print('Binary: 0b%s' % binary_string)
            print('Decimal: %d' % decimal)
            decimal_string = input('Enter an integer value: ')
            binary_string = dectobin(int(decimal_string))
            print('Decimal: %s' % decimal_string)
            print('Binary: 0b%s' % binary_string)
            break
        except ValueError as e:
            print('Invalid input: %s' % e)
            continue


if __name__ == "__main__":
    main()
