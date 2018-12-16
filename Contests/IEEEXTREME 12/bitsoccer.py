n = int(input())
players = sorted([int(x) for x in input().split()])
for i in range(int(input())):
    query = int(input())
    p = []
    for player in players:
        if (player > query):
            break
        if ((player & query) == player):
            p.append(player)
    x = 0   
    for y in p:
        if x == 0:
            x = y
            pass
        x = x | y
    if (x == query):
        print("YES")
    else:
        print("NO")