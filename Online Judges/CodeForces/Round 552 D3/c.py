import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
a, b, c = viread()

weeks = min(min(a // 3, b // 2), c)
a, b, c = a - (3 * weeks), b - (2 * weeks), c - weeks

print((weeks * 7) + )