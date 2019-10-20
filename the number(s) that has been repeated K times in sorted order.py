n, k = map(int, input().split())
l = [int(x) for x in input().split()]
a = []
flag = False
for i in l:
    if l.count(i)==k and i not in a:
        flag = True
        a.append(i)
if flag:
    a.sort()
    print(*a)
else: print(-1)
