import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
n = iread()
pages = viread()
days = 0
i = 0
while (i < len(pages)):
    days += 1
    goto = pages[i] - 1
    while (i < goto):
        i += 1
        if (i >= len(pages)):
            break
        goto = max(pages[i] - 1, goto)
    i += 1
print(days)
