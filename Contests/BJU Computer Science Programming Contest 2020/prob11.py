import re, math, decimal, bisect
from collections import deque
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def round(n): return int(n + 0.5)

n = iread()
for i in range(n):
    sx, sy, dx, dy = viread()

    md = abs(sx - dx) + abs(sy - dy)

    if md % 2:
        print("KNIGHT")
    elif md % 3:
        print("KNIGHT")
    elif md % 4:
        
        