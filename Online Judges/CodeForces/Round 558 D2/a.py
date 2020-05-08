import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
a, b = viread()
if b == 0:
    print(1)
    exit()
if a < 2 * b:
    print(a - b)
else:
    print(b)
