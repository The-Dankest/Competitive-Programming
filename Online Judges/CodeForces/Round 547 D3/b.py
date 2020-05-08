import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
n = iread()
nums = viread()
counts = [0]
for i in nums:
    if i == 1:
        counts[-1] += 1
    else:
        counts.append(0)
print(max(max(counts), counts[0] + counts[-1]))