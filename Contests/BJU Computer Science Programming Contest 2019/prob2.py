import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
words = []
for i in range(iread()):
    words.append(read())
words.sort()


for i in range(iread()):
    word = read()
    poss = 0
    last_word = ""
    if (word in words):
        print("okay")
        continue
    else:
        for j in range(len(word) - 1):
            new_word = list(word)
            new_word[j], new_word[j + 1] = word[j + 1], word[j]
            new_word = "".join(new_word)
            if (new_word in words):
                last_word = new_word
                poss += 1

    if (poss == 1):
        print(last_word)
    elif (poss > 1):
        print("{} possibilities".format(poss))
    else:
        print("unknown")
