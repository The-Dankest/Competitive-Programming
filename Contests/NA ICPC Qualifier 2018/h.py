mode, phrase = input().split()
if (mode == 'E'):
    # encode
    new = [phrase[0], 1]
    for i in range(len(phrase) - 1):
        if (phrase[i + 1] == new[-2]):
            new[-1] += 1
        else:
            new.append(phrase[i + 1])
            new.append(1)
    for x in new:
        print(x, end="")
    print()
else:
    # decode
    new = ""
    for i in range(len(phrase) // 2):
        new += phrase[i * 2] * int(phrase[(i * 2) + 1])
    print(new)
