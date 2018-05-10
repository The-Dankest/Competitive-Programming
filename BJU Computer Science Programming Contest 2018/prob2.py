n, k = input().split()
n = int(n)
k = int(k)

sayings = []
for i in range(n):
    sayings.append(input().strip())

for i in range(k):
    count = 0
    line = ""
    test = input().strip()
    for saying in sayings:
        if (saying.find(test) == 0):
            line = saying
            count += 1
    if (count == 0):
        print("No chapel sayings.")
    elif (count == 1):
        print(line)
    else:
        print("Multiple chapel sayings.")
