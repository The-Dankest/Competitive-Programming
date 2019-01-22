import math

def ncr(n, r):
    nr = math.factorial(n - r)
    n = math.factorial(n)
    r = math.factorial(r)
    return n // (r * nr)

for i in range(int(input())):
    c = {}
    for j in range(int(input())):
        x, y = input().split()
        c[y] = c[y] + 1 if y in c.keys() else 2
    total = 1
    for k in c.keys():
        total *= ncr(c[k], 1)
    print(total - 1)