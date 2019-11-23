n = int(input())
l = input().split()
a = []
k = 0
for i in range(n):
    b = []
    for j in range(3):
        b.append(l[k])
        k += 1
    a.append(b)
ans = []
flag = False
for i in range(len(a)):
    if int(a[i][2]) <= 1987:
        if int(a[i][2]) == 1987:
            if a[i][1] in ('JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY'):
                if (a[i][1]) == 'JULY':
                    if int(a[i][0]) <= 22:
                        ans.append(i+1)
                        flag = True
                    else:
                        continue
                else:
                    ans.append(i+1)
                    flag = True
            else:
                continue
        else:
            ans.append(i+1)
            flag = True
    else:
        continue
if flag:print(*ans)
else:print(-1)
