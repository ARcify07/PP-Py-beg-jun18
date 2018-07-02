""" This module can be used to find circumeference, area of a circle """
import math
pi = math.pi

def circumference(radius):
    return 2*pi*radius

def area(radius):
    return pi*(radius)**2

def sphereArea(radius):
    return 4*area(radius)

if __name__ == '__main__':
    import sys
    action, radius = sys.argv[1] , int(sys.argv[2])
    if action == 'area':
        print(area(radius))
    elif action == 'circumference':
        print(circumference(radius))
    else:
        print(sphereAres(radius))

