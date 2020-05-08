import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
n, b, a = viread()
path = viread()

max_a = a
ans = 0
while (a > 0 or b > 0):
    if (n == ans):
        break
    if path[ans] == 1:
        if a == max_a:
            a -= 1
        elif b > 0:
            b -= 1
            if a < max_a:
                a += 1
        else:
            a -= 1
    else:
        if a > 0:
            a -= 1
        else:
            b -= 1
    ans += 1
print(ans)
