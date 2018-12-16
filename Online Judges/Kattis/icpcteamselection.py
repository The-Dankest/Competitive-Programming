for i in range(int(input())):
    n = int(input())
    students = sorted([int(x) for x in input().split()])
    _sum = 0
    for j in range(n, n * 3, 2):
        _sum += students[j]
    print(_sum)
