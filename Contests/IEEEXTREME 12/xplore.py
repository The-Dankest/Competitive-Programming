import json

def find_h(cites):
    h = 0
    while (h < len(cites) and cites[h] > h):    
        h += 1
    return h

authors = {}
answer = []

for i in range(int(input())):
    line = input()
    j = json.loads(line)
    auths = []
    cites = []
    for a in (j["authors"]["authors"]):
        auths += [a["full_name"]]
    cites = j["citing_paper_count"]
    for auth in auths:
        if auth not in authors.keys():
            authors[auth] = [int(cites)]
        else:
            authors[auth] += [int(cites)]

for key in sorted(authors.keys()):
    answer += [[find_h(sorted(authors[key])[::-1]), key]]

for val in sorted([(-x, y) for x, y in answer]):
    print(val[1], -val[0])