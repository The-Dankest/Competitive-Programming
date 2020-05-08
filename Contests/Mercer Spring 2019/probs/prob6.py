# BJU Bitwise Blitz
# prob6.py

import math, re, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
for i in range(iread()):
    n = iread()
    l = sorted(viread())
    a = l[0]
    b = l[1]
    z = l[-1]
    y = l[-2]
    print((z - a) - (n - 2) - min(b - a, z - y))
