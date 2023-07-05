water_heat_capacity = 4.186
water_density = 1.0

def getUserInput():
    return [float(input('Enter mass of water (grams): ')),
            float(input('Enter delta T (Celsius): '))]

def computeEnergy(inputs):
    mass, delta_t = inputs
    return mass * water_heat_capacity * delta_t

print('The total amount of energy added or removed to achieve the desired',
      'temperature change is %.2f Joules.' % computeEnergy(getUserInput()))

