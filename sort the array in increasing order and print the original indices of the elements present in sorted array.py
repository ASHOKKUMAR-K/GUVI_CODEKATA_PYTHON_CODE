n = int(input())
l = [int(x) for x in input().split()]
d = {}
for i in range(len(l)):
    d[l[i]]=i+1
l.sort()
a = []
for i in l:
    a.append(d[i])
print(*a)
