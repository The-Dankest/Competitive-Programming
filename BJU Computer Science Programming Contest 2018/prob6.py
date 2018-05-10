n = int(input())
while (True):
    names = input().strip().split(" ")
    profits = {}
    for name in names:
        profits[name] = 0
    for i in range(n):
        givings = input().split()
        if (int(givings[2]) != 0):
            profits[givings[0]] -= (((int(givings[1])) // int(givings[2])) * int(givings[2]))
            if (len(givings) > 3):
                for name in givings[3:]:
                    profits[name] += int(givings[1]) // int(givings[2])
    for name in names:
        print("{0} {1}".format(name, profits[name]))
    n = int(input())
    if (n != 0):
        print("")
    else:
        break