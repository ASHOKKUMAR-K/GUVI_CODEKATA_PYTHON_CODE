(n , k) = map(int, input().split())
l = [int(x) for x in input().split()]
lst = []
for i in range(n):
    for j in range(i, n):
        a = []
        for k in range(i, j+1):
            a.append(l[k])
        lst.append(a)
count = 0
for i in lst:
    if max(i) > k:
        count += 1
print(count)
