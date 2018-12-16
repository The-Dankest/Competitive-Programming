b = []
a = []
for c in input():
    a_total = 0
    b_total = 0
    if c == "B":
        a_total += 1
        b_total -= 1
    else:
        a_total -= 1
        b_total += 1
    b.append(b_total)
    a.append(a_total)
a_max = 0
b_max = 0
a_range = [0, 0]
b_range = [0, 0]
a_start = 0
b_start = 0
a_sum = 0
b_sum = 0
for i in range(len(a)):
    a_sum += a[i]
    b_sum += b[i]
    if (a_sum > a_max):
        a_range = [a_start, i]
        a_max = a_sum
    if (a_sum < 0):
        a_sum = 0
        a_start = i + 1
    if (b_sum > b_max):
        b_range = [b_start, i]
        b_max = b_sum
    if (b_sum < 0):
        b_sum = 0
        b_start = i + 1

if (a_max > b_max or (a_max == b_max and a_range[0] <= b_range[0] and a_range[1] < b_range[1])):
    print(a_range[0] + 1, a_range[1] + 1)
else:
    print(b_range[0] + 1, b_range[1] + 1)
