(p, q, r) = map(int, input().split())
l = []
for i in range(3):
    l.append([int(x) for x in input().split()])
a = set(l[0])
b = set(l[1])
c = set(l[2])
cond = a.issuperset(b) or a.issuperset(c) or b.issuperset(a) or b.issuperset(c) or c.issuperset(a) or c.issuperset(b)
if cond:print("YES")
else:print("NO")
