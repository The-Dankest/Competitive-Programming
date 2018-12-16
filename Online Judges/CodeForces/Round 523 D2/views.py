w, h = [int(x) for x in input().split()]
num_top = 0
num_side = 0
total = 0
for stack in [int(x) for x in input().split()]:
    total += stack
    if stack > 1:
        num_top += 1
    num_side = max(num_side, stack)
ans = total - max(num_side, num_top)
if 
print(ans)

