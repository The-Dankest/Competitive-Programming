for i in range(int(input())):
    x, y = [int(j) for j in input().split()]
    offset = 0
    for j in range(x):
        offset += 1
        if offset == y:
            offset = 0
        print(chr(ord("a") + offset), end = "")
    print("")