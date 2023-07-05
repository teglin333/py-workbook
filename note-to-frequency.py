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

while True:
    try:
        input_string = input('Enter a note (A-G) and octave (0-8): ').upper()
        note = input_string[0]; octave = int(input_string[1])
        if (len(input_string) == 2 and note in middle_note_frequencies.keys()):
            if (octave >= min_octave and octave <= max_octave):
                print('The note %s has a frequency of %.2f.' % 
                      (input_string, getFrequency(note, octave)))
                break
    except ValueError:
        pass
    print('Invalid input.')
    continue