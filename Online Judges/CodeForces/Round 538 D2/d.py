n = int(input())
l = [int(x) for x in input().split()]
count = 0
found = []
for i in range(len(l) - 1):
    found.append(l[i])
    if l[i] != l[i + 1] and l[i + 1] not in found:
        count += 1

print(count)