import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [_ for _ in input().strip().split()]


# code goes here
n = read()
answ = 1
for c in n:
    answ *= int(c)
ans = [answ]
for i in range(len(n) - 1):
    answ = 1
    new = str(int(n[:i + 1]) - 1)
    new += "9" * (len(n) - i - 1)
    new = str(int(new))
    for c in new:
        answ *= int(c)
    ans.append(answ)
print(max(ans))