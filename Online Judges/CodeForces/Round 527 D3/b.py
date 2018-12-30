input()
peeps = sorted([int(x) for x in input().split()])
count = 0
for i in range(len(peeps) // 2):
    count += peeps[2 * i + 1] - peeps[2 * i]
print(count)