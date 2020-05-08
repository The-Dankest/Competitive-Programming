import re, math, decimal, bisect, random
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def round(n): return int(n + 0.5)

DEBUG = 1
# DEBUG = 0
def debug(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)
    
    
def gcd(a, b): return a if b == 0 else gcd(b, a % b)

# code goes here
n, k = viread()
nums = set(viread())
gcds = set()
for i in nums:
    for j in nums:
        gcds.add(gcd(i, j))
print(len(gcds))