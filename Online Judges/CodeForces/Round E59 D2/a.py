import re, math, decimal, bisect, collections
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

for i in range(iread()):
    n = iread()
    s = read()
    if n == 2:
        if s[0] < s[1]:
            print("YES")
            print("2")
            print("{} {}".format(s[0], s[1]))
        else:
            print("NO")
    else:
        print("YES")
        print("2")
        print("{} {}".format(s[0], s[1:]))