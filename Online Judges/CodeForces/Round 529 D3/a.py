input()
n = 1
s = list(input().strip())
while len(s) > 0:
    print(s[0], end="")
    for i in range(n):
        s.pop(0)
    n += 1
print("")