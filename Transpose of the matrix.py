(m, n)= map(int, input().split())
l = []
for i in range(m):
    a=[int(x) for x in input().split()]
    l.append(a)
for i in range(n):
    a = []
    for j in range(m):
        a.append(l[j][i])
    print(*a)
