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

n = iread()
l = []
for i in range(n):
    heapq.heappush(l, iread())

ans = 0
while (n > 1):
    n -= 1
    a, b = heapq.heappop(l), heapq.heappop(l)
    ans += a + b
    heapq.heappush(l, a + b)

print(ans)