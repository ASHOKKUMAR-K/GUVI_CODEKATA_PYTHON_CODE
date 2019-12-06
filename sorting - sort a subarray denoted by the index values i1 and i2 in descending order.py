n = int(input())
l = [int(x) for x in input().split()]
(i1, i2) = map(int, input().split())
a = []
for i in range(i1, i2+1):
    a.append(l.pop(i1))
a.sort()
for i in a:
    l.insert(i1, i)
print(*l)
