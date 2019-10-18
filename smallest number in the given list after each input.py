n = int(input())
l = [int(x) for x in input().split()]
a = []
b = []
for i in range(n):
  for j in range(i+1):
    a.append(l[j])
  b.append(min(a))
print(*b)
