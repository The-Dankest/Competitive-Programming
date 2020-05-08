n = int(input())
grid = []
for i in range(n):
    grid.append(list(input()))
count = 0
for i in range(1, n - 1):
    for j in range(1, n - 1):
        if (grid[i][j] == grid[i + 1][j + 1] == grid[i + 1][j - 1] == grid[i - 1][j + 1] == grid[i - 1][j - 1] == "X"):
            count += 1
print(count)