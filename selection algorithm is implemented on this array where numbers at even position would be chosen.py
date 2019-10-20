n = int(input())
l = [int(x) for x in input().split()]
d = {}
for i in range(n):
    d[l[i]] = i
while True:
    a = []
    for i in range(len(l)):
        if (i+1) % 2 == 0:
            a.append(l[i])
    l = a
    if len(l) == 1:
        ans = d[l[0]]
        break
print(ans)
