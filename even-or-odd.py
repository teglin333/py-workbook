input = int(input(('Enter an integer: ')))

print('The number %d is %s.' % (
    input, 'even' if not bool(input % 2) else 'odd'))