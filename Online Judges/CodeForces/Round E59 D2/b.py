import re, math, decimal, bisect, collections
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

for i in range(iread()):
    k, x = viread()
    print(9 * (k - 1) + x)
