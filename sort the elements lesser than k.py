(n, k) = map(int, input().split())
l = [int(x) for x in input().split()]
flag = True
a = []
for i in l:
    if i < k:
        flag = False
        a.append(i)
a.sort()
if flag:
    print(-1)
else:
    print(*a)
