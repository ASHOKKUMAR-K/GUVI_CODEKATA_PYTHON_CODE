n = int(input())
l = [int(x) for x in input().split()]
k = l.count(l[0])
for i in range(n):
    if k > l.count(l[i]):
        k = l.count(l[i])
a = []
for i in range(n):
    if l.count(l[i]) == k and l[i] not in a:
        a.append(l[i])
a.sort(reverse = True)
print(*a)
