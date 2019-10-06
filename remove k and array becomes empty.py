(n, k) = map(int, input().split())
l = [int(x) for x in input().split()]
l1 = []
for i in l:
    if i != k:
        l1.append(i)
if len(l1) != 0:
    print(*l1)
else:
    print("empty")
