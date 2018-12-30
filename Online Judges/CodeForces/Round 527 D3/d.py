n = int(input())
wall = [int(x) for x in input().split()]
_max = max(wall)
num_left = n - wall.count(_max)
change = True
while change:
    change = False
    for i in range(n - 1):
        if wall[i] == wall[i + 1]:
            if wall[i] < _max and wall[i + 1] < _max:
                change = True
                wall[i] += 1
                wall[i + 1] += 1
                num_left -= 1 if wall[i] == _max else 0
                num_left -= 1 if wall[i + 1] == _max else 0
        elif wall[i] < _max - 1:
            change = True
            wall[i] += 2
            num_left -= 1 if wall[i] == _max else 0
    if wall[-1] < _max - 1:
        change = True
        wall[-1] += 2
        num_left -= 1 if wall[-1] == _max else 0
    
if num_left == 0:
    print("YES")
else:
    print("NO")

                