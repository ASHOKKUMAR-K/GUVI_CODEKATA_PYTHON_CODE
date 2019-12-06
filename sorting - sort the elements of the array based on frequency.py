n = int(input())
l = [int(x) for x in input().split()]
l.sort()
maxfreq = l.count(l[0])
for i in l:
    if maxfreq < l.count(i):
        maxfreq = l.count(i)
#print(maxfreq)
a = []
for i in range(maxfreq+1):
    for j in l:
        if l.count(j) == i:
            a.append(j)
print(*a)
