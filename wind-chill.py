wc_factor = 13.12

def computeWindChill(air_temperature, wind_speed):
    return (wc_factor + (0.6215 * air_temperature) - 
            (11.37 * (wind_speed ** 0.16)) + (0.3965 * air_temperature * (wind_speed ** 0.16))
    )
def getUserInput():
    return {
        'air_temperature': int(input('Enter the air temperature in degrees Celsius: ')),
        'wind_speed': int(input('Enter the windspeed in km/h: '))
    }

print('The wind chill is %.1f degrees Celsius.' % computeWindChill(**getUserInput()))