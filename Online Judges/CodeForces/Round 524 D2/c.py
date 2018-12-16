from math import floor, ceil
for i in range(int(input())):
    n, m = [int(x) for x in input().split()]
    whites = ceil((n * m) / 2)
    blacks = floor((n * m) / 2)
    white = [int(x) for x in input().split()]
    white[0] -= 1
    white[1] -= 1
    black = [int(x) for x in input().split()]
    black[0] -= 1
    black[1] -=1
    if (white[1] % 2 == white[0] % 2):
        changed_whites = ceil(((white[2] - white[0]) * (white[3] - white[1])) / 2)
    else:
        changed_whites = floor(((white[2] - white[0]) * (white[3] - white[1])) / 2)
    whites += changed_whites
    blacks -= changed_whites
    if (white[1] % 2 == white[0] % 2):
        changed_blacks = floor(((black[2] - black[0]) * (black[3] - black[1])) / 2)
    else:
        changed_blacks = ceil(((black[2] - black[0]) * (black[3] - black[1])) / 2) 
    new_rect = [max(white[0], black[0]), max(white[1], black[1]), min(white[2], black[2]), min(white[3], black[3])]
    if (new_rect[1] % 2 != new_rect[0] % 2):
        changed_blacks += floor(((new_rect[2] - new_rect[0]) * (new_rect[3] - new_rect[1])) / 2)
    else:
        changed_blacks += ceil(((new_rect[2] - new_rect[0]) * (new_rect[3] - new_rect[1])) / 2)
    whites -= changed_blacks
    blacks += changed_blacks
    print(whites, blacks)