import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
n = iread()
s1 = read()
s2 = read()
lb = {}
rb = {}
for c in 'abcdefghijklmnopqrstuvwxyz?':
    lb[c] = []
    rb[c] = []
for i in range(n): 
    lb[s1[i]].append(i + 1)
    rb[s2[i]].append(i + 1)
pairs = []
for c in 'abcdefghijklmnopqrstuvwxyz':
    if len(lb[c]) >= len(rb[c]):
        for i in range(len(rb[c])):
            pairs.append([lb[c][i], rb[c][i]])
        lb[c] = lb[c][len(rb[c]):]
        rb[c] = []
    elif len(lb[c]) < len(rb[c]):
        for i in range(len(lb[c])):
            pairs.append([lb[c][i], rb[c][i]])
        rb[c] = rb[c][len(lb[c]):]
        lb[c] = []
    if type(rb[c]) is int:
        rb[c] = [rb[c]]
    if type(lb[c]) is int:
        lb[c] = [lb[c]]
for c in 'abcdefghijklmnopqrstuvwxyz?':
    if len(lb[c]) >= len(rb['?']):
        for i in range(len(rb['?'])):
            pairs.append([lb[c][i], rb['?'][i]])
        lb[c] = lb[c][len(rb['?']):]
        rb['?'] = []
    elif len(lb[c]) < len(rb['?']):
        for i in range(len(lb[c])):
            pairs.append([lb[c][i], rb['?'][i]])
        rb['?'] = rb['?'][len(lb[c]):]
        lb[c] = []
    if type(rb['?']) is int:
        rb['?'] = [rb['?']]
    if type(lb[c]) is int:
        lb[c] = [lb[c]]
for c in 'abcdefghijklmnopqrstuvwxyz?':
    if len(lb['?']) >= len(rb[c]):
        for i in range(len(rb[c])):
            pairs.append([lb['?'][i], rb[c][i]])
        lb['?'] = lb['?'][len(rb[c]):]
        rb[c] = []
    elif len(lb['?']) < len(rb[c]):
        for i in range(len(lb['?'])):
            pairs.append([lb['?'][i], rb[c][i]])
        rb[c] = rb[c][len(lb['?']):]
        lb['?'] = []
    if type(rb[c]) is int:
        rb[c] = [rb[c]]
    if type(lb['?']) is int:
        lb['?'] = [lb['?']]
print(len(pairs))
for p in pairs:
    print("{} {}".format(p[0], p[1]))