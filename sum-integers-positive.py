# Read a positive integer from the user
# and display the sum of all the integers from 1 to n

def sumIntegers(integer):
    return int(((integer * (integer + 1)) / 2))

integer_input = int(input('Enter a positive integer: '))

print(str(sumIntegers(integer_input)) + ' is the sum of all integers from 1 to ' + str(integer_input) + '.')
