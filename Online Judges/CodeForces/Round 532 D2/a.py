a, steps = [int(x) for x in input().split()]
tabs = [int(x) for x in input().split()]

_sum = -1 * a
__sum = sum(tabs)
for i in range(steps):
    arr = tabs[i::steps]
    _sum = max(abs(__sum - sum(arr)), _sum)
print(_sum)

