def find_closest(val1, val2, target):
    return val2 if target - val1 >= val2 - target else val1

def get_closest_value(arr, target):
    n = len(arr)
    left = 0
    right = n - 1
    mid = 0

    # edge case - last or above all
    if target >= arr[n - 1]:
        return arr[n - 1]
    # edge case - first or below all
    if target <= arr[0]:
        return arr[0]
    # BSearch solution: Time & Space: Log(N)

    while left < right:
        mid = (left + right) // 2  # find the mid
        if target < arr[mid]:
            right = mid
        elif target > arr[mid]:
            left = mid + 1
        else:
            return arr[mid]

    if target < arr[mid]:
        return find_closest(arr[mid - 1], arr[mid], target)
    else:
        return find_closest(arr[mid], arr[mid + 1], target)

case = 0
while True:
    try:
        # nums
        sums = []
        nums = []
        for i in range(int(input())):
            n = int(input())
            for j in range(len(nums)):
                sums.append(n + nums[j])
            nums.append(n) 
        sums.sort()
        case += 1
        print("Case {}:".format(case))
        # test cases
        for i in range(int(input())):
            s = int(input())

            # find the closest
            #j = 0
            #while (j < len(sums) - 1 and sums[j + 1] <= s):
            #    j += 1
            print("Closest sum to {} is {}.".format(s, get_closest_value(sums, s)))
    except EOFError:
        break
