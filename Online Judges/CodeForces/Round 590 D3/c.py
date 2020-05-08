import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
for i in range(iread()):
    n = iread()
    upper = read()
    lower = read()
    up = True
    col = 0
    while col < n:
        if up:
            if upper[col] == "1" or upper[col] == "2":
                col += 1
            elif lower[col] != "1" and lower[col] != "2":
                up = False
                col += 1
            else:
                break
        else:
            if lower[col] == "1" or lower[col] == "2":
                col += 1
            elif upper[col] != "1" and upper[col] != "2":
                up = True
                col += 1
            else:
                break

    if col == n and up == False:
        print("YES")
    else:
        print("NO")

