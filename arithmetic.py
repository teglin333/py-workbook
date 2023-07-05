# Compute and display arithemetic functions on two integers obtained
# from the user.

import math

def sum(a, b):
    return a + b

def difference(a, b):
    return a - b

def product(a, b):
    return a * b

def quotient(a, b):
    return a / b

def remainder(a, b):
    return a % b

def log10(a):
    return math.log10(a)

def powerof(a, b):
    return a ** b

a = int(input('Enter the first integer: '))
b = int(input('Enter the second integer: '))

print('The sum of %d and %d is %d.' % (a, b, sum(a, b)))
print('The difference when %d is subtracted from %d is %d.' % (
    b, a, difference(b, a)))
print('The product of %d and %d is %d.' % (a, b, product(a, b)))
print('The quotient when %d is divided by %d is %.2f.' % (a, b, quotient(a, b)))
print('The remainder when %d is divided by %d is %d.' % (a, b, remainder(a, b)))
print('The result of the common logarithm of %d is %d.' % (a, log10(a)))
print('The result when %d is raised to the power of %d is %.2g.' % (
    a, b, powerof(a, b)))