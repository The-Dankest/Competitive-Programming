n, b = [int(x) for x in input().strip().split()]

print(n)

digits = []
if n == 0:
    digits.append(0)
else:
    while n != 0:
        digits.append(int(n % b))
        n //= b

count = 0
while(count < len(digits) and digits[count] == 0):
    count += 1

print(count)