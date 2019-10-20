n = int(input())
l = [int(x) for x in input().split()]
lst = []
for i in range(n):
    for j in range(i, n):
        a = []
        for k in range(i, j+1):
            a.append(l[k])
        lst.append(a)
m = sum(lst[0])
for i in range(1, len(lst)):
    if m > sum(lst[i]):
        m = sum(lst[i])
print(m)
