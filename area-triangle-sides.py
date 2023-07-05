
import math

def calculateArea(inputs):
    side1, side2, side3 = inputs
    s = (side1 + side2 + side3) / 2
    return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))

def getUserInput():
    return [float(input('Enter the length of side 1: ')),
            float(input('Enter the length of side 2: ')),
            float(input('Enter the length of side 3: '))]
    
print('The area of the triangle is %.2f' % calculateArea(getUserInput()))