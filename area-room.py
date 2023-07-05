# area-room.py
# Compute and display the area of a room based on the width and lengnth
# provided by the user.

width = float(input('What is the width of the room in meters? '))
length = float(input('What is the length of the room in meters? '))
area = width * length
print("The area of the room is %.2f square ." % area)
