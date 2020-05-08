import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here

for i in range(iread()):
    n = iread()
    cost = sum(viread())
    print(math.ceil(cost / n))
