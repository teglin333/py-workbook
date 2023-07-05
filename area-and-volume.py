import math
import fractions

def computeAreaCircle(radius):
    return math.pi * (radius ** 2)

def computeVolumeCylinder(radius):
    return fractions.Fraction(4, 3) * math.pi * (radius ** 3)

def getUserInput():
    return float(input('Enter the radius in centimeters: '))

radius = getUserInput()
print('The area of a circle with radius %.2f is %.2f square centimeters.' % 
      (radius, computeAreaCircle(radius)))
print('The volume of a cylinder with radius %.2f is %.2f cubic centimeters.' % 
      (radius, computeVolumeCylinder(radius)))

