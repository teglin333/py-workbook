min_frequency = 16.35
max_frequency = 7902.08

min_octave = 0
max_octave = 8

middle_note_frequencies = {
    'C' : 261.63,
    'D' : 293.66,
    'E' : 329.63,
    'F' : 349.23,
    'G' : 392.00,
    'A' : 440.00,
    'B' : 493.88
}

def getFrequency(note, octave):
    middle_frequency = middle_note_frequencies[note]
    return middle_frequency / (2 ** (4 - octave))

def getNote(frequency):
    # determine the lowest octave
    floor_c = min_octave
    for i in range(min_octave, max_octave):
        floor_frequency = getFrequency('B', i)
        if (floor_frequency <= frequency): 
            floor_c += 1
        else:
            break
        
    # start iterating at the lowest octave
    for j in range(floor_c, max_octave + 1):
        # for each note in the octave
        for x in middle_note_frequencies.keys():
            # is the user frequence close to the note frequency?
            if abs(getFrequency(x, j) - frequency) <= 1:
                return (x + str(j))
    return None

while True:
    try:
        input_frequency = float(input('Enter a frequency (Hz): '))
        if min_frequency <= input_frequency <= max_frequency:
            note = getNote(input_frequency)
            if note:
                print('The frequency %.2f Hz corresponds to the note %s.' %
                    (input_frequency, note))
            else:
                print('The frequency %.2f Hz does not correspond to any note.' %
                      input_frequency)
            break
        else:
            print('You must specify a frequency between %.2f' % min_frequency,
                  'and %.2f Hz.' % max_frequency)
            continue
    except ValueError:
        pass
    print('Invalid input.')