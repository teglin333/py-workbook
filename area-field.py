# read the length and width of a farmer's field in feet from the user
# and display the area of the field in acres.

acre_area = 43560

length = float(input('Enter the length of your field in feet: '))
width = float(input('Enter the width of your field in feet: '))
area = (length * width) / acre_area

print('The area of your field in acres is %.2f.' % area)