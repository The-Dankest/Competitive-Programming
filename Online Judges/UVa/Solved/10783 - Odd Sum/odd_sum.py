for i in range(int(input())):
  a = int(input())
  b = int(input())
  if (a % 2 == 0):
    a += 1
  sum = 0
  for j in range(a, b + 1, 2):
    sum += j
  print("Case {}: {}".format(i + 1, sum))
