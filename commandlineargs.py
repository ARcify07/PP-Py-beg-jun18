""" This module has a function that returns sum of two numbers"""
import sys
a, b = sys.argv[1], sys.argv[2]
def sum(a,b):
    print(int(a) + int(b))
    return int(a) + int(b)

print(__doc__)
print(__name__)

if __name__ == '__main__':
    sum(a,b)
