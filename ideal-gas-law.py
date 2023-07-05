ideal_gas_constant = 8.314
pascals_conversion_factor = 6894.75729

class Temperature:
    _f = None
    _c = None
    _k = None

    @property
    def f(self):
        return self._f

    @f.setter
    def f(self, temp):
        self._f = temp
        self._k = (temp - 32) * 5 / 9 + 273.15
        self._c = (temp - 32) * 5 / 9

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, temp):
        self._c = temp
        self._f = 1.8 * temp + 32
        self._k = temp + 273.15

    @property
    def k(self):
        return self._k

    @k.setter
    def k(self, temp):
        self._k = temp
        self._c = temp - 273.15
        self._f = (temp - 273.15) * 9 / 5 + 32

def convertPsiToPascals(pressure_psi):
    return pressure_psi * pascals_conversion_factor
        
def calculateMoles(inputs):
    temperature_k, volume, pressure_psi = inputs
    pressure_pascals = convertPsiToPascals(pressure_psi)
    return (pressure_pascals * volume) / (ideal_gas_constant * temperature_k)

def getUserInput():
    temperature_input = float(input('Enter the gas temperature: '))
    temperature = Temperature()
    while True:
        units_input = input('Enter the temperature units (C, F, K): ').lower()
        if units_input == 'c':
            temperature.c = temperature_input
            break
        elif units_input == 'f':
            temperature.f = temperature_input
            break
        elif units_input == 'k':
            temperature.k = temperature_input
            break
        else:
            print('Invalid input. Please try again.')
            continue
    
    volume_input = float(input('Enter the volume in liters: '))
    pressure_input = float(input('Enter the pressure in PSI: '))

    return temperature.k, volume_input, pressure_input

print('Amount of gas in moles: %.2g' % calculateMoles(getUserInput()))
