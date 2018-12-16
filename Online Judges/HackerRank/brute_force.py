nums = [int(bin(x + 1)[2:]) * 9 for x in range(999999)]
ans = []
for i in range(500):
    j = 0
    while (nums[j] % (i + 1) != 0):
        j += 1
    ans.append(nums[j])
print(ans)