def print_multiplication_page(start: int, end:int) -> None:
    # print column headers
    print(' ' * 4, end='')
    for j in range(start, end + 1):
        print('%4d' % j, end='')
    print()
    # print row header and contents
    for i in range(start, end + 1):
        # row number
        print('%4d' % i, end='')
        for j in range(start, end + 1):
            print('%4d' % (int(i * j)), end='')
        print()