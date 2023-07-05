import math

acceleration_constant = 9.8
initial_speed = 0

def calculateSpeed(height):
    return math.sqrt((initial_speed ** 2) + 2 * acceleration_constant * height)

def getUserInput():
    return float(input('Enter the height of the object in meters: '))

print('The final speed of the falling object is %.2f m/s.' % 
      calculateSpeed(getUserInput()))

