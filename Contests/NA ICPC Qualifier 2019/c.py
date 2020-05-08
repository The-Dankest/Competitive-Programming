import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def round(n): return int(n + 0.5)
    
# code goes here
n, d = viread()
districts = {}
votes = 0
wasted_a = 0
wasted_b = 0
for i in range(n):
    c, a, b = viread()
    if c not in districts:
        districts[c] = [a, b]
    else:
        a2, b2 = districts[c]
        districts[c] = [a + a2, b + b2]

for i in sorted(districts.keys()):
    a, b = districts[i]
    votes += a + b
    w_a = a - ((a + b) // 2) - 1
    w_b = b - ((a + b) // 2) - 1
    if a < b:
        w_a = a
        print(f"B {w_a} {w_b}")
    else:
        w_b = b
        print(f"A {w_a} {w_b}")
    wasted_a += w_a
    wasted_b += w_b
print(f"{(round((abs(wasted_b - wasted_a) / votes) * (10 ** 10)) / (10 ** 10)):.10f}")

