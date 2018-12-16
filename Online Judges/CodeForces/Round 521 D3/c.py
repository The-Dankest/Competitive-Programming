from math import floor, ceil
n = int(input())
nums = [int(x) for x in input().split()]
sums = sum(nums)
ans_nums = 0
ans_list = []
for i in range(n):
    check = (sums - nums[i]) / 2
    if floor(check) == ceil(check) and check in nums:
        ans_nums += 1
        ans_list.append(str(i + 1))
print(ans_nums)
print(" ".join(ans_list))