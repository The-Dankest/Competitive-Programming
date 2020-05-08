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
stack = []
for i in range(iread()):
    cmd = read()
    if cmd == "undo":
        stack.pop()
    else:
        stack.append(int(cmd))
ans = set()
total = sum(stack)
for x in stack:
    ans.add(total - x)
print(len(ans))
print(*sorted(ans))
