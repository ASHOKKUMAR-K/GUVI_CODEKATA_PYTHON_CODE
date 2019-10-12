n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
d = {}
l = []
for i in range(n):
    d[b[i]] = a[i]
    l.append(b[i])
l.sort()
a = []
for i in l:
    a.append(d[i])
print(*a)
