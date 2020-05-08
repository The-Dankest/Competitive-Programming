for i in range(int(input())):
    n = int(input())
    d = {}
    for i in range(21):
        d[i] = []
    colors = [int(x) for x in input().split()]
    for i in range(n):
        d[colors[i]].append(i)
    b1 = 0 
    b2 = 0
    ans = 0
    for i in range(n):
        d[colors[i]].pop(0)
        if colors[i] == b1 or colors[i] == b2:
            pass
        else:
            ans += 1
            if d[b1] == []:
                b1 = colors[i]
            elif d[b2] == []:
                b2 = colors[i]
            elif d[b2][0] < d[b1][0]:
                b1 = colors[i]
            else:
                b2 = colors[i]
    print(ans)