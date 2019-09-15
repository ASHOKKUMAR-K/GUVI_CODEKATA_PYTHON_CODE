(n, q) = map(int, input().split())
l = [int(x) for x in input().split()]
a = []
b = []
for i in range(q):
    (m, n) = map(int, input().split())
    a.append(m)
    b.append(n)
for i in range(q):
    min = l[a[i]-1]
    for j in range(a[i]-1, b[i]):
        if min > l[j]:
            min = l[j]
    print(min)
