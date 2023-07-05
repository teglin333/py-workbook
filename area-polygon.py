import math

def computeArea(inputs):
    side_length, num_sides = inputs
    return (num_sides * (side_length ** 2) / 
           (4 * math.tan(math.pi / num_sides)))
    
def getUserInput():
    return [float(input('Enter length of a side in cm: ')),
            int(input('Enter the number of sides: '))]

print('The area of the regular polygon is %.2f square centimeters.' % 
      computeArea(getUserInput()))