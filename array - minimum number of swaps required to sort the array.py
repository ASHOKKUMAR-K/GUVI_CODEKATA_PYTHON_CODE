n = int(input())
l = [int(x) for x in input().split()]
a = l[:]
a.sort()
d = {}
for i in range(n): d[a[i]] = i
count = 0
for i in range(n):
    if l[i] == a[i]: continue
    else:
        idx = d[l[i]]
        l[i], l[idx] = l[idx], l[i]
        count += 1
print(count)
