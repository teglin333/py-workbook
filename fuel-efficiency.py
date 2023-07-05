# convert fuel efficiency in American units to the eqivalent value in
# Canadian units

km_conversion_factor = 1.609
liters_conversion_factor = 3.785

def convertMilesPerGallon(milesPerGallon):
    return ((milesPerGallon) * (1 / liters_conversion_factor)) * km_conversion_factor

mpg = float(input('What is the vehicle miles per gallon? '))

print('The value in Canadian units is %.2f liters per kilometer.'
      % convertMilesPerGallon(mpg))