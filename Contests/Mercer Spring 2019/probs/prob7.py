# BJU Bitwise Blitz 
# prob7.py

from math import factorial as fact
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]

# code goes here
for i in range(iread()): 
    n, k = viread()
    counts = []
    count = 0
    o = []
    string = read()
    for j in range(len(string)):
        if string[j] == "L":
            count += 1
        elif string[j] == "O":
            o.append(j) 
        counts.append(count)
    total = 0
    for index in o:
        if (counts[index] >= k and counts[-1] - counts[index] >= k):
            l_before = counts[index]
            l_after = counts[-1] - counts [index]
            total +- ((fact(l_before) // (fact(l_before - k) * fact(k))) * (fact (l_after) // (fact(l_after	k) * fact(k))))
    print (total % 10007)
