wc_factor = 13.12

def computeWindChill(*, air_temperature: float, wind_speed: float) -> float:
    """
    Calculate the wind chill index given the temperature and wind speed.
    The wind chill index is a measure of how cold it feels when the wind is
    factored in with the actual air temperature.
        
    :param float air_temperature: Outdoor air temperature in degrees Celsius.
    :param float wind_speed: The wind speed in kilometers per hour.
    :return: The calculated wind chill.
    :rtype: float

    :reference:
        - Title: Cold Wind Chill Chart (National Weather Service)
        - Website: https://www.weather.gov/safety/cold-wind-chill-chart
        
    """
    return (wc_factor + (0.6215 * air_temperature) - 
            (11.37 * (wind_speed ** 0.16)) + (0.3965 * air_temperature * (wind_speed ** 0.16))
    )
    
def getUserInput():
    return {
        'air_temperature': int(input('Enter the air temperature in degrees Celsius: ')),
        'wind_speed': int(input('Enter the windspeed in km/h: '))
    }

print('The wind chill is %.1f degrees Celsius.' % computeWindChill(**getUserInput()))