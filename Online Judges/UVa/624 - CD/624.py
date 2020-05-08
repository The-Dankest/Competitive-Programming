tracks = []
best = (0, 0)
cap = 0

def do_cd(idx, space, used):
    global tracks, best, cap
    if space < 0 or best[1] == cap:
        return
    if space == 0:
        best = (cap, used)
        return
    if idx >= 0: #len(tracks):
        do_cd(idx - 1, space - tracks[idx], used | (1 << idx))
        do_cd(idx - 1, space, used)
    else:
        if cap - space > best[0]:
            best = (cap - space, used)
        return

def bin_to_list(x):
    binary = bin(x)[:1:-1]
    l = []
    for i in range(len(binary)):
        if binary[i] == "1":
            l.append(str(tracks[i])) 
    return l

while (True):
    try:
        _input = [int(x) for x in input().strip().split()]
        cap = _input[0]
        best = (0, 0)
        tracks = _input[2:]
        do_cd(len(tracks), cap, 0)
        print("{0} sum:{1}".format(" ".join(bin_to_list(best[1])), best[0]))
    except EOFError:
        break