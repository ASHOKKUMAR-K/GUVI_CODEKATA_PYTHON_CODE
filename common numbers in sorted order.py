n, m = map(int, input().split())
l = [int(x) for x in input().split()]
a = []
b = []
for i in range(len(l)):
    if i<n:
        a.append(l[i])
    else:
        b.append(l[i])
c = []
for i in a:
    if i in b:
        c.append(i)
c.sort()
print(*c)
