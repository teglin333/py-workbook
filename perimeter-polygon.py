import math

def computePerimenter(L):
    if len(L) > 1:
        perimeter = 0
        for x in L:
            perimeter += math.sqrt(x[0] ** 2 + x[1] ** 2)
        return perimeter
    else:
        return 0

def getUserPoint():
    try:
        return [int(x) for x in input('Enter a point (x,y): ').split(',')]
    except:
        return 0
    
while True:
    try:
        polygon_vertices = []
        while True:
            point = getUserPoint()
            if point == 0:
                break
            polygon_vertices.append(point)
        print('The perimeter of the polygon is: %.2f' % 
                computePerimenter(polygon_vertices))
        break
    except ValueError:
        print('Invalid input.')