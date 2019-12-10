l = [str(x) for x in input().split()]
a = []
for i in l:
  a.append(i[::-1])
print(*a)
