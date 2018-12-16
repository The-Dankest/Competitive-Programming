import sys
col = ['a','b','c','d','e','f','g','h']
blacks = []
whites = []
grid = [input() for i in range(17)]
for y in range(8):
    for x in range(8):
        piece = grid[(y * 2) + 1][(x * 4) + 2]
        if (piece.isalpha()):
            if (piece.isupper()):
                whites.append([col[x], y, piece])
            else:
                blacks.append([col[x], y, piece.upper()])
print("White: {}".format(",".join(["{}{}{}".format(p[2],p[0],p[1]) for p in whites])))
print("Black: {}".format(",".join(["{}{}{}".format(p[2],p[0],p[1]) for p in blacks])))