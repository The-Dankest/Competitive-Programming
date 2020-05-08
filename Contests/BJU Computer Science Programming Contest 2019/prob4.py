import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
for t in range(iread()):
    docs = {}
    for i in range(iread()):
        word, _id, index = read().split()
        _id = int(_id)
        index = int(index)
        if _id not in docs.keys():
            docs[_id] = []
        docs[_id].append([index, word])
    for i in sorted(docs.keys()):
        words = docs[i]
        for word in sorted(words):
            print("{} ".format(word[1]), end="")
        print("")
