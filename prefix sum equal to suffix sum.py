n = int(input())
l = [int(x) for x in input().split()]
flag = False
for i in range(1,n-1):
    pre = 0
    for j in range(i):
        pre += l[j]
    suf = 0
    for j in range(i+1, n):
        suf += l[j]
    if pre == suf:
        flag = True
        break
if flag:
    print("yes")
else:
    print("no")
