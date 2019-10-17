n = int(input())
l = [int(x) for x in input().split()]
k = int(input())
a = []
for i in l:
    if i % k == 0:
        a.append(1)
    else:
        a.append(0)
print(*a)
