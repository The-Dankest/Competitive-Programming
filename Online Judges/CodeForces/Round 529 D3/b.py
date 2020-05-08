n = int(input())
nums = sorted([int(x) for x in input().split()])
if n == 2:
    print(0)
else:
    print(min(nums[-1] - nums[1], nums[-2] - nums[0]))
