import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
for i in range(iread()):
    n = iread()
    s = read()
    print(min(max(s.find(">"), 0), max(s[::-1].find("<"), 0)))
