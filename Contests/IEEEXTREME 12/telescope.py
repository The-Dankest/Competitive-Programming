stars = []
n = int(input())
for i in range(n):
    s, e, d = [int(x) for x in input().split()]
    stars.append([d, s, e, [], 0])

for i in range(n):
    for j in range(i + 1, n):
        if (i != j):
            if (((stars[j][1] > stars[i][1] and stars[j][1] < stars[i][2]) or (stars[j][2] > stars[i][1] and stars[j][2] < stars[i][2])) or ((stars[i][1] > stars[j][1] and stars[i][1] < stars[j][2]) or (stars[i][2] > stars[j][1] and stars[i][2] < stars[j][2]))):
                stars[i][3] += [j]
                stars[j][3] += [i]
            else:
                stars[i][4] += stars[j][0]
                stars[j][4] += stars[i][0]

total = 0
for i in range(n):
    for s in stars[i][3]:
        if (stars[s][4] > stars[i][4]):
            stars[i][0] = 0
            break
        elif (stars[i][4] > stars[s][4]):
            stars[s][0] = 0
            pass
    total += stars[i][0]
print(total)