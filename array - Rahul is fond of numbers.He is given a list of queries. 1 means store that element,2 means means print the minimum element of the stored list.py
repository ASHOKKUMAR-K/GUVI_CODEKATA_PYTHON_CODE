q = int(input())
l = []
b = []
for _ in range(q):
    a = [int(x) for x in input().split()]
    if a[0] == 1: l.append(a[1])
    if a[0] == 2:
        if len(l) == 0: b.append(-1)
        else: b.append(min(l))
print(*b)
