for i in range(int(input().strip())):
    v, e = [int(x) for x in input().strip().split()]
    adj = [[] for x in range(v)]
    found = [False for x in range(v)]
    colors = [0 for x in range(v)]
    for j in range(e):
        x, y = [int(x) for x in input().strip().split()]
        adj[x].append(y)
        adj[y].append(x)
    ans = 0
    start = 1
    while (found.count(False)):
        n = found.index(False)
        found[n] = True
        start += 2
        colors[n] = start
        queue = [n]
        while (queue and ans != -1):
            top = queue.pop(0)
            for v in adj[top]:
                if colors[v] == colors[top]:
                    ans = -1
                    break
                elif colors[v] == 0:
                    colors[v] = start + (colors[top] % 2)
                    queue.append(v)
                    found[v] = True
        if ans != -1:
            ans += max(1, min(colors.count(start), colors.count(start + 1)))
    print(ans)
