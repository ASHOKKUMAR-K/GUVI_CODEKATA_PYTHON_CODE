n = int(input())
l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
l = []
flag = True
for i in l1:
    if i in l2 and i not in l:
        l.append(i)
        flag = False
if flag:
    print(-1)
else:
    print(*l)
