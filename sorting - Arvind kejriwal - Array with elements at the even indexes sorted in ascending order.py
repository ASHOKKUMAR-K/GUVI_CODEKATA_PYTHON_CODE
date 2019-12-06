n = int(input())
l = [int(x) for x in input().split()]
e = []
for i in range(n):
    if i % 2 == 0: e.append(l[i])
e.sort()
j = 0
ans = []
for i in range(n):
    if i % 2 == 0:
        ans.append(e[j])
        j += 1
    else: ans.append(l[i])
print(*ans)
