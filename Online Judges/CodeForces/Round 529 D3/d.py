n = int(input())
nexts = []
for i in range(n):
    nexts.append([int(x) for x in input().split()])
visited = 0
cur_visited = nexts[0][0]
ans = [cur_visited, nexts[0][1]]
while (visited < n):
    if ans[visited + 1] in nexts[cur_visited]
    visited += 1
print(" ".join([str(x) for x in ans]))