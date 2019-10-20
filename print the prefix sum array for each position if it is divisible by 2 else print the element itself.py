n = int(input())
l = [int(x) for x in input().split()]
a = []
for i in range(n):
    count = 0
    for j in range(i+1):
        count+=l[j]
    if count%2==0:
        a.append(count)
    else:
        a.append(l[i])
print(*a)
