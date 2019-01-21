for i in range(int(input())):
    x = []
    for j in input().split(" "):
        x.append(int(j))
    print("Case {}: {}".format(i + 1, max(x)))
