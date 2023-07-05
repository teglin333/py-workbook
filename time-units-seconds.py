# convert the number of seconds into a duration string of the format
# D:HH:MM:SS

#conversion factors
days_to_secs_cf    = 86400
hours_to_secs_cf   = 3600
minutes_to_secs_cf = 60

def computeDurationValues(seconds):
    return {
        'days': seconds // days_to_secs_cf,
        'hours': (seconds % days_to_secs_cf) // hours_to_secs_cf,
        'minutes': ((seconds % days_to_secs_cf) % hours_to_secs_cf // 
                      minutes_to_secs_cf),
        'seconds': ((seconds % days_to_secs_cf) % hours_to_secs_cf) % 
                      minutes_to_secs_cf
    }

def formatDurationString(days, hours, minutes, seconds):
    return "%dd:%02dh:%02dm:%02ds" % (days, hours, minutes, seconds)

print('The duration is: %s' % formatDurationString(**computeDurationValues(
    int(input('Enter the total number of seconds: ')))))


