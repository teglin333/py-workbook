# Compute and display the denominations of the coins that should be used to
# give that amount of change, given a number of cents provided by the user.

import math

penny = 1
nickel = 5
dime = 10
quarter = 25
loonie = 100
toonie = 200

def calculateChange(cents):
    toonies = math.trunc(cents / toonie)
    cents -= toonies * toonie
    loonies = math.trunc(cents / loonie)
    cents -= loonies * loonie
    quarters = math.trunc(cents / quarter)
    cents -= quarters * quarter
    dimes = math.trunc(cents / dime)
    cents -= dimes * dime
    nickels = math.trunc(cents / nickel)
    cents -= nickels * nickel
    return [cents, nickels, dimes, quarters, loonies, toonies]
    
cents_input = int(input('Enter number of cents: '))
change = calculateChange(cents_input)
print('Your change is %d toonies, %d loonies, %d quarters, %d dimes, '
      % (change[5], change[4], change[3], change[2]),
      '%d nickels, and %d pennies.' % (change[1], change[0]))

