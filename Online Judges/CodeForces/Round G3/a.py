import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
a, b, c = viread()
ans = (2 * c) + (2 * min(a, b)) + (1 if a != b else 0)
print(ans)