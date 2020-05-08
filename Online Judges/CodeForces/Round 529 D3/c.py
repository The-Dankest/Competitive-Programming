n, k = [int(x) for x in input().split()]
b = bin(n)[2:][::-1]
if (b.count("1") > k or k > n):
    print("NO")
else:
    nums = []
    ans = ""
    for i in range(len(b)):
        if (b[i] == "1"):
            nums.append(2 ** i)
    _k = 0
    while _k + len(nums) < k:
        num = nums.pop()
        if num == 1:
            ans += "1 "
            _k += 1
        else:
            num = num // 2
            nums.append(num)
            nums.append(num)
    for n in nums:
        ans += str(n) + " "
    print("YES")
    print(ans[:len(ans)-1])