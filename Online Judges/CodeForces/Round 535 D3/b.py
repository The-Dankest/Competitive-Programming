import re, math, decimal, bisect, collections
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

iread()
nums = sorted(viread())
x = nums[-1]
found = []
for y in nums[::-1]:
    if x % y != 0 or y in found:
        print(x, y)
        break
    else:
        found.append(y)