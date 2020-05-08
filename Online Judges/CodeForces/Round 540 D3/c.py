import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
n = iread()
counts = {}
for num in viread():
    num = int(num)
    if num not in counts.keys():
        counts[num] = 1
    else:
        counts[num] += 1

even = n % 2 == 0
found_odd = False
good = True

grid = [[0 for y in range((n + 1) // 2)] for x in range((n + 1) // 2)]

for k in counts.keys():
    if counts[k] % 4 == 0:
        pass
    elif counts[k] % 4 == 1:
        if even or found_odd:
            good = False
            break
        else:
            found_odd = True
            grid[n // 2][n // 2] = k
    else:
        good = False
        break


if good:
    print("YES")
    for x in range(n):
        for y in range(n):
            print("{} ".format(grid[x][y]), end="")
        print("")
else:
    print("NO")
