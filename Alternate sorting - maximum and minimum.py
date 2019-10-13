n = int(input())
l = [int(x) for x in input().split()]
a = []
for i in range(n):
    if i % 2 == 0:
        a.append(max(l))
        l.remove(max(l))
    else:
        a.append(min(l))
        l.remove(min(l))
print(*a)
