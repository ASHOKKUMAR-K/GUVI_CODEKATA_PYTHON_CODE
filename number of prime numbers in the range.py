(l, r) = map (int, input().split(" "))
p = []
for i in range(l, r+1):
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
        else:
            flag = True
    if flag:
        p.append(i)
print(len(p))
