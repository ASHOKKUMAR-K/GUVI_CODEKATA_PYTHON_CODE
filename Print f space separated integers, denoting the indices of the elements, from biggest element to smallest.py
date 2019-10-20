n = int(input())
l = [int(x) for x in input().split()]
d = {}
a = []
for i in range(n):
    d[l[i]] = i
    a.append(l[i])
a.sort(reverse = True)
l = []
for i in a:
    l.append(d[i])
print(*l)
