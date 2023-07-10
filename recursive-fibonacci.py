cache = {0: 0, 1: 1}

def fibonacci_number(term):
    if term in cache:
        return cache[term]
    cache[term] = fibonacci_number(term - 1) + fibonacci_number(term - 2)
    return cache[term]
    
while True:
    try:
        input = int(input('Enter n to calcuate the nth Fibonacci number, F(n): '))
        print('For n = %d, F(n) is %d' % (input, fibonacci_number(input)))
        break
    except ValueError:
        print('Invalid input.')
        continue