admission_toddler = 0
admission_kids = 14
admission_adult = 23
admission_senior = 18

def calculateTotalAdmission(L):
    total = 0
    for x in L:
        if 0 <= x < 3:
            total += admission_toddler
        elif 3 <= x < 13:
            total += admission_kids
        elif 13 <= x < 65:
            total += admission_adult
        else:
            total += admission_senior
    return total

guest_list = []
while True:
    try:
        input_age = input('Enter guest age: ')
        if input_age:
            guest_list.append(int(input_age))
        else:
            print('Total admission: $%.2f' % calculateTotalAdmission(guest_list))
            break
    except ValueError:
        print('Invalid input. Please enter a valid age.')