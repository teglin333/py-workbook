import math

def sqrt(x: float, *, quality: int=12) -> float:
    """
    Implements Newton's method to compute and display the sequare root
    of a number.
    
    The number of iterations is implied by the convergence criterion, which is
    set using the integer passed to the function's quality parameter.
    
    :param float x: input
    :param int quality: modify the convergence criterion
    :return: estimated square root
    :rvalue: float
    """
    guess = (x / 2)
    while abs((guess * guess - x)) > (10 ** (0 - quality)):
        guess = ((guess + (x / guess)) / 2)
    return guess

print(sqrt(0))
print(sqrt(1))
print(sqrt(2))
print(sqrt(4))
print(sqrt(4, quality=99))
print(sqrt(764234, quality=99999))