"""
Ideal Gas Law Calculator
========================

SYNOPSIS
--------
Calculate the moles of a substance using the ideal gas law, based on
measurements provided by the user.

DESCRIPTION
-----------
Implements a calculator for estimating the moles of a substance using the ideal
gas law. It allows users to input temperature, volume, and pressure values in
and then calculates the corresponding amount of gas in moles. Included is a 
utility function to convert pressure from pounds per square inch (psi) to 
pascals, as well as a temperature class that handles temperature unit 
conversions between Celsius, Fahrenheit, and Kelvin. 


REFERENCE
---------
https://en.wikipedia.org/wiki/Ideal_gas_law

"""
from typing import Optional, Tuple

ideal_gas_constant = 8.314
pascals_conversion_factor = 6894.75729

class Temperature:
    """
    A class for handling temperature conversions between Celsius, Fahrenheit, 
    and Kelvin.

    Attributes:
        _f (Optional[float]): Temperature value in Fahrenheit.
        _c (Optional[float]): Temperature value in Celsius.
        _k (Optional[float]): Temperature value in Kelvin.

    Methods:
        f (property): Get or set the temperature in Fahrenheit.
        c (property): Get or set the temperature in Celsius.
        k (property): Get or set the temperature in Kelvin.
    """
    def __init__(self):
        self._f: Optional[float] = None
        self._c: Optional[float] = None
        self._k: Optional[float] = None

    @property
    def f(self) -> Optional[float]:
        return self._f

    @f.setter
    def f(self, temp: float) -> None:
        """
        Set the temperature in Fahrenheit.

        Args:
            temp (float): Temperature value in Fahrenheit.

        Returns:
            None
        """
        self._f = temp
        self._k = (temp - 32) * 5 / 9 + 273.15
        self._c = (temp - 32) * 5 / 9

    @property
    def c(self) -> Optional[float]:
        """Get or set the temperature in Celsius."""
        return self._c

    @c.setter
    def c(self, temp: float) -> None:
        """
        Set the temperature in Celsius.

        Args:
            temp (float): Temperature value in Celsius.

        Returns:
            None
        """        
        self._c = temp
        self._f = 1.8 * temp + 32
        self._k = temp + 273.15

    @property
    def k(self) -> Optional[float]:
        """Get or set the temperature in Kelvin."""
        return self._k

    @k.setter
    def k(self, temp: float) -> None:
        """
        Set the temperature in Kelvin.

        Args:
            temp (float): Temperature value in Kelvin.

        Returns:
            None
        """        
        self._k = temp
        self._c = temp - 273.15
        self._f = (temp - 273.15) * 9 / 5 + 32


convertPsiToPascals = lambda pressure_psi: pressure_psi * pascals_conversion_factor
        
def calculateMoles(
    *, temperature_k: float, volume: float, pressure_psi: float
    ) -> float:
    """
    Calculate the moles of a substance using the ideal gas law.
    
    :key temperature_k: The temperature of the gas in degrees Kelvin.
    :key volume: The volume of gas in cubic meters.
    :key pressure_psi: The pressure of the gas in PSI.
    :return: The moles of substance in the gas. 
    """
    pressure_pascals = convertPsiToPascals(pressure_psi)
    return (pressure_pascals * volume) / (ideal_gas_constant * temperature_k)

def getUserInput() -> Tuple[float, float, float]:
    """
    Obtain gas temperature, volume, and pressure from the user.
    """
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
