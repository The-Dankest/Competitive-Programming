scores = {}
_in = input().strip()
while (_in != "-1"):
    t, p, v = _in.split()
    t = int(t)
    if (p not in scores.keys()):
        scores[p] = [0, 0]
    if (v == "wrong"):
        scores[p][1] += 1
    else:
        scores[p][0] = t     
    _in = input().strip()

total = 0
count = 0
for k in scores.keys():
    score = scores[k]
    if (score[0] != 0):
        count += 1
        total += score[0] + (score[1] * 20)

print(count, total)