n = int(input())
l = [int(x) for x in input().split()]
a = []
for i in range(n):
  for j in range(i+1):
    a.append(l[j])
  print(min(a), end = " ")
