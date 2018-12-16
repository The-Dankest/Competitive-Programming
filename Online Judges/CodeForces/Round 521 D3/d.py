n, k = [int(x) for x in input().split()]
nums = sorted([int(x) for x in input().split()])
set_nums = set(nums)
counts = {}
for num in set_nums:
    counts[num] = nums.count(num)

