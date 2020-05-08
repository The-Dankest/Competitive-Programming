import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
l, w, h, angle = viread()
print(round(((l * h) - ((l * l * math.tan(math.pi * 2 / 360 * angle)) / 2)) * w, 3))
