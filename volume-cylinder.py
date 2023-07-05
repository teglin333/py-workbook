# Read the radius of the cylinder, along with its height, from the user and
# compute the volume. Display the result rounded to one decimal place.

import math

def baseArea(r):
    return (r ** 2) * math.pi

def volumeCylinder(r, h):
    return baseArea(r) * h

print('The volume of the cylinder is: %.1f centimeters.' % volumeCylinder(
    float(input('Enter the cylinder\'s base radius in centimeters: ')),
    float(input('Enter the cylinder\'s height in centimeters: '))))