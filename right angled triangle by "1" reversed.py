n=int(input())
for i in range(0,n):
  a = []
  for j in range(0,n-i):
    a.append(1)
  print(*a)
