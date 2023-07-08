# compute the real roots of a quadratic function
# display a message indicating the number and value(s) of the real roots

import math

def computeRoots(a, b, c):
    if (a != 0):
        discriminant = (b ** 2) - (4 * a * c)
        if discriminant > 0:
            return [(-b + math.sqrt(discriminant)) / (2 * a), 
                    (-b - math.sqrt(discriminant)) / (2 * a)]
        elif discriminant == 0:
            return [(-b / (2 * a))]
    else:
        return []  # no real roots
            
while True:
    try:
        a = float(input('Enter constant a (nonzero): ')) 
        if a != 0:
            constants = {'a': a, 
                         'b': float(input('Enter constant b: ')),
                         'c': float(input('Enter constant c: '))}
            roots = computeRoots(**constants)
            if len(roots): 
                if len(roots) == 2:
                    print('The real roots of the quadratic function with',
                          'constants %.2f, %.2f, and %.2f are' %
                          (tuple(constants.values())), '%.2f and %.2f.'
                          % tuple(roots))
                    break
                elif len(roots) == 1:
                    print('The real root of the quadratic function with',
                          'constants %.2f, %.2f, and %.2f is' % 
                          (tuple(constants.values())), '%.2f.' % tuple(roots))
                    break
            else:
                print('A quadratic function with constants %.2f, %.2f, and %.2f' 
                      % (tuple(constants.values())), 'has no real roots.')
                break
        else:
            raise ValueError("Constant a must be nonzero.")
    except ValueError as e:
        print("Invalid input. %s" % e)