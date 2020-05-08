bs = []

def prime_sieve(n):
    global bs
    bs = [True for i in range(n + 1)]
    bs[0] = False
    bs[1] = False
    p = 2
    while (p * p <= n): 
        if (bs[p] == True):
            for i in range(p * 2, n+1, p): 
                bs[i] = False
        p += 1

#for i in range(int(input())):
#    a,b = [int(x) for x in input().split()]

prime_sieve(1000000000)
