(l, r) = map(int, input().split())
a = []
for i in range(l, r): a.append(i)
for i in range(len(a)):
    z = a[i]
    sm = 0
    while z > 0:
        sm += (z%10)
        z //= 10
    a[i] = sm
count = 0
for i in a:
    flag = True
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
    if i == 1: flag = False
    if flag:
        count += 1
        #print(i)
print(count)
