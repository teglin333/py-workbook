feet_inches_cf = 12
inches_centimeter_cf = 2.54

def feetToInches(feet):
    return feet * feet_inches_cf

def inchesToCetimeters(inches):
    return inches * inches_centimeter_cf

def convertToCentimeters(inches, feet):
    return inchesToCetimeters(inches) + inchesToCetimeters(feetToInches(feet))

def getUserInput():
    return {'feet': int(input('How tall are you in feet? ')),
            'inches': int(input('How tall are you in inches? '))}
    
print('You are %.1f centimeters tall.' % convertToCentimeters(**getUserInput()))
