import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
n = iread()
nums = sorted(viread())
for i in range(len(nums)):
    nums[i] = nums[-1] - nums[i]
nums = set(nums) - {0}
if len(nums) == 0:
    print(0)
elif len(nums) == 1:
    if min(nums) % 2 == 0:
        print(min(nums) // 2)
    else:
        print(min(nums))
elif len(nums) == 2:
    if min(nums) * 2 == max(nums):
        print(min(nums))
    else:
        print(-1)
else:
    print(-1)