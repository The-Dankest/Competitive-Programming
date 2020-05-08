import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
n = iread()
nums = viread()
count = nums[len(nums) - 1]
last = count
for i in range(len(nums) - 2, -1, -1):
    if nums[i] < last:
        count += nums[i]
        last = nums[i]
    elif last > 1:
        count += last - 1
        last -= 1
print(count)