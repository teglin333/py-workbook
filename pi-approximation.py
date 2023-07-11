def approximatePi(i):
    if i > 0:
        series_sum = 3
        while i:
            series_sum += (-1)**(i-1) * 4 / ((2*i)*(2*i+1)*(2*i+2))
            i -= 1
        return series_sum
    else:
        return -1

while True:
    try:
        terms = int(input('Enter the number of approximations of pi: '))
        if terms > 0:  
            print('Approximating pi using %d terms:' % terms)
            #n = 1
            #while n <= terms:
            print('%s' % approximatePi(terms))
            #    n += 1
            break
        else:
            raise ValueError('You must enter an integer > 0.')
    except ValueError:
        print('Invalid input.')