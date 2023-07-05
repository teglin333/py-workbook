sound_levels = {
    130: 'a jackhammer',
    106: 'a gas lawnmower',
    70: 'an alarm clock',
    40: 'a quiet room'
}

while True:
    input_dbl = input('Enter the sound level in decibels: ')
    
    try:
        input_dbl = int(input_dbl)
        if input_dbl in sound_levels:
            print('A sound level of %d dB is comparable to the sound level of %s.' %
                  (input_dbl, sound_levels[input_dbl]))
            break
        else:
            min_dbl = max_dbl = 0
            for key in sound_levels.keys():
                if input_dbl <= key:
                    max_dbl = key
                if input_dbl >= key and key > min_dbl:
                    min_dbl = key
            if max_dbl and min_dbl:
                print('A sound level of %d dB is comparable to a sound louder than %s, but less than that of %s.' %
                      (input_dbl, sound_levels[min_dbl], sound_levels[max_dbl]))
                break 
            elif max_dbl and not min_dbl:
                print('A sound level of %d dB is comparable to a sound less than that of %s.' %
                      (input_dbl, sound_levels[max_dbl]))
                break
            elif min_dbl and not max_dbl:
                print('A sound level of %d dB is comparable to a sound louder than %s.' %
                      (input_dbl, sound_levels[min_dbl]))
                break
    except ValueError:
        print('Invalid input.')
        continue