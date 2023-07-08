black_squares = ['a', 'c', 'e', 'g']
white_squares = ['b', 'd', 'f', 'h']

def isWhite(row, column):
    return True if row % 2 and (column in white_squares) else False

while True:
    try:
        user_square = input('Enter a position: ')
        position = {'column': user_square[0].lower(),
                    'row'   : int(user_square[1])}
        if position['column'] in black_squares + white_squares and \
        0 < position['row'] < 9:
            print('The square is %s.' % 
                  ('white' if isWhite(**position) else 'black'))
            break
        else:
            raise ValueError()
    except ValueError:
        print('Invalid input. You specify a position (e.g. a4).')