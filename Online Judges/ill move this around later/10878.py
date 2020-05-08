import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
end = read()
n = read()
while (n != end):
    c = read()
    x = c[2:6] + c[8:-1]
    print(x)
    x = x.replace(" ", "0")
    x = x.replace("o", "1")
    x = int(x, 2)
    print(chr(x), end="")
    n = read()