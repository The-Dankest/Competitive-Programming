n = int(input())
lights = [int(x) for x in input().split()]
ans = 0
for i in range(1, n - 1):
    if lights[i - 1] == 1 and lights[i] == 0 and lights[i + 1] == 1:
        ans += 1
        lights[i + 1] = 0
print(ans)