best = 0
_list = []
total = 0

def get_best(a, b, c):
    global best, _list, total
    print(a, b, c)
    if total + 200 < a:
        return
    if b >= len(_list):
        if total >= a or (a > 2000 and total + 200 >= a):
            best = max(best, c)
        return    
    get_best(a, b + 1, c)
    get_best(a + _list[b][0], b + 1, c + _list[b][1])

while True:
    try:
        best = 0
        _list = []
        total, n = [int(x) for x in input().strip().split()]
        for i in range(n):
            _list.append([int(x) for x in input().strip().split()])
        get_best(0, 0, 0)
        print(best)
    except EOFError:
        break
