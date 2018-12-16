for i in range(int(input())):
    j = 0
    word = [c for c in input().strip()]
    while (j < len(word) - 1):
        if word[j] == "A" and word[j + 1] != "A":
            word[j], word[j + 1] = word[j + 1], word[j]
            j += 1
        j += 1
    print("".join(word))