import re, math, decimal, bisect, heapq
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def round(n): return int(n + 0.5)

DEBUG = 1
# DEBUG = 0
def debug(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)
    
# code goes here
n, p = viread()
ph = 0
for i in range(n):
    ph += iread()
print(math.ceil(p/ph))
