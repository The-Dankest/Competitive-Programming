#n, s = [int(x) for x in input().split()]
print(int(__import__("math").ceil(eval(" / ".join(input().split()[::-1])))))