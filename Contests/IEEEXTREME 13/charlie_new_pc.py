import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def round(n): return int(n + 0.5)
    
ans = []
correct = False
def recurse_from(b, c, parts):
    my_parts = parts[:]
    global ans, correct
    if c > b or correct == True:
        return 0
    elif c == b:
        correct = True
    elif len(my_parts) == 0:
        ans.append(c)
    else:
        for part in my_parts.pop(0):
            recurse_from(b, c + part, my_parts)


# code goes here
for i in range(iread()):
    ans = []
    correct = False
    b = iread()
    n = iread()
    parts = []
    _ = read()
    for j in range(n):
        parts.append(viread())
    recurse_from(b, 0, parts)
    print(b if correct else max(ans))
    
