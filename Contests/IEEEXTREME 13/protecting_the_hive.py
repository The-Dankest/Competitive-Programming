import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def round(n): return int(n + 0.5)
    
# code goes here
n, m = viread()
comb = []
for i in range(n):
    comb.append(viread())
for i in range(iread()):
    q, y, x = read().split()
    x, y = int(x), int(y)
    if q == "a":
        comb[y - 1][x - 1] = 1
    else:
        print(comb[y - 1][x - 1])
print(*comb, sep="\n")
