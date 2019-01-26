n, m = [int(x) for x in input().split()]
nums = sorted([int(x) for x in input().split()])
if n == 1:
    print(1)
else:
    ans = False
    for i in range(n - 1):
        if nums[i] + nums[i + 1] > m:
            ans = True
            print(i + 1)
            break
    if not ans:
        print(n)