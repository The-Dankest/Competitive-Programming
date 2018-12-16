import re
import math
import decimal
import bisect

def read():
    return input().strip()

def iread():
    return int(input().strip())

def viread():
    return list(map(int, input().strip().split()))

infix = ""
prefix = ""
strtree = []
depth = 0
maxdepth = 0

def buildtree(tree, root):
    global depth, maxdepth
    depth += 1
    maxdepth = max(maxdepth, depth)
    if len(tree) == 1:
        depth -= 1
        return [root]

    ret = [root]
    left, right = tree.split(root)
    if left != "":
        lroot = 30
        for c in left:
            lroot = min(lroot, prefix.find(c))
        ret.append(buildtree(left, left[left.find(prefix[lroot])]))
    else:
        ret.append([""])
    if right != "":
        rroot = 30
        for c in right:
            rroot = min(rroot, prefix.find(c))
        ret.append(buildtree(right, right[right.find(prefix[rroot])]))
    else:
        ret.append([""])
    depth -= 1
    return ret

def printtree(tree, depth):

# code goes here
try:
    while True:
        infix = read()
        prefix = read()
        tree = buildtree(infix, prefix[0])
        print(tree)
        strtree = [" "*len(infix)]*maxdepth
        printtree(tree, 0)
        print(*strtree, sep="\n")

        
except EOFError:
    pass
