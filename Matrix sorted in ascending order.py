(r, c) = map(int, input().split())
a = []
for i in range(r):
     l = [int(x) for x in input().split()]
     a.extend(l)
a.sort()
i = 0
for j in range(r):
    b = []
    for k in range(c):
        b.append(a[i])
        i += 1
    print(*b)
