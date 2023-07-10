# given an integer, return the factorial value
# fails when n >= 999 due to the default stack size setting in sys

from functools import reduce

def factorial_recursive(integer):
    return integer if integer == 1 else integer * factorial_recursive(integer - 1)
    
def factorial_nonrecursive(integer):
    return reduce(lambda x, y: x * y, range(1, integer+1))

while True:
    try:
        print('The value of the factorial is %d.' % 
              factorial_recursive(int(input('Enter an integer: '))))
        break
    except ValueError:
        print('Invalid input.')