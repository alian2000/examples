# Python program to find Area of a circle
# using inbuild library

import math
def area(r):
    area = math.pi* pow(r,2)
    return print('Area of circle is:' ,area)
def rectangle_area(base, height):
    area = base*height
    print("The rectangular area is " + str(area))


area(4)
area(19)
area(55)
rectangle_area(5,6)
rectangle_area(10,10)
