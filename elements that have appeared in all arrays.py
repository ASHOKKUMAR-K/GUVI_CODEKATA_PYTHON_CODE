(n, k) = map(int, input().split())
l = []
for i in range(n):
    l.append([int(x) for x in input().split()])
b = []
for i in l[0]:
    flag = True
    for j in range(n):
        if i not in l[j]:
            flag = False
    if flag:
        b.append(i)
print(*b)
