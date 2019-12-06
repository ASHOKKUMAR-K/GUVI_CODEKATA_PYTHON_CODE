n, m = map(int, input().split())
l = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
f = []
for i in a:
    for j in range(l.count(i)):
        f.append(i)
g = []
for i in l:
    if i not in a:
        g.append(i)
g.sort()
f.extend(g)
print(*f)
