# Read in a distance in feet and display the equivalent distance
# in inches, yards, and miles.

import fractions

inches_conversion_factor = 12
yards_conversion_factor = fractions.Fraction(1, 3)
miles_conversion_factor = fractions.Fraction(1, 5280)

def convert(x, conversion_factor):
    return x * conversion_factor

def feetToInches(x):
    return convert(x, inches_conversion_factor)

def feetToYards(x):
    return convert(x, yards_conversion_factor)

def feetToMiles(x):
    return convert(x, miles_conversion_factor)

def convertUnits(x):
    return [x, feetToInches(x), feetToYards(x), feetToMiles(x)]

print('%d feet corresponds to %d inches, %.2f yards, and %.2f miles.' % 
      tuple(convertUnits(int(input('Enter the number of feet as an integer: ')))))
