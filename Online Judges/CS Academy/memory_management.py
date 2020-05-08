for i in range(int(input())):
    p, s, n = [int(x) for x in input().strip().split()]
    fifo = 0
    lru = 0
    
    fifo_q = []
    fifo_s = set()
    
    lru_q = []
    lru_s = set()
    
    for _ in range(n):
        pg = int(input().strip()) // s
        if len(fifo_q) < p and pg not in fifo_s:
            fifo_q.append(pg)
            fifo_s.add(pg)
        elif pg not in fifo_s:
            fifo_s.remove(fifo_q.pop(0))
            fifo_q.append(pg)
            fifo_s.add(pg)
            fifo += 1
        if len(lru_q) < p and pg not in lru_s:
            lru_q.append(pg)
            lru_s.add(pg)
        elif pg not in lru_s:
            lru_s.remove(lru_q.pop(0))
            lru_q.append(pg)
            lru_s.add(pg)
            lru += 1
        else:
            lru_q.append(lru_q.pop(lru_q.index(pg)))
        
    
    
    print("no" if fifo <= lru else "yes", fifo, lru)