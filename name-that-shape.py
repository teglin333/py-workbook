shape_names =  {3:  ['three', 'triangle'],
                4:  ['four',  'quadrilateral'],
                5:  ['five',  'pentagon'],
                6:  ['six',   'hexagon'],
                7:  ['seven', 'heptagon'],
                8:  ['eight', 'octagon'],
                9:  ['nine',  'nonagon'],
                10: ['ten',   'decagon']}
while True:
    input_sides = int(input('Enter the number of sides of a 2D shape: '))
    if (input_sides >= 3) and (input_sides <= 10):
        print('A shape with %s sides is a %s.' % (shape_names[input_sides][0], 
              shape_names[input_sides][1]))
        break
    else:
        print('Invalid input.')
        continue


