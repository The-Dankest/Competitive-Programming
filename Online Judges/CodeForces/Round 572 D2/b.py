import re, math, decimal, bisect
from collections import deque
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
n = iread()
nums = sorted(viread())
ans = deque()
front = True
while len(nums) != 0:
    x = nums.pop()
    if front:
        ans.append(x)
    else:
        ans.appendleft(x)
    front = not front
good = True
for i in range(n - 2):
    if (ans[i] + ans[i + 2] <= ans[i + 1]):
        good = False
if (ans[0] >= ans[1] + ans[n - 1] or ans[n - 1] >= ans[0] + ans[n - 2]):
    good = False
if good:
    print("YES")
    print(*ans)
else:
    print("NO")