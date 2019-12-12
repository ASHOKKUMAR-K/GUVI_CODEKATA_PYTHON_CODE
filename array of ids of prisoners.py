n = int(input())
l = [int(x) for x in input().split()]
flag = True
a = []
ans = []
for i in range(n):
    if l[i] not in a:
        a.append(l[i])
    else:
        flag = False
        ans.append(l[i])
if flag: print("-1")
else: print(*ans)
