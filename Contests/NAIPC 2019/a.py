import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def vdread(): return [float(_) for _ in input().strip().split()]
def vsread(): return input().strip().split()

# code goes here

def area(p):
    result = 0
    for i in range(len(p) - 1):
        x1, y1 = p[i]
        x2, y2 = p[i + 1]
        result += (x1 * y2 - x2 * y1)
    return abs(result) / 2

n, k = viread()
points = []
for i in range(n):
    points.append(vdread())

print(area(points))
