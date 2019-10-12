n, d = map(int, input().split())
l = [int(x) for x in input().split()]
for i in range(d):
    l.append(l.pop(0))
print(*l)
