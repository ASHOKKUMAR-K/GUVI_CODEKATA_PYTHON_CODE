n = int(input())
patn = []
z = n
for i in range(n):
    a = []
    for j in range(n, 0, -1):
        if j > z: a.append(z)
        else: a.append(j)
    for k in range(2, n+1):
        if k > z: a.append(z)
        else: a.append(k)
    z -= 1
    patn.append(a)
for i in range(n -2, -1, -1): patn.append(patn[i])
for i in patn: print(*i)
