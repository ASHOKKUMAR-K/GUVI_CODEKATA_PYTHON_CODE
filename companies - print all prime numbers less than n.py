n = int(input())
l = []
for i in range(2,n+1):
    flag = False
    for j in range(2, i):
        if i % j == 0:
            flag = True
            break
    if not flag:
        l.append(i)
print(*l)
