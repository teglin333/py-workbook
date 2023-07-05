def computeSumDigits(input_string):
    sum = 0
    for x in input_string:
        sum += int(x)
    return sum

print('The sum of the digts is: %d' % 
      computeSumDigits(input('Enter an integer value: ').strip()))