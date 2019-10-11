(n, k) = map(int, input().split())
l = [int(x) for x in input().split()]
a = []
for i in l:
    if l.count(i) < k:
        a.append(i)
a.sort()
print(*a)
