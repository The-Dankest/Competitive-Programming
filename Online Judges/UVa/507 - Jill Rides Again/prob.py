for i in range(int(input().strip())):
    j  = int(input().strip()):
    ride = [int(input().strip()) for x in range(j)]

    max_sum = -1
    begin = 0
    end = 0
    new_begin = 0
    new_end = 0

    running_sum = 0
    for k in range(j):
        running_sum += ride[k]
        if running_sum > max_sum
        if running_sum < 0:
            running_sum = 0
            


    if max_sum >= 0:
        print("The nicest part of route {} is between stops {} and {}".format(i + 1, begin, end))
    else:
        print("Route {} has no nice parts".format(i + 1))