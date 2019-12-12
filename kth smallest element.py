(n, k) = map(int, input().split())
l = [int(x) for x in input().split()]
a = []
for i in l:
    if i not in a:
        a.append(i)
a.sort()
if k <= len(a):
    print(a[k-1])
else:
    print(-1)
