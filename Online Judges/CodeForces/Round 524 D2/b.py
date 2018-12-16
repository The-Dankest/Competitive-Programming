for i in range(int(input())):
    begin, end = [int(x) for x in input().split()]
    begin -= 1
    sum_begin = 0
    sum_end = 0
    if begin % 2 == 0:
        sum_begin = begin // 2
    else:
        sum_begin = ((begin + 1) // 2) * -1
    if end % 2 == 0:
        sum_end = end // 2
    else:
        sum_end = ((end + 1) // 2) * -1  
    print(sum_end - sum_begin)
