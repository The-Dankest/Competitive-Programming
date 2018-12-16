for i in range(int(input())):
    r, c = [int(x) for x in input().split()]
    sums = []
    diverse = True
    for j in range(r):
        _sum = sum([int(x) for x in input().split()])
        if _sum in sums:
            diverse = False
        sums.append(_sum)
    print("yes") if diverse else print("no")
    