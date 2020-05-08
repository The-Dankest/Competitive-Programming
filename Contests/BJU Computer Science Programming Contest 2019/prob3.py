import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here

for i in range(iread()):
    people = []
    for j in range(iread()):
        name = read()
        line = read().split()
        # calculate score
        score = 0
        last_throw = 0
        last_last_throw = 0
        moves = list("".join(line))
        for k in range(len(moves) - 1, -1, -1):
            move = moves[k]
            if move == "X":
                move = 10
                score += last_last_throw
                score += last_throw
            elif move == "/":
                move = 10 - int(moves[k - 1] if moves[k - 1] != "-" else 0)
                score += last_throw
            elif move == "-":
                move = 0
            else:
                move = int(move)
            score += move
            last_last_throw = last_throw
            last_throw = move
        people.append([score, name])

    people.sort()
    max_score = people[-1][0]
    names = [people[-1][1]]
    j = len(people) - 2
    while (max_score == people[j][0] and j >= 0):
        if people[j][0] == max_score:
            names.append(people[j][1])
        j -= 1
    
    if len(names) == 1:
        print("{} wins with {} points!".format(names[0], max_score))
    else:
        print("{} tie with {} points!".format(", ".join(sorted(names)), max_score))
