import re, math, decimal, bisect
def read(): return input().strip()
def iread(): return int(input().strip())
def viread(): return [int(_) for _ in input().strip().split()]
def round(n): return int(n + 0.5)
    
# code goes here

def reverse_sublist(lst,start,end):
    lst[start:end] = lst[start:end][::-1]
    return lst

def kthPermutation(int n, int k){
	nums = [i for i in range(n)]
	factorial = [1]
    for i in range(n):
        factorial.append((i + 1) * factorial[-1])
	
	
	if (k <= 1):
		return nums

	if (k >= factorial[n]):
		nums = reverse_sublist(nums, 0, n-1)
		return nums
	
	k -= 1 
	for i in range(n - 1):
		int fact = factorial[n-i-1];
		index = k / fact
		nums = shiftRight(nums, i, i+index)
		k = k - fact*index
	
	return nums

private static void shiftRight(a, s, e){
	temp = a[e];
	for i = e; i > s; i--){
		a[i] = a[i-1];
	}
	a[s] = temp;
}

for i in range(iread()):
    b, x = viread()
    p = 1
    while x > b ** p:
        x -= b ** p
        p += 1
    idx = x % p
    nth = x // p
    print(p, idx, nth)