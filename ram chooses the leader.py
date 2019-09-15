n = int(input())
l = [int(x) for x in input().split()]
a = []
for i in range(n):
    flag = True
    for j in range(i, n):
        if l[i] < l[j]:
            flag = False
            break
    if flag:
        a.append(l[i])
print(*a)
