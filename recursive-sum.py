# given a list of integers, return the sum of all the elements in the list

def sum_recursive(L):
    if not L:
        return 0
    else:
        return int(L[0]) + sum_recursive(L[1:])
    
def sum_nonrecursive(L):
    total = 0
    for x in L: total += x
    return total

while True:
    try:
        list_input = input('Enter a list of integers, seperated by commas: ')
        print('The sum of the integers is %d.' %
               sum_recursive([int(x) for x in list_input.split(',')]))
        break
    except ValueError:
        print('Invalid input.')