# time-units-days.py
# compute and display the total number of seconds

# conversion factors
days_to_secs_cf    = 86400
hours_to_secs_cf   = 3600
minutes_to_secs_cf = 60

def computeSeconds(days, hours, minutes, seconds):
    return ((days_to_secs_cf * days) + (hours_to_secs_cf * hours) +
           (minutes_to_secs_cf * minutes) + seconds)

def getUserInput():
    return {'days': int(input('Enter the number of days: ')),
            'hours': int(input('Enter the number of hours: ')),
            'minutes': int(input('Enter the number of minutes: ')),
            'seconds': int(input('Enter the number of seconds: '))}

print('The total number of seconds is %d.' % computeSeconds(**getUserInput()))
