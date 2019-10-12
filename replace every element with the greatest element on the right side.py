n = int(input())
l = [int(x) for x in input().split()]
b = []
for i in range(n-1):
    a = []
    for j in range(i+1, n):
        a.append(l[j])
    b.append(max(a))
b.append(0)
print(*b)
