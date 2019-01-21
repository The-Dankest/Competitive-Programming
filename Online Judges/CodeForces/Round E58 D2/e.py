min_x = 0
min_y = 0
ans = ""
for i in range(int(input())):
    q, _x, _y = input().split()
    _x = int(_x)
    _y = int(_y)
    x = min(_x, _y)
    y = max(_x, _y)
    if q == "+":
        min_x = max(x, min_x)
        min_y = max(y, min_y)
    else:
        if (x >= min_x and y >= min_y):
            ans += "YES\n"
        else:
            ans += "NO\n"
print(ans, end="") 