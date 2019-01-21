for i in range(int(input())):
    l1 = {}
    l2 = {}
    ans = []
    ans_found = True
    for j in range(int(input())):
        a, b = [int(x) for x in input().split()]
        if (a not in l2.keys() and b not in l2.keys()):
            l1[a] = True
            l1[b] = True
            ans.append("1")
        elif (a not in l1.keys() and b not in l1.keys()):
            l2[a] = True
            l2[b] = True
            ans.append("2")
        else:
            ans_found = False
    if ans_found:
        print("".join(ans))
    else:
        print(-1)



