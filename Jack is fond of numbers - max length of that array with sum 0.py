n = int(input())
l = [int(x) for x in input().split()]
lst = []
for i in range(n):
    for j in range(i, n):
        a = []
        for k in range(i, j+1):
            a.append(l[k])
        lst.append(a)
m = len(lst[0])
flag = False
for i in lst:
    if sum(i) == 0 and m < len(i):
        m = len(i)
        flag = True
if flag:print(m)
else:print(-1)
