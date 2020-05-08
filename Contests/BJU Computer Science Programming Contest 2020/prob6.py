import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def round(n): return int(n + 0.5)

DEBUG = 1
# DEBUG = 0
def debug(*args, **kwargs):
    if DEBUG: print(*args, **kwargs)
    
def can_merge(a, b):
    return True if (a[0] >= b[0] and a[0] <= b[1]) or (a[1] >= b[0] and a[1] <= b[1]) else False 

# code goes here
ins = []
start = 10000000000
end = 0
n = iread()
for i in range(n):
    a, b = viread()
    x, y = a - b, a + b
    ins.append((x, y))
ins.sort() #(key=lambda a: (a[0], -a[1]))
ans = n
last = ins[0]
for i in ins[1:]:
    if can_merge(i, last):
        ans -= 1
    last = i

print(ans)
