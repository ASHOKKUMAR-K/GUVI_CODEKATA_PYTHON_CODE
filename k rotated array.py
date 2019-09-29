(n, k) = map(int, input().split())
l = [int(x) for x in input().split()]
for i in range(k):
    d = l.pop(0)
    l.append(d)
print(*l)
