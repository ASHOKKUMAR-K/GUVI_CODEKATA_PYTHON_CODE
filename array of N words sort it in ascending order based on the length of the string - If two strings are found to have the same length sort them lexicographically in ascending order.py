n = int(input())
l = input().split()
maxlen = len(l[0])
for i in l:
    if maxlen < len(i):
        maxlen = len(i)
lst = []
for i in range(maxlen+1):
    a = []
    for j in l:
        if len(j) == i:
            a.append(j)
    a.sort()
    lst.extend(a)
print(*lst)
