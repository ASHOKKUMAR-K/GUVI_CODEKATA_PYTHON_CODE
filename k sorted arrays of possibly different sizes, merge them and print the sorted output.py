n = int(input())
l = []
for i in range(n):
    l.extend([int(x) for x in input().split()])
l.sort()
print(*l)
