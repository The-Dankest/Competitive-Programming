n = int(input())
output = []
count = 0
_sum = 0
for i in range(n):
    count += 1
    output.append("{0} {1}".format((n - count + 1) * count, input()))
    _sum += (n - count + 1) * count

print(_sum)
for line in output:
    print(line)