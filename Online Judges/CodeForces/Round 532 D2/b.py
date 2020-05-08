diff, prob = [int(x) for x in input().split()]
probs = [int(x) for x in input().split()]

counts = {}
comp = {}
num = 0
for i in range(diff):
    counts[i + 1] = 0
    comp[i + 1] = False

for p in probs:
    counts[p] += 1
    if comp[p] == False:
        num += 1
        comp[p] = True
        if (num == diff):
            num = 0
            for i in range(diff):
                counts[i + 1] -= 1
                if counts[i + 1] == 0:
                    comp[i + 1] = False
                else:
                    num += 1
            print("1", end="")
        else:
            print("0", end="")
    else:
        print("0", end="")
print("")
