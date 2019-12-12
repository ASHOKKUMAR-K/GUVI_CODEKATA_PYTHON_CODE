n = int(input())
l = [int(x) for x in input().split()]
ans = []
for i in range(len(l)):
    if len(l) % 2 == 1:
        ans.append(l.pop(len(l)//2))
    else:
        ans.append(l.pop(len(l)//2 - 1))
print(*ans)
