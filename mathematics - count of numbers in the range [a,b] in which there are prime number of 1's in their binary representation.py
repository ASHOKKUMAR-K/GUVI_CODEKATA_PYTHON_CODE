(l, r) = map(int, input().split())
a = []
for i in range(l, r+1): a.append(i)
for i in range(len(a)):
    z = a[i]
    sm = (str(bin(a[i]))[2:]).count("1")
    a[i] = sm
count = 0
#print(*a)
for i in a:
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if i == 1 or i == 0: flag = False
    if flag:count += 1
print(count)
