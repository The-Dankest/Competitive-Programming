import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
for i in range(iread()):
    b, p, f = viread()
    h, c = viread()
    b = b // 2
    if (h > c):
        count1 = min(b, p)
        count2 = min(b - count1, f)
        print(str(int(count1 * h + count2 * c)))
    else:
        count1 = min(b, f)
        count2 = min(b - count1, p)
        print(str(int(count1 * c + count2 * h)))

