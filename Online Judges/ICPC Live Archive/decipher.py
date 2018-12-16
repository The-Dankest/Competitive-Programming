while True:
    try:    
        m, n = [int(x) for x in input().strip().split()]
        trans = {'a':[set('a'),set()],
                'b':[set('b'),set()],
                'c':[set('c'),set()],
                'd':[set('d'),set()],
                'e':[set('e'),set()],
                'f':[set('f'),set()],
                'g':[set('g'),set()],
                'h':[set('h'),set()],
                'i':[set('i'),set()],
                'j':[set('j'),set()],
                'k':[set('k'),set()],
                'l':[set('l'),set()],
                'm':[set('m'),set()],
                'n':[set('n'),set()],
                'o':[set('o'),set()],
                'p':[set('p'),set()],
                'q':[set('q'),set()],
                'r':[set('r'),set()],
                's':[set('s'),set()],
                't':[set('t'),set()],
                'u':[set('u'),set()],
                'v':[set('v'),set()],
                'w':[set('w'),set()],
                'x':[set('x'),set()],
                'y':[set('y'),set()],
                'z':[set('z'),set()]}
        for i in range(m):
            a, b = input().strip().split()
            if b not in trans[a]:
                trans[a][0].add(b)
                for c in trans[b][1]:
                    trans[c][1].add(a)
                    trans[c][0].add(b)
                trans[b][1].add(a)
        fixable = []
        for k in trans.keys():
            if len(trans[k][1]) != 0:
                fixable.append(k)
        fixed = []
        while (fixed != fixable):
            for k in fixable:
                
        for k in sorted(fixable):
            print("{}: {}, {}".format(k, trans[k][0], trans[k][1]))
        for i in range(n):
            a, b = input().strip().split()
            out = "yes"
            if len(a) != len(b):
                out = "no"
            for i in range(len(a)):
                if b[i] not in trans[a[i]][0]:
                    out = "no"
            print(out)
    except EOFError:
        break