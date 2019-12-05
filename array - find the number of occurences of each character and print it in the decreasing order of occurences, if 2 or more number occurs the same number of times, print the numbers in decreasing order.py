n = int(input())
l = [int(x) for x in input().split()]
max_count = l.count(l[0])
for i in range(n):
    if max_count < l.count(l[i]):
        max_count = l.count(l[i])
a = []
for i in range(max_count, 0, -1):
    b = []
    for j in range(n):
        if i == l.count(l[j]) and l[j] not in b:
            b.append(l[j])
    b.sort(reverse = True)
    a.extend(b)
print(*a)
