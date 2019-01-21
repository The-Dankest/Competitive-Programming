while (True):
    try:
        nums = input().split()
        nums[0] = int(nums[0])
        nums[1] = int(nums[1])
        ans = 2 * nums[0] * nums[1]
        print(ans)
    except EOFError:
        break