import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def round(n): return int(n + 0.5)

DEBUG = 1
# DEBUG = 0
def debug(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)
    
# code goes here
a, b = viread()
ans = min(a // 3, b // 3) * 2
a = a % 3
b = b % 3
if (a == 2 and b > 0) or (b == 2 and a > 0):
        ans += 1
print(ans)
s