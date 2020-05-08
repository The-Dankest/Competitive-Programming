import re, math, decimal, bisect, collections
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

for i in range(iread()):
    a, b, c, d = viread()
    if (a != c):
        print(a, c)
    elif (a != d):
        print(a, d)
    elif (b != c):
        print(b, c)
    else:
        print(b, d)