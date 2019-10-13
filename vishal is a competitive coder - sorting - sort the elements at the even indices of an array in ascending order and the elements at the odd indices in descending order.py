n = int(input())
l = [int(x) for x in input().split()]
e = []
o = []
for i in range(n):
    if i % 2 == 0:
        e.append(l[i])
    else:
        o.append(l[i])
e.sort()
o.sort(reverse = True)
p = 0
q = 0
l = []
for i in range(n):
    if i%2==0:
        l.append(e[p])
        p+=1
    else:
        l.append(o[q])
        q+=1
print(*l)
