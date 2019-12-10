l = [int(x) for x in input().split()]
n = l[0]
l = l[1:]
i = 1
ans = []
while True:
    if i % 2 == 1:
        ans.append(max(l))
        l.remove(max(l))
    else:
        ans.append(min(l))
        l.remove(min(l))
    if i == n: break
    else: i += 1
print(*ans)
