n = int(input())
l = [int(x) for x in input().split()]
a = []
for i in range(n):
    count = 0
    for j in range(i, n):
        count+=l[j]
    a.append(count)
print(*a)
