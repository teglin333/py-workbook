# Calculate and display the difference between two points following the surface
# of the earth, in kilometers.

import math

avg_radius = 6371.01

def compute_distance(a, b):
    return avg_radius * math.acos(
        math.sin(math.radians(a[0])) * math.sin(math.radians(b[0])) +
        math.cos(math.radians(a[0])) * math.cos(math.radians(b[0])) *
        math.cos(math.radians(a[1]) - math.radians(b[1])))

point_a = [float(input('Point A latitude (degrees): ')),
           float(input('Point A longitude (degrees): '))]
point_b = [float(input('Point B latitude (degrees): ')),
           float(input('Point B longitude (degrees): '))]

print('The distance between %.2f N %.2f W' % (point_a[0], point_a[1]), 
      'and %.2f N %.2f W is %.2f kilometers.' % 
      (point_b[0], point_b[1], compute_distance(point_a, point_b)))