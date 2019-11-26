(n, q) = map(int, input().split())
l = [int(x) for x in input().split()]
for _ in range(q):
    (u, v) = map(int, input().split())
    lst = l[u-1 : v]
    xor = lst[0]
    for i in range(1, len(lst)):
        xor ^= lst[i]
    print(xor)
