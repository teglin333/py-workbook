def flatten(L):
    items = list(L)
    while items:
        front = items.pop(0)
        items[:0] = front if isinstance(front, list) else [front]
    return items

while True:
    input_all = []
    try:
        while True:
            input_list = input('Enter an integer or comma-delimited list of integers: ')
            if not input_list:
                break
            input_all.extend([int(x) for x in input_list.split(',')])
        print('The sorted list of integers is:', end=' ')
        for x in sorted(flatten(input_all)):
            print(x, end=' ')
        break
    except ValueError:
        print('Invalid input.')
        continue